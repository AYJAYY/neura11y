---
title: "Section 508 Technical Standards"
standard: "Section 508"
source_url: "https://www.access-board.gov/ict/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["section-508", "us", "federal", "ict", "software", "hardware", "procurement"]
ai_context: "Technical structure of the Revised Section 508 Standards. Load when you need chapter-level Section 508 requirements, not just the legal overview."
---

# Section 508 Technical Standards

**Status:** Revised 508 Standards final rule, issued January 18, 2017; effective January 18, 2018.

---

## How the Revised Standards Are Organized

The current Section 508 rule is split across:

- **Appendix A, Chapters 1-2** — application, definitions, scoping, exceptions
- **Appendix C, Chapters 3-7** — functional performance criteria and technical requirements
- **Appendix B** — Section 255 telecommunications guidance (related, but not the core Section 508 scope for most web/document tasks)

For most repository use cases, the key structure is:

| Chapter | What it covers | Why it matters |
|---------|----------------|----------------|
| 2 | Scoping requirements | Determines when ICT must conform |
| 3 | Functional performance criteria | Fallback requirements across disability types |
| 4 | Hardware | Kiosks, closed functionality, telecom, physical controls |
| 5 | Software | AT interoperability, application behavior, authoring tools |
| 6 | Support documentation and services | Accessible help, manuals, support channels |
| 7 | Referenced standards | Incorporates WCAG 2.0 and other external standards |

---

## Chapter 2 — Scoping Requirements

These sections determine what must conform and when.

| Section | Requirement Summary |
|---------|---------------------|
| `E201` | ICT procured, developed, maintained, or used by federal agencies must conform |
| `E202` | Exceptions: legacy ICT safe harbor, national security systems, incidental contractor ICT, maintenance-space controls, undue burden, fundamental alteration, and "best meets" procurement |
| `E203` | Agencies must provide access to the functionality needed by users with disabilities |
| `E204` | Functional performance criteria in Chapter 3 apply where relevant |
| `E205` | Electronic content is covered, including public-facing content and agency official communications |
| `E206` | Hardware must conform to Chapter 4 |
| `E207` | Software must conform to Chapter 5 and applicable WCAG requirements |
| `E208` | Support documentation and support services must conform to Chapter 6 |

### High-Impact Scoping Notes

- **Public-facing content** is explicitly covered under `E205.2`.
- **Agency official communication** is explicitly covered under `E205.3`.
- **Undue burden** and **fundamental alteration** require written documentation and an alternative means of access.
- **Best meets** applies when no fully conforming commercial product is available.

---

## Chapter 3 — Functional Performance Criteria

Chapter 3 provides user-needs-based requirements that complement the technical chapters.

| Section | User Need Covered |
|---------|-------------------|
| `302.1` | Without vision |
| `302.2` | With limited vision |
| `302.3` | Without perception of color |
| `302.4` | Without hearing |
| `302.5` | With limited hearing |
| `302.6` | Without speech |
| `302.7` | With limited manipulation |
| `302.8` | With limited reach and strength |
| `302.9` | With limited language, cognitive, and learning abilities |

Use Chapter 3 when evaluating whether ICT still works for users with disabilities even if a direct technical rule is unclear or incomplete.

---

## Chapter 4 — Hardware Requirements

Chapter 4 applies to hardware and closed-function ICT, including kiosks and telecom-related devices.

| Section | Requirement Area |
|---------|------------------|
| `402` | Closed functionality, speech output, braille instructions, volume, screen characters |
| `403` | Biometrics |
| `404` | Preservation of information provided for accessibility |
| `405` | Privacy |
| `406` | Standard connections for AT compatibility |
| `407` | Operable parts, tactile discernibility, contrast, key repeat, reach ranges |
| `408` | Display screens and flashing |
| `409` | Status indicators |
| `410` | Color coding |
| `411` | Audible signals |
| `412` | Two-way voice communication, RTT, caller ID, TTY support |
| `413` | Closed-caption processing technologies |
| `414` | Audio-description processing technologies |
| `415` | User controls for captions and audio descriptions |

This is the chapter to use for kiosks, multifunction devices, set-top boxes, self-service terminals, and other non-web physical ICT.

---

## Chapter 5 — Software Requirements

Chapter 5 is the core technical chapter for software, web apps, non-web software, and authoring tools.

| Section | Requirement Area |
|---------|------------------|
| `502` | Interoperability with assistive technology |
| `503` | Applications, user preferences, alternate UIs, caption/audio description controls |
| `504` | Authoring tools, including preservation of accessibility information and accessible PDF export |

### Section 502 — Interoperability with Assistive Technology

Section `502` requires software to expose accessibility information programmatically through platform accessibility services. Key requirement groups include:

- object information
- row/column/header relationships
- values and editable values
- label relationships
- hierarchical relationships
- text exposure and text modification
- action exposure
- focus tracking

This is the part of Section 508 that goes beyond a simple WCAG checklist for software products.

### Section 503 — Applications

Section `503` covers:

- preservation of user accessibility preferences
- alternate user interfaces where provided
- user controls for captions and audio descriptions

### Section 504 — Authoring Tools

Section `504` is especially important for CMSes, document editors, and publishing tools:

- accessibility information must be preserved during content creation/editing
- format conversion must preserve accessibility information
- PDF export must preserve accessibility information
- the tool should prompt for needed accessibility metadata
- accessible templates should be available

---

## Chapter 6 — Support Documentation and Services

Section 508 does not stop at product UI.

| Section | Requirement Area |
|---------|------------------|
| `602` | Support documentation, including electronic support docs |
| `603` | Support services, including communication accommodations |

This means help centers, manuals, release notes, and support workflows must also be accessible.

---

## Chapter 7 — Referenced Standards

Chapter 7 is where Section 508 incorporates external standards by reference.

High-value referenced standards include:

- **`702.10.1 WCAG 2.0`** — the core web/content/software accessibility baseline
- **`702.3.1 ANSI/AIIM/ISO 14289-1`** — PDF/UA
- telecommunications, hardware, and audio standards used by later technical chapters

For most web and document work, the practical result is:

- WCAG 2.0 Level A and AA is the baseline accessibility standard under Section 508
- PDF/UA is relevant for PDF-specific conformance requirements

---

## When WCAG 2.0 Applies Under Section 508

The main routing sections are:

| Section 508 Area | WCAG Relationship |
|------------------|-------------------|
| `E205 Electronic Content` | Applies WCAG 2.0 to web content and non-web documents, with word substitutions where needed |
| `E207 Software` | Applies WCAG 2.0 to software and non-web software, with word substitutions and software-specific additions |
| `E208 Support Documentation` | Electronic documentation often effectively inherits WCAG-style document requirements plus Chapter 6 obligations |

Section 508 is therefore **not just WCAG**:

- WCAG 2.0 is incorporated by reference
- Chapters 3, 5, and 6 add requirements that WCAG alone does not cover
- Chapter 4 covers hardware and closed functionality outside normal WCAG web scope

---

## Procurement and Compliance Implications

Use this file when the question is:

- "Which Section 508 chapter applies here?"
- "Does this ICT need WCAG, hardware rules, or software interoperability rules?"
- "What additional requirements exist beyond WCAG?"
- "What should be evaluated in a VPAT/ACR for software or hardware?"

Pair this file with:

- `standards/section-508/section-508-overview.md` for legal applicability
- `standards/section-508/section-508-wcag-mapping.md` for crosswalk guidance
- `standards/wcag/wcag-2.2-quick-ref.md` for current best-practice implementation targets
