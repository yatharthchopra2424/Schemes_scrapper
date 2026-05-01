"""
Application configuration — settings loading with YAML + environment overrides.

Additions from v1:
  - RuntimeSettings: parallel_workers, log_level, log_file
  - CrawlerSettings: disable_images flag
  - AppSettings now includes RuntimeSettings
  - All ENV overrides properly handled
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class CrawlerSettings(BaseModel):
    browser: str = "chrome"
    headless: bool = True
    page_load_timeout_seconds: int = 45
    render_wait_seconds: float = 2.0
    max_depth: int = 2
    max_pages_per_scheme: int = 15
    max_documents_per_scheme: int = 10    # Cap on documents downloaded per scheme
    user_agent: str = "SchemeScraperBot/1.0"
    disable_images: bool = True           # Disable image loading for speed


class ComplianceSettings(BaseModel):
    strict_mode: bool = True
    min_delay_seconds: float = 2.0
    request_timeout_seconds: int = 20


class DocumentSettings(BaseModel):
    enable_extraction: bool = True
    max_document_mb: int = 15


class LLMSettings(BaseModel):
    provider: str = "nvidia_openai_compat"
    base_url: str = "https://integrate.api.nvidia.com/v1"
    model: str = "meta/llama-3.3-70b-instruct"
    temperature: float = 0.2
    top_p: float = 0.95
    max_tokens: int = 8192
    timeout_seconds: int = 120
    max_retries: int = 3


class RuntimeSettings(BaseModel):
    """Runtime-only settings (not persisted in output)."""
    parallel_workers: int = 2            # Number of concurrent Chrome + LLM workers
    log_level: str = "INFO"
    log_to_file: bool = True             # Write pipeline.log to run directory


class OutputSettings(BaseModel):
    root_dir: str = "runs"
    enriched_csv_name: str = "enriched_schemes.csv"
    checkpoint_name: str = "checkpoint.json"


class VectorDBSettings(BaseModel):
    index_name: str = "infou-scheme-index"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    chunk_size: int = 1000
    chunk_overlap: int = 100


class AppSettings(BaseModel):
    crawler: CrawlerSettings = Field(default_factory=CrawlerSettings)
    compliance: ComplianceSettings = Field(default_factory=ComplianceSettings)
    documents: DocumentSettings = Field(default_factory=DocumentSettings)
    llm: LLMSettings = Field(default_factory=LLMSettings)
    runtime: RuntimeSettings = Field(default_factory=RuntimeSettings)
    output: OutputSettings = Field(default_factory=OutputSettings)
    vector_db: VectorDBSettings = Field(default_factory=VectorDBSettings)


# Environment variable override map:  ENV_NAME → (section, key, type_caster)
ENV_OVERRIDES: dict[str, tuple[str, str, Any]] = {
    "SCRAPER_HEADLESS":              ("crawler",  "headless",              lambda v: v.lower() == "true"),
    "SCRAPER_MAX_DEPTH":             ("crawler",  "max_depth",             int),
    "SCRAPER_MAX_PAGES_PER_SCHEME":  ("crawler",  "max_pages_per_scheme",  int),
    "SCRAPER_DISABLE_IMAGES":        ("crawler",  "disable_images",        lambda v: v.lower() == "true"),
    "SCRAPER_PARALLEL_WORKERS":      ("runtime",  "parallel_workers",       int),
    "SCRAPER_LOG_LEVEL":             ("runtime",  "log_level",             str),
}


def _set_nested(dct: dict[str, Any], section: str, key: str, value: Any) -> None:
    if section not in dct or not isinstance(dct[section], dict):
        dct[section] = {}
    dct[section][key] = value


def load_settings(config_path: str | Path | None = None) -> AppSettings:
    config_file = Path(
        config_path or os.environ.get("SCRAPER_CONFIG_PATH", "config/settings.yaml")
    )

    payload: dict[str, Any] = {}
    if config_file.exists():
        with config_file.open("r", encoding="utf-8") as fh:
            raw = yaml.safe_load(fh) or {}
            if isinstance(raw, dict):
                payload.update(raw)

    for env_name, (section, key, caster) in ENV_OVERRIDES.items():
        raw_value = os.getenv(env_name)
        if raw_value is None:
            continue
        try:
            _set_nested(payload, section, key, caster(raw_value))
        except (ValueError, TypeError):
            pass  # Silently ignore bad env values

    # Remove any non-model sections that YAML may have injected
    for extra_key in list(payload.keys()):
        if extra_key not in AppSettings.model_fields:
            payload.pop(extra_key, None)

    settings = AppSettings.model_validate(payload)

    # Basic validation
    if settings.crawler.max_depth < 0:
        raise ValueError("crawler.max_depth must be >= 0")
    if settings.crawler.max_pages_per_scheme < 1:
        raise ValueError("crawler.max_pages_per_scheme must be >= 1")
    if settings.runtime.parallel_workers < 1:
        raise ValueError("runtime.parallel_workers must be >= 1")

    return settings
