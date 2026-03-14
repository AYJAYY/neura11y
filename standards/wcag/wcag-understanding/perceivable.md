---
title: "Understanding WCAG 2.2 — Perceivable"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["wcag", "wcag-2.2", "understanding", "perceivable", "principle-1"]
ai_context: "Principle-level understanding guide for WCAG Perceivable requirements. Load when explaining why content fails or how perceivability requirements work together."
---

# Understanding WCAG 2.2 — Perceivable

Perceivable means information and user interface components can be presented in ways users can detect through sight, hearing, or alternative formats such as text, braille, speech, and magnification.

Understanding documents are **informative**, not normative. Use this file to explain intent, user benefit, and common implementation pitfalls behind Principle 1.

---

## What Perceivable Protects Against

Users cannot access content if:

- images have no usable text alternative
- time-based media has no captions, transcript, or description
- structure exists visually but not programmatically
- color, contrast, or hover-only behavior hides meaning

---

## Guideline Summary

| Guideline | Core Intent | High-Risk Areas |
|-----------|-------------|-----------------|
| `1.1 Text Alternatives` | Non-text content needs an equivalent text alternative | images, icons, charts, SVG, CAPTCHA |
| `1.2 Time-based Media` | Audio and video need text or described alternatives | captions, transcripts, audio description, live media |
| `1.3 Adaptable` | Structure and relationships must survive presentation changes | headings, lists, tables, labels, reading order |
| `1.4 Distinguishable` | Users must be able to see and hear content clearly | contrast, color-only cues, resize, reflow, non-text contrast |

---

## High-Value Success Criteria to Check Early

| SC | Why It Matters | Typical Failure Pattern |
|----|----------------|------------------------|
| `1.1.1` | Foundational for images and non-text UI | missing or meaningless alt text |
| `1.2.2` | Captions are mandatory for prerecorded synchronized media | auto-captions left uncorrected |
| `1.2.5` | Visual meaning in video must be conveyed audibly | demos or slides shown without description |
| `1.3.1` | Structure must be machine-readable | headings styled with CSS only, unlabeled controls, bad tables |
| `1.3.2` | Meaning depends on sequence | visual order differs from DOM order |
| `1.3.5` | Personal-data inputs need purpose tokens | missing `autocomplete` on forms |
| `1.4.3` | Text contrast must be sufficient | low-contrast body text or links |
| `1.4.10` | Content must reflow at small viewport widths | two-dimensional scrolling at 320px width |
| `1.4.11` | Important graphics and controls need 3:1 contrast | faint control outlines, low-contrast icons |
| `1.4.13` | Hover/focus content must remain usable | tooltip disappears on hover or blocks access |

---

## User Benefits

Perceivable requirements especially benefit:

- blind and low-vision users
- deaf and hard-of-hearing users
- users of screen readers, magnifiers, braille displays, and captions
- users in noisy, low-light, or zoomed environments
- users who need simpler presentation changes without losing meaning

---

## Common Implementation Themes

### Equivalent Alternatives

An equivalent alternative serves the same purpose as the original content. The goal is not literal description in every case; it is preserving meaning, function, or outcome.

### Programmatic Structure

If structure is only visual, assistive technology cannot reliably convey it. Headings, lists, form labels, table headers, regions, and sequences must exist in the markup or accessible tree.

### Visual Robustness

Passing contrast or reflow is not just about design polish. It determines whether users can read, track, and operate content at high zoom, on small screens, or with reduced visual acuity.

---

## Frequent Audit Questions

When a perceivable issue is borderline, ask:

- Does the text alternative preserve purpose, not just appearance?
- If audio were unavailable, would captions or transcript still convey meaning?
- If CSS were removed, would structure still make sense?
- If the page were viewed at 320px width or 400% zoom, would the task still work?
- If color cues vanished, would the meaning still be available?

---

## Recommended Pairings

- `standards/wcag/wcag-2.2-quick-ref.md`
- `standards/wcag/wcag-techniques/sufficient-techniques.md`
- `domains/web/images-and-media.md`
- `domains/web/color-and-contrast.md`
