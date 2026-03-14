---
title: "PDF Remediation Guide"
standard: "PDF/UA + WCAG + Section 508"
source_url: "https://pdfa.org/resource/the-matterhorn-protocol/"
domain: ["documents"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["pdf", "remediation", "acrobat", "documents", "tags"]
ai_context: "Focused guide to remediating existing PDFs. Load when the PDF already exists and needs repair rather than source-document fixes."
---

# PDF Remediation Guide

Remediation is the process of repairing an existing PDF so that structure, reading order, images, forms, and metadata are accessible.

---

## Typical Remediation Workflow

1. Run OCR if the PDF is scanned
2. Add tags if none exist
3. Fix reading order
4. Repair headings, lists, and tables
5. Add alt text to figures
6. Label form fields and verify tab order
7. Set title and language
8. Run Acrobat Accessibility Checker and, where available, PAC

---

## Common Fixes

| Problem | Typical Fix |
|---------|-------------|
| Untagged PDF | Add tags, then review manually |
| Wrong reading order | Reorder in Reading Order tool or tag tree |
| Data table has no headers | Convert relevant cells to `TH` and set scope |
| Form fields named `Text1` / `CheckBox2` | Add meaningful tooltip/title text |
| Decorative graphics announced | Mark as artifact |
| Scanned text only | OCR, then repair tags |

---

## When Not to Remediate in PDF First

If the source file still exists and is editable, it is often faster and higher quality to fix the source document and re-export than to remediate the PDF directly.
