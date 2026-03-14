---
title: "Coverage Gaps"
type: "meta"
status: "curated"
last_updated: "2026-03-14"
ai_context: "Known open gaps in repository coverage. Use to identify missing content before asserting completeness. Update after each content iteration."
---

# Coverage Gaps

Tracks **open gaps** in repository coverage, prioritized by impact. Resolved items from this pass are listed separately under "Closed in This Pass."

---

## Priority 1 — Critical Gaps (Open)

No open critical gaps at this time.

---

## Priority 2 — Important Gaps (Open)

No open important gaps at this time.

---

## Priority 3 — Nice-to-Have Backlog

| Gap | Domain | Impact | Action |
|----|---------|--------|--------|
| Video game accessibility | Gaming | Not covered | Out of scope for v1 |

---

## Closed in This Pass

| Item | Result |
|------|--------|
| `scripts/fetch-standards.py` WCAG group | Now includes raw techniques and understanding index sources so the fetch path matches repository expectations |
| `standards/wcag/wcag-techniques/` | Created curated sufficient, advisory, and failure technique files |
| `standards/wcag/wcag-understanding/` | Created principle-level understanding guides for Perceivable, Operable, Understandable, and Robust |
| `standards/other-standards/iso-9241-171.md` | Created software accessibility overview for ISO 9241-171 |
| `domains/web/mobile-accessibility-patterns.md` | Created mobile web accessibility guidance |
| `domains/web/pwa-accessibility.md` | Created PWA accessibility guidance |
| Document split files under `domains/documents/` | Added workflow-specific and checklist files for Word, PowerPoint, PDF, Excel, and readability |
| Social/media split files under `domains/social-media/` | Added image-type alt text, WebVTT, and emoji guidance files |
| `standards/section-508/section-508-technical-standards.md` | Created from locally available Access Board source material |
| `standards/section-508/section-508-wcag-mapping.md` | Created to clarify where Section 508 uses WCAG and where it adds requirements |
| `standards/other-standards/uaag-2.0-overview.md` | Created from locally available W3C source material |
| `AI-USAGE-GUIDE.md`, `README.md`, and `INDEX.md` stale references | Reconciled to the current canonical file set |
| Validation examples using the wrong expected WCAG criteria | Corrected to avoid false-positive citation guidance |
| `domains/documents/pdf-creation/pdf-form-accessibility-examples.md` | Added example-heavy PDF form field guidance |
| `domains/documents/excel-accessibility/excel-data-visualization-guide.md` | Added chart and dashboard accessibility examples for Excel |
| `domains/social-media/captions-and-transcripts/sign-language-video-guide.md` | Added sign-language-first and interpreted social video guidance |
| `domains/social-media/captions-and-transcripts/subtitles-vs-captions-by-region.md` | Added regional terminology note for captions vs subtitles |
| `domains/voice/voice-ui-accessibility.md` | Added voice UI accessibility guidance |
| `domains/physical-ict/kiosk-and-embedded-playbook.md` | Added kiosk and embedded systems implementation playbook |

---

## Phase Completion Status

| Phase | Description | Status | Completion |
|-------|-------------|--------|------------|
| 1 | Root files + `meta/` | **Complete** | 2026-03-13 |
| 2 | Standards (`/standards/`) | **Complete for current planned scope** — WCAG core, techniques, understanding, ARIA, Section 508, PDF/UA, EPUB, EN 301 549, ATAG, UAAG, and ISO 9241-171 overview are now present | 2026-03-14 |
| 3 | Web domains (`/domains/web/`) | **Complete for v1** — core web guides, component patterns, testing, screen reader support files, mobile patterns, and PWA guidance created | 2026-03-14 |
| 4 | Document domains (`/domains/documents/`) | **Complete for current planned scope** — broad guides plus split workflow/checklist files for Word, PowerPoint, PDF, Excel, and readability created | 2026-03-14 |
| 5 | Social media (`/domains/social-media/`) | **Complete for current planned scope** — platform guides, alt text, captions, inclusive writing, image-type alt text, WebVTT, and emoji guidance created | 2026-03-14 |
| 6 | Cognitive, color, media, screen readers | **~90% complete** — core guidance and support matrices created; additional split files remain optional | 2026-03-13 |
| 7 | AI prompts + legal compliance | **~90% complete** — key prompt templates and major legal files created | 2026-03-13 |
| 8 | Validation and gap filling | **In progress** — root docs reconciled and validation prompts corrected; end-to-end validation run still pending | 2026-03-14 |
| 9 | Voice + physical ICT (`/domains/voice/`, `/domains/physical-ict/`) | **Complete for current planned scope** — voice UI guide and kiosk/embedded systems playbook created | 2026-03-14 |

---

## AI Validation Results

*End-to-end validation has not been run yet. Use these corrected tests for the next validation pass.*

### Test 1: WCAG Audit

```
Load: standards/wcag/wcag-2.2-quick-ref.md + domains/web/html-semantics-guide.md
Prompt: Audit this HTML: <a href="/pricing" aria-label="View pricing plans">Click here</a>
Expected: Cites SC 2.4.4 and SC 2.5.3; does not falsely cite SC 4.1.2
```

### Test 2: Alt Text Generation

```
Load: domains/social-media/alt-text/alt-text-principles.md + domains/social-media/platforms/instagram/instagram-guide.md
Prompt: Write an accessible Instagram post for an image of a product launch event
Expected: Produces platform-appropriate alt text, keeps caption copy separate from alt text, and notes that exact platform limits should be verified if they matter
```

### Test 3: Component Generation

```
Load: standards/aria/wai-aria-1.2-roles.md + domains/web/component-patterns/modal-dialog.md
Prompt: Generate accessible HTML for a modal dialog
Expected: Uses role="dialog", aria-modal="true", aria-labelledby, focus trap, Escape key handler
```

---

## Known Issues

| Issue | File/Area | Severity | Status |
|-------|-----------|----------|--------|
| WCAG 2.2 SC `2.4.13` (AAA) is often confused with SC `2.4.11` (AA) | `standards/wcag/wcag-2.2-quick-ref.md` | Medium | Documented |
| PDF/UA full specification still depends on ISO/PDF Association distribution and cannot be fully mirrored as free normative text here | `standards/pdf-ua/` | Low | Documented |
| Platform social media guides need frequent verification because UI flows change | `domains/social-media/platforms/` | High | Flagged in `meta/update-schedule.md` |
| Full validation suite has not been run end-to-end after the latest file expansion | Repository-wide | Medium | Pending |
