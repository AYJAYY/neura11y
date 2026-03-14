---
title: "Word Styles and Structure Guide"
standard: "WCAG + PDF/UA"
source_url: "https://support.microsoft.com/en-us/office/make-your-word-documents-accessible-d9bf3683-87ac-47ea-b91a-78dcacb3c66d"
domain: ["documents"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["word", "styles", "headings", "structure", "documents"]
ai_context: "Focused guide to Word styles and document structure. Load when the question is specifically about headings, lists, or structural markup in Word."
---

# Word Styles and Structure Guide

Styles are the semantic structure of a Word document. They determine how screen readers, navigation panes, and PDF export understand the document.

---

## Heading Styles

- Use `Heading 1` for the document title or top-level section.
- Use `Heading 2` for major sections.
- Use `Heading 3` and below for subsections.
- Do not jump levels unless the content hierarchy really skips a level.

### Why Styles Matter

- Screen readers can jump by heading
- Word Navigation Pane reflects the style hierarchy
- Tagged PDF export depends on these styles

---

## Lists

- Use built-in list formatting for ordered and unordered lists.
- Do not fake lists with hyphens, tabs, or repeated spaces.

---

## Table of Contents

Automatic tables of contents depend on heading styles.

- References → Table of Contents
- Update after major edits

This improves navigation for all users and exports better to PDF bookmarks.

---

## Common Structural Mistakes

| Mistake | Why It Fails |
|---------|--------------|
| Manual bold/large text used as a heading | no semantic structure |
| Tabs/spaces used for layout | reading order and spacing become unreliable |
| Text boxes used for main content | often read out of order |
| Blank paragraphs for spacing | noisy navigation and inconsistent output |
