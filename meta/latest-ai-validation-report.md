---
title: "Latest AI Validation Report"
type: "meta"
status: "curated"
last_updated: "2026-03-14"
ai_context: "Most recent AI validation run against repository fixtures and structural checks."
---

# Latest AI Validation Report

Responses evaluated: no (preflight only)

## Structural Checks

- `validate-frontmatter.py` — PASS
  Output: Frontmatter validation passed.
- `validate-references.py` — PASS
  Output: Reference validation passed.

## Pattern Checks

### Pattern 1: Web Accessibility Audit

- Prompt file: `ai-prompts/web-content/audit-html-snippet.md`
- Result: PASS
- Expected citations: `SC 2.4.4`, `SC 2.5.3`

### Pattern 2: Accessible Web Component Generation

- Prompt file: `ai-prompts/web-content/generate-accessible-component.md`
- Result: PASS
- Expected citations: `SC 2.1.1`, `SC 4.1.2`

### Pattern 3: Social Media Post Creation

- Prompt file: `ai-prompts/social-media/accessible-social-post.md`
- Result: PASS
- Expected citations: `SC 1.1.1`, `CamelCase`

### Pattern 4: Document Accessibility

- Prompt file: `ai-prompts/documents/accessible-document.md`
- Result: PASS
- Expected citations: `PDF/UA`, `Plain Language`

### Pattern 5: Legal Compliance Check

- Prompt file: `ai-prompts/legal-and-compliance/check-accessibility-compliance.md`
- Result: PASS
- Expected citations: `Section 508`, `WCAG 2.1 Level AA`

### Pattern 6: Full Web Accessibility Context

- Prompt file: `ai-prompts/web-content/full-site-accessibility-review.md`
- Result: PASS
- Expected citations: `SC 1.4.3`, `SC 3.3.2`

### Pattern 7: Voice UI and Speech Commands

- Prompt file: `ai-prompts/voice/accessible-voice-ui.md`
- Result: PASS
- Expected citations: `ISO 9241-171`, `EN 301 549`

### Pattern 8: Kiosk and Embedded / Closed Functionality

- Prompt file: `ai-prompts/physical-ict/accessible-kiosk-and-embedded.md`
- Result: PASS
- Expected citations: `EN 301 549`, `closed functionality`
