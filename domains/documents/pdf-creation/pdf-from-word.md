---
title: "Creating Accessible PDF from Word"
standard: "PDF/UA + WCAG + Section 508"
source_url: "https://pdfa.org/resource/pdf-ua/"
domain: ["documents"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["pdf", "word", "export", "documents", "tags"]
ai_context: "Workflow for creating accessible PDFs from Word. Load when the user starts in Word and needs a tagged PDF outcome."
---

# Creating Accessible PDF from Word

The best accessible PDF usually starts as an accessible Word file.

---

## Before Export

- Use heading styles
- Use real lists and tables
- Add alt text to images
- Set document language
- Set document title
- Run Word's Accessibility Checker

---

## Export Steps

1. File → Save As → PDF
2. Click `Options...`
3. Enable `Document structure tags for accessibility`
4. Enable `Document properties`
5. Save

Do **not** use Print to PDF.

---

## After Export

Open the PDF in Acrobat and verify:

- tags exist
- heading levels are preserved
- reading order is logical
- links remain active and meaningful
- images retain alt text

If problems remain, move to `domains/documents/pdf-creation/pdf-remediation.md`.
