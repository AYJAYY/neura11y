---
title: "WCAG 2.2 Failure Techniques"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/understanding-techniques"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["wcag", "wcag-2.2", "techniques", "failures", "common-failures"]
ai_context: "Curated list of documented WCAG failure techniques. Load when an audit needs concrete examples of what definitely fails conformance."
---

# WCAG 2.2 Failure Techniques

Documented failures are informative, but a documented failure is strong evidence that the content does **not** meet the relevant success criterion unless an accessible alternative is provided.

---

## Common Failure Techniques for Audits

### Images and Non-Text Content

| Failure | Description | Common SCs |
|---------|-------------|------------|
| `F13` | Text alternative does not include information conveyed by color or function | `1.1.1`, `1.4.1` |
| `F20` | Text alternatives are not updated when the non-text content changes | `1.1.1`, `4.1.2` |
| `F30` | Placeholder text, filename, or non-equivalent text used as the alternative | `1.1.1`, `1.2.1` |
| `F38` | Decorative handling is incorrect and causes meaningful content to be hidden from AT | `1.1.1` |
| `F39` | Decorative images use non-null alt text like `alt="image"` | `1.1.1` |
| `F65` | `alt` omitted entirely from relevant image elements | `1.1.1` |
| `F67` | Long description does not present equivalent information | `1.1.1`, `1.2.1` |
| `F71` | Text look-alikes are used without a text alternative | `1.1.1` |
| `F72` | ASCII art used without a text alternative | `1.1.1` |

### Media

| Failure | Description | Common SCs |
|---------|-------------|------------|
| `F74` | Media alternative is not labeled as an alternative | `1.2.2`, `1.2.8` |
| `F75` | Synchronized media is provided without captions | `1.2.2` |
| `F113` | Important visual information is not audio-described despite available pauses | `1.2.5` |

### Structure and Relationships

| Failure | Description | Common SCs |
|---------|-------------|------------|
| `F33` | White space used to create multiple columns or structure | `1.3.1`, `1.3.2` |
| `F34` | White space used to format tables or layout | `1.3.1`, `1.3.2` |
| `F42` | Links or controls are emulated with non-semantic elements | `1.3.1`, `2.1.1`, `4.1.2` |
| `F43` | Structural markup does not represent the actual relationship in content | `1.3.1` |
| `F46` | Layout tables are given data-table semantics | `1.3.1` |
| `F48` | `pre` is used to present tabular data instead of proper structure | `1.3.1` |
| `F90` | `headers` and `id` associations are incorrect | `1.3.1` |
| `F91` | Table headers are not marked up correctly | `1.3.1` |
| `F92` | `role="presentation"` removes real semantic information | `1.3.1` |
| `F111` | Visible control label is not exposed in the accessible name | `1.3.1`, `2.5.3`, `4.1.2` |

### Visual Presentation and Resize

| Failure | Description | Common SCs |
|---------|-------------|------------|
| `F69` | Content or functionality is lost when text is resized | `1.4.4` |
| `F80` | Text-based form controls do not resize correctly | `1.4.4` |

---

## Audit Heuristics

If you see these patterns, check failure techniques immediately:

- image without `alt`
- icon-only control without accessible name
- `div`/`span` used as interactive control
- tables that visually look like data tables but have no headers
- placeholder-only form fields
- hover/focus tooltips that disappear on pointer movement
- media without corrected captions

---

## Notes

- Failure techniques are particularly useful in code review, audit findings, and training.
- Cite the failure technique together with the success criterion, not as a replacement for the criterion.
- Pair this file with `standards/wcag/wcag-2.2-quick-ref.md` for requirement text and with `standards/wcag/wcag-techniques/sufficient-techniques.md` for remediation options.
