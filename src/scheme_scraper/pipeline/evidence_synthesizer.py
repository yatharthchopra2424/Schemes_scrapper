"""
Evidence Synthesizer — merges all evidence sources into one rich context object.
─────────────────────────────────────────────────────────────────────────────────
Inputs (all post-crawl, already on disk):
  1. evidence_bundle.json  → crawled pages + downloaded doc metadata
  2. documents/            → actual PDF/DOCX files downloaded during crawl
  3. ai_summary.json       → structured LLM analysis from the enrichment stage

Output: SynthesizedEvidence
  - key_facts      : compact structured fact sheet (from ai_summary.json)
                     injected at the TOP of every report prompt so the LLM
                     has precise numbers, URLs, and names before reading raw text
  - page_text      : concatenated crawled page text
  - pdf_text       : concatenated PDF document text
  - full_text      : page_text + pdf_text combined (for evidence section of prompt)
  - ai_summary     : raw dict from ai_summary.json

Design note: key_facts acts as a "knowledge graph node" – it collapses the
structured data into a string report-writers can pre-pend to any prompt,
giving the model crisp facts before the fuzzy raw evidence.
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..extract.doc_extract import build_pdf_evidence_text

logger = logging.getLogger(__name__)


@dataclass
class SynthesizedEvidence:
    scheme_name: str
    scheme_url: str
    scheme_id: str
    ministry: str

    # ── Structured data from ai_summary.json ──────────────────────────────────
    ai_summary: dict[str, Any] = field(default_factory=dict)

    # ── Compact fact sheet (generated from ai_summary) ─────────────────────────
    key_facts: str = ""

    # ── Raw evidence text from pages + PDFs ───────────────────────────────────
    page_text: str = ""
    pdf_text: str = ""
    full_text: str = ""   # page_text + pdf_text combined

    # ── Stats ──────────────────────────────────────────────────────────────────
    pages_count: int = 0
    docs_count: int = 0
    pdf_chars: int = 0
    page_chars: int = 0


def _build_key_facts(summary: dict[str, Any]) -> str:
    """
    Convert a structured ai_summary dict into a compact, LLM-readable
    'key facts' block.  Injected at the top of every prompt so the model
    has exact figures before reading raw evidence.

    Think of this as a knowledge-graph node serialised to plain text.
    """
    lines: list[str] = ["=== SCHEME KEY FACTS (extracted structured data) ==="]

    def add(label: str, value: Any) -> None:
        if value and value != "" and value != [] and value != {}:
            if isinstance(value, list):
                joined = "; ".join(str(v) for v in value[:10])
                lines.append(f"{label}: {joined}")
            else:
                lines.append(f"{label}: {value}")

    add("Scheme Name",           summary.get("scheme_name"))
    add("Scheme ID",             summary.get("scheme_id"))
    add("Ministry / Category",   summary.get("ministry_or_category"))
    add("Scheme Type",           summary.get("scheme_type"))
    add("Geographic Scope",      summary.get("geographic_scope"))
    add("Implementing Agency",   summary.get("implementing_agency"))
    add("Application Portal",    summary.get("application_portal_url"))
    add("Status / Deadlines",    summary.get("deadlines"))
    add("Last Updated",          summary.get("last_updated_date"))

    add("Fund Size (Cr)",        summary.get("fund_size_crores"))
    add("Max Per Entity",        summary.get("grant_amount_per_entity"))
    add("Financial Support",     summary.get("financial_support"))
    add("Benefits",              summary.get("benefits"))

    add("Eligibility",           summary.get("eligibility"))
    add("Target Beneficiaries",  summary.get("target_beneficiaries"))

    docs = summary.get("required_documents", [])
    if docs:
        lines.append("Required Documents:")
        for i, doc in enumerate(docs[:15], 1):
            lines.append(f"  {i}. {doc}")

    add("Application Process",   summary.get("application_process"))
    add("Contact Details",       summary.get("contact_details"))

    caveats = summary.get("caveats", [])
    if caveats:
        lines.append("Key Caveats:")
        for c in caveats[:8]:
            lines.append(f"  - {c}")

    objectives = summary.get("objectives", [])
    if objectives:
        lines.append("Objectives:")
        for o in objectives[:8]:
            lines.append(f"  - {o}")

    add("Confidence",            summary.get("confidence"))

    lines.append("=== END KEY FACTS ===")
    return "\n".join(lines)


def _build_page_text(bundle: dict[str, Any], max_chars: int = 80_000) -> tuple[str, int]:
    """Extract and concatenate crawled page text from evidence_bundle.json."""
    evidence_section = bundle.get("evidence") or bundle.get("crawl") or {}
    pages = evidence_section.get("pages", [])

    chunks: list[str] = []
    total = 0

    for page in pages:
        text = (page.get("text") or "").strip()
        if not text or total >= max_chars:
            continue
        chunk = (
            f"--- CRAWLED PAGE ---\n"
            f"URL: {page.get('url', '')}\n"
            f"TITLE: {page.get('title', '')}\n"
            f"TEXT:\n{text[:18_000]}"
        )
        chunks.append(chunk)
        total += len(chunk)

    combined = "\n\n".join(chunks)
    return combined[:max_chars], len(pages)


def synthesize(scheme_dir: Path, max_full_text: int = 150_000) -> SynthesizedEvidence:
    """
    Build a SynthesizedEvidence for the given scheme artifact directory.

    Pipeline:
      1. Load ai_summary.json → structured facts + key_facts block
      2. Load evidence_bundle.json → crawled page text
      3. Read documents/ folder → PDF text (post-crawl, files already on disk)
      4. Combine page + PDF text → full_text (capped at max_full_text)
    """
    # ── 1. Load ai_summary.json ────────────────────────────────────────────────
    ai_summary: dict[str, Any] = {}
    ai_summary_path = scheme_dir / "ai_summary.json"
    if ai_summary_path.exists():
        try:
            ai_summary = json.loads(ai_summary_path.read_text(encoding="utf-8"))
            logger.debug("Loaded ai_summary.json for %s", scheme_dir.name)
        except Exception as exc:
            logger.warning("Could not load ai_summary.json in %s: %s", scheme_dir.name, exc)
    else:
        logger.warning("No ai_summary.json found in %s", scheme_dir.name)

    scheme_name = ai_summary.get("scheme_name") or scheme_dir.name
    scheme_url  = ai_summary.get("scheme_url") or ""
    scheme_id   = ai_summary.get("scheme_id") or ""
    ministry    = ai_summary.get("ministry_or_category") or ""

    key_facts = _build_key_facts(ai_summary) if ai_summary else ""

    # ── 2. Load evidence_bundle.json → page text ──────────────────────────────
    page_text: str = ""
    pages_count = 0
    bundle_path = scheme_dir / "evidence_bundle.json"
    if bundle_path.exists():
        try:
            bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
            page_text, pages_count = _build_page_text(bundle)
        except Exception as exc:
            logger.warning("Could not load evidence_bundle.json in %s: %s", scheme_dir.name, exc)
    else:
        logger.warning("No evidence_bundle.json found in %s", scheme_dir.name)

    # ── 3. Load PDFs from documents/ folder ───────────────────────────────────
    documents_dir = scheme_dir / "documents"
    pdf_text = build_pdf_evidence_text(documents_dir)
    docs_count = len(list(documents_dir.glob("*.pdf"))) + len(list(documents_dir.glob("*.docx"))) if documents_dir.exists() else 0

    # ── 4. Combine into full_text ─────────────────────────────────────────────
    parts = []
    if page_text:
        parts.append("=== CRAWLED WEB PAGES ===\n" + page_text)
    if pdf_text:
        parts.append("=== DOWNLOADED PDF DOCUMENTS ===\n" + pdf_text)

    full_text = "\n\n".join(parts)[:max_full_text]

    logger.info(
        "Evidence synthesized for '%s': %d pages, %d PDFs, %d page chars, %d pdf chars",
        scheme_name, pages_count, docs_count, len(page_text), len(pdf_text),
    )

    return SynthesizedEvidence(
        scheme_name=scheme_name,
        scheme_url=scheme_url,
        scheme_id=scheme_id,
        ministry=ministry,
        ai_summary=ai_summary,
        key_facts=key_facts,
        page_text=page_text,
        pdf_text=pdf_text,
        full_text=full_text,
        pages_count=pages_count,
        docs_count=docs_count,
        pdf_chars=len(pdf_text),
        page_chars=len(page_text),
    )
