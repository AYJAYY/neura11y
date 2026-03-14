---
title: "Understanding WCAG 2.2 — Operable"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["wcag", "wcag-2.2", "understanding", "operable", "principle-2"]
ai_context: "Principle-level understanding guide for WCAG Operable requirements. Load when explaining keyboard, focus, timing, navigation, gesture, or target-size issues."
---

# Understanding WCAG 2.2 — Operable

Operable means users can interact with the interface and navigate content without requiring abilities they may not have, such as fine pointer precision, dragging, or time-limited input.

---

## What Operable Protects Against

Users cannot operate content if:

- interaction depends on a mouse only
- focus gets trapped or lost
- timing expires before completion
- navigation requires guessing or hunting
- gestures, dragging, or tiny targets block completion

---

## Guideline Summary

| Guideline | Core Intent | High-Risk Areas |
|-----------|-------------|-----------------|
| `2.1 Keyboard Accessible` | Everything must work from keyboard | custom widgets, event handlers, focus traps |
| `2.2 Enough Time` | Time limits and motion must be controllable | auto-rotating content, session timeouts |
| `2.3 Seizures and Physical Reactions` | Avoid dangerous flashing | animations and media |
| `2.4 Navigable` | Users need orientation and wayfinding | skip links, page titles, headings, focus order, focus visibility |
| `2.5 Input Modalities` | Pointer, gesture, speech, and target use must be forgiving | label-in-name, dragging, target size |

---

## High-Value Success Criteria to Check Early

| SC | Why It Matters | Typical Failure Pattern |
|----|----------------|------------------------|
| `2.1.1` | Core keyboard access | click-only custom controls |
| `2.1.2` | Users must escape components | modal or menu traps focus |
| `2.2.2` | Moving content must be pausable | auto-rotating carousel with no pause |
| `2.4.1` | Repeated blocks need bypass | no skip link or landmarks |
| `2.4.3` | Focus order must make sense | DOM order mismatches visual order |
| `2.4.7` | Focus must be visible | `outline: none` with no replacement |
| `2.4.11` | Focus indicator must be large and visible enough | thin or low-contrast focus style |
| `2.4.12` | Focused element must not be hidden | sticky header covers the active control |
| `2.5.3` | Visible label must be reflected in the accessible name | icon button or mismatched `aria-label` |
| `2.5.7` | Dragging needs a non-drag alternative | sortable list only supports drag-and-drop |
| `2.5.8` | Targets need minimum size or spacing | tiny close buttons or icon-only controls |

---

## User Benefits

Operable requirements especially benefit:

- keyboard-only users
- switch and alternative input users
- screen reader users navigating by keyboard
- users with tremor, reduced dexterity, or limited reach
- users on touch devices or with temporary situational constraints

---

## Common Implementation Themes

### Keyboard Model First

If a component has no clear keyboard model, it is usually not ready. Native controls are preferred because they provide focus, activation, and semantics together.

### Focus Is Navigation State

Focus is not just a styling concern. It is how many users know where they are and what will happen next.

### Gesture Alternatives

Path-based gestures, drag motions, and small targets disproportionately block users with motor disabilities and mobile users. Provide single-point or button-based alternatives.

---

## Frequent Audit Questions

- Can every interactive control be reached and activated with keyboard only?
- If focus enters a component, is there an obvious way out?
- Does the focus order match the reading and task order?
- Is the focus indicator visibly stronger than the unfocused state?
- Can the same task be completed without dragging or precision tapping?

---

## Recommended Pairings

- `standards/wcag/wcag-2.2-quick-ref.md`
- `domains/web/keyboard-navigation-patterns.md`
- `domains/web/focus-management.md`
- `domains/web/mobile-accessibility-patterns.md`
- `domains/web/pwa-accessibility.md`
