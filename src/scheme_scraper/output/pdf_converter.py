import asyncio
import logging
import os
from pathlib import Path

import markdown
from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)

# Basic CSS for the PDF styling to ensure it looks professional and "dark-minimalist" style as requested
PDF_CSS = """
body {
    font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #333;
    line-height: 1.6;
    margin: 40px auto;
    max-width: 800px;
}
h1 {
    color: #1a1a1a;
    border-bottom: 2px solid #eaeaea;
    padding-bottom: 10px;
}
h2 {
    color: #2c3e50;
    margin-top: 30px;
}
h3 {
    color: #34495e;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    margin-bottom: 20px;
}
table, th, td {
    border: 1px solid #ddd;
}
th, td {
    padding: 12px;
    text-align: left;
}
th {
    background-color: #f8f9fa;
    color: #333;
}
strong {
    color: #000;
}
"""

async def _convert_html_to_pdf(html_content: str, output_path: Path) -> None:
    """Uses Playwright (browser-based, Puppeteer equivalent) to convert HTML to PDF."""
    async with async_playwright() as p:
        # Launch Chromium headless
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Set the HTML content
        await page.set_content(html_content, wait_until="networkidle")
        
        # Add basic CSS
        await page.add_style_tag(content=PDF_CSS)
        
        # Generate PDF
        await page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            margin={"top": "20px", "right": "20px", "bottom": "20px", "left": "20px"}
        )
        
        await browser.close()

def generate_pdf_from_markdown(md_file_path: Path, output_pdf_path: Path) -> None:
    """
    Reads a Markdown file, converts it to HTML, and then to PDF using a headless browser.
    """
    if not md_file_path.exists():
        logger.error("Markdown file %s does not exist.", md_file_path)
        return

    logger.info("Converting %s to PDF...", md_file_path.name)
    try:
        md_text = md_file_path.read_text(encoding="utf-8")
        
        # Convert Markdown to HTML (using extensions for tables, fended code, etc.)
        html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
        
        full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>{html_body}</body></html>"
        
        # Ensure output directory exists
        output_pdf_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Run async playwright function
        asyncio.run(_convert_html_to_pdf(full_html, output_pdf_path))
        
        logger.info("Successfully generated PDF: %s", output_pdf_path)
    except Exception as e:
        logger.error("Failed to generate PDF for %s: %s", md_file_path.name, e)
