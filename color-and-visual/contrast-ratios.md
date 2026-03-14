---
title: "Contrast Ratios and Color Accessibility"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["contrast", "color", "1.4.3", "1.4.6", "1.4.11", "wcag", "luminance"]
ai_context: "Complete contrast ratio thresholds for WCAG 2.2. Load when evaluating color choices or generating UI with text or interactive elements."
---

# Contrast Ratios and Color Accessibility

---

## Contrast Thresholds at a Glance

| Criterion | Element | Ratio | Level |
|-----------|---------|-------|-------|
| SC 1.4.3 | Normal text (< 18pt / < 14pt bold) | 4.5:1 | AA |
| SC 1.4.3 | Large text (≥ 18pt regular OR ≥ 14pt bold) | 3:1 | AA |
| SC 1.4.3 | Incidental text (disabled, decorative, logo) | None | — (exempt) |
| SC 1.4.6 | Normal text | 7:1 | AAA |
| SC 1.4.6 | Large text | 4.5:1 | AAA |
| SC 1.4.11 | UI components (borders, focus indicators, icons) | 3:1 | AA |
| SC 1.4.11 | Graphical objects needed to understand content | 3:1 | AA |

**Large text definition:**
- 18pt (24px) or larger in regular weight
- 14pt (approximately 18.67px) or larger in bold

---

## Relative Luminance Formula

The contrast ratio is calculated from the relative luminance (L) of two colors:

```
Contrast ratio = (L_lighter + 0.05) / (L_darker + 0.05)
```

Where L (relative luminance) for each color is calculated as:

```
L = 0.2126 × R + 0.7152 × G + 0.0722 × B
```

Where R, G, B are linearized sRGB values:
```
If C_sRGB ≤ 0.03928:   C = C_sRGB / 12.92
Else:                  C = ((C_sRGB + 0.055) / 1.055) ^ 2.4
```

**In practice:** Use a contrast checker tool. Do not calculate by hand.

---

## Common Color Pair Pass/Fail

| Text Color | Background | Ratio | Normal text | Large text |
|-----------|-----------|-------|-------------|------------|
| #000000 (black) | #FFFFFF (white) | 21:1 | ✅ AA/AAA | ✅ AA/AAA |
| #FFFFFF (white) | #000000 (black) | 21:1 | ✅ AA/AAA | ✅ AA/AAA |
| #767676 (gray) | #FFFFFF (white) | 4.54:1 | ✅ AA | ✅ AA |
| #949494 (gray) | #FFFFFF (white) | 3.03:1 | ❌ AA | ✅ AA |
| #FFFFFF (white) | #0066CC (blue) | 4.56:1 | ✅ AA | ✅ AA |
| #FFFFFF (white) | #006600 (green) | 5.74:1 | ✅ AA | ✅ AA |
| #FFFFFF (white) | #CC0000 (red) | 4.04:1 | ❌ AA | ✅ AA |
| #FFFFFF (white) | #FF0000 (bright red) | 3.99:1 | ❌ AA | ✅ AA |
| #333333 | #FFFFFF (white) | 12.63:1 | ✅ AA/AAA | ✅ AA/AAA |
| #555555 | #FFFFFF (white) | 7.46:1 | ✅ AA/AAA | ✅ AA/AAA |
| #666666 | #FFFFFF (white) | 5.74:1 | ✅ AA | ✅ AA |
| #999999 | #FFFFFF (white) | 2.85:1 | ❌ | ❌ |

---

## SC 1.4.11 — Non-Text Contrast

SC 1.4.11 requires 3:1 contrast for:

**User interface components:**
- Button borders against background
- Input field borders against background
- Focus indicators (the focus outline or ring)
- Checkbox/radio button borders

**Graphical objects:**
- Parts of icons needed to understand the icon's meaning
- Chart bars, lines, pie slices (when used to convey data)
- Parts of infographics essential to understanding

**Exempt from SC 1.4.11:**
- Disabled state components — exempt (conveys "unavailable")
- Inactive/decorative elements

### Focus Indicator Contrast (SC 2.4.11 — WCAG 2.2)

WCAG 2.2 added a minimum focus indicator size requirement. The focus area must:
- Have at least 3:1 contrast against adjacent colors
- Have a perimeter equal to the element perimeter × 2px (minimum enclosing perimeter)
- Not be fully obscured by other content

See `domains/web/focus-management.md` for implementation details.

---

## Tools for Checking Contrast

| Tool | Platform | Notes |
|------|----------|-------|
| WebAIM Contrast Checker (webaim.org/resources/contrastchecker/) | Web | Industry standard |
| Colour Contrast Analyser (TPGi) | Windows/macOS | Eyedropper tool |
| Axe browser extension | Browser | Checks page contrast automatically |
| Figma A11y plugins (Contrast, Stark) | Figma | Design-time checking |
| Chrome DevTools CSS Overview | Browser | Reports contrast failures |
| Lighthouse accessibility audit | Browser/CI | Includes contrast check |

---

## Using Color to Convey Information (SC 1.4.1)

SC 1.4.1 (Level A) requires that color is not the only visual means of conveying information.

**Examples of color-only information (non-compliant):**
- Error state shown only by red border (no icon or text)
- Required fields indicated only by colored label
- Active/selected state shown only by background color
- Chart legend where items are distinguished only by color

**Compliant approaches:**
- Error: red border + error icon + error text message
- Required fields: red asterisk + "(required)" text + `aria-required="true"`
- Active tab: color + bold text + underline or border indicator
- Chart: color + distinct patterns/shapes OR text labels on chart

---

## Color Blindness Considerations

Approximately 8% of males and 0.5% of females have some form of color blindness.

| Type | Affects | Impact |
|------|---------|--------|
| Deuteranopia | Red-green (can't see green) | Most common; reds and greens look similar |
| Protanopia | Red-green (can't see red) | Reds and greens look similar |
| Tritanopia | Blue-yellow | Less common |
| Achromatopsia | All color (monochrome) | Rare; relies entirely on luminance |

### Testing for Color Blindness

- Chrome DevTools → Rendering → Emulate vision deficiencies
- Figma: Stark plugin → Color Blind preview
- NoCoffee extension (Chrome)

### Design Principles

- Never use red/green alone to signal pass/fail (deuteranopia)
- Add icons to success/error states (checkmark, X)
- Use patterns in addition to color for charts
- Test in monochrome (grayscale) — all information should still be conveyed

---

## APCA (Advanced Perceptual Contrast Algorithm)

APCA is the contrast model being considered for WCAG 3.0. It differs from WCAG 2.x:

- WCAG 2.x: single ratio for all text sizes and weights
- APCA: different thresholds based on font size AND font weight (lighter fonts need more contrast)
- APCA uses Lc (Lightness Contrast) scale rather than a simple ratio

**Important:** APCA is NOT currently normative. WCAG 2.2 still uses the 4.5:1 / 3:1 model. Do not use APCA for compliance claims against WCAG 2.x.

See `standards/wcag/wcag-3.0-overview.md` for more on WCAG 3.0 and APCA.

---

## Practical CSS for Contrast-Safe Text

```css
/* Safe dark text on white */
body {
  color: #333333; /* 12.63:1 on white */
  background-color: #ffffff;
}

/* Safe light text on dark */
.dark-theme {
  color: #e0e0e0; /* ~11:1 on #1a1a1a */
  background-color: #1a1a1a;
}

/* Acceptable gray text (barely passes AA) */
.secondary-text {
  color: #767676; /* 4.54:1 on white */
}

/* Link color on white (passes AA with text underline as additional cue) */
a {
  color: #0056b3; /* ~7:1 on white */
}

/* Danger/error red that passes on white */
.error-text {
  color: #cc0000; /* 4.04:1 on white — fails AA for body text; use for large text only */
}
/* Better: */
.error-text-aa {
  color: #b30000; /* 5.93:1 on white — passes AA */
}
```
