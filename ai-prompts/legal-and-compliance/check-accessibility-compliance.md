---
title: "Prompt Template: Accessibility Compliance Review"
standard: "WCAG + Section 508 + ADA + EAA"
source_url: ""
domain: ["legal-and-compliance", "general"]
last_fetched: "2026-03-14"
status: "template"
tags: ["ai-prompt", "legal", "compliance", "wcag", "template"]
ai_context: "Prompt pack for mapping accessibility findings to legal and regulatory frameworks."
---

# Prompt Template: Accessibility Compliance Review

## Context Files to Load

```
standards/wcag/wcag-2.2-quick-ref.md
standards/section-508/section-508-overview.md
standards/section-508/section-508-technical-standards.md
legal-and-compliance/us-ada-overview.md
legal-and-compliance/eu-eaa-overview.md
legal-and-compliance/uk-accessibility-regulations.md
legal-and-compliance/canada-accessibility.md
legal-and-compliance/australia-accessibility.md
```

## Prompt

```
Assess this product, document, site, or service for accessibility compliance risk.

Jurisdiction: [US federal / US public sector / US private sector / EU / UK / Canada / Australia]
Asset type: [website / mobile app / PDF / social content / kiosk / software]
Known findings or issues: [paste findings]

Requirements:
1. Distinguish between normative requirements and risk indicators
2. State whether each issue maps to WCAG, Section 508, ADA, EAA, or another framework
3. Do not provide legal advice; identify compliance implications only
4. Flag where manual legal review is needed

Return:
- Compliance summary
- Issue-to-framework mapping table
- Highest-risk gaps
- Questions for legal/compliance counsel
```
