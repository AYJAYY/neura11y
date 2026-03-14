---
title: "Prompt Template: Full Web Accessibility Review"
standard: "WCAG + WAI-ARIA 1.2"
source_url: ""
domain: ["web"]
last_fetched: "2026-03-14"
status: "template"
tags: ["ai-prompt", "web", "audit", "site-review", "template"]
ai_context: "Prompt pack for broader site reviews using the full web accessibility context stack."
---

# Prompt Template: Full Web Accessibility Review

## Context Files to Load

```
standards/wcag/wcag-2.2-quick-ref.md
standards/wcag/wcag-conformance-levels.md
standards/aria/wai-aria-1.2-roles.md
standards/aria/wai-aria-1.2-states-properties.md
domains/web/web-accessibility-checklist.md
domains/web/html-semantics-guide.md
domains/web/forms-accessibility.md
domains/web/keyboard-navigation-patterns.md
domains/web/focus-management.md
domains/web/color-and-contrast.md
```

## Prompt

```
Review this website or page set for WCAG Level AA conformance.

Scope:
- URLs or templates under review: [list]
- Primary user journeys: [list]
- Known technologies: [CMS / framework / design system]

Tasks:
1. Identify likely failures by WCAG principle
2. Separate definitive failures from items that require manual testing
3. Call out repeated-pattern issues that may affect many pages
4. Provide a remediation plan ordered by severity and implementation effort

Return:
- Executive summary
- Issues grouped by WCAG principle
- Manual testing checklist
- Priority remediation backlog
- Citations for every normative claim
```
