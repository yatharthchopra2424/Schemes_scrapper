"""
Site crawler — BFS crawl with compliance, smart link scoring, and JS-content detection.

Improvements over v1:
  - Smart link queue: high-value links (eligibility, apply, guidelines) visited first
  - JS content detection: if text < 500 chars after first load, waits 3s and re-extracts
  - Structured metadata extraction (og:description, page title, h1)
  - Requests fallback: if Selenium fetch returns empty HTML, tries static GET
  - Better error classification (timeout / DNS / 403 / CAPTCHA / JS-heavy)
  - Per-page timing logged at DEBUG level
  - extract_links() now returns (url, score) tuples — sorted by priority
"""
from __future__ import annotations

import logging
import time
from collections import deque
from pathlib import Path
from typing import Any
from urllib import robotparser
from urllib.parse import urlparse

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from selenium.webdriver.common.by import By

from ..config import AppSettings
from ..extract.doc_extract import download_and_extract_document
from ..extract.html_extract import (
    extract_links,
    extract_structured_metadata,
    extract_visible_text,
)
from ..models import DocumentCapture, PageCapture, SchemeEvidence, SchemeInput
from ..utils import canonicalize_url, dedupe_preserve_order, same_domain
from .driver import wait_for_dom_ready

# Minimum visible text length to trust a Selenium render (below this → JS-heavy, wait more)
_MIN_TEXT_LENGTH = 500
_JS_EXTRA_WAIT_S = 3.0     # Extra wait for JS-heavy pages before re-extraction
_STATIC_TIMEOUT = 15       # Timeout for requests fallback


class RobotsCache:
    """Thread-compatible robots.txt parser with in-process domain cache."""

    def __init__(
        self,
        user_agent: str,
        timeout_seconds: int,
        logger: logging.Logger,
    ):
        self.user_agent = user_agent
        self.timeout_seconds = timeout_seconds
        self.logger = logger
        self._parsers: dict[str, robotparser.RobotFileParser] = {}
        self._delays: dict[str, float] = {}

    def _load_parser(self, url: str) -> robotparser.RobotFileParser:
        parsed = urlparse(url)
        netloc = parsed.netloc.lower()
        if netloc in self._parsers:
            return self._parsers[netloc]

        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        parser = robotparser.RobotFileParser()

        try:
            response = requests.get(
                robots_url,
                timeout=min(self.timeout_seconds, 10),
                headers={"User-Agent": self.user_agent},
                verify=False,
            )
            if response.status_code < 400:
                parser.parse(response.text.splitlines())
            else:
                parser.parse([])
        except Exception as exc:
            self.logger.debug("Could not fetch robots.txt for %s: %s", netloc, exc)
            parser.parse([])

        delay = parser.crawl_delay(self.user_agent) or parser.crawl_delay("*")
        self._delays[netloc] = float(delay or 0.0)
        self._parsers[netloc] = parser
        return parser

    def can_fetch(self, url: str) -> bool:
        return self._load_parser(url).can_fetch(self.user_agent, url)

    def crawl_delay(self, url: str) -> float:
        netloc = urlparse(url).netloc.lower()
        if netloc not in self._delays:
            self._load_parser(url)
        return self._delays.get(netloc, 0.0)


def _respect_delay(domain: str, delay: float, domain_last_seen: dict[str, float]) -> None:
    now = time.monotonic()
    remaining = delay - (now - domain_last_seen.get(domain, 0.0))
    if remaining > 0:
        time.sleep(remaining)


def _classify_error(exc_text: str) -> str:
    """Produce a concise, human-readable error label from a Selenium exception string."""
    text = exc_text.lower()
    if "timeout" in text or "timed out" in text:
        return "TIMEOUT"
    if "err_name_not_resolved" in text or "dns" in text:
        return "DNS_FAIL"
    if "403" in text or "forbidden" in text:
        return "HTTP_403"
    if "captcha" in text or "cloudflare" in text or "recaptcha" in text:
        return "CAPTCHA"
    if "javascript" in text or "err_aborted" in text:
        return "JS_BLOCKED"
    return "FETCH_ERROR"


def _try_static_fetch(url: str, user_agent: str) -> str:
    """
    Lightweight requests-based fallback to fetch static HTML.
    Used when Selenium returns empty or very thin content.
    """
    try:
        resp = requests.get(
            url,
            timeout=_STATIC_TIMEOUT,
            headers={
                "User-Agent": user_agent,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            },
            verify=False,
            allow_redirects=True,
        )
        if resp.status_code == 200:
            return resp.text
    except Exception:
        pass
    return ""


def _fetch_page_in_new_window(
    driver: Any,
    root_handle: str,
    url: str,
    settings: AppSettings,
    logger: logging.Logger,
    max_retries: int = 2,
) -> tuple[str, str, str | None]:
    """
    Open a new browser tab, fetch the URL, extract title + HTML, then close the tab.

    Includes:
      - Retry with increasing timeout
      - JS-heavy detection: if text < _MIN_TEXT_LENGTH after load, wait + re-check
      - Requests fallback for static pages that Selenium can't render
    """
    last_error: str | None = None

    for attempt in range(max_retries):
        driver.switch_to.window(root_handle)
        driver.switch_to.new_window("window")

        try:
            timeout = settings.crawler.page_load_timeout_seconds * (attempt + 1)
            driver.set_page_load_timeout(timeout)
            t0 = time.perf_counter()
            driver.get(url)
            wait_for_dom_ready(driver, timeout)

            # Render wait
            if settings.crawler.render_wait_seconds > 0:
                time.sleep(settings.crawler.render_wait_seconds)

            title = driver.title or ""
            html = driver.page_source or ""

            # JS-heavy detection: check text length
            quick_text = extract_visible_text(html)
            if len(quick_text) < _MIN_TEXT_LENGTH and html:
                logger.debug(
                    "JS-heavy page detected at %s (text=%d chars). Waiting %.1fs more.",
                    url,
                    len(quick_text),
                    _JS_EXTRA_WAIT_S,
                )
                time.sleep(_JS_EXTRA_WAIT_S)
                html = driver.page_source or html  # Re-fetch after extra wait

            elapsed = time.perf_counter() - t0
            logger.debug("Fetched %s in %.1fs (attempt %d)", url, elapsed, attempt + 1)
            return title, html, None

        except Exception as exc:
            raw_error = str(exc)
            first_line = raw_error.split("\n")[0]
            error_class = _classify_error(raw_error)
            last_error = f"{error_class}: {first_line}"
            logger.debug("Fetch error [%s] for %s: %s", error_class, url, first_line)

            try:
                driver.switch_to.alert.dismiss()
            except Exception:
                pass

        finally:
            try:
                driver.switch_to.alert.dismiss()
            except Exception:
                pass
            try:
                if len(driver.window_handles) > 1:
                    driver.close()
            except Exception:
                pass
            driver.switch_to.window(root_handle)

        time.sleep(1.5)  # Brief pause before retry

    # Requests fallback as last resort (catches static government pages)
    logger.debug("Attempting requests fallback for %s", url)
    fallback_html = _try_static_fetch(url, settings.crawler.user_agent)
    if fallback_html:
        logger.debug("Requests fallback succeeded for %s (%d chars)", url, len(fallback_html))
        return "", fallback_html, None

    return "", "", last_error


def crawl_scheme(
    driver: Any,
    scheme: SchemeInput,
    settings: AppSettings,
    scheme_dir: Path,
    logger: logging.Logger,
) -> SchemeEvidence:
    """
    BFS crawl of a government scheme website.

    Queue items are (url, depth, referrer).
    Links are sorted by priority score before being enqueued.
    """
    evidence = SchemeEvidence(scheme)
    html_dir = scheme_dir / "html"
    docs_dir = scheme_dir / "documents"
    html_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    # (url, depth, referrer)
    queue: deque[tuple[str, int, str | None]] = deque()
    queue.append((canonicalize_url(scheme.scheme_url), 0, None))

    root_handle = driver.current_window_handle
    visited: set[str] = set()
    seen_documents: set[str] = set()
    domain_last_seen: dict[str, float] = {}

    robots = RobotsCache(
        user_agent=settings.crawler.user_agent,
        timeout_seconds=settings.compliance.request_timeout_seconds,
        logger=logger,
    )

    while queue and len(evidence.pages) < settings.crawler.max_pages_per_scheme:
        current_url, depth, referrer = queue.popleft()
        canonical_url = canonicalize_url(current_url)

        if canonical_url in visited:
            continue
        if not same_domain(canonical_url, scheme.scheme_url):
            continue

        # Robots compliance
        if settings.compliance.strict_mode and not robots.can_fetch(canonical_url):
            evidence.skipped_urls.append(canonical_url)
            visited.add(canonical_url)
            logger.debug("Robots-blocked: %s", canonical_url)
            continue

        # Crawl delay compliance
        domain = urlparse(canonical_url).netloc.lower()
        required_delay = max(
            settings.compliance.min_delay_seconds,
            robots.crawl_delay(canonical_url),
        )
        _respect_delay(domain, required_delay, domain_last_seen)

        # Fetch
        title, html, error = _fetch_page_in_new_window(
            driver, root_handle, canonical_url, settings, logger
        )
        domain_last_seen[domain] = time.monotonic()

        # Save HTML to disk
        page_index = len(evidence.pages) + 1
        html_path = html_dir / f"page_{page_index:03d}.html"
        if html:
            try:
                html_path.write_text(html, encoding="utf-8", errors="ignore")
            except Exception as write_exc:
                logger.debug("Failed to write HTML file: %s", write_exc)

        # Extract text, links, metadata
        page_links: list[tuple[str, int]] = []
        doc_links: list[str] = []
        text = ""
        metadata: dict[str, str] = {}

        if html:
            text = extract_visible_text(html)
            metadata = extract_structured_metadata(html, canonical_url)
            page_links, doc_links = extract_links(html, canonical_url)

        page_capture = PageCapture(
            url=canonical_url,
            depth=depth,
            title=title or metadata.get("page_title", ""),
            text=text,
            html_path=str(html_path),
            discovered_links=[url for url, _ in page_links],
            discovered_documents=doc_links,
            referrer=referrer,
            error=error,
        )
        evidence.pages.append(page_capture)
        visited.add(canonical_url)

        if error:
            evidence.crawl_errors.append(f"{canonical_url}: {error}")
            logger.warning("Failed: %s — %s", canonical_url, error)
            continue

        logger.debug(
            "Crawled page %d/%d: %s | text=%d chars | links=%d",
            len(evidence.pages),
            settings.crawler.max_pages_per_scheme,
            canonical_url,
            len(text),
            len(page_links),
        )

        # Document downloads (capped)
        max_docs = settings.crawler.max_documents_per_scheme
        for doc_url in doc_links:
            if len(evidence.documents) >= max_docs:
                logger.debug("Document cap (%d) reached, skipping remaining docs", max_docs)
                break
            canonical_doc = canonicalize_url(doc_url)
            if canonical_doc in seen_documents:
                continue
            seen_documents.add(canonical_doc)

            if settings.compliance.strict_mode and not robots.can_fetch(canonical_doc):
                evidence.skipped_urls.append(canonical_doc)
                continue

            try:
                doc_capture = download_and_extract_document(
                    url=canonical_doc,
                    target_dir=docs_dir,
                    timeout_seconds=settings.compliance.request_timeout_seconds,
                    max_document_mb=settings.documents.max_document_mb,
                    user_agent=settings.crawler.user_agent,
                )
                evidence.documents.append(doc_capture)
                logger.debug(
                    "Downloaded doc: %s (%s, %d chars)",
                    canonical_doc,
                    doc_capture.extraction_status,
                    len(doc_capture.extracted_text),
                )
            except Exception as exc:
                evidence.documents.append(
                    DocumentCapture(
                        url=canonical_doc,
                        local_path="",
                        sha256="",
                        content_type="unknown",
                        extraction_status="failed",
                        error=str(exc)[:200],
                    )
                )
                evidence.crawl_errors.append(f"Doc download failed {canonical_doc}: {exc}")
                logger.debug("Doc download failed: %s — %s", canonical_doc, exc)

        # Enqueue child links if under max_depth
        if depth < settings.crawler.max_depth:
            for link_url, _score in page_links:
                canonical_link = canonicalize_url(link_url)
                if canonical_link in visited:
                    continue
                if not same_domain(canonical_link, scheme.scheme_url):
                    continue
                # Insert at front if high-score (priority crawl), otherwise append
                if _score >= 2:
                    queue.appendleft((canonical_link, depth + 1, canonical_url))
                else:
                    queue.append((canonical_link, depth + 1, canonical_url))

    logger.info(
        "Crawl complete for '%s': %d pages, %d docs, %d errors, %d skipped",
        scheme.scheme_name,
        len(evidence.pages),
        len(evidence.documents),
        len(evidence.crawl_errors),
        len(evidence.skipped_urls),
    )
    return evidence
