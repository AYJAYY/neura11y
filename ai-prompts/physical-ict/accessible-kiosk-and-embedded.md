---
title: "Prompt Template: Accessible Kiosk and Embedded ICT Review"
standard: "EN 301 549 + ISO 9241-171"
source_url: ""
domain: ["physical-ict"]
last_fetched: "2026-03-14"
status: "template"
tags: ["ai-prompt", "kiosk", "embedded", "closed-functionality", "template"]
ai_context: "Prompt pack for evaluating kiosks and closed-functionality ICT systems."
---

# Prompt Template: Accessible Kiosk and Embedded ICT Review

## Context Files to Load

```
standards/other-standards/iso-9241-171.md
standards/en-301-549/en-301-549-requirements.md
domains/physical-ict/kiosk-and-embedded-playbook.md
```

## Prompt

```
Review this kiosk or embedded ICT system for accessibility.

System type: [payment terminal / self-check-in / ticket kiosk / appliance / closed device]
Inputs: [touch / keypad / hardware buttons / voice]
Outputs: [screen / audio / tactile / printed receipt]
Environment: [public space / noisy / low-light / staffed / unstaffed]

Return:
- accessibility risks by user need
- hardware and software remediation recommendations
- closed-functionality concerns
- testing scenarios for public deployment
- citations to EN 301 549 or related guidance
```
