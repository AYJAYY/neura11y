---
title: "Section 508 to WCAG Mapping"
standard: "Section 508 + WCAG 2.0"
source_url: "https://www.access-board.gov/ict/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["section-508", "wcag", "mapping", "us", "federal", "compliance"]
ai_context: "Crosswalk between Section 508 scoping/technical chapters and WCAG 2.0 obligations. Load when comparing US federal compliance requirements with WCAG."
---

# Section 508 to WCAG Mapping

This file explains where Section 508 directly relies on WCAG 2.0 and where Section 508 adds requirements outside WCAG's scope.

---

## Core Rule

The Revised Section 508 Standards incorporate **WCAG 2.0** by reference through Chapter 7 (`702.10.1`) and then apply it through scoping sections such as `E205.4` and `E207.2`.

Practical interpretation:

- **Web content** under Section 508 is primarily measured against WCAG 2.0 Level A and AA.
- **Non-web documents** use the same WCAG success criteria with terminology substitutions.
- **Software** also uses WCAG 2.0-derived requirements, but must additionally satisfy software-specific Section 508 technical requirements.

Section 508 therefore equals:

`WCAG 2.0 A/AA where incorporated` + `Section 508 scoping rules` + `Section 508 technical additions`

---

## Mapping by ICT Type

| ICT Type | Main Section 508 Sections | WCAG Mapping | Additional Section 508 Requirements |
|----------|---------------------------|--------------|-------------------------------------|
| Public websites and web apps | `E205.2`, `E205.4` | WCAG 2.0 Level A and AA | Scoping, exceptions, procurement context |
| Agency official electronic communication | `E205.3`, `E205.4` | WCAG 2.0 Level A and AA | Same scoping rules as other covered electronic content |
| Non-web documents (PDF, Word, PPT, Excel) | `E205.4.1` | WCAG 2.0 Level A and AA with word substitutions | PDF/UA may also apply through Chapter 7 and procurement requirements |
| Non-web software | `E207.2`, `E207.2.1` | WCAG 2.0 Level A and AA with word substitutions | `502` interoperability, `503` applications |
| Authoring tools | `504` | Indirectly aligned with WCAG/ATAG concerns | Preservation of accessibility information, prompts, templates, accessible export |
| Hardware / kiosks / closed functionality | `E206`, Chapter 4 | No direct WCAG-only mapping | Hardware, speech output, tactile controls, reach ranges, caption controls |
| Support docs and services | `E208`, Chapter 6 | Electronic support docs often align with WCAG-style requirements | Accessible support documentation and communication accommodations |

---

## Word Substitution Rules

Section 508 explicitly adapts WCAG language for non-web content.

### Non-Web Documents

When WCAG is applied to non-web documents under `E205.4.1`, terms like "web page" are read as "non-web document" where appropriate.

### Non-Web Software

When WCAG is applied to non-web software under `E207.2.1`, terms like "web page" are read as "non-web software" where appropriate.

This is why Section 508 can use WCAG success criteria outside the browser-only context.

---

## Where Section 508 Goes Beyond WCAG

WCAG alone is not sufficient for the full Section 508 picture in these areas:

| Section 508 Area | Why WCAG Alone Is Not Enough |
|------------------|------------------------------|
| Chapter 3 functional performance criteria | Adds disability-user-needs coverage not expressed as normal WCAG SCs |
| `502` assistive technology interoperability | Requires software exposure through platform accessibility APIs |
| `503` application behavior | Adds software-specific requirements like preference handling and media controls |
| `504` authoring tools | Requires preservation of accessibility data and accessible export workflows |
| Chapter 4 hardware | Covers closed functionality, tactile controls, reach ranges, telecom, caption/audio-description controls |
| Chapter 6 support documentation/services | Requires accessible help content and support channels |

---

## Legacy 2000 Section 508 Crosswalk

Older VPATs and procurement documents still reference the legacy `1194.22` web provisions. This crosswalk helps interpret them against WCAG.

| Legacy Provision | Topic | Closest WCAG Equivalent |
|------------------|-------|-------------------------|
| `1194.22(a)` | Text alternatives | `1.1.1 Non-text Content` |
| `1194.22(b)` | Multimedia alternatives | `1.2.1`, `1.2.2` |
| `1194.22(c)` | Color not sole means | `1.4.1 Use of Color` |
| `1194.22(d)` | Readable without style sheets | `1.3.1 Info and Relationships` |
| `1194.22(e)` | Redundant links for image maps | `1.1.1` |
| `1194.22(g)` | Row and column headers | `1.3.1` |
| `1194.22(h)` | Data table markup | `1.3.1` |
| `1194.22(i)` | Frames titled | `4.1.2 Name, Role, Value` |
| `1194.22(j)` | Flicker / flashing | `2.3.1 Three Flashes or Below Threshold` |
| `1194.22(l)` | Script alternatives | `1.1.1`, `2.1.1`, `4.1.2` |
| `1194.22(n)` | Electronic forms | `1.3.1`, `3.3.x`, `4.1.2` |
| `1194.22(o)` | Skip repeated navigation | `2.4.1 Bypass Blocks` |
| `1194.22(p)` | Timed responses | `2.2.1 Timing Adjustable` |

This legacy table is useful for older contracts, but new federal work should be read through the **2017 refresh structure**, not only through `1194.22`.

---

## Practical Use

Use this file to answer:

- "Does Section 508 just mean WCAG?"
- "If software is not a website, which WCAG rules still apply?"
- "What extra Section 508 checks should I add to a WCAG audit?"
- "How should I interpret legacy VPAT references?"

Recommended pairings:

- `standards/section-508/section-508-overview.md`
- `standards/section-508/section-508-technical-standards.md`
- `standards/wcag/wcag-2.1-quick-ref.md` for strict federal conformance baselines
- `standards/wcag/wcag-2.2-quick-ref.md` for current best-practice targets
