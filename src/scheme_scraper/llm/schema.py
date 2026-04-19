"""
SchemeInsight — structured intelligence output from the NVIDIA LLM analysis step.

This is the canonical schema that flows through the entire pipeline:
    crawl → evidence_bundle → LLM analysis → SchemeInsight → CSV + Markdown reports

Adding a field here requires matching updates in:
  - prompts.py (include in JSON schema instruction)
  - writers.py (add to ENRICHED_COLUMNS if it belongs in the CSV)
  - runner.py  (if it's logged per-scheme)
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator


class SchemeInsight(BaseModel):
    # ── Core identity ──────────────────────────────────────────────────────────
    overview: str = ""
    scheme_type: Literal["grant", "loan", "subsidy", "recognition", "incubation", "tax_benefit", "other"] = "other"
    target_beneficiaries: list[str] = Field(default_factory=list)
    geographic_scope: str = ""          # "Pan-India", "Maharashtra only", etc.

    # ── Programme detail ───────────────────────────────────────────────────────
    objectives: list[str] = Field(default_factory=list)
    eligibility: str = ""
    benefits: str = ""

    # ── Financial specifics ────────────────────────────────────────────────────
    financial_support: str = ""
    fund_size_crores: str = ""          # Total corpus in INR crores (string to handle ranges)
    grant_amount_per_entity: str = ""   # Max benefit per applicant

    # ── Application mechanics ─────────────────────────────────────────────────
    application_process: str = ""
    application_portal_url: str = ""    # Direct URL of the apply portal
    required_documents: list[str] = Field(default_factory=list)
    deadlines: str = ""

    # ── Organisation ──────────────────────────────────────────────────────────
    implementing_agency: str = ""
    contact_details: str = ""

    # ── Metadata ──────────────────────────────────────────────────────────────
    caveats: list[str] = Field(default_factory=list)
    source_cited_notes: list[str] = Field(default_factory=list)
    last_updated_date: str = ""
    confidence: str = "unknown"         # low | medium | high
    analysis_timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    # ── Robust LLM Coercion ───────────────────────────────────────────────────
    @field_validator(
        "overview", "geographic_scope", "eligibility", "benefits",
        "financial_support", "fund_size_crores", "grant_amount_per_entity",
        "application_process", "application_portal_url", "deadlines",
        "implementing_agency", "contact_details", "last_updated_date",
        mode="before"
    )
    @classmethod
    def coerce_str_fields(cls, v: Any) -> str:
        if isinstance(v, list):
            return "\n".join(str(item) for item in v)
        if v is None:
            return ""
        return str(v)

    @field_validator(
        "target_beneficiaries", "objectives", "required_documents",
        "caveats", "source_cited_notes",
        mode="before"
    )
    @classmethod
    def coerce_list_fields(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [v] if v.strip() else []
        if v is None:
            return []
        if isinstance(v, list):
            return [str(item) for item in v]
        return []

    # ─────────────────────────────────────────────────────────────────────────

    @classmethod
    def empty(cls, reason: str) -> "SchemeInsight":
        return cls(
            overview=f"[Extraction failed] {reason}",
            confidence="low",
            source_cited_notes=["No validated LLM output available."],
        )

    # ── Rich Markdown renderer ────────────────────────────────────────────────

    def _badge(self, label: str, value: str, color: str = "blue") -> str:
        if not value:
            return ""
        safe = value.replace("-", "--").replace(" ", "_")
        lbl = label.replace(" ", "_")
        return f"![{label}](https://img.shields.io/badge/{lbl}-{safe}-{color})"

    def to_markdown(self, scheme_name: str, scheme_url: str) -> str:
        def bullet_list(items: list[str], fallback: str = "_Not available_") -> str:
            return "\n".join(f"- {i}" for i in items) if items else fallback

        def section(title: str, body: str, fallback: str = "_Not available_") -> str:
            return f"## {title}\n{body.strip() or fallback}\n"

        # Confidence badge colour
        conf_color = {"high": "brightgreen", "medium": "yellow", "low": "red"}.get(
            self.confidence.lower(), "lightgrey"
        )
        conf_badge = (
            f"![Confidence](https://img.shields.io/badge/Confidence-{self.confidence}-{conf_color})"
        )
        type_badge = (
            f"![Type](https://img.shields.io/badge/Type-{self.scheme_type.replace('_', '--')}-blue)"
            if self.scheme_type
            else ""
        )
        scope_badge = (
            f"![Scope](https://img.shields.io/badge/Scope-{self.geographic_scope.replace(' ', '_')}-purple)"
            if self.geographic_scope
            else ""
        )

        badges = "  ".join(b for b in [conf_badge, type_badge, scope_badge] if b)

        # Financial table
        fin_rows = []
        if self.fund_size_crores:
            fin_rows.append(f"| Total Fund Corpus | ₹ {self.fund_size_crores} Cr |")
        if self.grant_amount_per_entity:
            fin_rows.append(f"| Max Per Entity | {self.grant_amount_per_entity} |")
        fin_table = (
            "| Parameter | Value |\n|---|---|\n" + "\n".join(fin_rows)
            if fin_rows
            else "_Not specified_"
        )

        beneficiaries_line = ", ".join(self.target_beneficiaries) if self.target_beneficiaries else "_Not specified_"

        portal_line = (
            f"[Apply Here]({self.application_portal_url})"
            if self.application_portal_url
            else "_Not specified_"
        )

        return f"""# 🏛 Scheme Intelligence Report: {scheme_name}

{badges}

> **Source URL:** {scheme_url}
> **Analysis Timestamp:** {self.analysis_timestamp}
> **Last Known Update:** {self.last_updated_date or "Not specified"}

---

{section("📋 Executive Overview", self.overview)}

---

{section("🎯 Objectives", bullet_list(self.objectives))}

---

## 💰 Financial Summary

{fin_table}

---

{section("✅ Eligibility", self.eligibility)}

**Target Beneficiaries:** {beneficiaries_line}
**Geographic Scope:** {self.geographic_scope or "_Not specified_"}

---

{section("🎁 Benefits", self.benefits)}

---

{section("💳 Financial Support", self.financial_support)}

---

## 📝 How to Apply

{section("Application Process", self.application_process)}

**Application Portal:** {portal_line}

{section("Required Documents", bullet_list(self.required_documents))}

{section("⏰ Deadlines", self.deadlines)}

---

{section("🏢 Implementing Agency", self.implementing_agency)}

{section("📞 Contact Details", self.contact_details)}

---

{section("⚠️ Caveats & Conditions", bullet_list(self.caveats))}

---

## 📚 Sources

{bullet_list(self.source_cited_notes)}

---

*Confidence Level: **{self.confidence.upper()}***
"""
