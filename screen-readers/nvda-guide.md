---
title: "NVDA Screen Reader Guide for Testing"
standard: ""
source_url: "https://www.nvaccess.org/files/nvda/documentation/userGuide.html"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["nvda", "screen-reader", "testing", "windows", "keyboard-commands"]
ai_context: "NVDA key commands, modes, and testing workflow for web accessibility testing. Load when writing NVDA testing instructions."
---

# NVDA Screen Reader Guide for Testing

---

## About NVDA

NVDA (NonVisual Desktop Access) is a free, open-source screen reader for Windows, developed by NV Access. It is the second most widely used screen reader after JAWS. **Recommended test combination: NVDA + Chrome or NVDA + Firefox.**

**Download:** nvaccess.org

---

## NVDA Modifier Key

The NVDA key is `Insert` by default. The Caps Lock key can also be set as the NVDA modifier.

In this guide, **NVDA** = the Insert key (or Caps Lock if configured).

---

## Browse Mode vs. Forms/Application Mode

NVDA has two primary modes:

| Mode | What it does | When it activates |
|------|-------------|-------------------|
| **Browse Mode** | Navigate page with keyboard shortcuts; arrow keys read content | Default on web pages |
| **Forms/Application Mode** | Keys go directly to form fields and interactive widgets | Auto-activates when focus enters form field or application role |

**Toggle between modes:** `NVDA + Space`

When NVDA auto-switches to Forms Mode, it says "forms mode" aloud. When you Tab out of a form field, it may say "browse mode."

---

## Essential NVDA Commands

### Reading

| Action | Key |
|--------|-----|
| Read all from current position | `NVDA + Down Arrow` |
| Stop reading | `Ctrl` |
| Read current line | `NVDA + Up Arrow` |
| Read next word | `Ctrl + Right Arrow` |
| Read previous word | `Ctrl + Left Arrow` |
| Read current word | `NVDA + Numpad 5` |
| Say character | `Numpad 5` |
| Read from beginning | `NVDA + Home` |

### Browse Mode Navigation

| Navigate to | Key | Reverse |
|-------------|-----|---------|
| Next heading | `H` | `Shift + H` |
| Heading level 1 | `1` | `Shift + 1` |
| Heading level 2 | `2` | `Shift + 2` |
| Heading level 3 | `3` | `Shift + 3` |
| Next link | `K` | `Shift + K` |
| Next unvisited link | `U` | `Shift + U` |
| Next visited link | `V` | `Shift + V` |
| Next form field | `F` | `Shift + F` |
| Next button | `B` | `Shift + B` |
| Next checkbox | `X` | `Shift + X` |
| Next combobox | `C` | `Shift + C` |
| Next edit box | `E` | `Shift + E` |
| Next list | `L` | `Shift + L` |
| Next table | `T` | `Shift + T` |
| Next landmark / region | `D` | `Shift + D` |
| Next graphic | `G` | `Shift + G` |
| Next separator | `S` | `Shift + S` |

### Elements List

`NVDA + F7` opens a dialog listing:
- Links
- Headings
- Form fields
- Buttons
- Landmarks

Use this to quickly audit the page's accessible elements.

---

## Table Navigation (Browse Mode)

| Action | Key |
|--------|-----|
| Move to next cell | `Ctrl + Alt + Right Arrow` |
| Move to previous cell | `Ctrl + Alt + Left Arrow` |
| Move to cell below | `Ctrl + Alt + Down Arrow` |
| Move to cell above | `Ctrl + Alt + Up Arrow` |
| Read column header | NVDA announces header as you navigate |
| Read row header | NVDA announces header as you navigate |

---

## NVDA Settings Relevant to Testing

### Speech Verbosity

`NVDA Menu → Preferences → Settings → Speech`

- **Report dynamic content changes** — Enables announcement of aria-live region updates
- **Report object descriptions** — Reads `aria-describedby` content
- **Report object states** — Reports expanded/collapsed, checked/unchecked

### Browse Mode Settings

`NVDA Menu → Preferences → Settings → Browse Mode`

- **Use screen layout** — If on, respects visual position; if off, more linear
- **Automatic focus mode for focus changes** — Switches to Forms Mode on focus

### Document Formatting

`NVDA Menu → Preferences → Settings → Document Formatting`

Controls what NVDA reports: headings, links, lists, tables, colors, fonts.

---

## Common NVDA Testing Scenarios

### Testing Page Structure

1. `NVDA + F7` → Open Elements List → Select "Headings"
2. Verify: logical hierarchy, descriptive names, correct levels
3. `NVDA + F7` → Select "Landmarks"
4. Verify: main, nav (with name), header, footer present

### Testing Forms

1. Tab to form; NVDA should announce the label and type ("Email address, edit text")
2. Type in field; NVDA should echo characters
3. Tab to submit button; NVDA should announce button label
4. Submit with invalid data; NVDA should announce error messages

### Testing Dynamic Content

1. Toggle aria-live region; listen for announcement
2. Open a modal; NVDA should announce the dialog title and move focus inside
3. Close modal with Escape; focus should return to trigger
4. SPA navigation: page title should be announced after route change

### Testing a Component

For each interactive component (dropdown, tabs, accordion, modal):
1. Tab to the component
2. NVDA should announce the role and state: "button, collapsed" or "tab, selected, 1 of 3"
3. Activate with Enter/Space
4. NVDA should announce state change: "expanded" or "Tab 2, selected"
5. Navigate internal items with arrow keys
6. Close with Escape if applicable

---

## What NVDA Announces (Expected Outputs)

| Element | Expected Announcement |
|---------|----------------------|
| `<h2>Products</h2>` | "Products — heading level 2" |
| `<button aria-expanded="false">Menu</button>` | "Menu — button — collapsed" |
| `<input type="text" aria-label="Search">` | "Search — edit text" |
| `<input type="checkbox" checked aria-label="Subscribe">` | "Subscribe — checkbox — checked" |
| `<a href="/about">About us</a>` | "About us — link" |
| `<img alt="Company logo">` | "Company logo — graphic" |
| `<img alt="">` | (Silent — decorative) |
| `<div role="alert">Error occurred</div>` | Immediately: "Error occurred — alert" |
| `<div role="status">3 results found</div>` | After interaction pause: "3 results found" |

---

## NVDA + Chrome vs. NVDA + Firefox

| Feature | Chrome | Firefox |
|---------|--------|---------|
| ARIA support | Very good | Very good |
| Live region reliability | Good | Good (may differ slightly) |
| Custom roles/properties | Strong | Strong |
| Forms Mode behavior | Slightly different | Slightly different |
| Recommendation | Primary | Secondary |

**Always test with both** for thorough coverage of the NVDA user base.
