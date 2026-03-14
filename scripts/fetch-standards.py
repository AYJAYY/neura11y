#!/usr/bin/env python3
"""
Fetch accessibility standards for the claude-a11y-repo knowledge base.

Usage:
  python scripts/fetch-standards.py --all            # Fetch all standards
  python scripts/fetch-standards.py --wcag           # Fetch only WCAG
  python scripts/fetch-standards.py --aria           # Fetch only ARIA
  python scripts/fetch-standards.py --w3c-other      # ATAG, UAAG, EPUB, WebVTT, COGA, etc.
  python scripts/fetch-standards.py --us-gov         # Section 508, Plain Language
  python scripts/fetch-standards.py --source wcag-2.2  # Fetch specific source

Requirements:
  pip install requests beautifulsoup4 markdownify python-frontmatter

See meta/standards-registry.md for the full list of source URLs and target files.
"""

import argparse
import datetime
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional

# Third-party imports (install with pip)
try:
    import requests
    from bs4 import BeautifulSoup
    import markdownify
    import frontmatter
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install requests beautifulsoup4 markdownify python-frontmatter")
    sys.exit(1)

# Repository root (relative to this script's location)
REPO_ROOT = Path(__file__).parent.parent

# Default request headers
HEADERS = {
    "User-Agent": "claude-a11y-repo/1.0 (accessibility knowledge base; educational use)"
}

# Delay between requests in seconds (be respectful to W3C servers)
REQUEST_DELAY = 2.0


# ─────────────────────────────────────────────
# SOURCES REGISTRY
# Maps source key → (URL, output_file, frontmatter_template)
# ─────────────────────────────────────────────

SOURCES = {
    "wcag-2.1": {
        "url": "https://www.w3.org/TR/WCAG21/",
        "output": "standards/wcag/wcag-2.1-full.md",
        "frontmatter": {
            "title": "WCAG 2.1 Full Specification",
            "standard": "WCAG 2.1",
            "source_url": "https://www.w3.org/TR/WCAG21/",
            "domain": ["web", "documents", "general"],
            "status": "normative",
            "tags": ["wcag", "wcag-2.1"],
            "ai_context": "Complete WCAG 2.1 specification. Load wcag-2.1-quick-ref.md instead for most tasks.",
        },
        "selector": "body",
        "skip_selectors": ["nav", ".navbar", "#toc", ".header", "footer"],
    },
    "wcag-2.2": {
        "url": "https://www.w3.org/TR/WCAG22/",
        "output": "standards/wcag/wcag-2.2-full.md",
        "frontmatter": {
            "title": "WCAG 2.2 Full Specification",
            "standard": "WCAG 2.2",
            "source_url": "https://www.w3.org/TR/WCAG22/",
            "domain": ["web", "documents", "general"],
            "status": "normative",
            "tags": ["wcag", "wcag-2.2"],
            "ai_context": "Complete WCAG 2.2 specification. Load wcag-2.2-quick-ref.md instead for most tasks.",
        },
        "selector": "body",
        "skip_selectors": ["nav", ".navbar", "#toc", ".header", "footer"],
    },
    "wcag-2.2-quickref": {
        "url": "https://www.w3.org/WAI/WCAG22/quickref/",
        "output": "standards/wcag/wcag-2.2-quick-ref-fetched.md",
        "frontmatter": {
            "title": "WCAG 2.2 Quick Reference (Fetched)",
            "standard": "WCAG 2.2",
            "source_url": "https://www.w3.org/WAI/WCAG22/quickref/",
            "domain": ["web", "documents", "general"],
            "status": "normative",
            "tags": ["wcag", "wcag-2.2", "quick-ref"],
            "ai_context": "Auto-fetched WCAG 2.2 quick reference. May be incomplete due to JavaScript rendering. Prefer wcag-2.2-quick-ref.md for AI use.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "wcag-2.2-techniques": {
        "url": "https://www.w3.org/WAI/WCAG22/Techniques/",
        "output": "standards/wcag/wcag-techniques/all-techniques-fetched.md",
        "frontmatter": {
            "title": "WCAG 2.2 Techniques (Fetched)",
            "standard": "WCAG 2.2",
            "source_url": "https://www.w3.org/WAI/WCAG22/Techniques/",
            "domain": ["web", "documents", "general"],
            "status": "curated",
            "tags": ["wcag", "wcag-2.2", "techniques"],
            "ai_context": "Auto-fetched WCAG 2.2 techniques index. Use curated files in standards/wcag/wcag-techniques/ for repository loading.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "wcag-2.2-understanding": {
        "url": "https://www.w3.org/WAI/WCAG22/Understanding/",
        "output": "standards/wcag/wcag-understanding/all-understanding-docs-fetched.md",
        "frontmatter": {
            "title": "Understanding WCAG 2.2 (Fetched)",
            "standard": "WCAG 2.2",
            "source_url": "https://www.w3.org/WAI/WCAG22/Understanding/",
            "domain": ["web", "documents", "general"],
            "status": "curated",
            "tags": ["wcag", "wcag-2.2", "understanding"],
            "ai_context": "Auto-fetched WCAG 2.2 understanding index. Use curated files in standards/wcag/wcag-understanding/ for repository loading.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "wai-aria-1.2": {
        "url": "https://www.w3.org/TR/wai-aria-1.2/",
        "output": "standards/aria/wai-aria-1.2-full-fetched.md",
        "frontmatter": {
            "title": "WAI-ARIA 1.2 Full Specification (Fetched)",
            "standard": "WAI-ARIA 1.2",
            "source_url": "https://www.w3.org/TR/wai-aria-1.2/",
            "domain": ["web"],
            "status": "normative",
            "tags": ["aria", "wai-aria"],
            "ai_context": "Auto-fetched WAI-ARIA 1.2 specification. Prefer wai-aria-1.2-roles.md for AI use.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "aria-in-html": {
        "url": "https://www.w3.org/TR/html-aria/",
        "output": "standards/aria/aria-in-html-fetched.md",
        "frontmatter": {
            "title": "ARIA in HTML (Fetched)",
            "standard": "ARIA in HTML",
            "source_url": "https://www.w3.org/TR/html-aria/",
            "domain": ["web"],
            "status": "normative",
            "tags": ["aria", "html", "implicit-role"],
            "ai_context": "Auto-fetched ARIA in HTML specification.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "atag-2.0": {
        "url": "https://www.w3.org/TR/ATAG20/",
        "output": "standards/other-standards/atag-2.0-fetched.md",
        "frontmatter": {
            "title": "ATAG 2.0 (Fetched)",
            "standard": "ATAG 2.0",
            "source_url": "https://www.w3.org/TR/ATAG20/",
            "domain": ["general"],
            "status": "normative",
            "tags": ["atag", "authoring-tools"],
            "ai_context": "ATAG 2.0 specification for authoring tools.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "uaag-2.0": {
        "url": "https://www.w3.org/TR/UAAG20/",
        "output": "standards/other-standards/uaag-2.0-fetched.md",
        "frontmatter": {
            "title": "UAAG 2.0 (Fetched)",
            "standard": "UAAG 2.0",
            "source_url": "https://www.w3.org/TR/UAAG20/",
            "domain": ["general"],
            "status": "normative",
            "tags": ["uaag", "user-agents"],
            "ai_context": "UAAG 2.0 specification for user agents and browsers.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "epub-a11y-1.1": {
        "url": "https://www.w3.org/TR/epub-a11y-11/",
        "output": "standards/epub/epub-accessibility-1.1-fetched.md",
        "frontmatter": {
            "title": "EPUB Accessibility 1.1 (Fetched)",
            "standard": "EPUB Accessibility 1.1",
            "source_url": "https://www.w3.org/TR/epub-a11y-11/",
            "domain": ["documents"],
            "status": "normative",
            "tags": ["epub", "ebooks"],
            "ai_context": "Auto-fetched EPUB Accessibility 1.1 specification.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "section-508-tech": {
        "url": "https://www.access-board.gov/ict/",
        "output": "standards/section-508/section-508-technical-fetched.md",
        "frontmatter": {
            "title": "Section 508 Technical Standards (Fetched)",
            "standard": "Section 508",
            "source_url": "https://www.access-board.gov/ict/",
            "domain": ["web", "documents", "general"],
            "status": "normative",
            "tags": ["section-508", "us", "federal"],
            "ai_context": "Auto-fetched Section 508 technical standards from Access Board.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "header", "footer"],
    },
    "plain-language": {
        "url": "https://www.plainlanguage.gov/guidelines/",
        "output": "domains/documents/plain-language/plain-language-fetched.md",
        "frontmatter": {
            "title": "Federal Plain Language Guidelines (Fetched)",
            "standard": "Plain Language Guidelines",
            "source_url": "https://www.plainlanguage.gov/guidelines/",
            "domain": ["documents", "general"],
            "status": "prescriptive",
            "tags": ["plain-language", "writing", "federal"],
            "ai_context": "Auto-fetched federal plain language guidelines.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "header", "footer"],
    },
    "webvtt-1.0": {
        "url": "https://www.w3.org/TR/webvtt1/",
        "output": "media/video/webvtt-spec.md",
        "frontmatter": {
            "title": "WebVTT 1.0 Specification",
            "standard": "WebVTT 1.0",
            "source_url": "https://www.w3.org/TR/webvtt1/",
            "domain": ["media", "social-media"],
            "status": "normative",
            "tags": ["webvtt", "captions", "timed-text", "video"],
            "ai_context": "WebVTT timed text specification. Load for caption file syntax, cue settings, and track authoring details.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "alt-text-tree": {
        "url": "https://www.w3.org/WAI/tutorials/images/decision-tree/",
        "output": "media/images/alt-text-decision-tree.md",
        "frontmatter": {
            "title": "Alt Text Decision Tree (Fetched)",
            "standard": "WCAG 2.2",
            "source_url": "https://www.w3.org/WAI/tutorials/images/decision-tree/",
            "domain": ["web", "documents", "social-media"],
            "status": "prescriptive",
            "tags": ["alt-text", "images", "decision-tree"],
            "ai_context": "W3C alt text decision tree for determining the correct alt text approach.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "header", "footer"],
    },
    "coga-usable": {
        "url": "https://www.w3.org/TR/coga-usable/",
        "output": "cognitive/coga-design-guide-fetched.md",
        "frontmatter": {
            "title": "Making Content Usable for People with Cognitive Disabilities (Fetched)",
            "standard": "COGA",
            "source_url": "https://www.w3.org/TR/coga-usable/",
            "domain": ["web", "documents", "general"],
            "status": "normative",
            "tags": ["coga", "cognitive", "accessibility"],
            "ai_context": "Auto-fetched COGA design guide for cognitive accessibility.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
}

# Group sources by family
SOURCE_GROUPS = {
    "wcag": [
        "wcag-2.1",
        "wcag-2.2",
        "wcag-2.2-quickref",
        "wcag-2.2-techniques",
        "wcag-2.2-understanding",
    ],
    "aria": ["wai-aria-1.2", "aria-in-html"],
    "w3c-other": ["atag-2.0", "uaag-2.0", "epub-a11y-1.1", "webvtt-1.0", "alt-text-tree", "coga-usable"],
    "us-gov": ["section-508-tech", "plain-language"],
}


# ─────────────────────────────────────────────
# FETCH FUNCTIONS
# ─────────────────────────────────────────────

def fetch_url(url: str, delay: float = REQUEST_DELAY) -> Optional[str]:
    """Fetch a URL and return the HTML content."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        response.encoding = "utf-8"
        time.sleep(delay)
        return response.text
    except requests.RequestException as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def html_to_markdown(
    html: str,
    selector: str = "body",
    skip_selectors: list = None,
) -> str:
    """Extract content from HTML and convert to Markdown."""
    soup = BeautifulSoup(html, "html.parser")

    # Extract main content area
    content_el = soup.select_one(selector)
    if not content_el:
        content_el = soup.body or soup

    # Remove unwanted elements
    if skip_selectors:
        for sel in skip_selectors:
            for el in content_el.select(sel):
                el.decompose()

    # Convert to Markdown
    md = markdownify.markdownify(
        str(content_el),
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
        convert_as_inline=["a"],
    )

    # Clean up excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip()

    return md


def apply_frontmatter(content: str, fm_data: dict) -> str:
    """Prepend YAML frontmatter to content."""
    post = frontmatter.Post(content, **fm_data)
    return frontmatter.dumps(post)


def write_output(content: str, output_path: str, repo_root: Path) -> None:
    """Write content to output file, creating directories as needed."""
    full_path = repo_root / output_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8")
    print(f"  Written: {output_path}")


def check_line_count(content: str, output_path: str) -> None:
    """Warn if content exceeds 2000 lines."""
    lines = content.count("\n")
    if lines > 2000:
        print(f"  WARNING: {output_path} has {lines} lines (exceeds 2000-line limit)")
        print(f"  Consider splitting at guideline/principle boundaries")


def fetch_source(key: str, config: dict) -> bool:
    """Fetch a single source and write to output file."""
    print(f"\nFetching: {key}")

    html = fetch_url(config["url"])
    if not html:
        return False

    markdown = html_to_markdown(
        html,
        selector=config.get("selector", "body"),
        skip_selectors=config.get("skip_selectors", []),
    )

    # Add fetch timestamp to frontmatter
    fm_data = config["frontmatter"].copy()
    fm_data["last_fetched"] = datetime.date.today().isoformat()

    content = apply_frontmatter(markdown, fm_data)
    check_line_count(content, config["output"])
    write_output(content, config["output"], REPO_ROOT)
    return True


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Fetch accessibility standards for claude-a11y-repo"
    )
    parser.add_argument("--all", action="store_true", help="Fetch all sources")
    parser.add_argument("--wcag", action="store_true", help="Fetch WCAG standards")
    parser.add_argument("--aria", action="store_true", help="Fetch ARIA standards")
    parser.add_argument("--w3c-other", action="store_true", help="Fetch other W3C standards")
    parser.add_argument("--us-gov", action="store_true", help="Fetch US government standards")
    parser.add_argument("--source", type=str, help="Fetch specific source by key")
    parser.add_argument("--list", action="store_true", help="List all available sources")
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY,
                        help=f"Delay between requests in seconds (default: {REQUEST_DELAY})")

    args = parser.parse_args()

    if args.list:
        print("Available sources:")
        for key, config in SOURCES.items():
            print(f"  {key:30s} → {config['output']}")
        return

    sources_to_fetch = []

    if args.all:
        sources_to_fetch = list(SOURCES.keys())
    elif args.wcag:
        sources_to_fetch = SOURCE_GROUPS["wcag"]
    elif args.aria:
        sources_to_fetch = SOURCE_GROUPS["aria"]
    elif getattr(args, "w3c_other", False):
        sources_to_fetch = SOURCE_GROUPS["w3c-other"]
    elif getattr(args, "us_gov", False):
        sources_to_fetch = SOURCE_GROUPS["us-gov"]
    elif args.source:
        if args.source not in SOURCES:
            print(f"Unknown source: {args.source}")
            print("Use --list to see available sources")
            sys.exit(1)
        sources_to_fetch = [args.source]
    else:
        parser.print_help()
        return

    if not sources_to_fetch:
        print("No sources to fetch. Use --list to see options.")
        return

    print(f"Fetching {len(sources_to_fetch)} source(s) with {args.delay}s delay...")

    success = 0
    failed = []

    for key in sources_to_fetch:
        if key not in SOURCES:
            print(f"  SKIP: Unknown source '{key}'")
            continue
        try:
            if fetch_source(key, SOURCES[key]):
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
        print("Check meta/fetch-log.md for details")
        print("Common fixes: --delay 5 (for rate limiting), check network connection")


if __name__ == "__main__":
    main()
