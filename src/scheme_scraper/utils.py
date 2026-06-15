from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from .models import SchemeInput


def slugify(value: str, max_length: int = 80) -> str:
    lowered = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    return slug[:max_length] or "item"


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def canonicalize_url(raw_url: str) -> str:
    parsed = urlparse(raw_url.strip())
    if not parsed.scheme or not parsed.netloc:
        return raw_url.strip()
    netloc = parsed.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    cleaned_query = urlencode(sorted(parse_qsl(parsed.query, keep_blank_values=True)))
    canonical = parsed._replace(netloc=netloc, query=cleaned_query, fragment="")
    return urlunparse(canonical)


def same_domain(url_a: str, url_b: str) -> bool:
    a = urlparse(canonicalize_url(url_a)).netloc
    b = urlparse(canonicalize_url(url_b)).netloc
    return bool(a and b and a == b)


def sha256_bytes(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def detect_delimiter(sample: str) -> str:
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;")
        return dialect.delimiter
    except csv.Error:
        return ","


def load_scheme_inputs(csv_path: Path) -> list[SchemeInput]:
    import logging
    
    encodings_to_try = ["utf-8-sig", "windows-1252", "latin-1"]
    used_encoding = "utf-8-sig"
    
    for enc in encodings_to_try:
        try:
            text = csv_path.read_text(encoding=enc)
            used_encoding = enc
            break
        except UnicodeDecodeError:
            continue
    else:
        text = csv_path.read_text(encoding="utf-8-sig", errors="replace")
        used_encoding = "utf-8-sig"

    delimiter = detect_delimiter(text[:2048])

    rows: list[SchemeInput] = []
    with csv_path.open("r", encoding=used_encoding, errors="replace", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        
        if not reader.fieldnames:
            raise ValueError("Input CSV is empty or has no headers.")

        # Clean headers: lowercase and strip whitespace to ensure match
        cleaned_headers = [str(h).strip().lower() for h in reader.fieldnames]
        
        required = {"ministry_or_category", "scheme_name", "scheme_url"}
        if not required.issubset(set(cleaned_headers)):
            raise ValueError(
                f"Input CSV must include headers: {', '.join(required)}. "
                f"Found headers: {', '.join(cleaned_headers)}"
            )

        # Update reader's fieldnames to the cleaned versions
        reader.fieldnames = cleaned_headers

        for idx, row in enumerate(reader, start=1):
            ministry = (row.get("ministry_or_category") or "").strip()
            name = (row.get("scheme_name") or "").strip()
            url = (row.get("scheme_url") or "").strip()
            
            # Skip completely empty rows
            if not ministry and not name and not url:
                continue
                
            # Log and skip if missing required data, instead of silently continuing
            if not (ministry and name and url):
                logging.getLogger(__name__).warning("Row %d has missing data. Skipping.", idx + 1)
                continue

            rows.append(
                SchemeInput(
                    row_id=f"row-{idx}",
                    ministry_or_category=ministry,
                    scheme_name=name,
                    scheme_url=url,
                )
            )

    if not rows:
        raise ValueError("No valid rows were found in the input CSV.")

    return rows


def dedupe_preserve_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out
