---
title: "Accessible Tooltip Pattern"
standard: "WAI-ARIA APG + WCAG SC 1.4.13"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["tooltip", "aria-describedby", "1.4.13", "hover", "focus", "component-pattern"]
ai_context: "Accessible tooltip pattern conforming to SC 1.4.13 (Content on Hover or Focus). Load when implementing tooltips, popovers, or hover-reveal content."
---

# Accessible Tooltip Pattern

---

## SC 1.4.13 — Content on Hover or Focus (Level AA)

When content appears on pointer hover or keyboard focus, that content must:

1. **Dismissible** — The user can dismiss it without moving pointer or focus (Escape key)
2. **Hoverable** — If triggered by pointer hover, the pointer can move into the tooltip content without it disappearing
3. **Persistent** — Content stays visible until the hover/focus trigger leaves, it is dismissed, or it is no longer valid

---

## ARIA Role and Attributes

| Element | Role / Attribute | Notes |
|---------|-----------------|-------|
| Tooltip content | `role="tooltip"` | Required |
| Trigger element | `aria-describedby="tooltip-id"` | Links trigger to tooltip |
| Tooltip container | `id` matching the `aria-describedby` | Required |

**Important:** `role="tooltip"` is a description role — it does NOT receive focus. The trigger element receives focus; the tooltip is a description only.

---

## Keyboard Interaction

| Key | Behavior |
|-----|----------|
| Focus trigger element | Tooltip appears |
| `Escape` | Dismiss tooltip (required by SC 1.4.13) |
| Blur trigger element | Tooltip hides |
| Mouse hover on trigger | Tooltip appears |
| Move mouse into tooltip | Tooltip stays visible (SC 1.4.13 "hoverable") |
| Mouse leaves trigger AND tooltip | Tooltip hides |

---

## HTML Structure

```html
<!-- The trigger -->
<button
  type="button"
  id="info-btn"
  aria-describedby="info-tooltip"
>
  More info
</button>

<!-- The tooltip -->
<div
  role="tooltip"
  id="info-tooltip"
  class="tooltip"
>
  This action cannot be undone. All data will be permanently deleted.
</div>
```

---

## CSS

```css
.tooltip {
  position: absolute;
  background: #1a1a1a;
  color: #ffffff;
  padding: 6px 10px;
  border-radius: 4px;
  font-size: 0.875rem;
  max-width: 250px;
  z-index: 100;
  pointer-events: none; /* Will be overridden for hoverable requirement */
}

/* Hidden state */
.tooltip[hidden] {
  display: none;
}

/* Visible state */
.tooltip:not([hidden]) {
  pointer-events: auto; /* Allow mouse to enter tooltip */
}

/* Arrow (optional, CSS-only) */
.tooltip::before {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-bottom-color: #1a1a1a;
}
```

---

## JavaScript

```javascript
class Tooltip {
  constructor(trigger) {
    this.trigger = trigger;
    this.tooltip = document.getElementById(trigger.getAttribute('aria-describedby'));
    this.hideTimer = null;

    this.show = this.show.bind(this);
    this.hide = this.hide.bind(this);
    this.handleKeydown = this.handleKeydown.bind(this);

    // Keyboard focus/blur
    trigger.addEventListener('focus', this.show);
    trigger.addEventListener('blur', () => this.scheduleHide());
    trigger.addEventListener('keydown', this.handleKeydown);

    // Mouse hover
    trigger.addEventListener('mouseenter', this.show);
    trigger.addEventListener('mouseleave', () => this.scheduleHide());

    // SC 1.4.13: Allow mouse to move into tooltip without hiding
    this.tooltip.addEventListener('mouseenter', () => this.cancelHide());
    this.tooltip.addEventListener('mouseleave', () => this.scheduleHide());
  }

  show() {
    this.cancelHide();
    this.positionTooltip();
    this.tooltip.hidden = false;
  }

  scheduleHide() {
    this.hideTimer = setTimeout(() => {
      this.tooltip.hidden = true;
    }, 100); // Small delay allows mouse to enter tooltip
  }

  cancelHide() {
    if (this.hideTimer) {
      clearTimeout(this.hideTimer);
      this.hideTimer = null;
    }
  }

  handleKeydown(e) {
    if (e.key === 'Escape') {
      this.tooltip.hidden = true; // SC 1.4.13: dismiss with Escape
    }
  }

  positionTooltip() {
    const rect = this.trigger.getBoundingClientRect();
    this.tooltip.style.top = `${rect.bottom + window.scrollY + 8}px`;
    this.tooltip.style.left = `${rect.left + window.scrollX}px`;
  }
}

// Initialize all tooltips
document.querySelectorAll('[aria-describedby]').forEach(trigger => {
  const targetId = trigger.getAttribute('aria-describedby');
  const target = document.getElementById(targetId);
  if (target && target.getAttribute('role') === 'tooltip') {
    new Tooltip(trigger);
  }
});
```

---

## Icon-Only Button with Tooltip

A common pattern: icon-only button that reveals its label as a tooltip.

```html
<button
  type="button"
  aria-label="Delete item"
  aria-describedby="delete-tooltip"
  class="icon-btn"
>
  <!-- Decorative trash icon -->
  <svg aria-hidden="true" focusable="false" width="20" height="20">
    <!-- trash icon path -->
  </svg>
</button>

<div role="tooltip" id="delete-tooltip" hidden>
  Delete this item permanently
</div>
```

**Note:** The button MUST still have `aria-label="Delete item"` for screen readers who navigate by Tab — they may never hover to reveal the tooltip. The tooltip is an enhancement, not the only label.

---

## Popover vs. Tooltip

| Feature | Tooltip | Popover |
|---------|---------|---------|
| Contains interactive elements | No | Yes |
| Dismissal | Escape or blur | Escape, click outside, or close button |
| ARIA role | `tooltip` | `dialog` or `none` |
| Triggers on | Hover + focus | Click/Enter only |
| Focus moves into it | No | Yes (for interactive content) |

If the reveal content has buttons, links, or inputs — use a popover/dialog pattern, not a tooltip.

---

## Common Tooltip Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Tooltip only on hover, not focus | Inaccessible to keyboard users | Show tooltip on `:focus` as well as `:hover` |
| No Escape dismissal | Violates SC 1.4.13 | Add `keydown → Escape` handler |
| Tooltip disappears when mouse moves to it | Violates SC 1.4.13 "hoverable" | Add hover delay + mouseenter handler on tooltip |
| `title` attribute used as tooltip | Not keyboard accessible; no styling control | Use `role="tooltip"` + `aria-describedby` pattern |
| Icon button with tooltip only label | Button has no programmatic label | Always add `aria-label` on the trigger button |
| Tooltip with interactive content | Can't Tab to content | Use popover/dialog instead |
