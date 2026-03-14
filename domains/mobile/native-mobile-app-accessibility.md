---
title: "Native Mobile App Accessibility Guide"
standard: "WCAG 2.2 + Platform Accessibility APIs"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["mobile"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["mobile", "ios", "android", "native-apps", "voiceover", "talkback"]
ai_context: "Applied guidance for native iOS and Android accessibility, including semantics, focus, gestures, and dynamic text."
---

# Native Mobile App Accessibility Guide

## Semantics and Labels

- Use native accessibility roles, labels, traits, and hints
- Ensure visible labels match spoken labels where possible
- Do not expose decorative icons as actionable elements
- Group related content only when it improves navigation

## Focus and Navigation

- Reading order should match the visual layout
- Modal screens must move focus to the new context
- Focus should return predictably after dialogs and temporary surfaces close
- Avoid hidden focusable elements behind drawers, sheets, or overlays

## Touch and Gesture Input

- Targets should be at least 24 by 24 CSS pixels equivalent, with larger platform-specific tap areas preferred
- Provide alternatives for drag, swipe, long-press, and multi-finger gestures
- Avoid gesture-only onboarding that cannot be revisited

## Text, Scaling, and Layout

- Support Dynamic Type or font scaling without clipping
- Re-test custom controls at large text sizes
- Preserve contrast in light mode, dark mode, and high-contrast modes

## Announcements and Status Changes

- Announce loading, success, and error states through platform accessibility APIs
- Keep announcement text short and action-oriented
- Avoid spamming users with repeated live updates for every minor change

## Platform Testing

Minimum checks:
- VoiceOver on iOS
- TalkBack on Android
- keyboard or switch access where supported
- landscape and portrait
- large text and display zoom
