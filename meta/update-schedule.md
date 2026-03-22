---
title: "Update Schedule"
type: "meta"
status: "curated"
last_updated: "2026-03-21"
ai_context: "Maintenance cadence for all repository content. Use to determine when content may be stale."
---

# Update Schedule

Maintenance cadence for all repository content. Distinguishes auto-fetchable from manually maintained content.

---

## Auto-Fetchable Content

| Content | Trigger | Frequency | Script | Owner |
|---------|---------|-----------|--------|-------|
| WCAG 2.1 full spec | W3C publication | On new W3C errata publication | `fetch-wcag.py` | Auto |
| WCAG 2.2 full spec | W3C publication | On new W3C errata publication | `fetch-wcag.py` | Auto |
| WCAG 3.0 | W3C Working Draft update | Every 6 months | `fetch-wcag.py` | Auto |
| WCAG quick refs | W3C update | On WCAG publication | `fetch-wcag.py` | Auto |
| WCAG techniques | Living document | Quarterly | `fetch-wcag.py` | Auto |
| WCAG understanding docs | Living document | Quarterly | `fetch-wcag.py` | Auto |
| WAI-ARIA 1.2 | W3C publication | On new W3C publication | `fetch-aria.py` | Auto |
| AccName 1.2 | W3C Working Draft update | Every 6 months | `fetch-aria.py` | Auto |
| Core-AAM 1.2 | W3C Candidate Recommendation update | Every 6 months | `fetch-aria.py` | Auto |
| HTML-AAM 1.0 | W3C Working Draft update | Every 6 months | `fetch-aria.py` | Auto |
| ARIA APG patterns | Living document | Monthly | `fetch-aria.py` | Auto |
| ARIA in HTML | W3C publication | On new W3C publication | `fetch-aria.py` | Auto |
| ATAG 2.0 | Stable spec | Annually | `fetch-w3c-other.py` | Auto |
| UAAG 2.0 | Stable spec | Annually | `fetch-w3c-other.py` | Auto |
| EPUB Accessibility 1.1 | W3C publication | On new W3C publication | `fetch-w3c-other.py` | Auto |
| WebVTT | Stable spec | Annually | `fetch-w3c-other.py` | Auto |
| COGA design guide | W3C update | Every 6 months | `fetch-w3c-other.py` | Auto |
| WCAG2ICT 2.2 | W3C Group Note update | Every 6 months | `fetch-w3c-other.py` | Auto |
| Alt text decision tree | W3C update | Quarterly | `fetch-w3c-other.py` | Auto |
| WAI tutorials | W3C tutorial updates | Quarterly | `fetch-w3c-other.py` | Auto |
| NVDA user guide | NVDA documentation update | Quarterly | `fetch-screen-readers.py` | Auto |
| VoiceOver for Mac user guide | Apple support update | Quarterly | `fetch-screen-readers.py` | Auto |
| TalkBack guide | Google support update | Quarterly | `fetch-screen-readers.py` | Auto |
| JAWS keystrokes guide | Freedom Scientific support update | Quarterly | `fetch-screen-readers.py` | Auto |
| Section 508 technical | Stable (2017) | On federal update | `fetch-us-gov.py` | Auto |
| Plain Language guidelines | Living document | Quarterly | `fetch-us-gov.py` | Auto |
| EN 301 549 | ETSI publication | On new ETSI publication | `fetch-en-301-549.py` | Auto |
| PDF/UA summary | PDF Association | Annually | `fetch-iso.py` | Auto |
| Matterhorn Protocol | PDF Association | On new version | `fetch-iso.py` | Auto |

---

## Manually Maintained Content

| Content | Frequency | Trigger | Notes |
|---------|-----------|---------|-------|
| Twitter/X guide | Monthly | Platform UI changes | Alt text UI and character limits change frequently |
| LinkedIn guide | Monthly | Platform UI changes | Native alt text UI evolves |
| Instagram guide | Monthly | Platform UI changes | Alt text workflow changes with app updates |
| Facebook guide | Monthly | Platform UI changes | Varies by surface (feed, stories, reels) |
| TikTok guide | Monthly | Platform UI changes | Caption tools evolving rapidly |
| YouTube guide | Monthly | Platform/policy changes | Auto-caption quality guidelines change |
| Mastodon guide | Quarterly | Platform/instance changes | Stable but instances vary |
| ARIA common mistakes | Quarterly | Community audit reports | Synthesize from a11ysupport.io and audit findings |
| Alt text examples | Quarterly | Community feedback | Add new before/after examples |
| Screen reader support matrices | Quarterly | SR release notes | JAWS, NVDA, VoiceOver major releases |
| JAWS guide | On JAWS major release | Freedom Scientific release | Curated guide; refresh alongside fetched keystrokes source |
| NVDA guide | On NVDA major release | NV Access release | Curated guide; refresh alongside fetched NVDA user guide |
| VoiceOver guide | On macOS/iOS release | Apple release | Curated guide; refresh alongside fetched VoiceOver support docs |
| TalkBack guide | On Android release | Google release | Curated guide; refresh alongside fetched TalkBack support docs |
| Cross-screen-reader workflow guides | Quarterly | After vendor or browser changes | Refresh `screen-readers/` workflow files when testing guidance changes materially |
| US legal landscape | Quarterly | Court decisions, DOJ guidance | ADA Title III web cases |
| EU EAA compliance | Quarterly | EAA enforcement updates | Post-June 2025 enforcement period |
| UK compliance | Quarterly | UK legislative changes | Post-Brexit |
| Canada compliance | Quarterly | ACA and provincial updates | |
| Australia compliance | Quarterly | DDA and WCAG 2.1 adoption | |
| Component patterns | On APG update | W3C APG living document | Synthesize from APG + real-world testing |
| SPA patterns | Quarterly | Framework release notes | React, Angular, Vue accessibility changes |
| CMS authoring workflow | Quarterly | CMS/editor UX changes | Re-check reusable blocks, link fields, media workflows |
| Design-to-development handoff guide | Quarterly | Design system updates | Update when component states or tokens change |
| Native mobile app guide | On iOS/Android major release | Apple or Google release | Re-check focus, gestures, scaling, and announcement APIs |
| Email/newsletter guide | Quarterly | Major client rendering changes | Review Outlook, Gmail, Apple Mail behavior changes |
| Google Workspace guides | Quarterly | Google Workspace UI/export changes | Re-check Docs, Slides, Sheets workflows |
| Automated testing tools and checker references | Quarterly | Tool release notes | Refresh `domains/web/testing/automated-testing.md`, `reference/accessibility-checkers-and-cli-tools.md`, and `reference/accessibility-tools.md` for axe, WAVE, Lighthouse, Pa11y, linting, and related tooling |
| Prompt templates | After each context-pattern change | Manual | Keep prompt packs aligned with AI-USAGE-GUIDE patterns |
| AI validation fixtures | After each prompt or context change | Manual | Keep fixtures aligned with prompt/context expectations |
| Coverage gaps | After each content update | Manual | Track known gaps for next iteration |

---

## Staleness Thresholds

| Content Type | Stale After | Action When Stale |
|---|---|---|
| Platform social media guides | 60 days | Manual review required; add `stale: true` to frontmatter |
| Legal compliance files | 90 days | Manual review required; add `stale: true` to frontmatter |
| Screen reader support matrices | 90 days | Manual review required |
| WCAG/ARIA (stable specs) | 365 days | Re-run fetch script |
| Living documents (APG, techniques) | 90 days | Re-run fetch script |

AI systems loading files should check `last_fetched`, `last_verified`, or `last_reviewed` against the staleness threshold above and add a caveat to outputs when content may be outdated.

---

## Calendar Reminders (Suggested)

Create calendar reminders for:
- **First Monday of each month** — Review all 7 platform guides for UI changes
- **First Monday of each quarter** — Run `scripts/fetch-all.py` followed by `scripts/refresh-repo.py`; review legal and SR matrices
- **After vendor AT documentation changes** — Run `scripts/fetch-screen-readers.py` and refresh curated screen-reader workflow guides
- **First Monday after major browser/SR release** — Update screen reader support matrices
- **First Monday after major iOS/Android release** — Review native mobile and Google Workspace guidance
- **On W3C publication** — Subscribe to https://www.w3.org/TR/ RSS feed for WCAG and ARIA publications
