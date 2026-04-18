"""
HTML extraction utilities for scheme evidence gathering.

Enhancements over v1:
  - extract_structured_metadata: pulls h1/h2/h3 + meta description + og:description
  - extract_tables: converts HTML <table> → pipe-delimited text (government sites use these extensively)
  - extract_definition_lists: converts <dl>/<dt>/<dd> → key: value pairs
  - extract_visible_text: now strips nav/footer/header to reduce noise
  - chunk_text: unchanged (used by LLM context building)
"""
from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, NavigableString, Tag

DOCUMENT_EXTENSIONS = (".pdf", ".doc", ".docx", ".xlsx", ".xls", ".pptx", ".ppt")

# Tag names that typically contain navigation boilerplate (pruned before text extraction)
_NOISE_TAGS = ["script", "style", "noscript", "svg", "nav", "aside", "footer", "header", "form"]

# Keywords that indicate high-value scheme pages (used for link scoring)
_PRIORITY_KEYWORDS = [
    "eligib", "apply", "application", "how-to", "guidelines", "notification",
    "circular", "scheme", "benefit", "fund", "grant", "loan", "subsidy",
    "crore", "lakh", "amount", "support", "document", "criteria", "portal",
    "register", "registration",
]


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


# ── Text Extraction ────────────────────────────────────────────────────────────

def extract_visible_text(html: str) -> str:
    """
    Extract human-readable text from HTML, removing navigation, scripts, and style.
    Tables and definition lists are rendered inline for better LLM comprehension.
    """
    soup = BeautifulSoup(html, "lxml")

    # Remove boilerplate tags first
    for tag in soup(_NOISE_TAGS):
        tag.decompose()

    # Render tables to text before extracting
    for table in soup.find_all("table"):
        table.replace_with(NavigableString(_table_to_text(table) + "\n"))

    # Render definition lists to text
    for dl in soup.find_all("dl"):
        dl.replace_with(NavigableString(_dl_to_text(dl) + "\n"))

    text = soup.get_text(separator=" ", strip=True)
    return normalize_whitespace(text)


def extract_structured_metadata(html: str, url: str) -> dict[str, str]:
    """
    Pull structured metadata from the HTML head and first heading:
      - title tag
      - meta description
      - og:title, og:description
      - first h1
    Returns a dict that can be prepended to the evidence text.
    """
    soup = BeautifulSoup(html, "lxml")
    meta: dict[str, str] = {"url": url}

    title_tag = soup.find("title")
    if title_tag:
        meta["page_title"] = normalize_whitespace(title_tag.get_text())

    for attr, key in [
        ("description", "meta_description"),
        ("og:description", "og_description"),
        ("og:title", "og_title"),
        ("keywords", "meta_keywords"),
    ]:
        tag = soup.find("meta", attrs={"name": attr}) or soup.find("meta", attrs={"property": attr})
        if tag and isinstance(tag, Tag):
            content = tag.get("content", "")
            if content:
                meta[key] = normalize_whitespace(str(content))

    h1 = soup.find("h1")
    if h1:
        meta["h1"] = normalize_whitespace(h1.get_text())

    return meta


def _table_to_text(table: Tag) -> str:
    """Convert an HTML table to pipe-delimited text rows."""
    lines: list[str] = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"])
        if not cells:
            continue
        row_text = " | ".join(normalize_whitespace(cell.get_text()) for cell in cells)
        lines.append(f"| {row_text} |")
    return "\n".join(lines)


def _dl_to_text(dl: Tag) -> str:
    """Convert <dl><dt>key</dt><dd>value</dd></dl> to 'key: value' pairs."""
    pairs: list[str] = []
    parts = dl.find_all(["dt", "dd"])
    i = 0
    while i < len(parts):
        part = parts[i]
        if part.name == "dt":
            key = normalize_whitespace(part.get_text())
            val = ""
            if i + 1 < len(parts) and parts[i + 1].name == "dd":
                val = normalize_whitespace(parts[i + 1].get_text())
                i += 1
            pairs.append(f"{key}: {val}" if val else key)
        i += 1
    return "\n".join(pairs)


# ── Link Extraction ────────────────────────────────────────────────────────────

def _score_link(url: str, anchor_text: str) -> int:
    """
    Score a link for crawl priority. Higher = more likely to contain scheme content.
    Used by navigator.py to sort the crawl queue.
    """
    score = 0
    combined = (url + " " + anchor_text).lower()
    for kw in _PRIORITY_KEYWORDS:
        if kw in combined:
            score += 1
    # Penalise obvious non-content pages
    if any(x in url.lower() for x in ["login", "logout", "contact", "sitemap", "faq", "privacy", "terms"]):
        score -= 2
    return score


def extract_links(
    html: str, base_url: str
) -> tuple[list[tuple[str, int]], list[str]]:
    """
    Extract page links (with priority scores) and document links from HTML.

    Returns:
        page_links : list of (url, score) tuples, sorted descending by score
        doc_links  : list of document URLs (PDF/DOCX/etc.)
    """
    soup = BeautifulSoup(html, "lxml")
    page_links: list[tuple[str, int]] = []
    doc_links: list[str] = []
    seen: set[str] = set()

    for anchor in soup.find_all("a", href=True):
        href = str(anchor.get("href", "")).strip()
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)
        if parsed.scheme not in {"http", "https"}:
            continue
        if full_url in seen:
            continue
        seen.add(full_url)

        anchor_text = normalize_whitespace(anchor.get_text())
        path_lower = parsed.path.lower()

        if any(path_lower.endswith(ext) for ext in DOCUMENT_EXTENSIONS):
            doc_links.append(full_url)
        else:
            score = _score_link(full_url, anchor_text)
            page_links.append((full_url, score))

    # Sort page links by score descending (high-value pages visited first)
    page_links.sort(key=lambda x: x[1], reverse=True)
    return page_links, doc_links


# ── Text Chunking ──────────────────────────────────────────────────────────────

def chunk_text(text: str, max_chars: int = 12000, overlap: int = 500) -> list[str]:
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]
    chunks: list[str] = []
    step = max_chars - overlap
    cursor = 0
    while cursor < len(text):
        chunks.append(text[cursor : cursor + max_chars])
        cursor += step
    return chunks
