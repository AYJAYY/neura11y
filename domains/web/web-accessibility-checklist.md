---
title: "Web Accessibility Checklist — WCAG 2.2 Level AA"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["wcag", "checklist", "audit", "aa", "web", "wcag-2.2"]
ai_context: "Complete WCAG 2.2 Level AA checklist for web content. Use for auditing web pages or confirming accessible content generation. Organized by POUR principles."
---

# Web Accessibility Checklist — WCAG 2.2 Level AA

All Level A (30) and Level AA (20 additional) success criteria. Check all items for WCAG 2.2 AA conformance.

---

## Principle 1: Perceivable

### 1.1 Text Alternatives

- [ ] **SC 1.1.1** — Every informative image has descriptive alt text that conveys the same information
- [ ] **SC 1.1.1** — Every functional image (icon button, linked image) has alt text describing its function
- [ ] **SC 1.1.1** — Every decorative image has `alt=""` (empty alt)
- [ ] **SC 1.1.1** — Every image of text has alt text containing the text
- [ ] **SC 1.1.1** — Every complex image (chart, graph, diagram) has a short alt plus a detailed description

### 1.2 Time-based Media

- [ ] **SC 1.2.1** — Audio-only content has a full text transcript
- [ ] **SC 1.2.1** — Video-only (no audio) content has either a text transcript or audio description track
- [ ] **SC 1.2.2** — All prerecorded video with audio has synchronized captions (human-edited, not auto-only)
- [ ] **SC 1.2.3** — All prerecorded video has audio description or a full text transcript
- [ ] **SC 1.2.4** — All live video/audio broadcasts have live captions
- [ ] **SC 1.2.5** — All prerecorded video has an audio description track

### 1.3 Adaptable

- [ ] **SC 1.3.1** — Headings are marked with `<h1>`–`<h6>`, not just bold/large text
- [ ] **SC 1.3.1** — Lists are marked with `<ul>`, `<ol>`, or `<dl>`
- [ ] **SC 1.3.1** — Data tables have `<th>` elements with `scope` attributes
- [ ] **SC 1.3.1** — Required fields are programmatically indicated (not only by color or asterisk)
- [ ] **SC 1.3.1** — Related form controls are grouped with `<fieldset>`/`<legend>`
- [ ] **SC 1.3.2** — DOM reading order matches logical visual/content order
- [ ] **SC 1.3.3** — Instructions do not rely solely on color, shape, size, or location
- [ ] **SC 1.3.4** — Content is not locked to portrait or landscape orientation
- [ ] **SC 1.3.5** — Personal information inputs have correct `autocomplete` attribute values

### 1.4 Distinguishable

- [ ] **SC 1.4.1** — Color is not the only means of conveying information (errors, links, charts)
- [ ] **SC 1.4.2** — Any audio that auto-plays for 3+ seconds can be paused/stopped/muted
- [ ] **SC 1.4.3** — Normal text has ≥ 4.5:1 contrast ratio against its background
- [ ] **SC 1.4.3** — Large text (≥18pt regular or ≥14pt bold) has ≥ 3:1 contrast ratio
- [ ] **SC 1.4.4** — Text resizes to 200% without loss of content or functionality
- [ ] **SC 1.4.4** — `<meta name="viewport">` does not include `user-scalable=no`
- [ ] **SC 1.4.5** — Text is used instead of images of text (except logos and essential cases)
- [ ] **SC 1.4.10** — Content reflows at 320px width equivalent without horizontal scrolling
- [ ] **SC 1.4.11** — Form control borders, icons conveying information, and focus indicators have ≥ 3:1 contrast
- [ ] **SC 1.4.12** — Content remains usable when line height is 1.5×, letter spacing 0.12×, word spacing 0.16×, paragraph spacing 2×
- [ ] **SC 1.4.13** — Custom tooltips and hover/focus content can be dismissed (Escape), hovered over, and remain persistent

---

## Principle 2: Operable

### 2.1 Keyboard Accessible

- [ ] **SC 2.1.1** — All functionality can be operated using only a keyboard
- [ ] **SC 2.1.2** — Keyboard focus is never trapped (can always Tab away from any component)
- [ ] **SC 2.1.4** — Any single-character keyboard shortcuts can be turned off or remapped

### 2.2 Enough Time

- [ ] **SC 2.2.1** — Time limits can be turned off, adjusted, or extended
- [ ] **SC 2.2.2** — Moving/blinking/scrolling/auto-updating content can be paused, stopped, or hidden

### 2.3 Seizures and Physical Reactions

- [ ] **SC 2.3.1** — No content flashes more than 3 times per second (or is below the flash threshold)

### 2.4 Navigable

- [ ] **SC 2.4.1** — A skip navigation link (or landmarks) allows bypassing repeated navigation
- [ ] **SC 2.4.2** — Every page has a descriptive, unique `<title>` element
- [ ] **SC 2.4.3** — Tab order is logical and follows content sequence
- [ ] **SC 2.4.4** — Every link's purpose is clear from the link text or its context
- [ ] **SC 2.4.5** — Multiple ways to find pages exist (search, sitemap, navigation, etc.)
- [ ] **SC 2.4.6** — Headings and labels are descriptive of their content/purpose
- [ ] **SC 2.4.7** — Keyboard focus is always visible
- [ ] **SC 2.4.11** — Focus indicator area ≥ perimeter of component × 2 CSS pixels
- [ ] **SC 2.4.11** — Focus indicator has ≥ 3:1 contrast against adjacent colors
- [ ] **SC 2.4.12** — Focused components are not entirely hidden behind sticky headers or other overlays

### 2.5 Input Modalities

- [ ] **SC 2.5.1** — Multi-point gestures (pinch, swipe) have single-pointer alternatives
- [ ] **SC 2.5.2** — Actions activate on up-event (mouseup/pointerup), not down-event
- [ ] **SC 2.5.3** — The accessible name of every interactive element includes its visible label text
- [ ] **SC 2.5.4** — Device-motion functionality (shake, tilt) has a UI control alternative
- [ ] **SC 2.5.7** — All drag-and-drop functionality has a single-pointer (non-drag) alternative
- [ ] **SC 2.5.8** — Interactive targets are ≥ 24×24 CSS pixels (or have sufficient spacing)

---

## Principle 3: Understandable

### 3.1 Readable

- [ ] **SC 3.1.1** — `<html>` element has a `lang` attribute with the correct language code
- [ ] **SC 3.1.2** — Passages in a different language have a `lang` attribute

### 3.2 Predictable

- [ ] **SC 3.2.1** — Receiving focus does not cause a change of context (page navigation, dialog opening, etc.)
- [ ] **SC 3.2.2** — Changing an input value does not cause a change of context without warning
- [ ] **SC 3.2.3** — Navigation is in the same relative order across pages
- [ ] **SC 3.2.4** — Components with the same function are identified consistently across pages
- [ ] **SC 3.2.6** — Help mechanisms (contact, chat, FAQ) appear in the same relative position across pages

### 3.3 Input Assistance

- [ ] **SC 3.3.1** — Form errors are described in text (not only by color) and identify the specific field
- [ ] **SC 3.3.2** — All form inputs have labels or instructions
- [ ] **SC 3.3.3** — Error messages suggest how to correct the error (when possible)
- [ ] **SC 3.3.4** — Legal/financial/data submissions are reversible, verifiable, or confirmed
- [ ] **SC 3.3.7** — Information entered earlier in a process is auto-populated or selectable when needed again
- [ ] **SC 3.3.8** — Authentication does not require a cognitive function test (or has an alternative)

---

## Principle 4: Robust

### 4.1 Compatible

- [ ] **SC 4.1.1** — (Obsolete in WCAG 2.2 — always passes; HTML validation still recommended)
- [ ] **SC 4.1.2** — Every interactive element has an accessible name, role, and programmatically determinable state
- [ ] **SC 4.1.3** — Status messages (success, error, loading) are exposed via live regions without receiving focus

---

## Additional Checks (Non-WCAG but Essential)

- [ ] All `<iframe>` elements have a descriptive `title` attribute
- [ ] No content is accessible only via CSS hover (no keyboard equivalent)
- [ ] All JavaScript event handlers have keyboard equivalents
- [ ] Error messages appear near the field they describe, not only in a banner
- [ ] `<html lang>` matches actual language of content
- [ ] Links to documents (PDF, Word) identify the file type and size
- [ ] External links warn users if opening in a new tab/window
- [ ] Forms do not auto-submit when last field is filled
- [ ] Page has a `<main>` landmark containing primary content
- [ ] Pages with forms have `<form>` with an accessible name

---

## How to Test

### Automated Testing (run first)

Tools: axe DevTools, WAVE, Lighthouse, ARC Toolkit, IBM Equal Access Checker. These catch ~30–40% of issues.

### Keyboard Testing (run second)

1. Disconnect mouse
2. Tab through entire page — verify focus is always visible and order is logical
3. Activate all interactive elements with Enter/Space
4. Navigate within widgets with arrow keys
5. Verify all dialogs/menus can be closed with Escape
6. Check skip navigation link appears on first Tab

### Screen Reader Testing (run third)

Minimum: NVDA + Chrome, VoiceOver + Safari. See `domains/web/testing/screen-reader-testing-matrix.md`.

### Manual Visual Testing

1. Zoom to 200% — verify no content loss
2. Zoom to 400% on mobile viewport (320px equivalent) — verify reflow
3. Apply text spacing bookmarklet — verify no content clipping
4. Disable CSS — verify reading order matches visual order
5. Disable color (grayscale) — verify no information conveyed by color alone
