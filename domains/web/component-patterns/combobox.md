---
title: "Accessible Combobox (Autocomplete) Pattern"
standard: "WAI-ARIA APG"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/combobox/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["combobox", "autocomplete", "listbox", "aria", "component-pattern", "keyboard"]
ai_context: "Complete accessible combobox/autocomplete pattern with ARIA markup and keyboard interaction. Load when implementing a search-with-suggestions, autocomplete, or select-with-filter component."
---

# Accessible Combobox (Autocomplete) Pattern

A combobox is a widget combining a text input with a popup list of options. Used for: autocomplete search, city/country selection, tag input.

---

## ARIA Roles and Attributes

| Element | Role | Required Attributes |
|---------|------|---------------------|
| Text input | `combobox` | `aria-expanded`, `aria-autocomplete`, `aria-haspopup="listbox"`, `aria-controls` |
| Options container | `listbox` | — |
| Each option | `option` | `aria-selected` |
| Input container | none | — |

### aria-autocomplete Values

| Value | Meaning |
|-------|---------|
| `list` | A list of suggested values appears, user can select from it |
| `inline` | The first suggested value is auto-completed in the input |
| `both` | Both list and inline completion |
| `none` | Input can have a listbox, but autocomplete is not provided |

---

## Keyboard Interaction

| Key | Context | Behavior |
|-----|---------|----------|
| `Down Arrow` | Input, popup closed | Open popup; move focus to first option |
| `Down Arrow` | Input or option, popup open | Move to next option |
| `Up Arrow` | Input, popup closed | Open popup; move focus to last option |
| `Up Arrow` | Input or option, popup open | Move to previous option |
| `Enter` | Option focused | Select option; close popup; set input value |
| `Enter` | Input, popup closed | If single matching value, select it |
| `Escape` | Popup open | Close popup; return focus to input |
| `Escape` | Input value typed | Clear input OR revert to previous value |
| `Alt + Down Arrow` | Input | Open popup without moving focus |
| `Alt + Up Arrow` | Option focused | Close popup; return focus to input |
| `Tab` | Popup open | Close popup; move focus to next tab stop |
| `Backspace` / `Delete` | Input | Edit text; filter list |
| Type characters | Input | Filter list; keep focus in input |

---

## HTML Structure

```html
<div class="combobox-container">
  <label for="city-input">City</label>

  <div class="combobox-wrapper">
    <input
      type="text"
      id="city-input"
      role="combobox"
      aria-expanded="false"
      aria-autocomplete="list"
      aria-haspopup="listbox"
      aria-controls="city-listbox"
      aria-activedescendant=""
      autocomplete="off"
    >
    <!-- Optional toggle button -->
    <button
      type="button"
      tabindex="-1"
      aria-label="Show city suggestions"
      class="combobox-toggle"
    >
      ▼
    </button>
  </div>

  <ul
    id="city-listbox"
    role="listbox"
    aria-label="City suggestions"
    hidden
  >
    <!-- Options inserted dynamically -->
  </ul>
</div>
```

---

## Option Markup (Dynamic)

```html
<!-- Generated option items -->
<li
  role="option"
  id="option-new-york"
  aria-selected="false"
>
  New York
</li>

<li
  role="option"
  id="option-los-angeles"
  aria-selected="true"
  class="focused-option"
>
  Los Angeles
</li>
```

When using `aria-activedescendant`, focus stays in the input and the active option is indicated by pointing `aria-activedescendant` at the option's `id`.

---

## JavaScript (aria-activedescendant Pattern)

```javascript
class Combobox {
  constructor(input, listbox) {
    this.input = input;
    this.listbox = listbox;
    this.options = [];
    this.activeIndex = -1;

    this.input.addEventListener('input', this.handleInput.bind(this));
    this.input.addEventListener('keydown', this.handleKeydown.bind(this));
    this.input.addEventListener('blur', this.handleBlur.bind(this));

    // Click on option
    this.listbox.addEventListener('mousedown', this.handleOptionClick.bind(this));
  }

  handleInput(e) {
    const value = this.input.value;
    if (value.length < 1) {
      this.closeListbox();
      return;
    }
    this.filterOptions(value);
    if (this.options.length > 0) {
      this.openListbox();
    } else {
      this.closeListbox();
    }
    this.activeIndex = -1;
    this.input.removeAttribute('aria-activedescendant');
  }

  handleKeydown(e) {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        if (!this.isOpen()) this.openListbox();
        this.moveActive(1);
        break;
      case 'ArrowUp':
        e.preventDefault();
        if (!this.isOpen()) this.openListbox();
        this.moveActive(-1);
        break;
      case 'Enter':
        if (this.activeIndex >= 0) {
          e.preventDefault();
          this.selectOption(this.activeIndex);
        }
        break;
      case 'Escape':
        this.closeListbox();
        this.input.focus();
        break;
      case 'Tab':
        this.closeListbox();
        break;
      case 'Alt':
        // Alt+Down/Up handled by checking e.altKey in ArrowDown/ArrowUp
        break;
    }
  }

  moveActive(direction) {
    const count = this.options.length;
    if (count === 0) return;

    this.activeIndex = Math.max(-1, Math.min(count - 1, this.activeIndex + direction));

    this.options.forEach((opt, i) => {
      opt.setAttribute('aria-selected', i === this.activeIndex ? 'true' : 'false');
      opt.classList.toggle('focused-option', i === this.activeIndex);
    });

    if (this.activeIndex >= 0) {
      this.input.setAttribute('aria-activedescendant', this.options[this.activeIndex].id);
    } else {
      this.input.removeAttribute('aria-activedescendant');
    }
  }

  selectOption(index) {
    this.input.value = this.options[index].textContent.trim();
    this.closeListbox();
    this.input.focus();
  }

  handleOptionClick(e) {
    const option = e.target.closest('[role="option"]');
    if (option) {
      e.preventDefault(); // Prevent blur on input
      const index = this.options.indexOf(option);
      if (index >= 0) this.selectOption(index);
    }
  }

  handleBlur() {
    // Delay close so option click can complete
    setTimeout(() => this.closeListbox(), 150);
  }

  openListbox() {
    this.listbox.hidden = false;
    this.input.setAttribute('aria-expanded', 'true');
  }

  closeListbox() {
    this.listbox.hidden = true;
    this.input.setAttribute('aria-expanded', 'false');
    this.input.removeAttribute('aria-activedescendant');
    this.activeIndex = -1;
  }

  isOpen() {
    return !this.listbox.hidden;
  }

  filterOptions(query) {
    // Example: filter a data array and re-render listbox
    const filtered = this.allCities.filter(city =>
      city.toLowerCase().startsWith(query.toLowerCase())
    );

    this.listbox.innerHTML = filtered.map((city, i) =>
      `<li role="option" id="option-${i}" aria-selected="false">${city}</li>`
    ).join('');

    this.options = [...this.listbox.querySelectorAll('[role="option"]')];
  }
}
```

---

## React Implementation

```jsx
import { useState, useRef, useId } from 'react';

function Combobox({ label, options, onChange }) {
  const [inputValue, setInputValue] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(-1);
  const inputRef = useRef(null);
  const listboxId = useId();

  const filtered = options.filter(opt =>
    opt.toLowerCase().includes(inputValue.toLowerCase())
  );

  const handleKeyDown = (e) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setIsOpen(true);
        setActiveIndex(i => Math.min(filtered.length - 1, i + 1));
        break;
      case 'ArrowUp':
        e.preventDefault();
        setActiveIndex(i => Math.max(-1, i - 1));
        break;
      case 'Enter':
        if (activeIndex >= 0 && filtered[activeIndex]) {
          selectOption(filtered[activeIndex]);
        }
        break;
      case 'Escape':
        setIsOpen(false);
        setActiveIndex(-1);
        break;
    }
  };

  const selectOption = (value) => {
    setInputValue(value);
    setIsOpen(false);
    setActiveIndex(-1);
    onChange?.(value);
    inputRef.current?.focus();
  };

  return (
    <div>
      <label htmlFor="cb-input">{label}</label>
      <input
        ref={inputRef}
        id="cb-input"
        type="text"
        role="combobox"
        aria-expanded={isOpen}
        aria-autocomplete="list"
        aria-haspopup="listbox"
        aria-controls={listboxId}
        aria-activedescendant={activeIndex >= 0 ? `opt-${activeIndex}` : undefined}
        value={inputValue}
        onChange={e => { setInputValue(e.target.value); setIsOpen(true); setActiveIndex(-1); }}
        onKeyDown={handleKeyDown}
        onBlur={() => setTimeout(() => setIsOpen(false), 150)}
        autoComplete="off"
      />
      {isOpen && filtered.length > 0 && (
        <ul id={listboxId} role="listbox">
          {filtered.map((opt, i) => (
            <li
              key={opt}
              id={`opt-${i}`}
              role="option"
              aria-selected={i === activeIndex}
              onMouseDown={() => selectOption(opt)}
            >
              {opt}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Focus moves into listbox on arrow key | Breaks input editing | Use `aria-activedescendant` pattern; keep focus in input |
| No `aria-expanded` on input | Screen readers don't know popup state | Always maintain `aria-expanded` on the combobox input |
| Listbox not empty when closed | Stale options announced | Clear listbox or use `hidden` attribute |
| No `aria-activedescendant` update | Active option not announced | Update on each `moveActive()` call |
| Selecting an option moves Tab focus away | Unexpected focus change | After selection, return focus to input |
| `autocomplete="on"` conflicts with custom list | Browser autocomplete overlaps | Set `autocomplete="off"` on the input |
