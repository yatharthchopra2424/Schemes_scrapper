from scheme_scraper.extract.html_extract import extract_links, extract_visible_text


HTML_SAMPLE = """
<html>
  <head><title>Test</title><style>.x {color:red;}</style></head>
  <body>
    <script>console.log('ignore')</script>
    <h1>Scheme</h1>
    <p>Important details</p>
    <a href="/apply">Apply</a>
    <a href="/docs/guideline.pdf">Guideline</a>
  </body>
</html>
"""


def test_extract_visible_text_excludes_script_and_style() -> None:
    text = extract_visible_text(HTML_SAMPLE)
    assert "Important details" in text
    assert "console.log" not in text


def test_extract_links_splits_pages_and_documents() -> None:
    links, docs = extract_links(HTML_SAMPLE, "https://example.gov.in/scheme")
    assert "https://example.gov.in/apply" in links
    assert "https://example.gov.in/docs/guideline.pdf" in docs
