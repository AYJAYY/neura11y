---
title: "Color Blindness and Vision Impairment Design Guide"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["color-blindness", "vision", "1.4.1", "contrast", "simulation", "design"]
ai_context: "Design guidance for color blindness and low vision. Covers types, design patterns, and testing approaches. Load when reviewing designs for color accessibility."
---

# Color Blindness and Vision Impairment Design Guide

---

## Color Vision Deficiency (Color Blindness)

Approximately 8% of males and 0.5% of females have some form of color vision deficiency (CVD).

### Types

| Type | What's affected | How colors appear | Prevalence (males) |
|------|----------------|------------------|--------------------|
| **Deuteranomaly** | Green cones (reduced) | Greens shifted toward yellow/brown | ~5% |
| **Deuteranopia** | Green cones (absent) | Reds and greens look similar (brownish) | ~1% |
| **Protanomaly** | Red cones (reduced) | Reds shifted toward green/brown | ~1% |
| **Protanopia** | Red cones (absent) | Reds appear dark; red-green confusion | ~1% |
| **Tritanomaly** | Blue cones (reduced) | Blue-yellow confusion | Rare |
| **Tritanopia** | Blue cones (absent) | Blues appear green; yellows appear pink | Very rare |
| **Achromatopsia** | No color cones | Complete grayscale vision | Very rare (~0.003%) |

**Most common:** Deuteranomaly and Deuteranopia (red-green color blindness combined = ~6% of males)

---

## SC 1.4.1 — Use of Color (Level A)

Color must not be the only visual means of conveying information, indicating an action, or distinguishing a visual element.

### Common Failures

| Pattern | Failure | Fix |
|---------|---------|-----|
| Required fields: red asterisk, no text | Red only | Add "(required)" text in label |
| Error state: red border only | Color only | Add error icon + error message text |
| Status: green dot = active, red = inactive | Color only | Add text labels: "Active" / "Inactive" |
| Chart: four lines distinguished only by color | Color only | Add distinct line patterns (solid, dashed, dotted) + labels |
| Link color different from body text, no underline | Color only | Add underline or other visual indicator |
| Calendar: booked days shown only in grey | Color only | Add strikethrough, label, or icon |

---

## Designing for Color Blindness

### Safe Color Pairs (Red-Green CVD)

Most problematic: red-green confusion in deuteranopia/protanopia.

| Avoid (similar in red-green CVD) | Use instead |
|----------------------------------|-------------|
| Red + Green | Red + Blue; Orange + Purple; Blue + Yellow |
| Dark red + dark green | Add symbols or patterns |
| Pure red + pure green for pass/fail | Add ✓ / ✗ icons + text labels |

### Universal Design Patterns

1. **Combine color with other cues:**
   - Icons (✓ for success, ✗ for error, ! for warning)
   - Text labels (not just color)
   - Patterns and textures (in charts and graphs)
   - Position and shape

2. **Ensure adequate contrast:**
   - High contrast helps low vision users
   - Even if colors look different to color-blind users, if contrast ratio is high, the distinction is clearer

3. **Test in grayscale:**
   - If information is still conveyed in grayscale (Chrome DevTools → Rendering → Achromatopsia), color is not the only cue

### Chart and Graph Patterns

```
// Instead of color-only chart lines:
// - Use different line styles
// - Use direct data labels
// - Use different point shapes

Series 1: Solid line   — ●
Series 2: Dashed line  — ■
Series 3: Dotted line  — ▲
Series 4: Dash-dot     — ◆
```

---

## Low Vision

Low vision is distinct from color blindness — it refers to reduced visual acuity not fully correctable with glasses.

WHO estimates 246 million people globally have low vision.

### Design for Low Vision

1. **Text size:** Body text 16px minimum; allow user resizing
2. **Zoom:** Content must work at 400% browser zoom (WCAG SC 1.4.10)
3. **Contrast:** Higher contrast benefits low vision users most; target AAA (7:1) for primary text
4. **Spacing:** Generous line height (1.6+), letter spacing, paragraph spacing
5. **Text over images:** Always use high contrast and a solid background behind text
6. **Focus indicators:** Large, high-contrast focus indicators

---

## Testing for Color Blindness

### Browser DevTools

Chrome DevTools → More Tools → Rendering → Emulate vision deficiencies:
- Blurred vision
- Deuteranopia
- Protanopia
- Tritanopia
- Achromatopsia

### Browser Extensions

- **NoCoffee** (Chrome): Simulates all CVD types + low vision
- **Colorblinding** (Chrome): Quick CVD simulation

### Design Tools

- **Figma:** Stark plugin → Color Blind mode (simulates multiple CVD types)
- **Adobe XD:** Stark plugin available
- **Sketch:** Stark plugin available

### Grayscale Quick Test

Convert entire page to grayscale and verify all information is still distinguishable. Chrome shortcut:

```
DevTools → Rendering → Emulate vision deficiencies → Achromatopsia (no color)
```

---

## Color Blindness in Common UI Patterns

### Status Indicators

```
// Bad: color only
🔴 Error   🟡 Warning   🟢 Success

// Good: color + icon + text label
❌ Error: Unable to save
⚠️ Warning: Action required
✅ Success: Changes saved
```

### Forms

```html
<!-- Bad: red border only for error -->
<input style="border: 2px solid red;">

<!-- Good: red border + icon + text -->
<input aria-invalid="true" aria-describedby="email-err">
<span id="email-err">
  ⚠️ Please enter a valid email address (example@domain.com)
</span>
```

### Data Tables

```html
<!-- Bad: cell background color only to indicate status -->
<td style="background: #ffcccc;">Overdue</td>

<!-- Good: text status value + optional color supplement -->
<td>
  <span class="status overdue">Overdue</span>
</td>
```

### Navigation: Current Page Indication

```html
<!-- Bad: active link colored differently (only) -->
<a href="/products" class="active">Products</a>

<!-- Good: color + font weight + aria-current -->
<a href="/products" aria-current="page" class="active">Products</a>
<!-- CSS: .active { font-weight: bold; border-bottom: 3px solid currentColor; } -->
```
