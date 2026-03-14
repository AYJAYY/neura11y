---
title: "Microsoft Excel Accessibility Guide"
standard: "WCAG + Section 508"
source_url: "https://support.microsoft.com/en-us/office/make-your-excel-documents-accessible-6cc05fc5-1314-48b5-8eb3-683e49b3e593"
domain: ["documents"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["excel", "spreadsheets", "documents", "tables", "alt-text", "accessibility-checker"]
ai_context: "How to create accessible Microsoft Excel spreadsheets. Load when advising on Excel accessibility."
---

# Microsoft Excel Accessibility Guide

---

## Structure Spreadsheets as Tables

The most critical Excel accessibility requirement: format data ranges as proper Excel tables.

### How to Create a Table

1. Click any cell in your data range
2. Home tab → Format as Table → Select a style
3. Ensure "My table has headers" is checked

This creates a proper table structure with column headers that screen readers can identify.

### Table Benefits

- Column headers are programmatically associated with data cells
- Screen readers announce column name as users navigate
- Keyboard navigation works within the table structure
- Table name can be set for reference

### Setting a Table Name

1. Click within the table
2. Table Design tab → Table Name field (top left)
3. Enter a descriptive name: "SalesData2025" not "Table1"

---

## Cell Structure

### Column Headers

- Row 1 should contain descriptive column headers
- Headers must be unique (no two columns with the same header)
- Keep headers short and descriptive

### Avoid Merged Cells

Merged cells break the table structure and confuse screen readers.

**Instead of merging to create visual hierarchy:**
- Use separate rows with clear labels
- Use indentation (increase indent) for subordinate data
- Or use group/outline features

### Blank Rows and Columns

Remove blank rows and columns used for visual spacing. They interrupt the logical flow for screen reader navigation.

---

## Alt Text for Charts and Images

Every chart and image embedded in a worksheet needs alt text.

### Adding Alt Text to a Chart

1. Click the chart
2. Chart Format tab → Accessibility → Alt Text
3. Or right-click chart → Edit Alt Text
4. Write a description of the chart's key insight

**Good chart alt text:**
- "Bar chart showing Q4 revenue: North America $4.2M, Europe $2.9M, APAC $0.8M. North America leads by a significant margin."

**Bad chart alt text:**
- "Chart" or "Chart 1"

### Decorative Images

For decorative images or logos:
1. Right-click → Edit Alt Text
2. Check "Mark as decorative"

---

## Worksheet Navigation

### Descriptive Sheet Names

Name worksheets descriptively, not "Sheet1," "Sheet2."

Right-click the sheet tab → Rename → Type descriptive name: "Sales Data," "Employee List," "Summary"

### Logical Tab Order

Avoid data that jumps around. Screen readers navigate cells left-to-right, top-to-bottom within each row.

---

## Hyperlinks

Links must have descriptive text.

### Adding a Link

1. Select the cell or text for the link
2. Insert → Link (Ctrl + K)
3. "Text to display" should be descriptive
4. Avoid cell content like "Click here" or bare URLs

---

## Color and Contrast

- Do not use color as the only way to convey information (e.g., red cells = errors)
- Add text, symbols, or a separate column with the same information
- Ensure text meets 4.5:1 contrast against cell background

### Color-Only Example (Fails)

Red cell background means "overdue," green means "completed" — no other indicator.

### Compliant Example

Status column with text values: "Overdue," "In Progress," "Completed" (can also have color background as a visual supplement).

---

## Named Ranges

Named ranges help screen reader users navigate large spreadsheets.

1. Select a cell range
2. In the Name Box (top-left, shows cell reference), type a name
3. Or: Formulas → Define Name

Named ranges appear in the Name Box dropdown and can be navigated to quickly.

---

## Running the Accessibility Checker

1. Review tab → Check Accessibility
2. Review Errors, Warnings, and Tips

### Common Checker Results in Excel

| Issue | Fix |
|-------|-----|
| Missing alt text | Add alt text to charts and images |
| Sheet tab has default name | Rename Sheet1 to descriptive name |
| Table header row missing | Format data range as table with header row |
| Merged cells | Remove merges; use alternative formatting |
| Hard to read text contrast | Adjust cell background or font color |
| Hyperlink text not descriptive | Change "Click here" to descriptive text |
| Blank cells in table | Remove blank rows/columns in data table |

---

## Exporting Accessible Spreadsheets

### Export to PDF

1. File → Save As → PDF
2. Options → check "Document structure tags for accessibility"

Note: Excel PDFs are often less accessible than Word PDFs. Complex spreadsheets with many worksheets may need additional PDF remediation.

### Sharing as Excel File

When sharing the native .xlsx file, all table structure and alt text is preserved. This is often preferred over PDF for data that users need to interact with.

---

## Checklist

- [ ] Data formatted as Excel Tables (not loose cell ranges)
- [ ] Column headers are unique and descriptive
- [ ] No merged cells for layout purposes
- [ ] No blank rows or columns used for spacing
- [ ] All charts have descriptive alt text with key insight
- [ ] Decorative images marked as decorative
- [ ] Worksheet tabs have descriptive names
- [ ] Hyperlinks have descriptive text
- [ ] Color is not the only way to convey information
- [ ] Text contrast meets 4.5:1
- [ ] Accessibility Checker shows no errors
