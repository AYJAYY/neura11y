---
title: "Coverage Gaps"
type: "meta"
status: "curated"
last_updated: "2026-03-13"
ai_context: "Known gaps in repository coverage. Use to identify missing content before asserting completeness. Update after each content iteration."
---

# Coverage Gaps

Tracks known gaps in repository coverage, prioritized by impact. Updated after each content iteration and after AI validation runs.

---

## Priority 1 — Critical Gaps (Blocking for Core Use Cases)

These gaps mean AI outputs in the affected areas may be incomplete or hallucinated.

| Gap | Domain | Impact | Action |
|----|---------|--------|--------|
| WCAG techniques not yet fetched | Web | AI cannot cite specific technique IDs (e.g., H37, ARIA10) | Run `fetch-wcag.py` |
| WCAG understanding docs not yet fetched | Web | AI lacks normative intent for borderline SCs | Run `fetch-wcag.py` |
| Section 508 technical standards detail missing | Web/Docs | AI cannot confirm specific 508 mapping beyond WCAG 2.0 | Run `fetch-us-gov.py` |
| carousel.md component pattern not yet created | Web | AI lacks accessible carousel/slider pattern | ✅ Created |
| combobox.md component pattern not yet created | Web | AI lacks accessible combobox/autocomplete pattern | ✅ Created |
| tooltip.md component pattern not yet created | Web | AI lacks SC 1.4.13 content-on-hover pattern | ✅ Created |
| manual-testing-checklist.md not yet created | Web | AI lacks structured manual test procedure | ✅ Created |

---

## Priority 2 — Important Gaps (Reduced Quality)

| Gap | Domain | Impact | Action |
|----|---------|--------|--------|
| Screen reader HTML/ARIA support matrices missing | Web | AI cannot advise on SR-specific bugs or workarounds | ✅ Created (screen-reader-html-support.md + screen-reader-aria-support.md) |
| JAWS guide not yet created | Web | Incomplete SR testing coverage | ✅ Created |
| TalkBack guide not yet created | Web | Incomplete mobile SR testing coverage | ✅ Created |
| WCAG understanding docs not yet fetched | Web | AI lacks normative intent for borderline SCs | Run `fetch-wcag.py` |
| EN 301 549 non-web chapters missing | Non-web ICT | AI cannot address hardware/software accessibility outside web | Run `fetch-en-301-549.py` |
| EU/UK/Canada/Australia legal files missing | Legal | AI cannot provide UK/Canada/Australia legal guidance | ✅ Created (eu-eaa, uk, canada, australia) |
| EPUB metadata schema not yet created | EPUB | Incomplete EPUB accessibility coverage | ✅ Created |
| apca-contrast.md and color-blindness.md missing | Color/Visual | AI lacks APCA model detail and color blindness specifics | ✅ Created |

---

## Priority 3 — Nice-to-Have (Quality Improvements)

| Gap | Domain | Impact | Action |
|----|---------|--------|--------|
| Mobile accessibility (iOS/Android) patterns | Mobile | No mobile-specific web accessibility guidance | Manual curation |
| Touch target guidance (beyond SC 2.5.8) | Mobile | Incomplete touch interaction guidance | Manual curation |
| PWA accessibility patterns | Web | No progressive web app specific guidance | Manual curation |
| Video game accessibility | Gaming | Not covered | Out of scope for v1; add to backlog |
| Kiosk/embedded systems | Physical ICT | Not covered | Out of scope for v1 |
| Voice UI accessibility (Alexa, Siri) | Voice | Not covered | Backlog |
| PDF form field accessibility | Documents | Covered at high level; needs examples | Manual curation |
| Excel data visualization accessibility | Documents | Charts and graphs in Excel | Manual curation |
| Sign language considerations | Social Media | BSL/ASL video accessibility | Backlog |
| Subtitle vs. caption distinction by region | Social Media | Regional terminology varies | Manual curation |

---

## Phase Completion Status

| Phase | Description | Status | Completion |
|-------|-------------|--------|------------|
| 1 | Root files + meta/ | **Complete** | 2026-03-13 |
| 2 | Standards (/standards/) | **~85% complete** — WCAG 2.1/2.2, ARIA, 508, PDF/UA, EPUB, EN 301 549, ATAG created; techniques/understanding docs need fetching | 2026-03-13 |
| 3 | Web domains (/domains/web/) | **~80% complete** — checklist, semantics, focus, keyboard, forms, images, color, SPA, modal, tabs, accordion, nav, data-table, testing created; carousel, combobox, tooltip still needed | 2026-03-13 |
| 4 | Document domains (/domains/documents/) | **~70% complete** — Word, PowerPoint, PDF, Excel, plain language guides created; remediation-specific files and InDesign workflows not yet created | 2026-03-13 |
| 5 | Social media (/domains/social-media/) | **Complete** — all 7 platforms (Twitter/X, Instagram, LinkedIn, YouTube, Mastodon, Facebook, TikTok) + overview + alt text + captions + hashtag/inclusive writing created | 2026-03-13 |
| 6 | Cognitive, color, media, screen readers | **~85% complete** — COGA overview + design guide, contrast ratios, typography, color-blindness, APCA, screen reader overview + JAWS/NVDA/VoiceOver/TalkBack guides + HTML/ARIA support matrices, alt text decision tree, video captions guide, audio description created | 2026-03-13 |
| 7 | AI prompts + legal compliance | **~90% complete** — web audit, social media, document templates created; US ADA, EU EAA, UK, Canada, Australia legal files created | 2026-03-13 |
| 8 | Validation and gap filling | Not started | Requires Phases 2–7 completion |

---

## AI Validation Results

*Not yet run. After Phase 2 completion, run these validation tests:*

### Test 1: WCAG Audit
```
Load: standards/wcag/wcag-2.2-quick-ref.md + domains/web/web-accessibility-checklist.md
Prompt: Audit this HTML: <button onclick="submitForm()">Click here</button>
Expected: Cites SC 2.4.4 (Link Purpose), SC 4.1.2, notes that "click here" is non-descriptive
```

### Test 2: Alt Text Generation
```
Load: domains/social-media/alt-text/alt-text-principles.md + domains/social-media/platforms/instagram/instagram-guide.md
Prompt: Write an accessible Instagram post for an image of a product launch event
Expected: Alt text ≤ 125 chars, describes image meaningfully, notes platform character limit
```

### Test 3: Component Generation
```
Load: standards/aria/wai-aria-1.2-roles.md + domains/web/component-patterns/modal-dialog.md
Prompt: Generate accessible HTML for a modal dialog
Expected: Uses role="dialog", aria-modal="true", aria-labelledby, focus trap, Escape key handler
```

---

## Known Issues

| Issue | File | Severity | Status |
|-------|------|----------|--------|
| WCAG 2.2 SC 2.4.13 (Focus Appearance Enhanced) is AAA but often confused with 2.4.11 (AA) | `standards/wcag/wcag-2.2-quick-ref.md` | Medium | Note added in file |
| PDF/UA full spec requires ISO purchase; only free summary available | `standards/pdf-ua/pdf-ua-overview.md` | Low | Documented |
| EN 301 549 Chapter 9 largely defers to WCAG 2.1; avoid duplication | `standards/en-301-549/` | Low | Documented |
| Platform social media guides must be verified monthly; UI changes frequently | All platform files | High | Flagged in update-schedule.md |
