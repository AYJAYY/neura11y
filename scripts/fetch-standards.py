#!/usr/bin/env python3
"""
Fetch accessibility standards for the claude-a11y-repo knowledge base.

Usage:
  python scripts/fetch-standards.py --all            # Fetch all standards
  python scripts/fetch-standards.py --wcag           # Fetch only WCAG
  python scripts/fetch-standards.py --aria           # Fetch only ARIA
  python scripts/fetch-standards.py --w3c-other      # ATAG, UAAG, EPUB, WebVTT, COGA, WCAG2ICT, tutorials
  python scripts/fetch-standards.py --screen-readers # Vendor screen reader support docs
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
GOOGLE_API_KEY_PATTERN = re.compile(r"AIza[0-9A-Za-z_-]{20,}")


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
    "accname-1.2": {
        "url": "https://www.w3.org/TR/accname-1.2/",
        "output": "standards/aria/accname-1.2.md",
        "frontmatter": {
            "title": "Accessible Name and Description Computation 1.2",
            "standard": "Accessible Name and Description Computation 1.2",
            "source_url": "https://www.w3.org/TR/accname-1.2/",
            "domain": ["web"],
            "status": "normative",
            "tags": ["aria", "accname", "accessible-name", "labeling"],
            "ai_context": "Accessible name and description computation algorithm for labels, names, and descriptions exposed to assistive technologies.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
    },
    "core-aam-1.2": {
        "url": "https://www.w3.org/TR/core-aam-1.2/",
        "output": "standards/aria/core-aam-1.2-full-fetched.md",
        "frontmatter": {
            "title": "Core Accessibility API Mappings 1.2 (Full Fetched)",
            "standard": "Core Accessibility API Mappings 1.2",
            "source_url": "https://www.w3.org/TR/core-aam-1.2/",
            "domain": ["web"],
            "status": "normative",
            "tags": ["aria", "core-aam", "accessibility-api", "mappings"],
            "ai_context": "Auto-fetched full Core-AAM 1.2 specification. Prefer split core-aam-1.2-*.md files for AI use.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
        "derived_outputs": [
            {
                "output": "standards/aria/core-aam-1.2-overview.md",
                "document_title": "Core Accessibility API Mappings 1.2 Overview",
                "frontmatter": {
                    "title": "Core Accessibility API Mappings 1.2 Overview",
                    "standard": "Core Accessibility API Mappings 1.2",
                    "source_url": "https://www.w3.org/TR/core-aam-1.2/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "core-aam", "overview", "accessibility-api", "mappings"],
                    "ai_context": "Overview of Core-AAM 1.2 scope, conformance, accessibility API model, and algorithm context.",
                },
                "ranges": [
                    {
                        "start": "## Abstract",
                        "end_before": "### 3.1 General rules for exposing WAI-ARIA semantics",
                    },
                    {
                        "start": "## 5. Privacy considerations",
                        "end_before": "## A. Change Log",
                    },
                ],
            },
            {
                "output": "standards/aria/core-aam-1.2-role-mappings.md",
                "document_title": "Core Accessibility API Mappings 1.2 Role Mappings",
                "frontmatter": {
                    "title": "Core Accessibility API Mappings 1.2 Role Mappings",
                    "standard": "Core Accessibility API Mappings 1.2",
                    "source_url": "https://www.w3.org/TR/core-aam-1.2/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "core-aam", "roles", "role-mappings", "accessibility-api"],
                    "ai_context": "Core-AAM role exposure rules and role mapping tables for WAI-ARIA semantics.",
                },
                "ranges": [
                    {
                        "wrap_heading": "General Rules and Role Mappings",
                        "start": "### 3.1 General rules for exposing WAI-ARIA semantics",
                        "end_before": "### 3.5 State and Property Mapping",
                    },
                ],
            },
            {
                "output": "standards/aria/core-aam-1.2-state-property-and-event-mappings.md",
                "document_title": "Core Accessibility API Mappings 1.2 State, Property, and Event Mappings",
                "frontmatter": {
                    "title": "Core Accessibility API Mappings 1.2 State, Property, and Event Mappings",
                    "standard": "Core Accessibility API Mappings 1.2",
                    "source_url": "https://www.w3.org/TR/core-aam-1.2/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "core-aam", "states", "properties", "events", "accessibility-api"],
                    "ai_context": "Core-AAM mappings for ARIA states, properties, special processing, actions, events, and notify algorithms.",
                },
                "ranges": [
                    {
                        "wrap_heading": "State, Property, Action, and Event Mappings",
                        "start": "### 3.5 State and Property Mapping",
                        "end_before": "### 4.1 ARIANotifyMixin Algorithm Mapping Tables",
                    },
                    {
                        "wrap_heading": "ARIANotifyMixin Algorithm Mapping Tables",
                        "start": "### 4.1 ARIANotifyMixin Algorithm Mapping Tables",
                        "end_before": "## 5. Privacy considerations",
                    },
                ],
            },
        ],
    },
    "html-aam-1.0": {
        "url": "https://www.w3.org/TR/html-aam-1.0/",
        "output": "standards/aria/html-aam-1.0-full-fetched.md",
        "frontmatter": {
            "title": "HTML Accessibility API Mappings 1.0 (Full Fetched)",
            "standard": "HTML Accessibility API Mappings 1.0",
            "source_url": "https://www.w3.org/TR/html-aam-1.0/",
            "domain": ["web"],
            "status": "normative",
            "tags": ["aria", "html-aam", "html", "accessibility-api", "mappings"],
            "ai_context": "Auto-fetched full HTML-AAM 1.0 specification. Prefer split html-aam-1.0-*.md files for AI use.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
        "derived_outputs": [
            {
                "output": "standards/aria/html-aam-1.0-overview.md",
                "document_title": "HTML Accessibility API Mappings 1.0 Overview",
                "frontmatter": {
                    "title": "HTML Accessibility API Mappings 1.0 Overview",
                    "standard": "HTML Accessibility API Mappings 1.0",
                    "source_url": "https://www.w3.org/TR/html-aam-1.0/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "html-aam", "overview", "html", "accessibility-api"],
                    "ai_context": "Overview of HTML-AAM 1.0 scope, conformance, and general HTML-to-accessibility API rules.",
                },
                "ranges": [
                    {
                        "start": "## Abstract",
                        "end_before": "### 3.5 HTML Element Role Mappings",
                    },
                    {
                        "start": "## 5. Privacy considerations",
                        "end_before": "## A. Appendices",
                    },
                ],
            },
            {
                "output": "standards/aria/html-aam-1.0-element-role-mappings.md",
                "document_title": "HTML Accessibility API Mappings 1.0 Element Role Mappings",
                "frontmatter": {
                    "title": "HTML Accessibility API Mappings 1.0 Element Role Mappings",
                    "standard": "HTML Accessibility API Mappings 1.0",
                    "source_url": "https://www.w3.org/TR/html-aam-1.0/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "html-aam", "html", "roles", "element-mappings"],
                    "ai_context": "HTML-AAM element role mappings for native HTML elements and states.",
                },
                "ranges": [
                    {
                        "wrap_heading": "HTML Element Role Mappings",
                        "start": "### 3.5 HTML Element Role Mappings",
                        "end_before": "### 3.6 HTML Attribute State and Property Mappings",
                    },
                ],
            },
            {
                "output": "standards/aria/html-aam-1.0-attribute-state-property-mappings-a-to-m.md",
                "document_title": "HTML Accessibility API Mappings 1.0 Attribute State and Property Mappings A-M",
                "frontmatter": {
                    "title": "HTML Accessibility API Mappings 1.0 Attribute State and Property Mappings A-M",
                    "standard": "HTML Accessibility API Mappings 1.0",
                    "source_url": "https://www.w3.org/TR/html-aam-1.0/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "html-aam", "html", "attributes", "states", "properties"],
                    "ai_context": "HTML-AAM attribute mappings for HTML attributes from abbr through muted.",
                },
                "ranges": [
                    {
                        "wrap_heading": "HTML Attribute State and Property Mappings A-M",
                        "start": "### 3.6 HTML Attribute State and Property Mappings",
                        "end_before": "#### 3.6.92 `name`",
                    },
                ],
            },
            {
                "output": "standards/aria/html-aam-1.0-attribute-state-property-mappings-n-to-z.md",
                "document_title": "HTML Accessibility API Mappings 1.0 Attribute State and Property Mappings N-Z",
                "frontmatter": {
                    "title": "HTML Accessibility API Mappings 1.0 Attribute State and Property Mappings N-Z",
                    "standard": "HTML Accessibility API Mappings 1.0",
                    "source_url": "https://www.w3.org/TR/html-aam-1.0/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "html-aam", "html", "attributes", "states", "properties"],
                    "ai_context": "HTML-AAM attribute mappings for HTML attributes from name through wrap.",
                },
                "ranges": [
                    {
                        "wrap_heading": "HTML Attribute State and Property Mappings N-Z",
                        "start": "#### 3.6.92 `name`",
                        "end_before": "## 4. Accessible Name and Description Computation",
                    },
                ],
            },
            {
                "output": "standards/aria/html-aam-1.0-accessible-name-and-description-computation.md",
                "document_title": "HTML Accessibility API Mappings 1.0 Accessible Name and Description Computation",
                "frontmatter": {
                    "title": "HTML Accessibility API Mappings 1.0 Accessible Name and Description Computation",
                    "standard": "HTML Accessibility API Mappings 1.0",
                    "source_url": "https://www.w3.org/TR/html-aam-1.0/",
                    "domain": ["web"],
                    "status": "normative",
                    "tags": ["aria", "html-aam", "accessible-name", "accessible-description", "html"],
                    "ai_context": "HTML-AAM accessible name and accessible description computation rules for HTML elements.",
                },
                "ranges": [
                    {
                        "start": "## 4. Accessible Name and Description Computation",
                        "end_before": "## 5. Privacy considerations",
                    },
                ],
            },
        ],
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
    "wcag2ict-22": {
        "url": "https://www.w3.org/TR/wcag2ict-22/",
        "output": "standards/other-standards/wcag2ict-22-full-fetched.md",
        "frontmatter": {
            "title": "WCAG2ICT 2.2 (Full Fetched)",
            "standard": "WCAG2ICT 2.2",
            "source_url": "https://www.w3.org/TR/wcag2ict-22/",
            "domain": ["documents", "mobile", "physical-ict", "general"],
            "status": "prescriptive",
            "tags": ["wcag2ict", "non-web", "documents", "software", "ict"],
            "ai_context": "Auto-fetched full WCAG2ICT 2.2 Note. Prefer split wcag2ict-22-*.md files for AI use.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "#toc", "header", "footer"],
        "derived_outputs": [
            {
                "output": "standards/other-standards/wcag2ict-22-overview.md",
                "document_title": "WCAG2ICT 2.2 Overview",
                "frontmatter": {
                    "title": "WCAG2ICT 2.2 Overview",
                    "standard": "WCAG2ICT 2.2",
                    "source_url": "https://www.w3.org/TR/wcag2ict-22/",
                    "domain": ["documents", "mobile", "physical-ict", "general"],
                    "status": "prescriptive",
                    "tags": ["wcag2ict", "non-web", "overview", "documents", "software", "ict"],
                    "ai_context": "Overview of WCAG2ICT scope, terminology, closed functionality, text interfaces, and conformance notes.",
                },
                "ranges": [
                    {
                        "start": "## Abstract",
                        "end_before": "### 1. Perceivable",
                    },
                ],
            },
            {
                "output": "standards/other-standards/wcag2ict-22-guideline-comments-perceivable-and-operable.md",
                "document_title": "WCAG2ICT 2.2 Guideline Comments: Perceivable and Operable",
                "frontmatter": {
                    "title": "WCAG2ICT 2.2 Guideline Comments: Perceivable and Operable",
                    "standard": "WCAG2ICT 2.2",
                    "source_url": "https://www.w3.org/TR/wcag2ict-22/",
                    "domain": ["documents", "mobile", "physical-ict", "general"],
                    "status": "prescriptive",
                    "tags": ["wcag2ict", "non-web", "perceivable", "operable", "guideline-comments"],
                    "ai_context": "WCAG2ICT interpretations for Principles 1 and 2 in non-web documents and software contexts.",
                },
                "ranges": [
                    {
                        "wrap_heading": "Guideline Comments for Principles 1 and 2",
                        "start": "### 1. Perceivable",
                        "end_before": "### 3. Understandable",
                    },
                ],
            },
            {
                "output": "standards/other-standards/wcag2ict-22-guideline-comments-understandable-and-robust.md",
                "document_title": "WCAG2ICT 2.2 Guideline Comments: Understandable and Robust",
                "frontmatter": {
                    "title": "WCAG2ICT 2.2 Guideline Comments: Understandable and Robust",
                    "standard": "WCAG2ICT 2.2",
                    "source_url": "https://www.w3.org/TR/wcag2ict-22/",
                    "domain": ["documents", "mobile", "physical-ict", "general"],
                    "status": "prescriptive",
                    "tags": ["wcag2ict", "non-web", "understandable", "robust", "guideline-comments"],
                    "ai_context": "WCAG2ICT interpretations for Principles 3 and 4 in non-web documents and software contexts.",
                },
                "ranges": [
                    {
                        "wrap_heading": "Guideline Comments for Principles 3 and 4",
                        "start": "### 3. Understandable",
                        "end_before": "## Comments on Definitions in WCAG 2 Glossary",
                    },
                ],
            },
            {
                "output": "standards/other-standards/wcag2ict-22-glossary-and-appendices.md",
                "document_title": "WCAG2ICT 2.2 Glossary and Appendices",
                "frontmatter": {
                    "title": "WCAG2ICT 2.2 Glossary and Appendices",
                    "standard": "WCAG2ICT 2.2",
                    "source_url": "https://www.w3.org/TR/wcag2ict-22/",
                    "domain": ["documents", "mobile", "physical-ict", "general"],
                    "status": "prescriptive",
                    "tags": ["wcag2ict", "non-web", "glossary", "appendices", "definitions"],
                    "ai_context": "WCAG2ICT glossary interpretations, privacy and security considerations, appendices, and references.",
                },
                "ranges": [
                    {
                        "start": "## Comments on Definitions in WCAG 2 Glossary",
                    },
                ],
            },
        ],
    },
    "wai-tutorial-forms": {
        "url": "https://www.w3.org/WAI/tutorials/forms/",
        "output": "domains/web/source/wai-tutorials/forms-tutorial-fetched.md",
        "frontmatter": {
            "title": "WAI Forms Tutorial (Fetched)",
            "standard": "WAI Tutorials",
            "source_url": "https://www.w3.org/WAI/tutorials/forms/",
            "domain": ["web"],
            "status": "prescriptive",
            "tags": ["forms", "tutorial", "wai", "web"],
            "ai_context": "Auto-fetched W3C forms tutorial. Supporting source for forms guidance and examples.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer", ".pager", ".nextprev"],
    },
    "wai-tutorial-tables": {
        "url": "https://www.w3.org/WAI/tutorials/tables/",
        "output": "domains/web/source/wai-tutorials/tables-tutorial-fetched.md",
        "frontmatter": {
            "title": "WAI Tables Tutorial (Fetched)",
            "standard": "WAI Tutorials",
            "source_url": "https://www.w3.org/WAI/tutorials/tables/",
            "domain": ["web", "documents"],
            "status": "prescriptive",
            "tags": ["tables", "tutorial", "wai", "web"],
            "ai_context": "Auto-fetched W3C tables tutorial. Supporting source for accessible data table guidance and examples.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer", ".pager", ".nextprev"],
    },
    "wai-tutorial-page-structure": {
        "url": "https://www.w3.org/WAI/tutorials/page-structure/",
        "output": "domains/web/source/wai-tutorials/page-structure-tutorial-fetched.md",
        "frontmatter": {
            "title": "WAI Page Structure Tutorial (Fetched)",
            "standard": "WAI Tutorials",
            "source_url": "https://www.w3.org/WAI/tutorials/page-structure/",
            "domain": ["web"],
            "status": "prescriptive",
            "tags": ["page-structure", "tutorial", "wai", "web"],
            "ai_context": "Auto-fetched W3C page structure tutorial. Supporting source for headings, landmarks, and navigation guidance.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer", ".pager", ".nextprev"],
    },
    "wai-tutorial-menus": {
        "url": "https://www.w3.org/WAI/tutorials/menus/",
        "output": "domains/web/source/wai-tutorials/menus-tutorial-fetched.md",
        "frontmatter": {
            "title": "WAI Menus Tutorial (Fetched)",
            "standard": "WAI Tutorials",
            "source_url": "https://www.w3.org/WAI/tutorials/menus/",
            "domain": ["web"],
            "status": "prescriptive",
            "tags": ["menus", "tutorial", "wai", "web"],
            "ai_context": "Auto-fetched W3C menus tutorial. Supporting source for navigation and disclosure menu guidance.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer", ".pager", ".nextprev"],
    },
    "wai-tutorial-images": {
        "url": "https://www.w3.org/WAI/tutorials/images/",
        "output": "media/images/images-tutorial-fetched.md",
        "frontmatter": {
            "title": "WAI Images Tutorial (Fetched)",
            "standard": "WAI Tutorials",
            "source_url": "https://www.w3.org/WAI/tutorials/images/",
            "domain": ["web", "documents", "social-media"],
            "status": "prescriptive",
            "tags": ["images", "tutorial", "wai", "alt-text"],
            "ai_context": "Auto-fetched W3C images tutorial. Supporting source for image purpose and text alternative guidance.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "#toc", "header", "footer", ".pager", ".nextprev"],
    },
    "nvda-user-guide": {
        "url": "https://www.nvaccess.org/files/nvda/documentation/userGuide.html",
        "output": "screen-readers/source/nvda-user-guide-fetched.md",
        "frontmatter": {
            "title": "NVDA User Guide (Fetched)",
            "standard": "NVDA",
            "source_url": "https://www.nvaccess.org/files/nvda/documentation/userGuide.html",
            "domain": ["web", "general"],
            "status": "prescriptive",
            "tags": ["screen-reader", "nvda", "windows", "testing", "commands"],
            "ai_context": "Auto-fetched NVDA user guide. Supporting provenance source for the curated NVDA testing guides.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "header", "footer", ".sidebar", ".menu"],
    },
    "voiceover-user-guide-mac": {
        "url": "https://support.apple.com/guide/voiceover/welcome/mac",
        "output": "screen-readers/source/voiceover-user-guide-mac-fetched.md",
        "frontmatter": {
            "title": "VoiceOver User Guide for Mac (Fetched)",
            "standard": "VoiceOver",
            "source_url": "https://support.apple.com/guide/voiceover/welcome/mac",
            "domain": ["web", "general"],
            "status": "prescriptive",
            "tags": ["screen-reader", "voiceover", "macos", "testing", "commands"],
            "ai_context": "Auto-fetched VoiceOver for Mac user guide. Supporting provenance source for the curated VoiceOver testing guides.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "header", "footer", "aside"],
    },
    "talkback-user-guide": {
        "url": "https://support.google.com/accessibility/android/answer/6283677",
        "output": "screen-readers/source/talkback-user-guide-fetched.md",
        "frontmatter": {
            "title": "TalkBack Guide for Android (Fetched)",
            "standard": "TalkBack",
            "source_url": "https://support.google.com/accessibility/android/answer/6283677",
            "domain": ["mobile", "web", "general"],
            "status": "prescriptive",
            "tags": ["screen-reader", "talkback", "android", "testing", "gestures"],
            "ai_context": "Auto-fetched TalkBack support guide. Supporting provenance source for curated Android and TalkBack guidance.",
        },
        "selector": "main",
        "skip_selectors": ["nav", "header", "footer", "aside"],
        "truncate_after_markers": ["window['prt']= new Date().getTime();"],
    },
    "jaws-keystrokes": {
        "url": "https://support.freedomscientific.com/content/html/jawshq/JAWS-Keystrokes.html",
        "output": "screen-readers/source/jaws-keystrokes-fetched.md",
        "frontmatter": {
            "title": "JAWS Keystrokes Guide (Fetched)",
            "standard": "JAWS",
            "source_url": "https://support.freedomscientific.com/content/html/jawshq/JAWS-Keystrokes.html",
            "domain": ["web", "documents", "general"],
            "status": "prescriptive",
            "tags": ["screen-reader", "jaws", "windows", "testing", "keyboard"],
            "ai_context": "Auto-fetched JAWS keystrokes guide. Supporting provenance source for curated JAWS testing guidance.",
        },
        "selector": "body",
        "skip_selectors": ["nav", "header", "footer", "aside"],
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
    "aria": ["wai-aria-1.2", "accname-1.2", "core-aam-1.2", "html-aam-1.0", "aria-in-html"],
    "w3c-other": [
        "atag-2.0",
        "uaag-2.0",
        "epub-a11y-1.1",
        "webvtt-1.0",
        "alt-text-tree",
        "coga-usable",
        "wcag2ict-22",
        "wai-tutorial-forms",
        "wai-tutorial-tables",
        "wai-tutorial-page-structure",
        "wai-tutorial-menus",
        "wai-tutorial-images",
    ],
    "screen-readers": [
        "nvda-user-guide",
        "voiceover-user-guide-mac",
        "talkback-user-guide",
        "jaws-keystrokes",
    ],
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


def truncate_at_markers(markdown: str, markers: list[str]) -> tuple[str, str | None]:
    """Trim unwanted bootstrap content that appears after the real article."""
    first_marker: str | None = None
    first_index: int | None = None
    for marker in markers:
        index = markdown.find(marker)
        if index == -1:
            continue
        if first_index is None or index < first_index:
            first_index = index
            first_marker = marker

    if first_index is None:
        return markdown, None
    return markdown[:first_index].rstrip(), first_marker


def redact_google_api_keys(markdown: str) -> tuple[str, int]:
    """Redact Google-style API keys if a fetched page leaks them into markdown."""
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        replacements += 1
        return "[REDACTED_GOOGLE_API_KEY]"

    return GOOGLE_API_KEY_PATTERN.sub(replace, markdown), replacements


def sanitize_markdown(markdown: str, config: dict) -> str:
    """Apply source-specific cleanup and token redaction to fetched markdown."""
    truncate_markers = config.get("truncate_after_markers", [])
    if truncate_markers:
        markdown, marker = truncate_at_markers(markdown, truncate_markers)
        if marker:
            print(f"  Truncated content at marker: {marker}")

    markdown, redactions = redact_google_api_keys(markdown)
    if redactions:
        print(f"  Redacted {redactions} Google API-style token(s)")

    return markdown.strip()


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


def extract_heading_range(content: str, start_heading: str, end_before_heading: str | None = None) -> str:
    """Extract content between two exact markdown headings."""
    start_pattern = re.compile(rf"(?m)^{re.escape(start_heading)}\s*$")
    start_match = start_pattern.search(content)
    if not start_match:
        raise ValueError(f"Heading not found: {start_heading}")

    start = start_match.start()
    end = len(content)
    if end_before_heading:
        end_pattern = re.compile(rf"(?m)^{re.escape(end_before_heading)}\s*$")
        end_match = end_pattern.search(content, start_match.end())
        if not end_match:
            raise ValueError(f"Heading not found: {end_before_heading}")
        end = end_match.start()

    return content[start:end].strip()


def build_derived_markdown(markdown: str, document_title: str, ranges: list[dict]) -> str:
    """Build a split markdown file from selected ranges of a fetched source."""
    parts = [f"# {document_title}"]
    for range_config in ranges:
        excerpt = extract_heading_range(
            markdown,
            range_config["start"],
            range_config.get("end_before"),
        )
        wrap_heading = range_config.get("wrap_heading")
        if wrap_heading:
            parts.append(f"## {wrap_heading}\n\n{excerpt}")
        else:
            parts.append(excerpt)
    return "\n\n".join(part.strip() for part in parts if part.strip())


def write_derived_outputs(markdown: str, derived_outputs: list[dict], last_fetched: str) -> None:
    """Write split canonical files derived from a fetched raw source."""
    for derived in derived_outputs:
        derived_markdown = build_derived_markdown(
            markdown,
            derived["document_title"],
            derived["ranges"],
        )
        fm_data = derived["frontmatter"].copy()
        fm_data["last_fetched"] = last_fetched
        content = apply_frontmatter(derived_markdown, fm_data)
        check_line_count(content, derived["output"])
        write_output(content, derived["output"], REPO_ROOT)


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
    markdown = sanitize_markdown(markdown, config)

    # Add fetch timestamp to frontmatter
    last_fetched = datetime.date.today().isoformat()
    fm_data = config["frontmatter"].copy()
    fm_data["last_fetched"] = last_fetched

    content = apply_frontmatter(markdown, fm_data)
    check_line_count(content, config["output"])
    write_output(content, config["output"], REPO_ROOT)

    derived_outputs = config.get("derived_outputs", [])
    if derived_outputs:
        write_derived_outputs(markdown, derived_outputs, last_fetched)
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
    parser.add_argument("--screen-readers", action="store_true", help="Fetch screen reader source docs")
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
    elif getattr(args, "screen_readers", False):
        sources_to_fetch = SOURCE_GROUPS["screen-readers"]
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
