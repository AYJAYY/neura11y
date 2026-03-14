---
title: "WCAG 3.0 Overview"
standard: "WCAG 3.0"
source_url: "https://www.w3.org/TR/wcag-3.0/"
domain: ["web", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["wcag", "wcag-3.0", "emerging", "working-draft", "w3ag"]
ai_context: "WCAG 3.0 Working Draft overview. NOT stable — do not use for compliance claims. Load only for awareness of emerging accessibility direction. Flag outputs as based on draft guidance."
---

# WCAG 3.0 Overview

**IMPORTANT:** WCAG 3.0 is a W3C Working Draft. It is NOT stable, NOT finalized, and NOT appropriate for compliance claims. All content here is subject to change. For current compliance requirements, use WCAG 2.2.

Source: https://www.w3.org/TR/wcag-3.0/
Official name: W3C Accessibility Guidelines (W3AG) 3.0 — note the name change from "Web Content"

---

## What is WCAG 3.0?

WCAG 3.0 (internally called "W3AG 3.0" to reflect broader scope) is the next major version of the W3C accessibility guidelines. It is a complete restructuring of WCAG, not an incremental update.

Key goals:
- Address limitations of WCAG 2.x (binary pass/fail doesn't reflect real-world accessibility)
- Expand scope to non-web ICT, XR, emerging technologies
- Better address cognitive accessibility needs
- Introduce a more nuanced scoring system
- Replace the pass/fail model with outcomes-based conformance

---

## Major Structural Changes from WCAG 2.x

### From Success Criteria to Outcomes

WCAG 2.x: Tests pass or fail based on measurable success criteria (binary)
WCAG 3.0: "Outcomes" replace success criteria; outcomes can have multiple methods for demonstrating conformance

### From POUR to Functional Needs

WCAG 2.x: Organized by 4 POUR principles (Perceivable, Operable, Understandable, Robust)
WCAG 3.0: Organized by functional needs (visual, auditory, cognitive, physical, speech, communication needs)

### New Conformance Model

WCAG 2.x: A, AA, AAA conformance levels (all-or-nothing per level)
WCAG 3.0: Bronze, Silver, Gold tiers
- **Bronze:** Core outcomes met; essential minimum
- **Silver:** Broader coverage; better addresses diverse needs
- **Gold:** Comprehensive coverage including cognitive and complex interaction needs

The scoring model is process-based: organizations demonstrate accessibility through testing, evaluation, and continuous improvement processes, not just point-in-time audits.

---

## Key New Concepts

### APCA (Accessible Perceptual Contrast Algorithm)

WCAG 3.0 is expected to incorporate APCA as the contrast model, replacing the simple luminance ratio (L1+0.05)/(L2+0.05) used in WCAG 2.x.

APCA differences from WCAG 2.x contrast:
- Accounts for spatial frequency (font size and weight affect perceptibility)
- Accounts for polarity (light text on dark background vs. dark on light)
- Non-linear relationship: a ratio of 3:1 at one font size doesn't equal the same perceptibility at a different size
- Uses Lightness contrast (Lc) values: target typically Lc 60 for normal body text
- Still experimental; values in WCAG 3.0 drafts are subject to change

**Important:** APCA is not normative in any current standard. WCAG 2.2 still uses the 4.5:1 / 3:1 / 7:1 model.

### Coga Integration

WCAG 3.0 integrates cognitive accessibility (COGA) guidance more deeply:
- Memory requirements
- Attention and distraction
- Clear and simple language
- Consistent interaction patterns
- Error prevention and recovery

### Broader Technology Scope

WCAG 3.0 is designed to cover:
- Native mobile apps
- Augmented/virtual reality (XR)
- Wearables
- IoT devices
- Non-web software
- Documents

### Critical Error Concept

WCAG 3.0 introduces "critical errors" — accessibility failures that are so severe they block the functional need entirely. Critical errors prevent achieving any conformance tier regardless of other passing outcomes.

---

## What Stays the Same

- Most accessibility requirements in WCAG 2.x map to WCAG 3.0 outcomes
- The underlying accessibility needs are the same
- Standards-based testing methods (with AT, keyboard, code inspection) remain relevant
- WCAG 2.x will remain the legal standard for years after WCAG 3.0 publishes

---

## WCAG 3.0 vs WCAG 2.2: When to Use Which

| Scenario | Use |
|----------|-----|
| Legal compliance (US, EU, UK, Canada) | WCAG 2.2 Level AA |
| Section 508 compliance | WCAG 2.0 Level AA (2017 refresh) |
| EN 301 549 compliance | WCAG 2.1 Level AA |
| Future-proofing design decisions | Aware of WCAG 3.0 direction |
| Cognitive accessibility guidance | COGA design guide (currently best source) |
| Contrast decisions | WCAG 2.2 (normative) + APCA awareness |

---

## Current Status (as of early 2026)

- WCAG 3.0 remains a Working Draft with significant open issues
- The conformance model is not yet stable
- Score calculations and tier thresholds are being revised
- No finalization date has been committed to by W3C
- Organizations should NOT use WCAG 3.0 for compliance claims
- WCAG 2.2 is the current recommended standard

---

## Resources

- WCAG 3.0 Working Draft: https://www.w3.org/TR/wcag-3.0/
- Explainer: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/
- WCAG 2.x to 3.0 comparison: https://www.w3.org/WAI/standards-guidelines/wcag/faq/
- APCA research: https://www.myndex.com/APCA/
