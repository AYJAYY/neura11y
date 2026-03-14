---
title: "Common ARIA Mistakes"
standard: "WAI-ARIA 1.2"
source_url: ""
domain: ["web"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["aria", "mistakes", "anti-patterns", "audit", "errors"]
ai_context: "Curated list of the 20 most common ARIA implementation errors found in accessibility audits. Use when reviewing or generating ARIA markup to avoid these patterns."
---

# Common ARIA Mistakes

The most common ARIA implementation errors found in production audits. Organized by category. Each entry includes the incorrect pattern, the correct fix, and the WCAG SC violated.

---

## Rule 0: The First Rule of ARIA Use

**Before using ARIA, check if a native HTML element does the job.**

Do not use: `<div role="button" onclick="...">Click me</div>`
Use instead: `<button type="button">Click me</button>`

Native HTML provides semantics, keyboard handling, and AT support without additional code. ARIA overrides or supplements native semantics; it never exceeds them. Every div/span with a role requires manual implementation of all keyboard interaction that HTML provides for free.

**WCAG reference:** SC 4.1.2 (Name, Role, Value); Technique H91

---

## Mistake 1: aria-hidden on Focusable Elements

**Problem:** Applying `aria-hidden="true"` to an element that can receive keyboard focus.

```html
<!-- WRONG: Icon button hidden from AT but still focusable -->
<button aria-hidden="true">
  <svg>...</svg>
</button>

<!-- WRONG: Entire navigation hidden but links are focusable -->
<nav aria-hidden="true">
  <a href="/about">About</a>
</nav>
```

**Fix:** Never set `aria-hidden="true"` on focusable elements or elements containing focusable children. If the element should be hidden from AT, also ensure it cannot receive focus (`tabindex="-1"` or `display:none`).

```html
<!-- CORRECT: Decorative icon with empty alt -->
<button>
  <svg aria-hidden="true" focusable="false">...</svg>
  <span class="sr-only">Close dialog</span>
</button>
```

**WCAG SC:** 1.3.1, 4.1.2; also creates keyboard trap (SC 2.1.2)

---

## Mistake 2: Missing Accessible Name

**Problem:** Interactive or informative elements without an accessible name.

```html
<!-- WRONG: Icon button with no label -->
<button><svg><path d="..."/></svg></button>

<!-- WRONG: Input with no label -->
<input type="search" placeholder="Search...">

<!-- WRONG: Image with no alt -->
<img src="logo.png">
```

**Fix:**
```html
<!-- Use aria-label, aria-labelledby, or visually hidden text -->
<button aria-label="Close dialog"><svg aria-hidden="true">...</svg></button>

<!-- Proper label for input -->
<label for="search">Search</label>
<input id="search" type="search">

<!-- Descriptive alt -->
<img src="logo.png" alt="Acme Corporation">
```

**WCAG SC:** 4.1.2 (Name, Role, Value); SC 1.1.1 for images

---

## Mistake 3: aria-label on Non-Interactive Elements

**Problem:** Using `aria-label` on non-interactive, non-landmark elements.

```html
<!-- WRONG: aria-label on a div with no role -->
<div aria-label="Product description">...</div>

<!-- WRONG: aria-label on a paragraph -->
<p aria-label="Note">This is a note.</p>
```

`aria-label` is only valid on interactive elements, landmark elements, or elements with a role that permits naming. On generic elements like `<div>` and `<p>`, it is ignored by most AT.

**Fix:** Use a heading, visible label, or assign a landmark role if naming is needed.

```html
<!-- Use a heading for sections -->
<section aria-labelledby="desc-heading">
  <h2 id="desc-heading">Product Description</h2>
  ...
</section>
```

---

## Mistake 4: Redundant ARIA Roles

**Problem:** Adding ARIA roles that duplicate the native HTML element's implicit role.

```html
<!-- WRONG: <button> already has role="button" -->
<button role="button">Submit</button>

<!-- WRONG: <nav> already has role="navigation" -->
<nav role="navigation">...</nav>

<!-- WRONG: <main> already has role="main" -->
<main role="main">...</main>
```

**Fix:** Remove redundant `role` attributes. Use native HTML elements.

**Why it matters:** Redundant roles are harmless but indicate misunderstanding of ARIA; more problematic patterns often accompany them.

---

## Mistake 5: Missing aria-expanded on Disclosure Widgets

**Problem:** Interactive controls that open/close content without communicating state to AT.

```html
<!-- WRONG: Button that toggles a menu but doesn't communicate state -->
<button onclick="toggleMenu()">Menu</button>
<ul id="menu" hidden>...</ul>
```

**Fix:** Add `aria-expanded` and toggle it with JavaScript.

```html
<button aria-expanded="false" aria-controls="menu" onclick="toggleMenu(this)">Menu</button>
<ul id="menu" hidden>...</ul>

<script>
function toggleMenu(btn) {
  const expanded = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', String(!expanded));
  document.getElementById('menu').hidden = expanded;
}
</script>
```

**WCAG SC:** 4.1.2 (Name, Role, Value) — state not communicated

---

## Mistake 6: Using aria-describedby Instead of aria-labelledby for Names

**Problem:** Confusing the accessible name (what an element is) with the accessible description (additional context).

```html
<!-- WRONG: This sets description, not name; icon button still unnamed -->
<button aria-describedby="btn-desc">
  <svg aria-hidden="true">...</svg>
</button>
<span id="btn-desc">Delete this item</span>
```

**Fix:** Use `aria-labelledby` (or `aria-label`) for the accessible name; use `aria-describedby` for supplementary description.

```html
<!-- CORRECT: aria-labelledby provides the name -->
<button aria-labelledby="btn-label">
  <svg aria-hidden="true">...</svg>
</button>
<span id="btn-label" class="sr-only">Delete this item</span>

<!-- OR: Use aria-label directly -->
<button aria-label="Delete this item">
  <svg aria-hidden="true">...</svg>
</button>
```

---

## Mistake 7: aria-label Conflicts with Visible Label (Label in Name Failure)

**Problem:** The `aria-label` or `aria-labelledby` value does not include the visible label text.

```html
<!-- WRONG: Visible text is "Submit" but aria-label is "Send form" -->
<!-- Voice control users saying "Submit" won't activate this button -->
<button aria-label="Send form">Submit</button>
```

**Fix:** Accessible name must contain (start with, or include) the visible text.

```html
<!-- CORRECT: aria-label starts with visible text -->
<button aria-label="Submit registration form">Submit</button>

<!-- BEST: Let the button text be the accessible name -->
<button>Submit</button>
```

**WCAG SC:** 2.5.3 (Label in Name)

---

## Mistake 8: Using tabindex > 0

**Problem:** Positive tabindex values override the natural tab order.

```html
<!-- WRONG: Creates unpredictable tab order -->
<a href="/" tabindex="3">Home</a>
<a href="/about" tabindex="1">About</a>
<a href="/contact" tabindex="2">Contact</a>
```

Positive tabindex creates a custom tab sequence that jumps to those elements first (in ascending order), then returns to the document order. This is almost always wrong and confusing.

**Fix:** Use `tabindex="0"` to add custom elements to the tab order, and fix DOM order instead of using positive values.

**Exception:** `tabindex="-1"` is valid and common — removes element from tab order but allows programmatic focus.

**WCAG SC:** 2.4.3 (Focus Order)

---

## Mistake 9: role="presentation" or role="none" on Interactive Elements

**Problem:** Using role="presentation" (or its synonym role="none") on elements that should be interactive or that have children with semantic meaning.

```html
<!-- WRONG: Removes semantics from a table with data -->
<table role="presentation">
  <tr><th>Name</th><th>Score</th></tr>
  <tr><td>Alice</td><td>95</td></tr>
</table>

<!-- WRONG: Image that conveys information -->
<img src="warning.png" role="presentation" alt="">
```

`role="presentation"` is valid only for purely layout tables and truly decorative images.

**Fix:** Only use on elements that have no semantic value (layout tables, spacer images, decorative icons).

---

## Mistake 10: Missing Required Owned Elements

**Problem:** ARIA composite roles require specific child roles (owned elements). Missing them breaks AT output.

```html
<!-- WRONG: listbox without option children -->
<ul role="listbox">
  <li>Apple</li>  <!-- must be role="option" -->
  <li>Banana</li>
</ul>

<!-- WRONG: tablist without tab children -->
<div role="tablist">
  <button>Tab 1</button>  <!-- must be role="tab" -->
</div>
```

**Required parent → child relationships:**
- `listbox` → `option`
- `tablist` → `tab`
- `tab` → `tabpanel` (controlled via aria-controls)
- `tree` → `treeitem`
- `treegrid` → `row` → `gridcell` or `rowheader` / `columnheader`
- `grid` → `row` → `gridcell`
- `radiogroup` → `radio`
- `menu` or `menubar` → `menuitem`, `menuitemcheckbox`, or `menuitemradio`

---

## Mistake 11: aria-live="assertive" for Non-Critical Updates

**Problem:** Using `assertive` for every live region, interrupting AT users constantly.

```html
<!-- WRONG: Assertive for routine status updates -->
<div aria-live="assertive" id="status"></div>
<!-- When search results load: "Showing 42 results" — interrupts reading -->
```

`assertive` interrupts the current AT announcement, which is highly disruptive.

**Fix:** Default to `polite`. Use `assertive` only for errors that require immediate attention.

```html
<!-- CORRECT: polite for status updates -->
<div role="status" aria-live="polite" id="status"></div>

<!-- CORRECT: assertive only for errors -->
<div role="alert" aria-live="assertive" id="error"></div>
```

---

## Mistake 12: Modal Without aria-modal="true"

**Problem:** Dialog opened without `aria-modal="true"`, allowing AT to browse background content.

```html
<!-- WRONG: Dialog without aria-modal -->
<div role="dialog" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Delete</h2>
  ...
</div>
```

**Fix:**
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Delete</h2>
  ...
</div>
```

Also required: trap focus within modal, send focus to first focusable element when opened, restore focus to trigger element on close, close on Escape key.

**Note:** `aria-modal` alone does not prevent background interaction — must also use `inert` attribute or ARIA-hide background content.

---

## Mistake 13: Injecting aria-live Region Dynamically

**Problem:** Creating the live region element at the same time as inserting content.

```html
<!-- WRONG: AT doesn't register the live region before content is inserted -->
<script>
  const div = document.createElement('div');
  div.setAttribute('aria-live', 'polite');
  div.textContent = 'Form submitted successfully';
  document.body.appendChild(div);
</script>
```

**Fix:** Live regions must be present in the DOM on page load, empty, before content is inserted.

```html
<!-- HTML on page load -->
<div id="status" role="status" aria-live="polite"></div>

<!-- Later, via JS: only insert the message -->
<script>
  document.getElementById('status').textContent = 'Form submitted successfully';
</script>
```

---

## Mistake 14: aria-labelledby Pointing to Hidden Element

**Problem:** `aria-labelledby` references an element that is visually or programmatically hidden.

```html
<!-- WRONG: Label is visually hidden with display:none -->
<span id="my-label" style="display:none">Search</span>
<input aria-labelledby="my-label" type="text">
```

Elements hidden with `display:none` or `visibility:hidden` are not in the accessibility tree. `aria-labelledby` cannot reference them.

**Fix:** Use `visibility: visible` with `clip` technique for visually hidden but AT-accessible text, or use `aria-label` directly.

```html
<!-- Visually hidden but accessible to AT -->
<span id="my-label" class="sr-only">Search</span>
<input aria-labelledby="my-label" type="text">

/* CSS */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}
```

---

## Mistake 15: Using placeholder as Label

**Problem:** Relying on `placeholder` attribute instead of a proper label.

```html
<!-- WRONG: No label, only placeholder -->
<input type="email" placeholder="Email address">
```

Placeholder text: disappears when user types, often insufficient contrast (SC 1.4.3), not announced by all AT as a label, not shown on focus in some browsers.

**Fix:** Always use a `<label>` element.

```html
<label for="email">Email address</label>
<input id="email" type="email" placeholder="you@example.com">
```

**WCAG SC:** 3.3.2 (Labels or Instructions), 1.4.3 (Contrast)

---

## Mistake 16: Incorrect aria-controls Reference

**Problem:** `aria-controls` pointing to a non-existent ID.

```html
<!-- WRONG: aria-controls references "dropdown-menu" but element has id="menu" -->
<button aria-expanded="false" aria-controls="dropdown-menu">Products</button>
<ul id="menu">...</ul>
```

**Fix:** Ensure IDs match exactly. Validate with automated tools that check ID references.

---

## Mistake 17: Missing aria-haspopup on Combobox Triggers

**Problem:** Input or button that opens a popup list without communicating this to AT.

```html
<!-- WRONG: Input opens autocomplete list but doesn't tell AT -->
<input type="text" id="city" aria-autocomplete="list">
<ul role="listbox">...</ul>
```

**Fix:**
```html
<input type="text" id="city"
       role="combobox"
       aria-expanded="false"
       aria-autocomplete="list"
       aria-haspopup="listbox"
       aria-controls="city-list">
<ul id="city-list" role="listbox">...</ul>
```

---

## Mistake 18: Using role="button" Without Keyboard Handler

**Problem:** Custom button role without Enter/Space key activation.

```html
<!-- WRONG: role="button" but only onclick handler, no keydown -->
<div role="button" tabindex="0" onclick="doAction()">Click me</div>
```

**Fix:** Add keyboard event handler. Prefer `<button>` element.

```html
<div role="button" tabindex="0"
     onclick="doAction()"
     onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();doAction();}">
  Click me
</div>

<!-- Better: just use a button -->
<button onclick="doAction()">Click me</button>
```

**WCAG SC:** 2.1.1 (Keyboard)

---

## Mistake 19: Landmark Role Soup

**Problem:** Overusing landmark roles, creating navigation noise for screen reader users who use landmark navigation.

```html
<!-- WRONG: Every section is a navigation landmark -->
<nav>Main navigation</nav>
<nav>Breadcrumb navigation</nav>
<nav>Pagination</nav>
<nav>Social media links</nav>
<nav>Footer links</nav>
```

With 5 navigation landmarks, screen reader users see "navigation, navigation, navigation..." with no way to distinguish them.

**Fix:** Limit landmarks to meaningful regions. Label multiple landmarks of the same type.

```html
<nav aria-label="Main">...</nav>
<nav aria-label="Breadcrumb">...</nav>
<nav aria-label="Pagination">...</nav>
<!-- Social media links in footer, not a separate nav -->
```

---

## Mistake 20: Not Testing with Actual Screen Readers

**Problem:** Relying only on automated tools (axe, WAVE, Lighthouse) for ARIA validation.

Automated tools catch ~30-40% of WCAG issues. ARIA errors that automated tools miss:
- Illogical reading order
- Poor accessible name quality (technically present but unhelpful)
- Live region timing issues
- Focus management that fails in practice
- Component keyboard patterns that don't match APG expectations

**Fix:** Test with NVDA + Chrome and VoiceOver + Safari (minimum). Use keyboard-only navigation testing for every interactive feature.

---

## Quick Reference: ARIA Attribute Rules

| If you want to... | Use |
|---|---|
| Name an element (no visible label) | `aria-label` |
| Name an element (using visible text) | `aria-labelledby="id-of-text"` |
| Add supplementary description | `aria-describedby="id-of-desc"` |
| Hide decorative content from AT | `aria-hidden="true"` (on non-focusable elements only) |
| Indicate expanded/collapsed state | `aria-expanded="true/false"` |
| Indicate checked/selected state | `aria-checked`, `aria-selected`, `aria-pressed` |
| Indicate invalid input | `aria-invalid="true"` + `aria-errormessage="id"` |
| Create live region | `aria-live="polite"` or `role="status"` / `role="alert"` |
| Define custom role | `role="[rolename]"` |
| Mark required field (custom control) | `aria-required="true"` |
| Indicate disabled state (keep in AT) | `aria-disabled="true"` |
