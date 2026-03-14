---
title: "Color and Contrast Requirements"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["contrast", "color", "1.4.3", "1.4.6", "1.4.11", "2.4.11", "apca", "color-blindness"]
ai_context: "Exact color contrast ratios, thresholds, and requirements for WCAG 2.2. Load when specifying colors, reviewing visual design, or generating content with color specifications."
---

# Color and Contrast Requirements

---

## Contrast Ratio Requirements Summary

| Criterion | Level | Text Type | Minimum Ratio |
|-----------|-------|-----------|---------------|
| SC 1.4.3 | AA | Normal text | **4.5:1** |
| SC 1.4.3 | AA | Large text (≥18pt or ≥14pt bold) | **3:1** |
| SC 1.4.6 | AAA | Normal text | **7:1** |
| SC 1.4.6 | AAA | Large text | **4.5:1** |
| SC 1.4.11 | AA | UI components and graphical objects | **3:1** |
| SC 2.4.11 | AA | Focus indicator vs. adjacent colors | **3:1** |

---

## SC 1.4.3 — Contrast (Minimum) — Level AA

### Large Text Definition

Text is "large" if it meets EITHER of:
- **≥18pt** (≥24px) at regular (400) font weight
- **≥14pt** (approximately ≥18.67px) at bold (700+) font weight

Note: "pt" in CSS is 1.333px. 18pt = 24px exactly. 14pt ≈ 18.67px.

### Exceptions (No Contrast Requirement)

- **Inactive UI components** — Disabled buttons, grayed-out controls
- **Decorative text** — Text that is part of a purely decorative image, logo, or background
- **Logotypes** — Text that is part of a logo or brand name
- **Incidental text** — Text in photographs or complex imagery

### Contrast Ratio Formula

Contrast ratio = (L1 + 0.05) / (L2 + 0.05)

Where:
- L1 = relative luminance of the lighter color
- L2 = relative luminance of the darker color
- Relative luminance of black = 0; white = 1
- Maximum ratio = 21:1 (black on white)
- Minimum passing ratio for normal text = 4.5:1

### Relative Luminance Calculation

```
For each RGB channel (R, G, B in range 0-1):
  If c <= 0.04045: c_lin = c / 12.92
  Else: c_lin = ((c + 0.055) / 1.055) ^ 2.4

L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin
```

Tools perform this automatically — use WebAIM Contrast Checker or browser DevTools.

### Common Failing Color Combinations

| Background | Text Color | Ratio | Passes AA? |
|---|---|---|---|
| #ffffff (white) | #767676 (gray) | 4.48:1 | Fail (just below 4.5:1) |
| #ffffff (white) | #777777 (gray) | 4.48:1 | Fail |
| #ffffff (white) | #595959 (gray) | 7.0:1 | Pass (AAA) |
| #ffffff (white) | #767676 bold 14pt | 4.48:1 | Pass (large text) |
| #0071bc (blue) | #ffffff (white) | 4.6:1 | Pass AA |
| #d0021b (red) | #ffffff (white) | 5.74:1 | Pass AA |
| #f5a623 (orange) | #000000 (black) | 6.65:1 | Pass AA |
| #f5a623 (orange) | #ffffff (white) | 2.63:1 | Fail |

---

## SC 1.4.11 — Non-text Contrast — Level AA

### What It Applies To

- **Form control boundaries** — The outline/border of `<input>`, `<textarea>`, `<select>` (against background)
- **Icons that convey information** — Not decorative icons
- **Graphical objects** — Parts of charts, graphs, maps that convey information
- **Focus indicators** — The focus outline (see also SC 2.4.11)
- **UI component state indicators** — Checkbox border, radio button border

### What It Does NOT Apply To

- Decorative images
- Inactive/disabled components
- Logos
- Text (text is covered by SC 1.4.3)

### 3:1 Requirement for Form Control Borders

A light gray border on white background is a common failure:
- `#d3d3d3` (light gray) on `#ffffff` (white) = 1.78:1 — **FAIL**
- `#767676` (mid gray) on `#ffffff` (white) = 4.48:1 — **PASS**
- `#949494` (gray) on `#ffffff` (white) = 2.98:1 — **FAIL** (just below 3:1)
- `#949494` (gray) on `#ffffff` (white) large text = pass (large text exception applies only to SC 1.4.3, not 1.4.11)

**Note:** SC 1.4.11 has no "large" exception — the 3:1 threshold applies regardless of component size.

---

## SC 1.4.1 — Use of Color — Level A

Color cannot be the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

### Failing Examples

- Required fields marked only by red text (no asterisk, no "required" label)
- Error fields highlighted only by red border (no error icon, no error text adjacent)
- Links in body text that are the same color as non-link text but underlined on hover only
- Chart lines distinguished only by color (no patterns, labels, or shapes)
- "Green = available, Red = unavailable" status without text labels

### Passing Examples

- Links with underline (or other non-color visual difference from body text)
- Error fields with red border AND an error icon AND error text
- Required fields with asterisk (*) in addition to red color
- Chart lines with different dash patterns in addition to different colors
- Status badges with text labels ("Available" / "Unavailable") in addition to colors

---

## SC 2.4.11 — Focus Appearance (Minimum) — Level AA (WCAG 2.2)

Focus indicator contrast is measured differently from text contrast:

**Requirement:** The focus indicator must have a contrast ratio of ≥ 3:1 between:
- The focused state color of the indicator, AND
- The adjacent colors in the unfocused state

Example: Blue outline (`#005fcc`) on white (`#ffffff`) background:
- `#005fcc` vs `#ffffff` = approximately 8.6:1 ✓

If the button itself has a colored background, the focus indicator must contrast against that background:
- Blue outline (`#005fcc`) on blue button (`#0071bc`): very low contrast ✗
- White outline (`#ffffff`) on blue button (`#0071bc`): approximately 4.6:1 ✓

---

## Color Independence (SC 1.4.1 Techniques)

### Links in Body Text

If links within paragraph text are not distinguishable by color alone:
- Option 1: Use underline (default browser behavior — don't remove it)
- Option 2: Use a 3:1 contrast ratio between link color and surrounding text color (not background — this is text-to-text contrast)

The 3:1 text-to-text contrast (link vs. non-link body text) + underline on hover is a common pattern:
```css
a {
  color: #0051a2;  /* Must have 3:1 contrast vs body text color */
  text-decoration: underline; /* OR remove underline and ensure 3:1 text contrast */
}
a:hover, a:focus {
  text-decoration: underline;
}
```

### Error States

```css
/* WRONG: color-only error indication */
.error { border-color: red; }

/* CORRECT: color + icon + text */
.error { border-color: #d93025; }  /* Red border */
/* Plus an error icon before the field */
/* Plus an error message in text */
```

---

## Color Blindness Considerations (Beyond SC 1.4.1)

Approximately 8% of men and 0.5% of women have some form of color vision deficiency.

| Type | Prevalence | Colors confused |
|------|-----------|----------------|
| Deuteranopia/Deuteranomaly | ~5% of men | Red-green (most common) |
| Protanopia/Protanomaly | ~1% of men | Red-green |
| Tritanopia/Tritanomaly | ~0.01% | Blue-yellow |
| Achromatopsia | Very rare | All color |

### Design Strategies

1. **Never rely on red/green alone** — Most common color blindness
2. **Add patterns to charts** — Hatching, dots in addition to colors
3. **Add shapes/icons to statuses** — Check mark (not just green), X (not just red)
4. **Test with grayscale** — If the page still conveys information in grayscale, it likely passes SC 1.4.1

### Testing Tools

- macOS/iOS: Accessibility → Display → Color Filters → Greyscale
- Chrome DevTools: Rendering → Emulate vision deficiencies
- Firefox: DevTools → Accessibility → Simulate color vision deficiency
- Colour Blindness Simulator (browser extension)

---

## APCA (Accessible Perceptual Contrast Algorithm)

**Status: Not normative in any current standard. Research only.**

APCA is a proposed contrast model for WCAG 3.0 that accounts for:
- Font size and weight (spatial frequency)
- Polarity (dark text on light vs. light text on dark)
- Background luminance effects

APCA uses a Lightness Contrast (Lc) value rather than a ratio.

Proposed APCA targets (subject to change):
- Normal body text: Lc 60+
- Large display text: Lc 45+
- Placeholder/non-body text: Lc 30+

**Important:** Use WCAG 2.2 contrast ratios (4.5:1, 3:1, 7:1) for all current compliance work. APCA is for research and future-proofing awareness only.

APCA tools: https://www.myndex.com/APCA/

---

## Color Specification Formats for AI

When specifying colors in accessibility contexts, provide:
1. Hex code (e.g., `#005fcc`)
2. Contrast ratio against expected background
3. Whether it passes AA, AAA, or neither for normal/large text
4. Whether it passes SC 1.4.11 for UI components (3:1)

Example: "Text color `#595959` on white `#ffffff` background — contrast ratio 7.0:1 — passes WCAG AA (4.5:1) and AAA (7:1) for normal text."
