---
title: "US ADA Web Accessibility Overview"
standard: "Americans with Disabilities Act"
source_url: "https://www.ada.gov/"
domain: ["web", "general"]
last_fetched: "2026-03-13"
status: "curated"
last_reviewed: "2026-03-13"
tags: ["ada", "us", "legal", "compliance", "title-iii", "doj"]
ai_context: "US ADA web accessibility legal framework. Covers Title II (government), Title III (private businesses), DOJ rules, and litigation trends. Load for US legal compliance questions."
---

# US ADA Web Accessibility Overview

**IMPORTANT:** Legal guidance in this file reflects the state as of 2026-03-13. Consult an attorney for specific legal advice. Legal requirements change through court decisions and regulatory action.

---

## What is the ADA?

The Americans with Disabilities Act (1990) prohibits discrimination based on disability. Three titles are relevant to digital accessibility:

- **Title I** — Employment (not directly related to web content)
- **Title II** — State and local government (public entities)
- **Title III** — Places of public accommodation (private businesses open to the public)

---

## Title II — State and Local Government

### 2024 DOJ Final Rule

The Department of Justice issued a **final rule on April 24, 2024** (effective June 24, 2024) requiring WCAG 2.1 Level AA compliance for state and local government websites and mobile apps.

**Key requirements:**
- All state and local government web content must meet WCAG 2.1 Level AA
- Compliance deadlines based on population served:
  - **Larger entities** (≥50,000 population): April 24, 2026
  - **Smaller entities** (<50,000 population): April 26, 2027
  - Special district governments: April 26, 2027

**Exceptions:**
- Archived web content not being actively used
- Preexisting conventional electronic documents (PDFs posted before the effective date)
- Content posted by third parties without oversight
- Password-protected documents (individual-specific)
- Social media content posted by third parties

**Source:** 28 CFR Part 35; https://www.ada.gov/resources/2024-03-08-web-rule/

### Pre-2024 Title II

Before the 2024 rule, courts applied ADA Title II to government websites based on the broad prohibition against discrimination. The 2024 rule provides clear, enforceable standards.

---

## Title III — Private Businesses

### No Final Rule Yet (as of 2026)

The DOJ has NOT issued a final rule for Title III (private businesses) requiring specific technical standards for websites. However:

### Courts Have Applied Title III to Websites

The majority of federal circuit courts have held that private company websites are "places of public accommodation" under ADA Title III. Key circuit split:

- **11th Circuit (SE US):** Requires a nexus to a physical place (Winn-Dixie, 2021) — websites must be connected to a physical store
- **1st, 2nd, 6th, 7th, 9th, 10th Circuits:** Websites and apps are covered without requiring a physical nexus

### DOJ 2022 Guidance

The DOJ issued guidance in March 2022 stating:
- "The Department believes that the ADA's requirements apply to all the goods, services, privileges, or activities offered by public accommodations, including those offered on the web."
- Suggested WCAG 2.1 as the technical standard

### Litigation Trends

ADA Title III web accessibility lawsuits are among the most common disability discrimination cases:
- **~4,000+ cases filed annually** (estimate for 2024-2025)
- Most target e-commerce websites
- Serial filers and law firms that specialize in ADA web cases
- Most cases settle without reaching trial (~$50,000-$150,000 settlement range)
- Common targets: retail, hospitality, food service, healthcare, financial services
- Common issues: missing alt text, inaccessible forms, keyboard navigation failures

### WCAG as the De Facto Standard

Even without a federal regulation, courts have consistently used WCAG as the measuring stick for Title III compliance:
- WCAG 2.0 Level AA was most commonly referenced 2018-2022
- WCAG 2.1 Level AA is the current standard referenced in most guidance
- Some courts use plaintiff's expert opinion on what is "accessible enough"

---

## Practical Standard for US Compliance

For organizations subject to US law:

| Entity Type | Applicable Law | Required Standard |
|---|---|---|
| State/local government | ADA Title II (2024 Rule) | WCAG 2.1 Level AA |
| Federal agency | Section 508 | WCAG 2.0 Level AA |
| Federal contractor | Section 508 | WCAG 2.0 Level AA |
| Private business | ADA Title III | WCAG 2.1 AA (de facto) |
| Healthcare (HIPAA covered) | ADA + HIPAA | WCAG 2.1 AA |
| Financial services | ADA + CFPB guidance | WCAG 2.1 AA |

**Best practice:** Target WCAG 2.1 Level AA or WCAG 2.2 Level AA for all US organizations.

---

## Other US Federal Laws

### Rehabilitation Act Section 508
- Applies to federal agencies and federal contractors
- 2017 refresh incorporated WCAG 2.0 Level AA
- See `standards/section-508/section-508-overview.md`

### Air Carrier Access Act (ACAA)
- DOT regulations require airline websites to be accessible
- WCAG 2.0 AA required for core booking functionality (since 2015)
- Extended to all public-facing pages

### 21st Century Communications and Video Accessibility Act (CVAA)
- Applies to telecommunications and video providers
- Requires accessible communications services and equipment
- Administered by FCC

### Affordable Care Act Section 1557
- Prohibits discrimination in health programs receiving federal funding
- Courts have applied to patient portals and healthcare websites

---

## Resources

- DOJ ADA website: https://www.ada.gov/
- DOJ 2022 guidance on web accessibility: https://www.ada.gov/resources/web-guidance/
- DOJ 2024 Title II rule: https://www.ada.gov/resources/2024-03-08-web-rule/
- Section508.gov: https://www.section508.gov/
