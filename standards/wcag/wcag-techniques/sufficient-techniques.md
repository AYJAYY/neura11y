---
title: "WCAG 2.2 Sufficient Techniques"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Techniques/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["wcag", "wcag-2.2", "techniques", "sufficient-techniques", "html", "aria", "pdf"]
ai_context: "High-value WCAG 2.2 sufficient techniques with IDs and short descriptions. Load when an audit or code review needs technique citations."
---

# WCAG 2.2 Sufficient Techniques

Techniques are **informative**, not normative. Conformance is determined by the WCAG success criteria, not by use of a specific technique. This file is a curated, high-value technique index for common audit and implementation tasks.

---

## How to Use This File

- Use technique IDs when the user wants implementation-oriented evidence or remediation examples.
- Do not claim that a single technique is the only valid way to satisfy a success criterion.
- Pair technique citations with the relevant success criterion.

---

## Common HTML Techniques

| Technique | Description | Common SCs |
|-----------|-------------|------------|
| `H25` | Use the `title` element to provide a page title | `2.4.2` |
| `H30` | Provide descriptive link text for anchor elements | `2.4.4` |
| `H32` | Provide submit buttons for form submission | `3.2.2`, `3.3.x` |
| `H36` | Use `alt` on image submit buttons | `1.1.1`, `4.1.2` |
| `H37` | Use `alt` on `img` elements | `1.1.1` |
| `H39` | Use `caption` for data table captions | `1.3.1` |
| `H42` | Use `h1`-`h6` for headings | `1.3.1`, `2.4.6` |
| `H43` | Use `id` and `headers` to associate table cells | `1.3.1` |
| `H44` | Use `label` elements for form fields | `1.3.1`, `3.3.2`, `4.1.2` |
| `H48` | Use semantic list elements | `1.3.1` |
| `H71` | Use `fieldset` and `legend` to group controls | `1.3.1`, `3.3.2` |
| `H95` | Use `track` for captions | `1.2.2` |
| `H96` | Use `track` for audio descriptions | `1.2.5` |
| `H98` | Use `autocomplete` tokens correctly | `1.3.5` |
| `H101` | Use semantic HTML regions and landmarks | `1.3.1`, `2.4.1` |

---

## Common ARIA Techniques

| Technique | Description | Common SCs |
|-----------|-------------|------------|
| `ARIA1` | Use `aria-describedby` for descriptive labeling | `3.3.2`, `4.1.2` |
| `ARIA6` | Use `aria-label` for accessible names | `1.1.1`, `4.1.2` |
| `ARIA10` | Use `aria-labelledby` for text alternatives | `1.1.1`, `4.1.2` |
| `ARIA11` | Use landmarks to identify page regions | `1.3.1`, `2.4.1` |
| `ARIA12` | Use `role="heading"` with `aria-level` where needed | `1.3.1`, `2.4.6` |
| `ARIA16` | Use `aria-labelledby` to name UI controls | `1.3.1`, `4.1.2` |
| `ARIA17` | Use grouping roles for related form controls | `1.3.1` |
| `ARIA19` | Use alert/live-region patterns for error messaging | `3.3.1`, `4.1.3` |
| `ARIA22` | Use `role="status"` for status messages | `4.1.3` |
| `ARIA24` | Use `role="img"` for icon fonts or similar non-text content | `1.1.1` |

---

## Common General and CSS Techniques

| Technique | Description | Common SCs |
|-----------|-------------|------------|
| `G1` | Add a skip link to main content | `2.4.1` |
| `G14` | Ensure color-coded information is also in text | `1.4.1` |
| `G18` | Ensure 4.5:1 contrast for normal text | `1.4.3` |
| `G57` | Order content in a meaningful sequence | `1.3.2` |
| `G87` | Provide closed captions | `1.2.2` |
| `G93` | Provide open captions | `1.2.2` |
| `G95` | Provide short text alternatives for non-text content | `1.1.1` |
| `G115` | Use semantic elements to mark up structure | `1.3.1` |
| `G141` | Organize a page using headings | `1.3.1`, `2.4.6` |
| `G145` | Ensure 3:1 contrast for large text | `1.4.3` |
| `G149` | Use user-agent focus indicators or clearly visible custom focus styles | `2.4.7`, `2.4.13` |
| `G157` | Use live captioning for live media | `1.2.4` |
| `G208` | Include visible label text in the accessible name | `2.5.3` |
| `G211` | Match the accessible name to the visible label | `2.5.3` |
| `G215` | Provide alternatives to path-based or multipoint gestures | `2.5.1` |
| `G216` | Provide single-point alternatives to dragging | `2.5.7` |
| `C15` | Change component presentation on focus with CSS | `2.4.7`, `2.4.13` |
| `C17` | Scale form controls containing text | `1.4.4` |
| `C18` | Use CSS margin/padding instead of spacer images | `1.1.1` |
| `C22` | Use CSS for visual presentation of text | `1.3.1`, `1.4.x` |
| `C27` | Make DOM order match visual order | `1.3.2`, `2.4.3` |

---

## Common Script and PDF Techniques

| Technique | Description | Common SCs |
|-----------|-------------|------------|
| `SCR26` | Insert dynamic content immediately after its trigger in the DOM | `1.3.2`, `4.1.3` |
| `SCR32` | Add client-side validation and error text via the DOM | `3.3.1`, `3.3.3`, `4.1.3` |
| `SCR39` | Make hover/focus content hoverable, dismissible, and persistent | `1.4.13` |
| `SCR40` | Respect `prefers-reduced-motion` in JavaScript | advisory support for motion-sensitive users |
| `PDF1` | Apply alt text to images in PDFs | `1.1.1` |
| `PDF3` | Ensure correct tab and reading order in PDFs | `1.3.2`, `2.4.3` |
| `PDF6` | Use table elements for PDF tables | `1.3.1` |
| `PDF9` | Provide headings via PDF heading tags | `1.3.1`, `2.4.6` |
| `PDF10` | Provide labels for interactive form controls in PDFs | `3.3.2`, `4.1.2` |
| `PDF11` | Provide links and meaningful link text in PDFs | `2.4.4` |
| `PDF12` | Provide name/role/value for PDF form fields | `4.1.2` |
| `PDF17` | Provide consistent page numbering in PDFs | navigation support |
| `PDF21` | Use list tags for lists in PDFs | `1.3.1` |

---

## High-Use Technique Sets by Success Criterion

| SC | Common Techniques to Start With |
|----|---------------------------------|
| `1.1.1` | `H37`, `H36`, `G95`, `ARIA6`, `ARIA10`, `PDF1` |
| `1.2.2` | `G87`, `G93`, `H95` |
| `1.2.5` | `G78`, `G173`, `H96` |
| `1.3.1` | `H42`, `H43`, `H44`, `H48`, `H71`, `ARIA11`, `ARIA17`, `PDF6`, `PDF9` |
| `1.3.5` | `H98` |
| `1.4.3` | `G18`, `G145`, `C22` |
| `2.4.1` | `G1`, `ARIA11`, `H101` |
| `2.4.4` | `H30`, `PDF11` |
| `2.4.7` / `2.4.13` | `C15`, `G149` |
| `2.5.3` | `G208`, `G211` |
| `4.1.2` | `H44`, `ARIA6`, `ARIA16`, `PDF12` |
| `4.1.3` | `ARIA19`, `ARIA22`, `SCR26`, `SCR32` |

---

## Notes

- Many techniques are technology-specific; choose the technology family that matches the implementation being audited.
- A technique can be useful evidence in an audit even when the final conformance claim is tied to the success criterion.
- Pair this file with `standards/wcag/wcag-2.2-quick-ref.md` for the actual success-criterion requirement text.
