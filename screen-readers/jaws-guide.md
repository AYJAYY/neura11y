---
title: "JAWS Screen Reader Guide"
standard: "JAWS 2024 / 2025"
source_url: "https://support.freedomscientific.com/content/html/jawshq/JAWS-Keystrokes.html"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["jaws", "screen-reader", "windows", "testing", "keyboard"]
ai_context: "Comprehensive JAWS screen reader guide covering commands, modes, and testing workflows. Load when testing or advising on JAWS compatibility."
---

# JAWS Screen Reader Guide

**Version:** JAWS 2024 / 2025 (Freedom Scientific). Windows only.

**Market position:** Most widely used desktop screen reader in enterprise and government; historically dominant in workplace settings.

---

## Basic Navigation Modes

JAWS operates in two primary modes that affect how key presses are interpreted.

### Virtual PC Cursor (Browse Mode)
- **Default mode** for reading web content and documents
- Arrow keys move through content character by character, word by word, or line by line
- JAWS intercepts key presses to navigate the virtual buffer (not the live page)
- Use for reading, navigating headings, links, landmarks

### Forms Mode (Application/PC Cursor Mode)
- Activated automatically when focus enters a form control
- Key presses are passed to the application/form field
- Press `Enter` on an edit field, or `JAWS Key + Z` to toggle
- Required for typing in inputs, interacting with custom widgets

### JAWS Key
- **Desktop layout:** `Insert`
- **Laptop layout:** `CapsLock`
- Referenced below as `JAWS Key`

---

## Essential Navigation Commands

### Reading

| Command | Action |
|---------|--------|
| `Down Arrow` | Next line |
| `Up Arrow` | Previous line |
| `Ctrl + Home` | Jump to top of page |
| `Ctrl + End` | Jump to bottom of page |
| `JAWS Key + Down Arrow` | Say all (read from cursor) |
| `Ctrl` | Stop reading |
| `JAWS Key + Up Arrow` | Read current line |
| `JAWS Key + Numpad 5` | Read current word |
| `JAWS Key + F` | Read font information |

### Headings

| Command | Action |
|---------|--------|
| `H` | Next heading |
| `Shift + H` | Previous heading |
| `1–6` | Next heading of level 1–6 |
| `Shift + 1–6` | Previous heading of level 1–6 |
| `JAWS Key + F6` | Open Headings list dialog |

### Links

| Command | Action |
|---------|--------|
| `Tab` | Next focusable element |
| `Shift + Tab` | Previous focusable element |
| `K` | Next link |
| `Shift + K` | Previous link |
| `U` | Next unvisited link |
| `V` | Next visited link |
| `JAWS Key + F7` | Open Links list dialog |
| `Enter` | Activate link |

### Landmarks / Regions

| Command | Action |
|---------|--------|
| `R` | Next ARIA landmark/region |
| `Shift + R` | Previous landmark |
| `JAWS Key + F5` | Open Select a Form Field dialog |
| `Q` | Jump to main content landmark |

### Tables

| Command | Action |
|---------|--------|
| `T` | Next table |
| `Shift + T` | Previous table |
| `Ctrl + Alt + Arrow keys` | Navigate table cells |
| `JAWS Key + Ctrl + Alt + Home` | Move to first cell |
| `JAWS Key + Ctrl + Alt + End` | Move to last cell |

JAWS reads column headers automatically when navigating cells if `<th>` or `scope` attributes are present.

### Forms

| Command | Action |
|---------|--------|
| `F` | Next form control |
| `Shift + F` | Previous form control |
| `B` | Next button |
| `Shift + B` | Previous button |
| `X` | Next checkbox |
| `A` | Next radio button |
| `Z` | Next combo box |
| `Enter` (on combo box) | Open combo box |
| `Space` | Check/uncheck checkbox; activate button |

### Lists and Other Elements

| Command | Action |
|---------|--------|
| `L` | Next list |
| `I` | Next list item |
| `G` | Next graphic |
| `D` | Next landmark/region (same as R) |
| `M` | Next frame |
| `P` | Next paragraph |
| `S` | Next sentence |
| `W` | Next word |
| `C` | Next combo box |
| `E` | Next edit field |

---

## Virtual Viewer and JAWS Specific Features

### Virtual Viewer
`JAWS Key + F2` — Opens JAWS Help/Virtual Viewer for reading content JAWS generates (like table summaries, descriptions)

### Find
`Ctrl + F` — JAWS Find dialog (search virtual buffer)

### Search Next
`Ctrl + G` or `F3` — Find next occurrence

### JAWS Key + T
Read window title bar

### JAWS Key + E
Read status bar

### JAWS Key + Delete
Read focus

---

## Behavior on Common HTML Elements

### `<button>` vs `<div role="button">`
- Native `<button>`: JAWS announces "Button" and activates on Space/Enter
- `role="button"`: JAWS announces "Button" only if `tabindex` is present; Enter works, Space may not without `keydown` handler

### `<select>`
- Forms mode required; Up/Down Arrow selects options
- `Alt + Down Arrow` opens the dropdown in Windows standard behavior

### `aria-expanded`
- JAWS announces "expanded" / "collapsed" when state changes on disclosure buttons, accordions, menus

### `aria-live` Regions
- `aria-live="polite"` — JAWS reads when idle
- `aria-live="assertive"` — interrupts current speech
- `aria-atomic="true"` — reads entire region, not just changed portion
- Common quirk: JAWS may not announce live regions injected via JavaScript before the virtual buffer loads them

### Focus Management
- When focus is moved programmatically (e.g., to a modal), JAWS follows if focus is moved to a visible element in the DOM
- `aria-modal="true"` helps JAWS restrict virtual cursor to modal boundaries (JAWS 2019+)

### Skip Links
- JAWS users typically navigate by heading or landmark rather than using skip links
- Skip links still useful for keyboard-only users; ensure they work on Enter press

---

## JAWS Settings Affecting Testing

| Setting | Default | Notes |
|---------|---------|-------|
| Virtual PC Cursor | On | Should be on for web testing |
| Smart Navigation | On | Auto-switches forms mode |
| HTML Processing | Enabled | Builds virtual buffer from HTML |
| Text Processing | Adjustable | Controls verbosity |

**Check JAWS version:** `JAWS Key + J` → Help → About

---

## Testing Checklist for JAWS

1. **Page title** — Press `Ctrl + Home`, confirm title is read (maps to `<title>`)
2. **Heading structure** — Open headings list (`JAWS Key + F6`); verify logical H1–H6 hierarchy
3. **Landmark navigation** — Press `R` repeatedly; verify main, nav, header, footer announced
4. **Link list** — Open links list (`JAWS Key + F7`); verify no "click here" / "read more" links
5. **Form labels** — Tab to each input; verify label/placeholder is announced before "Edit"
6. **Error announcements** — Submit invalid form; verify errors announced (aria-live or focus move)
7. **Modal dialogs** — Open modal; verify focus inside, background virtual cursor restricted
8. **Dynamic content** — Trigger live region update; verify announced after action
9. **Images** — Navigate with `G`; verify alt text meaningful, decorative images skipped
10. **Table headers** — Navigate table; verify row/column headers announced with cell content

---

## JAWS Quirks and Known Issues

| Issue | Mitigation |
|-------|-----------|
| `aria-modal="true"` support requires JAWS 2019+ | Test in current versions; `inert` attribute provides broader support |
| Live regions may not announce if content is loaded before JAWS Virtual PC cursor is enabled | Trigger update after page load; use `aria-live="polite"` not "off" by default |
| `<details>/<summary>` support inconsistent in older JAWS | Favor `aria-expanded` on button-based accordions |
| SVG content often ignored unless `role="img"` + `aria-label` | Always add role + label to informative SVGs |
| Announced text may differ from visually rendered text for CSS-generated content | Avoid using CSS `::before`/`::after` for meaningful content |
| Focus on `<div tabindex="-1">` read inconsistently | Prefer `tabindex="0"` or native elements for focus targets |

---

## JAWS + Browser Compatibility Matrix

| Browser | Compatibility | Notes |
|---------|--------------|-------|
| Chrome (latest) | Best | Primary supported browser |
| Edge (Chromium) | Excellent | Near-equivalent to Chrome |
| Firefox | Good | Some ARIA support differences |
| Internet Explorer 11 | Legacy only | JAWS still supports; avoid IE11 |
| Safari (Windows) | Not applicable | Safari not available on Windows |

---

## Key Resources

- JAWS Quick Start Guide: freedomscientific.com/products/software/jaws/
- JAWS keyboard shortcuts (PDF): available from Freedom Scientific support
- ARIA in JAWS notes: a11ysupport.io (filter by JAWS)
