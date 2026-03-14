---
title: "Repository Index"
type: "index"
status: "curated"
last_updated: "2026-03-13"
ai_context: "Machine-readable cross-reference map. Use this to navigate the repository without loading all files. Filter by standard, domain, tag, or conformance level."
---

# Repository Index

Machine-readable cross-reference map. Organized by standard, domain, and tag.

---

## By Standard

### WCAG 2.1
| File | Description | Status |
|------|-------------|--------|
| `standards/wcag/wcag-2.1-full.md` | Complete WCAG 2.1 specification | normative |
| `standards/wcag/wcag-2.1-quick-ref.md` | All 78 SCs with levels, intent, and techniques | normative |
| `standards/wcag/wcag-understanding/perceivable.md` | Understanding docs — Principle 1 | normative |
| `standards/wcag/wcag-understanding/operable.md` | Understanding docs — Principle 2 | normative |
| `standards/wcag/wcag-understanding/understandable.md` | Understanding docs — Principle 3 | normative |
| `standards/wcag/wcag-understanding/robust.md` | Understanding docs — Principle 4 | normative |
| `standards/wcag/wcag-techniques/sufficient-techniques.md` | WCAG sufficient techniques (HTML, CSS, ARIA, Script) | normative |
| `standards/wcag/wcag-techniques/advisory-techniques.md` | WCAG advisory techniques | normative |
| `standards/wcag/wcag-techniques/failure-techniques.md` | Documented WCAG failures | normative |

### WCAG 2.2
| File | Description | Status |
|------|-------------|--------|
| `standards/wcag/wcag-2.2-full.md` | Complete WCAG 2.2 specification | normative |
| `standards/wcag/wcag-2.2-quick-ref.md` | All 87 SCs with levels, intent, and techniques | normative |
| `standards/wcag/wcag-2.2-new-criteria.md` | The 9 new SCs added in WCAG 2.2 | normative |
| `standards/wcag/wcag-conformance-levels.md` | Level A, AA, AAA definitions and requirements | normative |

### WCAG 3.0
| File | Description | Status |
|------|-------------|--------|
| `standards/wcag/wcag-3.0-overview.md` | WCAG 3.0 working draft overview and key changes | normative |

### WAI-ARIA 1.2
| File | Description | Status |
|------|-------------|--------|
| `standards/aria/wai-aria-1.2-roles.md` | All ARIA roles with required/supported states and properties | normative |
| `standards/aria/wai-aria-1.2-states-properties.md` | All ARIA states and properties with allowed values | normative |
| `standards/aria/aria-authoring-practices.md` | APG patterns for common UI components | prescriptive |
| `standards/aria/aria-in-html.md` | ARIA in HTML specification — native semantics and overrides | normative |
| `standards/aria/aria-common-mistakes.md` | Curated list of common ARIA implementation errors | curated |

### Section 508
| File | Description | Status |
|------|-------------|--------|
| `standards/section-508/section-508-overview.md` | Section 508 overview, applicability, and legal context | normative |
| `standards/section-508/section-508-technical-standards.md` | Technical standards from Access Board ICT refresh | normative |
| `standards/section-508/section-508-wcag-mapping.md` | Mapping between Section 508 chapters and WCAG 2.0 SCs | curated |

### PDF/UA
| File | Description | Status |
|------|-------------|--------|
| `standards/pdf-ua/pdf-ua-overview.md` | PDF/UA (ISO 14289-1) overview and key requirements | normative |
| `standards/pdf-ua/matterhorn-protocol.md` | Matterhorn Protocol 1.1 — 136 PDF/UA checkpoints | normative |
| `standards/pdf-ua/pdf-ua-tagging-guide.md` | PDF tag structure and reading order requirements | prescriptive |

### EPUB Accessibility
| File | Description | Status |
|------|-------------|--------|
| `standards/epub/epub-accessibility-1.1.md` | EPUB Accessibility 1.1 specification | normative |
| `standards/epub/epub-metadata-schema.md` | a11y discovery metadata vocabulary | normative |

### EN 301 549
| File | Description | Status |
|------|-------------|--------|
| `standards/en-301-549/en-301-549-overview.md` | EN 301 549 overview and relationship to WCAG 2.1 | normative |
| `standards/en-301-549/en-301-549-requirements.md` | Non-web ICT requirements from EN 301 549 | normative |

### Other Standards
| File | Description | Status |
|------|-------------|--------|
| `standards/other-standards/atag-2.0-overview.md` | ATAG 2.0 overview — requirements for authoring tools | normative |
| `standards/other-standards/uaag-2.0-overview.md` | UAAG 2.0 overview — requirements for user agents | normative |
| `standards/other-standards/iso-9241-171.md` | ISO 9241-171 — ergonomics of software accessibility | normative |

---

## By Domain

### Web
| File | Description | Tags |
|------|-------------|------|
| `domains/web/web-accessibility-checklist.md` | Complete WCAG 2.2 AA checklist for web content | wcag, checklist, audit |
| `domains/web/html-semantics-guide.md` | Semantic HTML elements and their accessibility roles | html, semantics, aria |
| `domains/web/focus-management.md` | Focus management patterns for dynamic content | focus, keyboard, spa |
| `domains/web/keyboard-navigation-patterns.md` | Keyboard interaction patterns by component type | keyboard, patterns |
| `domains/web/forms-accessibility.md` | Forms: labels, errors, grouping, autocomplete | forms, labels, errors |
| `domains/web/images-and-media.md` | Images, SVG, video, audio accessibility | images, alt-text, media |
| `domains/web/color-and-contrast.md` | Contrast requirements, APCA, color independence | contrast, color |
| `domains/web/spa-accessibility.md` | Single-page app patterns: routing, live regions, focus | spa, react, angular |
| `domains/web/component-patterns/modal-dialog.md` | Accessible modal dialog pattern | modal, aria, focus-trap |
| `domains/web/component-patterns/navigation-menu.md` | Accessible navigation menu and disclosure pattern | menu, nav, disclosure |
| `domains/web/component-patterns/accordion.md` | Accessible accordion pattern | accordion, aria-expanded |
| `domains/web/component-patterns/carousel.md` | Accessible carousel/slider pattern | carousel, live-region |
| `domains/web/component-patterns/tabs.md` | Accessible tab panel pattern | tabs, tablist, tabpanel |
| `domains/web/component-patterns/combobox.md` | Accessible combobox/autocomplete pattern | combobox, listbox |
| `domains/web/component-patterns/data-table.md` | Accessible data table pattern | table, headers, scope |
| `domains/web/component-patterns/tooltip.md` | Accessible tooltip pattern | tooltip, aria-describedby |
| `domains/web/testing/automated-testing.md` | Automated accessibility testing tools and limitations | testing, axe, lighthouse |
| `domains/web/testing/manual-testing-checklist.md` | Manual testing procedures and screen reader testing | testing, manual, sr |
| `domains/web/testing/screen-reader-testing-matrix.md` | Browser/SR combinations for testing | testing, jaws, nvda, vo |

### Documents
| File | Description | Tags |
|------|-------------|------|
| `domains/documents/word-accessibility/word-checklist.md` | Microsoft Word accessibility checklist | word, documents |
| `domains/documents/word-accessibility/word-styles-guide.md` | Using Word styles for accessible structure | word, styles, headings |
| `domains/documents/powerpoint-accessibility/ppt-checklist.md` | PowerPoint accessibility checklist | powerpoint, slides |
| `domains/documents/powerpoint-accessibility/slide-layout-guide.md` | Accessible slide layout and reading order | powerpoint, layout |
| `domains/documents/pdf-creation/pdf-from-word.md` | Creating accessible PDF from Word | pdf, word, tags |
| `domains/documents/pdf-creation/pdf-from-indesign.md` | Creating accessible PDF from InDesign | pdf, indesign, tags |
| `domains/documents/pdf-creation/pdf-remediation.md` | Remediating existing PDFs for accessibility | pdf, remediation, acrobat |
| `domains/documents/excel-accessibility/excel-checklist.md` | Excel accessibility checklist | excel, spreadsheets |
| `domains/documents/plain-language/plain-language-guide.md` | Federal plain language guidelines | plain-language, writing |
| `domains/documents/plain-language/readability-guide.md` | Readability levels, Flesch-Kincaid, and cognitive load | readability, cognitive |

### Social Media
| File | Description | Tags |
|------|-------------|------|
| `domains/social-media/social-media-overview.md` | Overview of social media accessibility requirements | social-media |
| `domains/social-media/alt-text/alt-text-principles.md` | Alt text writing principles for all image types | alt-text, images |
| `domains/social-media/alt-text/alt-text-by-image-type.md` | Alt text approaches by image category | alt-text, images |
| `domains/social-media/alt-text/alt-text-examples.md` | Before/after alt text examples with annotations | alt-text, examples |
| `domains/social-media/captions-and-transcripts/caption-guide.md` | Caption writing standards and quality requirements | captions, webvtt |
| `domains/social-media/captions-and-transcripts/audio-description-guide.md` | Audio description for social media video | audio-description |
| `domains/social-media/captions-and-transcripts/webvtt-format.md` | WebVTT format reference | webvtt, captions |
| `domains/social-media/platforms/twitter-x/twitter-guide.md` | Twitter/X accessibility guide | twitter, platform |
| `domains/social-media/platforms/linkedin/linkedin-guide.md` | LinkedIn accessibility guide | linkedin, platform |
| `domains/social-media/platforms/instagram/instagram-guide.md` | Instagram accessibility guide | instagram, platform |
| `domains/social-media/platforms/facebook/facebook-guide.md` | Facebook accessibility guide | facebook, platform |
| `domains/social-media/platforms/tiktok/tiktok-guide.md` | TikTok accessibility guide | tiktok, platform |
| `domains/social-media/platforms/youtube/youtube-guide.md` | YouTube accessibility guide | youtube, platform |
| `domains/social-media/platforms/mastodon/mastodon-guide.md` | Mastodon accessibility guide | mastodon, platform |
| `domains/social-media/writing-for-accessibility/emoji-guide.md` | Accessible emoji usage | emoji, writing |
| `domains/social-media/writing-for-accessibility/hashtag-guide.md` | CamelCase hashtags and accessibility | hashtags, writing |
| `domains/social-media/writing-for-accessibility/inclusive-language.md` | Inclusive language guidelines | inclusive, language |

---

## By Success Criterion

### Perceivable (Principle 1)

| SC | Title | Level | Key Files |
|----|-------|-------|-----------|
| 1.1.1 | Non-text Content | A | `standards/wcag/wcag-2.2-quick-ref.md`, `domains/web/images-and-media.md`, `domains/social-media/alt-text/alt-text-principles.md` |
| 1.2.1 | Audio-only and Video-only | A | `domains/media/audio/transcripts.md`, `domains/media/video/video-accessibility.md` |
| 1.2.2 | Captions (Prerecorded) | A | `domains/social-media/captions-and-transcripts/caption-guide.md` |
| 1.2.3 | Audio Description or Media Alternative | A | `domains/media/video/audio-description.md` |
| 1.2.4 | Captions (Live) | AA | `domains/social-media/captions-and-transcripts/caption-guide.md` |
| 1.2.5 | Audio Description (Prerecorded) | AA | `domains/media/video/audio-description.md` |
| 1.3.1 | Info and Relationships | A | `domains/web/html-semantics-guide.md`, `standards/aria/wai-aria-1.2-roles.md` |
| 1.3.2 | Meaningful Sequence | A | `domains/web/html-semantics-guide.md` |
| 1.3.3 | Sensory Characteristics | A | `domains/web/web-accessibility-checklist.md` |
| 1.3.4 | Orientation | AA | `domains/web/web-accessibility-checklist.md` |
| 1.3.5 | Identify Input Purpose | AA | `domains/web/forms-accessibility.md` |
| 1.4.1 | Use of Color | A | `domains/web/color-and-contrast.md` |
| 1.4.2 | Audio Control | A | `domains/media/audio/audio-control.md` |
| 1.4.3 | Contrast (Minimum) | AA | `domains/web/color-and-contrast.md`, `color-and-visual/contrast-ratios.md` |
| 1.4.4 | Resize Text | AA | `domains/web/web-accessibility-checklist.md` |
| 1.4.5 | Images of Text | AA | `domains/web/images-and-media.md` |
| 1.4.10 | Reflow | AA | `domains/web/web-accessibility-checklist.md` |
| 1.4.11 | Non-text Contrast | AA | `domains/web/color-and-contrast.md` |
| 1.4.12 | Text Spacing | AA | `domains/web/web-accessibility-checklist.md` |
| 1.4.13 | Content on Hover or Focus | AA | `domains/web/component-patterns/tooltip.md` |

### Operable (Principle 2)

| SC | Title | Level | Key Files |
|----|-------|-------|-----------|
| 2.1.1 | Keyboard | A | `domains/web/keyboard-navigation-patterns.md` |
| 2.1.2 | No Keyboard Trap | A | `domains/web/focus-management.md` |
| 2.1.4 | Character Key Shortcuts | A | `domains/web/keyboard-navigation-patterns.md` |
| 2.2.1 | Timing Adjustable | A | `domains/web/web-accessibility-checklist.md` |
| 2.2.2 | Pause, Stop, Hide | A | `domains/web/component-patterns/carousel.md` |
| 2.4.1 | Bypass Blocks | A | `domains/web/html-semantics-guide.md` |
| 2.4.2 | Page Titled | A | `domains/web/web-accessibility-checklist.md` |
| 2.4.3 | Focus Order | A | `domains/web/focus-management.md` |
| 2.4.4 | Link Purpose (In Context) | A | `domains/web/html-semantics-guide.md` |
| 2.4.5 | Multiple Ways | AA | `domains/web/web-accessibility-checklist.md` |
| 2.4.6 | Headings and Labels | AA | `domains/web/html-semantics-guide.md` |
| 2.4.7 | Focus Visible | AA | `domains/web/focus-management.md` |
| 2.4.11 | Focus Appearance | AA | `domains/web/focus-management.md` (WCAG 2.2) |
| 2.4.12 | Focus Not Obscured (Minimum) | AA | `domains/web/focus-management.md` (WCAG 2.2) |
| 2.5.1 | Pointer Gestures | A | `domains/web/web-accessibility-checklist.md` |
| 2.5.2 | Pointer Cancellation | A | `domains/web/web-accessibility-checklist.md` |
| 2.5.3 | Label in Name | A | `domains/web/forms-accessibility.md` |
| 2.5.4 | Motion Actuation | A | `domains/web/web-accessibility-checklist.md` |
| 2.5.7 | Dragging Movements | AA | `domains/web/keyboard-navigation-patterns.md` (WCAG 2.2) |
| 2.5.8 | Target Size (Minimum) | AA | `domains/web/web-accessibility-checklist.md` (WCAG 2.2) |

### Understandable (Principle 3)

| SC | Title | Level | Key Files |
|----|-------|-------|-----------|
| 3.1.1 | Language of Page | A | `domains/web/web-accessibility-checklist.md` |
| 3.1.2 | Language of Parts | AA | `domains/web/web-accessibility-checklist.md` |
| 3.2.1 | On Focus | A | `domains/web/web-accessibility-checklist.md` |
| 3.2.2 | On Input | A | `domains/web/forms-accessibility.md` |
| 3.2.3 | Consistent Navigation | AA | `domains/web/web-accessibility-checklist.md` |
| 3.2.4 | Consistent Identification | AA | `domains/web/web-accessibility-checklist.md` |
| 3.2.6 | Consistent Help | A | `standards/wcag/wcag-2.2-new-criteria.md` (WCAG 2.2) |
| 3.3.1 | Error Identification | A | `domains/web/forms-accessibility.md` |
| 3.3.2 | Labels or Instructions | A | `domains/web/forms-accessibility.md` |
| 3.3.3 | Error Suggestion | AA | `domains/web/forms-accessibility.md` |
| 3.3.4 | Error Prevention | AA | `domains/web/forms-accessibility.md` |
| 3.3.7 | Redundant Entry | A | `standards/wcag/wcag-2.2-new-criteria.md` (WCAG 2.2) |
| 3.3.8 | Accessible Authentication (Minimum) | AA | `standards/wcag/wcag-2.2-new-criteria.md` (WCAG 2.2) |

### Robust (Principle 4)

| SC | Title | Level | Key Files |
|----|-------|-------|-----------|
| 4.1.1 | Parsing | A | `domains/web/web-accessibility-checklist.md` |
| 4.1.2 | Name, Role, Value | A | `standards/aria/wai-aria-1.2-roles.md`, `domains/web/html-semantics-guide.md` |
| 4.1.3 | Status Messages | AA | `domains/web/spa-accessibility.md` |

---

## By Tag

### alt-text
- `domains/social-media/alt-text/alt-text-principles.md`
- `domains/social-media/alt-text/alt-text-by-image-type.md`
- `domains/social-media/alt-text/alt-text-examples.md`
- `domains/web/images-and-media.md`
- `media/images/alt-text-decision-tree.md`

### captions
- `domains/social-media/captions-and-transcripts/caption-guide.md`
- `domains/social-media/captions-and-transcripts/webvtt-format.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 1.2.2, 1.2.4)

### contrast
- `domains/web/color-and-contrast.md`
- `color-and-visual/contrast-ratios.md`
- `color-and-visual/apca-contrast.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 1.4.3, 1.4.6, 1.4.11)

### forms
- `domains/web/forms-accessibility.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 1.3.5, 3.3.1–3.3.4)

### keyboard
- `domains/web/keyboard-navigation-patterns.md`
- `domains/web/focus-management.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 2.1.1, 2.1.2)

### screen-reader
- `screen-readers/jaws-guide.md`
- `screen-readers/nvda-guide.md`
- `screen-readers/voiceover-guide.md`
- `screen-readers/talkback-guide.md`
- `screen-readers/sr-html-support-matrix.md`
- `screen-readers/sr-aria-support-matrix.md`

### pdf
- `standards/pdf-ua/pdf-ua-overview.md`
- `standards/pdf-ua/matterhorn-protocol.md`
- `domains/documents/pdf-creation/pdf-from-word.md`
- `domains/documents/pdf-creation/pdf-remediation.md`

### social-media
- All files under `domains/social-media/`

### legal
- All files under `legal-and-compliance/`

---

## Priority Files (Load First for Any Task)

1. `standards/wcag/wcag-2.2-quick-ref.md` — Most comprehensive single-file reference
2. `domains/social-media/alt-text/alt-text-principles.md` — Highest cross-domain utility
3. `AI-USAGE-GUIDE.md` — Context-loading instructions
4. `INDEX.md` — This file (navigation)
5. `meta/standards-registry.md` — All sources with canonical URLs
