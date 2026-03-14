---
title: "Screen Reader Testing Matrix"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/test-evaluate/preliminary/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["testing", "screen-reader", "nvda", "jaws", "voiceover", "talkback", "matrix"]
ai_context: "Screen reader and browser combinations for accessibility testing. Covers minimum test matrix, key SR commands, and what to check. Load when writing testing instructions."
---

# Screen Reader Testing Matrix

---

## Minimum Testing Combinations

Testing with a single screen reader is insufficient. Each AT+browser combination has different behavior.

### Recommended Minimum Matrix

| Screen Reader | Browser | Platform | Priority |
|---|---|---|---|
| NVDA (latest) | Chrome (latest) | Windows | **High** |
| NVDA (latest) | Firefox (latest) | Windows | Medium |
| JAWS (latest) | Chrome (latest) | Windows | **High** |
| JAWS (latest) | Edge (latest) | Windows | Medium |
| VoiceOver | Safari (latest) | macOS | **High** |
| VoiceOver | Safari (latest) | iOS | **High** |
| TalkBack (latest) | Chrome | Android | **High** |
| Narrator (latest) | Edge (latest) | Windows | Low |

**Rationale:** JAWS+Chrome and NVDA+Chrome cover the majority of Windows screen reader users. VoiceOver+Safari is the only fully supported combination on Apple platforms.

### Market Share Context (2024 WebAIM Survey approximations)

| Screen Reader | Desktop share |
|---|---|
| JAWS | ~40% |
| NVDA | ~35% |
| VoiceOver (macOS) | ~10% |
| Narrator | ~5% |
| Other | ~10% |

---

## What to Test on Each Combination

### Minimum Checks per Test Run

1. **Page title announced** — Does the SR announce the page title when the page loads?
2. **Reading order** — Can you read through the entire page in logical order using arrow keys?
3. **Headings** — Can you navigate by headings (H key in NVDA/JAWS)?
4. **Links** — Can you list all links and are they descriptive?
5. **Forms** — Are all inputs labeled? Are errors announced?
6. **Images** — Are meaningful images described? Are decorative images skipped?
7. **Interactive components** — Do buttons, menus, dialogs, tabs work correctly?
8. **Focus management** — Does focus move correctly after interactions (modal open/close, route change)?
9. **Live regions** — Are status messages announced?

---

## NVDA Key Commands

**Modes:** Browse mode (reading) vs. Forms mode (interacting). NVDA auto-switches.

| Action | Key |
|--------|-----|
| Toggle browse/forms mode | `Insert + Space` |
| Read next item | `Down Arrow` (browse mode) |
| Read all from cursor | `Insert + Down Arrow` |
| Stop reading | `Ctrl` |
| Next heading | `H` |
| Previous heading | `Shift + H` |
| Heading level N | `1`–`6` |
| Next link | `K` |
| Next form field | `F` |
| Next button | `B` |
| Next landmark/region | `D` |
| Next table | `T` |
| Next list | `L` |
| Open elements list | `Insert + F7` |
| NVDA menu | `Insert + N` |

**NVDA modifier key:** `Insert` (or `Caps Lock` if configured)

---

## JAWS Key Commands

| Action | Key |
|--------|-----|
| Toggle virtual cursor | `Insert + Z` |
| Read all | `Insert + Down Arrow` |
| Next heading | `H` |
| Headings list | `Insert + F6` |
| Links list | `Insert + F7` |
| Next form field | `F` |
| Next landmark | `R` |
| Next table | `T` |
| Next graphic | `G` |
| JAWS help | `Insert + F1` |
| Say line | `Insert + Up Arrow` |
| Say next word | `Insert + Right Arrow` |

**JAWS modifier key:** `Insert`

---

## VoiceOver (macOS) Key Commands

**VO key = `Ctrl + Option`**

| Action | Key |
|--------|-----|
| Start/stop VoiceOver | `Cmd + F5` |
| Read all | `VO + A` |
| Next item | `VO + Right Arrow` |
| Interact with item | `VO + Shift + Down Arrow` |
| Stop interacting | `VO + Shift + Up Arrow` |
| Rotor | `VO + U` (then arrows to navigate by type) |
| Next heading | In Rotor: select Headings, then `Down Arrow` |
| Web item rotor | `VO + Command + H` (headings) |
| Open Web Rotor | `VO + U` |

**VoiceOver Rotor categories:** Headings, Links, Form Controls, Tables, Landmarks, Images, Frames

---

## VoiceOver (iOS) Gestures

| Action | Gesture |
|--------|---------|
| Enable VoiceOver | Settings → Accessibility → VoiceOver |
| Navigate to next item | Swipe right with one finger |
| Navigate to previous item | Swipe left with one finger |
| Activate item | Double tap |
| Scroll | Three-finger swipe |
| Open rotor | Rotate two fingers (like turning a dial) |
| Rotor options | Swipe up/down to cycle through rotor setting |

---

## TalkBack (Android) Key Commands

| Action | Gesture |
|--------|---------|
| Enable TalkBack | Settings → Accessibility → TalkBack |
| Next item | Swipe right |
| Previous item | Swipe left |
| Activate item | Double tap |
| Next heading | Local context menu → Headings |
| Open TalkBack menu | Swipe down then right |

---

## Testing Checklist by Component

### Navigation

- [ ] Skip link visible on focus and works
- [ ] Main nav is a `<nav>` with an accessible name
- [ ] Active page indicated (aria-current="page" announced)
- [ ] All links have descriptive text (no "click here")

### Forms

- [ ] Every input has a visible and programmatic label
- [ ] Required fields indicated programmatically (`aria-required` or `required`)
- [ ] Error messages linked to fields via `aria-describedby`
- [ ] `aria-invalid="true"` set on invalid fields
- [ ] Form groups use `<fieldset>` + `<legend>`
- [ ] Submit button is descriptive

### Images

- [ ] Decorative images have `alt=""`
- [ ] Meaningful images have descriptive alt text
- [ ] Complex images have long descriptions

### Interactive Components

- [ ] Buttons announce their state (expanded/collapsed, pressed/not pressed)
- [ ] Modals trap focus when open
- [ ] Modals return focus on close
- [ ] Tab panels: active tab announced as selected
- [ ] Menus: items announced as menu items

### Dynamic Content

- [ ] Status messages in live regions are announced
- [ ] Loading states announced
- [ ] Route changes announced (in SPAs)
- [ ] Error alerts announced immediately

---

## Common Screen Reader Bugs to Test For

| Bug | Test |
|-----|------|
| Hidden content read aloud | Content inside `display:none` — should NOT be read |
| Focusable elements inside `aria-hidden` | Tab into `aria-hidden` container — focus should not enter |
| Focus order doesn't match visual order | Tab through page; compare to visual reading order |
| Button reads as "button button" | Use `<button>` + `aria-label` that doesn't include "button" |
| Form field reads label twice | Check for duplicate `<label>` + `aria-label` both present |
| "Unlabeled" announced for input | Verify `<label for>` matches `id`; or `aria-label` present |
| Landmark not announced | Verify `<main>`, `<nav>`, `<header>` in DOM |
| Table headers not associated | Verify `<th scope="col/row">` or `headers` attribute |

---

## Automated vs. Manual Testing Coverage

Automated tools (Axe, Lighthouse, WAVE) find approximately **30-40%** of WCAG failures.

| Category | Automatable? |
|----------|-------------|
| Missing alt text | Yes |
| Color contrast | Yes |
| Missing form labels | Partially |
| Keyboard focus visible | Partially |
| Focus order logical | No |
| ARIA semantics valid | Partially |
| Screen reader announcements correct | No |
| Meaningful alt text quality | No |
| Cognitive load | No |

**Rule:** Automated testing is a filter, not a certification. Always follow with manual keyboard and screen reader testing.
