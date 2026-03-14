---
title: "WCAG Conformance Levels"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/TR/WCAG22/#conformance"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["wcag", "conformance", "levels", "a", "aa", "aaa"]
ai_context: "Defines WCAG conformance levels A, AA, AAA with requirements for claiming conformance. Load when determining compliance level requirements."
---

# WCAG Conformance Levels

## Overview

WCAG 2.2 defines three conformance levels: A (minimum), AA (standard), and AAA (enhanced). These levels are cumulative — AA conformance requires satisfying all Level A AND all Level AA success criteria. AAA requires satisfying all A, all AA, and all AAA criteria.

Conformance levels apply to entire pages (or entire processes, where applicable), not to individual components in isolation.

---

## Level A — Minimum Conformance

- **Criteria count:** 30 success criteria (WCAG 2.2)
- **Meaning:** The most critical barriers are removed. Without Level A, some users cannot access the content at all.
- **Typical failures at this level:** images with no alt text, keyboard inaccessibility, no captions on prerecorded video, pages that change language without notification.
- **Legal baseline:** Level A alone is rarely sufficient for legal compliance frameworks. Most laws and standards require at least AA.

Level A criteria span all four POUR principles (Perceivable, Operable, Understandable, Robust). Failure of any single Level A criterion means the page does not conform at Level A, and therefore does not conform at any level.

---

## Level AA — Standard Conformance

- **Criteria count:** 50 success criteria total — all 30 Level A criteria PLUS all 20 Level AA criteria (WCAG 2.2)
- **Meaning:** Addresses the most significant barriers for users with disabilities across a broad range of assistive technologies and usage contexts.
- **Typical additions at this level:** sufficient color contrast (4.5:1 for normal text), live captions, orientation not locked, input purpose identifiable, reflow at 320px, non-text contrast 3:1, text spacing support, content on hover/focus, focus visible, multiple navigation methods, consistent navigation and identification, error suggestions, error prevention for legal/financial transactions, language of parts, status messages.
- **Legal baseline:** The most widely referenced level in accessibility law, regulation, and procurement policy worldwide (e.g., EN 301 549, Section 508, AODA, EAA).

### Critical Clarification: What AA Conformance Means

AA conformance does NOT mean satisfying 50% of criteria or only the AA-labelled criteria. It means satisfying ALL Level A criteria AND ALL Level AA criteria — every single one of the 50 applicable criteria without exception. A single unresolved failure of any A or AA criterion means the page does not conform at Level AA.

---

## Level AAA — Enhanced Conformance

- **Criteria count (WCAG 2.1):** 78 success criteria total — all A, AA, and AAA criteria
- **Criteria count (WCAG 2.2):** 87 success criteria total — all A, AA, and AAA criteria (includes 9 new criteria added in 2.2; note 4.1.1 Parsing is obsolete/always-passes)
- **Meaning:** The highest level of accessibility. Not recommended as a blanket conformance target for entire sites because some AAA criteria cannot be met for all content types.
- **W3C guidance:** "It is not recommended that Level AAA conformance be required as a general policy for entire sites because it is not possible to satisfy all Level AAA Success Criteria for some content." (WCAG 2.2 spec)
- **Appropriate use:** Target specific AAA criteria that are achievable and beneficial for your user base rather than claiming full AAA conformance.

---

## The Five Conformance Requirements

To claim conformance to WCAG 2.2 at a given level (A, AA, or AAA), all five of the following requirements must be met:

### Requirement 1: Conformance Level

One of the following levels must be fully met: Level A, Level AA, or Level AAA. Meeting a level means satisfying every applicable success criterion at that level (and all lower levels). There is no partial credit within a level.

### Requirement 2: Full Pages

Conformance applies to full Web pages. No part of a page may be excluded from the conformance claim. If any part of a page fails a criterion, the entire page fails that criterion.

**Important:** A page that relies on a conforming alternate version for inaccessible content can still claim conformance only if the alternate version is reachable from the non-conforming page and the non-conforming page does not interfere with the user's ability to access the alternate version.

### Requirement 3: Complete Processes

If a Web page is part of a series of pages constituting a process (e.g., a multi-step checkout or form submission), all pages in the process must conform at the claimed level. A process fails if any page within it fails.

**Example:** If pages 1–3 of a checkout conform at AA but page 4 (the confirmation page) fails SC 1.3.1, the entire checkout process fails AA conformance.

### Requirement 4: Accessibility-Supported Technologies Only

Only accessibility-supported ways of using technologies are relied upon. A technology is "accessibility supported" when:
- The way it is used is supported by users' assistive technologies (AT), AND
- The user agents and AT that support the technology are available to users with disabilities.

Technologies that are not accessibility-supported may be used (e.g., for enhancement), but the content must remain accessible when that technology is turned off or not supported. Authors cannot rely on a technology if it is not accessibility-supported.

**Implication:** You cannot claim conformance by relying solely on CSS, JavaScript, or SVG features that are not supported by common AT/browser combinations unless a fallback is provided.

### Requirement 5: Non-Interference

Using non-conforming technologies (e.g., decorative Flash, auto-playing video) must not interfere with the user's ability to access the rest of the page. The following success criteria must be satisfied even for non-conforming content:

- **1.4.2** Audio Control
- **2.1.2** No Keyboard Trap
- **2.3.1** Three Flashes or Below Threshold
- **2.2.2** Pause, Stop, Hide

These four criteria are designated as "non-interference" requirements. Failure of any of these, even in content that is otherwise excluded from the conformance claim, voids conformance for the entire page.

---

## Conformance Claims

A conformance claim is an optional, formal statement that a page meets WCAG at a given level. It is not required by WCAG itself, but is often required by legal frameworks or procurement contracts.

### Required Components of a Conformance Claim

1. **Date** of the claim
2. **Guidelines title, version, and URI** (e.g., "Web Content Accessibility Guidelines 2.2 at https://www.w3.org/TR/WCAG22/")
3. **Conformance level** satisfied (Level A, AA, or AAA)
4. **A concise description** of the Web content covered (e.g., URL or set of URLs)
5. **A list of Web content technologies relied upon**

### Optional Components

- A list of accessibility-supported Web content technologies used
- A list of user agents (including AT) used to verify conformance
- Information about any additional steps taken beyond the minimum

---

## Partial Conformance

### Partial Conformance — Third-Party Content

A page may claim partial conformance when it cannot control all of its content. The claim must use this form:

> "This page does not conform, but would conform to WCAG 2.2 at level [X] if the following parts were removed: [description of third-party content]."

**Conditions:**
- The non-conforming content must be provided by a third party over whom the author has no control.
- The author must otherwise ensure the page satisfies all criteria.

**Examples of third-party content:** embedded social media feeds, third-party chat widgets, user-generated content in forums, third-party payment iframes.

### Partial Conformance — Language

A page may claim partial conformance when the page is in a language for which an accessible user agent or AT does not exist. The statement must specify the language affected.

---

## Iframes and Third-Party Content

Iframes embedded in a page are part of that page for conformance purposes. If an iframe contains content that fails a success criterion, the embedding page fails that criterion — even if the iframe content is served from a third-party domain.

**Practical implications:**
- A third-party chat widget, cookie consent banner, or embedded map that fails SC 1.4.3 (color contrast) causes the host page to fail SC 1.4.3.
- Authors who cannot remediate third-party iframe content should consider the partial conformance statement above, or switch to conforming alternatives.
- When procuring third-party products, Voluntary Product Accessibility Templates (VPATs) / Accessibility Conformance Reports (ACRs) should be obtained and reviewed.

---

## Common Misconceptions

### Misconception 1: "AA means we only need to meet AA-labeled criteria."

**Incorrect.** Level AA conformance requires meeting ALL Level A criteria AND ALL Level AA criteria — all 50 applicable criteria in WCAG 2.2. The label "AA" on a criterion does not mean only AA-designated criteria need to be met.

### Misconception 2: "AA means we've met 50% of the criteria."

**Incorrect.** The letters A, AA, AAA do not represent percentages. They are ordinal severity/priority levels. There is no such thing as "50% conformance" in WCAG.

### Misconception 3: "We pass if most users can access the page."

**Incorrect.** Conformance is binary per criterion per page. A page either satisfies a criterion or it does not. There is no sliding scale based on percentage of users who can access content.

### Misconception 4: "A third-party widget is not our responsibility."

**Incorrect** for conformance purposes. Content embedded in your page is part of your page. If you control the decision to embed it, you are responsible for its accessibility impact. See the partial conformance provision for cases where you genuinely have no control.

### Misconception 5: "Level AAA is the goal all organizations should pursue."

**Incorrect as a blanket policy.** W3C explicitly recommends against requiring AAA conformance for entire sites because some AAA criteria are impossible to satisfy for certain content types. A more effective approach is selecting high-impact AAA criteria to implement alongside full AA conformance.

### Misconception 6: "Passing an automated accessibility scan means we conform."

**Incorrect.** Automated tools detect a subset of issues — typically 30–40% of applicable success criteria. Manual testing, including testing with assistive technologies, is required to assess the full range of WCAG criteria.

---

## Criterion Count by Level (WCAG 2.2)

| Level | Criteria at That Level | Cumulative Total |
|-------|----------------------|-----------------|
| A     | 30                   | 30              |
| AA    | 20                   | 50              |
| AAA   | 28 (incl. 4.1.1 obsolete) | 87 (incl. 4.1.1) |

Note: SC 4.1.1 Parsing is formally listed in WCAG 2.2 but is noted as always passing for HTML and XML content given modern browsers. It is effectively obsolete. Some count tables show 86 "active" criteria; the official specification lists 87 numbered criteria at all levels combined.

---

## Reference: Conformance Section

The authoritative source for WCAG 2.2 conformance requirements is Section 5 of the specification:
https://www.w3.org/TR/WCAG22/#conformance
