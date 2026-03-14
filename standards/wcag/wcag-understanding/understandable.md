---
title: "Understanding WCAG 2.2 — Understandable"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["wcag", "wcag-2.2", "understanding", "understandable", "principle-3"]
ai_context: "Principle-level understanding guide for WCAG Understandable requirements. Load when explaining language, consistency, help, forms, or authentication issues."
---

# Understanding WCAG 2.2 — Understandable

Understandable means users can comprehend both the information and the operation of the interface. Content should not surprise users, hide meaning behind jargon, or create avoidable memory burdens.

---

## What Understandable Protects Against

Users struggle when:

- language is unspecified or overly complex
- controls trigger unexpected changes
- navigation and help move around unpredictably
- forms expose errors without helping recovery
- authentication depends on memory, transcription, or cognitive puzzles

---

## Guideline Summary

| Guideline | Core Intent | High-Risk Areas |
|-----------|-------------|-----------------|
| `3.1 Readable` | Language and terminology should be understandable | page language, jargon, abbreviations |
| `3.2 Predictable` | Components should not surprise users | auto-submit, inconsistent help, navigation shifts |
| `3.3 Input Assistance` | Users need help entering, correcting, and confirming data | labels, errors, recovery, authentication |

---

## High-Value Success Criteria to Check Early

| SC | Why It Matters | Typical Failure Pattern |
|----|----------------|------------------------|
| `3.1.1` | Screen readers need correct language | missing `lang` on page |
| `3.1.2` | Pronunciation changes inside content matter | language changes in quotes or labels not marked |
| `3.2.2` | Input changes should not trigger surprise context changes | select box auto-submits without warning |
| `3.2.6` | Help should appear consistently | support link moves between pages |
| `3.3.1` | Users need clear error identification | generic “invalid input” with no field association |
| `3.3.2` | Users need labels and instructions before failing | unlabeled or ambiguous inputs |
| `3.3.3` | Users need suggestions to recover | error shown with no fix guidance |
| `3.3.4` | High-stakes submissions need prevention or confirmation | legal/financial submission with no review step |
| `3.3.7` | Re-entering known data creates unnecessary burden | repeated address entry in same process |
| `3.3.8` | Authentication should not rely on memory or puzzles | blocked password-manager paste, CAPTCHA transcription |

---

## User Benefits

Understandable requirements especially benefit:

- users with cognitive and learning disabilities
- users with memory or attention limitations
- users under stress, fatigue, or time pressure
- non-native speakers
- users relying on assistive tech announcements for context

---

## Common Implementation Themes

### Predictability Lowers Cognitive Load

Consistent layout, repeated help placement, and stable control behavior reduce the amount users must remember from page to page.

### Error Recovery Is Part of Accessibility

A field that becomes “invalid” without telling the user what to fix is not enough. Good recovery includes location, explanation, and next step.

### Authentication Should Not Demand Memory Tricks

Modern accessible authentication accepts password managers, passkeys, copy/paste, and other assistive mechanisms rather than blocking them.

---

## Frequent Audit Questions

- Is the page language specified and accurate?
- Does any control change context before the user is ready?
- If an error occurs, is the problem identified, associated with the field, and fixable?
- Does the flow force users to remember or retype information unnecessarily?
- Can users authenticate without a cognitive-function test or memory burden?

---

## Recommended Pairings

- `standards/wcag/wcag-2.2-quick-ref.md`
- `domains/web/forms-accessibility.md`
- `domains/documents/plain-language/plain-language-guide.md`
- `domains/documents/plain-language/readability-guide.md`
