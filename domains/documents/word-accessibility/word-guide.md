---
title: "Microsoft Word Accessibility Guide"
standard: "WCAG + PDF/UA + Section 508"
source_url: "https://support.microsoft.com/en-us/office/make-your-word-documents-accessible-d9bf3683-87ac-47ea-b91a-78dcacb3c66d"
domain: ["documents"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["word", "microsoft", "documents", "headings", "alt-text", "accessibility-checker"]
ai_context: "How to create accessible Microsoft Word documents. Load when advising on Word document accessibility or document remediation."
---

# Microsoft Word Accessibility Guide

---

## Use Heading Styles (Not Manual Formatting)

The most critical Word accessibility requirement: use built-in heading styles to create document structure. Do not format text as a heading by making it large and bold — that creates no semantic structure.

### How to Apply Heading Styles

**Ribbon method:**
1. Select your heading text
2. Home tab → Styles group → Select Heading 1, Heading 2, etc.

**Keyboard method:**
- Heading 1: `Ctrl + Alt + 1`
- Heading 2: `Ctrl + Alt + 2`
- Heading 3: `Ctrl + Alt + 3`
- Normal text: `Ctrl + Alt + N`

### Heading Hierarchy Rules

- Document title → Heading 1 (usually)
- Major sections → Heading 2
- Subsections → Heading 3
- Keep heading levels consistent with the document outline; avoid unnecessary jumps

---

## Lists

Use the built-in list tools, not manual hyphen+space formatting.

**Bulleted list:** Home → Paragraph group → Bullets button
**Numbered list:** Home → Paragraph group → Numbering button

Why this matters: Proper list markup tells screen readers "this is a list with N items." Manually typed bullets are just text.

---

## Alt Text for Images

Every meaningful image must have alt text.

### Adding Alt Text

**Right-click method:**
1. Right-click the image
2. Select "Edit Alt Text…"
3. Type description in the text field
4. Click outside to save

**Ribbon method:**
1. Click image to select it
2. Format tab → Accessibility group → Alt Text

### Decorative Images

For purely decorative images:
1. Open Edit Alt Text
2. Check "Mark as decorative"

This sets `alt=""` when exported to PDF or HTML.

### Alt Text Best Practices

- Describe content and function, not appearance
- Include text that appears in the image
- Keep under 250 characters for simple images
- Complex images (charts): add description in surrounding text, reference in alt text

---

## Tables

Use simple tables with proper header rows.

### Creating an Accessible Table

1. Insert → Table → choose dimensions
2. Select the first row
3. Table Design tab → check "Header Row"
4. Right-click first row → Table Properties → Row tab → check "Repeat as header row at the top of each page"

### Table Properties for Accessibility

1. Right-click table → Table Properties
2. "Alt Text" tab → add a title and description

### Avoid:

- Nested tables (table within a table)
- Merged cells used only for visual spacing
- Blank rows or columns as spacers
- Text boxes instead of table cells

---

## Links

Links must have descriptive text. Avoid "click here" or "read more."

### Making Links Accessible

1. Select the link text
2. Right-click → Edit Hyperlink
3. In "Text to display" field, ensure text is descriptive
4. In "ScreenTip" field (optional), add more context

**Or use:** Insert → Links → Link

### Link text examples

| Wrong | Correct |
|-------|---------|
| Click here | Download the 2025 Annual Report (PDF, 2.4 MB) |
| More information | More information about our return policy |
| Read more | Read more about WCAG |

---

## Document Language

Set the document's language for correct screen reader pronunciation.

1. File → Options → Language
2. Under "Office authoring languages," select primary language
3. Or: Review tab → Language → Set Proofing Language

---

## Document Properties

Set the document title (shown in PDF title bar and screen reader).

1. File → Info → Properties (right panel)
2. Enter "Title" in the properties panel

---

## Color and Contrast

Word documents should meet WCAG 1.4.3 contrast requirements (4.5:1 for body text).

- Do not convey information by color alone
- Ensure body text meets 4.5:1 contrast against background
- Avoid light grey text on white backgrounds

---

## Text Boxes

Text boxes in Word are typically read out of document reading order and may be invisible to screen readers.

**Recommendation:** Avoid text boxes. Use table cells or paragraph text instead.

If text boxes are unavoidable:
1. Right-click text box → Format Shape
2. Size & Properties → Alt Text: describe the content

---

## Running the Accessibility Checker

Word has a built-in accessibility checker.

1. Review tab → Check Accessibility
2. The "Accessibility" pane opens on the right
3. Errors — must fix (missing alt text, no header row, etc.)
4. Warnings — should fix
5. Tips — recommended improvements

**Run the checker before saving the final version.**

### Common Checker Results

| Issue | What it means | Fix |
|-------|--------------|-----|
| Missing Alt Text | Image has no alt text | Add alt text or mark decorative |
| No header row | Table lacks header row | Repeat first row as header |
| Merged cells | Table has merged cells | Simplify table structure |
| Hard to read text contrast | Text fails 4.5:1 | Change text or background color |
| Missing document title | No title in File Properties | Add title in File → Properties |
| Repeated blank characters | Spaces used as formatting | Remove and use proper spacing |
| Use of floating objects | Image anchored incorrectly | Set image wrap to "In Line with Text" |

---

## Images: Inline vs. Floating

**Always use "In Line with Text" image wrapping** for screen reader compatibility.

1. Click image
2. Picture Format tab → Wrap Text → In Line with Text

Floating images (Square, Tight, Through) are not reliably read by screen readers in correct order.

---

## Exporting to PDF

When converting a Word document to PDF:
1. File → Save As → PDF
2. Click "Options…"
3. Ensure "Document structure tags for accessibility" is checked
4. Ensure "Document properties" is checked
5. Click OK and Save

This preserves heading structure, alt text, language, and tags in the PDF.

**Do NOT use: Print → Print to PDF** — this flattens the document and loses all accessibility structure.

---

## Checklist

- [ ] Heading styles used (H1, H2, H3) — not manual bold/large text
- [ ] Lists use built-in list tools
- [ ] All meaningful images have alt text
- [ ] Decorative images marked as decorative
- [ ] Tables have header row with "Repeat header row" enabled
- [ ] All links have descriptive text
- [ ] Document language set
- [ ] Document title in File Properties
- [ ] Color is not used as the only way to convey information
- [ ] Accessibility Checker shows no errors
- [ ] PDF export includes document structure tags
