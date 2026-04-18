from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class SchemeInput:
    row_id: str
    ministry_or_category: str
    scheme_name: str
    scheme_url: str


@dataclass
class PageCapture:
    url: str
    depth: int
    title: str
    text: str
    html_path: str
    discovered_links: list[str] = field(default_factory=list)
    discovered_documents: list[str] = field(default_factory=list)
    referrer: str | None = None
    fetched_at: str = field(default_factory=utc_now_iso)
    error: str | None = None


@dataclass
class DocumentCapture:
    url: str
    local_path: str
    sha256: str
    content_type: str
    extraction_status: str
    extracted_text: str = ""
    fetched_at: str = field(default_factory=utc_now_iso)
    error: str | None = None


@dataclass
class SchemeEvidence:
    scheme: SchemeInput
    pages: list[PageCapture] = field(default_factory=list)
    documents: list[DocumentCapture] = field(default_factory=list)
    skipped_urls: list[str] = field(default_factory=list)
    crawl_errors: list[str] = field(default_factory=list)


@dataclass
class SchemeResult:
    scheme: SchemeInput
    status: str
    evidence_json_path: str | None = None
    report_markdown_path: str | None = None
    error: str | None = None
    llm_summary: dict[str, Any] | None = None
