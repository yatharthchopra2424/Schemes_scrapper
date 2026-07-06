"""
resume_llm_docs.py
------------------
Smart resume script that handles two cases automatically:

  CASE A - Evidence exists (ai_summary.json or evidence_bundle.json found):
    Runs only the ReportGenerator to create the 9 business .md documents.
    No web crawling. Fast.

  CASE B - No evidence found (crawl was never completed):
    Reads the input CSV, matches the scheme to the artifact dir, then runs
    the full PipelineRunner (crawl + LLM enrichment + report generation)
    for that scheme. Uses the same run directory so output is consistent.

Usage:
    python resume_llm_docs.py                           # auto-detect latest run
    python resume_llm_docs.py --run-id run_20260623_0022
    python resume_llm_docs.py --run-dir runs/run_20260623_0022

Idempotent: any scheme whose 9 docs already exist (> 100 bytes each) is skipped.
Safe to Ctrl+C and re-run at any time.
"""
from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

# ── CLI ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Smart resume: LLM-docs-only for crawled schemes, full pipeline for empty ones.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--run-id", type=str, default=None,
                       help="Run ID (e.g. run_20260623_0022). Default: latest run.")
    group.add_argument("--run-dir", type=Path, default=None,
                       help="Full path to run directory.")
    parser.add_argument("--output-root", type=Path, default=Path("runs"))
    parser.add_argument("--input", type=Path, default=Path("data/input/sample_schemes.csv"),
                        help="Input CSV (needed for no-evidence schemes).")
    parser.add_argument("--config", type=Path, default=Path("config/settings.yaml"))
    parser.add_argument("--workers", type=int, default=None,
                        help="Parallel workers for full-pipeline schemes (default: from config).")
    parser.add_argument("--log-level", default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


# ── Helpers ──────────────────────────────────────────────────────────────────

DOC_NAMES = [
    "report.md",
    "SCHEME_MASTER_DATABASE.md",
    "PITCH_AND_SALES_SCRIPTS.md",
    "APPLICATION_PLAYBOOK.md",
    "CLIENT_ONBOARDING_AND_CRM.md",
    "LIVE_CASE_TRACKER.md",
    "FEE_AND_REVENUE_MODEL.md",
    "CLIENT_PROPOSAL_TEMPLATE.md",
    "COMPLIANCE_AND_LEGAL_PACK.md",
]


def _has_all_docs(scheme_dir: Path) -> bool:
    return all(
        (scheme_dir / f).exists() and (scheme_dir / f).stat().st_size > 100
        for f in DOC_NAMES
    )


def _has_evidence(scheme_dir: Path) -> bool:
    """True if the scheme directory has any usable evidence."""
    if (scheme_dir / "ai_summary.json").exists():
        return True
    if (scheme_dir / "evidence_bundle.json").exists():
        return True
    docs_dir = scheme_dir / "documents"
    if docs_dir.exists() and any(docs_dir.iterdir()):
        return True
    return False


def get_run_dir(args: argparse.Namespace) -> Path:
    if args.run_dir:
        return args.run_dir.resolve()
    if not args.output_root.exists():
        print(f"[ERROR] Output root not found: {args.output_root}", file=sys.stderr)
        sys.exit(1)
    if args.run_id:
        run_dir = args.output_root / args.run_id
        if not run_dir.exists():
            print(f"[ERROR] Run directory not found: {run_dir}", file=sys.stderr)
            sys.exit(1)
        return run_dir
    run_dirs = sorted(
        [d for d in args.output_root.iterdir() if d.is_dir() and d.name.startswith("run_")],
        key=lambda d: d.stat().st_mtime, reverse=True,
    )
    if not run_dirs:
        print(f"[ERROR] No run dirs in: {args.output_root}", file=sys.stderr)
        sys.exit(1)
    latest = run_dirs[0]
    print(f"[INFO] Auto-detected latest run: {latest.name}")
    return latest


def setup_logging(run_dir: Path, log_level: str) -> logging.Logger:
    import io as _io
    logger = logging.getLogger("scheme_scraper")
    logger.handlers.clear()
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)
    fmt = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                            datefmt="%H:%M:%S")
    safe_out = (_io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace", line_buffering=True)
                if hasattr(sys.stdout, "buffer") else sys.stdout)
    ch = logging.StreamHandler(safe_out)
    ch.setFormatter(fmt)
    ch.setLevel(level)
    logger.addHandler(ch)
    run_dir.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(run_dir / "pipeline.log", mode="a", encoding="utf-8")
    fh.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger


# ── Core logic ────────────────────────────────────────────────────────────────

def build_slug_map(input_csv: Path) -> dict[str, object]:
    """
    Load the input CSV and build a map:  dir_name_prefix -> SchemeInput
    where dir_name_prefix = "{row_id}-{slugified_scheme_name}".
    """
    from scheme_scraper.utils import load_scheme_inputs, slugify
    schemes = load_scheme_inputs(input_csv)
    mapping: dict[str, object] = {}
    for s in schemes:
        key = f"{s.row_id}-{slugify(s.scheme_name)}"
        mapping[key] = s
    return mapping


def run_full_pipeline_for_schemes(
    schemes: list,
    run_dir: Path,
    settings,
    logger: logging.Logger,
) -> None:
    """Run crawl + LLM enrichment + report generation for a list of SchemeInput."""
    from scheme_scraper.pipeline.runner import PipelineRunner

    runner = PipelineRunner(
        settings=settings,
        input_csv=Path("data/input/sample_schemes.csv"),   # not actually used when we pass directly
        run_dir=run_dir,
        resume=True,   # existing checkpoint is respected
        skip_llm=False,
        logger=logger,
    )
    # Directly process only the no-evidence schemes
    runner._checkpoint = runner._load_checkpoint()
    runner._rows = {}

    from scheme_scraper.llm.nvidia_client import NvidiaLLMClient
    llm_client = NvidiaLLMClient(settings)

    total = len(schemes)
    for i, scheme in enumerate(schemes, 1):
        logger.info(
            "[%d/%d] Full pipeline (crawl+LLM): %s", i, total, scheme.scheme_name
        )
        try:
            row = runner._process_scheme(scheme, llm_client)
            runner._persist(scheme, row)
        except KeyboardInterrupt:
            logger.warning("Interrupted. Partial results saved. Re-run to continue.")
            raise
        except Exception as exc:
            logger.error("Failed processing %s: %s", scheme.scheme_name, exc)


def run_report_generator(scheme_dirs: list[Path], run_dir: Path, settings, logger: logging.Logger) -> None:
    """Run ReportGenerator (LLM docs only) for schemes that already have evidence."""
    from scheme_scraper.pipeline.report_generator import ReportGenerator

    class _SubsetReportGenerator(ReportGenerator):
        """Only processes the given list of scheme dirs instead of all in artifacts/."""
        def process_subset(self, dirs: list[Path]) -> None:
            logger.info("Generating 9 business docs for %d scheme(s) with evidence...", len(dirs))
            for d in dirs:
                self._process_scheme_dir(d)
            logger.info("All document reports complete.")

    generator = _SubsetReportGenerator(settings)
    generator.process_subset(scheme_dirs)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    load_dotenv()
    args = parse_args()

    run_dir = get_run_dir(args)
    logger = setup_logging(run_dir, args.log_level)

    logger.info("=" * 60)
    logger.info("  SMART RESUME: LLM DOCUMENT GENERATION")
    logger.info("=" * 60)
    logger.info("  Run directory : %s", run_dir)
    logger.info("=" * 60)

    artifacts_dir = run_dir / "artifacts"
    if not artifacts_dir.exists():
        logger.error("No artifacts/ directory in %s -- nothing to process.", run_dir)
        sys.exit(1)

    try:
        from scheme_scraper.config import load_settings
    except ImportError as exc:
        logger.error("Cannot import scheme_scraper: %s\nRun from project root with venv active.", exc)
        sys.exit(1)

    settings = load_settings(args.config)
    if args.workers is not None:
        settings.runtime.parallel_workers = args.workers

    # ── Categorise all scheme dirs ──────────────────────────────────────────
    all_dirs = [d for d in sorted(artifacts_dir.iterdir()) if d.is_dir()]
    logger.info("Found %d scheme artifact directories.", len(all_dirs))

    already_done: list[Path] = []
    has_evidence: list[Path] = []
    needs_crawl_names: list[str] = []   # dir names that need full pipeline

    for d in all_dirs:
        if _has_all_docs(d):
            already_done.append(d)
        elif _has_evidence(d):
            has_evidence.append(d)
        else:
            needs_crawl_names.append(d.name)

    logger.info(
        "  Already complete     : %d  (will skip)",
        len(already_done),
    )
    logger.info(
        "  Has evidence (LLM only) : %d  (will generate docs only)",
        len(has_evidence),
    )
    logger.info(
        "  No evidence (needs full crawl+LLM) : %d",
        len(needs_crawl_names),
    )

    # ── Phase A: LLM docs for evidence-rich schemes ─────────────────────────
    if has_evidence:
        logger.info("=" * 60)
        logger.info("  PHASE A: Generating docs for evidence-rich schemes")
        logger.info("=" * 60)
        try:
            run_report_generator(has_evidence, run_dir, settings, logger)
        except KeyboardInterrupt:
            logger.warning("Interrupted in Phase A. Re-run to continue.")
            sys.exit(1)

    # ── Phase B: Full pipeline for no-evidence schemes ──────────────────────
    if needs_crawl_names:
        logger.info("=" * 60)
        logger.info("  PHASE B: Full crawl+LLM for %d scheme(s) with no evidence", len(needs_crawl_names))
        logger.info("  (Loading input CSV to match scheme URLs...)")
        logger.info("=" * 60)

        if not args.input.exists():
            logger.error(
                "Input CSV not found: %s\n"
                "Pass --input <path> to specify it, or ensure data/input/sample_schemes.csv exists.",
                args.input,
            )
            sys.exit(1)

        slug_map = build_slug_map(args.input)

        # Match artifact dir names to SchemeInput objects
        matched: list = []
        unmatched: list[str] = []
        for dir_name in needs_crawl_names:
            if dir_name in slug_map:
                matched.append(slug_map[dir_name])
            else:
                # Fallback: fuzzy prefix match (handles truncated slugs)
                found = None
                for key, scheme in slug_map.items():
                    if dir_name.startswith(key[:30]) or key.startswith(dir_name[:30]):
                        found = scheme
                        break
                if found:
                    matched.append(found)
                else:
                    unmatched.append(dir_name)

        if unmatched:
            logger.warning(
                "Could not match %d scheme dir(s) to CSV rows: %s",
                len(unmatched), unmatched[:5],
            )

        if matched:
            logger.info("Matched %d scheme(s) to input CSV. Starting full pipeline...", len(matched))
            t0 = time.perf_counter()
            try:
                run_full_pipeline_for_schemes(matched, run_dir, settings, logger)
            except KeyboardInterrupt:
                logger.warning("Interrupted in Phase B. Re-run to continue.")
                sys.exit(1)
            elapsed = time.perf_counter() - t0
            logger.info("Phase B complete in %.1fs", elapsed)

    if not has_evidence and not needs_crawl_names:
        logger.info("Nothing to do -- all %d schemes already have complete documentation.", len(already_done))

    logger.info("=" * 60)
    logger.info("  RESUME COMPLETE")
    logger.info("  Output: %s", run_dir / "artifacts")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
