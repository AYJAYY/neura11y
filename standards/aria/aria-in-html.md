---
title: "ARIA in HTML — Implicit Semantics and Allowed Overrides"
standard: "ARIA in HTML"
source_url: "https://www.w3.org/TR/html-aria/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["aria", "html", "implicit-role", "native-semantics", "allowed-aria"]
ai_context: "Defines which ARIA roles and attributes are allowed on HTML elements, and HTML elements' implicit ARIA roles. Use to avoid redundant or conflicting ARIA markup."
---

# ARIA in HTML

Specification: https://www.w3.org/TR/html-aria/ (W3C Recommendation)

Defines the relationship between HTML elements and WAI-ARIA roles, states, and properties. Specifies which ARIA attributes may be used on which HTML elements.

---

## The 5 Rules of ARIA Use

From the WAI-ARIA spec, in priority order:

1. **Use native HTML** — If a native HTML element or attribute provides the semantics and behavior you require, use it rather than repurposing an element with ARIA.

2. **Don't change native semantics unless essential** — Do not change the native semantics of an element unless you have no other choice. `<h2 role="tab">` is invalid.

3. **All interactive ARIA controls must be usable with the keyboard** — If you add a widget role, implement all required keyboard interactions.

4. **Don't use role="presentation" or aria-hidden="true" on focusable elements** — This removes semantics while leaving the element in the tab order, creating confusion.

5. **All interactive elements must have an accessible name** — Every control that users interact with must have a name communicated to AT.

---

## HTML Elements — Implicit ARIA Roles

The implicit role is the role the element has by default, without any ARIA. Do NOT add `role=` when it matches the implicit role.

### Document Structure

| HTML Element | Conditions | Implicit Role |
|---|---|---|
| `<article>` | — | `article` |
| `<aside>` | — | `complementary` |
| `<body>` | — | `generic` |
| `<caption>` | — | `caption` |
| `<col>` | — | no corresponding role |
| `<colgroup>` | — | no corresponding role |
| `<datalist>` | — | `listbox` |
| `<details>` | — | `group` |
| `<dialog>` | — | `dialog` |
| `<div>` | — | `generic` |
| `<fieldset>` | — | `group` |
| `<figure>` | — | `figure` |
| `<footer>` | within `<body>` or main landmark | `contentinfo` |
| `<footer>` | within `<article>`, `<aside>`, `<main>`, `<nav>`, `<section>` | `generic` |
| `<form>` | has accessible name | `form` |
| `<form>` | no accessible name | `generic` |
| `<h1>` — `<h6>` | — | `heading` (level 1–6) |
| `<header>` | within `<body>` or main landmark | `banner` |
| `<header>` | within sectioning content | `generic` |
| `<hr>` | — | `separator` |
| `<html>` | — | `document` |
| `<li>` | within `<ol>` or `<ul>` | `listitem` |
| `<li>` | not within `<ol>` or `<ul>` | `generic` |
| `<main>` | — | `main` |
| `<math>` | — | `math` |
| `<menu>` | — | `list` |
| `<nav>` | — | `navigation` |
| `<ol>` | — | `list` |
| `<p>` | — | `paragraph` |
| `<search>` | — | `search` |
| `<section>` | has accessible name | `region` |
| `<section>` | no accessible name | `generic` |
| `<span>` | — | `generic` |
| `<summary>` | first child of `<details>` | `button` |
| `<table>` | — | `table` |
| `<tbody>` | — | `rowgroup` |
| `<td>` | within `<table>` | `cell` |
| `<tfoot>` | — | `rowgroup` |
| `<th>` | in column | `columnheader` |
| `<th>` | in row | `rowheader` |
| `<thead>` | — | `rowgroup` |
| `<tr>` | — | `row` |
| `<ul>` | — | `list` |

### Interactive Elements

| HTML Element | Conditions | Implicit Role |
|---|---|---|
| `<a>` | with `href` | `link` |
| `<a>` | without `href` | `generic` |
| `<button>` | — | `button` |
| `<input type="button">` | — | `button` |
| `<input type="checkbox">` | — | `checkbox` |
| `<input type="color">` | — | no corresponding role |
| `<input type="date">` | — | no corresponding role |
| `<input type="datetime-local">` | — | no corresponding role |
| `<input type="email">` | no list attribute | `textbox` |
| `<input type="email">` | with list attribute | `combobox` |
| `<input type="file">` | — | no corresponding role |
| `<input type="hidden">` | — | no corresponding role |
| `<input type="image">` | — | `button` |
| `<input type="month">` | — | no corresponding role |
| `<input type="number">` | — | `spinbutton` |
| `<input type="password">` | — | no corresponding role |
| `<input type="radio">` | — | `radio` |
| `<input type="range">` | — | `slider` |
| `<input type="reset">` | — | `button` |
| `<input type="search">` | no list attribute | `searchbox` |
| `<input type="search">` | with list attribute | `combobox` |
| `<input type="submit">` | — | `button` |
| `<input type="tel">` | no list attribute | `textbox` |
| `<input type="tel">` | with list attribute | `combobox` |
| `<input type="text">` | no list attribute | `textbox` |
| `<input type="text">` | with list attribute | `combobox` |
| `<input type="time">` | — | no corresponding role |
| `<input type="url">` | no list attribute | `textbox` |
| `<input type="url">` | with list attribute | `combobox` |
| `<input type="week">` | — | no corresponding role |
| `<meter>` | — | `meter` |
| `<option>` | — | `option` |
| `<output>` | — | `status` |
| `<progress>` | — | `progressbar` |
| `<select>` | no `multiple` and no `size > 1` | `combobox` |
| `<select>` | with `multiple` or `size > 1` | `listbox` |
| `<textarea>` | — | `textbox` |

### Media and Embedded Elements

| HTML Element | Conditions | Implicit Role |
|---|---|---|
| `<audio>` | — | no corresponding role |
| `<canvas>` | — | no corresponding role |
| `<embed>` | — | no corresponding role |
| `<iframe>` | — | no corresponding role |
| `<img>` | non-empty alt | `img` |
| `<img>` | empty alt (`alt=""`) | `presentation` / `none` |
| `<img>` | no alt attribute | `img` (with warning) |
| `<map>` | — | no corresponding role |
| `<object>` | — | no corresponding role |
| `<picture>` | — | no corresponding role |
| `<svg>` | — | `img` (depends on content) |
| `<video>` | — | no corresponding role |

---

## Allowed ARIA Roles by HTML Element

When an ARIA `role` conflicts with or duplicates the native semantics, it is prohibited or redundant. These are the allowed role overrides:

### Elements Where role Is Prohibited

Do not add ANY `role` to these elements (native semantics cannot be meaningfully overridden):

- `<caption>`
- `<col>`, `<colgroup>`
- `<dd>`, `<dt>`
- `<dfn>`
- `<html>`
- `<link>` (in head)
- `<meta>`
- `<noscript>`
- `<script>`
- `<select>` (role can only be `combobox` or `listbox`, matching native)
- `<style>`
- `<title>`

### Common Allowed Overrides

| Element | Allowed Roles (in addition to default) |
|---------|----------------------------------------|
| `<a href>` | `button`, `checkbox`, `menuitem`, `menuitemcheckbox`, `menuitemradio`, `option`, `radio`, `switch`, `tab`, `treeitem` |
| `<article>` | `application`, `document`, `feed`, `main`, `none`, `presentation`, `region` |
| `<aside>` | `feed`, `none`, `note`, `presentation`, `region`, `search` |
| `<button>` | `checkbox`, `combobox`, `link`, `menuitem`, `menuitemcheckbox`, `menuitemradio`, `option`, `radio`, `switch`, `tab` |
| `<div>` | Any role |
| `<footer>` | `contentinfo`, `generic`, `group`, `none`, `presentation` |
| `<header>` | `banner`, `generic`, `group`, `none`, `presentation` |
| `<img>` (with alt) | `button`, `checkbox`, `listitem`, `menuitem`, `menuitemcheckbox`, `menuitemradio`, `meter`, `none`, `option`, `presentation`, `progressbar`, `radio`, `scrollbar`, `separator`, `slider`, `switch`, `tab`, `treeitem` |
| `<input type="checkbox">` | `menuitemcheckbox`, `option`, `switch` |
| `<input type="radio">` | `menuitemradio` |
| `<li>` | `menuitem`, `menuitemcheckbox`, `menuitemradio`, `none`, `option`, `presentation`, `radio`, `separator`, `tab`, `treeitem` |
| `<nav>` | `menu`, `menubar`, `none`, `presentation`, `tablist` |
| `<ol>`, `<ul>` | `group`, `listbox`, `menu`, `menubar`, `none`, `presentation`, `radiogroup`, `tablist`, `toolbar`, `tree` |
| `<section>` | `alert`, `alertdialog`, `application`, `banner`, `complementary`, `contentinfo`, `dialog`, `document`, `feed`, `log`, `main`, `marquee`, `navigation`, `none`, `note`, `presentation`, `search`, `status`, `tabpanel` |
| `<span>` | Any role |
| `<table>` | `any` |
| `<td>` | `cell`, `gridcell`, `columnheader`, `rowheader` |

---

## Global ARIA Attributes

These attributes are valid on any HTML element that can have an accessible role:

- `aria-atomic`
- `aria-busy`
- `aria-controls`
- `aria-current`
- `aria-describedby`
- `aria-description`
- `aria-details`
- `aria-disabled`
- `aria-dropeffect` (deprecated)
- `aria-errormessage`
- `aria-flowto`
- `aria-grabbed` (deprecated)
- `aria-haspopup`
- `aria-hidden`
- `aria-invalid`
- `aria-keyshortcuts`
- `aria-label`
- `aria-labelledby`
- `aria-live`
- `aria-owns`
- `aria-relevant`
- `aria-roledescription`

---

## Common Mistakes This Document Prevents

1. Adding `role="navigation"` to `<nav>` (redundant)
2. Adding `role="main"` to `<main>` (redundant)
3. Adding `role="button"` to `<button>` (redundant)
4. Adding `role="heading"` + `aria-level` to `<h2>` (redundant)
5. Using `role="list"` on `<div>` instead of `<ul>` (use native HTML)
6. Adding `aria-label` to `<p>` (not valid; no role that supports naming)
7. Using `role="contentinfo"` on `<footer>` within an `<article>` (footer in sectioning context has generic role)
8. Adding `role="img"` to `<img>` (redundant)
