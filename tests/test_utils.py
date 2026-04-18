from pathlib import Path

from scheme_scraper.utils import canonicalize_url, load_scheme_inputs, same_domain, slugify


def test_slugify_basic() -> None:
    assert slugify("Startup India Seed Fund Scheme") == "startup-india-seed-fund-scheme"


def test_canonicalize_url_normalizes_www_and_fragment() -> None:
    raw = "https://www.Example.com/path?a=2&b=1#section"
    assert canonicalize_url(raw) == "https://example.com/path?a=2&b=1"


def test_same_domain() -> None:
    assert same_domain("https://www.example.com/a", "https://example.com/b")
    assert not same_domain("https://example.com", "https://other.com")


def test_load_scheme_inputs_tab_delimited(tmp_path: Path) -> None:
    csv_path = tmp_path / "input.tsv"
    csv_path.write_text(
        "ministry_or_category\tscheme_name\tscheme_url\n"
        "Cat\tName\thttps://example.com\n",
        encoding="utf-8",
    )
    rows = load_scheme_inputs(csv_path)
    assert len(rows) == 1
    assert rows[0].scheme_name == "Name"
