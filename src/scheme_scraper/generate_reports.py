import argparse
import logging
from pathlib import Path

from .config import load_settings
from .pipeline.report_generator import ReportGenerator

logging.basicConfig(
    level=logging.INFO,
    format=f"%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate 3 standalone markdown reports per scheme.")
    parser.add_argument(
        "--config",
        type=str,
        default="config/settings.yaml",
        help="Path to settings.yaml",
    )
    parser.add_argument(
        "--run-dir",
        type=str,
        required=True,
        help="Path to the finished run directory (e.g. runs/startup_batch_01)",
    )

    args = parser.parse_args()

    run_dir_path = Path(args.run_dir)
    if not run_dir_path.exists():
        logging.error("Run directory does not exist: %s", run_dir_path)
        return

    settings = load_settings(args.config)
    generator = ReportGenerator(settings)
    generator.process_run(run_dir_path)


if __name__ == "__main__":
    main()