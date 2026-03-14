---
title: "ATAG 2.0 — Authoring Tool Accessibility Guidelines Overview"
standard: "ATAG 2.0"
source_url: "https://www.w3.org/TR/ATAG20/"
domain: ["web", "tools"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["atag", "authoring-tools", "cms", "wysiwyg", "standards"]
ai_context: "Overview of ATAG 2.0 requirements for authoring tools like CMSes, rich text editors, and social media platforms. Load when advising on CMS or editor accessibility."
---

# ATAG 2.0 — Authoring Tool Accessibility Guidelines Overview

**Status:** W3C Recommendation, September 2015

---

## What Is ATAG?

ATAG (Authoring Tool Accessibility Guidelines) defines how authoring tools — software that creates, edits, or publishes web content — should be accessible. Authoring tools include:

- CMS platforms (WordPress, Drupal, Contentful)
- WYSIWYG editors (TinyMCE, CKEditor, Quill)
- Code editors (VS Code with web preview)
- Social media publishing tools (Buffer, Hootsuite)
- Email marketing platforms (Mailchimp, Constant Contact)
- Website builders (Wix, Squarespace, Webflow)
- Document editors (Google Docs, Microsoft 365 Online)

---

## ATAG's Two Parts

### Part A: Make the authoring tool UI accessible

The tool itself (menus, buttons, dialog boxes, panels) must be accessible to authors who have disabilities.

This means: the CMS admin interface should meet WCAG 2.0 standards.

### Part B: Support the production of accessible content

The tool must help authors produce accessible output:
- Provide prompts for alt text when images are added
- Generate accessible markup automatically
- Provide accessibility checking built into the authoring workflow
- Repair inaccessible content when possible

---

## Key ATAG Success Criteria

### Part A — Authoring Tool UI

| Guideline | Requirement |
|-----------|------------|
| A.1.1 | Authoring tool user interfaces follow applicable WCAG success criteria |
| A.2.1 | Alternative content for non-text content |
| A.3.2 | Authors can navigate using keyboard |
| A.3.4 | Authors have enough time to complete tasks |
| A.4.2 | Authors can understand the UI and fix problems |

### Part B — Accessible Content Production

| Guideline | Requirement |
|-----------|------------|
| B.1.1 | Automatically generated content is accessible (or prompts author) |
| B.1.2 | Accessibility information is preserved when content is edited |
| B.2.1 | Authors are guided to produce accessible content |
| B.2.3 | Authors are assisted in managing alt text for non-text content |
| B.2.4 | Authors are assisted in making time-based media accessible |
| B.3.1 | The tool provides accessibility checking |
| B.3.2 | Authors are assisted in repairing accessibility problems |
| B.4.1 | Accessible content production features are promoted |

---

## ATAG Conformance Levels

Like WCAG, ATAG has Level A, AA, and AAA success criteria.

- Level A — Minimum
- Level AA — Standard compliance target (recommended for most tools)
- Level AAA — Enhanced

**ATAG AA conformance** requires both Part A and Part B at Level AA.

---

## Practical Implications for CMS and Editor Selection

When selecting a CMS or authoring tool, evaluate:

1. **Alt text prompts** — Does the image upload workflow prompt for alt text?
2. **Built-in accessibility checker** — Does the editor have an accessibility check function?
3. **Generated markup quality** — Does the tool produce semantic HTML (headings, lists, proper links)?
4. **Keyboard accessibility of the editor UI** — Can all editor functions be used without a mouse?
5. **VPAT/ACR** — Has the vendor provided a conformance report for the tool itself?

---

## ATAG and Social Media Tools

Social media publishing platforms (Buffer, Hootsuite, Sprout Social) are authoring tools if they allow creating content that is posted to web platforms.

Under ATAG B.2.3, these tools should assist authors in managing alt text for images being posted. Several platforms have added alt text support in response to ATAG-informed accessibility requirements.

---

## Reference

Full ATAG 2.0 specification: https://www.w3.org/TR/ATAG20/
Understanding ATAG 2.0: https://www.w3.org/TR/UNDERSTANDING-ATAG20/
ATAG at a Glance: https://www.w3.org/WAI/standards-guidelines/atag/glance/
