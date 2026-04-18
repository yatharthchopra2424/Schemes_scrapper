"""
Post-run Pipeline Health Dashboard

Usage:
    python -m scheme_scraper.pipeline.pipeline_summary --run-dir runs/run_20260418_1527

Prints a rich, colourised summary table of all schemes processed in a run.
Flags low-confidence rows for manual review.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def _bar(value: float, max_val: float, width: int = 10) -> str:
    if max_val == 0:
        return " " * width
    filled = int((value / max_val) * width)
    return "█" * filled + "░" * (width - filled)


def _confidence_icon(conf: str) -> str:
    return {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(conf.lower(), "⚪")


def _status_icon(status: str) -> str:
    return {"completed": "✔", "failed": "✘"}.get(status.lower(), "?")


def print_summary(run_dir: Path) -> None:
    csv_path = run_dir / "enriched_schemes.csv"
    log_path = run_dir / "pipeline.log"

    if not csv_path.exists():
        print(f"[ERROR] No enriched_schemes.csv found in {run_dir}", file=sys.stderr)
        sys.exit(1)

    with csv_path.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    if not rows:
        print("[INFO] No rows found in CSV.", file=sys.stderr)
        return

    # Aggregate stats
    total = len(rows)
    completed = sum(1 for r in rows if r.get("status") == "completed")
    failed = total - completed
    high_conf = sum(1 for r in rows if r.get("confidence") == "high")
    medium_conf = sum(1 for r in rows if r.get("confidence") == "medium")
    low_conf = sum(1 for r in rows if r.get("confidence") == "low")

    elapseds = []
    for r in rows:
        try:
            elapseds.append(float(r.get("elapsed_seconds") or 0))
        except ValueError:
            pass
    total_time = sum(elapseds)
    avg_time = total_time / len(elapseds) if elapseds else 0

    max_pages = max((int(r.get("pages_crawled") or 0) for r in rows), default=1)

    print()
    print("═" * 80)
    print("  INFOU SCHEME SCRAPER — RUN SUMMARY")
    print("═" * 80)
    print(f"  Run Directory : {run_dir}")
    if log_path.exists():
        print(f"  Log File      : {log_path}")
    print(f"  Total Schemes : {total}  |  ✔ Completed: {completed}  |  ✘ Failed: {failed}")
    print(f"  Confidence    : 🟢 High: {high_conf}  🟡 Medium: {medium_conf}  🔴 Low: {low_conf}")
    print(f"  Timing        : Total {total_time:.0f}s | Avg {avg_time:.0f}s/scheme")
    print("─" * 80)
    print(
        f"  {'#':<3} {'SCHEME NAME':<35} {'ST':<2} {'CONF':<5} {'PG':<3} {'DOC':<3} "
        f"{'CRAWL PAGES':12} {'TIME':>6}"
    )
    print("─" * 80)

    needs_review: list[str] = []
    for i, row in enumerate(rows, 1):
        name = (row.get("scheme_name") or "")[:33]
        status = _status_icon(row.get("status", ""))
        conf = row.get("confidence", "?")
        conf_icon = _confidence_icon(conf)
        pages = row.get("pages_crawled") or "0"
        docs = row.get("documents_found") or "0"
        try:
            elapsed = f"{float(row.get('elapsed_seconds') or 0):.0f}s"
        except ValueError:
            elapsed = "?"
        try:
            page_bar = _bar(int(pages), max_pages)
        except ValueError:
            page_bar = " " * 10

        print(
            f"  {i:<3} {name:<35} {status:<2} {conf_icon}{conf:<4} {pages:<3} {docs:<3} "
            f"{page_bar}  {elapsed:>6}"
        )

        if conf.lower() == "low" or row.get("status") == "failed":
            needs_review.append(row.get("scheme_name", f"row-{i}"))

    print("─" * 80)

    if needs_review:
        print(f"\n  ⚠ NEEDS MANUAL REVIEW ({len(needs_review)} scheme(s)):")
        for name in needs_review:
            print(f"    • {name}")

    print()
    print(f"  Enriched CSV  : {run_dir / 'enriched_schemes.csv'}")
    print(f"  Artifacts     : {run_dir / 'artifacts'}/")
    print("═" * 80)
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a post-run pipeline health summary.")
    parser.add_argument(
        "--run-dir",
        type=Path,
        required=True,
        help="Path to completed run directory (e.g. runs/run_20260418_1527)",
    )
    args = parser.parse_args()
    print_summary(args.run_dir)


if __name__ == "__main__":
    main()
