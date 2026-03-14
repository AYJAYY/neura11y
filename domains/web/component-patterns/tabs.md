---
title: "Accessible Tabs Component Pattern"
standard: "WAI-ARIA APG"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/tabs/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["tabs", "tablist", "tabpanel", "aria", "component-pattern", "keyboard"]
ai_context: "Complete accessible tabs pattern with ARIA markup, keyboard interaction, and JavaScript. Load when implementing a tabs component."
---

# Accessible Tabs Component Pattern

---

## ARIA Roles

| Element | Role | Required attributes |
|---------|------|---------------------|
| Container wrapping all tabs | `tablist` | `aria-label` or `aria-labelledby` |
| Individual tab button | `tab` | `aria-selected`, `aria-controls` |
| Tab content panel | `tabpanel` | `aria-labelledby` |

---

## Keyboard Interaction

### Automatic Activation (activates on arrow key)

| Key | Behavior |
|-----|----------|
| `Left Arrow` | Move focus to previous tab AND activate it (wraps) |
| `Right Arrow` | Move focus to next tab AND activate it (wraps) |
| `Home` | Move focus to first tab AND activate it |
| `End` | Move focus to last tab AND activate it |
| `Tab` | Move focus into the active tabpanel |
| `Shift + Tab` | Move focus back to the active tab from inside the panel |

### Manual Activation (requires Enter/Space to activate)

| Key | Behavior |
|-----|----------|
| `Left Arrow` | Move focus to previous tab (does NOT activate) |
| `Right Arrow` | Move focus to next tab (does NOT activate) |
| `Enter` / `Space` | Activate focused tab |

**When to use each:**
- **Automatic:** Tabs that don't require async data loading; tab content loads instantly
- **Manual:** Tabs that trigger network requests; prevents unnecessary API calls on arrow navigation

---

## HTML Structure

```html
<div class="tabs-container">
  <div role="tablist" aria-label="Product information">
    <button
      role="tab"
      id="tab-overview"
      aria-selected="true"
      aria-controls="panel-overview"
      tabindex="0"
    >
      Overview
    </button>
    <button
      role="tab"
      id="tab-specs"
      aria-selected="false"
      aria-controls="panel-specs"
      tabindex="-1"
    >
      Specifications
    </button>
    <button
      role="tab"
      id="tab-reviews"
      aria-selected="false"
      aria-controls="panel-reviews"
      tabindex="-1"
    >
      Reviews
    </button>
  </div>

  <div
    role="tabpanel"
    id="panel-overview"
    aria-labelledby="tab-overview"
  >
    <h2>Product Overview</h2>
    <p>Overview content...</p>
  </div>

  <div
    role="tabpanel"
    id="panel-specs"
    aria-labelledby="tab-specs"
    hidden
  >
    <h2>Specifications</h2>
    <p>Specs content...</p>
  </div>

  <div
    role="tabpanel"
    id="panel-reviews"
    aria-labelledby="tab-reviews"
    hidden
  >
    <h2>Customer Reviews</h2>
    <p>Reviews content...</p>
  </div>
</div>
```

---

## JavaScript (Automatic Activation)

```javascript
class Tabs {
  constructor(container) {
    this.container = container;
    this.tablist = container.querySelector('[role="tablist"]');
    this.tabs = [...container.querySelectorAll('[role="tab"]')];
    this.panels = [...container.querySelectorAll('[role="tabpanel"]')];

    this.tablist.addEventListener('keydown', this.handleKeydown.bind(this));
    this.tabs.forEach(tab => {
      tab.addEventListener('click', this.handleClick.bind(this));
    });
  }

  handleKeydown(e) {
    const currentIndex = this.tabs.indexOf(document.activeElement);
    let newIndex;

    switch (e.key) {
      case 'ArrowLeft':
        newIndex = currentIndex === 0 ? this.tabs.length - 1 : currentIndex - 1;
        break;
      case 'ArrowRight':
        newIndex = currentIndex === this.tabs.length - 1 ? 0 : currentIndex + 1;
        break;
      case 'Home':
        newIndex = 0;
        break;
      case 'End':
        newIndex = this.tabs.length - 1;
        break;
      default:
        return;
    }

    e.preventDefault();
    this.activateTab(newIndex);
  }

  handleClick(e) {
    const index = this.tabs.indexOf(e.currentTarget);
    this.activateTab(index);
  }

  activateTab(index) {
    // Deactivate all tabs
    this.tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', 'false');
      tab.setAttribute('tabindex', '-1');
    });

    // Hide all panels
    this.panels.forEach(panel => {
      panel.hidden = true;
    });

    // Activate selected tab
    this.tabs[index].setAttribute('aria-selected', 'true');
    this.tabs[index].setAttribute('tabindex', '0');
    this.tabs[index].focus();

    // Show selected panel
    this.panels[index].hidden = false;
  }
}

// Initialize
document.querySelectorAll('.tabs-container').forEach(container => {
  new Tabs(container);
});
```

---

## CSS

```css
/* Tab list container */
[role="tablist"] {
  display: flex;
  border-bottom: 2px solid #ccc;
  gap: 0;
}

/* Individual tabs */
[role="tab"] {
  padding: 8px 16px;
  border: none;
  background: transparent;
  cursor: pointer;
  color: #555;
  border-bottom: 3px solid transparent;
  margin-bottom: -2px; /* Overlap the tablist border */
  font-size: 1rem;
}

/* Active tab */
[role="tab"][aria-selected="true"] {
  color: #0066cc;
  border-bottom-color: #0066cc;
  font-weight: 600;
}

/* Focus visible */
[role="tab"]:focus-visible {
  outline: 3px solid #0066cc;
  outline-offset: 2px;
}

/* Hover */
[role="tab"]:hover {
  color: #0066cc;
  background-color: #f0f4ff;
}

/* Tab panel */
[role="tabpanel"] {
  padding: 16px 0;
}

/* Hidden panels */
[role="tabpanel"][hidden] {
  display: none;
}
```

---

## Vertical Tabs

For vertical tab layouts, add `aria-orientation="vertical"` and use Up/Down arrows instead of Left/Right.

```html
<div role="tablist" aria-orientation="vertical" aria-label="Settings sections">
  <!-- tabs -->
</div>
```

```javascript
// Replace ArrowLeft/ArrowRight with ArrowUp/ArrowDown in keydown handler
case 'ArrowUp':
  newIndex = currentIndex === 0 ? this.tabs.length - 1 : currentIndex - 1;
  break;
case 'ArrowDown':
  newIndex = currentIndex === this.tabs.length - 1 ? 0 : currentIndex + 1;
  break;
```

---

## React Implementation

```jsx
import { useState, useRef, useCallback } from 'react';

function Tabs({ tabs }) {
  const [activeIndex, setActiveIndex] = useState(0);
  const tabRefs = useRef([]);

  const handleKeydown = useCallback((e, index) => {
    let newIndex;
    if (e.key === 'ArrowLeft') newIndex = index === 0 ? tabs.length - 1 : index - 1;
    else if (e.key === 'ArrowRight') newIndex = index === tabs.length - 1 ? 0 : index + 1;
    else if (e.key === 'Home') newIndex = 0;
    else if (e.key === 'End') newIndex = tabs.length - 1;
    else return;

    e.preventDefault();
    setActiveIndex(newIndex);
    tabRefs.current[newIndex]?.focus();
  }, [tabs.length]);

  return (
    <div>
      <div role="tablist" aria-label="Sections">
        {tabs.map((tab, i) => (
          <button
            key={tab.id}
            role="tab"
            id={`tab-${tab.id}`}
            aria-selected={i === activeIndex}
            aria-controls={`panel-${tab.id}`}
            tabIndex={i === activeIndex ? 0 : -1}
            ref={el => tabRefs.current[i] = el}
            onClick={() => setActiveIndex(i)}
            onKeyDown={e => handleKeydown(e, i)}
          >
            {tab.label}
          </button>
        ))}
      </div>
      {tabs.map((tab, i) => (
        <div
          key={tab.id}
          role="tabpanel"
          id={`panel-${tab.id}`}
          aria-labelledby={`tab-${tab.id}`}
          hidden={i !== activeIndex}
        >
          {tab.content}
        </div>
      ))}
    </div>
  );
}
```

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| All tabs have `tabindex="0"` | 3+ Tab stops instead of 1 | Only active tab has `tabindex="0"` |
| Missing `aria-controls` | Panel not associated with tab | Add `aria-controls` on each tab |
| Missing `aria-labelledby` on panel | Panel not labelled | Add `aria-labelledby` pointing to tab id |
| Panel hidden with `display:none` and no `hidden` | May interfere with ARIA | Use `hidden` attribute OR `display:none` (both work; `hidden` is simpler) |
| Tab panels contain no heading | Hard for users to orient after Tab into panel | Add heading inside each panel |
| Focus moves to panel on tab activation | Unexpected for automatic activation | Focus stays on tab; user presses Tab to enter panel |
