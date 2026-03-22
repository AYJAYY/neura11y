---
title: "Coverage Gaps"
type: "meta"
status: "curated"
last_updated: "2026-03-21"
ai_context: "Known open gaps in repository coverage. Use to identify missing content before asserting completeness. Update after each content iteration."
---

# Coverage Gaps

Tracks **open gaps** in repository coverage, prioritized by impact. The current repo now includes AI ingestion scripts, richer chunk metadata export, schema and reference validation, freshness and release-metadata sync, expanded pattern-level validation fixtures, and screen-reader vendor provenance.

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
| `scripts/export-ai-context.py` | Added chunked JSONL export and summary manifests for AI ingestion |
| `scripts/validate-frontmatter.py` | Added path-specific metadata schema validation |
| `scripts/validate-references.py` | Added repository-wide internal reference auditing |
| `scripts/validate-ai-suite.py` + `meta/ai-validation-fixtures.json` | Added repeatable validation harness covering all 8 AI usage patterns |
| `scripts/sync-freshness.py` | Added freshness manifest generation and registry synchronization |
| `scripts/fetch-all.py` | Now writes structured JSONL fetch logs and refreshes registry freshness metadata |
| `AI-USAGE-GUIDE.md` frontmatter guidance | Replaced single-schema assumption with canonical schemas by file class |
| Legal compliance frontmatter | Added `last_reviewed` to all legal files for consistent freshness handling |
| Prompt coverage under `ai-prompts/` | Added prompt packs for web component generation, full-site review, legal compliance, voice UI, and physical ICT |
| Authoring workflow coverage | Added email/newsletter, Google Docs/Slides/Sheets, CMS authoring, design handoff, and native mobile guidance |
| `media/video/webvtt-spec.md` | Added the missing WebVTT canonical target referenced by the standards registry |
| `meta/latest-ai-validation-report.md` | Generated a validation report showing the current structural and pattern checks passing |
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
| `standards/aria/accname-1.2.md` | Added accessible name and description computation reference for labeling and name-calculation tasks |
| `standards/aria/core-aam-1.2-*.md` | Split Core-AAM into AI-usable overview and mapping files with a retained full fetched capture |
| `standards/aria/html-aam-1.0-*.md` | Split HTML-AAM into overview, role mappings, attribute mappings, and accessible-name computation files |
| `standards/other-standards/wcag2ict-22-*.md` | Split WCAG2ICT into overview, guideline-comment, and glossary/appendix files for non-web interpretation |
| `domains/web/source/wai-tutorials/` + `media/images/images-tutorial-fetched.md` | Added WAI tutorial provenance captures for forms, tables, page structure, menus, and images |
| `scripts/fetch-screen-readers.py` + `screen-readers/source/` | Added vendor provenance fetch support for NVDA, VoiceOver, TalkBack, and JAWS source docs |
| `screen-readers/screen-reader-testing-workflows.md`, `mobile-screen-reader-testing.md`, `common-announcements-and-quirks.md` | Added task-oriented canonical screen-reader workflow guides on top of the per-tool files |
| `ai-prompts/screen-readers/` + `meta/ai-validation-fixtures.json` | Added 4 screen-reader prompt packs and expanded validation coverage from 8 to 12 patterns |
| `scripts/validate-ai-suite.py` | Added dynamic report dates plus richer response checks for required terms and normative/prescriptive language |
| `scripts/export-ai-context.py` + `scripts/repo_utils.py` | Added stable chunk IDs, content-kind/family metadata, source URLs, tags, and explicit freshness fields to exported chunks |
| `scripts/sync-release-metadata.py` + `scripts/refresh-repo.py` | Added release/count sync and a single local refresh path for freshness, export, and AI validation artifacts |

---

## Phase Completion Status

| Phase | Description | Status | Completion |
|-------|-------------|--------|------------|
| 1 | Root files + `meta/` | **Complete for current planned scope** — schemas, freshness metadata, and meta tooling are aligned with current repo usage | 2026-03-14 |
| 2 | Standards (`/standards/`) | **Complete for current planned scope** — WCAG core, techniques, understanding, ARIA, Section 508, PDF/UA, EPUB, EN 301 549, ATAG, UAAG, and ISO 9241-171 overview are now present | 2026-03-14 |
| 3 | Web domains (`/domains/web/`) | **Complete for v1** — core web guides, component patterns, testing, screen reader support files, mobile patterns, and PWA guidance created | 2026-03-14 |
| 4 | Document domains (`/domains/documents/`) | **Complete for current planned scope** — broad guides plus split workflow/checklist files for Word, PowerPoint, PDF, Excel, and readability created | 2026-03-14 |
| 5 | Social media (`/domains/social-media/`) | **Complete for current planned scope** — platform guides, alt text, captions, inclusive writing, image-type alt text, WebVTT, and emoji guidance created | 2026-03-14 |
| 6 | Cognitive, color, media, screen readers | **Complete for current planned scope** — core guidance, matrices, workflow guides, and vendor provenance now exist | 2026-03-21 |
| 7 | AI prompts + legal compliance | **Complete for current planned scope** — prompt coverage now maps to all documented AI usage patterns and legal freshness fields are consistent | 2026-03-14 |
| 8 | Validation and gap filling | **Complete for current planned scope** — validation harness now covers 12 patterns with richer behavioral checks and a current generated report | 2026-03-21 |
| 9 | Voice + physical ICT (`/domains/voice/`, `/domains/physical-ict/`) | **Complete for current planned scope** — voice UI guide and kiosk/embedded systems playbook created | 2026-03-14 |
| 10 | AI ingestion + evaluation tooling | **Complete for current planned scope** — chunk export, schema validation, reference auditing, freshness sync, release metadata sync, and pattern validation scripts created | 2026-03-21 |

---

## AI Validation Results

Latest local validation artifacts:
- `meta/latest-ai-validation-report.md`
- `meta/chunk-manifest.jsonl`
- `meta/chunk-manifest-summary.json`
- `meta/freshness-manifest.json`

Latest result snapshot:
- Structural checks: 2/2 passed (`validate-frontmatter.py`, `validate-references.py`)
- Pattern checks: 12/12 passed against `meta/ai-validation-fixtures.json`

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
| Validation harness now supports richer saved-response checks, but live model scoring still depends on the caller supplying captured responses | Repository-wide | Medium | Documented |
