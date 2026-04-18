"""
Pipeline output writers — CSV, JSON, Markdown.

Changes from v1:
  - ENRICHED_COLUMNS expanded with all new SchemeInsight fields
  - write_evidence_bundle saves evidence under BOTH 'crawl' and 'evidence' keys
    (report_generator.py looks for 'evidence' — now both are present for compatibility)
  - write_ai_summary_json: saves a clean per-scheme AI summary JSON for downstream use
"""
from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from ..llm.schema import SchemeInsight
from ..models import SchemeEvidence, SchemeInput


ENRICHED_COLUMNS = [
    # ── Identity ────────────────────────────────
    "row_id",
    "ministry_or_category",
    "scheme_name",
    "scheme_url",
    # ── Run status ──────────────────────────────
    "status",
    "pages_crawled",
    "documents_found",
    "elapsed_seconds",
    # ── Core insight ────────────────────────────
    "overview",
    "scheme_type",
    "target_beneficiaries",
    "geographic_scope",
    "eligibility",
    "benefits",
    # ── Financial ───────────────────────────────
    "financial_support",
    "fund_size_crores",
    "grant_amount_per_entity",
    # ── Application ─────────────────────────────
    "application_process",
    "application_portal_url",
    "deadlines",
    # ── Organisation ────────────────────────────
    "implementing_agency",
    "contact_details",
    # ── Quality ─────────────────────────────────
    "confidence",
    "last_updated_date",
    # ── Paths ───────────────────────────────────
    "evidence_json_path",
    "report_markdown_path",
    "pitch_md_path",
    "howto_md_path",
    "summary_md_path",
    # ── Error ───────────────────────────────────
    "error",
]


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_evidence_bundle(
    path: Path,
    scheme: SchemeInput,
    evidence: SchemeEvidence,
    insight: SchemeInsight,
    llm_raw: str,
) -> None:
    """
    Save the full evidence bundle as JSON.

    The crawl data is stored under BOTH 'crawl' (original key) and 'evidence'
    (key used by report_generator.py) to ensure backward compatibility.
    """
    crawl_data = {
        "pages": [asdict(page) for page in evidence.pages],
        "documents": [asdict(doc) for doc in evidence.documents],
        "skipped_urls": evidence.skipped_urls,
        "crawl_errors": evidence.crawl_errors,
    }
    payload = {
        "scheme": asdict(scheme),
        "crawl": crawl_data,
        "evidence": crawl_data,       # Alias for report_generator compatibility
        "analysis": insight.model_dump(),
        "analysis_raw": llm_raw,
    }
    write_json(path, payload)


def write_ai_summary_json(path: Path, scheme: SchemeInput, insight: SchemeInsight) -> None:
    """
    Save a clean, downstream-friendly AI summary JSON (no raw HTML or crawl blobs).
    Suitable for feeding into downstream pipelines, APIs, or databases.
    """
    payload = {
        "scheme_id": scheme.row_id,
        "scheme_name": scheme.scheme_name,
        "scheme_url": scheme.scheme_url,
        "ministry_or_category": scheme.ministry_or_category,
        **insight.model_dump(),
    }
    write_json(path, payload)


def write_enriched_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=ENRICHED_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            # Serialise list fields to semicolon-separated strings for CSV compatibility
            serialised = {}
            for col in ENRICHED_COLUMNS:
                val = row.get(col, "")
                if isinstance(val, list):
                    val = "; ".join(str(v) for v in val)
                serialised[col] = val
            writer.writerow(serialised)


def read_enriched_csv(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))
