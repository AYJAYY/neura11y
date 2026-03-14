---
title: "WCAG 2.2 Advisory Techniques"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/understanding-techniques"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["wcag", "wcag-2.2", "techniques", "advisory-techniques", "best-practice"]
ai_context: "Curated advisory techniques and beyond-minimum accessibility practices. Load when the task asks for best practice, enhanced usability, or AAA-oriented guidance beyond strict conformance."
---

# WCAG 2.2 Advisory Techniques

Advisory techniques are **informative** and go beyond the minimum needed for many WCAG success criteria. They are useful when the goal is strong usability, resilience, or broader disability support, not just a pass/fail conformance check.

---

## How to Interpret Advisory Techniques

- They can improve accessibility without being mandatory for conformance.
- The same implementation pattern can be sufficient in one context and advisory in another.
- Do not present advisory techniques as if the specification requires them by name.

---

## High-Value Advisory Patterns

| Pattern | Why It Matters | Example Techniques or Patterns |
|---------|----------------|-------------------------------|
| Stronger-than-minimum focus styles | Helps low-vision and keyboard users find focus faster | Full-outline focus, stronger contrast, inset + outset focus rings |
| Motion reduction support | Reduces vestibular and distraction issues | `SCR40`, `prefers-reduced-motion`, pause controls |
| Larger targets than the minimum | Reduces motor precision demands | 44px+ controls, generous spacing, forgiving hit areas |
| Redundant cues beyond color | Helps users with color vision differences and cognitive load | icons + text + color, chart patterns, explicit labels |
| Extra orientation and zoom resilience | Helps mobile, low-vision, and magnification users | no orientation lock, robust 400% zoom behavior |
| Supplemental help and recovery guidance | Helps cognitive and new users complete tasks | inline hints, examples, confirmation screens, retry guidance |
| Plain-language labeling and error copy | Helps comprehension and task completion | user-facing language instead of internal or legal jargon |
| Longer descriptions for complex visuals | Helps users understand charts, infographics, and diagrams | summaries, data tables, text equivalents, speaker notes |

---

## Common Advisory Technique Areas by Topic

### Content Clarity

- Use simpler wording even when a technical term is allowed.
- Add examples for complex instructions.
- Prefer descriptive headings over short labels.

### Forms and Error Recovery

- Explain expected input format before submission.
- Provide recovery suggestions, not just error states.
- Preserve entered data after validation failures.

### Motion and Interaction

- Respect reduced-motion settings.
- Avoid auto-rotating content for critical information.
- Provide non-drag alternatives even where dragging is technically allowed.

### Visual Design

- Exceed minimum contrast where practical.
- Keep visible focus obvious against all adjacent colors.
- Avoid dense or cramped layouts that only barely meet reflow.

### Media

- Add transcripts even where only captions are required.
- Integrate visual narration into the main soundtrack for social video.
- Provide longer summaries for charts, demos, and complex screen recordings.

---

## When to Cite Advisory Techniques

Use advisory techniques when the user asks for:

- best practices
- enhanced accessibility
- usability improvements beyond minimum compliance
- AAA-oriented improvements
- resilience across screen readers, zoom, and mobile contexts

For strict compliance questions, cite the WCAG success criterion first and then note the advisory technique as an optional enhancement.
