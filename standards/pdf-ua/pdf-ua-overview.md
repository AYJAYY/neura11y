---
title: "PDF/UA Overview"
standard: "PDF/UA (ISO 14289-1)"
source_url: "https://pdfa.org/resource/pdf-ua/"
domain: ["documents"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["pdf", "pdf-ua", "iso-14289", "documents", "accessibility"]
ai_context: "PDF/UA (Universal Accessibility) standard overview. Load when creating or auditing accessible PDF documents."
---

# PDF/UA (ISO 14289-1) Overview

PDF/UA is the ISO standard for accessible PDF documents. "UA" stands for Universal Accessibility. The standard defines requirements for PDF files that enable use with assistive technology.

**Full standard:** ISO 14289-1:2014 (requires purchase)
**Free summary:** https://pdfa.org/resource/pdf-ua/
**Matterhorn Protocol:** https://pdfa.org/resource/matterhorn-protocol/ (136 testable checkpoints)

---

## What PDF/UA Requires

PDF/UA is organized around the PDF format's accessibility features:

### 1. Document Tagging

All real content must be tagged. Tags define the logical structure and reading order.

Required tag types:
- `<Document>` — Root tag
- `<Part>` / `<Sect>` — Document divisions
- `<H1>`–`<H6>` — Headings
- `<P>` — Paragraphs
- `<L>` — Lists; `<LI>` — List items; `<LBody>` — List body
- `<Table>`, `<TR>`, `<TH>`, `<TD>` — Tables
- `<Figure>` — Images, charts
- `<Caption>` — Figure and table captions
- `<TOC>`, `<TOCI>` — Table of contents entries
- `<Link>` — Hyperlinks
- `<Note>` — Footnotes/endnotes
- `<Artifact>` — Decorative content (excluded from reading order)

### 2. Reading Order

The logical reading order (as conveyed to AT by tag order) must match the visual presentation order. Column-based layouts must be tagged in column order, not visual left-to-right order that crosses columns.

### 3. Alternative Text

All non-decorative images, charts, and figures must have `Alt` text in their tag attributes. Decorative elements must be tagged as `Artifact`.

### 4. Language

The document must specify a natural language (`/Lang` entry in the catalog dictionary). Passages in different languages must specify their language.

### 5. Security

Security settings must not prevent AT from accessing document content. DRM that blocks screen readers is not permitted.

### 6. Fonts

All fonts must be embedded. Character encoding must allow text extraction (Unicode mapping required).

### 7. Color and Contrast

No information conveyed by color alone. (Aligns with WCAG 1.4.1.)

### 8. Bookmarks/Navigation

Documents with 21 or more pages must include bookmarks (navigation pane). Bookmarks must match heading structure.

### 9. Document Title

The document's title must be set in the document properties, and the title must be the displayed window title (not the filename).

### 10. Headings Must Be Nested

Heading tags must not skip levels (e.g., `<H1>` directly to `<H3>`). Must be nested correctly.

### 11. Tables

Header cells must be `<TH>` with scope. Tables used for layout must be tagged as Artifact or use `<Table>` without header designations.

### 12. Links

All hyperlinks must be tagged as `<Link>` with associated text and an `Alt` attribute if the link text is insufficient. Links must have an active rectangle that overlaps with the visible text.

### 13. Annotations

All annotations (comments, form fields, media clips) must have alt text. Form fields must have a `TU` (tooltip/alternate description) entry.

### 14. Form Fields

Interactive form fields must:
- Have meaningful names (TU entry)
- Have a `Tab` order following logical reading order
- Be keyboard operable

---

## Matterhorn Protocol Checkpoints

The Matterhorn Protocol 1.1 (PDF Association, 2014) defines 136 testable checkpoints for PDF/UA conformance. Organized in 31 problem categories.

Key checkpoint categories:

| Category | Description | Checkpoints |
|----------|-------------|-------------|
| 01 | Document — General | 01-001 to 01-007 |
| 06 | Graphics | 06-001 to 06-003 |
| 07 | Headings | 07-001 to 07-003 |
| 09 | Natural language | 09-001 to 09-003 |
| 13 | Graphics (Alt text) | 13-001 to 13-004 |
| 14 | Headers in tables | 14-001 to 14-002 |
| 15 | Lists | 15-001 to 15-004 |
| 16 | Mathematical formulas | 16-001 |
| 17 | Metadata | 17-001 to 17-002 |
| 22 | Objects/figures | 22-001 to 22-002 |
| 25 | Page header/footer | 25-001 to 25-002 |
| 26 | Reading order | 26-001 |
| 27 | Security | 27-001 |
| 28 | Standard tag types | 28-001 to 28-019 |
| 29 | Structure types | 29-001 to 29-009 |
| 30 | Tables | 30-001 to 30-019 |
| 31 | XObjects | 31-001 to 31-002 |

---

## Creating PDF/UA-Compliant Documents

### From Microsoft Word (recommended approach)

1. Use Word's built-in accessibility features (Styles for headings, proper alt text)
2. Run Word's Accessibility Checker before export
3. Export via File → Save As → PDF with these settings:
   - Check "Document structure tags for accessibility"
   - Check "Document properties"
   - Check "Bookmarks" (for docs with headings)
4. Verify in Acrobat Pro: Tools → Accessibility → Full Check

### From Adobe InDesign

1. Apply paragraph styles for all headings and body text
2. Set reading order in Articles panel
3. Add alt text to all placed images
4. Set language for text frames
5. Export as PDF/UA: File → Export → PDF → Advanced → PDF/UA-1

### Remediation with Adobe Acrobat Pro

1. Open Tags panel (View → Show/Hide → Navigation Panes → Tags)
2. Run Accessibility Full Check (Tools → Accessibility → Full Check)
3. Fix issues: add missing tags, set reading order, add alt text
4. Verify with PAC 2024 (free PDF/UA checker)

---

## PDF/UA Testing Tools

| Tool | Type | Cost | URL |
|------|------|------|-----|
| PAC 2024 | PDF/UA checker | Free | https://pac.pdf-accessible.com/ |
| Adobe Acrobat Pro | Authoring + checking | Paid | adobe.com |
| axesPDF | Remediation | Paid | axespdf.com |
| CommonLook PDF | Remediation | Paid | commonlook.com |
| NVDA + Adobe Reader | Manual AT testing | Free | — |
| Adobe Accessibility Checker | Basic check | Free (in Acrobat) | — |

---

## PDF/UA vs WCAG

PDF/UA and WCAG are complementary:
- WCAG 1.1.1 (Non-text content) → PDF/UA: Alt text on `<Figure>` tags
- WCAG 1.3.1 (Info and Relationships) → PDF/UA: Tag structure, table headers
- WCAG 1.3.2 (Meaningful Sequence) → PDF/UA: Reading order
- WCAG 2.4.2 (Page Titled) → PDF/UA: Document title in properties
- WCAG 4.1.2 (Name, Role, Value) → PDF/UA: Form field TU entries

For document accessibility, aim for both WCAG 2.1 AA and PDF/UA-1 compliance.
