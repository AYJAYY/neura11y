#!/usr/bin/env python3
"""
Fetch ISO-adjacent free summaries:
  - PDF/UA (ISO 14289-1) overview from the PDF Association
  - Matterhorn Protocol 1.1 from the PDF Association

Note: The full ISO 14289-1 standard requires purchase from ISO.
This script fetches only the freely available summary page and the
Matterhorn Protocol PDF (which is freely distributed by the PDF Association).

Requirements:
  pip install requests beautifulsoup4 markdownify pdfplumber python-frontmatter

Usage:
  python scripts/fetch-iso.py
  python scripts/fetch-iso.py --delay 3
  python scripts/fetch-iso.py --source pdf-ua       # Only PDF/UA summary
  python scripts/fetch-iso.py --source matterhorn   # Only Matterhorn Protocol

See meta/update-schedule.md: annually or on new PDF Association publication.
See meta/standards-registry.md for source URLs and target files.
"""

import argparse
import datetime
import io
import re
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import requests
    from bs4 import BeautifulSoup
    import markdownify
    import pdfplumber
    import frontmatter
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install requests beautifulsoup4 markdownify pdfplumber python-frontmatter")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent

HEADERS = {
    "User-Agent": "claude-a11y-repo/1.0 (accessibility knowledge base; educational use)"
}

REQUEST_DELAY = 2.0

SOURCES = {
    "pdf-ua": {
        "type": "html",
        "url": "https://pdfa.org/resource/iso-14289-pdfua/",
        "output": "standards/pdf-ua/pdf-ua-overview.md",
        "selector": "main",
        "skip_selectors": ["nav", "header", "footer", ".sidebar"],
        "frontmatter": {
            "title": "PDF/UA (ISO 14289-1) Overview",
            "standard": "PDF/UA (ISO 14289-1:2014)",
            "source_url": "https://pdfa.org/resource/iso-14289-pdfua/",
            "domain": ["documents"],
            "status": "normative",
            "tags": ["pdf-ua", "pdf", "iso-14289", "documents"],
            "ai_context": (
                "PDF/UA (ISO 14289-1:2014) overview from the PDF Association. "
                "Defines requirements for universally accessible PDF documents. "
                "Note: Full ISO standard requires purchase; this is the free summary. "
                "Use alongside matterhorn-protocol.md for PDF accessibility conformance checking."
            ),
        },
    },
    "matterhorn": {
        "type": "pdf",
        "url": "https://pdfa.org/resource/the-matterhorn-protocol/",
        # The resource page links to the PDF — we fetch the page to find the PDF link,
        # then download and extract the PDF.
        "output": "standards/pdf-ua/matterhorn-protocol.md",
        "frontmatter": {
            "title": "Matterhorn Protocol 1.1 — PDF/UA Conformance Checking",
            "standard": "Matterhorn Protocol 1.1",
            "source_url": "https://pdfa.org/resource/the-matterhorn-protocol/",
            "domain": ["documents"],
            "status": "normative",
            "tags": ["matterhorn", "pdf-ua", "pdf", "conformance", "documents"],
            "ai_context": (
                "Matterhorn Protocol 1.1 from the PDF Association. "
                "Defines 136 failure conditions for PDF/UA (ISO 14289-1) conformance. "
                "Each failure condition maps to a PDF/UA clause and is categorised as "
                "machine-checkable or requiring human inspection. "
                "Use when advising on PDF accessibility audit procedures."
            ),
        },
    },
}


# ─────────────────────────────────────────────
# HTML FETCH (PDF/UA summary page)
# ─────────────────────────────────────────────

def fetch_html(url: str, delay: float) -> Optional[str]:
    print(f"  Fetching HTML: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        response.encoding = "utf-8"
        time.sleep(delay)
        return response.text
    except requests.RequestException as e:
        print(f"  ERROR: {e}")
        return None


def html_to_markdown(html: str, selector: str, skip_selectors: list) -> str:
    soup = BeautifulSoup(html, "html.parser")
    content_el = soup.select_one(selector) or soup.body or soup
    if skip_selectors:
        for sel in skip_selectors:
            for el in content_el.select(sel):
                el.decompose()
    md = markdownify.markdownify(
        str(content_el),
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
        convert_as_inline=["a"],
    )
    return re.sub(r"\n{3,}", "\n\n", md).strip()


# ─────────────────────────────────────────────
# PDF FETCH (Matterhorn Protocol)
# ─────────────────────────────────────────────

def find_pdf_link(page_url: str, delay: float) -> Optional[str]:
    """Load the resource page and find the first .pdf link."""
    html = fetch_html(page_url, delay)
    if not html:
        return None
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.lower().endswith(".pdf"):
            if href.startswith("http"):
                return href
            # Relative URL
            from urllib.parse import urljoin
            return urljoin(page_url, href)
    return None


def download_pdf(url: str, delay: float) -> Optional[bytes]:
    print(f"  Downloading PDF: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=120, stream=True)
        response.raise_for_status()
        data = response.content
        print(f"  Downloaded {len(data) / 1024:.0f} KB")
        time.sleep(delay)
        return data
    except requests.RequestException as e:
        print(f"  ERROR: {e}")
        return None


def pdf_to_markdown(pdf_bytes: bytes) -> str:
    """Extract text from PDF and lightly convert to Markdown."""
    pages_text = []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        total = len(pdf.pages)
        print(f"  Extracting text from {total} pages...")
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)

    raw = "\n".join(pages_text)

    # Basic cleanup
    raw = re.sub(r"\n{3,}", "\n\n", raw)

    # Promote lines that look like numbered section headings
    lines = raw.splitlines()
    md_lines = []
    for line in lines:
        stripped = line.strip()
        # e.g. "1 Introduction" or "2.1 Scope"
        if re.match(r"^\d+(\.\d+)*\s{2,}[A-Z]", stripped):
            depth = stripped.split()[0].count(".")
            hashes = "#" * min(depth + 2, 5)
            md_lines.append(f"\n{hashes} {stripped}")
        else:
            md_lines.append(stripped)

    md = "\n".join(md_lines)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


# ─────────────────────────────────────────────
# COMMON OUTPUT
# ─────────────────────────────────────────────

def apply_frontmatter(content: str, fm_data: dict) -> str:
    post = frontmatter.Post(content, **fm_data)
    return frontmatter.dumps(post)


def write_output(content: str, output_path: str) -> None:
    full_path = REPO_ROOT / output_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8")
    lines = content.count("\n")
    print(f"  Written: {output_path} ({lines} lines)")
    if lines > 2000:
        print(f"  WARNING: file exceeds 2000 lines. Consider splitting.")


def fetch_source(key: str, config: dict, delay: float) -> bool:
    print(f"\nFetching: {key}")
    source_type = config["type"]

    if source_type == "html":
        html = fetch_html(config["url"], delay)
        if not html:
            return False
        markdown = html_to_markdown(
            html, config["selector"], config.get("skip_selectors", [])
        )

    elif source_type == "pdf":
        # Find the PDF download link on the resource page, then download
        pdf_url = find_pdf_link(config["url"], delay)
        if not pdf_url:
            print(f"  Could not find a .pdf link on {config['url']}")
            print("  Falling back to fetching the page as HTML instead.")
            html = fetch_html(config["url"], delay)
            if not html:
                return False
            markdown = html_to_markdown(
                html, "main", ["nav", "header", "footer", ".sidebar"]
            )
        else:
            pdf_bytes = download_pdf(pdf_url, delay)
            if not pdf_bytes:
                return False
            markdown = pdf_to_markdown(pdf_bytes)

    else:
        print(f"  Unknown source type: {source_type}")
        return False

    fm = config["frontmatter"].copy()
    fm["last_fetched"] = datetime.date.today().isoformat()

    content = apply_frontmatter(markdown, fm)
    write_output(content, config["output"])
    return True


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Fetch ISO/PDF Association free summaries (PDF/UA, Matterhorn Protocol)"
    )
    parser.add_argument(
        "--source", choices=list(SOURCES.keys()),
        help="Fetch a specific source only"
    )
    parser.add_argument(
        "--delay", type=float, default=REQUEST_DELAY,
        help=f"Delay between requests in seconds (default: {REQUEST_DELAY})"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List available sources"
    )
    args = parser.parse_args()

    if args.list:
        print("Available sources:")
        for key, config in SOURCES.items():
            print(f"  {key:20s} → {config['output']}")
        return

    keys = [args.source] if args.source else list(SOURCES.keys())

    success = 0
    failed = []
    for key in keys:
        try:
            if fetch_source(key, SOURCES[key], args.delay):
                success += 1
            else:
                failed.append(key)
        except Exception as e:
            print(f"  EXCEPTION fetching {key}: {e}")
            failed.append(key)

    print(f"\n{'='*50}")
    print(f"Fetch complete: {success} succeeded, {len(failed)} failed")
    if failed:
        print(f"Failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
