"""
Pipeline entry point — argument parsing, logging setup, run orchestration.

Improvements over v1:
  - File logging to runs/<run_id>/pipeline.log (always enabled — persists after CMD closes)
  - Colourised stream output using simple ANSI codes (no extra dependencies)
  - Startup banner with key config values, API key status, Python version
  - Overall elapsed time and per-scheme summary at completion
  - Automatic timestamped run-id if --run-id is not specified
  - Graceful keyboard interrupt handling
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from .config import load_settings
from .pipeline.runner import PipelineRunner


# ── Colourised formatter ───────────────────────────────────────────────────────

class _ColourFormatter(logging.Formatter):
    """ANSI colour codes for Windows console (works in Windows Terminal)."""
    COLOURS = {
        logging.DEBUG:    "\033[36m",   # Cyan
        logging.INFO:     "\033[32m",   # Green
        logging.WARNING:  "\033[33m",   # Yellow
        logging.ERROR:    "\033[31m",   # Red
        logging.CRITICAL: "\033[35m",   # Magenta
    }
    RESET = "\033[0m"
    FMT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

    def format(self, record: logging.LogRecord) -> str:
        colour = self.COLOURS.get(record.levelno, "")
        formatter = logging.Formatter(f"{colour}{self.FMT}{self.RESET}", datefmt="%H:%M:%S")
        return formatter.format(record)


def configure_logging(run_dir: Path, log_level: str = "INFO") -> logging.Logger:
    """
    Set up:
      1. Colourised StreamHandler → stdout
      2. FileHandler → run_dir/pipeline.log (plain text, full timestamps)
    """
    root_logger = logging.getLogger("scheme_scraper")
    if root_logger.handlers:
        root_logger.handlers.clear()

    level = getattr(logging, log_level.upper(), logging.INFO)
    root_logger.setLevel(level)

    # Fix Windows CMD encoding: wrap stdout in UTF-8 with replace fallback
    import io as _io
    if hasattr(sys.stdout, 'buffer'):
        safe_stdout = _io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace', line_buffering=True)
    else:
        safe_stdout = sys.stdout

    # Stream handler (colourised)
    stream_handler = logging.StreamHandler(safe_stdout)
    stream_handler.setFormatter(_ColourFormatter())
    stream_handler.setLevel(level)
    root_logger.addHandler(stream_handler)

    # File handler (plain text, everything including DEBUG)
    run_dir.mkdir(parents=True, exist_ok=True)
    log_file = run_dir / "pipeline.log"
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    file_handler.setLevel(logging.DEBUG)   # Log everything to file
    root_logger.addHandler(file_handler)

    return root_logger


# ── Argument parsing ───────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Infou Scheme Intelligence Scraper — NVIDIA LLM enrichment pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/input/sample_schemes.csv"),
        help="Path to input CSV with ministry_or_category, scheme_name, scheme_url",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/settings.yaml"),
        help="Path to YAML settings file (default: config/settings.yaml)",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("runs"),
        help="Root directory for run outputs (default: runs/)",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        default=None,
        help="Run ID (default: auto-generated timestamp like run_20260418_1527)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from checkpoint — skip schemes already marked 'completed'",
    )
    parser.add_argument(
        "--max-schemes",
        type=int,
        default=None,
        help="Optional limit on number of schemes to process (useful for testing)",
    )
    parser.add_argument(
        "--skip-llm",
        action="store_true",
        help="Crawl only — skip NVIDIA LLM enrichment (fast mode for debugging)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Override parallel_workers from config (e.g. --workers 3)",
    )
    return parser.parse_args()


# ── Startup banner ─────────────────────────────────────────────────────────────

def _print_banner(logger: logging.Logger, settings, run_dir: Path, input_csv: Path) -> None:
    api_key = os.environ.get("NVIDIA_API_KEY", "")
    key_status = f"SET ({api_key[:8]}...)" if api_key else "MISSING ⚠"
    logger.info("=" * 60)
    logger.info("  INFOU SCHEME INTELLIGENCE PIPELINE")
    logger.info("=" * 60)
    logger.info("  Python        : %s", sys.version.split()[0])
    logger.info("  Input CSV     : %s", input_csv)
    logger.info("  Run Directory : %s", run_dir)
    logger.info("  Log File      : %s", run_dir / "pipeline.log")
    logger.info("  Model         : %s", settings.llm.model)
    logger.info("  Workers       : %d", settings.runtime.parallel_workers)
    logger.info("  Headless      : %s", settings.crawler.headless)
    logger.info("  Images Off    : %s", settings.crawler.disable_images)
    logger.info("  Max Pages     : %d/scheme", settings.crawler.max_pages_per_scheme)
    logger.info("  NVIDIA Key    : %s", key_status)
    logger.info("=" * 60)


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    load_dotenv()
    args = parse_args()

    # Auto-generate run ID if not provided
    run_id = args.run_id or f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    settings = load_settings(args.config)

    # CLI override for workers
    if args.workers is not None:
        settings.runtime.parallel_workers = args.workers

    run_dir = args.output_root / run_id
    logger = configure_logging(run_dir, settings.runtime.log_level)

    _print_banner(logger, settings, run_dir, args.input)

    t_pipeline_start = time.perf_counter()

    runner = PipelineRunner(
        settings=settings,
        input_csv=args.input,
        run_dir=run_dir,
        resume=args.resume,
        skip_llm=args.skip_llm,
        logger=logger,
    )

    try:
        enriched_csv_path = runner.run(max_schemes=args.max_schemes)
    except KeyboardInterrupt:
        logger.warning("Pipeline interrupted by user. Partial results saved to checkpoint.")
        sys.exit(1)
    except Exception as exc:
        logger.critical("Pipeline failed with unhandled exception: %s", exc, exc_info=True)
        sys.exit(2)

    # Post-crawl report generation (pitch / how-to / summary)
    if not args.skip_llm:
        logger.info("=" * 60)
        logger.info("  PHASE 2: Generating supplementary Markdown reports...")
        logger.info("=" * 60)
        try:
            from .pipeline.report_generator import ReportGenerator
            generator = ReportGenerator(settings)
            generator.process_run(run_dir)
        except Exception as exc:
            logger.error("Supplementary report generation failed: %s", exc, exc_info=True)

    elapsed_total = time.perf_counter() - t_pipeline_start

    logger.info("=" * 60)
    logger.info("  PIPELINE COMPLETE")
    logger.info("  Total elapsed   : %.1f seconds (%.1f minutes)", elapsed_total, elapsed_total / 60)
    logger.info("  Enriched CSV    : %s", enriched_csv_path)
    logger.info("  Artifacts       : %s/artifacts/", run_dir)
    logger.info("  Full log        : %s/pipeline.log", run_dir)
    logger.info("=" * 60)

    # Print inline summary to stdout
    _print_run_summary(enriched_csv_path, logger)


def _print_run_summary(csv_path: Path, logger: logging.Logger) -> None:
    """Print a quick per-scheme status table to the log."""
    try:
        import csv
        if not csv_path.exists():
            return
        with csv_path.open("r", encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
        if not rows:
            return

        logger.info("\n  %-40s %-10s %-6s %-10s", "SCHEME", "STATUS", "CONF", "TIME(s)")
        logger.info("  " + "-" * 70)
        for row in rows:
            name = (row.get("scheme_name") or "")[:38]
            status = row.get("status", "?")
            conf = row.get("confidence", "?")
            elapsed = row.get("elapsed_seconds", "?")
            logger.info("  %-40s %-10s %-6s %-10s", name, status, conf, elapsed)
    except Exception:
        pass


if __name__ == "__main__":
    main()
