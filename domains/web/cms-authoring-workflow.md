---
title: "CMS Authoring Workflow Accessibility Guide"
standard: "WCAG"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["cms", "authoring", "workflow", "content-model", "publishing"]
ai_context: "Accessibility guidance for CMS-driven publishing workflows, including content modeling, editor UX, and pre-publish QA."
---

# CMS Authoring Workflow Accessibility Guide

## Content Model Requirements

- Separate headings, body text, alt text, captions, and call-to-action labels into distinct fields
- Make alt text a first-class field on media records
- Provide explicit fields for accordion titles, table captions, and embed transcripts
- Avoid rich-text fields that encourage authors to paste entire layouts into a single blob

## Editor Workflow

- Use templates that start with correct heading levels
- Require descriptive page titles and meta descriptions
- Provide helper text for link text, alt text, and file-download labels
- Warn authors when they upload PDFs or images without the needed supporting text

## Common CMS Failure Points

- heading levels reset inside reusable components
- link buttons use generic labels like "Learn more"
- embeds lack captions or transcript links
- carousel, tab, and accordion blocks expose no usage guidance to authors

## Pre-Publish Checklist

- Verify heading hierarchy
- Check image alt text and decorative images
- Confirm link purpose is clear out of context
- Check tables for captions and simple structure
- Verify embeds and downloadable files have accessible alternatives
- Run automated checks on the rendered page, not just the editor view
