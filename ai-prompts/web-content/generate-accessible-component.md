---
title: "Prompt Template: Generate Accessible Web Component"
standard: "WCAG 2.2 + WAI-ARIA 1.2"
source_url: ""
domain: ["web"]
last_fetched: "2026-03-14"
status: "template"
tags: ["ai-prompt", "web", "components", "aria", "template"]
ai_context: "Prompt pack for generating accessible interactive web components with WCAG and ARIA support."
---

# Prompt Template: Generate Accessible Web Component

## Context Files to Load

```
standards/wcag/wcag-2.2-quick-ref.md
standards/aria/wai-aria-1.2-roles.md
standards/aria/wai-aria-1.2-states-properties.md
standards/aria/aria-authoring-practices.md
domains/web/component-patterns/[component-name].md
domains/web/keyboard-navigation-patterns.md
domains/web/focus-management.md
```

## Base Prompt

```
Generate an accessible [component-name] for the web.

Requirements:
1. Use native HTML first; use ARIA only where native semantics are insufficient
2. Match WCAG 2.2 Level AA requirements
3. Include keyboard interaction details
4. Include focus management behavior
5. Include accessible name/role/state handling
6. Explain any screen reader announcements or live-region behavior

Return:
- HTML
- CSS hooks or state classes if needed
- JavaScript behavior
- Keyboard interaction table
- Accessibility notes citing WCAG or ARIA requirements
```

## Review Prompt

```
Review this [component-name] implementation for accessibility defects.

Check:
- correct role and state usage
- accessible name computation
- focus entry, containment, and exit
- keyboard support for Tab, Shift+Tab, Enter, Space, Escape, Arrow keys where relevant
- visible focus styling
- error states or status announcements

Return:
- [FAIL], [WARN], or [BEST PRACTICE]
- exact code changes required
- WCAG SC number and ARIA rule when applicable
```
