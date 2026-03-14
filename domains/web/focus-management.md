---
title: "Focus Management"
standard: "WCAG"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["focus", "keyboard", "tabindex", "focus-trap", "focus-visible", "skip-nav", "1.4.11", "2.4.11", "2.4.13"]
ai_context: "Focus management patterns for web applications. Covers focus order, visible focus indicators, focus obscuration, focus trapping in modals, and programmatic focus. Critical for modal dialogs and SPAs."
---

# Focus Management

---

## What is Focus?

Keyboard focus is the browser state indicating which interactive element will receive keyboard input. Only one element has focus at a time. The focused element is the current point of interaction for keyboard and AT users.

**WCAG success criteria for focus:**
- SC 2.1.1 — All functionality keyboard accessible
- SC 2.1.2 — No keyboard traps
- SC 2.4.3 — Logical focus order
- SC 2.4.7 — Focus visible (some indicator required)
- SC 1.4.11 — Non-text contrast for focus indicators [WCAG]
- SC 2.4.11 — Focus not obscured (minimum) [WCAG 2.2]
- SC 2.4.12 — Focus not obscured (enhanced) [WCAG 2.2]
- SC 2.4.13 — Focus appearance [WCAG 2.2 AAA]

---

## What is Focusable?

Elements that receive focus by default (without `tabindex`):
- `<a href="...">`
- `<button>`
- `<input>` (all types except `type="hidden"`)
- `<select>`
- `<textarea>`
- `<summary>` (first child of `<details>`)
- Elements with `tabindex="0"`

Elements that do NOT receive focus by default:
- `<div>`, `<span>`, `<p>`, `<h1>–<h6>` — static elements
- `<a>` without `href`
- `<button disabled>` (disabled controls are removed from tab order)

---

## tabindex Values

### tabindex="0"

Adds a custom element to the natural tab order at its DOM position.

Use when: Creating a custom interactive widget (custom button, custom toggle) from a non-interactive element.

```html
<div role="button" tabindex="0" onclick="doAction()"
     onkeydown="if(e.key==='Enter'||e.key===' ')doAction()">
  Action
</div>
```

### tabindex="-1"

Removes element from tab order but allows programmatic focus via `.focus()`.

Use when: Creating a focus target that should not be tabbed to naturally (modal container, alert region, route heading in SPA, custom widget items managed by arrow keys).

```html
<div id="modal" role="dialog" aria-modal="true" tabindex="-1">
  ...
</div>
// When opening:
document.getElementById('modal').focus();
```

### tabindex > 0 (Positive Values)

**NEVER use.** Positive tabindex creates a parallel tab sequence (elements with positive tabindex are tabbed first, in ascending order, before natural tab order). This is almost always wrong and violates SC 2.4.3.

---

## Visible Focus Indicators

WCAG focus-indicator requirements span multiple criteria.

### SC 2.4.7 (AA — WCAG 2.1+)

Some focus indicator must be visible. Browser default outlines satisfy this.

### SC 1.4.11 (AA — WCAG)

Focus indicators, as visual UI-state indicators, need at least 3:1 contrast against adjacent colors.

### SC 2.4.13 (AAA — WCAG 2.2)

The focus indicator must meet ALL of:
1. **Area:** ≥ perimeter of unfocused component × 2 CSS pixels
2. **Contrast:** ≥ 3:1 between the same pixels in the focused and unfocused states

### Never Do This

```css
/* NEVER remove focus outline without replacement */
*:focus { outline: none; }
*:focus { outline: 0; }
```

This fails SC 2.4.7, SC 1.4.11, and, if you are targeting AAA, SC 2.4.13.

### Accessible Focus Style Pattern

```css
/* Visible focus for keyboard users only */
:focus-visible {
  outline: 3px solid #005fcc;
  outline-offset: 2px;
  border-radius: 2px;
}

/* Remove outline for mouse users (only if you also have :focus-visible support) */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Calculating Minimum Focus Area

For a 100px × 30px button:
- Perimeter = (100 + 30) × 2 = 260 CSS pixels
- Minimum focus area = 260 × 2 = 520 CSS square pixels
- A 2px solid outline on this button = approximately 2 × 260 = 520 CSS pixels of focus area (passes minimum)
- A 3px outline provides 780 CSS pixels (exceeds minimum)

### Focus Contrast Requirements

The focus indicator color must have 3:1 contrast ratio between:
- Focused state color AND
- Unfocused state color (or adjacent background color if indicator doesn't change between states)

Example: If focus outline is `#005fcc` (dark blue) against a white button background:
- Blue `#005fcc` contrast vs white `#ffffff` = approximately 8.6:1 ✓

---

## Focus Order (SC 2.4.3)

Focus must follow a logical sequence that preserves meaning and operation. "Logical" means the order makes sense for the content — typically top-to-bottom, left-to-right for LTR languages.

### DOM Order

The default tab order follows DOM order. Ensure DOM order matches visual/logical reading order.

```html
<!-- CORRECT: DOM order matches visual order -->
<header>...</header>
<nav>...</nav>
<main>
  <h1>...</h1>
  <article>...</article>
</main>
<footer>...</footer>
```

### Disrupted Focus Order (Common Bugs)

```css
/* PROBLEMATIC: Visual order differs from DOM/tab order */
.container { display: flex; }
.sidebar { order: -1; } /* Appears first visually, but last in DOM */
```

Users Tab through content in DOM order, but visually see a different order. Fix: reorder DOM to match visual order.

---

## Focus Trapping (Modals)

When a modal dialog is open, keyboard focus must be confined to the modal. This is an intentional focus trap for the duration of the dialog and is not a failure of SC 2.1.2 when users can dismiss the dialog and return to the rest of the page with keyboard alone.

### Modal Focus Requirements

1. When modal opens: move focus to modal container or first focusable element inside
2. Tab and Shift+Tab cycle through focusable elements within the modal only
3. Focus cannot leave the modal by tabbing
4. Escape key closes the modal
5. When modal closes: return focus to the element that triggered the modal

### Focus Trap Implementation

```javascript
function trapFocus(modal) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstFocusable = focusableElements[0];
  const lastFocusable = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', function(e) {
    if (e.key !== 'Tab') return;

    if (e.shiftKey) {
      // Shift+Tab: if on first element, wrap to last
      if (document.activeElement === firstFocusable) {
        lastFocusable.focus();
        e.preventDefault();
      }
    } else {
      // Tab: if on last element, wrap to first
      if (document.activeElement === lastFocusable) {
        firstFocusable.focus();
        e.preventDefault();
      }
    }
  });
}
```

### Libraries for Focus Trapping

- `focus-trap` npm package
- Angular CDK FocusTrap
- React: `@radix-ui/react-focus-scope`, `@headlessui/react` Dialog

---

## Skip Navigation (SC 2.4.1)

Allows keyboard users to bypass repeated navigation blocks.

```html
<!-- First element in <body> -->
<a class="skip-link" href="#main-content">Skip to main content</a>

<!-- Visually hidden until focused -->
<style>
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  padding: 1rem;
  background: #000;
  color: #fff;
  font-size: 1rem;
  z-index: 9999;
}
.skip-link:focus {
  top: 0;
}
</style>

<!-- Skip link target -->
<main id="main-content">
```

Note: `<main>` with a proper `id` is sufficient. The target element does not need `tabindex="-1"` in modern browsers, but adding it ensures `.focus()` works across all browsers.

---

## Programmatic Focus Management

### When to Move Focus Programmatically

| Situation | Where to Send Focus |
|---|---|
| Modal opens | First focusable element in modal, or modal container (with tabindex="-1") |
| Modal closes | Element that triggered the modal |
| Inline error appears | Stay on field (errors use aria-describedby, not focus movement) |
| Error summary appears after submit | Error summary container (tabindex="-1") |
| Page route changes in SPA | `<h1>` of new content (tabindex="-1") or top of page |
| Alert/notification appears | Do not move focus; use role="alert" |
| Expanded accordion section | Do not move focus; content is now visible above fold |
| Delete action removes focused element | Next item in list, or parent container |

### Focus After Async Operations

When content loads asynchronously and focus needs to move:

```javascript
// Wait for content to be in DOM before focusing
async function loadAndFocus() {
  const content = await fetchContent();
  document.getElementById('container').innerHTML = content;

  // Use setTimeout(0) or requestAnimationFrame to ensure DOM is ready
  requestAnimationFrame(() => {
    document.getElementById('new-heading').focus();
  });
}
```

---

## Focus During Dynamic Content Updates

### Content Added to Page (Not Route Change)

Do NOT move focus when content is added below the current focus point. Use `aria-live` regions instead.

```html
<!-- Announce search results without moving focus -->
<div role="status" aria-live="polite" id="result-count"></div>

<script>
document.getElementById('result-count').textContent = `Showing ${count} results`;
</script>
```

### Content Removed from Page (Focused Element Deleted)

If the currently focused element is removed:

```javascript
function deleteItem(itemElement) {
  // Find where focus should go before removing the item
  const nextItem = itemElement.nextElementSibling
                || itemElement.previousElementSibling
                || itemElement.closest('ul');

  itemElement.remove();

  if (nextItem) {
    nextItem.focus(); // If nextItem is not naturally focusable, add tabindex="-1"
  }
}
```

---

## Focus Not Obscured (SC 2.4.11 / SC 2.4.12)

At WCAG AA, focused elements must not be entirely hidden by sticky/fixed-position content. At WCAG AAA, no part of the focused component may be hidden.

Common culprits:
- Sticky headers (`position: sticky; top: 0`)
- Cookie consent banners
- Chat widget overlays
- Fixed footer navigation bars (mobile)

Fix with CSS `scroll-padding-top`:

```css
html {
  /* Offset for 60px sticky header */
  scroll-padding-top: 60px;
}
```

Or use JavaScript to check and scroll if focused element is obscured:

```javascript
document.addEventListener('focusin', (e) => {
  const rect = e.target.getBoundingClientRect();
  const stickyHeaderHeight = document.querySelector('header').offsetHeight;

  if (rect.top < stickyHeaderHeight) {
    window.scrollBy(0, rect.top - stickyHeaderHeight - 8);
  }
});
```
