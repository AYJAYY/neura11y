---
title: "Fetch Log"
type: "meta"
status: "curated"
last_updated: "2026-03-13"
ai_context: "Record of all auto-fetch operations. Use to determine content freshness and diagnose fetch failures."
---

# Fetch Log

Record of all automated content fetch operations. Updated by fetch scripts on each run.

---

## Log Format

Each fetch entry records:
- `date` — ISO 8601 date of fetch
- `script` — Script that performed the fetch
- `target` — Source URL fetched
- `output_file` — Repository file written
- `status` — success | partial | failed
- `notes` — Any errors, truncations, or anomalies

---

## Fetch History

*No fetches performed yet. Run fetch scripts from `/scripts/` to populate.*

---

## How to Run Fetch Scripts

### Prerequisites

```bash
pip install requests beautifulsoup4 markdownify pdfplumber python-frontmatter
```

### Run individual scripts

```bash
# WCAG standards
python scripts/fetch-wcag.py

# WAI-ARIA standards
python scripts/fetch-aria.py

# Other W3C standards (ATAG, UAAG, EPUB, COGA, WebVTT)
python scripts/fetch-w3c-other.py

# US government (Section 508, Plain Language)
python scripts/fetch-us-gov.py

# European standard EN 301 549
python scripts/fetch-en-301-549.py

# ISO summaries (PDF/UA, Matterhorn)
python scripts/fetch-iso.py

# Run all scripts
python scripts/fetch-all.py
```

### Run all scripts

```bash
python scripts/fetch-all.py --log meta/fetch-log.md
```

The `--log` flag writes fetch results back to this file automatically.

---

## Fetch Failures Reference

Common failure patterns and resolutions:

| Failure | Cause | Resolution |
|---------|-------|-----------|
| HTTP 403 | W3C rate limiting | Add delay between requests; use `--delay 2` flag |
| Content truncated | Page JavaScript-rendered | Use `--renderer` flag to enable headless Chrome |
| Encoding errors | Non-UTF-8 content | Script uses `response.encoding = 'utf-8'` by default |
| PDF parse failure | EN 301 549 PDF version change | Update `scripts/fetch-en-301-549.py` page ranges |
| Missing sections | W3C document structure changed | Review BeautifulSoup selectors in fetch script |

---

## Planned Fetch Schedule

See `meta/update-schedule.md` for maintenance cadence.

| Script | Next Scheduled Run |
|--------|-------------------|
| `fetch-wcag.py` | On W3C WCAG publication |
| `fetch-aria.py` | On W3C ARIA publication |
| `fetch-w3c-other.py` | Every 6 months |
| `fetch-us-gov.py` | Quarterly |
| `fetch-en-301-549.py` | On ETSI publication |
| `fetch-iso.py` | Annually |

### fetch-all run — 2026-03-13T23:23:04

| wcag            | fetch-wcag.py             | failed | — |
| aria            | fetch-aria.py             | failed | — |
| w3c-other       | fetch-w3c-other.py        | failed | — |
| us-gov          | fetch-us-gov.py           | failed | — |
| en-301-549      | fetch-en-301-549.py       | failed | — |
| iso             | fetch-iso.py              | failed | — |

### fetch-all run — 2026-03-13T23:24:01

| wcag            | fetch-wcag.py             | success | — |
| aria            | fetch-aria.py             | success | — |
| w3c-other       | fetch-w3c-other.py        | success | — |
| us-gov          | fetch-us-gov.py           | success | — |
| en-301-549      | fetch-en-301-549.py       | failed | — |
| iso             | fetch-iso.py              | success | — |

### fetch-all run — 2026-03-13T23:28:26

| en-301-549      | fetch-en-301-549.py       | success | — |
| iso             | fetch-iso.py              | success | — |
