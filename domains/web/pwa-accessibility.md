---
title: "PWA Accessibility Patterns"
standard: "WCAG"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["pwa", "progressive-web-app", "offline", "install", "spa", "notifications"]
ai_context: "Accessibility patterns for progressive web apps. Load when advising on install prompts, offline states, update flows, notifications, or app-shell navigation."
---

# PWA Accessibility Patterns

Progressive web apps inherit normal web accessibility requirements and add extra risk around app-shell routing, install flows, offline behavior, update prompts, and notifications.

---

## PWA-Specific Risk Areas

| Area | Common Risk |
|------|-------------|
| Install prompt | modal or banner steals focus or is not dismissible |
| Offline mode | empty state gives no status or recovery path |
| Cached shell | route changes are not announced like page changes |
| Update prompt | user is interrupted without context or loses work |
| Push notifications | inaccessible copy or no settings path |
| App-like navigation | landmarks, headings, and focus behavior are missing |

---

## Core Patterns

### Treat Route Changes Like Page Changes

- Update the document title on route change.
- Move focus to the new main heading or landmark.
- Announce major content updates when the visual change is not obvious to assistive tech.

### Make Install UI Dismissible and Predictable

- Use a real dialog or banner pattern with keyboard and screen reader support.
- Do not trap users in install prompts.
- Provide clear actions: install now, remind later, dismiss.

### Design Offline States as First-Class Content

- Explain that the app is offline.
- Show what still works and what is unavailable.
- Provide retry and reconnect options with clear status text.

### Handle Updates Without Surprising Users

- If a new version is available, explain what will happen before reload.
- Preserve user work where possible.
- Do not refresh automatically during critical workflows.

### Notifications Need Accessible Copy and Controls

- Use plain language for notification permission requests.
- Explain why notifications are useful before triggering the browser permission UI.
- Provide an in-app settings path to change notification behavior.

---

## Practical Checklist

- [ ] App-shell route changes update title and focus
- [ ] Main content region and headings remain stable across routes
- [ ] Install prompt is accessible and dismissible
- [ ] Offline state includes status, limits, and recovery actions
- [ ] Update flow does not silently destroy user work
- [ ] Permission prompts are explained in plain language
- [ ] Push-related settings are reachable without hidden gestures or unlabeled icons

---

## Recommended Pairings

- `domains/web/spa-accessibility.md`
- `domains/web/focus-management.md`
- `domains/web/mobile-accessibility-patterns.md`
- `standards/wcag/wcag-understanding/operable.md`
