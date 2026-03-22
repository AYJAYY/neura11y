---
title: "Prompt Template: TalkBack Mobile Web Review"
standard: "TalkBack + WCAG"
source_url: ""
domain: ["mobile", "web"]
last_fetched: "2026-03-21"
status: "template"
tags: ["ai-prompt", "screen-reader", "talkback", "android", "mobile", "template"]
ai_context: "Prompt pack for reviewing Android web or app-like experiences with TalkBack."
---

# Prompt Template: TalkBack Mobile Web Review

## Context Files to Load

```
screen-readers/talkback-guide.md
screen-readers/screen-reader-overview.md
domains/web/testing/screen-reader-testing-matrix.md
domains/mobile/native-mobile-app-accessibility.md
```

## Prompt

```
Review this Android experience for TalkBack accessibility.

Surface: [mobile web / webview / native app]
Primary flow: [list]
Input model: [touch / keyboard / switch / voice]

Return:
- the TalkBack gestures and reading controls needed to test the flow
- expected announcements for controls, headings, landmarks, and errors
- touch target and focus-order risks
- Android-specific remediation guidance
```
