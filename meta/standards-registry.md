---
title: "Standards Registry"
type: "meta"
status: "curated"
last_updated: "2026-03-21"
ai_context: "Master list of all accessibility standards tracked in this repository, with canonical URLs, current versions, and fetch status. Use to validate source URLs before fetching."
---

# Standards Registry

Master source-of-truth for all standards tracked in this repository. All fetch scripts reference this file for source URLs.

---

## W3C Standards

### WCAG (Web Content Accessibility Guidelines)

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| WCAG 2.1 | 2.1 (June 2018) | W3C Recommendation | https://www.w3.org/TR/WCAG21/ | `standards/wcag/wcag-2.1-full.md` | 2026-03-13 |
| WCAG 2.2 | 2.2 (October 2023) | W3C Recommendation | https://www.w3.org/TR/WCAG22/ | `standards/wcag/wcag-2.2-full.md` | 2026-03-13 |
| WCAG 3.0 | 3.0 (Working Draft) | W3C Working Draft | https://www.w3.org/TR/wcag-3.0/ | `standards/wcag/wcag-3.0-overview.md` | 2026-03-13 |
| WCAG 2.1 Quick Ref | 2.1 | Living Document | https://www.w3.org/WAI/WCAG21/quickref/ | `standards/wcag/wcag-2.1-quick-ref.md` | 2026-03-13 |
| WCAG 2.2 Quick Ref | 2.2 | Living Document | https://www.w3.org/WAI/WCAG22/quickref/ | `standards/wcag/wcag-2.2-quick-ref.md` | 2026-03-14 |
| WCAG Techniques (2.1) | 2.1 | Living Document | https://www.w3.org/WAI/WCAG21/Techniques/ | `standards/wcag/wcag-techniques/` | — |
| WCAG Techniques (2.2) | 2.2 | Living Document | https://www.w3.org/WAI/WCAG22/Techniques/ | `standards/wcag/wcag-techniques/` | — |
| Understanding WCAG 2.2 | 2.2 | Living Document | https://www.w3.org/WAI/WCAG22/Understanding/ | `standards/wcag/wcag-understanding/` | — |

### WAI-ARIA

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| WAI-ARIA | 1.2 (June 2023) | W3C Recommendation | https://www.w3.org/TR/wai-aria-1.2/ | `standards/aria/wai-aria-1.2-roles.md` | 2026-03-13 |
| AccName | 1.2 (11 March 2026) | W3C Working Draft | https://www.w3.org/TR/accname-1.2/ | `standards/aria/accname-1.2.md` | 2026-03-21 |
| Core-AAM | 1.2 (11 March 2026) | W3C Candidate Recommendation Draft | https://www.w3.org/TR/core-aam-1.2/ | `standards/aria/core-aam-1.2-overview.md` (primary canonical file; full raw capture in `standards/aria/core-aam-1.2-full-fetched.md`) | 2026-03-21 |
| HTML-AAM | 1.0 (11 March 2026) | W3C Working Draft | https://www.w3.org/TR/html-aam-1.0/ | `standards/aria/html-aam-1.0-overview.md` (primary canonical file; full raw capture in `standards/aria/html-aam-1.0-full-fetched.md`) | 2026-03-21 |
| WAI-ARIA States/Props | 1.2 | W3C Recommendation | https://www.w3.org/TR/wai-aria-1.2/#state_prop_def | `standards/aria/wai-aria-1.2-states-properties.md` | 2026-03-13 |
| ARIA in HTML | 2023 | W3C Recommendation | https://www.w3.org/TR/html-aria/ | `standards/aria/aria-in-html.md` | 2026-03-13 |
| ARIA APG Patterns | 2024 | Living Document | https://www.w3.org/WAI/ARIA/apg/patterns/ | `standards/aria/aria-authoring-practices.md` | 2026-03-13 |

### Other W3C Standards

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| ATAG 2.0 | 2.0 (Sept 2015) | W3C Recommendation | https://www.w3.org/TR/ATAG20/ | `standards/other-standards/atag-2.0-overview.md` | 2026-03-13 |
| UAAG 2.0 | 2.0 (Dec 2015) | W3C Note | https://www.w3.org/TR/UAAG20/ | `standards/other-standards/uaag-2.0-overview.md` | 2026-03-13 |
| EPUB Accessibility 1.1 | 1.1 (May 2023) | W3C Recommendation | https://www.w3.org/TR/epub-a11y-11/ | `standards/epub/epub-accessibility-1.1.md` | 2026-03-13 |
| EPUB A11y Metadata | 2021 | W3C Note | https://www.w3.org/2021/a11y-discov-vocab/latest/ | `standards/epub/epub-metadata-schema.md` | 2026-03-13 |
| WebVTT | 1.0 (Nov 2019) | W3C Recommendation | https://www.w3.org/TR/webvtt1/ | `media/video/webvtt-spec.md` | 2026-03-21 |
| Alt Text Decision Tree | — | W3C Tutorial | https://www.w3.org/WAI/tutorials/images/decision-tree/ | `media/images/alt-text-decision-tree.md` | 2026-03-21 |
| COGA Design Guide | 2021 | W3C Candidate Recommendation | https://www.w3.org/TR/coga-usable/ | `cognitive/coga-design-guide.md` | 2026-03-13 |
| COGA Overview | — | W3C Resource | https://www.w3.org/WAI/cognitive/ | `cognitive/coga-overview.md` | 2026-03-13 |
| WCAG2ICT 2.2 | 11 December 2025 | W3C Group Note | https://www.w3.org/TR/wcag2ict-22/ | `standards/other-standards/wcag2ict-22-overview.md` (primary canonical file; full raw capture in `standards/other-standards/wcag2ict-22-full-fetched.md`) | 2026-03-21 |

### WAI Tutorials

| Tutorial | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| Forms Tutorial | Living Resource | W3C Tutorial | https://www.w3.org/WAI/tutorials/forms/ | `domains/web/source/wai-tutorials/forms-tutorial-fetched.md` | 2026-03-21 |
| Tables Tutorial | Living Resource | W3C Tutorial | https://www.w3.org/WAI/tutorials/tables/ | `domains/web/source/wai-tutorials/tables-tutorial-fetched.md` | 2026-03-21 |
| Page Structure Tutorial | Living Resource | W3C Tutorial | https://www.w3.org/WAI/tutorials/page-structure/ | `domains/web/source/wai-tutorials/page-structure-tutorial-fetched.md` | 2026-03-21 |
| Menus Tutorial | Living Resource | W3C Tutorial | https://www.w3.org/WAI/tutorials/menus/ | `domains/web/source/wai-tutorials/menus-tutorial-fetched.md` | 2026-03-21 |
| Images Tutorial | Living Resource | W3C Tutorial | https://www.w3.org/WAI/tutorials/images/ | `media/images/images-tutorial-fetched.md` | 2026-03-21 |

### Assistive Technology Source Docs

| Source | Version | Status | Source URL | Target File | Last Fetched |
|--------|---------|--------|-----------|-------------|--------------|
| NVDA User Guide | Living Resource | NV Access documentation | https://www.nvaccess.org/files/nvda/documentation/userGuide.html | `screen-readers/source/nvda-user-guide-fetched.md` | 2026-03-21 |
| VoiceOver User Guide for Mac | Living Resource | Apple support documentation | https://support.apple.com/guide/voiceover/welcome/mac | `screen-readers/source/voiceover-user-guide-mac-fetched.md` | 2026-03-21 |
| TalkBack Guide for Android | Living Resource | Google support documentation | https://support.google.com/accessibility/android/answer/6283677 | `screen-readers/source/talkback-user-guide-fetched.md` | 2026-03-21 |
| JAWS Keystrokes Guide | Living Resource | Freedom Scientific support documentation | https://support.freedomscientific.com/content/html/jawshq/JAWS-Keystrokes.html | `screen-readers/source/jaws-keystrokes-fetched.md` | 2026-03-21 |

---

## US Government Standards

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| Section 508 Technical Standards | 2017 Refresh | Federal Regulation | https://www.access-board.gov/ict/ | `standards/section-508/section-508-technical-standards.md` | 2026-03-13 |
| Section 508 Overview | Current | Federal Resource | https://www.section508.gov/manage/laws-and-policies/ | `standards/section-508/section-508-overview.md` | 2026-03-13 |
| Plain Language Guidelines | Current | Federal Guidelines | https://www.plainlanguage.gov/guidelines/ | `domains/documents/plain-language/plain-language-guide.md` | 2026-03-13 |

---

## European Standards

| Standard | Version | Status | Source URL | Target File | Last Fetched |
|----------|---------|--------|-----------|-------------|--------------|
| EN 301 549 | v3.2.1 (2021) | ETSI/CEN/CENELEC Standard | https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf | `standards/en-301-549/en-301-549-requirements.md` | 2026-03-13 |

Note: EN 301 549 is a PDF. Fetch with `pdfplumber`. The standard incorporates WCAG 2.1 Level AA by reference (Chapter 9) and adds requirements for non-web ICT (Chapters 5–8, 10–13).

---

## ISO Standards

| Standard | Version | Status | Source URL | Target File | Notes |
|----------|---------|--------|-----------|-------------|-------|
| PDF/UA (ISO 14289-1) | 2014 | ISO Standard | https://pdfa.org/resource/iso-14289-pdfua/ | `standards/pdf-ua/pdf-ua-overview.md` | 2026-03-13 |
| Matterhorn Protocol 1.1 | 1.1 | PDF Association | https://pdfa.org/resource/the-matterhorn-protocol/ | `standards/pdf-ua/matterhorn-protocol.md` | 2026-03-13 |
| ISO 9241-171 | 2008 | ISO Standard | (ISO store — requires purchase) | `standards/other-standards/iso-9241-171.md` | 2026-03-14 |

---

## Fetch Script Configuration

Each standard family has a corresponding fetch script in `/scripts/`:

| Script | Standards Fetched |
|--------|------------------|
| `scripts/fetch-wcag.py` | WCAG 2.1, WCAG 2.2, quick refs, techniques index, understanding index |
| `scripts/fetch-aria.py` | WAI-ARIA 1.2, AccName, Core-AAM, HTML-AAM, ARIA in HTML |
| `scripts/fetch-w3c-other.py` | ATAG, UAAG, EPUB Accessibility, WebVTT, COGA, WCAG2ICT, WAI tutorials |
| `scripts/fetch-screen-readers.py` | NVDA, VoiceOver, TalkBack, and JAWS support docs |
| `scripts/fetch-us-gov.py` | Section 508 and Plain Language |
| `scripts/fetch-en-301-549.py` | EN 301 549 PDF extraction |
| `scripts/fetch-iso.py` | PDF/UA summary and Matterhorn Protocol |

---

## Version Tracking

| Standard | Current Tracked Version | Next Expected Version | Expected Date |
|----------|------------------------|----------------------|---------------|
| WCAG 2.2 | 2.2 (Oct 2023) | No planned update | — |
| WCAG 3.0 | Working Draft | First Public Working Draft updates | Ongoing |
| WAI-ARIA | 1.2 (Jun 2023) | 1.3 (in development) | TBD |
| AccName | 1.2 (Mar 2026 WD) | Working Draft updates | Ongoing |
| Core-AAM | 1.2 (Mar 2026 CRD) | Candidate Recommendation updates | Ongoing |
| HTML-AAM | 1.0 (Mar 2026 WD) | Working Draft updates | Ongoing |
| ARIA APG | Living document | Continuous | Monthly |
| EPUB Accessibility | 1.1 (May 2023) | 1.2 (in development) | TBD |
| EN 301 549 | v3.2.1 (2021) | v4.x (planned) | TBD |
| Section 508 | 2017 Refresh | No planned update | — |

---

## Notes

- W3C standards are freely available HTML pages and can be fetched with requests + BeautifulSoup.
- WAI tutorials are also fetched as HTML and stored as supporting `*-fetched.md` provenance files.
- Large W3C sources may generate split canonical files for AI use plus a companion `*-full-fetched.md` raw capture for provenance.
- EN 301 549 is a PDF requiring pdfplumber for extraction.
- ISO standards require purchase; only free summaries and the Matterhorn Protocol are auto-fetchable.
- Platform social media guides are not in this registry — they are manually maintained in `/domains/social-media/platforms/`.
- All auto-fetched content goes through frontmatter injection before writing to target files.
- Run `scripts/sync-freshness.py` to update the `Last Fetched` column from file frontmatter and emit `meta/freshness-manifest.json`.
