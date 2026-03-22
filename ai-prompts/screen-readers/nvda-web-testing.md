---
title: "Prompt Template: NVDA Web Testing Workflow"
standard: "NVDA + WCAG"
source_url: ""
domain: ["web"]
last_fetched: "2026-03-21"
status: "template"
tags: ["ai-prompt", "screen-reader", "nvda", "web-testing", "template"]
ai_context: "Prompt pack for planning or reviewing NVDA-based web accessibility testing."
---

# Prompt Template: NVDA Web Testing Workflow

## Context Files to Load

```
screen-readers/nvda-guide.md
screen-readers/screen-reader-overview.md
domains/web/testing/screen-reader-testing-matrix.md
domains/web/focus-management.md
```

## Prompt

```
Create an NVDA-based accessibility testing plan for this page, flow, or component.

Scope: [page / component / modal / checkout / form]
Browser: [Chrome / Firefox]
User journey: [list the steps]

Return:
- the exact NVDA commands to use
- what to verify in browse mode and forms mode
- expected announcements for headings, landmarks, controls, and live regions
- likely failure points
- remediation guidance when behavior is wrong
```
