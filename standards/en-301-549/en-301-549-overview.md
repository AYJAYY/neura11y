---
title: "EN 301 549 Overview"
standard: "EN 301 549 v3.2.1"
source_url: "https://www.etsi.org/deliver/etsi_en/301500_302000/301549/03.02.01_60/en_301549v030201p.pdf"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["en-301-549", "europe", "eaa", "legal", "compliance", "wcag-2.1"]
ai_context: "European accessibility standard EN 301 549 overview. Incorporates WCAG 2.1 Level AA for web and non-web content. Referenced by the European Accessibility Act. Load for EU compliance questions."
---

# EN 301 549 Overview

**Standard:** EN 301 549 v3.2.1 (2021)
**Published by:** ETSI (European Telecommunications Standards Institute), jointly with CEN and CENELEC
**Full title:** "Accessibility requirements for ICT products and services"

EN 301 549 is the harmonized European standard referenced by the European Accessibility Act (EAA) and the Web Accessibility Directive.

---

## Relationship to WCAG

Chapter 9 of EN 301 549 v3.2.1 incorporates WCAG 2.1 Level AA by reference for web content.

**This means:** Organizations conforming to EN 301 549 v3.2.1 must meet all 50 WCAG 2.1 Level AA success criteria (the 30 Level A + 20 Level AA criteria from WCAG 2.1).

WCAG 2.1 requires WCAG 2.0 AA plus these additional 12 criteria:
- 1.3.4 Orientation (AA)
- 1.3.5 Identify Input Purpose (AA)
- 1.4.10 Reflow (AA)
- 1.4.11 Non-text Contrast (AA)
- 1.4.12 Text Spacing (AA)
- 1.4.13 Content on Hover or Focus (AA)
- 2.1.4 Character Key Shortcuts (A)
- 2.5.1 Pointer Gestures (A)
- 2.5.2 Pointer Cancellation (A)
- 2.5.3 Label in Name (A)
- 2.5.4 Motion Actuation (A)
- 4.1.3 Status Messages (AA)

---

## Standard Structure

| Chapter | Title | Scope |
|---------|-------|-------|
| 1–4 | Introduction, Scope, References, Definitions | — |
| 5 | Generic ICT requirements | All ICT |
| 6 | ICT with two-way voice communication | Phones, video calls |
| 7 | ICT with video capabilities | Video displays, players |
| 8 | Hardware | Physical ICT |
| 9 | Web | Web content (WCAG 2.1 AA) |
| 10 | Non-web documents | Office documents, PDFs |
| 11 | Software | Desktop/mobile apps |
| 12 | Documentation and support services | User documentation, help desks |
| 13 | ICT providing relay or emergency services | Telecoms services |
| Annexes A–F | Support annexes | |

---

## Chapter 9 — Web Content

Chapter 9 requires conformance with WCAG 2.1, Sections 5 through 13 of the WCAG specification. This covers all four POUR principles and all criteria at the required conformance level.

Key references:
- **9.1.x** — Perceivable (maps to WCAG Principle 1)
- **9.2.x** — Operable (maps to WCAG Principle 2)
- **9.3.x** — Understandable (maps to WCAG Principle 3)
- **9.4.x** — Robust (maps to WCAG Principle 4)

EN 301 549 clause numbering matches WCAG SC numbering prefixed with "9.". For example:
- EN 301 549 **9.1.4.3** = WCAG 2.1 **1.4.3** Contrast (Minimum)
- EN 301 549 **9.2.4.7** = WCAG 2.1 **2.4.7** Focus Visible

---

## Chapter 10 — Non-Web Documents

Chapter 10 applies WCAG 2.1 principles to non-web documents (PDF, Word, Excel, PowerPoint, EPUB).

Equivalent structure to Chapter 9 with modifications:
- Some web-specific criteria are not applicable to documents (e.g., 9.2.4.2 Page Titled is adapted)
- Additional document-specific requirements

Key Chapter 10 requirements:
- **10.1.1.1** Non-text content (images must have alt text)
- **10.1.3.1** Info and relationships (headings, lists, table structure)
- **10.1.4.3** Contrast minimum (same 4.5:1 / 3:1 thresholds)
- **10.2.4.2** Document titled
- **10.4.1.2** Name, role, value (interactive form fields)

---

## Chapter 11 — Software

Chapter 11 applies to software applications (desktop, mobile, web apps that are treated as software). Requirements beyond WCAG include:

### 11.5 — Interoperability with Assistive Technology
Software must:
- Use documented platform accessibility APIs
- Not disrupt AT on the platform
- Expose name, role, state, value, and boundaries for UI components

### 11.6 — Documented Accessibility Usage
Software that provides a UI must document all accessibility features, how to use AT with the software, and any known AT compatibility issues.

### 11.7 — User Preferences
Software must honor platform-level accessibility preferences (font size, contrast, motion settings) unless overriding is essential.

### 11.8 — Authoring Tools
If the software creates content, it must:
- Produce accessible content (meeting the applicable standard)
- Be accessible itself to people using AT
- Provide prompts to create accessible content

---

## Chapter 5 — Generic Requirements

Applies to all ICT:

### 5.2 — Activation of Accessibility Features
Accessibility features that are documented must be activatable through a mechanism at least as accessible as the standard operation of the ICT.

### 5.3 — Biometrics
Biometric identification must have an alternative that does not rely on biometrics (or is used in addition to, not instead of, other methods).

### 5.4 — Preservation of Accessibility Information During Conversion
If ICT converts content between formats, accessibility information in the source must be preserved to the extent technically possible.

### 5.5 — Operable Parts
Physical controls must be operable with limited dexterity. If keys are required, a keyboard alternative must be available.

### 5.7 — Key Repeat
Keyboard must allow adjusting key repeat rate or disabling it.

### 5.9 — Simultaneous User Actions
ICT that requires simultaneous actions (e.g., holding two keys) must have a sequential alternative.

---

## European Accessibility Act (EAA)

The EAA (EU Directive 2019/882) requires accessibility for:
- Computers and operating systems
- ATMs, ticketing machines, payment terminals
- Smartphones and tablets
- TV set-top boxes
- Telephony services and equipment
- Banking services
- E-books
- E-commerce

**Transposition deadline:** June 28, 2022 (all EU member states)
**Enforcement deadline:** June 28, 2025

EN 301 549 v3.2.1 is the harmonized standard that satisfies EAA requirements.

---

## Web Accessibility Directive

EU Directive 2016/2102 requires accessibility for public sector websites and mobile apps in EU member states. References EN 301 549 v3.2.1 (and thus WCAG 2.1 AA).

Applies to: government websites, government mobile apps, government-provided PDFs (published after September 2018).

---

## Key Differences: EN 301 549 vs Section 508

| Aspect | EN 301 549 v3.2.1 | Section 508 (2017) |
|--------|------------------|---------------------|
| WCAG version | WCAG 2.1 Level AA | WCAG 2.0 Level AA |
| Web scope | Chapter 9 | E205 |
| Document scope | Chapter 10 | E205 |
| Software scope | Chapter 11 | E206 |
| Hardware scope | Chapter 8 | Chapters 4-7 |
| Jurisdiction | EU | US federal |
