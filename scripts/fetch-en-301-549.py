#!/usr/bin/env python3
"""
Fetch EN 301 549 v3.2.1 — European ICT accessibility standard.

EN 301 549 is distributed as a PDF by ETSI. This script downloads the PDF,
extracts the text with pdfplumber, and writes a structured Markdown file to
standards/en-301-549/en-301-549-requirements.md.

Requirements:
  pip install requests pdfplumber python-frontmatter

Usage:
  python scripts/fetch-en-301-549.py
  python scripts/fetch-en-301-549.py --delay 3

See meta/update-schedule.md: trigger is new ETSI publication.
See meta/standards-registry.md for source URL and target file.
"""

import argparse
import datetime
import io
import re
import sys
import time
from pathlib import Path

try:
    import requests
    import pdfplumber
    import frontmatter
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install requests pdfplumber python-frontmatter")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent

# EN 301 549 v3.2.1 PDF — ETSI direct download
SOURCE_URL = (
    "https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/"
    "en_301549v030201p.pdf"
)
OUTPUT_FILE = "standards/en-301-549/en-301-549-requirements.md"

HEADERS = {
    "User-Agent": "claude-a11y-repo/1.0 (accessibility knowledge base; educational use)"
}

FRONTMATTER_DATA = {
    "title": "EN 301 549 v3.2.1 — Accessibility Requirements for ICT Products and Services",
    "standard": "EN 301 549",
    "version": "3.2.1 (2021)",
    "source_url": SOURCE_URL,
    "domain": ["web", "documents", "general"],
    "status": "normative",
    "tags": ["en-301-549", "european", "etsi", "ict"],
    "ai_context": (
        "EN 301 549 v3.2.1 European ICT accessibility standard. "
        "Chapter 9 incorporates WCAG 2.1 Level AA by reference. "
        "Chapters 5–8 and 10–13 cover non-web ICT (hardware, software, documents, communication). "
        "Required for EU public procurement and underpins the European Accessibility Act (EAA)."
    ),
}

# Chapters to extract (skip front matter and annexes beyond Annex A)
CHAPTER_HEADINGS = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
    "Annex A", "Annex B", "Annex C",
]


def download_pdf(url: str, delay: float) -> bytes:
    print(f"  Downloading PDF: {url}")
    response = requests.get(url, headers=HEADERS, timeout=120, stream=True)
    response.raise_for_status()
    data = response.content
    print(f"  Downloaded {len(data) / 1024:.0f} KB")
    time.sleep(delay)
    return data


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from the PDF using pdfplumber, page by page."""
    pages_text = []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        total = len(pdf.pages)
        print(f"  Extracting text from {total} pages...")
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                pages_text.append(text)
            if i % 20 == 0:
                print(f"    Processed {i}/{total} pages")
    return "\n".join(pages_text)


def clean_pdf_text(raw: str) -> str:
    """Clean common PDF extraction artefacts."""
    # Remove repeated header/footer lines (page numbers, document title)
    lines = raw.splitlines()
    cleaned = []
    prev = None
    for line in lines:
        stripped = line.strip()
        # Skip blank duplicates and short page-number lines
        if stripped == prev:
            continue
        if re.match(r"^\d+$", stripped) and len(stripped) <= 4:
            prev = stripped
            continue
        cleaned.append(line)
        prev = stripped

    text = "\n".join(cleaned)
    # Collapse runs of 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def text_to_markdown(text: str) -> str:
    """
    Heuristically convert the extracted plain text to Markdown.
    EN 301 549 uses numbered clauses (e.g. '9.1.1.1') and table structures.
    """
    lines = text.splitlines()
    md_lines = []

    # Regex patterns for clause headings
    top_clause = re.compile(r"^(\d{1,2})\s{2,}([A-Z].{3,})$")
    sub_clause = re.compile(r"^(\d{1,2}\.\d[\d.]*)\s{2,}(.+)$")

    for line in lines:
        stripped = line.strip()
        if not stripped:
            md_lines.append("")
            continue

        m = top_clause.match(stripped)
        if m:
            md_lines.append(f"\n## {m.group(1)} {m.group(2)}")
            continue

        m = sub_clause.match(stripped)
        if m:
            depth = m.group(1).count(".")
            hashes = "#" * min(depth + 2, 6)
            md_lines.append(f"\n{hashes} {m.group(1)} {m.group(2)}")
            continue

        md_lines.append(stripped)

    md = "\n".join(md_lines)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


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
        print(f"  WARNING: file exceeds 2000 lines. Consider splitting by chapter.")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch EN 301 549 PDF and convert to Markdown"
    )
    parser.add_argument(
        "--delay", type=float, default=2.0,
        help="Delay after download in seconds (default: 2)"
    )
    args = parser.parse_args()

    print("Fetching EN 301 549 v3.2.1...")

    try:
        pdf_bytes = download_pdf(SOURCE_URL, args.delay)
    except requests.RequestException as e:
        print(f"ERROR: Failed to download PDF: {e}")
        print("Check network connection and that the ETSI URL is still valid.")
        print("See meta/standards-registry.md for the current URL.")
        sys.exit(1)

    raw_text = extract_text_from_pdf(pdf_bytes)
    cleaned = clean_pdf_text(raw_text)
    markdown = text_to_markdown(cleaned)

    fm = FRONTMATTER_DATA.copy()
    fm["last_fetched"] = datetime.date.today().isoformat()

    content = apply_frontmatter(markdown, fm)
    write_output(content, OUTPUT_FILE)

    print("\nDone. If extraction looks garbled, try:")
    print("  - Update page ranges if the PDF structure changed")
    print("  - Check meta/fetch-log.md for known issues")


if __name__ == "__main__":
    main()
