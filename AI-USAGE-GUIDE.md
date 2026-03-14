---
title: "AI Usage Guide"
type: "meta"
status: "curated"
last_updated: "2026-03-13"
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

Every file in this repository uses this YAML frontmatter schema:

```yaml
---
title: ""            # Descriptive title of the file
standard: ""         # Primary standard (e.g., "WCAG 2.2", "WAI-ARIA 1.2")
source_url: ""       # Canonical URL of the normative source
domain: []           # Array: "web", "documents", "social-media", "general"
last_fetched: ""     # ISO 8601 date of last content update (YYYY-MM-DD)
status: ""           # "normative" | "prescriptive" | "curated" | "template"
tags: []             # Searchable tags
ai_context: ""       # One-line hint for AI: what this file is for
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
domains/social-media/alt-text/alt-text-principles.md
domains/social-media/platforms/[platform]/[platform]-guide.md
domains/social-media/writing-for-accessibility/inclusive-language.md
```

### Pattern 4: Document Accessibility (PDF/Word/PowerPoint)

```
standards/pdf-ua/pdf-ua-overview.md        (for PDF)
standards/epub/epub-accessibility-1.1.md   (for ebooks)
domains/documents/[format]-accessibility/[format]-checklist.md
domains/documents/plain-language/plain-language-guide.md
```

### Pattern 5: Legal Compliance Check

```
standards/wcag/wcag-2.2-quick-ref.md
standards/section-508/section-508-overview.md
legal-and-compliance/[jurisdiction]-compliance.md
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
| `platform` | Extracted from `platforms/[platform]/` path | Filter by platform |
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

---

## Prompt Engineering Guidance

### System Prompt Template

When using this repository for accessibility tasks, include this in the system prompt:

```
You are an accessibility expert with access to a comprehensive knowledge base.
When providing guidance:
1. Cite specific success criteria (e.g., WCAG 2.2 SC 1.4.3, Level AA)
2. Distinguish normative requirements from prescriptive best practices
3. Note when requirements differ by conformance level (A vs. AA vs. AAA)
4. For platform-specific guidance, note when information may be outdated (UIs change frequently)
5. When uncertain about a requirement, say so rather than hallucinating
```

### Pre-built Templates

See `/ai-prompts/` for ready-to-use prompt templates covering:
- `ai-prompts/web-content/` — HTML generation, ARIA patterns, component auditing
- `ai-prompts/documents/` — Word, PDF, PowerPoint creation
- `ai-prompts/social-media/` — Platform-specific accessible content creation

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
Audit this HTML snippet and list all WCAG 2.2 Level AA violations with specific SC numbers:
<button onclick="submitForm()">Click here</button>
```

Expected output should cite:
- SC 2.4.6 (Headings and Labels) — if applicable
- SC 4.1.2 (Name, Role, Value) — if the button lacks accessible name
- SC 2.5.3 (Label in Name) — if visible text differs from accessible name

---

## Content Freshness

| Content Type | Location | Freshness Signal |
|---|---|---|
| WCAG 2.1/2.2 | `/standards/wcag/` | `last_fetched` frontmatter |
| ARIA 1.2 | `/standards/aria/` | `last_fetched` frontmatter |
| Platform guides | `/domains/social-media/platforms/` | `last_verified` frontmatter |
| Legal compliance | `/legal-and-compliance/` | `last_reviewed` frontmatter |

If `last_fetched` or `last_verified` is more than 6 months old for platform guides, treat content as potentially outdated and recommend manual verification.

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
