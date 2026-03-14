---
title: "Microsoft PowerPoint Accessibility Guide"
standard: "WCAG + Section 508"
source_url: "https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25"
domain: ["documents"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["powerpoint", "presentations", "slides", "alt-text", "reading-order", "documents"]
ai_context: "How to create accessible PowerPoint presentations. Covers slide structure, alt text, reading order, and export. Load when advising on PowerPoint accessibility."
---

# Microsoft PowerPoint Accessibility Guide

---

## Slide Titles (Required for Every Slide)

Every slide must have a unique, descriptive title. Titles serve as navigation landmarks for screen reader users and are required by Section 508.

### How to Add a Slide Title

1. Each slide layout includes a Title placeholder — use it
2. If the title is not needed visually: move it off the slide edge or use the Selection Pane to hide it
3. Do NOT simply delete the title placeholder

**To hide a title visually while keeping it for screen readers:**
1. View tab → Selection Pane
2. Find the title placeholder in the list
3. Click the eye icon to hide it from view (it remains accessible)

### Unique Titles

Each slide title must be unique. "Slide 3" or repeated section titles are insufficient.

---

## Slide Layout and Reading Order

PowerPoint reads objects on a slide in the order they appear in the **Selection Pane** (from bottom to top by default).

### Checking Reading Order

1. Home tab → Drawing group → Arrange → Selection Pane
2. The Selection Pane lists all objects on the slide
3. The reading order goes from the bottom of the list to the top

### Fixing Reading Order

In the Selection Pane:
- Drag items to reorder them
- Reading order = from bottom item (read first) to top item (read last)

**Standard reading order:** Title → Content → Other elements

---

## Alt Text for Images and Objects

Every image, chart, SmartArt, icon, or video needs alt text.

### Adding Alt Text

**Right-click method:**
1. Right-click the image or object
2. Select "Edit Alt Text…"
3. Type the description

**Ribbon method:**
1. Click the object
2. Picture Format (or Shape Format) tab → Accessibility → Alt Text

### Decorative Images

1. Open Edit Alt Text
2. Check "Mark as decorative"

### Charts and SmartArt

Charts need descriptive alt text explaining the data's key message.

**Alt text examples:**
- Chart: "Bar chart showing North America leading Q4 revenue at $4.2M, followed by Europe at $2.9M and APAC at $0.8M"
- SmartArt: "Process diagram showing three sequential steps: Research, Design, Launch"
- Infographic: "Timeline of key company milestones from 2010 to 2025 — see speaker notes for full details"

---

## Text in Slides

### Use Built-in Text Placeholders

Text in built-in placeholders is read by screen readers. Text in shapes or text boxes may not be in the correct reading order.

### Text Formatting

- Minimum 24pt font size for slide body text
- Use high-contrast colors (4.5:1 for body text)
- Do not use color as the only way to convey meaning
- Use san-serif fonts (Calibri, Arial, Helvetica)
- Ensure auto-fit text is not too small to read

---

## Tables in Presentations

Tables in PowerPoint have limited accessibility support. If the presentation will be read as a PowerPoint file (not converted to PDF), tables should be simple.

1. Insert → Table
2. Design tab → check "Header Row"
3. Keep tables simple — no merged cells if possible
4. Add alt text to describe the table's data

---

## Hyperlinks

Links need descriptive text.

1. Select descriptive text
2. Insert → Link (Ctrl + K)
3. Text to display should be descriptive
4. Avoid bare URLs as link text in slides

---

## Color and Contrast

- Body text: 4.5:1 contrast ratio minimum
- Large headings (18pt+ regular or 14pt+ bold): 3:1 minimum
- Do not convey information by color alone
- Use slide theme colors that meet contrast requirements

### Checking Contrast

Use the Colour Contrast Analyser (free tool) to check text and background colors:
1. Use the eyedropper to pick text color
2. Use the eyedropper to pick background color
3. Verify ratio meets 4.5:1 (or 3:1 for large text)

---

## Audio and Video in Presentations

- Video: embed captions using the caption track feature
- Audio: provide transcript
- Auto-playing media: provide user control

### Adding Captions to Video in PowerPoint

1. Click the video
2. Playback tab → Insert Captions
3. Select your .srt or .vtt file

---

## Running the Accessibility Checker

1. Review tab → Check Accessibility
2. Review all Errors, Warnings, and Tips
3. Fix errors before distribution

### Common Issues Found

| Issue | Fix |
|-------|-----|
| Missing slide title | Add title to every slide |
| Missing alt text | Add alt text to all images and objects |
| Hard to read text contrast | Change text/background colors |
| Check reading order | Rearrange items in Selection Pane |
| Repeated blank characters | Remove extra spaces; use proper spacing |
| Missing table header | Mark first row as header row |
| Object with no description | Add alt text to shapes/SmartArt |

---

## Exporting to PDF

If distributing as PDF:
1. File → Save As → PDF
2. Options → check "Document structure tags for accessibility"
3. Check "Document properties"
4. This preserves the reading order and slide titles

---

## Speaker Notes for Complex Content

For slides with complex visual content (maps, complex charts, diagrams):
- Add full text description in speaker notes
- Reference the notes in alt text: "Complex diagram — see speaker notes for full description"
- When sharing slides, share with notes view or as a separate transcript

---

## Checklist

- [ ] Every slide has a unique, descriptive title
- [ ] Reading order is logical in the Selection Pane
- [ ] All meaningful images have alt text
- [ ] Decorative images marked as decorative
- [ ] All links have descriptive text (no bare URLs)
- [ ] Color is not the only way to convey information
- [ ] Text contrast meets 4.5:1 (body) or 3:1 (large)
- [ ] Charts have descriptive alt text with key findings
- [ ] Tables have header row
- [ ] Video/audio has captions/transcripts
- [ ] Accessibility Checker shows no errors
- [ ] PDF export includes document structure tags
