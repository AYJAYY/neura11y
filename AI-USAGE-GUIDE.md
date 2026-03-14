---
title: "AI Usage Guide"
type: "meta"
status: "curated"
last_updated: "2026-03-14"
tags: ["ai", "context-loading", "rag", "prompting"]
ai_context: "Read this file first. It defines how to use this repository in AI context windows and RAG pipelines."
---

# AI Usage Guide

This file tells AI systems and their operators how to use this repository effectively. It defines context-loading patterns, RAG configuration, file format standards, and quality checks.

---

## Repository Design Principles

1. **AI Ingestion First** — Files are flat, factual Markdown with YAML frontmatter. No narrative prose, no decorative language.
2. **Standards Traceability** — Every requirement cites its normative source: URL, version, and section number.
3. **Normative vs. Prescriptive Separation** — `/standards/` contains what the spec says. `/domains/` contains how to apply it.
4. **Chunk-Friendly Structure** — All content sections begin with `##` headings followed by structured data. This is the optimal RAG chunk boundary.

---

## File Frontmatter Format

This repository uses **path-specific frontmatter schemas** rather than a single universal schema.

### Content Files

Use for files under `/standards/`, `/domains/`, `/media/`, `/color-and-visual/`, `/cognitive/`, `/screen-readers/`, `/reference/`, and `/ai-prompts/`.

```yaml
---
title: ""            # Descriptive title of the file
standard: ""         # Primary standard or framework
source_url: ""       # Canonical source URL when applicable
domain: []           # Domain tags such as "web", "documents", "social-media", "mobile"
last_fetched: ""     # ISO 8601 date of content update
status: ""           # "normative" | "prescriptive" | "curated" | "template"
tags: []             # Searchable tags
ai_context: ""       # One-line hint for AI: what this file is for
---
```

### Manually Verified Content

Add these fields when manual review matters more than fetch date:

```yaml
last_verified: ""    # Platform-specific or UI-specific manual verification
last_reviewed: ""    # Legal or editorial review date
stale: false         # Optional; set true when the file exceeds freshness thresholds
```

### Root and Meta Files

Use for `README.md`, `INDEX.md`, `GLOSSARY.md`, `AI-USAGE-GUIDE.md`, and `/meta/`.

```yaml
---
title: ""
type: ""             # "root" | "index" | "reference" | "meta"
status: "curated"
last_updated: ""     # ISO 8601 date of metadata update
tags: []             # Optional
ai_context: ""
---
```

**Status values:**
- `normative` — Directly reflects a W3C or regulatory standard; auto-fetchable
- `prescriptive` — Best-practice guidance derived from standards; curated
- `curated` — Editorial synthesis; requires manual maintenance
- `template` — Prompt template for AI use

---

## Context-Loading Patterns

### Pattern 1: Web Accessibility Audit

Load in this order:
```
standards/wcag/wcag-2.2-quick-ref.md
standards/aria/wai-aria-1.2-roles.md
standards/aria/aria-common-mistakes.md
domains/web/web-accessibility-checklist.md
domains/web/html-semantics-guide.md
```

For component-specific audits, add:
```
domains/web/component-patterns/[component-name].md
```

For mobile web or installable-app scope, also add:
```
domains/web/mobile-accessibility-patterns.md
domains/web/pwa-accessibility.md
```

### Pattern 2: Accessible Web Component Generation

```
standards/wcag/wcag-2.2-quick-ref.md
standards/aria/wai-aria-1.2-roles.md
standards/aria/wai-aria-1.2-states-properties.md
standards/aria/aria-authoring-practices.md
domains/web/component-patterns/[component-name].md
domains/web/keyboard-navigation-patterns.md
domains/web/focus-management.md
```

### Pattern 3: Social Media Post Creation

```
domains/social-media/social-media-overview.md
domains/social-media/alt-text/alt-text-principles.md
domains/social-media/writing-for-accessibility/inclusive-language.md
```

Then choose one platform guide from this list:
```
domains/social-media/platforms/facebook/facebook-guide.md
domains/social-media/platforms/instagram/instagram-guide.md
domains/social-media/platforms/linkedin/linkedin-guide.md
domains/social-media/platforms/mastodon/mastodon-guide.md
domains/social-media/platforms/tiktok/tiktok-guide.md
domains/social-media/platforms/twitter-x/twitter-guide.md
domains/social-media/platforms/youtube/youtube-guide.md
```

Add these when the task is more specific than general post creation:
```
domains/social-media/alt-text/alt-text-by-image-type.md
domains/social-media/captions-and-transcripts/webvtt-format.md
domains/social-media/captions-and-transcripts/sign-language-video-guide.md
domains/social-media/captions-and-transcripts/subtitles-vs-captions-by-region.md
domains/social-media/writing-for-accessibility/emoji-guide.md
```

### Pattern 4: Document Accessibility (PDF/Word/PowerPoint)

```
standards/pdf-ua/pdf-ua-overview.md
standards/epub/epub-accessibility-1.1.md   (for ebooks)
domains/documents/word-accessibility/word-guide.md
domains/documents/word-accessibility/word-checklist.md
domains/documents/word-accessibility/word-styles-guide.md
domains/documents/powerpoint-accessibility/powerpoint-guide.md
domains/documents/powerpoint-accessibility/ppt-checklist.md
domains/documents/powerpoint-accessibility/slide-layout-guide.md
domains/documents/pdf-creation/pdf-accessibility-guide.md
domains/documents/pdf-creation/pdf-form-accessibility-examples.md
domains/documents/pdf-creation/pdf-from-word.md
domains/documents/pdf-creation/pdf-from-indesign.md
domains/documents/pdf-creation/pdf-remediation.md
domains/documents/excel-accessibility/excel-guide.md
domains/documents/excel-accessibility/excel-checklist.md
domains/documents/excel-accessibility/excel-data-visualization-guide.md
domains/documents/plain-language/plain-language-guide.md
domains/documents/plain-language/readability-guide.md
```

Add these when the workflow is authoring-surface specific:
```
domains/documents/email-accessibility/email-and-newsletters-guide.md
domains/documents/google-workspace/google-docs-guide.md
domains/documents/google-workspace/google-slides-guide.md
domains/documents/google-workspace/google-sheets-guide.md
```

### Pattern 5: Legal Compliance Check

```
standards/wcag/wcag-2.2-quick-ref.md
standards/section-508/section-508-overview.md
standards/section-508/section-508-technical-standards.md
legal-and-compliance/us-ada-overview.md
legal-and-compliance/eu-eaa-overview.md
legal-and-compliance/uk-accessibility-regulations.md
legal-and-compliance/canada-accessibility.md
legal-and-compliance/australia-accessibility.md
```

### Pattern 6: Full Web Accessibility Context (maximum coverage)

```
standards/wcag/wcag-2.2-quick-ref.md
standards/wcag/wcag-conformance-levels.md
standards/aria/wai-aria-1.2-roles.md
standards/aria/wai-aria-1.2-states-properties.md
domains/web/web-accessibility-checklist.md
domains/web/html-semantics-guide.md
domains/web/forms-accessibility.md
domains/web/keyboard-navigation-patterns.md
domains/web/focus-management.md
domains/web/color-and-contrast.md
```

Add these for production workflow coverage:
```
domains/web/cms-authoring-workflow.md
domains/web/design-to-development-handoff.md
```

### Pattern 7: Voice UI and Speech Commands

```
standards/wcag/wcag-2.2-quick-ref.md
standards/other-standards/iso-9241-171.md
standards/en-301-549/en-301-549-requirements.md
domains/voice/voice-ui-accessibility.md
```

### Pattern 8: Kiosk and Embedded / Closed Functionality

```
standards/other-standards/iso-9241-171.md
standards/en-301-549/en-301-549-requirements.md
domains/physical-ict/kiosk-and-embedded-playbook.md
```

### Supplemental Context Bundles

These are not part of the core 8 loading patterns above, but they reflect newer repo coverage that is often useful in production workflows.

#### Native Mobile App Accessibility

```
standards/wcag/wcag-2.2-quick-ref.md
domains/mobile/native-mobile-app-accessibility.md
screen-readers/voiceover-guide.md
screen-readers/talkback-guide.md
```

#### CMS and Design Handoff

```
domains/web/cms-authoring-workflow.md
domains/web/design-to-development-handoff.md
domains/web/html-semantics-guide.md
domains/web/forms-accessibility.md
```

#### Email and Newsletter Workflow

```
standards/wcag/wcag-2.2-quick-ref.md
domains/documents/email-accessibility/email-and-newsletters-guide.md
domains/web/color-and-contrast.md
media/images/alt-text-decision-tree.md
```

#### Google Workspace Workflow

```
domains/documents/google-workspace/google-docs-guide.md
domains/documents/google-workspace/google-slides-guide.md
domains/documents/google-workspace/google-sheets-guide.md
domains/documents/plain-language/plain-language-guide.md
```

---

## RAG Pipeline Configuration

### Chunking Strategy

- **Chunk boundary:** `##` heading level (H2)
- **Minimum chunk size:** Do not split below 100 tokens
- **Maximum chunk size:** 512 tokens (recommended), 1024 tokens (maximum)
- **Overlap:** 50 tokens between adjacent chunks from the same file

### Required Chunk Metadata

Preserve these fields as chunk metadata for all ingested files:

| Field | Source | Purpose |
|-------|--------|---------|
| `source_file` | File path relative to repo root | Provenance |
| `heading_path` | Concatenated H1 > H2 path | Navigation |
| `standard` | Frontmatter `standard` field | Filter by standard |
| `sc_number` | Extracted from `## SC X.X.X` headings | Filter by SC |
| `domain` | Frontmatter `domain` field | Filter by domain |
| `platform` | Extracted from the platform directory segment under `/domains/social-media/platforms/` | Filter by platform |
| `status` | Frontmatter `status` field | Filter normative vs. curated |
| `level` | Extracted from `Level A/AA/AAA` text | Filter by conformance level |

### Recommended Embedding Model

Use a model with at least 8,192 token context. Content includes technical terms that benefit from domain-specific embeddings. If using OpenAI embeddings, `text-embedding-3-large` is recommended. For local deployment, `nomic-embed-text` performs well on technical content.

### Query Routing

When the user's query includes:
- SC numbers (e.g., "1.4.3") → Filter chunks by `sc_number`
- Platform names → Filter chunks by `platform`
- Conformance levels → Filter chunks by `level`
- "WCAG" → Prefer `/standards/wcag/` chunks
- "social media" or platform name → Prefer `/domains/social-media/` chunks
- "document" or "PDF" or "Word" → Prefer `/domains/documents/` chunks
- "mobile app" or "iOS" or "Android" → Prefer `/domains/mobile/` chunks
- "email" or "newsletter" → Prefer `/domains/documents/email-accessibility/` chunks
- "Google Docs" or "Google Slides" or "Google Sheets" → Prefer `/domains/documents/google-workspace/` chunks
- "CMS" or "content model" → Prefer `/domains/web/cms-authoring-workflow.md`
- "handoff" or "design system" → Prefer `/domains/web/design-to-development-handoff.md`

---

## Prompt Engineering Guidance

### System Prompt Template

When using this repository for accessibility tasks, include this in the system prompt:

```
You are an accessibility expert with access to a comprehensive knowledge base.
When providing guidance:
1. Cite specific success criteria (e.g., WCAG SC 1.4.3, Level AA)
2. Distinguish normative requirements from prescriptive best practices
3. Note when requirements differ by conformance level (A vs. AA vs. AAA)
4. For platform-specific guidance, note when information may be outdated (UIs change frequently)
5. When uncertain about a requirement, say so rather than hallucinating
```

### Pre-built Templates

See `/ai-prompts/` for ready-to-use prompt templates:
- `ai-prompts/web-content/audit-html-snippet.md` — HTML auditing and remediation
- `ai-prompts/web-content/generate-accessible-component.md` — component generation and review
- `ai-prompts/web-content/full-site-accessibility-review.md` — broader site review and remediation planning
- `ai-prompts/documents/accessible-document.md` — accessible document creation
- `ai-prompts/social-media/accessible-social-post.md` — accessible social post creation
- `ai-prompts/legal-and-compliance/check-accessibility-compliance.md` — issue-to-regulation mapping
- `ai-prompts/voice/accessible-voice-ui.md` — voice UI design and review
- `ai-prompts/physical-ict/accessible-kiosk-and-embedded.md` — kiosk and closed-functionality review

---

## Quality Checks

### Verify AI Output Against These Criteria

1. **SC citations must be correct** — Check that cited SC numbers match actual WCAG criterion numbers and titles.
2. **Thresholds must be exact** — Contrast ratios (4.5:1, 3:1, 7:1), character limits, pixel minimums must be accurate.
3. **Level designations must be correct** — A vs. AA vs. AAA cannot be wrong in compliance contexts.
4. **Platform limits must be current** — Alt text character limits and UI flows change frequently; flag outputs for verification.
5. **Normative vs. advisory** — AI must not present advisory techniques as required.

### Verification Prompts

After loading context, test with:

```
Audit this HTML snippet and list all WCAG Level AA violations with specific SC numbers:
<a href="/pricing" aria-label="View pricing plans">Click here</a>
```

Expected output should cite:
- SC 2.4.4 (Link Purpose (In Context)) — visible text is non-descriptive
- SC 2.5.3 (Label in Name) — accessible name does not include the visible label text

Expected output should **not** cite:
- SC 4.1.2 (Name, Role, Value) — the link already has a programmatic name and role

---

## Content Freshness

| Content Type | Location | Freshness Signal |
|---|---|---|
| WCAG 2.1/2.2 | `/standards/wcag/` | `last_fetched` frontmatter |
| ARIA 1.2 | `/standards/aria/` | `last_fetched` frontmatter |
| Platform guides | `/domains/social-media/platforms/` | `last_verified` frontmatter |
| Legal compliance | `/legal-and-compliance/` | `last_reviewed` frontmatter |

If `last_fetched` or `last_verified` is more than 6 months old for platform guides, treat content as potentially outdated and recommend manual verification.

If `stale: true` is present, surface that caveat explicitly in the AI output.

---

## Automation Scripts

Use these scripts to keep AI ingestion and validation assets current:

- `scripts/export-ai-context.py` — export chunked JSONL plus a summary manifest for RAG ingestion
- `scripts/validate-frontmatter.py` — enforce path-specific frontmatter schemas
- `scripts/validate-references.py` — detect broken internal file references
- `scripts/validate-ai-suite.py` — run the fixture-based validation harness using `meta/ai-validation-fixtures.json`; add `--responses-dir` to validate saved model responses
- `scripts/sync-freshness.py` — build a freshness manifest and sync registry freshness columns

### Generated Artifacts

These files are produced or refreshed by the automation scripts and can be treated as operational outputs rather than hand-authored guidance:

- `meta/chunk-manifest.jsonl` — canonical exported chunk corpus for ingestion
- `meta/chunk-manifest-summary.json` — chunk counts and export settings
- `meta/freshness-manifest.json` — per-file freshness metadata for tooling
- `meta/latest-ai-validation-report.md` — latest structural and fixture-validation report
- `meta/fetch-log.jsonl` — structured fetch history

### Recommended Refresh Sequence

For a full repo refresh or release pass, run:

1. `scripts/fetch-all.py`
2. `scripts/export-ai-context.py`
3. `scripts/sync-freshness.py`
4. `scripts/validate-ai-suite.py`

```bash
python3 scripts/fetch-all.py
python3 scripts/export-ai-context.py
python3 scripts/sync-freshness.py
python3 scripts/validate-ai-suite.py
```

---

## File Naming Conventions

- Lowercase letters only
- Hyphens as word separators (no underscores, no spaces)
- Include version number when relevant (e.g., `wcag-2.2-quick-ref.md`)
- Include platform name in platform files (e.g., `instagram-guide.md`)
- Maximum 2,000 lines per file; split at `##` boundaries if exceeded

---

## Repository Layers

| Layer | Location | When to Use |
|-------|----------|-------------|
| 1 — Standards | `/standards/` | Need exact SC numbers, thresholds, or normative text |
| 2 — Domain Guides | `/domains/` | Need applied guidance for a specific content type |
| 3 — Prompt Templates | `/ai-prompts/` | Need ready-to-use prompts for common tasks |

For most tasks, load Layer 2 (domain guide) + the relevant Layer 1 (standard) for the success criteria being applied. Layer 3 templates pre-wire both layers for common use cases.
