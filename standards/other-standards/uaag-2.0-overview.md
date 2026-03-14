---
title: "UAAG 2.0 — User Agent Accessibility Guidelines Overview"
standard: "UAAG 2.0"
source_url: "https://www.w3.org/TR/UAAG20/"
domain: ["web", "software", "tools"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["uaag", "user-agents", "browsers", "media-players", "assistive-technology", "standards"]
ai_context: "Overview of UAAG 2.0 requirements for browsers, media players, reader apps, and other user agents. Load when advising on user agent or platform accessibility."
---

# UAAG 2.0 — User Agent Accessibility Guidelines Overview

**Status:** W3C Working Group Note, December 2015.

UAAG 2.0 is not a current Recommendation-track conformance target in the way WCAG 2.x is, but it remains useful as a structured reference for browser, media player, and reader application accessibility.

---

## What Is UAAG?

UAAG stands for **User Agent Accessibility Guidelines**.

A **user agent** is software that retrieves, renders, or helps users interact with web content, including:

- web browsers
- media players
- ebook readers
- browser extensions and add-ons
- reader modes and web-view shells
- apps that render web-based or document content

UAAG focuses on the accessibility of the **tool that presents content**, not just the content itself.

---

## UAAG's Five Principles

UAAG 2.0 organizes requirements under five principles:

| Principle | Focus |
|-----------|-------|
| 1. Perceivable | The user interface and rendered content must be perceivable |
| 2. Operable | The user interface must be operable, especially from keyboard and alternative input |
| 3. Understandable | The user interface and its documentation must be understandable and predictable |
| 4. Programmatic Access | Assistive technologies must be able to obtain and control accessibility-relevant information |
| 5. Specifications and Conventions | The user agent should implement accessibility features from relevant specs and platform conventions |

Principles 1-3 parallel WCAG's POUR concepts. Principles 4 and 5 are more specific to software, browsers, and platform interoperability.

---

## High-Value UAAG Guidance Areas

### Alternative Content and Missing Content

UAAG expects user agents to:

- render alternative text and other alternatives correctly
- make missing alternatives detectable
- help users repair or work around missing content where possible

### Text, Viewport, and Display Configuration

UAAG covers:

- text resizing and reflow
- viewport positioning and history
- zoom and orientation support
- user stylesheet support
- synthesized speech and volume controls

### Keyboard and Structural Navigation

UAAG gives strong emphasis to:

- full keyboard access
- avoiding keyboard traps
- sequential navigation
- direct navigation to headings, landmarks, and other structures
- efficient search within rendered content

### Media Control

UAAG addresses:

- pausing and controlling time-based media
- caption and alternative-content handling
- avoiding flashing content issues
- playback rate and navigation controls

### Documentation and Predictability

UAAG expects user agents to:

- document accessibility features clearly
- describe changes between versions
- behave predictably with focus and commands

### Assistive Technology Interoperability

UAAG emphasizes:

- platform accessibility services
- exposing accessible properties and relationships
- making DOMs or equivalent structures programmatically available
- ensuring AT can track focus and interact with content

---

## Conformance Model

Like WCAG and ATAG, UAAG uses **Level A, AA, and AAA** success criteria.

- **Level A** — minimum conformance
- **Level AA** — broader conformance target
- **Level AAA** — highest conformance target

Important caveat: UAAG 2.0 was published as a **Working Group Note**, not a W3C Recommendation, because it did not complete final Recommendation-track implementation testing.

That means UAAG is best used here as:

- structured guidance
- a design/review checklist for browsers and reader tools
- a source of implementation ideas for accessible software

---

## UAAG vs. WCAG vs. ATAG

| Standard | Primary Target |
|----------|----------------|
| WCAG | Web content and digital content |
| ATAG | Authoring tools that create content |
| UAAG | User agents that render or present content |

These standards work together:

- **WCAG** says what accessible content should do
- **ATAG** says what content-creation tools should do
- **UAAG** says what browsers and readers should do

---

## When to Use UAAG in This Repository

Load this file when advising on:

- browser accessibility features
- media player accessibility
- reader mode or web-view accessibility
- ebook reader accessibility
- kiosk or embedded browser shells
- software that renders HTML or document content

UAAG is especially useful when the question is about the **accessibility of the platform or rendering tool itself**, not just the accessibility of authored content.

---

## Recommended Pairings

- `standards/wcag/wcag-2.2-quick-ref.md` for content requirements
- `standards/other-standards/atag-2.0-overview.md` for authoring tool requirements
- `standards/section-508/section-508-technical-standards.md` for software interoperability requirements in US federal contexts
- `screen-readers/screen-reader-html-support.md` and `screen-readers/screen-reader-aria-support.md` for practical interoperability guidance
