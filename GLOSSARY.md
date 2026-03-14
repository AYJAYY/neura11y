---
title: "Accessibility Glossary"
type: "reference"
status: "curated"
last_updated: "2026-03-13"
tags: ["glossary", "definitions", "terminology"]
ai_context: "Canonical definitions for accessibility terms used throughout this repository. Load this file when precision of terminology is required."
---

# Accessibility Glossary

Canonical definitions for terms used throughout this repository. Sources are cited for normative definitions. Definitions without a citation are synthesized from common usage in the field.

---

## A

**Accessibility** — The degree to which a product, service, or environment can be used by people with disabilities. In digital contexts, typically refers to conformance with WCAG and related standards.

**Accessible Name** — The text label computed by the browser's accessibility tree for an interactive or informational element. Determined by the accessible name computation algorithm. Sources: ARIA spec section 5.2.7; WCAG SC 4.1.2.

**Accessible Rich Internet Applications (ARIA)** — A W3C specification (WAI-ARIA) that defines roles, states, and properties to make dynamic web content and UI components accessible. Current version: WAI-ARIA 1.2 (June 2023). Source: https://www.w3.org/TR/wai-aria-1.2/

**ACAA** — Air Carrier Access Act (US). Prohibits discrimination against people with disabilities in air travel.

**ADA** — Americans with Disabilities Act (US, 1990). Title II covers state and local governments; Title III covers places of public accommodation. Federal courts have increasingly applied ADA to websites.

**Advisory Technique** — A WCAG technique that goes beyond what is required to satisfy a success criterion. Not required for conformance. Contrast with Sufficient Technique.

**APCA** — Accessible Perceptual Contrast Algorithm. An advanced contrast model proposed for WCAG 3.0 that accounts for spatial frequency, polarity, and font weight. Not yet normative. See: https://www.myndex.com/APCA/

**APG** — ARIA Authoring Practices Guide. W3C resource providing implementation patterns for common UI components using ARIA. Source: https://www.w3.org/WAI/ARIA/apg/

**Assistive Technology (AT)** — Software or hardware that helps people with disabilities use computers and digital content. Examples: screen readers, screen magnifiers, switch access, voice recognition, braille displays.

**ATAG** — Authoring Tool Accessibility Guidelines. W3C standard (version 2.0) defining requirements for tools that create web content. Source: https://www.w3.org/TR/ATAG20/

**Audio Description** — Narration added to a video to describe important visual elements not conveyed by the soundtrack alone. Required for Level AA under WCAG SC 1.2.5.

---

## B

**Baseline** — In WCAG, a set of web technologies that authors can rely on users having support for. Affects which techniques are sufficient.

**Braille Display** — Hardware device that converts digital text to braille characters via a row of refreshable pins. Used by people who are deafblind or prefer tactile reading.

---

## C

**Caption** — Text synchronized with audio in video content. Includes dialogue, speaker identification, sound effects, and music descriptions. Differs from subtitle (translation only). Required under WCAG SC 1.2.2 (Level A).

**COGA** — Cognitive and Learning Disabilities Accessibility Task Force. W3C group producing guidance for cognitive accessibility, including the COGA design guide and "Making Content Usable for People with Cognitive and Learning Disabilities."

**Color Contrast Ratio** — A mathematical ratio comparing the relative luminance of two colors, calculated per WCAG Success Criterion 1.4.3. Formula: (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter color. Minimum ratio: 4.5:1 for normal text (AA), 3:1 for large text (AA), 7:1 for enhanced text (AAA).

**Conformance** — The degree to which a web page satisfies WCAG requirements. Levels: A (minimum), AA (standard), AAA (enhanced).

**Conformance Level** — WCAG grades success criteria as Level A, AA, or AAA based on impact and implementation effort.

---

## D

**Decorative Image** — An image that adds no informational value to content. Should have empty alt text (`alt=""`) so screen readers skip it. Source: WCAG technique H67.

**Descriptive Link Text** — Link text that conveys the purpose of the link without needing surrounding context. Required under WCAG SC 2.4.4 (Level A) or 2.4.9 (Level AAA).

**DHTML** — Dynamic HTML. Historical term for JavaScript-driven page updates; now subsumed under general web development practice.

**DOM** — Document Object Model. The browser's in-memory tree representation of a web page. Screen readers and other AT typically interact with the accessibility tree derived from the DOM.

---

## E

**EN 301 549** — European harmonized standard for ICT accessibility, referenced by the European Accessibility Act. Current version: v3.2.1 (2021). Incorporates WCAG 2.1 Level AA by reference. Source: https://www.etsi.org/

**EPUB** — Electronic Publication format. Open standard for digital books. EPUB Accessibility 1.1 defines requirements for accessible ebooks. Source: https://www.w3.org/TR/epub-a11y-11/

**European Accessibility Act (EAA)** — EU Directive 2019/882, requiring accessibility of key products and services including websites, mobile apps, e-commerce, and banking. Transposition deadline: June 2022; enforcement deadline: June 2025.

---

## F

**Failure Technique** — A documented way of failing a WCAG success criterion. Listed in WCAG understanding documents. Presence of a failure technique means the page does not conform.

**Focus** — The keyboard focus indicator showing which interactive element is currently active. Visible focus is required under WCAG SC 2.4.7 (Level AA) and SC 2.4.11 (Level AA, WCAG 2.2).

**Focus Indicator** — The visual outline or other styling that shows which element has keyboard focus. WCAG 2.2 SC 2.4.11 requires minimum focus appearance: area ≥ perimeter × CSS pixel offset of 2 × 2 pixels; contrast ratio ≥ 3:1 against adjacent color.

**Focus Management** — The practice of programmatically controlling where keyboard focus moves, particularly important in single-page apps, modals, and dynamic content updates.

**Focus Trap** — A pattern (usually intentional in modals) that confines keyboard focus within a component until the user dismisses it. Required for modal dialogs; incorrect implementation is a common accessibility bug.

---

## G

**Guideline** — In WCAG, a high-level accessibility goal organized under one of four principles (POUR). Each guideline contains one or more testable success criteria.

---

## H

**Heading Hierarchy** — The ordered structure of `<h1>` through `<h6>` elements providing document outline. Must not skip levels (e.g., `<h1>` directly to `<h3>`). Supports WCAG SC 1.3.1.

---

## I

**Informative** — Content in a specification that explains or illustrates normative requirements but is not itself required for conformance. Contrast with normative.

**Input Purpose** — The specific semantic meaning of a form input (e.g., name, email, phone). Required to be programmatically determinable under WCAG SC 1.3.5 (Level AA).

---

## K

**Keyboard Accessible** — Achievable using only a keyboard (no pointer device). Required for all interactive content under WCAG SC 2.1.1 (Level A).

**Keyboard Trap** — A situation where keyboard focus becomes stuck in a component and cannot exit using standard keyboard navigation. This is a Level A failure under WCAG SC 2.1.2.

---

## L

**Landmark** — An ARIA role (or equivalent HTML5 sectioning element) that identifies major regions of a page. Common landmarks: `banner` (`<header>`), `navigation` (`<nav>`), `main` (`<main>`), `complementary` (`<aside>`), `contentinfo` (`<footer>`), `search`, `form`, `region`.

**Large Text** — Per WCAG: at least 18pt (24px) regular weight, or 14pt (approximately 18.67px) bold weight. Large text has a lower contrast requirement: 3:1 at Level AA.

**Live Region** — An ARIA feature (`aria-live`) that announces dynamic content changes to screen reader users without requiring focus to move. Values: `polite` (waits for user to be idle), `assertive` (interrupts immediately), `off`.

---

## M

**Matterhorn Protocol** — A framework for testing PDF/UA conformance, published by PDF Association. Defines 136 checkpoints for PDF accessibility testing.

**Minimum Bounding Box** — The smallest rectangle that encloses a UI component or focus indicator. Relevant to WCAG 2.2 SC 2.4.11 focus appearance requirements.

**MSAA** — Microsoft Active Accessibility. Legacy accessibility API for Windows. Largely superseded by UI Automation (UIA).

---

## N

**Non-Text Content** — Any content that is not a sequence of characters. Images, video, audio, controls, and CAPTCHA are all non-text content requiring text alternatives under WCAG SC 1.1.1.

**Normative** — In a specification, requirements that must be met for conformance (typically indicated by "must," "shall," "required"). Contrast with informative.

**NVDA** — NonVisual Desktop Access. Free, open-source screen reader for Windows. One of the most widely used screen readers globally.

---

## P

**PDF/UA** — PDF for Universal Accessibility. ISO standard (ISO 14289-1:2014) defining requirements for accessible PDF documents. "UA" stands for Universal Accessibility.

**Plain Language** — Communication that is clear, concise, and organized so the intended audience can find and understand the information. Governed in the US by the Plain Writing Act of 2010 and guidelines at plainlanguage.gov.

**POUR** — The four principles of WCAG: **P**erceivable, **O**perable, **U**nderstandable, **R**obust. All WCAG success criteria fall under one of these principles.

**Programmatically Determinable** — Information that can be read by user agents (browsers, screen readers) through standard APIs. Required by multiple WCAG success criteria (e.g., SC 1.3.1, 4.1.2).

---

## R

**Reading Order** — The sequence in which content is presented to screen readers and other AT. Must match the logical content order. Supported by WCAG SC 1.3.2.

**Relative Luminance** — The relative brightness of a color in a colorspace, normalized to 0 (black) and 1 (white). Used in WCAG contrast ratio calculations. Formula defined in WCAG 2.x success criterion 1.4.3.

**Role** — In ARIA, the semantic function of an element (e.g., `button`, `dialog`, `navigation`). Roles are required for programmatic determinability under WCAG SC 4.1.2.

---

## S

**Screen Magnifier** — Software that enlarges portions of the screen. Examples: ZoomText, macOS Zoom, Windows Magnifier. Relevant to WCAG reflow (SC 1.4.10) and text resize (SC 1.4.4).

**Screen Reader** — Software that converts digital text and UI information into speech or braille output. Major screen readers: JAWS (Windows), NVDA (Windows), VoiceOver (macOS/iOS), TalkBack (Android), Narrator (Windows).

**Section 508** — Section 508 of the US Rehabilitation Act. Requires federal agencies to make their ICT (information and communications technology) accessible. 2017 refresh incorporated WCAG 2.0 Level AA by reference. Technical standards: https://www.access-board.gov/ict/

**Semantic HTML** — HTML that conveys meaning through element choice rather than presentation. Examples: `<button>` for interactive controls, `<nav>` for navigation, `<h1>-<h6>` for headings. Foundation of accessibility without ARIA.

**Skip Navigation** — A link at the top of a page allowing keyboard users to bypass repeated navigation and jump directly to main content. Supports WCAG SC 2.4.1 (Level A).

**State** — In ARIA, a dynamic property of a widget that can change in response to user interaction (e.g., `aria-checked`, `aria-expanded`, `aria-selected`). Required under WCAG SC 4.1.2.

**Success Criterion (SC)** — A testable statement in WCAG that defines a specific accessibility requirement. Designated by a three-part number (e.g., SC 1.4.3 = Principle 1, Guideline 4, Criterion 3).

**Sufficient Technique** — A WCAG technique that, if followed correctly, satisfies a success criterion. Not the only way to satisfy a criterion, but a documented, reliable way.

**Switch Access** — An assistive technology input method using one or more switches (buttons). Used by people with limited motor control who cannot use standard keyboard or pointer.

---

## T

**Tab Order** — The sequence in which focusable elements receive focus when the user presses Tab. Must be logical and predictable. Source: WCAG SC 2.4.3 (Level A).

**TalkBack** — Google's built-in screen reader for Android devices.

**Text Alternative** — Text that serves as a substitute for non-text content. Includes `alt` attribute for images, captions for audio/video, and other programmatic labels.

**Transcript** — A text version of audio or video content. Required for audio-only content under WCAG SC 1.2.1 (Level A). For video, a transcript alone does not satisfy the synchronized captions requirement.

---

## U

**UAAG** — User Agent Accessibility Guidelines. W3C standard (version 2.0) defining requirements for browsers and media players. Source: https://www.w3.org/TR/UAAG20/

**UI Automation (UIA)** — Microsoft's primary Windows accessibility API. Replaced MSAA. Used by screen readers to get accessibility information from Windows applications.

---

## V

**VoiceOver** — Apple's built-in screen reader for macOS, iOS, iPadOS, tvOS, and watchOS.

---

## W

**WAI** — Web Accessibility Initiative. The W3C program that develops accessibility guidelines including WCAG, ARIA, ATAG, and UAAG. Source: https://www.w3.org/WAI/

**WCAG** — Web Content Accessibility Guidelines. W3C standard defining requirements for web content accessibility. Current stable version: WCAG 2.2 (October 2023). Source: https://www.w3.org/TR/WCAG22/

**WebVTT** — Web Video Text Tracks Format. W3C specification for timed text tracks (captions, subtitles, descriptions) for use with HTML `<track>` element. Source: https://www.w3.org/TR/webvtt1/

---

## Abbreviations Quick Reference

| Abbreviation | Full Term |
|---|---|
| ACAA | Air Carrier Access Act |
| ADA | Americans with Disabilities Act |
| APCA | Accessible Perceptual Contrast Algorithm |
| APG | ARIA Authoring Practices Guide |
| ARIA | Accessible Rich Internet Applications |
| AT | Assistive Technology |
| ATAG | Authoring Tool Accessibility Guidelines |
| COGA | Cognitive and Learning Disabilities Accessibility Task Force |
| DOM | Document Object Model |
| EAA | European Accessibility Act |
| EPUB | Electronic Publication |
| POUR | Perceivable, Operable, Understandable, Robust |
| SC | Success Criterion |
| SR | Screen Reader |
| UAAG | User Agent Accessibility Guidelines |
| UIA | UI Automation |
| WAI | Web Accessibility Initiative |
| WCAG | Web Content Accessibility Guidelines |
| WebVTT | Web Video Text Tracks |
