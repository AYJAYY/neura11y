---
title: "Section 508 Overview"
standard: "Section 508"
source_url: "https://www.section508.gov/manage/laws-and-policies/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["section-508", "us", "federal", "legal", "compliance"]
ai_context: "US Section 508 overview including applicability, relationship to WCAG, and key requirements. Load for US federal accessibility compliance questions."
---

# Section 508 Overview

## What is Section 508?

Section 508 of the Rehabilitation Act of 1973 (29 U.S.C. § 794d) requires US federal agencies to develop, procure, maintain, and use information and communications technology (ICT) that is accessible to people with disabilities — both federal employees and members of the public.

Source: https://www.access-board.gov/ict/

---

## 2017 Refresh (Current Standard)

The Access Board published a final rule refreshing the Section 508 standards on January 18, 2017, effective March 20, 2018.

### Key change: WCAG 2.0 Level AA incorporated by reference

The 2017 refresh incorporates WCAG 2.0 Level AA by reference for:
- Web content (all 38 WCAG 2.0 Level A and AA success criteria)
- Software (with some exceptions)
- Electronic documents

This means all 38 WCAG 2.0 AA criteria (not WCAG 2.1 or 2.2) are legally required for federal ICT under Section 508 as of 2026.

**Note:** WCAG 2.0 does not include the 17 new criteria added in WCAG 2.1 or the 9 added in WCAG 2.2. Best practice is to target WCAG 2.1 or 2.2 AA, which is backwards-compatible with WCAG 2.0.

---

## Who Must Comply

Section 508 applies to:
- All US federal agencies (executive, legislative, judicial)
- Organizations receiving federal funding
- Contractors providing ICT to federal agencies
- Programs and activities receiving federal financial assistance

It does NOT directly apply to:
- Private sector organizations (covered by ADA Title III instead)
- State/local governments (covered by ADA Title II)

---

## What Is Covered (ICT Categories)

The 2017 refresh covers these ICT categories:

### E205 — Electronic Content
- Web pages and web applications
- Electronic documents (PDF, Word, Excel, PowerPoint)
- Content distributed or made available to the public
- All WCAG 2.0 Level A and AA criteria apply

### E206 — Software
- Desktop and web software applications
- Mobile apps
- Most WCAG 2.0 AA criteria apply, plus additional software-specific requirements

### E207 — Authoring Tools
- Software used to create electronic content
- Must produce accessible content and be accessible to authors with disabilities

### E208 — Support Documentation and Services
- User documentation must be accessible
- Help desk and support must be accessible

### Hardware-Specific Requirements (Chapters 4-7)
- E401 — Hardware (biometrics, keys, tactile output, etc.)
- E402 — Closed functionality (kiosks, ATMs, copiers)
- E403 — Telecommunications products
- E404 — Functional performance criteria (alternative input/output)

---

## Chapter 5 — Software Requirements

Software requirements that go beyond WCAG 2.0 include:

### 502 — Interoperability with Assistive Technology
- Software must not interfere with AT platform features
- Must support accessibility APIs (Windows: UIA/MSAA; macOS/iOS: NSAccessibility; Android: Accessibility Service API)
- Focus must be programmatically determinable and settable

### 503 — Applications
- User preferences for AT settings must be preserved
- Authoring functions must be accessible

---

## WCAG 2.0 vs Section 508

| Section | Requirement | WCAG Equivalent |
|---------|-------------|-----------------|
| 1194.22(a) | Text alternatives | 1.1.1 |
| 1194.22(b) | Multimedia alternatives | 1.2.1, 1.2.2 |
| 1194.22(c) | Color not sole means | 1.4.1 |
| 1194.22(d) | Readable without style | 1.3.1 |
| 1194.22(e) | Redundant links for image maps | 1.1.1 |
| 1194.22(f) | Client-side image maps | (covered) |
| 1194.22(g) | Row/column headers | 1.3.1 |
| 1194.22(h) | Markup for data tables | 1.3.1 |
| 1194.22(i) | Frames titled | 4.1.2 |
| 1194.22(j) | Flickering/flashing | 2.3.1 |
| 1194.22(k) | Text-only version | (last resort) |
| 1194.22(l) | Script alternatives | 1.1.1, 2.1.1 |
| 1194.22(m) | Applets/plugins accessible | 1.1.1, 2.1.1 |
| 1194.22(n) | Electronic forms | 1.3.1, 4.1.2 |
| 1194.22(o) | Skip navigation | 2.4.1 |
| 1194.22(p) | Timed responses | 2.2.1 |

---

## Voluntary Product Accessibility Template (VPAT)

The VPAT is the standard format for vendors to document their ICT accessibility compliance. Federal agencies use VPATs for procurement decisions.

VPAT versions:
- **VPAT 2.5** (current) — covers WCAG 2.1, Section 508, and EN 301 549

A completed VPAT becomes an **Accessibility Conformance Report (ACR)**.

Key sections of VPAT 2.5:
- Section 508 (WCAG 2.0 AA)
- WCAG 2.1 Success Criteria
- EN 301 549 Chapters 5-13

---

## Exceptions to Section 508

### Undue Burden
An agency may claim "undue burden" if compliance would impose a significant difficulty or expense. The agency must still provide equivalent access through alternative means.

### Fundamental Alteration
If compliance would fundamentally alter the nature of a program or activity.

### Archived/Legacy Content
The 2017 refresh does not retroactively require existing content to be updated, but all new content must comply.

---

## Enforcement

- Filed with the agency's Section 508 Coordinator
- Formal complaint to the agency's EEO office
- Complaint to the Access Board or DOJ
- Civil lawsuit under Section 508

---

## Key Resources

- Access Board technical standards: https://www.access-board.gov/ict/
- Section508.gov guidance: https://www.section508.gov/
- VPAT/ACR resources: https://www.itic.org/policy/accessibility/vpat
- Testing guidance: https://www.section508.gov/test/
