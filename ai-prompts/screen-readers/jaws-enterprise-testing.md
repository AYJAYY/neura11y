---
title: "Prompt Template: JAWS Enterprise Testing"
standard: "JAWS + WCAG"
source_url: ""
domain: ["web", "documents"]
last_fetched: "2026-03-21"
status: "template"
tags: ["ai-prompt", "screen-reader", "jaws", "enterprise", "template"]
ai_context: "Prompt pack for planning JAWS testing in enterprise or government accessibility workflows."
---

# Prompt Template: JAWS Enterprise Testing

## Context Files to Load

```
screen-readers/jaws-guide.md
screen-readers/screen-reader-overview.md
domains/web/testing/screen-reader-testing-matrix.md
domains/web/focus-management.md
```

## Prompt

```
Create a JAWS-focused testing plan for this experience.

Experience type: [web app / internal tool / document workflow / form-heavy flow]
Browser: [Chrome / Edge]
Primary tasks: [list]

Return:
- the exact JAWS commands to use
- what to verify with virtual cursor, forms mode, headings, landmarks, and tables
- expected announcements for key controls and status messages
- enterprise-specific risks to flag
- remediation guidance grounded in native semantics first and ARIA second
```
