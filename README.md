---
title: "neura11y — AI-Ready Accessibility Knowledge Repository"
type: "root"
status: "curated"
last_updated: "2026-03-21"
ai_context: "Entry point for neura11y. Read AI-USAGE-GUIDE.md before loading other files into AI context."
---

# neura11y

<p align="center">
  <img src="https://raw.githubusercontent.com/AYJAYY/neura11y/main/logo-bright3.png" alt="neura11y logo" width="84">
</p>

<p align="center">
  <strong>Accessibility knowledge, structured for AI.</strong>
</p>

<p align="center">
  Neura11y<img src="https://img.shields.io/badge/neural-accessibility-purple?style=plastic" alt="Static Badge">
</p>

<p align="center">
  neura11y is a structured accessibility knowledge base for AI context loading, RAG pipelines, and accessibility-aware content generation across web, documents, social media, voice UI, and physical ICT.
</p>

<p align="center">
  <a href="https://neura11y.com">neura11y.com</a>
</p>

<p align="center">
  <code>v0.3.0</code> • standards • workflow guides • prompt packs • validation tooling
</p>

neura11y packages normative standards, applied workflow guidance, prompt templates, and validation tooling into a single repository so AI systems can produce accessibility guidance and accessible outputs with stronger traceability and less hallucination.

## Purpose

neura11y enables AI systems to:

- Generate accessible HTML, content, and documents without hallucinating requirements
- Cite specific WCAG success criteria with correct thresholds and level designations
- Apply platform-specific social media accessibility conventions
- Distinguish normative requirements from prescriptive best practices
- Produce legally defensible guidance grounded in Section 508, WCAG, and the EU EAA

## How to Use This Repository

**Read `AI-USAGE-GUIDE.md` first.** It defines context-loading patterns for different task types.

**Quick navigation:** Use `INDEX.md` to find files by standard, domain, or tag without loading the full repository.

**For AI pipelines:** Chunk at `##` heading level. Preserve `source_file`, `heading_path`, `standard`, `sc_number`, `domain`, `platform`, `status`, `level`, `last_fetched`, `last_verified`, `last_reviewed`, and `stale` as chunk metadata.

**Canonical files:** Prefer the curated and split canonical files referenced by `INDEX.md` and `AI-USAGE-GUIDE.md`. Treat `*-fetched.md` and `*-full-fetched.md` files as raw source captures and provenance, not the default context payload.

## Repository Structure

```
claude-a11y-repo/
├── VERSION                   — Repository release version
├── README.md                 — This file
├── INDEX.md                  — Machine-readable cross-reference map
├── GLOSSARY.md               — Canonical definitions for all key terms
├── AI-USAGE-GUIDE.md         — Context-loading patterns for AI systems
│
├── meta/                     — Repository management metadata
│   ├── standards-registry.md — Master list of all standards with source URLs
│   ├── fetch-log.md          — Record of auto-fetch operations
│   ├── fetch-log.jsonl       — Structured fetch history for tooling
│   ├── ai-validation-fixtures.json — Validation fixtures for AI usage patterns
│   ├── chunk-manifest.jsonl  — Exported AI-ingestion corpus
│   ├── chunk-manifest-summary.json — Chunk-export summary statistics
│   ├── freshness-manifest.json — Per-file freshness signals for tooling
│   ├── latest-ai-validation-report.md — Latest validation run report
│   ├── update-schedule.md    — Maintenance cadence per content type
│   └── coverage-gaps.md      — Known gaps and planned additions
│
├── standards/                — Normative standards content (Layer 1)
│   ├── wcag/                 — WCAG 2.1, 2.2, 3.0
│   ├── aria/                 — WAI-ARIA 1.2, APG, ARIA in HTML
│   ├── section-508/          — US Section 508 technical standards
│   ├── pdf-ua/               — PDF/UA (ISO 14289)
│   ├── epub/                 — EPUB Accessibility 1.1
│   ├── en-301-549/           — European standard EN 301 549
│   └── other-standards/      — ATAG 2.0, UAAG 2.0, ISO 9241-171
│
├── domains/                  — Applied guidance by content domain (Layer 2)
│   ├── web/                  — HTML, ARIA, components, testing
│   ├── documents/            — Word, PowerPoint, PDF, Excel, plain language, email, Google Workspace
│   ├── mobile/               — Native iOS and Android app guidance
│   ├── social-media/         — Alt text, captions, 7 platform guides
│   ├── voice/                — Voice UI and speech-command guidance
│   └── physical-ict/         — Kiosk and embedded system playbooks
│
├── cognitive/                — COGA, cognitive accessibility patterns
├── color-and-visual/         — Contrast ratios, APCA, typography
├── media/                    — Images, video, audio accessibility
├── screen-readers/           — AT guides, support matrices, and fetched vendor source docs
├── ai-prompts/               — Ready-to-use prompt templates (Layer 3)
├── legal-and-compliance/     — ADA, Section 508, EU EAA, UK, Canada, Australia
├── reference/                — Tools, statistics, citations
└── scripts/                  — Fetch, validation, chunk-export, and maintenance scripts
```

## Content Layers

| Layer | Location | Purpose |
|-------|----------|---------|
| 1 — Standards | `/standards/` | Normative requirements, SC numbers, thresholds |
| 2 — Domain Guides | `/domains/` | How standards apply to each content type |
| 3 — Prompt Templates | `/ai-prompts/` | Ready-to-use prompts wiring layers 1 and 2 |

## Standards Covered

- **WCAG 2.1** (W3C Recommendation, June 2018) — 78 success criteria
- **WCAG** (current stable W3C Recommendation: 2.2, October 2023) — 86 active success criteria in the current version (9 new; SC 4.1.1 obsolete)
- **WCAG 3.0** (Working Draft) — Overview and emerging guidance
- **WAI-ARIA 1.2** (W3C Recommendation, June 2023)
- **Accessible Name and Description Computation 1.2** (W3C Working Draft, March 2026)
- **Core Accessibility API Mappings 1.2** (W3C Candidate Recommendation Draft, March 2026)
- **HTML Accessibility API Mappings 1.0** (W3C Working Draft, March 2026)
- **ARIA Authoring Practices Guide (APG)**
- **WCAG2ICT 2.2** (W3C Group Note, December 2025)
- **Section 508** (US, 2017 refresh)
- **PDF/UA** (ISO 14289-1:2014)
- **EPUB Accessibility 1.1** (W3C Recommendation, May 2023)
- **EN 301 549** (European standard, v3.2.1)
- **ATAG 2.0**, **UAAG 2.0**
- **ISO 9241-171** (software accessibility overview)

## Domains Covered

- **Web** — HTML semantics, ARIA, focus management, keyboard navigation, forms, components, SPAs, mobile patterns, PWAs, testing
- **Documents** — Microsoft Word, PowerPoint, PDF, Excel; federal plain language guidelines; PDF form and Excel data-viz examples
- **Document Workflows** — Accessible email/newsletters and Google Docs/Slides/Sheets authoring
- **Mobile** — Native iOS and Android accessibility patterns for labels, focus, gestures, scaling, and announcements
- **Social Media** — Twitter/X, LinkedIn, Instagram, Facebook, TikTok, YouTube, Mastodon; sign-language and terminology notes
- **Voice** — Voice command and spoken UI accessibility patterns
- **Physical ICT** — Kiosk and embedded system accessibility playbook
- **Production Workflows** — CMS authoring workflow and design-to-development handoff guidance

## Current Coverage Notes

- **Release 0.3.0:** Adds fetchable AccName, Core-AAM, HTML-AAM, WCAG2ICT, WAI tutorial, and screen-reader vendor sources; expands screen-reader testing coverage; enriches AI chunk metadata; and adds release/refresh automation around the expanded source model.
- **Tooling references:** The repo now includes an AI-first checker and CLI routing file at `reference/accessibility-checkers-and-cli-tools.md`, alongside the broader tools catalog and automated web testing guide.
- **AI operations:** The repository now includes schema validation, reference auditing, enriched chunk export, freshness sync, release-metadata sync, and fixture-based AI validation scripts under `scripts/`.
- **Prompt coverage:** Prompt packs now exist for all documented AI usage patterns in `AI-USAGE-GUIDE.md`.
- **Remaining backlog:** The primary optional backlog item remains video game accessibility, which is still out of scope for v1.

## Maintenance

Auto-fetchable standards and vendor source docs are refreshed via scripts in `/scripts/`. Use `scripts/fetch-all.py` for managed runs, `scripts/refresh-repo.py` to sync release metadata plus AI artifacts, `scripts/export-ai-context.py` for direct JSONL regeneration, `scripts/sync-freshness.py` to update registry freshness signals, and `scripts/validate-ai-suite.py` for structural plus fixture validation (or response validation with `--responses-dir`). See `meta/update-schedule.md` for cadence.

## Contributing

See `meta/coverage-gaps.md` for known gaps and priority areas. All files must follow the frontmatter format defined in `AI-USAGE-GUIDE.md`.
