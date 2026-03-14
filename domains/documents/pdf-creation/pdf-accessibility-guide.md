---
title: "PDF Accessibility Guide"
standard: "PDF/UA (ISO 14289-1) + WCAG 2.2 + Section 508"
source_url: "https://pdfa.org/resource/pdf-ua/"
domain: ["documents"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["pdf", "pdf-ua", "adobe-acrobat", "tagging", "remediation", "documents"]
ai_context: "How to create and remediate accessible PDF documents. Covers tagging, reading order, alt text, and testing. Load when advising on PDF accessibility."
---

# PDF Accessibility Guide

---

## Why PDFs Are Accessibility-Critical

PDFs are the most common inaccessible document format. The root problem: PDFs rendered from print workflows have no semantic structure — they are images of text unless explicitly tagged.

An untagged PDF is completely inaccessible to screen readers.

---

## PDF Accessibility Requirements (PDF/UA + Section 508)

| Requirement | Standard |
|------------|---------|
| Document must be tagged | PDF/UA 7.1 |
| Tags must reflect reading order | PDF/UA 7.2 |
| All images need alt text | PDF/UA 7.3 |
| Document language specified | PDF/UA 7.2 |
| Document title in metadata | PDF/UA 7.1 |
| Bookmarks for documents > 9 pages | PDF/UA 7.1 |
| No flicker content | PDF/UA 7.1 |
| Tables properly tagged | PDF/UA 7.5 |
| Form fields labeled | PDF/UA 7.18 |
| Text not part of an image | PDF/UA 7.1 |

---

## Best Source: Create from Accessible Source Document

The best way to create an accessible PDF is to start from an accessible Word, PowerPoint, or InDesign file.

**Workflow:**
1. Create document with proper structure (headings, lists, alt text) in source application
2. Export with accessibility tags enabled
3. Verify tags in Adobe Acrobat

**Word → PDF:** File → Save As → PDF → Options → Check "Document structure tags for accessibility"

**Do NOT:**
- Print to PDF (loses all structure)
- Scan a paper document without OCR + tagging

---

## Tag Types

PDF tags parallel HTML elements. Key tags:

| PDF Tag | Equivalent | Use |
|---------|-----------|-----|
| `<H1>` through `<H6>` | `<h1>`–`<h6>` | Headings |
| `<P>` | `<p>` | Paragraph |
| `<L>` | `<ul>` or `<ol>` | List container |
| `<LI>` | `<li>` | List item |
| `<LBody>` | — | List item body |
| `<Table>` | `<table>` | Table |
| `<TR>` | `<tr>` | Table row |
| `<TH>` | `<th>` | Table header cell |
| `<TD>` | `<td>` | Table data cell |
| `<Figure>` | — | Image or graphic |
| `<Artifact>` | `alt=""` | Decorative element |
| `<Link>` | `<a>` | Hyperlink |
| `<Form>` | `<form>` | Form element |
| `<TOC>` | — | Table of contents |

---

## Checking Accessibility in Adobe Acrobat

### Full Accessibility Check

1. Tools → Accessibility → Full Check (or Accessibility Checker)
2. Select all categories
3. Run
4. Review results in the Accessibility Checker panel

### Reading Order Check

1. Tools → Accessibility → Reading Order
2. The Reading Order panel shows tagged content with order numbers
3. Verify the numbers match the logical reading sequence

### Tags Panel

1. View → Show/Hide → Navigation Panes → Tags
2. The Tags tree shows all PDF tags
3. Expand to verify headings, paragraphs, lists, tables

---

## Remediation in Adobe Acrobat Pro

### Adding Tags to an Untagged PDF

1. Tools → Accessibility → Add Tags to Document
2. Acrobat auto-tags — this is a starting point only; always verify manually
3. Review and fix the tag tree

### Fixing Reading Order

1. Tools → Accessibility → Reading Order
2. Click and drag to reorder content blocks
3. Use the Reading Order panel to assign correct tag types

### Adding Alt Text to Images

1. Tools → Accessibility → Reading Order
2. Right-click image → Edit Alternate Text
3. Enter description; save

**Or:** Right-click image in PDF → Properties → Tag tab → Add alternate text

### Fixing Tables

1. View → Navigation Panes → Tags
2. Expand the `<Table>` tag
3. Right-click `<TD>` cells that should be headers → Properties → Change Type to `<TH>`
4. Right-click `<TH>` → Properties → Scope → Set to "Column" or "Row"

### Setting Document Language

1. File → Properties → Advanced tab
2. Reading Options → Language → Select language

### Setting Document Title

1. File → Properties → Description tab
2. Fill in "Title" field
3. In the Initial View tab: Window Options → "Show: Document Title"

---

## PDF Forms Accessibility

Accessible PDF forms require:

1. **Every field labeled** — form fields need tooltip/title text visible to screen readers
2. **Tab order matches visual order** — verify tab order in Acrobat
3. **Required fields marked** — use "Required" property in field settings
4. **Error messages** — validate with visual error indicators + text

### Adding Labels to Form Fields (Acrobat Pro)

1. Tools → Prepare Form
2. Right-click any field → Properties
3. General tab → Tooltip → Enter field description
4. Example: "First name" not "Text1"

### Setting Tab Order

1. File → Properties → Tab Order tab
2. Select "Use Document Structure" for logical order
3. Or: Page Thumbnails → right-click page → Page Properties → Tab Order

---

## Scanned PDFs

A scanned PDF is an image — there is no text, no tags, no accessibility.

### Remediation

1. Open scanned PDF in Adobe Acrobat Pro
2. Tools → Enhance Scans → Recognize Text (OCR)
3. Select language → Run OCR
4. Verify recognized text for accuracy
5. Add tags (Tools → Accessibility → Add Tags to Document)
6. Manually verify and fix tag tree

**Note:** OCR can introduce errors, especially with non-standard fonts, handwriting, or low-resolution scans. Always review.

---

## PDF Bookmarks

Documents with 9+ pages should have bookmarks for navigation.

1. View → Navigation Panes → Bookmarks
2. Or: automatically generated from heading structure if using Word export

Bookmarks should mirror the heading structure.

---

## Testing PDF Accessibility

| Tool | Method | Cost |
|------|--------|------|
| Adobe Acrobat Accessibility Checker | Built-in checker | Acrobat Pro |
| PAC 3 (PDF Accessibility Checker) | Free Windows tool | Free |
| CommonLook PDF Validator | Detailed report | Paid |
| NVDA + Adobe Reader | Manual screen reader test | Free |
| VoiceOver + Preview/Adobe | Manual screen reader test | Free (macOS) |

### Manual Test: Reading Order

Open PDF in Adobe Acrobat Reader. Use:
- `Tab` — move through interactive elements in order
- `Ctrl + A` (select all) → copy → paste to text editor — check if reading order is logical

### PAC 3 Testing (Windows)

PAC 3 validates against the Matterhorn Protocol's 136 PDF/UA failure conditions.

1. Download PAC 3 from pdfa.org
2. Open PDF → Run check
3. Review results by failure condition category
4. Failures prefixed with "Error" are PDF/UA violations

---

## Checklist

- [ ] Document is tagged (not an image-only PDF)
- [ ] Reading order matches visual/logical order
- [ ] Headings tagged as H1, H2, H3 (not just large bold text)
- [ ] Lists tagged as L → LI → LBody
- [ ] All images have alt text OR marked as Artifact (decorative)
- [ ] Tables: TH with scope, properly nested
- [ ] Form fields have tooltips/labels
- [ ] Document language set
- [ ] Document title in metadata and shown in title bar
- [ ] Bookmarks present (for 9+ page documents)
- [ ] Color is not the only way to convey information
- [ ] No scanned/image-only pages
- [ ] Accessibility Checker: no errors or failures
