---
title: "WCAG 2.1 Quick Reference — All Success Criteria"
standard: "WCAG 2.1"
source_url: "https://www.w3.org/WAI/WCAG21/quickref/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["wcag", "wcag-2.1", "quick-ref", "success-criteria"]
ai_context: "Complete reference for all 78 WCAG 2.1 success criteria. WCAG 2.2 supersedes this — prefer wcag-2.2-quick-ref.md for new work. Use this when explicitly targeting WCAG 2.1 compliance (e.g., EN 301 549 v3.2.1 references WCAG 2.1)."
---

# WCAG 2.1 Quick Reference

All 78 success criteria from WCAG 2.1 (W3C Recommendation, June 5, 2018). WCAG 2.2 includes all WCAG 2.1 criteria plus 9 new ones. Use `wcag-2.2-quick-ref.md` for new work unless specifically targeting WCAG 2.1.

**Why you may need WCAG 2.1 specifically:**
- EN 301 549 v3.2.1 (2021) references WCAG 2.1 Level AA
- Some Section 508 implementations reference WCAG 2.0 (not 2.1)
- Some contracts and policies specify WCAG 2.1

---

## Differences: WCAG 2.1 vs WCAG 2.0

WCAG 2.1 added 17 new success criteria to the 61 from WCAG 2.0:

### New in WCAG 2.1

| SC | Title | Level |
|----|-------|-------|
| 1.3.4 | Orientation | AA |
| 1.3.5 | Identify Input Purpose | AA |
| 1.3.6 | Identify Purpose | AAA |
| 1.4.10 | Reflow | AA |
| 1.4.11 | Non-text Contrast | AA |
| 1.4.12 | Text Spacing | AA |
| 1.4.13 | Content on Hover or Focus | AA |
| 2.1.4 | Character Key Shortcuts | A |
| 2.5.1 | Pointer Gestures | A |
| 2.5.2 | Pointer Cancellation | A |
| 2.5.3 | Label in Name | A |
| 2.5.4 | Motion Actuation | A |
| 2.5.5 | Target Size | AAA |
| 2.5.6 | Concurrent Input Mechanisms | AAA |
| 4.1.3 | Status Messages | AA |

(Plus 1.3.5 and 2.2.6 — 17 total new criteria)

---

## All 78 Success Criteria

For full details on criteria shared with WCAG 2.2, see `wcag-2.2-quick-ref.md`. This file notes the WCAG 2.1-specific context.

### Principle 1: Perceivable

**SC 1.1.1** Non-text Content — Level A — All non-text content has a text alternative
**SC 1.2.1** Audio-only and Video-only (Prerecorded) — Level A — Transcript for audio-only; transcript or audio for video-only
**SC 1.2.2** Captions (Prerecorded) — Level A — Synchronized captions for prerecorded video
**SC 1.2.3** Audio Description or Media Alternative (Prerecorded) — Level A
**SC 1.2.4** Captions (Live) — Level AA
**SC 1.2.5** Audio Description (Prerecorded) — Level AA
**SC 1.2.6** Sign Language (Prerecorded) — Level AAA
**SC 1.2.7** Extended Audio Description (Prerecorded) — Level AAA
**SC 1.2.8** Media Alternative (Prerecorded) — Level AAA
**SC 1.2.9** Audio-only (Live) — Level AAA
**SC 1.3.1** Info and Relationships — Level A — Structure programmatically determinable
**SC 1.3.2** Meaningful Sequence — Level A — Reading order determinable
**SC 1.3.3** Sensory Characteristics — Level A — No sole reliance on sensory characteristics
**SC 1.3.4** Orientation — Level AA [NEW in 2.1] — Don't lock to portrait or landscape
**SC 1.3.5** Identify Input Purpose — Level AA [NEW in 2.1] — autocomplete attribute for personal inputs
**SC 1.3.6** Identify Purpose — Level AAA [NEW in 2.1]
**SC 1.4.1** Use of Color — Level A — Color not sole means of conveying info
**SC 1.4.2** Audio Control — Level A — Auto-playing audio can be controlled
**SC 1.4.3** Contrast (Minimum) — Level AA — Normal text 4.5:1; large text 3:1
**SC 1.4.4** Resize Text — Level AA — Text resizable to 200% without loss
**SC 1.4.5** Images of Text — Level AA — Avoid images of text
**SC 1.4.6** Contrast (Enhanced) — Level AAA — Normal text 7:1; large text 4.5:1
**SC 1.4.7** Low or No Background Audio — Level AAA
**SC 1.4.8** Visual Presentation — Level AAA
**SC 1.4.9** Images of Text (No Exception) — Level AAA
**SC 1.4.10** Reflow — Level AA [NEW in 2.1] — Content reflows at 320px width without horizontal scroll
**SC 1.4.11** Non-text Contrast — Level AA [NEW in 2.1] — UI components and graphics 3:1 against adjacent
**SC 1.4.12** Text Spacing — Level AA [NEW in 2.1] — Content survives text spacing overrides
**SC 1.4.13** Content on Hover or Focus — Level AA [NEW in 2.1] — Tooltip/hover content is dismissible, hoverable, persistent

### Principle 2: Operable

**SC 2.1.1** Keyboard — Level A — All functionality keyboard accessible
**SC 2.1.2** No Keyboard Trap — Level A — Focus can escape all components
**SC 2.1.3** Keyboard (No Exception) — Level AAA
**SC 2.1.4** Character Key Shortcuts — Level A [NEW in 2.1] — Remappable or disableable single-key shortcuts
**SC 2.2.1** Timing Adjustable — Level A
**SC 2.2.2** Pause, Stop, Hide — Level A
**SC 2.2.3** No Timing — Level AAA
**SC 2.2.4** Interruptions — Level AAA
**SC 2.2.5** Re-authenticating — Level AAA
**SC 2.2.6** Timeouts — Level AAA [NEW in 2.1]
**SC 2.3.1** Three Flashes or Below Threshold — Level A
**SC 2.3.2** Three Flashes — Level AAA
**SC 2.3.3** Animation from Interactions — Level AAA [NEW in 2.1]
**SC 2.4.1** Bypass Blocks — Level A — Skip navigation
**SC 2.4.2** Page Titled — Level A
**SC 2.4.3** Focus Order — Level A
**SC 2.4.4** Link Purpose (In Context) — Level A
**SC 2.4.5** Multiple Ways — Level AA
**SC 2.4.6** Headings and Labels — Level AA
**SC 2.4.7** Focus Visible — Level AA
**SC 2.4.8** Location — Level AAA
**SC 2.4.9** Link Purpose (Link Only) — Level AAA
**SC 2.4.10** Section Headings — Level AAA
**SC 2.5.1** Pointer Gestures — Level A [NEW in 2.1] — Single-pointer alternative for multi-point gestures
**SC 2.5.2** Pointer Cancellation — Level A [NEW in 2.1] — Up-event activation
**SC 2.5.3** Label in Name — Level A [NEW in 2.1] — Accessible name contains visible label text
**SC 2.5.4** Motion Actuation — Level A [NEW in 2.1] — Device motion has UI alternative
**SC 2.5.5** Target Size — Level AAA [NEW in 2.1] — 44×44 CSS pixels minimum
**SC 2.5.6** Concurrent Input Mechanisms — Level AAA [NEW in 2.1]

### Principle 3: Understandable

**SC 3.1.1** Language of Page — Level A — `<html lang="xx">`
**SC 3.1.2** Language of Parts — Level AA — `lang` on sections in different language
**SC 3.1.3** Unusual Words — Level AAA
**SC 3.1.4** Abbreviations — Level AAA
**SC 3.1.5** Reading Level — Level AAA
**SC 3.1.6** Pronunciation — Level AAA
**SC 3.2.1** On Focus — Level A
**SC 3.2.2** On Input — Level A
**SC 3.2.3** Consistent Navigation — Level AA
**SC 3.2.4** Consistent Identification — Level AA
**SC 3.2.5** Change on Request — Level AAA
**SC 3.3.1** Error Identification — Level A
**SC 3.3.2** Labels or Instructions — Level A
**SC 3.3.3** Error Suggestion — Level AA
**SC 3.3.4** Error Prevention (Legal, Financial, Data) — Level AA
**SC 3.3.5** Help — Level AAA
**SC 3.3.6** Error Prevention (All) — Level AAA

### Principle 4: Robust

**SC 4.1.1** Parsing — Level A — Valid HTML (still active in WCAG 2.1, unlike 2.2)
**SC 4.1.2** Name, Role, Value — Level A — Accessible name, role, states for all UI components
**SC 4.1.3** Status Messages — Level AA [NEW in 2.1] — role="status"/role="alert" for status messages

---

## WCAG 2.1 AA Checklist (Additions to WCAG 2.0 AA)

If your baseline is WCAG 2.0 AA and you need to uplift to WCAG 2.1 AA, focus on these new AA criteria:

- [ ] **1.3.4** Does content work in both portrait and landscape orientations?
- [ ] **1.3.5** Do personal information inputs have correct `autocomplete` attribute values?
- [ ] **1.4.10** Does content reflow at 320px width without horizontal scrolling?
- [ ] **1.4.11** Do UI component borders and graphics have 3:1 contrast against adjacent colors?
- [ ] **1.4.12** Does content survive line height 1.5×, letter spacing 0.12×, word spacing 0.16×, paragraph spacing 2×?
- [ ] **1.4.13** Are hover/focus-triggered tooltips dismissible (Escape), hoverable (pointer can move onto them), and persistent?
- [ ] **2.1.4** Can single-character keyboard shortcuts be turned off or remapped?
- [ ] **2.5.1** Is there a single-pointer alternative for all multi-pointer gestures?
- [ ] **2.5.2** Does activation happen on up-event, not down-event?
- [ ] **2.5.3** Does the accessible name of each component contain its visible label text?
- [ ] **2.5.4** Is there a UI alternative for all device-motion-operated functionality?
- [ ] **4.1.3** Are status messages exposed via live regions (role="status", role="alert") without requiring focus?
