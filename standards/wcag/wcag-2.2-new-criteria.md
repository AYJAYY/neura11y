---
title: "WCAG 2.2 New Success Criteria"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["wcag", "wcag-2.2", "new-criteria", "2.4.11", "2.4.12", "2.4.13", "2.5.7", "2.5.8", "3.2.6", "3.3.7", "3.3.8", "3.3.9"]
ai_context: "The 9 new success criteria added in WCAG 2.2 (October 2023) beyond WCAG 2.1. Also notes SC 4.1.1 obsolescence. Load when determining what changed between WCAG 2.1 and 2.2."
---

# WCAG 2.2 New Success Criteria

WCAG 2.2 was published as a W3C Recommendation on October 5, 2023. It adds 9 new success criteria to the 78 from WCAG 2.1, and makes SC 4.1.1 (Parsing) effectively obsolete. All WCAG 2.1 success criteria are included in WCAG 2.2 unchanged except where noted.

---

## Summary Table

| SC | Title | Level | Primary Beneficiary |
|----|-------|-------|---------------------|
| 2.4.11 | Focus Appearance (Minimum) | AA | Keyboard, low vision |
| 2.4.12 | Focus Not Obscured (Minimum) | AA | Keyboard |
| 2.4.13 | Focus Appearance (Enhanced) | AAA | Keyboard, low vision |
| 2.5.7 | Dragging Movements | AA | Motor disabilities |
| 2.5.8 | Target Size (Minimum) | AA | Motor disabilities |
| 3.2.6 | Consistent Help | A | Cognitive |
| 3.3.7 | Redundant Entry | A | Cognitive, motor |
| 3.3.8 | Accessible Authentication (Minimum) | AA | Cognitive |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | Cognitive |

---

## SC 2.4.11 — Focus Appearance (Minimum)

**Level:** AA
**Source:** https://www.w3.org/TR/WCAG22/#focus-appearance

### Normative Requirement

The keyboard focus indicator must meet ALL of these conditions:
1. **Area:** The focus indicator area is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component.
2. **Contrast:** The focus indicator has a contrast ratio of at least 3:1 between the pixels of the focus indicator in focused and unfocused states. If the color of the focus indicator is the same in both states, contrast is measured against adjacent colors.

### Exceptions
- The focus indicator is determined by the user agent (browser) and not modified by the author.
- The focus indicator is not modified by the author.

### Exact Formula
- Minimum area = perimeter of the unfocused component (in CSS pixels) × 2 CSS pixels
- For a 100px × 30px button: perimeter = 260px; minimum focus area = 520 CSS square pixels

### Common Implementations That Pass
- A 2px solid outline around a button with sufficient contrast against the button background
- A 3px solid outline (exceeds minimum)
- A box-shadow that covers sufficient area

### Common Failures
- Removing the browser default focus outline with `outline: none` or `outline: 0` without a replacement that meets the requirements
- Using a focus indicator whose contrast ratio against adjacent colors is less than 3:1
- A focus indicator that covers fewer pixels than the perimeter × 2 formula

---

## SC 2.4.12 — Focus Not Obscured (Minimum)

**Level:** AA
**Source:** https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum

### Normative Requirement

When a user interface component receives keyboard focus, it is not entirely hidden due to author-created content.

### Key Points
- "Not entirely hidden" means at least part of the focused component must be visible
- A component that is partially obscured still passes this criterion (see 2.4.13 for full visibility)
- Sticky headers, cookie banners, and chat widgets are common causes of obscuring focused elements
- The obstruction must be created by the author — content scrolled off-screen by the user does not fail

### Common Failures
- Sticky/fixed-position headers that cover the focused element
- Modal overlays that do not properly manage focus
- Cookie consent banners that appear over interactive content
- `overflow: hidden` clipping focused elements

---

## SC 2.4.13 — Focus Appearance (Enhanced)

**Level:** AAA
**Source:** https://www.w3.org/TR/WCAG22/#focus-appearance-enhanced

### Normative Requirement

When the keyboard focus indicator is visible, both of the following are true:
1. **Enclosed:** The focus indicator completely encloses the component or sub-component that is focused.
2. **Contrast:** The focus indicator has a contrast ratio of at least 3:1 between pixels in focused and unfocused states, AND a contrast ratio of at least 4.5:1 against every adjacent color in the unfocused state.
3. **Not hidden:** The focused component is not entirely hidden by author-created content.

### Comparison with 2.4.11 (AA)
- 2.4.11: Area ≥ perimeter × 2; contrast ≥ 3:1 (focused vs. unfocused)
- 2.4.13: Full enclosure; contrast ≥ 3:1 (focused vs. unfocused) AND ≥ 4.5:1 against adjacent colors

---

## SC 2.5.7 — Dragging Movements

**Level:** AA
**Source:** https://www.w3.org/TR/WCAG22/#dragging-movements

### Normative Requirement

All functionality that uses a dragging movement for operation can be achieved with a single pointer without dragging, unless dragging is essential or the functionality is determined by the user agent.

### Key Points
- Applies to drag-and-drop operations, sliders moved by dragging, sortable lists
- Must provide an alternative that uses only single-pointer actions (click/tap, not drag)
- Examples of alternatives: up/down arrow buttons for sortable items, click-to-place instead of drag
- Does NOT apply if dragging is fundamental to the purpose (e.g., a drawing application)

### Common Implementations
- Drag-and-drop file upload: add a click-to-browse fallback
- Sortable list items: add up/down move buttons
- Range slider with drag: also support click-on-track to set value

---

## SC 2.5.8 — Target Size (Minimum)

**Level:** AA
**Source:** https://www.w3.org/TR/WCAG22/#target-size-minimum

### Normative Requirement

The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except where:
1. **Spacing:** Undersized targets (those less than 24×24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target or the circle for another undersized target.
2. **Equivalent:** The same function can be achieved through a different control on the same page that meets this criterion.
3. **Inline:** The target is in a sentence or its size is otherwise constrained to the line-height of non-target text.
4. **User agent:** The target size is determined by the user agent and not modified by the author.
5. **Essential:** A particular presentation of the target is essential or is legally required.

### Key Points
- The 24×24px requirement is a minimum; the enhanced criterion (2.5.5, AAA) requires 44×44px
- The spacing exception allows smaller targets if they have sufficient spacing around them
- Inline links in body text are exempt (Inline exception)
- Icon buttons, close buttons, and small interactive controls commonly fail this

### Practical Guidance
- Default button height of 44px (using padding) comfortably exceeds both 24px (AA) and 44px (AAA)
- For icon-only buttons: `min-width: 44px; min-height: 44px` with flexbox centering
- iOS Human Interface Guidelines recommend 44pt tap targets; Android Material recommends 48dp

---

## SC 3.2.6 — Consistent Help

**Level:** A
**Source:** https://www.w3.org/TR/WCAG22/#consistent-help

### Normative Requirement

If a web page contains any of the following help mechanisms, and those mechanisms are repeated on multiple web pages, they occur in the same relative order to other page content on each page where they appear, unless a change is initiated by the user:
- Human contact details (phone, email, physical address)
- Human contact mechanism (contact form, chat)
- Self-help option (FAQ, how-to, support documentation)
- Automated contact mechanism (chatbot, virtual assistant)

### Key Points
- Does NOT require that you provide help, only that if you do, it appears consistently
- "Same relative order" means the position relative to other content does not change, not that it must be in the same pixel location
- Navigation patterns (e.g., help always in the footer) satisfy this

---

## SC 3.3.7 — Redundant Entry

**Level:** A
**Source:** https://www.w3.org/TR/WCAG22/#redundant-entry

### Normative Requirement

Information previously entered by or provided to the user that is required to be entered again in the same process is either:
- Auto-populated, or
- Available for the user to select

### Exceptions
- Re-entering information is essential (e.g., password confirmation)
- Re-entering the information is necessary to ensure the accuracy of the information
- The previously entered information is no longer valid

### Key Use Cases
- Multi-step checkout: billing address should auto-populate shipping address (or provide "same as billing" checkbox)
- Multi-page forms: information from step 1 should not need to be re-entered in step 3
- Account creation: if user enters email on one step, don't ask again

---

## SC 3.3.8 — Accessible Authentication (Minimum)

**Level:** AA
**Source:** https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum

### Normative Requirement

A cognitive function test (such as remembering a password, solving a puzzle, or transcribing distorted characters) is not required for any step in an authentication process unless at least one of the following is true:
1. **Alternative:** Another authentication method is available that does not rely on a cognitive function test.
2. **Mechanism:** A mechanism is available to assist the user in completing the cognitive function test.
3. **Object recognition:** The cognitive function test is to recognize objects.
4. **Personal content:** The cognitive function test is to identify non-text content the user provided to the website.

### Key Points
- Password managers must be allowed (do not block copy/paste in password fields)
- CAPTCHA with an audio alternative still requires cognitive function (transcription) — but object recognition CAPTCHA (click all traffic lights) is exempt under exception 3
- Passkeys and biometrics are compliant authentication methods
- "Remember me" / persistent sessions help reduce authentication barriers

### What Fails
- Requiring users to type a password without allowing paste (blocks password managers)
- Requiring users to solve a math puzzle
- Text-based CAPTCHA without alternative (audio CAPTCHA is also a cognitive test)

---

## SC 3.3.9 — Accessible Authentication (Enhanced)

**Level:** AAA
**Source:** https://www.w3.org/TR/WCAG22/#accessible-authentication-enhanced

### Normative Requirement

Same as 3.3.8 (Minimum) but without the "Object recognition" and "Personal content" exceptions.

A cognitive function test is not required for authentication unless:
1. An alternative method exists that doesn't rely on cognitive function
2. A mechanism is available to assist completion

### Difference from 3.3.8
- 3.3.8 (AA): Object recognition CAPTCHA and personal content recognition are allowed
- 3.3.9 (AAA): These exceptions are removed — no cognitive function test at all

---

## SC 4.1.1 — Parsing (Obsolete in WCAG 2.2)

**Level:** A (was normative in WCAG 2.0 and 2.1)
**Source:** https://www.w3.org/TR/WCAG22/#parsing

### Status

In WCAG 2.2, SC 4.1.1 has been made **always satisfied** (effectively obsolete). The WCAG working group determined that modern browser error correction makes parsing errors no longer a direct cause of accessibility failures in contemporary browsers.

The criterion text remains in WCAG 2.2 for backwards compatibility, but the understanding document notes that it always passes in the context of HTML content.

### Practical Impact
- HTML validation for its own sake is still good practice but is no longer a WCAG 2.2 requirement
- Tools like axe-core have deprecated their 4.1.1 rules accordingly
- If conforming to WCAG 2.2, 4.1.1 does not need to be evaluated separately
