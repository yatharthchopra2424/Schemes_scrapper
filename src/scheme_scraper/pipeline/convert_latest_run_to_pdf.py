import os
import glob
from pathlib import Path
import logging

from src.scheme_scraper.output.pdf_converter import generate_pdf_from_markdown

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-8s | %(message)s")
logger = logging.getLogger("pdf_batch_converter")

def get_latest_run_dir(runs_dir: str = "runs") -> Path:
    runs_path = Path(runs_dir)
    if not runs_path.exists():
        raise FileNotFoundError(f"Runs directory '{runs_dir}' not found.")
        
    # Get all run directories (e.g., run_20260520_1423)
    subdirs = [d for d in runs_path.iterdir() if d.is_dir() and d.name.startswith("run_")]
    
    if not subdirs:
        raise FileNotFoundError(f"No run directories found in '{runs_dir}'.")
        
    # Sort by creation time or name. Since format is run_YYYYMMDD_HHMM, sorting by name works perfectly
    latest_run = sorted(subdirs)[-1]
    return latest_run

def convert_latest_run_pdfs():
    try:
        latest_run = get_latest_run_dir()
        logger.info(f"Targeting latest run directory: {latest_run}")
        
        # Find all markdown files in the artifacts directory of the latest run
        md_files = list(latest_run.rglob("*.md"))
        
        if not md_files:
            logger.warning(f"No .md files found in {latest_run}")
            return
            
        logger.info(f"Found {len(md_files)} Markdown files. Starting conversion...")
        
        pdf_base_dir = latest_run / "pdfs"
        logger.info(f"PDFs will be saved to: {pdf_base_dir}")
        
        success_count = 0
        for md_path in md_files:
            # Calculate relative path to maintain structure
            rel_path = md_path.relative_to(latest_run)
            pdf_path = pdf_base_dir / rel_path.with_suffix('.pdf')
            
            # Ensure subdirectory exists
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            
            logger.info(f"Converting: {md_path.name} -> {pdf_path}")
            try:
                generate_pdf_from_markdown(md_path, pdf_path)
                success_count += 1
            except Exception as e:
                logger.error(f"Failed to convert {md_path.name}: {e}")
                
        logger.info(f"Conversion complete! Successfully generated {success_count}/{len(md_files)} PDFs.")
        
    except Exception as e:
        logger.error(f"Batch conversion failed: {e}")

if __name__ == "__main__":
    convert_latest_run_pdfs()
