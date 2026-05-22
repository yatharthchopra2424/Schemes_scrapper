"""
Pipeline Runner — orchestrates crawl + LLM enrichment for all schemes.

Major upgrade from v1:
  1. ThreadPoolExecutor with per-scheme isolated Chrome drivers (parallel execution)
  2. Thread-safe checkpoint and CSV writes (threading.Lock)
  3. Per-scheme elapsed timing tracked in CSV output
  4. Worker exception isolation (one failure never kills others)
  5. Rich evidence text building: metadata + page text + docs
  6. LLM fallback handled cleanly at worker level
  7. Progress logging via completed count / total count
"""
from __future__ import annotations

import json
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from ..config import AppSettings
from ..crawler.driver import managed_driver
from ..crawler.navigator import crawl_scheme
from ..llm.nvidia_client import NvidiaLLMClient
from ..llm.schema import SchemeInsight
from ..models import SchemeInput
from ..output.writers import (
    read_enriched_csv,
    write_ai_summary_json,
    write_enriched_csv,
    write_evidence_bundle,
    write_markdown,
)
from ..utils import ensure_dir, load_scheme_inputs, slugify

class PipelineRunner:
    """
    Orchestrates the full crawl + LLM enrichment pipeline.

    When parallel_workers > 1, each scheme runs in its own thread with its
    own isolated Chrome session. Checkpoint and CSV writes are mutex-protected.
    """

    def __init__(
        self,
        settings: AppSettings,
        input_csv: Path,
        run_dir: Path,
        resume: bool,
        skip_llm: bool,
        logger: logging.Logger,
    ):
        self.settings = settings
        self.input_csv = input_csv
        self.run_dir = ensure_dir(run_dir)
        self.resume = resume
        self.skip_llm = skip_llm
        self.logger = logger

        self.artifacts_dir = ensure_dir(self.run_dir / "artifacts")
        self.checkpoint_path = self.run_dir / self.settings.output.checkpoint_name
        self.enriched_csv_path = self.run_dir / self.settings.output.enriched_csv_name

        # Thread-safety
        self._lock = threading.Lock()
        self._checkpoint: dict[str, Any] = {}
        self._rows: dict[str, dict[str, Any]] = {}   # key → row dict

    # ── Checkpoint helpers ────────────────────────────────────────────────────

    def _load_checkpoint(self) -> dict[str, Any]:
        if not self.checkpoint_path.exists():
            return {}
        try:
            return json.loads(self.checkpoint_path.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def _save_checkpoint(self) -> None:
        """Must be called under self._lock."""
        self.checkpoint_path.write_text(
            json.dumps(self._checkpoint, indent=2), encoding="utf-8"
        )

    @staticmethod
    def _scheme_key(scheme: SchemeInput) -> str:
        return f"{scheme.row_id}|{scheme.scheme_name}|{scheme.scheme_url}"

    # ── Evidence text builder ─────────────────────────────────────────────────

    @staticmethod
    def _build_evidence_text(
        pages: list[Any],
        docs: list[Any],
        limit: int = 400_000,
    ) -> str:
        """
        Build a plain-text evidence block for the LLM from crawled pages + documents.
        Pages are formatted with clear section separators and URL attribution.
        """
        chunks: list[str] = []

        for page in pages:
            text = (page.text or "").strip()
            if not text:
                continue
            chunks.append(
                f"--- PAGE ---\n"
                f"URL: {page.url}\n"
                f"TITLE: {page.title or 'Untitled'}\n"
                f"TEXT:\n{text[:18_000]}"
            )

        for doc in docs:
            text = (doc.extracted_text or "").strip()
            if not text:
                continue
            chunks.append(
                f"--- DOCUMENT ---\n"
                f"URL: {doc.url}\n"
                f"TEXT:\n{text[:18_000]}"
            )

        combined = "\n\n".join(chunks)
        return combined[:limit]

    # ── Per-scheme worker ─────────────────────────────────────────────────────

    def _process_scheme(
        self,
        scheme: SchemeInput,
        llm_client: NvidiaLLMClient | None,
    ) -> dict[str, Any]:
        """
        Full crawl + LLM enrichment for a single scheme.
        Runs in its own thread (when parallel_workers > 1) with an isolated Chrome driver.
        """
        t_start = time.perf_counter()
        scheme_slug = slugify(scheme.scheme_name)
        scheme_dir = ensure_dir(self.artifacts_dir / f"{scheme.row_id}-{scheme_slug}")

        self.logger.info(">> Starting: %s [%s]", scheme.scheme_name, scheme.row_id)

        try:
            # ──── Crawl ────────────────────────────────────────────────────────
            with managed_driver(self.settings) as driver:
                evidence = crawl_scheme(
                    driver, scheme, self.settings, scheme_dir, self.logger
                )

            pages_crawled = len(evidence.pages)
            docs_found = len(evidence.documents)

            # ──── Build evidence text ──────────────────────────────────────────
            evidence_text = self._build_evidence_text(evidence.pages, evidence.documents)

            self.logger.info(
                "  Crawled %d pages, %d docs, evidence text: %d chars",
                pages_crawled,
                docs_found,
                len(evidence_text),
            )

            # ──── LLM enrichment ───────────────────────────────────────────────
            if llm_client is not None:
                insight, llm_raw = llm_client.analyze_scheme(scheme, evidence_text)
                
                # ──── Agentic Fallback ─────────────────────────────────────────
                if insight.confidence == "low":
                    self.logger.warning("Primary crawl yielded low confidence. Triggering Agentic Fallback.")
                    from ..crawler.agent import run_agentic_fallback
                    
                    # Identify missing critical fields
                    missing = [
                        f for f in ["application_process", "eligibility", "financial_support", "benefits"]
                        if not getattr(insight, f)
                    ]
                    
                    interactive_evidence = run_agentic_fallback(
                        driver=driver,
                        scheme=scheme,
                        missing_fields=missing,
                        llm_client=llm_client
                    )
                    
                    if interactive_evidence.strip():
                        self.logger.info("Agent extracted additional evidence. Re-running LLM analysis.")
                        combined_evidence = evidence_text + "\n\n" + interactive_evidence
                        insight, llm_raw = llm_client.analyze_scheme(scheme, combined_evidence)
            else:
                insight = SchemeInsight.empty("LLM step skipped (--skip-llm or no API key).")
                llm_raw = ""

            # ──── Write artifacts ──────────────────────────────────────────────
            evidence_json = scheme_dir / "evidence_bundle.json"
            report_md = scheme_dir / "report.md"
            ai_summary_json = scheme_dir / "ai_summary.json"

            write_evidence_bundle(evidence_json, scheme, evidence, insight, llm_raw)
            write_ai_summary_json(ai_summary_json, scheme, insight)

            elapsed = time.perf_counter() - t_start
            self.logger.info(
                "[DONE] Completed: %s | confidence=%s | %.1fs",
                scheme.scheme_name,
                insight.confidence,
                elapsed,
            )

            return {
                "row_id": scheme.row_id,
                "ministry_or_category": scheme.ministry_or_category,
                "scheme_name": scheme.scheme_name,
                "scheme_url": scheme.scheme_url,
                "status": "completed",
                "pages_crawled": pages_crawled,
                "documents_found": docs_found,
                "elapsed_seconds": round(elapsed, 1),
                "overview": insight.overview,
                "scheme_type": insight.scheme_type,
                "target_beneficiaries": insight.target_beneficiaries,
                "geographic_scope": insight.geographic_scope,
                "eligibility": insight.eligibility,
                "benefits": insight.benefits,
                "financial_support": insight.financial_support,
                "fund_size_crores": insight.fund_size_crores,
                "grant_amount_per_entity": insight.grant_amount_per_entity,
                "application_process": insight.application_process,
                "application_portal_url": insight.application_portal_url,
                "deadlines": insight.deadlines,
                "implementing_agency": insight.implementing_agency,
                "contact_details": insight.contact_details,
                "confidence": insight.confidence,
                "last_updated_date": insight.last_updated_date,
                "evidence_json_path": str(evidence_json),
                "report_markdown_path": str(report_md),
                "pitch_md_path": str(scheme_dir / "pitch.md"),
                "howto_md_path": str(scheme_dir / "how_to_apply.md"),
                "summary_md_path": str(scheme_dir / "summary.md"),
                "error": "",
            }

        except Exception as exc:
            elapsed = time.perf_counter() - t_start
            self.logger.error(
                "[FAIL] Failed: %s | %.1fs | %s", scheme.scheme_name, elapsed, exc, exc_info=True
            )
            insight = SchemeInsight.empty(str(exc))
            return {
                "row_id": scheme.row_id,
                "ministry_or_category": scheme.ministry_or_category,
                "scheme_name": scheme.scheme_name,
                "scheme_url": scheme.scheme_url,
                "status": "failed",
                "pages_crawled": 0,
                "documents_found": 0,
                "elapsed_seconds": round(elapsed, 1),
                "overview": insight.overview,
                "scheme_type": "",
                "target_beneficiaries": [],
                "geographic_scope": "",
                "eligibility": "",
                "benefits": "",
                "financial_support": "",
                "fund_size_crores": "",
                "grant_amount_per_entity": "",
                "application_process": "",
                "application_portal_url": "",
                "deadlines": "",
                "implementing_agency": "",
                "contact_details": "",
                "confidence": "low",
                "last_updated_date": "",
                "evidence_json_path": "",
                "report_markdown_path": "",
                "pitch_md_path": "",
                "howto_md_path": "",
                "summary_md_path": "",
                "error": str(exc)[:500],
            }

    # ── Main orchestrator ─────────────────────────────────────────────────────

    def run(self, max_schemes: int | None = None) -> Path:
        """
        Run the full pipeline: crawl + LLM enrichment for all schemes.
        Supports parallel execution via ThreadPoolExecutor.

        Returns the path to the enriched CSV.
        """
        schemes = load_scheme_inputs(self.input_csv)
        if max_schemes is not None:
            schemes = schemes[:max_schemes]

        # Load existing checkpoint / CSV if resuming
        if self.resume:
            self._checkpoint = self._load_checkpoint()
            self._rows = {
                f"{r.get('row_id')}|{r.get('scheme_name')}|{r.get('scheme_url')}": r
                for r in read_enriched_csv(self.enriched_csv_path)
            }
            self.logger.info("Resume mode: checkpoint has %d completed entries", len(self._checkpoint))
        else:
            self._checkpoint = {}
            self._rows = {}

        # Filter out already-completed schemes
        pending: list[SchemeInput] = []
        for scheme in schemes:
            key = self._scheme_key(scheme)
            if self.resume and self._checkpoint.get(key, {}).get("status") == "completed":
                self.logger.info("↷ Skipping (already done): %s", scheme.scheme_name)
            else:
                pending.append(scheme)

        self.logger.info(
            "Pipeline start: %d total, %d pending, %d workers",
            len(schemes),
            len(pending),
            self.settings.runtime.parallel_workers,
        )

        # Initialise LLM client once (thread-safe — openai client is thread-safe)
        llm_client: NvidiaLLMClient | None = None
        if not self.skip_llm:
            try:
                llm_client = NvidiaLLMClient(self.settings)
            except Exception as exc:
                self.logger.warning("LLM init failed (%s). Running crawl-only.", exc)

        completed = 0
        total = len(pending)
        workers = self.settings.runtime.parallel_workers

        if workers <= 1:
            # Sequential mode: single driver lifecycle
            for scheme in pending:
                row = self._process_scheme(scheme, llm_client)
                self._persist(scheme, row)
                completed += 1
                self.logger.info("Progress: %d/%d", completed, total)
        else:
            # Parallel mode: each worker spawns its own Chrome driver
            with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="scheme-worker") as pool:
                future_to_scheme = {
                    pool.submit(self._process_scheme, scheme, llm_client): scheme
                    for scheme in pending
                }
                for future in as_completed(future_to_scheme):
                    scheme = future_to_scheme[future]
                    try:
                        row = future.result()
                    except Exception as exc:
                        self.logger.error(
                            "Unhandled worker error for %s: %s", scheme.scheme_name, exc
                        )
                        row = {
                            "row_id": scheme.row_id,
                            "scheme_name": scheme.scheme_name,
                            "scheme_url": scheme.scheme_url,
                            "ministry_or_category": scheme.ministry_or_category,
                            "status": "failed",
                            "error": str(exc)[:500],
                        }
                    self._persist(scheme, row)
                    completed += 1
                    self.logger.info(
                        "Progress: %d/%d (%s)",
                        completed,
                        total,
                        row.get("status", "?"),
                    )

        return self.enriched_csv_path

    def _persist(self, scheme: SchemeInput, row: dict[str, Any]) -> None:
        """Thread-safe checkpoint + CSV update."""
        key = self._scheme_key(scheme)
        status = row.get("status", "failed")
        with self._lock:
            self._checkpoint[key] = {
                "status": status,
                "error": row.get("error", ""),
            }
            self._rows[key] = row
            self._save_checkpoint()
            write_enriched_csv(self.enriched_csv_path, list(self._rows.values()))
