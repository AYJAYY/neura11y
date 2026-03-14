---
title: "HTML Semantics for Accessibility"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["html", "semantics", "headings", "landmarks", "links", "tables", "lists"]
ai_context: "Guide to semantic HTML for accessibility. Covers document structure, headings, landmarks, links, tables, and lists. Load with forms-accessibility.md for complete HTML semantics guidance."
---

# HTML Semantics for Accessibility

Semantic HTML is the foundation of web accessibility. Correct element choice provides structure, meaning, and behavior to assistive technology without requiring ARIA.

---

## Document Structure

### Required Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Page Name — Site Name</title>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <header>
    <nav aria-label="Main">...</nav>
  </header>
  <main id="main-content">
    <h1>Page Title</h1>
    ...
  </main>
  <footer>...</footer>
</body>
</html>
```

### `<html lang>`

The `lang` attribute on `<html>` is required by WCAG SC 3.1.1. It tells screen readers which language engine and pronunciation rules to use.

Valid values: BCP 47 language tags
- `lang="en"` — English
- `lang="en-US"` — American English
- `lang="fr"` — French
- `lang="es"` — Spanish
- `lang="ar"` — Arabic
- `lang="zh-Hans"` — Simplified Chinese

For inline content in a different language: `<span lang="fr">bonjour</span>`

### `<title>`

Required by WCAG SC 2.4.2. Must be:
- Descriptive of the current page content/purpose
- Unique across pages in the site
- Format: "Page Name — Site Name" (most specific first)

Examples:
- `<title>Shopping Cart (3 items) — ACME Store</title>`
- `<title>Contact Us — ACME Corporation</title>`
- `<title>Error: Please correct the form — ACME Store</title>` (update on error)

### Skip Navigation

Required by WCAG SC 2.4.1. Allows keyboard users to bypass repeated navigation.

```html
<!-- Appears as first element in <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- May be visually hidden until focused -->
<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}
.skip-link:focus {
  top: 0;
}
</style>

<!-- Target -->
<main id="main-content" tabindex="-1">
```

Note: `tabindex="-1"` on `<main>` ensures `.focus()` works programmatically in older browsers but doesn't add it to the tab order.

---

## Landmark Regions

HTML5 sectioning elements create landmark regions. Screen reader users navigate by landmarks (not just headings).

| HTML Element | ARIA Role | When to Use |
|---|---|---|
| `<header>` (direct child of body) | `banner` | Site header with logo, primary nav |
| `<nav>` | `navigation` | Navigation links; give unique `aria-label` if multiple |
| `<main>` | `main` | Primary page content; only one per page |
| `<aside>` | `complementary` | Related but non-essential content |
| `<footer>` (direct child of body) | `contentinfo` | Site footer |
| `<section>` (with accessible name) | `region` | Named section; use `aria-labelledby` |
| `<form>` (with accessible name) | `form` | Form container with meaningful name |
| `<search>` | `search` | Search widget or section |

### Multiple Landmarks

When the same landmark type appears more than once, label each one:

```html
<nav aria-label="Main">...</nav>
<nav aria-label="Breadcrumb">...</nav>
<nav aria-label="Pagination">...</nav>
```

For `<section>`:
```html
<section aria-labelledby="features-heading">
  <h2 id="features-heading">Features</h2>
  ...
</section>
```

---

## Heading Hierarchy

Headings provide document structure and enable navigation by screen reader users.

### Rules

1. **One `<h1>` per page** — Usually the page title or main topic
2. **Do not skip levels** — `<h1>` → `<h2>` → `<h3>` is correct; `<h1>` → `<h3>` is a failure
3. **Nest logically** — Headings define an outline; sub-sections go under their parent
4. **Don't use for visual style** — Use CSS classes if you want a smaller heading style; don't use `<h4>` just because it's visually smaller
5. **Heading text must be descriptive** — "Section 3" is not descriptive; "Contact Information" is

### Example Outline

```
h1: Product Documentation
  h2: Getting Started
    h3: Installation
    h3: Configuration
  h2: API Reference
    h3: Authentication
    h3: Endpoints
      h4: GET /users
      h4: POST /users
```

### Common Failures

- Using `<div class="heading">` instead of `<h2>` (fails SC 1.3.1)
- Multiple `<h1>` elements (confusing, not technically a WCAG failure but poor practice)
- Skipping from `<h1>` to `<h3>` (AT may warn users of "missing" level)
- `<h1>` inside `<nav>` (nav labels should use `aria-label`, not `<h1>`)

---

## Links

### Link Text Rules

WCAG SC 2.4.4 requires link purpose to be determinable from text alone or context.

**Failing patterns:**
- `<a href="...">Click here</a>`
- `<a href="...">Read more</a>`
- `<a href="...">Download</a>` (without identifying what)

**Passing patterns:**
- `<a href="...">2024 Annual Report</a>`
- `<a href="...">Learn more about our accessibility policy</a>`
- Context-sufficient: `<p>See our <a href="...">accessibility policy</a> for details.</p>`

### Link vs. Button

| Use `<a href>` for... | Use `<button>` for... |
|---|---|
| Navigation to another page or location | Actions (submit, open modal, toggle, delete) |
| Navigation within same page (`href="#section"`) | Form submission |
| Downloading a file | Menu activation |

Do not use `<a>` without `href` as a button. Do not use `<button>` for navigation.

### External Links

Warn users when links open in a new tab/window:
```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  ACME Documentation
  <span class="sr-only">(opens in new tab)</span>
</a>
```

Or use an icon with alt text:
```html
<a href="https://example.com" target="_blank" rel="noopener">
  ACME Documentation
  <img src="external.svg" alt=" (opens in new tab)">
</a>
```

---

## Lists

Use semantic list elements to convey grouped items.

| List Type | Element | When to Use |
|---|---|---|
| Unordered | `<ul>` | Items without meaningful order |
| Ordered | `<ol>` | Items with sequence (steps, rankings) |
| Description | `<dl>` | Term-definition pairs |

### Rules

- Always use `<li>` as direct children of `<ul>` and `<ol>`
- Do not use `<li>` outside a list element
- Don't use CSS `list-style: none` without `role="list"` — some screen readers stop announcing list semantics when visual list styling is removed

```html
<!-- Unordered list -->
<ul>
  <li>Item one</li>
  <li>Item two</li>
</ul>

<!-- Ordered steps -->
<ol>
  <li>Open the application</li>
  <li>Click Settings</li>
  <li>Select Accessibility</li>
</ol>

<!-- Description list -->
<dl>
  <dt>WCAG</dt>
  <dd>Web Content Accessibility Guidelines</dd>
  <dt>ARIA</dt>
  <dd>Accessible Rich Internet Applications</dd>
</dl>
```

---

## Tables

Data tables must have headers. Layout tables must either be marked as `role="presentation"` or use `<table>` with no header markup.

### Simple Table

```html
<table>
  <caption>Q1 Sales by Region</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">January</th>
      <th scope="col">February</th>
      <th scope="col">March</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North</th>
      <td>$12,000</td>
      <td>$13,500</td>
      <td>$11,200</td>
    </tr>
  </tbody>
</table>
```

### `scope` values

- `scope="col"` — Header applies to cells below it in the same column
- `scope="row"` — Header applies to cells to the right in the same row
- `scope="colgroup"` — Header spans multiple columns
- `scope="rowgroup"` — Header spans multiple rows

### Complex Tables

For tables with irregular header structure:

```html
<table>
  <caption>Course Schedule</caption>
  <tr>
    <th id="time">Time</th>
    <th id="mon">Monday</th>
    <th id="tue">Tuesday</th>
  </tr>
  <tr>
    <th id="nine" headers="time">9:00 AM</th>
    <td headers="mon nine">Math</td>
    <td headers="tue nine">English</td>
  </tr>
</table>
```

Use `id` on `<th>` and `headers` on `<td>` for irregular tables.

### `<caption>`

The `<caption>` element provides an accessible name for the table. Required for data tables without another accessible name.

---

## Interactive Elements: Native vs. Custom

Always prefer native HTML elements. They provide keyboard interaction, AT semantics, and operating system integration for free.

| Needed Behavior | Use | Never use |
|---|---|---|
| Button | `<button>` | `<div onclick>`, `<span onclick>` |
| Text input | `<input type="text">` | `<div contenteditable>` |
| Checkbox | `<input type="checkbox">` | `<div role="checkbox">` (unless unavoidable) |
| Select menu | `<select>` | Custom select (only if required by design) |
| Form submission | `<button type="submit">` or `<input type="submit">` | `<a href="#">Submit</a>` |
| Link | `<a href="...">` | `<span onclick="navigate()">` |

If you must use a custom interactive element, you need to add:
1. Appropriate `role` attribute
2. `tabindex="0"` (to add to tab order)
3. Keyboard event handlers (Enter, Space, Arrow keys as appropriate)
4. ARIA states (`aria-expanded`, `aria-checked`, etc.)
5. Accessible name (`aria-label` or visible text)

---

## Language of Parts (SC 3.1.2)

Mark passages in a different language:

```html
<p>The French word for accessibility is
  <span lang="fr">accessibilité</span>.
</p>

<blockquote lang="de">
  <p>Zugänglichkeit ist ein Grundrecht.</p>
</blockquote>
```

Exceptions: proper nouns, technical terms, and words of indeterminate language don't need `lang` attributes.

---

## Reading Order (SC 1.3.2)

The DOM order must match the logical reading order. Screen readers and CSS-independent users consume content in DOM order.

**Problematic patterns:**

CSS `order` property or `flex`/`grid` reordering that changes visual order without matching DOM order:
```css
/* PROBLEMATIC: Visual order differs from DOM order */
.sidebar { order: -1; } /* sidebar appears first visually but last in DOM */
```

**Fix:** Match DOM order to reading order. Use CSS to adjust position, not logical order.

Exception: purely decorative elements (icons, background images) may be positioned anywhere without affecting reading order.
