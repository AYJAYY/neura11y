---
title: "Typography Accessibility"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["typography", "fonts", "text-spacing", "1.4.4", "1.4.12", "dyslexia", "readability"]
ai_context: "Typography requirements and best practices for accessibility. Covers text spacing, resize, dyslexia-friendly fonts, and line length. Load when generating CSS or reviewing content design."
---

# Typography Accessibility

---

## SC 1.4.4 — Resize Text (Level AA)

Text must be resizable up to 200% without loss of content or functionality.

**Requirements:**
- Do not use `px` for font size in ways that prevent resizing
- Do not set `max-height` on containers that clips overflow when text is large
- Ensure no text becomes inaccessible at 200% zoom

**Implementation:**
```css
/* WRONG: px font sizes prevent browser font size preferences */
body { font-size: 14px; }

/* CORRECT: rem respects browser base font size */
body { font-size: 1rem; }       /* 16px default */
h1 { font-size: 2rem; }         /* 32px default */
small { font-size: 0.875rem; }  /* 14px default */

/* CORRECT: em respects parent element's size */
.card-title { font-size: 1.25em; }
```

---

## SC 1.4.12 — Text Spacing (Level AA)

Users must be able to set the following text spacing properties without loss of content or functionality:

| Property | Minimum override |
|----------|-----------------|
| Line height | 1.5× the font size |
| Letter spacing | 0.12em |
| Word spacing | 0.16em |
| Spacing after paragraphs | 2× the font size |

**This does NOT mean you must set these values.** It means your design must not break if a user sets them via a user stylesheet or browser extension.

### Testing with a Bookmarklet

```javascript
// Paste into browser console to apply all WCAG 1.4.12 thresholds simultaneously
(function() {
  const style = document.createElement('style');
  style.textContent = `
    * {
      line-height: 1.5 !important;
      letter-spacing: 0.12em !important;
      word-spacing: 0.16em !important;
    }
    p { margin-bottom: 2em !important; }
  `;
  document.head.appendChild(style);
})();
```

After applying, verify no content is hidden, clipped, or overlapping.

### Common Failure Patterns

```css
/* FAILS: Fixed-height container clips overflow text */
.card {
  height: 120px;       /* ❌ clashes with text spacing */
  overflow: hidden;
}

/* FIX: Use min-height instead */
.card {
  min-height: 120px;   /* ✅ allows expansion */
  overflow: visible;
}

/* FAILS: Fixed-line-height on input clips text at 1.5× */
input {
  line-height: 1;   /* ❌ may be overridden, breaking layout */
}

/* FIX: Use at least 1.5 natively */
input {
  line-height: 1.5; /* ✅ */
}
```

---

## Recommended Typography Defaults

These values exceed the WCAG minimum and provide good readability for a broad audience including people with dyslexia.

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
  font-size: 1rem;         /* 16px default */
  line-height: 1.6;        /* Exceeds 1.5× minimum */
  color: #333333;          /* 12.6:1 on white */
}

p {
  max-width: 70ch;         /* 60–80 characters per line */
  margin-bottom: 1.5em;    /* Generous paragraph spacing */
}

h1, h2, h3, h4 {
  line-height: 1.25;       /* Tighter for headings */
  margin-top: 2em;
  margin-bottom: 0.5em;
}
```

---

## Font Selection for Accessibility

### Body Text

**Recommended:**
- System font stacks (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif`)
- Open Sans, Nunito, Lato, Source Sans Pro
- Georgia, Palatino (serif fonts — fine for body text)

**Avoid for body text:**
- Very thin weight variants (100, 200) — low contrast even at correct ratio
- Highly decorative or script fonts
- Comic Sans in professional contexts (despite some dyslexia research suggesting it may help some readers)

### Dyslexia-Specific Considerations

Research on dyslexia-specific fonts (OpenDyslexic, Dyslexie) is mixed. The strongest design factors for dyslexia are:

1. **Letter spacing** — more helps (0.12em minimum)
2. **Line height** — more helps (1.5 minimum)
3. **Line length** — shorter helps (60–70 characters)
4. **Left-aligned text** — consistent left margin helps
5. **Not justified** — justified text creates irregular word spacing ("rivers")

These are all achievable with standard fonts using the CSS above.

---

## Line Length

Optimal reading line length is 60–80 characters (approximately 30–40em).

```css
article, .readable-text {
  max-width: 70ch;   /* ch = width of "0" character */
}

/* Responsive: don't restrict on small screens */
@media (min-width: 700px) {
  article {
    max-width: 70ch;
  }
}
```

---

## Text Alignment

- **Left-aligned text** is easier to read than centered or justified
- **Justified text** creates irregular word spacing — avoid for body text
- **Centered text** is acceptable for headings and short labels, not for paragraphs

```css
body { text-align: left; }         /* ✅ */
.prose { text-align: justify; }    /* ❌ for body text */
h2 { text-align: center; }        /* ✅ for short headings */
```

---

## All-Caps Text

All-caps text is harder to read (we recognize word shapes, which disappear in all caps). Use it sparingly.

```css
/* Visual all-caps with proper letter spacing */
.label {
  text-transform: uppercase;
  letter-spacing: 0.1em;  /* Wider spacing improves legibility */
  font-size: 0.875rem;
}
```

**Note:** `text-transform: uppercase` is read in lowercase by some screen readers. For abbreviations, use `<abbr>` with `title` attribute.

---

## Italics and Bold

- Italics: hard to read for dyslexia; use sparingly for brief emphasis
- Bold: effective for emphasis; use for key terms and labels
- Do not use italics for entire paragraphs

---

## Text Decoration (Underlines for Links)

Underlines on links help distinguish them from non-link text for people with color blindness.

```css
/* Default browsers: links are underlined */
a { text-decoration: underline; }

/* If removing underline, add another visual cue */
a {
  text-decoration: none;
  border-bottom: 2px solid currentColor;  /* Border-based underline */
}

/* Restore on hover/focus */
a:hover, a:focus {
  text-decoration: underline;
}
```

---

## Font Size Minimum Recommendations

| Context | Minimum | Recommended |
|---------|---------|-------------|
| Body text | 16px (1rem) | 16–18px |
| Small/secondary text | 14px | Avoid if possible |
| Caption text | 12px | Treat as large text (3:1 contrast) if possible |
| UI labels | 14px | 16px preferred |
| Mobile body | 16px (prevents iOS zoom) | 16–18px |

**iOS input zoom:** If `font-size` on `<input>` is less than 16px, iOS Safari automatically zooms in when the field is focused. Use 16px minimum for form inputs.

```css
input, select, textarea {
  font-size: 1rem; /* 16px — prevents iOS auto-zoom */
}
```
