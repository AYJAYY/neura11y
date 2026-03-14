---
title: "AI Prompt Templates — Document Accessibility"
standard: "WCAG 2.2 + PDF/UA + Section 508"
source_url: ""
domain: ["documents"]
last_fetched: "2026-03-13"
status: "template"
tags: ["ai-prompts", "documents", "word", "pdf", "powerpoint", "templates"]
ai_context: "Ready-to-use prompt templates for document accessibility tasks. Load when generating accessible document content or reviewing document accessibility."
---

# AI Prompt Templates — Document Accessibility

---

## Template 1: Word Document Accessibility Review

**Context files to load:**
- `domains/documents/word-accessibility/word-guide.md`
- `standards/wcag/wcag-2.2-quick-ref.md` (for content requirements)

**Prompt:**

```
Review the following document description for accessibility issues and provide specific remediation steps.

Document description:
[Describe the document or paste the text content]

Check for:
1. Heading structure (logical hierarchy H1→H2→H3, no skipped levels)
2. List formatting (using built-in lists, not manual hyphens)
3. Images (alt text or decorative marking)
4. Links (descriptive text, no "click here")
5. Tables (header row, no complex nested/merged cells)
6. Color usage (not color-only for information)
7. Language and reading level
8. Document properties (title, language)

For each issue found, provide:
- [FAIL] or [WARN] classification
- The specific problem
- The exact fix required
- The relevant standard or best practice
```

---

## Template 2: Generate Accessible Document Structure

**Context files to load:**
- `domains/documents/word-accessibility/word-guide.md`
- `cognitive/coga-overview.md` (for plain language)

**Prompt:**

```
Generate an accessible document structure for the following content.

Topic: [topic]
Audience: [intended audience]
Purpose: [what the document should accomplish]
Length: [estimated length]

Requirements:
- Logical heading hierarchy (one H1, appropriate H2/H3 sections)
- Use of numbered or bulleted lists for multi-item content
- Plain language (Grade 8 level for general audience)
- Short sentences (max 15-20 words)
- Active voice
- CamelCase hashtags if any social media tags needed

Return:
- Full document outline with heading hierarchy
- Guidance notes on where to use lists vs. paragraphs
- Alt text templates for anticipated image types
```

---

## Template 3: Alt Text for Document Images

**Context files to load:**
- `media/images/alt-text-decision-tree.md`

**Prompt:**

```
Write alt text for the following image in a Microsoft Word or PowerPoint document.

Image description: [describe what the image shows]
Document context: [what section is this image in? what point does it support?]
Image type: [photograph / chart / diagram / screenshot / logo / decorative]

Rules:
- Do not begin with "Image of" or "Photo of"
- Include text visible in the image verbatim
- For charts/graphs: state the key finding, not just what the chart looks like
- For decorative images: respond with "Mark as decorative (empty alt)"
- Keep under 250 characters for simple images
- For complex diagrams: provide both a short alt (under 125 chars) AND a long description

Return:
- Alt text (formatted for direct copy-paste into Word/PowerPoint)
- For complex images: long description text
```

---

## Template 4: PDF Remediation Assessment

**Context files to load:**
- `domains/documents/pdf-creation/pdf-accessibility-guide.md`
- `standards/pdf-ua/pdf-ua-overview.md`

**Prompt:**

```
Assess the accessibility of the following PDF and provide a remediation plan.

PDF description:
- Source: [Word export / scanned / designed in InDesign / unknown]
- Content type: [report / form / brochure / manual / other]
- Number of pages: [approximate]
- Contains: [check all that apply] images / tables / forms / charts / figures

Remediation scope: [full remediation / minimum compliance / quick review]

Provide:
1. List of likely accessibility issues given the description above
2. Priority order for remediation (most critical first)
3. Tools needed (Adobe Acrobat Pro, PAC 3, etc.)
4. Estimated effort level (Low / Medium / High) for each fix
5. PDF/UA requirements applicable to this document type
```

---

## Template 5: PowerPoint Accessible Slide Content

**Context files to load:**
- `domains/documents/powerpoint-accessibility/powerpoint-guide.md`
- `media/images/alt-text-decision-tree.md`

**Prompt:**

```
Generate accessible content for a PowerPoint slide.

Slide purpose: [what this slide needs to communicate]
Slide content: [bullet points, data, or descriptive content to include]
Visual elements: [describe any charts, images, or diagrams]
Audience: [presentation audience]

Requirements:
- Unique, descriptive slide title
- Maximum 5-6 bullet points per slide
- Each bullet: one idea, maximum 10-12 words
- Reading order: title → content → any supplemental elements
- Alt text for any described visual elements
- Font size: minimum 24pt for body, 36pt+ for titles

Return:
- Slide title
- Bullet points (formatted for direct use)
- Alt text for each visual element
- Notes field text (longer explanation for speaker/transcript)
```

---

## Template 6: Accessible Table Design

**Context files to load:**
- `domains/web/component-patterns/data-table.md`
- `domains/documents/word-accessibility/word-guide.md`

**Prompt:**

```
Design an accessible table for the following data.

Data to present:
[Describe or paste the data]

Table context: [report / web page / presentation / spreadsheet]

Requirements:
- Simple structure preferred (no merged/nested cells)
- Clear column and/or row headers
- Descriptive table caption or title
- For web: provide HTML with proper <th scope="col|row"> attributes
- For documents: describe the header row configuration and alt text

Return:
- Table structure recommendation
- For web: complete HTML table code
- For documents: step-by-step setup instructions
- Caption/title text
- Alt text if the table is an image
```

---

## Template 7: Plain Language Rewrite

**Context files to load:**
- `cognitive/coga-overview.md`

**Prompt:**

```
Rewrite the following text in plain language for accessibility.

Original text:
[paste text to rewrite]

Target audience: [general public / technical professional / legal / other]
Target reading level: [Grade 6-8 for general public / Grade 10-12 for professionals]

Apply these rules:
1. Sentences: maximum 15-20 words each
2. Voice: active (not passive)
3. Words: common everyday words; define jargon on first use
4. Structure: one idea per paragraph; use bullet points for lists
5. Headings: descriptive headings for sections longer than 2 paragraphs
6. Acronyms: spell out on first use: "Web Content Accessibility Guidelines (WCAG)"

Return:
- Rewritten text
- Brief explanation of changes made
- Flesch-Kincaid grade level estimate
```
