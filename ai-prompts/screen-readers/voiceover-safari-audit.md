---
title: "Prompt Template: VoiceOver + Safari Audit"
standard: "VoiceOver + WCAG"
source_url: ""
domain: ["web", "mobile"]
last_fetched: "2026-03-21"
status: "template"
tags: ["ai-prompt", "screen-reader", "voiceover", "safari", "template"]
ai_context: "Prompt pack for reviewing web experiences with VoiceOver on macOS or iOS Safari."
---

# Prompt Template: VoiceOver + Safari Audit

## Context Files to Load

```
screen-readers/voiceover-guide.md
screen-readers/screen-reader-overview.md
domains/web/testing/screen-reader-testing-matrix.md
domains/web/focus-management.md
```

## Prompt

```
Review this experience for VoiceOver users on Safari.

Platform: [macOS / iOS]
Surface: [web page / app-like flow / form / menu / modal]
Primary tasks: [list]

Return:
- the exact VoiceOver commands or gestures to use
- what the rotor should expose
- expected announcements for controls, headings, landmarks, and dialogs
- Safari-specific risks
- remediation guidance for any missing or misleading announcements
```
