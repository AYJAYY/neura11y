---
title: "Repository Index"
type: "index"
status: "curated"
last_updated: "2026-03-14"
ai_context: "Machine-readable cross-reference map. Lists current canonical files by standard, domain, and topic. Prefer these files over raw *-fetched.md source captures."
---

# Repository Index

Machine-readable cross-reference map. This index lists the current canonical files that exist in the repository.

---

## By Standard

### WCAG

| File | Description | Status |
|------|-------------|--------|
| `standards/wcag/wcag-2.1-full.md` | Complete WCAG 2.1 specification | normative |
| `standards/wcag/wcag-2.1-quick-ref.md` | WCAG 2.1 success criteria quick reference | normative |
| `standards/wcag/wcag-2.2-full.md` | Complete WCAG 2.2 specification | normative |
| `standards/wcag/wcag-2.2-quick-ref.md` | WCAG 2.2 success criteria quick reference | normative |
| `standards/wcag/wcag-2.2-new-criteria.md` | The 9 new success criteria added in WCAG 2.2 | normative |
| `standards/wcag/wcag-conformance-levels.md` | Level A, AA, AAA definitions and requirements | normative |
| `standards/wcag/wcag-3.0-overview.md` | WCAG 3.0 working draft overview | normative |
| `standards/wcag/wcag-techniques/sufficient-techniques.md` | High-value sufficient techniques with IDs | curated |
| `standards/wcag/wcag-techniques/advisory-techniques.md` | Advisory and beyond-minimum technique guidance | curated |
| `standards/wcag/wcag-techniques/failure-techniques.md` | Common documented WCAG failures | curated |
| `standards/wcag/wcag-understanding/perceivable.md` | Principle 1 understanding guide | curated |
| `standards/wcag/wcag-understanding/operable.md` | Principle 2 understanding guide | curated |
| `standards/wcag/wcag-understanding/understandable.md` | Principle 3 understanding guide | curated |
| `standards/wcag/wcag-understanding/robust.md` | Principle 4 understanding guide | curated |

### WAI-ARIA

| File | Description | Status |
|------|-------------|--------|
| `standards/aria/wai-aria-1.2-roles.md` | ARIA roles with required and supported states/properties | normative |
| `standards/aria/wai-aria-1.2-states-properties.md` | ARIA states and properties with allowed values | normative |
| `standards/aria/aria-authoring-practices.md` | APG patterns for common UI components | prescriptive |
| `standards/aria/aria-in-html.md` | ARIA in HTML rules for native semantics and overrides | normative |
| `standards/aria/aria-common-mistakes.md` | Curated list of common ARIA implementation errors | curated |

### Section 508

| File | Description | Status |
|------|-------------|--------|
| `standards/section-508/section-508-overview.md` | Legal and applicability overview for Section 508 | normative |
| `standards/section-508/section-508-technical-standards.md` | Chapter-level structure of the Revised 508 Standards | normative |
| `standards/section-508/section-508-wcag-mapping.md` | Crosswalk between Section 508 and WCAG use cases | curated |

### PDF/UA

| File | Description | Status |
|------|-------------|--------|
| `standards/pdf-ua/pdf-ua-overview.md` | PDF/UA overview and conformance context | normative |
| `standards/pdf-ua/matterhorn-protocol.md` | Matterhorn Protocol checkpoints for PDF/UA testing | normative |

### EPUB Accessibility

| File | Description | Status |
|------|-------------|--------|
| `standards/epub/epub-accessibility-1.1.md` | EPUB Accessibility 1.1 specification | normative |
| `standards/epub/epub-metadata-schema.md` | Accessibility discovery metadata vocabulary | normative |

### EN 301 549

| File | Description | Status |
|------|-------------|--------|
| `standards/en-301-549/en-301-549-overview.md` | EN 301 549 overview and relationship to WCAG 2.1 | normative |
| `standards/en-301-549/en-301-549-requirements.md` | Non-web ICT requirements from EN 301 549 | normative |

### Other Standards

| File | Description | Status |
|------|-------------|--------|
| `standards/other-standards/atag-2.0-overview.md` | ATAG 2.0 overview for authoring tools | prescriptive |
| `standards/other-standards/uaag-2.0-overview.md` | UAAG 2.0 overview for browsers and user agents | prescriptive |
| `standards/other-standards/iso-9241-171.md` | ISO 9241-171 software accessibility overview | curated |
| `media/video/webvtt-spec.md` | WebVTT 1.0 file-structure and cue-syntax overview | normative |

---

## By Domain

### Web

| File | Description | Tags |
|------|-------------|------|
| `domains/web/web-accessibility-checklist.md` | WCAG 2.2 AA checklist for web content | wcag, checklist, audit |
| `domains/web/html-semantics-guide.md` | Semantic HTML guidance and native role mapping | html, semantics, aria |
| `domains/web/focus-management.md` | Focus movement and restoration patterns | focus, keyboard, spa |
| `domains/web/keyboard-navigation-patterns.md` | Keyboard interaction patterns by component type | keyboard, patterns |
| `domains/web/forms-accessibility.md` | Labels, errors, grouping, autocomplete | forms, labels, errors |
| `domains/web/images-and-media.md` | Images, SVG, video, and audio accessibility | images, alt-text, media |
| `domains/web/color-and-contrast.md` | WCAG contrast and color-use guidance | contrast, color |
| `domains/web/spa-accessibility.md` | SPA routing, announcements, and focus handling | spa, react, live-region |
| `domains/web/mobile-accessibility-patterns.md` | Mobile web accessibility guidance | mobile, touch, gestures |
| `domains/web/pwa-accessibility.md` | Progressive web app accessibility guidance | pwa, offline, install |
| `domains/web/cms-authoring-workflow.md` | Accessibility requirements for CMS-driven publishing workflows | cms, authoring, workflow |
| `domains/web/design-to-development-handoff.md` | Accessibility expectations for design-to-development handoff | design, development, handoff |
| `domains/web/component-patterns/accordion.md` | Accessible accordion pattern | accordion, disclosure |
| `domains/web/component-patterns/carousel.md` | Accessible carousel pattern | carousel, rotation |
| `domains/web/component-patterns/combobox.md` | Accessible combobox/autocomplete pattern | combobox, listbox |
| `domains/web/component-patterns/data-table.md` | Accessible data table pattern | table, headers |
| `domains/web/component-patterns/modal-dialog.md` | Accessible modal dialog pattern | modal, focus-trap |
| `domains/web/component-patterns/navigation-menu.md` | Accessible navigation/disclosure menu pattern | menu, nav |
| `domains/web/component-patterns/tabs.md` | Accessible tabs pattern | tabs, tablist |
| `domains/web/component-patterns/tooltip.md` | Accessible tooltip/content-on-hover pattern | tooltip, aria-describedby |
| `domains/web/testing/automated-testing.md` | Automated accessibility testing tools and limits | testing, axe, lighthouse |
| `domains/web/testing/manual-testing-checklist.md` | Manual web accessibility testing procedure | testing, manual |
| `domains/web/testing/screen-reader-testing-matrix.md` | Browser and screen reader combinations to test | testing, sr |

### Documents

| File | Description | Tags |
|------|-------------|------|
| `domains/documents/word-accessibility/word-guide.md` | Microsoft Word accessibility guide | word, headings, alt-text |
| `domains/documents/word-accessibility/word-checklist.md` | Short Word accessibility checklist | word, checklist |
| `domains/documents/word-accessibility/word-styles-guide.md` | Word styles and structure guidance | word, styles |
| `domains/documents/powerpoint-accessibility/powerpoint-guide.md` | Microsoft PowerPoint accessibility guide | powerpoint, reading-order |
| `domains/documents/powerpoint-accessibility/ppt-checklist.md` | Short PowerPoint accessibility checklist | powerpoint, checklist |
| `domains/documents/powerpoint-accessibility/slide-layout-guide.md` | Slide layout and reading-order guidance | powerpoint, layout |
| `domains/documents/pdf-creation/pdf-accessibility-guide.md` | PDF creation and remediation guide | pdf, tags, remediation |
| `domains/documents/pdf-creation/pdf-form-accessibility-examples.md` | Example-heavy PDF form accessibility guide | pdf, forms, examples |
| `domains/documents/pdf-creation/pdf-from-word.md` | Accessible PDF workflow from Word | pdf, word, export |
| `domains/documents/pdf-creation/pdf-from-indesign.md` | Accessible PDF workflow from InDesign | pdf, indesign, export |
| `domains/documents/pdf-creation/pdf-remediation.md` | Focused PDF remediation guide | pdf, remediation |
| `domains/documents/excel-accessibility/excel-guide.md` | Microsoft Excel accessibility guide | excel, tables, charts |
| `domains/documents/excel-accessibility/excel-checklist.md` | Short Excel accessibility checklist | excel, checklist |
| `domains/documents/excel-accessibility/excel-data-visualization-guide.md` | Focused chart and dashboard accessibility guide | excel, charts, dashboards |
| `domains/documents/plain-language/plain-language-guide.md` | Federal plain language guidance | plain-language, writing |
| `domains/documents/plain-language/readability-guide.md` | Readability metrics and targets | readability, cognitive |
| `domains/documents/email-accessibility/email-and-newsletters-guide.md` | Accessible email and newsletter authoring guide | email, newsletter, html-email |
| `domains/documents/google-workspace/google-docs-guide.md` | Google Docs accessibility workflow guide | google-docs, workspace |
| `domains/documents/google-workspace/google-slides-guide.md` | Google Slides accessibility workflow guide | google-slides, workspace |
| `domains/documents/google-workspace/google-sheets-guide.md` | Google Sheets accessibility workflow guide | google-sheets, workspace |

### Social Media

| File | Description | Tags |
|------|-------------|------|
| `domains/social-media/social-media-overview.md` | Overview of social media accessibility requirements | social-media |
| `domains/social-media/alt-text/alt-text-principles.md` | Cross-platform alt text principles | alt-text, images |
| `domains/social-media/alt-text/alt-text-by-image-type.md` | Alt text strategies by image category | alt-text, image-types |
| `domains/social-media/alt-text/alt-text-examples.md` | Before/after alt text examples | alt-text, examples |
| `domains/social-media/captions-and-transcripts/caption-guide.md` | Caption writing and file-format guidance | captions, video, webvtt |
| `domains/social-media/captions-and-transcripts/audio-description-guide.md` | Audio description guidance for social video | audio-description |
| `domains/social-media/captions-and-transcripts/webvtt-format.md` | Focused WebVTT reference | webvtt, captions |
| `domains/social-media/captions-and-transcripts/sign-language-video-guide.md` | Sign language guidance for social video | sign-language, video |
| `domains/social-media/captions-and-transcripts/subtitles-vs-captions-by-region.md` | Terminology note for captions vs subtitles | captions, subtitles, terminology |
| `domains/social-media/platforms/twitter-x/twitter-guide.md` | Twitter/X accessibility guide | twitter, platform |
| `domains/social-media/platforms/linkedin/linkedin-guide.md` | LinkedIn accessibility guide | linkedin, platform |
| `domains/social-media/platforms/instagram/instagram-guide.md` | Instagram accessibility guide | instagram, platform |
| `domains/social-media/platforms/facebook/facebook-guide.md` | Facebook accessibility guide | facebook, platform |
| `domains/social-media/platforms/tiktok/tiktok-guide.md` | TikTok accessibility guide | tiktok, platform |
| `domains/social-media/platforms/youtube/youtube-guide.md` | YouTube accessibility guide | youtube, platform |
| `domains/social-media/platforms/mastodon/mastodon-guide.md` | Mastodon accessibility guide | mastodon, platform |
| `domains/social-media/writing-for-accessibility/emoji-guide.md` | Accessible emoji guidance | emoji, writing |
| `domains/social-media/writing-for-accessibility/hashtag-guide.md` | CamelCase hashtag guidance | hashtags, writing |
| `domains/social-media/writing-for-accessibility/inclusive-language.md` | Inclusive language guidance | inclusive, language |

### Voice

| File | Description | Tags |
|------|-------------|------|
| `domains/voice/voice-ui-accessibility.md` | Voice command and spoken UI accessibility guide | voice, speech, multimodal |

### Mobile

| File | Description | Tags |
|------|-------------|------|
| `domains/mobile/native-mobile-app-accessibility.md` | Native iOS and Android accessibility guidance | mobile, ios, android |

### Physical ICT

| File | Description | Tags |
|------|-------------|------|
| `domains/physical-ict/kiosk-and-embedded-playbook.md` | Kiosk and embedded systems accessibility playbook | kiosk, embedded, closed-functionality |

### Supporting Coverage

| Area | File | Description |
|------|------|-------------|
| Cognitive | `cognitive/coga-overview.md` | COGA overview and scope |
| Cognitive | `cognitive/coga-design-guide.md` | Cognitive accessibility design guidance |
| Color and Visual | `color-and-visual/contrast-ratios.md` | WCAG contrast ratio reference |
| Color and Visual | `color-and-visual/apca-contrast.md` | APCA overview and usage notes |
| Color and Visual | `color-and-visual/color-blindness.md` | Color blindness considerations |
| Color and Visual | `color-and-visual/typography.md` | Accessible typography guidance |
| Media | `media/images/alt-text-decision-tree.md` | Alt text decision tree |
| Media | `media/video/video-captions-guide.md` | Captions, transcripts, audio description, WebVTT, SRT |
| Media | `media/video/webvtt-spec.md` | WebVTT 1.0 overview for timed text files |
| Screen Readers | `screen-readers/screen-reader-overview.md` | Screen reader ecosystem overview |
| Screen Readers | `screen-readers/jaws-guide.md` | JAWS guide |
| Screen Readers | `screen-readers/nvda-guide.md` | NVDA guide |
| Screen Readers | `screen-readers/voiceover-guide.md` | VoiceOver guide |
| Screen Readers | `screen-readers/talkback-guide.md` | TalkBack guide |
| Screen Readers | `screen-readers/screen-reader-html-support.md` | HTML support matrix |
| Screen Readers | `screen-readers/screen-reader-aria-support.md` | ARIA support matrix |
| Legal | `legal-and-compliance/us-ada-overview.md` | US ADA overview |
| Legal | `legal-and-compliance/eu-eaa-overview.md` | EU EAA overview |
| Legal | `legal-and-compliance/uk-accessibility-regulations.md` | UK accessibility regulations |
| Legal | `legal-and-compliance/canada-accessibility.md` | Canada accessibility overview |
| Legal | `legal-and-compliance/australia-accessibility.md` | Australia accessibility overview |
| Prompts | `ai-prompts/web-content/audit-html-snippet.md` | Web audit prompt template |
| Prompts | `ai-prompts/web-content/generate-accessible-component.md` | Web component generation prompt template |
| Prompts | `ai-prompts/web-content/full-site-accessibility-review.md` | Full-site web review prompt template |
| Prompts | `ai-prompts/documents/accessible-document.md` | Document creation prompt template |
| Prompts | `ai-prompts/social-media/accessible-social-post.md` | Social post prompt template |
| Prompts | `ai-prompts/legal-and-compliance/check-accessibility-compliance.md` | Compliance review prompt template |
| Prompts | `ai-prompts/voice/accessible-voice-ui.md` | Voice UI prompt template |
| Prompts | `ai-prompts/physical-ict/accessible-kiosk-and-embedded.md` | Kiosk and embedded ICT prompt template |
| Reference | `GLOSSARY.md` | Canonical terminology |
| Reference | `reference/accessibility-tools.md` | Tools and testing resources |
| Reference | `reference/statistics.md` | Accessibility statistics and reference data |

---

## By Topic

### alt-text

- `domains/social-media/alt-text/alt-text-principles.md`
- `domains/social-media/alt-text/alt-text-by-image-type.md`
- `domains/social-media/alt-text/alt-text-examples.md`
- `domains/web/images-and-media.md`
- `media/images/alt-text-decision-tree.md`

### captions-and-audio-description

- `domains/social-media/captions-and-transcripts/caption-guide.md`
- `domains/social-media/captions-and-transcripts/audio-description-guide.md`
- `domains/social-media/captions-and-transcripts/webvtt-format.md`
- `domains/social-media/captions-and-transcripts/sign-language-video-guide.md`
- `domains/social-media/captions-and-transcripts/subtitles-vs-captions-by-region.md`
- `media/video/video-captions-guide.md`
- `media/video/webvtt-spec.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 1.2.x)

### color-and-contrast

- `domains/web/color-and-contrast.md`
- `color-and-visual/contrast-ratios.md`
- `color-and-visual/apca-contrast.md`
- `color-and-visual/color-blindness.md`

### forms

- `domains/web/forms-accessibility.md`
- `domains/web/html-semantics-guide.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 1.3.5, 3.3.x, 4.1.2)

### keyboard-and-focus

- `domains/web/keyboard-navigation-patterns.md`
- `domains/web/focus-management.md`
- `domains/web/mobile-accessibility-patterns.md`
- `domains/web/component-patterns/modal-dialog.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (SC 2.1.x, 2.4.x)

### mobile-and-pwa

- `domains/web/mobile-accessibility-patterns.md`
- `domains/web/pwa-accessibility.md`
- `domains/web/spa-accessibility.md`
- `domains/mobile/native-mobile-app-accessibility.md`
- `screen-readers/talkback-guide.md`
- `screen-readers/voiceover-guide.md`

### pdf-and-documents

- `domains/documents/pdf-creation/pdf-accessibility-guide.md`
- `domains/documents/pdf-creation/pdf-form-accessibility-examples.md`
- `domains/documents/pdf-creation/pdf-from-word.md`
- `domains/documents/pdf-creation/pdf-from-indesign.md`
- `domains/documents/pdf-creation/pdf-remediation.md`
- `standards/pdf-ua/pdf-ua-overview.md`
- `standards/pdf-ua/matterhorn-protocol.md`
- `domains/documents/word-accessibility/word-guide.md`
- `domains/documents/word-accessibility/word-checklist.md`
- `domains/documents/word-accessibility/word-styles-guide.md`
- `domains/documents/powerpoint-accessibility/powerpoint-guide.md`
- `domains/documents/powerpoint-accessibility/ppt-checklist.md`
- `domains/documents/powerpoint-accessibility/slide-layout-guide.md`
- `domains/documents/excel-accessibility/excel-guide.md`
- `domains/documents/excel-accessibility/excel-checklist.md`
- `domains/documents/excel-accessibility/excel-data-visualization-guide.md`
- `domains/documents/email-accessibility/email-and-newsletters-guide.md`
- `domains/documents/google-workspace/google-docs-guide.md`
- `domains/documents/google-workspace/google-slides-guide.md`
- `domains/documents/google-workspace/google-sheets-guide.md`

### authoring-workflows

- `domains/web/cms-authoring-workflow.md`
- `domains/web/design-to-development-handoff.md`
- `domains/documents/email-accessibility/email-and-newsletters-guide.md`
- `domains/documents/google-workspace/google-docs-guide.md`
- `domains/documents/google-workspace/google-slides-guide.md`
- `domains/documents/google-workspace/google-sheets-guide.md`
- `domains/mobile/native-mobile-app-accessibility.md`

### screen-reader-support

- `screen-readers/screen-reader-overview.md`
- `screen-readers/screen-reader-html-support.md`
- `screen-readers/screen-reader-aria-support.md`
- `screen-readers/jaws-guide.md`
- `screen-readers/nvda-guide.md`
- `screen-readers/voiceover-guide.md`
- `screen-readers/talkback-guide.md`

### section-508-and-legal

- `standards/section-508/section-508-overview.md`
- `standards/section-508/section-508-technical-standards.md`
- `standards/section-508/section-508-wcag-mapping.md`
- `legal-and-compliance/us-ada-overview.md`
- `legal-and-compliance/eu-eaa-overview.md`

### voice-ui

- `domains/voice/voice-ui-accessibility.md`
- `standards/other-standards/iso-9241-171.md`
- `standards/en-301-549/en-301-549-requirements.md`

### physical-ict

- `domains/physical-ict/kiosk-and-embedded-playbook.md`
- `standards/en-301-549/en-301-549-requirements.md`
- `standards/other-standards/iso-9241-171.md`

### wcag-techniques-and-understanding

- `standards/wcag/wcag-techniques/sufficient-techniques.md`
- `standards/wcag/wcag-techniques/advisory-techniques.md`
- `standards/wcag/wcag-techniques/failure-techniques.md`
- `standards/wcag/wcag-understanding/perceivable.md`
- `standards/wcag/wcag-understanding/operable.md`
- `standards/wcag/wcag-understanding/understandable.md`
- `standards/wcag/wcag-understanding/robust.md`

---

## Priority Files

1. `AI-USAGE-GUIDE.md` — context-loading instructions
2. `standards/wcag/wcag-2.2-quick-ref.md` — primary standards reference
3. `INDEX.md` — navigation map
4. `GLOSSARY.md` — terminology precision
5. `meta/standards-registry.md` — canonical sources and fetch targets

---

## Coverage Notes

- Canonical prompt templates now exist for every context-loading pattern documented in `AI-USAGE-GUIDE.md`.
- AI operations now include schema validation, reference auditing, chunk export, freshness sync, and pattern-level validation scripts.
- Remaining optional content backlog is limited to video game accessibility.
- Prefer canonical files listed here over raw `*-fetched.md` source captures.
