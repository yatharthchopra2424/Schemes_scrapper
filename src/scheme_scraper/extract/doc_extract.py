from __future__ import annotations

import logging
from pathlib import Path
from urllib.parse import urlparse

import requests
from docx import Document
from pypdf import PdfReader

from ..models import DocumentCapture
from ..utils import sha256_bytes, slugify

logger = logging.getLogger(__name__)

# Silence PyPDF warnings (e.g. "Ignoring wrong pointing object" or "invalid pdf header")
logging.getLogger("pypdf").setLevel(logging.CRITICAL)
logging.getLogger("pypdf.errors").setLevel(logging.CRITICAL)
SUPPORTED_DOCUMENT_EXTENSIONS = (".pdf", ".doc", ".docx")


def is_document_url(url: str) -> bool:
    path = urlparse(url).path.lower()
    return path.endswith(SUPPORTED_DOCUMENT_EXTENSIONS)


def _document_name_from_url(url: str) -> str:
    parsed = urlparse(url)
    original_name = Path(parsed.path).name or "document.bin"
    suffix = Path(original_name).suffix.lower() or ".bin"
    base_name = Path(original_name).stem or "document"
    safe_base = slugify(base_name, max_length=64)
    return f"{safe_base}{suffix}"


def _extract_pdf_text(path: Path) -> str:
    with path.open("rb") as fh:
        header = fh.read(5)
        if not header.startswith(b"%PDF-"):
            raise ValueError(f"Invalid PDF header: {header!r}")

    reader = PdfReader(str(path))
    pages: list[str] = []
    for page in reader.pages:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            pass
    return "\n".join(pages).strip()


def _extract_docx_text(path: Path) -> str:
    doc = Document(str(path))
    lines = [paragraph.text.strip() for paragraph in doc.paragraphs if paragraph.text.strip()]
    return "\n".join(lines)


def _best_effort_extract_text(path: Path, content_type: str) -> tuple[str, str]:
    suffix = path.suffix.lower()
    try:
        if suffix == ".pdf" or "pdf" in content_type:
            return _extract_pdf_text(path), "parsed"
        if suffix == ".docx":
            return _extract_docx_text(path), "parsed"
    except Exception as exc:
        logger.debug("Extraction failed for %s: %s", path.name, exc)
        return "", "error"

    if suffix == ".doc":
        # Legacy .doc requires native converters in most environments.
        return "", "downloaded_only"
    return "", "downloaded_only"


def download_and_extract_document(
    url: str,
    target_dir: Path,
    timeout_seconds: int,
    max_document_mb: int,
    user_agent: str,
) -> DocumentCapture:
    target_dir.mkdir(parents=True, exist_ok=True)
    max_bytes = max_document_mb * 1024 * 1024

    response = requests.get(
        url,
        timeout=timeout_seconds,
        headers={"User-Agent": user_agent},
        stream=True,
        verify=False,
    )
    response.raise_for_status()

    chunks: list[bytes] = []
    total = 0
    for chunk in response.iter_content(chunk_size=65536):
        if not chunk:
            continue
        total += len(chunk)
        if total > max_bytes:
            raise ValueError(f"Document exceeded max size ({max_document_mb} MB): {url}")
        chunks.append(chunk)

    blob = b"".join(chunks)
    file_name = _document_name_from_url(url)
    raw_path = target_dir / file_name
    raw_path.write_bytes(blob)

    content_type = response.headers.get("Content-Type", "application/octet-stream")
    extracted_text, extraction_status = _best_effort_extract_text(raw_path, content_type)

    return DocumentCapture(
        url=url,
        local_path=str(raw_path),
        sha256=sha256_bytes(blob),
        content_type=content_type,
        extraction_status=extraction_status,
        extracted_text=extracted_text,
    )


def build_pdf_evidence_text(
    documents_dir: Path,
    max_chars_per_doc: int = 100_000,
    max_total_chars: int = 300_000,
) -> str:
    """
    Read all already-downloaded PDF/DOCX files from a scheme's documents/ folder
    and return their combined extracted text.

    This is a POST-CRAWL stage — files are already on disk from the crawl run.
    We just re-read and concatenate them for use during report generation.

    Returns an empty string if the directory does not exist or is empty.
    """
    if not documents_dir.exists():
        return ""

    chunks: list[str] = []
    total_chars = 0

    supported_suffixes = {".pdf", ".docx"}
    files = sorted(documents_dir.iterdir())

    for file_path in files:
        if file_path.suffix.lower() not in supported_suffixes:
            continue
        if total_chars >= max_total_chars:
            break
        try:
            if file_path.suffix.lower() == ".pdf":
                text = _extract_pdf_text(file_path)
            else:
                text = _extract_docx_text(file_path)

            text = text.strip()
            if not text:
                continue

            # Truncate individual doc to avoid token flooding
            truncated = text[:max_chars_per_doc]
            chunk = (
                f"--- PDF DOCUMENT: {file_path.name} ---\n"
                f"{truncated}"
            )
            chunks.append(chunk)
            total_chars += len(chunk)
            logger.debug("PDF evidence loaded: %s (%d chars)", file_path.name, len(truncated))

        except Exception as exc:
            logger.warning("Could not extract text from %s: %s", file_path.name, exc)
            continue

    combined = "\n\n".join(chunks)
    return combined[:max_total_chars]
