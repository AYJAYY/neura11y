---
title: "Accessible Modal Dialog Pattern"
standard: "WAI-ARIA APG + WCAG"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["modal", "dialog", "aria", "focus-trap", "keyboard", "component-pattern"]
ai_context: "Complete accessible modal dialog implementation. Includes ARIA markup, keyboard behavior, focus management, and common failures. Use as the authoritative reference for modal dialogs."
---

# Accessible Modal Dialog Pattern

Source: ARIA Authoring Practices Guide — https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

---

## Required ARIA Markup

```html
<!-- Trigger button -->
<button type="button" id="open-dialog">Open Dialog</button>

<!-- Dialog (hidden initially) -->
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
  id="my-dialog"
  tabindex="-1"
  hidden
>
  <h2 id="dialog-title">Confirm Delete</h2>
  <p id="dialog-desc">
    Are you sure you want to delete this item? This action cannot be undone.
  </p>

  <div class="dialog-actions">
    <button type="button" id="confirm-delete">Delete</button>
    <button type="button" id="cancel-delete">Cancel</button>
  </div>

  <button
    type="button"
    class="dialog-close"
    aria-label="Close dialog"
  >×</button>
</div>

<!-- Backdrop/overlay (optional, behind dialog) -->
<div class="dialog-backdrop" hidden aria-hidden="true"></div>
```

---

## Required ARIA Attributes

| Attribute | Value | Required | Purpose |
|---|---|---|---|
| `role="dialog"` | — | Yes | Identifies as a dialog |
| `aria-modal="true"` | `true` | Yes | Tells AT background is inert |
| `aria-labelledby` | ID of heading | Yes (or aria-label) | Dialog's accessible name |
| `aria-describedby` | ID of description | Recommended | Additional context for AT |
| `tabindex="-1"` | — | Yes | Allows programmatic focus on container |

**Note:** `aria-modal="true"` tells AT that only dialog content should be accessible. However, it does NOT automatically inert the background — you must also manage focus and optionally use the HTML `inert` attribute on background content.

---

## Keyboard Interaction (Required)

| Key | Behavior |
|-----|---------|
| `Tab` | Move focus to next focusable element inside dialog; wrap to first if at last |
| `Shift + Tab` | Move focus to previous focusable element; wrap to last if at first |
| `Escape` | Close the dialog and return focus to trigger element |
| `Enter` / `Space` | Activate focused button (standard button behavior) |

**Focus must be trapped within the dialog.** Users cannot Tab or Shift+Tab out of an open modal.

---

## JavaScript Implementation

```javascript
class AccessibleDialog {
  constructor(dialogEl, triggerEl) {
    this.dialog = dialogEl;
    this.trigger = triggerEl;
    this.focusableSelectors = [
      'button:not([disabled])',
      '[href]',
      'input:not([disabled])',
      'select:not([disabled])',
      'textarea:not([disabled])',
      '[tabindex]:not([tabindex="-1"])'
    ].join(', ');
  }

  open() {
    this.dialog.removeAttribute('hidden');
    this.dialog.removeAttribute('aria-hidden');

    // Inert background (modern browsers)
    document.querySelector('main').setAttribute('inert', '');
    document.querySelector('header').setAttribute('inert', '');

    // Focus first focusable element (or dialog container)
    const firstFocusable = this.getFocusableElements()[0];
    (firstFocusable || this.dialog).focus();

    // Bind keyboard events
    this.keydownHandler = (e) => this.handleKeydown(e);
    this.dialog.addEventListener('keydown', this.keydownHandler);
  }

  close() {
    this.dialog.setAttribute('hidden', '');

    // Remove inert from background
    document.querySelector('main').removeAttribute('inert');
    document.querySelector('header').removeAttribute('inert');

    // Return focus to trigger
    this.trigger.focus();

    // Remove event listener
    this.dialog.removeEventListener('keydown', this.keydownHandler);
  }

  handleKeydown(e) {
    if (e.key === 'Escape') {
      this.close();
      return;
    }

    if (e.key !== 'Tab') return;

    const focusable = this.getFocusableElements();
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (e.shiftKey) {
      if (document.activeElement === first) {
        last.focus();
        e.preventDefault();
      }
    } else {
      if (document.activeElement === last) {
        first.focus();
        e.preventDefault();
      }
    }
  }

  getFocusableElements() {
    return Array.from(
      this.dialog.querySelectorAll(this.focusableSelectors)
    ).filter(el => !el.closest('[hidden]'));
  }
}

// Usage
const dialog = document.getElementById('my-dialog');
const trigger = document.getElementById('open-dialog');
const modal = new AccessibleDialog(dialog, trigger);

trigger.addEventListener('click', () => modal.open());
document.getElementById('cancel-delete').addEventListener('click', () => modal.close());
document.getElementById('confirm-delete').addEventListener('click', () => {
  // Handle action
  modal.close();
});
```

---

## CSS

```css
[role="dialog"] {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1000;
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.3);
  max-width: 500px;
  width: calc(100% - 2rem);
  max-height: 90vh;
  overflow-y: auto;
}

.dialog-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 999;
}

/* Ensure dialog never loses focus ring */
[role="dialog"]:focus {
  outline: none; /* Container; individual elements have focus styles */
}
```

---

## alert vs. dialog Role

| Role | When to Use | Focus behavior |
|------|-------------|----------------|
| `role="dialog"` | General-purpose modals; user must interact | Move focus in; trap focus |
| `role="alertdialog"` | Critical messages requiring immediate response | Move focus to dialog; trap focus |
| `role="alert"` | Non-interactive status messages (errors, confirmations) | Do NOT move focus; use live region |

Use `role="alertdialog"` when:
- Dialog is an error requiring acknowledgment
- Dialog presents critical information
- Dialog requires user decision before proceeding

---

## Common Failures

1. **Focus not sent to dialog on open** — Screen reader doesn't know dialog opened
2. **Focus not returned to trigger on close** — User loses their place in the page
3. **No focus trap** — Tab moves out of dialog into background content
4. **Escape doesn't close** — Keyboard trap without escape
5. **`aria-modal="true"` without inert on background** — AT still browses background
6. **`aria-hidden="true"` on dialog** — Dialog invisible to AT while open
7. **No accessible name** — Missing `aria-labelledby` or `aria-label` on dialog
8. **Dialog in `aria-hidden` container** — Entire modal zone hidden from AT
9. **Scroll within dialog not keyboard accessible** — Long dialogs need keyboard scrolling
10. **Multiple `role="dialog"` elements at once** — Stack dialogs properly if nesting needed

---

## HTML `<dialog>` Element (Native)

The HTML `<dialog>` element provides built-in dialog semantics:

```html
<dialog id="my-dialog" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Delete</h2>
  <p>Are you sure?</p>
  <button autofocus>Confirm</button>
  <button>Cancel</button>
</dialog>
```

```javascript
// Open as modal (focus trapping and backdrop built in)
document.getElementById('my-dialog').showModal();

// Close
document.getElementById('my-dialog').close();
```

**Advantages of `<dialog>`:**
- Built-in focus trap (in browsers that support it)
- Built-in Escape key handling
- Implicit `role="dialog"`
- `::backdrop` pseudo-element for overlay
- No need for `aria-modal`

**Caveats:**
- AT support varies; always test with screen readers
- `autofocus` attribute on first button moves focus correctly
- Return focus to trigger must still be implemented manually
