---
title: "Screen Reader HTML Support Matrix"
standard: "WCAG 2.2 / HTML Living Standard"
source_url: "https://a11ysupport.io"
domain: ["web"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["screen-reader", "html", "support", "jaws", "nvda", "voiceover", "talkback", "matrix"]
ai_context: "Screen reader support matrix for HTML elements. Shows which HTML elements work reliably across JAWS, NVDA, VoiceOver, and TalkBack. Load when advising on HTML element choice for maximum screen reader compatibility."
---

# Screen Reader HTML Support Matrix

**Sources:** a11ysupport.io, WebAIM Screen Reader Survey (2024), developer testing.
**Last reviewed:** 2026-03-13

Screen readers tested:
- **JAWS** — JAWS 2024/2025 + Chrome on Windows
- **NVDA** — NVDA 2024.x + Chrome/Firefox on Windows
- **VoiceOver macOS** — VoiceOver + Safari on macOS Ventura/Sonoma
- **VoiceOver iOS** — VoiceOver + Safari on iOS 17
- **TalkBack** — TalkBack + Chrome on Android 14

**Legend:** ✅ Full support | ⚠️ Partial/inconsistent | ❌ Not announced | 🔵 Notes

---

## Headings

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<h1>`–`<h6>` | ✅ | ✅ | ✅ | ✅ | ✅ | Announces heading text + level |
| `role="heading" aria-level="2"` | ✅ | ✅ | ✅ | ✅ | ✅ | Use when native heading markup not possible |
| CSS `font-size` only (no `<h>`) | ❌ | ❌ | ❌ | ❌ | ❌ | **Never use CSS alone for headings** |

---

## Landmark Regions

| Element / Role | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|----------------|------|------|----------|--------|----------|-------|
| `<header>` / `role="banner"` | ✅ | ✅ | ✅ | ✅ | ✅ | Must be top-level or direct child of `<body>` for banner role |
| `<nav>` / `role="navigation"` | ✅ | ✅ | ✅ | ✅ | ✅ | Announce with `aria-label` if multiple navs |
| `<main>` / `role="main"` | ✅ | ✅ | ✅ | ✅ | ✅ | Only one `<main>` per page |
| `<footer>` / `role="contentinfo"` | ✅ | ✅ | ✅ | ✅ | ✅ | Must be top-level for contentinfo role |
| `<aside>` / `role="complementary"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<section aria-label>` / `role="region"` | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | Only announced as landmark if given accessible name |
| `<form aria-label>` / `role="form"` | ✅ | ✅ | ✅ | ✅ | ✅ | Requires accessible name to be announced as landmark |
| `role="search"` / `<search>` element | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | HTML `<search>` element support improving |

---

## Lists

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<ul>` + `<li>` | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | VoiceOver suppresses list semantics with `list-style: none` (CSS) |
| `<ol>` + `<li>` | ✅ | ✅ | ✅ | ✅ | ✅ | Announces item count and position |
| `<dl>` + `<dt>` + `<dd>` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Inconsistent across SRs; VoiceOver macOS announces well |

**VoiceOver `list-style: none` issue:** Safari/VoiceOver removes list semantics when `list-style: none` is applied. Fix: add `role="list"` to `<ul>` if list semantics must be preserved.

```html
<ul role="list" style="list-style: none;">
  <li>Item 1</li>
</ul>
```

---

## Links and Buttons

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<a href="...">` | ✅ | ✅ | ✅ | ✅ | ✅ | Announced as "link" |
| `<a>` without `href` | ❌ | ❌ | ❌ | ❌ | ❌ | Not keyboard focusable or announced as link |
| `<button>` | ✅ | ✅ | ✅ | ✅ | ✅ | Activates on Enter and Space |
| `<div role="button">` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Needs `tabindex="0"` and keydown handler for Space |
| `<button disabled>` | ✅ | ✅ | ✅ | ✅ | ✅ | Announced as "dimmed button" or "unavailable" |
| `<a>` with `role="button"` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Confusing; avoid — use `<button>` instead |

---

## Form Controls

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<input type="text">` with `<label>` | ✅ | ✅ | ✅ | ✅ | ✅ | Use `for`/`id` association |
| `<input>` with `aria-label` | ✅ | ✅ | ✅ | ✅ | ✅ | When visible label not possible |
| `<input>` with `aria-labelledby` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<input>` with only `placeholder` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Placeholder disappears on input; not a label |
| `<input type="checkbox">` | ✅ | ✅ | ✅ | ✅ | ✅ | Announces "checked"/"unchecked" |
| `<input type="radio">` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<select>` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<textarea>` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<fieldset>` + `<legend>` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Legend announced with each field in JAWS/NVDA; VoiceOver iOS inconsistent |
| `<input required>` / `aria-required="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `aria-invalid="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | Announces "invalid" or "error" |
| `aria-describedby` (error message) | ✅ | ✅ | ✅ | ✅ | ✅ | Read after label and role |

---

## Images

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<img alt="text">` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<img alt="">` (decorative) | ✅ | ✅ | ✅ | ✅ | ✅ | Correctly skipped |
| `<img>` without `alt` | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | SRs announce filename or "unlabeled image" |
| `<figure>` + `<figcaption>` | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | figcaption support inconsistent; supplement with aria-labelledby |
| `role="img"` + `aria-label` (SVG) | ✅ | ✅ | ✅ | ✅ | ✅ | Required for informative SVGs |
| SVG without role/label | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | SVG child text nodes may be read individually |
| CSS background images | ❌ | ❌ | ❌ | ❌ | ❌ | Not accessible; never use for informative images |

---

## Tables

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<table>` + `<th>` (column) | ✅ | ✅ | ✅ | ✅ | ✅ | Column headers announced with each cell |
| `<th scope="row">` | ✅ | ✅ | ✅ | ✅ | ✅ | Row headers announced |
| `<th scope="col">` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<caption>` | ✅ | ✅ | ✅ | ✅ | ⚠️ | Announced on table entry |
| `<table>` used for layout | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | Add `role="presentation"` to suppress table semantics |
| `role="grid"` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Grid widget role; different navigation model |

---

## Interactive Content

| Element | JAWS | NVDA | VO macOS | VO iOS | TalkBack | Notes |
|---------|------|------|----------|--------|----------|-------|
| `<details>` + `<summary>` | ⚠️ | ✅ | ✅ | ✅ | ✅ | JAWS support improved in 2023+ |
| `<dialog>` native | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Native HTML `<dialog>` support still maturing |
| `<dialog>` with `aria-modal="true"` | ✅ | ✅ | ✅ | ✅ | ✅ | Better SR support than native |
| `<video>` with `<track kind="captions">` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `<progress>` | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Announces percentage; iOS/Android vary |
| `<meter>` | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | Inconsistent announcements; use `aria-valuenow` etc. |

---

## Key Insights

1. **Native HTML always preferred** over ARIA equivalents — better and more consistent support
2. **VoiceOver + `list-style: none`** — Always add `role="list"` when removing list bullets
3. **`<button>` over `<div role="button">`** — Native buttons get Space key for free; custom buttons need explicit keydown handler
4. **SVG images** — Always add `role="img"` + `aria-label` to informative SVG
5. **Placeholder ≠ label** — Never rely on placeholder as the sole label for an input
6. **`<details>/<summary>`** — Test in JAWS specifically; behavior improved but verify

---

## Resources

- a11ysupport.io — element-by-element support data
- WebAIM Screen Reader User Survey: webaim.org/projects/screenreadersurvey
- HTML Accessibility API Mappings (HTML-AAM): w3.org/TR/html-aam/
