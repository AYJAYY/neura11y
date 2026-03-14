---
title: "APCA Contrast Model Guide"
standard: "APCA W3C Candidate (WCAG 3.0)"
source_url: "https://www.w3.org/TR/wcag-3.0/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["apca", "contrast", "wcag3", "color", "typography", "accessibility"]
ai_context: "Guide to the APCA (Accessible Perceptual Contrast Algorithm) contrast model proposed for WCAG 3.0. Covers Lc values, use cases, and comparison to WCAG 2.x contrast ratios. Load when advising on future-facing contrast decisions or WCAG 3.0 planning."
---

# APCA Contrast Model Guide

---

## What is APCA?

**APCA** (Accessible Perceptual Contrast Algorithm) is a contrast assessment method developed by Andrew Somers (Myndex Research) and proposed as the contrast model for **WCAG 3.0**.

APCA replaces the WCAG 2.x contrast ratio formula, which has been criticized for:
- Treating dark-on-light and light-on-dark as equivalent (they are not perceptually equal)
- Not accounting for font size, weight, or spatial frequency in determining readability
- Producing counterintuitive results (e.g., some blue-white combinations fail despite appearing readable)

---

## Core Concepts

### Lightness Contrast (Lc)
APCA outputs a **Lc value** (Lightness Contrast), not a ratio. Lc values range from 0 to approximately ±106.

- **Positive Lc:** Dark text on light background
- **Negative Lc:** Light text on dark background
- **Sign is important:** APCA is not symmetric; dark-on-light and light-on-dark have different minimum thresholds

### Perceptual Uniformity
APCA uses a perceptually uniform colorspace model (based on sRGB), which better correlates with how humans perceive contrast differences.

### Font-Dependent Thresholds
APCA thresholds vary based on **font size** and **font weight** — a key difference from WCAG 2.x which has fixed ratios regardless of typography.

---

## APCA Contrast Thresholds (Proposed for WCAG 3.0)

**Note:** These values are from the APCA WCAG3 Bridge specification (Silver/WCAG 3.0 working drafts) and may change as WCAG 3.0 is finalized. Do not use these as compliance requirements until WCAG 3.0 is adopted.

### Body Text (Normal Reading)

| Lc Value | Minimum Use Case |
|----------|-----------------|
| Lc 90 | Preferred for body text — body, captions, placeholder |
| Lc 75 | Minimum for normal weight body text |
| Lc 60 | Large, bold text (18pt+ bold or 24pt+ normal) |
| Lc 45 | Decorative or non-critical large text |
| Lc 30 | Non-content UI elements (dividers, inactive) |
| Below Lc 15 | Not perceivable; avoid for any content |

### Font Size × Weight Lookup Table (Simplified)

| Font Size | Regular Weight (400) | Bold Weight (700) |
|-----------|---------------------|-------------------|
| 12px | Lc 90 required | Lc 75 required |
| 14px | Lc 90 required | Lc 60 required |
| 16px | Lc 75 required | Lc 60 required |
| 18px | Lc 75 required | Lc 45 required |
| 24px | Lc 60 required | Lc 45 required |
| 36px+ | Lc 45 required | Lc 30 required |

*These are approximations. The full APCA lookup table (available at readtech.org/ARC/) provides precise values.*

---

## APCA vs. WCAG 2.x Contrast Ratio: Key Differences

| Aspect | WCAG 2.x Contrast Ratio | APCA Lc |
|--------|------------------------|---------|
| Output | Ratio (e.g., 4.5:1) | Lc value (e.g., 60) |
| Symmetry | Symmetric (dark-on-light = light-on-dark) | Asymmetric |
| Font consideration | None (fixed thresholds) | Thresholds vary by size and weight |
| Polarity | Not tracked | Positive (dark-on-light) vs negative (light-on-dark) |
| Color model | Relative luminance (WCAG formula) | Perceptually uniform sRGB model |
| Current status | Normative (WCAG 2.1, 2.2) | Proposed (WCAG 3.0 — not yet adopted) |

---

## When to Use APCA

### Current Guidance (2026)

- **WCAG 2.1/2.2 compliance** — Use WCAG 2.x ratios (4.5:1 / 3:1). APCA is not a recognized conformance criterion.
- **WCAG 3.0 readiness** — Consider APCA alongside WCAG 2.x to future-proof designs
- **Advanced design evaluation** — APCA can identify cases where WCAG 2.x passes but perceptual contrast is poor
- **Low vision / readability research** — APCA more accurately models perceptual readability

### Practical Approach

1. First ensure WCAG 2.x contrast ratio compliance (4.5:1 for normal text, 3:1 for large text)
2. Use APCA as a secondary check for readability quality
3. If APCA suggests higher contrast is needed, consider design improvements beyond the minimum

---

## Checking APCA Contrast

### Tools

| Tool | URL | Notes |
|------|-----|-------|
| APCA Contrast Calculator | readtech.org/ARC/ | Official reference implementation |
| Colour Contrast Analyser (updated) | TPGi.com | Desktop app, supports APCA |
| apcach (npm) | npm package | Programmatic APCA calculation |
| Figma plugins | Stark, Able, Contrast | Some support APCA mode |

### Code Example (APCA npm package)

```javascript
// npm install apcach
import { apcach } from 'apcach'

// Calculate Lc for text on background
const lc = apcach('#595959', '#ffffff')
console.log(lc)  // e.g., 60.2 — check against lookup table
```

---

## APCA Failure Examples

### Case 1: Medium Gray on White (WCAG passes, APCA warns)

```
Text: #767676 on #FFFFFF
WCAG 2.x ratio: 4.54:1  ← Passes (barely)
APCA Lc: ~45.0           ← Below Lc 75 for 16px regular body text
```

Many designs using near-minimum WCAG contrast for body text may need to be improved under APCA.

### Case 2: Bold Large Heading (APCA more permissive)

```
Text: #767676 on #FFFFFF — 36px Bold
WCAG 2.x ratio: 4.54:1  ← Passes (large text 3:1 required)
APCA Lc: ~45.0           ← Passes for 36px bold (Lc 45 threshold)
```

APCA allows lower absolute contrast for large bold text, which aligns with perceptual readability research.

---

## Status of WCAG 3.0 and APCA

As of 2026:
- WCAG 3.0 is in active development (W3C Working Draft)
- APCA is the proposed contrast method for WCAG 3.0
- **No legal enforcement of APCA** — all current laws reference WCAG 2.0 or 2.1
- WCAG 3.0 adoption timeline: not confirmed; estimated several years from formal recommendation

**Recommendation:** Monitor WCAG 3.0 progress. Design systems may wish to build APCA-compatible color scales now to reduce future remediation effort.

---

## Key Resources

- APCA research and tools: readtech.org/ARC/
- WCAG 3.0 working draft: w3.org/TR/wcag-3.0/
- APCA on GitHub: github.com/Myndex/SAPC-APCA
- WCAG 3.0 explainer: w3.org/WAI/standards-guidelines/wcag/wcag3-intro/
