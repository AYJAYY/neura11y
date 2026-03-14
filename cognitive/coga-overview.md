---
title: "Cognitive Accessibility Overview"
standard: "WCAG 2.2 + COGA"
source_url: "https://www.w3.org/WAI/cognitive/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["cognitive", "coga", "dyslexia", "adhd", "memory", "plain-language"]
ai_context: "Overview of cognitive accessibility requirements and COGA guidance. Load when creating content for broad audiences or addressing cognitive disability requirements."
---

# Cognitive Accessibility Overview

Source: https://www.w3.org/WAI/cognitive/
COGA Design Guide: https://www.w3.org/TR/coga-usable/

---

## What is Cognitive Accessibility?

Cognitive accessibility addresses the needs of people with cognitive disabilities including:
- Memory impairments
- Attention deficit disorders (ADHD)
- Learning disabilities (dyslexia, dyscalculia)
- Autism spectrum
- Mental health conditions that affect concentration
- Acquired cognitive disabilities (TBI, stroke, dementia)
- Age-related cognitive changes

**WHO estimates:** 10-15% of the global population has a cognitive disability of some kind.

---

## WCAG Success Criteria for Cognitive Accessibility

WCAG 2.2 criteria most relevant to cognitive access:

| SC | Title | Level | Benefit |
|----|-------|-------|---------|
| 1.3.5 | Identify Input Purpose | AA | Reduces cognitive load on forms |
| 2.2.1 | Timing Adjustable | A | Users need more time |
| 2.2.6 | Timeouts | AAA | Warning about session expiry |
| 2.4.6 | Headings and Labels | AA | Clear structure aids comprehension |
| 3.1.5 | Reading Level | AAA | Supplemental simple version |
| 3.2.1 | On Focus | A | Predictability |
| 3.2.2 | On Input | A | Predictability |
| 3.2.3 | Consistent Navigation | AA | Predictability |
| 3.2.6 | Consistent Help | A | (New in 2.2) |
| 3.3.1 | Error Identification | A | Error recovery |
| 3.3.4 | Error Prevention | AA | Confirmation before irreversible |
| 3.3.7 | Redundant Entry | A | (New in 2.2) |
| 3.3.8 | Accessible Authentication | AA | (New in 2.2) No cognitive tests |

---

## COGA Design Patterns (W3C Task Force)

The Cognitive and Learning Disabilities Accessibility Task Force (COGA) has identified 8 design objectives:

### Objective 1: Help Users Understand What Things Are and How to Use Them

- Use familiar names, roles, and states for interactive elements
- Use common icons with text labels (not icon-only)
- Use standard UI patterns (hamburger menu, breadcrumb, etc.)
- Avoid custom UI that doesn't follow common patterns

### Objective 2: Help Users Find What They Need

- Clear, consistent navigation structure
- Search functionality available at all times
- Site map available
- Clear page titles and headings

### Objective 3: Use Clear and Understandable Content and Text

- Plain language: short sentences, common words, active voice
- Define technical terms and acronyms
- Target Grade 8 reading level for general audiences
- Supplement complex text with illustrations or summaries
- Use consistent terminology throughout

### Objective 4: Prevent Users from Making Mistakes

- Instructions before inputs, not after
- Format hints inline with labels
- Confirmation dialogs for irreversible actions
- Auto-save/draft feature where possible
- Avoid form fields that clear on error

### Objective 5: Help Users Recover from Mistakes

- Clear error messages that describe what went wrong and how to fix it
- Error messages stay visible until corrected
- "Are you sure?" dialogs for permanent actions
- Allow undo where possible

### Objective 6: Ensure Processes Do Not Rely on Memory

- Don't require users to remember information between steps
- Auto-populate previously entered information (SC 3.3.7)
- Don't require remembering complex passwords (SC 3.3.8)
- Visual breadcrumb trail for multi-step processes
- Visible cart/progress summary throughout checkout

### Objective 7: Provide Help and Support

- Context-sensitive help available
- Clear customer support contact (SC 3.2.6)
- Tooltips on complex fields (with keyboard dismissal per SC 1.4.13)
- Video tutorials as alternative to text instructions

### Objective 8: Support Adaptation and Personalization

- Support browser zoom without content loss (SC 1.4.4)
- Don't override user agent text spacing settings (SC 1.4.12)
- Allow user to control motion and animation
- Respect prefers-reduced-motion

---

## Dyslexia Considerations

Dyslexia affects approximately 10-17% of the population. Key design factors:

### Typography

- Use san-serif fonts (Arial, Helvetica, Verdana, Open Sans) — easier for many people with dyslexia
- Avoid justified text — uneven spacing causes "rivers" that are distracting
- Use left-aligned text
- Line height: 1.5-2x (SC 1.4.12 minimum is 1.5x)
- Letter spacing: 0.12em+ (SC 1.4.12 minimum)
- Word spacing: 0.16em+ (SC 1.4.12 minimum)
- Paragraph spacing: 2x line height (SC 1.4.12 minimum)
- Avoid thin or very light font weights for body text

### Layout

- Short line length: 60-70 characters per line
- Generous margins
- High contrast between text and background (SC 1.4.3)
- Avoid busy/patterned backgrounds behind text

### Content

- Short sentences and paragraphs
- Use bullet points for lists
- Use headings frequently
- Avoid double negatives
- Use concrete, specific language

---

## ADHD Considerations

Attention Deficit Hyperactivity Disorder (ADHD) affects approximately 5% of adults.

### Focus and Attention

- Minimize distractions: avoid auto-playing media, scrolling banners, blinking elements
- Clear visual hierarchy directs attention
- Progressive disclosure: show content in manageable chunks
- Avoid time-limited content without user control (SC 2.2.1)

### Working Memory

- Summary boxes for key points
- Repeat key information in different formats
- Progress indicators for multi-step processes
- Clear feedback on actions taken

### Impulsivity

- Confirmation for irreversible actions (SC 3.3.4)
- Easy undo/cancel for forms
- Auto-save drafts

---

## Plain Language for Cognitive Accessibility

Plain language serves everyone, especially people with cognitive disabilities. Key rules:

### Words

- Use common, everyday words
- One idea per sentence
- Avoid jargon (or explain it immediately)
- Spell out acronyms on first use
- Use the same term consistently (don't alternate synonyms)

### Sentences

- Active voice: "We will send you a confirmation" not "A confirmation will be sent"
- Short: 15-20 words maximum
- One main idea per sentence
- Avoid multiple clauses

### Paragraphs

- 3-5 sentences maximum
- One topic per paragraph
- Lead with the most important information (inverted pyramid)

### Structure

- Clear headings describe what follows
- Bulleted/numbered lists for multiple items
- Summary/key points box at start
- Table of contents for long documents

### Reading Level Testing

Tools:
- Hemingway App (https://hemingwayapp.com)
- Flesch-Kincaid Grade Level (built into Word/Google Docs)
- Readable.io
- WebFX Readability Test Tool

Target scores:
- General public: Grade 6-8 (Flesch Reading Ease 60+)
- Technical professionals: Grade 10-12
- Legal/regulatory: Grade 12-14 (necessary complexity; add plain summary)

---

## Cognitive Accessibility and AI Content Generation

When generating content for broad or inclusive audiences:

1. **Default to plain language** — Grade 8 level unless specified otherwise
2. **Use active voice** — More direct and clearer
3. **Short sentences** — Break complex ideas into multiple sentences
4. **Avoid idioms** — They don't translate across cultures or to people with cognitive disabilities
5. **Concrete examples** — Abstract concepts need illustration
6. **Consistent terminology** — Don't switch between synonyms
7. **Define technical terms** — Always on first use
8. **Structured output** — Use headings, bullets, numbered lists
