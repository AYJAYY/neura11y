---
title: "Accessible Accordion Component Pattern"
standard: "WAI-ARIA APG"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/accordion/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["accordion", "disclosure", "aria", "component-pattern", "keyboard", "expanded"]
ai_context: "Complete accessible accordion pattern with ARIA markup, keyboard interaction, and JavaScript. Load when implementing an accordion or show/hide component."
---

# Accessible Accordion Component Pattern

An accordion is a vertically stacked set of interactive headings, each toggling a section of content.

---

## ARIA Roles and Attributes

| Element | Role / Attribute | Notes |
|---------|-----------------|-------|
| Heading wrapping button | `<h2>` through `<h6>` | Level matches document hierarchy |
| Toggle button | `<button>` | Native; no `role="button"` needed |
| Button state | `aria-expanded="true|false"` | Required |
| Button and panel link | `aria-controls="panel-id"` | Points to the panel |
| Panel | `role="region"` | Only if panel has a landmark role meaning; optional |
| Panel label | `aria-labelledby="button-id"` | Associates panel with header |

---

## Keyboard Interaction

| Key | Behavior |
|-----|----------|
| `Enter` / `Space` | Toggle focused accordion header (expand/collapse) |
| `Tab` | Move focus to next focusable element |
| `Shift + Tab` | Move focus to previous focusable element |
| `Down Arrow` *(optional)* | Move focus to next accordion header |
| `Up Arrow` *(optional)* | Move focus to previous accordion header |
| `Home` *(optional)* | Move focus to first accordion header |
| `End` *(optional)* | Move focus to last accordion header |

Arrow key navigation is optional in the APG spec. If implemented, it must cycle through headers without activating them.

---

## HTML Structure

```html
<div class="accordion">

  <!-- Item 1 -->
  <h3 class="accordion__heading">
    <button
      type="button"
      class="accordion__trigger"
      id="acc-btn-1"
      aria-expanded="true"
      aria-controls="acc-panel-1"
    >
      What is your return policy?
    </button>
  </h3>
  <div
    id="acc-panel-1"
    role="region"
    aria-labelledby="acc-btn-1"
    class="accordion__panel"
  >
    <p>You may return any item within 30 days of purchase for a full refund...</p>
  </div>

  <!-- Item 2 -->
  <h3 class="accordion__heading">
    <button
      type="button"
      class="accordion__trigger"
      id="acc-btn-2"
      aria-expanded="false"
      aria-controls="acc-panel-2"
    >
      How long does shipping take?
    </button>
  </h3>
  <div
    id="acc-panel-2"
    role="region"
    aria-labelledby="acc-btn-2"
    class="accordion__panel"
    hidden
  >
    <p>Standard shipping takes 3–5 business days...</p>
  </div>

</div>
```

---

## JavaScript

```javascript
class Accordion {
  constructor(container) {
    this.container = container;
    this.buttons = [...container.querySelectorAll('.accordion__trigger')];
    this.panels = [...container.querySelectorAll('.accordion__panel')];
    this.allowMultiple = container.hasAttribute('data-allow-multiple');

    this.buttons.forEach(btn => {
      btn.addEventListener('click', this.handleClick.bind(this));
    });

    // Optional: arrow key navigation
    this.container.addEventListener('keydown', this.handleKeydown.bind(this));
  }

  handleClick(e) {
    const btn = e.currentTarget;
    const isExpanded = btn.getAttribute('aria-expanded') === 'true';

    if (!this.allowMultiple) {
      // Close all others
      this.buttons.forEach(b => {
        b.setAttribute('aria-expanded', 'false');
      });
      this.panels.forEach(p => {
        p.hidden = true;
      });
    }

    // Toggle clicked
    btn.setAttribute('aria-expanded', isExpanded ? 'false' : 'true');
    const panel = document.getElementById(btn.getAttribute('aria-controls'));
    panel.hidden = isExpanded;
  }

  handleKeydown(e) {
    const index = this.buttons.indexOf(document.activeElement);
    if (index === -1) return;

    let newIndex;
    if (e.key === 'ArrowDown') {
      newIndex = index === this.buttons.length - 1 ? 0 : index + 1;
    } else if (e.key === 'ArrowUp') {
      newIndex = index === 0 ? this.buttons.length - 1 : index - 1;
    } else if (e.key === 'Home') {
      newIndex = 0;
    } else if (e.key === 'End') {
      newIndex = this.buttons.length - 1;
    } else {
      return;
    }

    e.preventDefault();
    this.buttons[newIndex].focus();
  }
}

document.querySelectorAll('.accordion').forEach(el => new Accordion(el));
```

---

## CSS

```css
.accordion {
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
}

.accordion__heading {
  margin: 0;
}

.accordion__trigger {
  width: 100%;
  text-align: left;
  padding: 16px;
  background: #f9f9f9;
  border: none;
  border-bottom: 1px solid #ccc;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Arrow icon using CSS — toggles on expanded state */
.accordion__trigger::after {
  content: '▼';
  font-size: 0.75em;
  transition: transform 0.2s ease;
}

.accordion__trigger[aria-expanded="true"]::after {
  transform: rotate(-180deg);
}

.accordion__trigger:hover {
  background: #eef2ff;
}

.accordion__trigger:focus-visible {
  outline: 3px solid #0066cc;
  outline-offset: -3px;
}

.accordion__panel {
  padding: 16px;
}

.accordion__panel[hidden] {
  display: none;
}

/* Animate open/close (respects reduced motion) */
@media (prefers-reduced-motion: no-preference) {
  .accordion__panel {
    animation: slideDown 0.2s ease;
  }
  @keyframes slideDown {
    from { opacity: 0; transform: translateY(-4px); }
    to { opacity: 1; transform: translateY(0); }
  }
}
```

---

## React Implementation

```jsx
import { useState } from 'react';

function Accordion({ items, allowMultiple = false }) {
  const [openItems, setOpenItems] = useState(new Set([0])); // First open by default

  const toggleItem = (index) => {
    setOpenItems(prev => {
      const next = new Set(allowMultiple ? prev : []);
      if (prev.has(index)) {
        next.delete(index);
      } else {
        next.add(index);
      }
      return next;
    });
  };

  return (
    <div className="accordion">
      {items.map((item, i) => {
        const isOpen = openItems.has(i);
        const btnId = `acc-btn-${i}`;
        const panelId = `acc-panel-${i}`;

        return (
          <div key={i}>
            <h3 style={{ margin: 0 }}>
              <button
                type="button"
                id={btnId}
                aria-expanded={isOpen}
                aria-controls={panelId}
                onClick={() => toggleItem(i)}
                className="accordion__trigger"
              >
                {item.heading}
              </button>
            </h3>
            <div
              id={panelId}
              role="region"
              aria-labelledby={btnId}
              hidden={!isOpen}
              className="accordion__panel"
            >
              {item.content}
            </div>
          </div>
        );
      })}
    </div>
  );
}
```

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| `role="button"` on a `<div>` | Missing keyboard activation | Use native `<button>` element |
| `aria-expanded` on heading instead of button | Incorrect semantics | `aria-expanded` must be on the button |
| Collapsing panel with `visibility:hidden` only | Panel still accessible to AT | Use `hidden` attribute OR `display:none` |
| No heading wrapping the button | Breaks heading outline | Wrap button in `<h2>`–`<h6>` |
| Icon inside button not hidden | "Down arrow" read aloud | Add `aria-hidden="true"` to icon element |
| `aria-controls` missing | Panel not associated | Add `aria-controls` pointing to panel id |

---

## When to Use role="region"

`role="region"` creates a landmark that appears in the landmarks list in screen readers. Only use it when the panel content is meaningful as a standalone section. For simple FAQ content, `role="region"` may create landmark clutter.

**Use `role="region"`:** When the panel contains structured, named content worth navigating to directly.
**Omit `role="region"`:** For simple FAQs, terms, or short content snippets.
