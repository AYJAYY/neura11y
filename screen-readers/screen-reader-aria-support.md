---
title: "Screen Reader ARIA Support Matrix"
standard: "WAI-ARIA 1.2"
source_url: "https://a11ysupport.io"
domain: ["web"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["screen-reader", "aria", "support", "jaws", "nvda", "voiceover", "talkback", "matrix"]
ai_context: "Screen reader support matrix for ARIA roles, states, and properties. Shows cross-SR compatibility for ARIA patterns. Load when advising on ARIA usage or diagnosing screen reader compatibility issues."
---

# Screen Reader ARIA Support Matrix

**Sources:** a11ysupport.io, WAI-ARIA 1.2 authoring practices, developer testing.
**Last reviewed:** 2026-03-13

Screen readers tested:
- **JAWS** — JAWS 2024/2025 + Chrome on Windows
- **NVDA** — NVDA 2024.x + Chrome/Firefox on Windows
- **VoiceOver macOS** — VoiceOver + Safari on macOS Ventura/Sonoma
- **VoiceOver iOS** — VoiceOver + Safari on iOS 17
- **TalkBack** — TalkBack + Chrome on Android 14

**Legend:** ✅ Full support | ⚠️ Partial/inconsistent | ❌ Not supported | 🔵 Notes

---

## ARIA Landmark Roles

| Role | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|------|------|------|----------|--------|----------|-------|
| `role="banner"` | ✅ | ✅ | ✅ | ✅ | ✅ | Announced as "banner" or "header" |
| `role="navigation"` | ✅ | ✅ | ✅ | ✅ | ✅ | With `aria-label` for multiple navs |
| `role="main"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `role="complementary"` | ✅ | ✅ | ✅ | ✅ | ✅ | "complementary" or "aside" |
| `role="contentinfo"` | ✅ | ✅ | ✅ | ✅ | ✅ | "content information" or "footer" |
| `role="form"` | ✅ | ✅ | ✅ | ✅ | ✅ | Requires accessible name to be landmark |
| `role="search"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | iOS/Android improving support |
| `role="region"` | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | Only landmark when has accessible name |

---

## ARIA Widget Roles

### Common Widget Roles

| Role | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|------|------|------|----------|--------|----------|-------|
| `role="button"` | ✅ | ✅ | ✅ | ✅ | ✅ | Needs `tabindex="0"` and keydown Space handler |
| `role="link"` | ✅ | ✅ | ✅ | ✅ | ✅ | Needs `tabindex="0"` |
| `role="checkbox"` | ✅ | ✅ | ✅ | ✅ | ✅ | Requires `aria-checked` |
| `role="radio"` | ✅ | ✅ | ✅ | ✅ | ✅ | Use `role="radiogroup"` as container |
| `role="textbox"` | ✅ | ✅ | ✅ | ✅ | ✅ | For custom text inputs |
| `role="combobox"` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | Complex; use APG pattern; Safari support varies |
| `role="listbox"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Needs `aria-selected` on options |
| `role="option"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Child of listbox/combobox |
| `role="menuitem"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Part of menu/menubar pattern |
| `role="menu"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Application menus; not navigation menus |
| `role="menubar"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | |
| `role="tab"` | ✅ | ✅ | ✅ | ✅ | ✅ | With `role="tablist"` and `role="tabpanel"` |
| `role="tablist"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `role="tabpanel"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `role="slider"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Needs `aria-valuenow/min/max/valuetext` |
| `role="spinbutton"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | |
| `role="switch"` | ✅ | ✅ | ✅ | ✅ | ✅ | Announced as on/off toggle |
| `role="tooltip"` | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ | Typically used with `aria-describedby`; role itself poorly supported |

### Composite Widget Roles

| Role | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|------|------|------|----------|--------|----------|-------|
| `role="tree"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Complex; use APG tree pattern |
| `role="treeitem"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | |
| `role="grid"` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | Differs from `role="table"` — grid is interactive |
| `role="gridcell"` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | |
| `role="rowheader"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `role="columnheader"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `role="dialog"` | ✅ | ✅ | ✅ | ✅ | ✅ | Needs `aria-labelledby` |
| `role="alertdialog"` | ✅ | ✅ | ✅ | ✅ | ✅ | Interrupts SR like alert |
| `role="alert"` | ✅ | ✅ | ✅ | ✅ | ✅ | Equivalent to `aria-live="assertive"` |
| `role="status"` | ✅ | ✅ | ✅ | ✅ | ✅ | Equivalent to `aria-live="polite"` |
| `role="log"` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | Chat/log regions; polite live |
| `role="progressbar"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | With `aria-valuenow/min/max` |

---

## ARIA States and Properties

### States

| Attribute | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Announces As |
|-----------|------|------|----------|--------|----------|-------------|
| `aria-expanded="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | "expanded" |
| `aria-expanded="false"` | ✅ | ✅ | ✅ | ✅ | ✅ | "collapsed" |
| `aria-checked="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | "checked" |
| `aria-checked="mixed"` | ✅ | ✅ | ✅ | ✅ | ⚠️ | "mixed" / "partially checked" |
| `aria-selected="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | "selected" |
| `aria-pressed="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | "pressed" / toggle button |
| `aria-pressed="mixed"` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Varies |
| `aria-disabled="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | "dimmed" / "unavailable" |
| `aria-hidden="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | Removes from AT tree |
| `aria-invalid="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | "invalid entry" / "error" |
| `aria-busy="true"` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | May announce "busy" |

### Properties — Labeling

| Attribute | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|-----------|------|------|----------|--------|----------|-------|
| `aria-label` | ✅ | ✅ | ✅ | ✅ | ✅ | Overrides text content |
| `aria-labelledby` | ✅ | ✅ | ✅ | ✅ | ✅ | References another element's text |
| `aria-describedby` | ✅ | ✅ | ✅ | ✅ | ✅ | Supplementary description |
| `aria-placeholder` | ✅ | ✅ | ✅ | ✅ | ✅ | For custom inputs |
| `aria-valuetext` | ✅ | ✅ | ✅ | ✅ | ✅ | Human-readable value for sliders |

### Properties — Live Regions

| Attribute | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|-----------|------|------|----------|--------|----------|-------|
| `aria-live="polite"` | ✅ | ✅ | ✅ | ✅ | ✅ | Reads when SR idle |
| `aria-live="assertive"` | ✅ | ✅ | ✅ | ✅ | ✅ | Interrupts current speech |
| `aria-live="off"` | ✅ | ✅ | ✅ | ✅ | ✅ | Suppresses announcements |
| `aria-atomic="true"` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | Reads entire region; inconsistent |
| `aria-relevant` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Poorly supported; avoid |

### Properties — Relationships

| Attribute | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|-----------|------|------|----------|--------|----------|-------|
| `aria-controls` | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | Poorly supported; don't rely on |
| `aria-owns` | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | Reparents DOM elements in AT tree |
| `aria-haspopup` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Announces "has popup" / "submenu" |
| `aria-flowto` | ❌ | ❌ | ❌ | ❌ | ❌ | Not implemented; avoid |
| `aria-current="page"` | ✅ | ✅ | ✅ | ✅ | ✅ | "current page" in nav |
| `aria-current="step"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Wizard steps |

### Modal

| Attribute | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|-----------|------|------|----------|--------|----------|-------|
| `aria-modal="true"` | ✅ (2019+) | ✅ | ✅ | ✅ | ✅ | Restricts virtual cursor to dialog |

---

## Key Compatibility Insights

### Reliable Patterns (Use Confidently)

1. **`aria-label` / `aria-labelledby`** — Consistent across all SRs
2. **`aria-expanded`** — Consistently announced for disclosures and menus
3. **`role="alert"`** — Reliable live region for errors and status messages
4. **`role="dialog"` + `aria-modal="true"` + `aria-labelledby`** — Well-supported modal pattern
5. **`aria-live="polite"`** — Reliable for status updates (search results count, cart updates)
6. **`role="tab/tablist/tabpanel"`** — Well-supported tabs pattern
7. **`aria-current="page"`** — Well-supported for current navigation indication

### Problematic Patterns (Use with Caution)

1. **`aria-controls`** — VoiceOver does not implement; don't rely on it for functionality
2. **`aria-relevant`** — Use `aria-atomic` instead for live region behavior
3. **`role="tooltip"`** — Poorly supported on mobile; always supplement with visible text or `aria-describedby`
4. **`role="combobox"`** — Complex; test thoroughly across browsers. Follow APG pattern exactly.
5. **VoiceOver + `list-style: none`** — Lists lose semantics; add `role="list"` to restore

### Never Use

- `aria-flowto` — Not implemented anywhere
- ARIA to override incorrect semantic HTML — Fix the HTML instead
- `aria-hidden="true"` on focusable elements — Creates keyboard traps

---

## Resources

- a11ysupport.io — detailed per-attribute test results
- WAI-ARIA 1.2: w3.org/TR/wai-aria-1.2/
- ARIA in HTML: w3.org/TR/html-aria/
- APG Patterns: w3.org/WAI/ARIA/apg/patterns/
