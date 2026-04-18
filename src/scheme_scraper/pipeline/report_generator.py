"""
Report Generator v2 — produces 8 structured business documents per scheme artifact.
────────────────────────────────────────────────────────────────────────────────────
Output files (per scheme directory):
  FILE 1:  SCHEME_MASTER_DATABASE.md    — full scheme entry, AI brain for client qualification
  FILE 2:  PITCH_AND_SALES_SCRIPTS.md  — discovery call + objection handlers
  FILE 3:  APPLICATION_PLAYBOOK.md     — 5-stage operational execution guide
  FILE 4:  CLIENT_ONBOARDING_AND_CRM.md — intake form + CRM pipeline
  FILE 5:  LIVE_CASE_TRACKER.md        — active case tracker with scheme-specific fields
  FILE 6:  FEE_AND_REVENUE_MODEL.md    — pricing tiers + revenue projections
  FILE 7:  CLIENT_PROPOSAL_TEMPLATE.md — ready-to-send client proposal
  FILE 8:  COMPLIANCE_AND_LEGAL_PACK.md — NDAs, disclaimers, data policy

Architecture:
  1. EvidenceSynthesizer runs FIRST for each scheme — merges crawled page text,
     downloaded PDF text, and structured ai_summary.json into a SynthesizedEvidence object.
  2. The key_facts block (compact structured summary from ai_summary.json) is injected at
     the TOP of every prompt, giving the LLM precise facts before it reads raw evidence.
  3. Each of the 8 files is generated with a separate LLM call for isolation and quality.
  4. Idempotency: existing files > 100 bytes are skipped (safe to re-run).

Changes from v1:
  - Replaces 3-file generic generation with 8-file business document generation
  - Uses EvidenceSynthesizer (merges pages + PDFs + ai_summary.json)
  - Uses BUSINESS_DOCS_SYSTEM_PROMPT for all 8 files
  - Separate functools.partial per file (lambda capture bug fix preserved)
  - Per-file timing logs
  - Old files (pitch.md, how_to_apply.md, summary.md, report.md) are preserved
"""
from __future__ import annotations

import functools
import logging
import time
from pathlib import Path
from typing import Callable

from ..config import AppSettings
from ..llm.nvidia_client import NvidiaLLMClient
from ..llm.prompts import (
    BUSINESS_DOCS_SYSTEM_PROMPT,
    build_scheme_master_db_prompt,
    build_pitch_scripts_prompt,
    build_application_playbook_prompt,
    build_client_onboarding_prompt,
    build_case_tracker_prompt,
    build_fee_model_prompt,
    build_client_proposal_prompt,
    build_compliance_pack_prompt,
)
from .evidence_synthesizer import synthesize, SynthesizedEvidence

logger = logging.getLogger(__name__)


# ── 8 Business document definitions ───────────────────────────────────────────
# Each entry: (output_filename, prompt_builder_function, description_for_log)

_BUSINESS_DOCS: list[tuple[str, Callable[..., str], str]] = [
    (
        "SCHEME_MASTER_DATABASE.md",
        build_scheme_master_db_prompt,
        "Scheme Master DB entry (AI qualification brain)",
    ),
    (
        "PITCH_AND_SALES_SCRIPTS.md",
        build_pitch_scripts_prompt,
        "Pitch & Sales Scripts (discovery call + objection handlers)",
    ),
    (
        "APPLICATION_PLAYBOOK.md",
        build_application_playbook_prompt,
        "Application Playbook (5-stage execution guide)",
    ),
    (
        "CLIENT_ONBOARDING_AND_CRM.md",
        build_client_onboarding_prompt,
        "Client Onboarding & CRM (intake form + pipeline)",
    ),
    (
        "LIVE_CASE_TRACKER.md",
        build_case_tracker_prompt,
        "Live Case Tracker (operations dashboard)",
    ),
    (
        "FEE_AND_REVENUE_MODEL.md",
        build_fee_model_prompt,
        "Fee & Revenue Model (pricing + projections)",
    ),
    (
        "CLIENT_PROPOSAL_TEMPLATE.md",
        build_client_proposal_prompt,
        "Client Proposal Template (ready-to-send)",
    ),
    (
        "COMPLIANCE_AND_LEGAL_PACK.md",
        build_compliance_pack_prompt,
        "Compliance & Legal Pack (NDAs, disclaimers, data policy)",
    ),
]


class ReportGenerator:
    """
    Generates the 8 business document Markdown files for each scheme artifact directory.

    Each file gets a separate LLM call using:
      - key_facts: compact structured summary from ai_summary.json
      - full_text:  crawled page text + PDF document text
    """

    def __init__(self, settings: AppSettings):
        self.settings = settings
        self.client = NvidiaLLMClient(settings)

    def process_run(self, run_dir: Path) -> None:
        artifacts_dir = run_dir / "artifacts"
        if not artifacts_dir.exists():
            logger.error("No artifacts directory found in %s", run_dir)
            return

        scheme_dirs = [d for d in sorted(artifacts_dir.iterdir()) if d.is_dir()]
        logger.info(
            "Generating 8 business documents for %d scheme(s)...", len(scheme_dirs)
        )

        for scheme_dir in scheme_dirs:
            self._process_scheme_dir(scheme_dir)

        logger.info("All business document reports complete.")

    def _process_scheme_dir(self, scheme_dir: Path) -> None:
        logger.info("─" * 60)
        logger.info("  Processing scheme dir: %s", scheme_dir.name)

        # ── Stage 1: Synthesize evidence ──────────────────────────────────────
        try:
            ev: SynthesizedEvidence = synthesize(scheme_dir)
            logger.info(
                "  Evidence: %d page chars + %d pdf chars | key_facts: %d chars",
                ev.page_chars,
                ev.pdf_chars,
                len(ev.key_facts),
            )
        except Exception as exc:
            logger.error("  Evidence synthesis failed for %s: %s", scheme_dir.name, exc)
            return

        if not ev.key_facts and not ev.full_text:
            logger.warning(
                "  No evidence available for '%s' — skipping document generation",
                scheme_dir.name,
            )
            return

        # ── Stage 2: Generate each of the 8 business documents ───────────────
        logger.info("  Generating 8 business documents for: %s", ev.scheme_name)

        for filename, prompt_builder, description in _BUSINESS_DOCS:
            output_path = scheme_dir / filename

            # Build the prompt for this specific document type
            # functools.partial captures ev.key_facts and ev.full_text at iteration time
            # (avoids Python loop closure / lambda capture bug)
            generator = functools.partial(
                self._call_llm,
                prompt=prompt_builder(ev.key_facts, ev.full_text),
                label=filename,
            )

            self._generate_and_save(output_path, generator, description)

        logger.info("  ✓ All 8 documents generated for '%s'", ev.scheme_name)

    def _call_llm(self, prompt: str, label: str) -> str:
        """Make a single LLM call with the business docs system prompt."""
        return self.client.generate_markdown_report_with_system(
            system_prompt=BUSINESS_DOCS_SYSTEM_PROMPT,
            user_prompt=prompt,
        )

    def _generate_and_save(
        self,
        path: Path,
        generator: Callable[[], str],
        description: str,
    ) -> None:
        if path.exists() and path.stat().st_size > 100:
            logger.info("    -> Already exists (skipping): %s", path.name)
            return

        t0 = time.perf_counter()
        try:
            content = generator()
            path.write_text(content, encoding="utf-8")
            elapsed = time.perf_counter() - t0
            logger.info(
                "    -> [%.1fs] Created %-42s (%d chars) | %s",
                elapsed,
                path.name,
                len(content),
                description,
            )
        except Exception as exc:
            logger.error("    -> Failed to create %s: %s", path.name, exc)
