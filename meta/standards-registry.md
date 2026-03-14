---
title: "Standards Registry"
type: "meta"
status: "curated"
last_updated: "2026-03-13"
ai_context: "Master list of all accessibility standards tracked in this repository, with canonical URLs, current versions, and fetch status. Use to validate source URLs before fetching."
---

# Standards Registry

Master source-of-truth for all standards tracked in this repository. All fetch scripts reference this file for source URLs.

---

## W3C Standards

### WCAG (Web Content Accessibility Guidelines)

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| WCAG 2.1 | 2.1 (June 2018) | W3C Recommendation | https://www.w3.org/TR/WCAG21/ | `standards/wcag/wcag-2.1-full.md` | — |
| WCAG 2.2 | 2.2 (October 2023) | W3C Recommendation | https://www.w3.org/TR/WCAG22/ | `standards/wcag/wcag-2.2-full.md` | — |
| WCAG 3.0 | 3.0 (Working Draft) | W3C Working Draft | https://www.w3.org/TR/wcag-3.0/ | `standards/wcag/wcag-3.0-overview.md` | — |
| WCAG 2.1 Quick Ref | 2.1 | Living Document | https://www.w3.org/WAI/WCAG21/quickref/ | `standards/wcag/wcag-2.1-quick-ref.md` | — |
| WCAG 2.2 Quick Ref | 2.2 | Living Document | https://www.w3.org/WAI/WCAG22/quickref/ | `standards/wcag/wcag-2.2-quick-ref.md` | — |
| WCAG Techniques (2.1) | 2.1 | Living Document | https://www.w3.org/WAI/WCAG21/Techniques/ | `standards/wcag/wcag-techniques/` | — |
| WCAG Techniques (2.2) | 2.2 | Living Document | https://www.w3.org/WAI/WCAG22/Techniques/ | `standards/wcag/wcag-techniques/` | — |
| Understanding WCAG 2.2 | 2.2 | Living Document | https://www.w3.org/WAI/WCAG22/Understanding/ | `standards/wcag/wcag-understanding/` | — |

### WAI-ARIA

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| WAI-ARIA | 1.2 (June 2023) | W3C Recommendation | https://www.w3.org/TR/wai-aria-1.2/ | `standards/aria/wai-aria-1.2-roles.md` | — |
| WAI-ARIA States/Props | 1.2 | W3C Recommendation | https://www.w3.org/TR/wai-aria-1.2/#state_prop_def | `standards/aria/wai-aria-1.2-states-properties.md` | — |
| ARIA in HTML | 2023 | W3C Recommendation | https://www.w3.org/TR/html-aria/ | `standards/aria/aria-in-html.md` | — |
| ARIA APG Patterns | 2024 | Living Document | https://www.w3.org/WAI/ARIA/apg/patterns/ | `standards/aria/aria-authoring-practices.md` | — |

### Other W3C Standards

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| ATAG 2.0 | 2.0 (Sept 2015) | W3C Recommendation | https://www.w3.org/TR/ATAG20/ | `standards/other-standards/atag-2.0-overview.md` | — |
| UAAG 2.0 | 2.0 (Dec 2015) | W3C Note | https://www.w3.org/TR/UAAG20/ | `standards/other-standards/uaag-2.0-overview.md` | — |
| EPUB Accessibility 1.1 | 1.1 (May 2023) | W3C Recommendation | https://www.w3.org/TR/epub-a11y-11/ | `standards/epub/epub-accessibility-1.1.md` | — |
| EPUB A11y Metadata | 2021 | W3C Note | https://www.w3.org/2021/a11y-discov-vocab/latest/ | `standards/epub/epub-metadata-schema.md` | — |
| WebVTT | 1.0 (Nov 2019) | W3C Recommendation | https://www.w3.org/TR/webvtt1/ | `media/video/webvtt-spec.md` | — |
| Alt Text Decision Tree | — | W3C Tutorial | https://www.w3.org/WAI/tutorials/images/decision-tree/ | `media/images/alt-text-decision-tree.md` | — |
| COGA Design Guide | 2021 | W3C Candidate Recommendation | https://www.w3.org/TR/coga-usable/ | `cognitive/coga-design-guide.md` | — |
| COGA Overview | — | W3C Resource | https://www.w3.org/WAI/cognitive/ | `cognitive/coga-overview.md` | — |

---

## US Government Standards

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| Section 508 Technical Standards | 2017 Refresh | Federal Regulation | https://www.access-board.gov/ict/ | `standards/section-508/section-508-technical-standards.md` | — |
| Section 508 Overview | Current | Federal Resource | https://www.section508.gov/manage/laws-and-policies/ | `standards/section-508/section-508-overview.md` | — |
| Plain Language Guidelines | Current | Federal Guidelines | https://www.plainlanguage.gov/guidelines/ | `domains/documents/plain-language/plain-language-guide.md` | — |

---

## European Standards

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| EN 301 549 | v3.2.1 (2021) | ETSI/CEN/CENELEC Standard | https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf | `standards/en-301-549/en-301-549-requirements.md` | — |

Note: EN 301 549 is a PDF. Fetch with `pdfplumber`. The standard incorporates WCAG 2.1 Level AA by reference (Chapter 9) and adds requirements for non-web ICT (Chapters 5–8, 10–13).

---

## ISO Standards

| Standard | Version | Status | Source URL | Target File | Notes |
|----------|---------|--------|-----------|-------------|-------|
| PDF/UA (ISO 14289-1) | 2014 | ISO Standard | https://pdfa.org/resource/iso-14289-pdfua/ | `standards/pdf-ua/pdf-ua-overview.md` | Summary free; full ISO requires purchase |
| Matterhorn Protocol 1.1 | 1.1 | PDF Association | https://pdfa.org/resource/the-matterhorn-protocol/ | `standards/pdf-ua/matterhorn-protocol.md` | Free PDF |
| ISO 9241-171 | 2008 | ISO Standard | (ISO store — requires purchase) | `standards/other-standards/iso-9241-171.md` | Ergonomics of software accessibility |

---

## Fetch Script Configuration

Each standard family has a corresponding fetch script in `/scripts/`:

| Script | Standards Fetched |
|--------|------------------|
| `scripts/fetch-wcag.py` | WCAG 2.1, 2.2, 3.0, quick refs, techniques, understanding docs |
| `scripts/fetch-aria.py` | WAI-ARIA 1.2 roles, states/props, ARIA in HTML, APG patterns |
| `scripts/fetch-w3c-other.py` | ATAG, UAAG, EPUB, WebVTT, alt text tree, COGA, EPUB metadata |
| `scripts/fetch-us-gov.py` | Section 508 (Access Board + section508.gov), Plain Language |
| `scripts/fetch-en-301-549.py` | EN 301 549 PDF (uses pdfplumber) |
| `scripts/fetch-iso.py` | PDF/UA summary, Matterhorn Protocol |

---

## Version Tracking

| Standard | Current Tracked Version | Next Expected Version | Expected Date |
|----------|------------------------|----------------------|---------------|
| WCAG 2.2 | 2.2 (Oct 2023) | No planned update | — |
| WCAG 3.0 | Working Draft | First Public Working Draft updates | Ongoing |
| WAI-ARIA | 1.2 (Jun 2023) | 1.3 (in development) | TBD |
| ARIA APG | Living document | Continuous | Monthly |
| EPUB Accessibility | 1.1 (May 2023) | 1.2 (in development) | TBD |
| EN 301 549 | v3.2.1 (2021) | v4.x (planned) | TBD |
| Section 508 | 2017 Refresh | No planned update | — |

---

## Notes

- W3C standards are freely available HTML pages and can be fetched with requests + BeautifulSoup.
- EN 301 549 is a PDF requiring pdfplumber for extraction.
- ISO standards require purchase; only free summaries and the Matterhorn Protocol are auto-fetchable.
- Platform social media guides are not in this registry — they are manually maintained in `/domains/social-media/platforms/`.
- All auto-fetched content goes through frontmatter injection before writing to target files.
