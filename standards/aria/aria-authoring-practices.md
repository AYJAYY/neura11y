---
title: "ARIA Authoring Practices Guide — Keyboard Patterns"
standard: "ARIA APG"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["aria", "apg", "patterns", "keyboard", "components"]
ai_context: "APG keyboard interaction patterns for common UI components. The authoritative source for keyboard behavior in custom widgets. Load when generating accessible component code."
---

# ARIA Authoring Practices Guide — Keyboard Patterns

Source: https://www.w3.org/WAI/ARIA/apg/patterns/

The APG defines keyboard interaction models and ARIA markup patterns for common UI components. These are not normative requirements but represent established, widely-supported patterns that screen readers expect.

---

## Core Keyboard Concepts

### Tab Stop vs. Arrow Key Navigation

**Composite widgets use a single tab stop.** Internal navigation uses arrow keys.

- Tab moves to the widget container
- Arrow keys navigate within the widget
- This prevents users from tabbing through every item (e.g., 50 options in a listbox)

**Simple widgets are individual tab stops.** Each button, link, and input is a separate tab stop.

### Roving tabindex Pattern

Used in composite widgets to manage which item is focusable:

```javascript
// Only the "active" item has tabindex="0"; all others have tabindex="-1"
function setActive(items, activeIndex) {
  items.forEach((item, i) => {
    item.setAttribute('tabindex', i === activeIndex ? '0' : '-1');
  });
  items[activeIndex].focus();
}
```

### aria-activedescendant Pattern

Alternative to roving tabindex — container keeps focus, active descendant is communicated via `aria-activedescendant`:

```html
<ul role="listbox" tabindex="0" aria-activedescendant="opt-2">
  <li role="option" id="opt-1" aria-selected="false">Option 1</li>
  <li role="option" id="opt-2" aria-selected="true">Option 2</li>
</ul>
```

---

## Component Keyboard Patterns

### Accordion (Disclosure Pattern)

**Roles:** Heading + button, region

| Key | Behavior |
|-----|---------|
| `Enter` / `Space` | Toggle expanded/collapsed state of focused accordion header |
| `Tab` | Move focus to next focusable element |
| `Shift + Tab` | Move focus to previous focusable element |
| `Down Arrow` (optional) | Move focus to next accordion header |
| `Up Arrow` (optional) | Move focus to previous accordion header |
| `Home` (optional) | Move focus to first accordion header |
| `End` (optional) | Move focus to last accordion header |

```html
<div class="accordion">
  <h3>
    <button aria-expanded="false" aria-controls="panel-1" id="btn-1">
      Section 1
    </button>
  </h3>
  <div id="panel-1" role="region" aria-labelledby="btn-1" hidden>
    <p>Panel content...</p>
  </div>
</div>
```

---

### Button

**Role:** `button`

| Key | Behavior |
|-----|---------|
| `Enter` | Activate the button |
| `Space` | Activate the button |

Note: Both Enter and Space must activate buttons (unlike links, which only use Enter).

---

### Carousel

**Roles:** `group` (container), `button` (controls), `listitem` (slides)

| Key | Behavior |
|-----|---------|
| `Tab` | Move focus through interactive elements: prev/next buttons, rotation control, slide indicators |
| `Enter` / `Space` | Activate focused button |

Required controls:
- Previous/Next buttons
- Pause/play button (if auto-rotating)
- Slide picker buttons or indicators

```html
<section aria-label="Featured products" aria-roledescription="carousel">
  <button aria-label="Stop automatic slide show">Pause</button>
  <button aria-label="Previous slide">‹</button>
  <button aria-label="Next slide">›</button>
  <div aria-live="polite">
    <div role="group" aria-label="Slide 1 of 5">
      ...
    </div>
  </div>
</section>
```

---

### Checkbox

**Role:** `checkbox`

| Key | Behavior |
|-----|---------|
| `Space` | Toggle checked state |
| `Tab` | Move focus to next focusable element |

States: `aria-checked="true"`, `aria-checked="false"`, `aria-checked="mixed"` (indeterminate)

---

### Combobox (Editable with Listbox)

**Roles:** `combobox` (input), `listbox` (dropdown), `option` (items)

| Key | Behavior |
|-----|---------|
| `Down Arrow` | If popup closed and empty: open popup; move focus to first option. If open: move focus to next option |
| `Up Arrow` | If popup closed: open popup; move focus to last option. If open: move focus to previous option |
| `Enter` | Select focused option; close popup; set input value |
| `Escape` | Close popup; if input was changed, revert or clear |
| `Backspace` | Delete last character in input |
| `Alt + Down Arrow` | Open popup without moving focus |
| `Alt + Up Arrow` | If popup open: close popup; move focus to input |

```html
<label for="city-input">City</label>
<input
  id="city-input"
  type="text"
  role="combobox"
  aria-expanded="false"
  aria-autocomplete="list"
  aria-haspopup="listbox"
  aria-controls="city-options"
>
<ul id="city-options" role="listbox" hidden>
  <li role="option" id="city-1">New York</li>
  <li role="option" id="city-2">Los Angeles</li>
</ul>
```

---

### Dialog (Modal)

**Role:** `dialog` or `alertdialog`

| Key | Behavior |
|-----|---------|
| `Tab` | Move focus to next focusable element in dialog; wrap to first if at last |
| `Shift + Tab` | Move focus to previous focusable element; wrap to last if at first |
| `Escape` | Close the dialog; return focus to trigger element |

See `domains/web/component-patterns/modal-dialog.md` for complete implementation.

---

### Disclosure (Show/Hide)

**Role:** `button` (trigger), any role (controlled content)

| Key | Behavior |
|-----|---------|
| `Enter` / `Space` | Toggle visibility of controlled content |

```html
<button type="button" aria-expanded="false" aria-controls="more-info">
  Show more information
</button>
<div id="more-info" hidden>
  Additional content here...
</div>
```

---

### Link

**Role:** `link`

| Key | Behavior |
|-----|---------|
| `Enter` | Activate link (navigate or trigger action) |

Note: Space does NOT activate links (unlike buttons). Using a link as a button is a common mistake.

---

### Listbox (Single-Select)

**Role:** `listbox` (container), `option` (items)

| Key | Behavior |
|-----|---------|
| `Down Arrow` | Move focus to next option |
| `Up Arrow` | Move focus to previous option |
| `Home` | Move focus to first option |
| `End` | Move focus to last option |
| `Enter` / `Space` | Select focused option |
| `Type-ahead` | Type characters to move focus to matching option |

```html
<ul role="listbox" aria-label="Choose a color" tabindex="0">
  <li role="option" aria-selected="true">Red</li>
  <li role="option" aria-selected="false">Blue</li>
  <li role="option" aria-selected="false">Green</li>
</ul>
```

---

### Menu and Menu Button

**Roles:** `button` (trigger), `menu` (container), `menuitem`, `menuitemcheckbox`, `menuitemradio`

| Key | Behavior |
|-----|---------|
| `Enter` / `Space` | Open menu; focus first item |
| `Down Arrow` | Move focus to next item (wraps) |
| `Up Arrow` | Move focus to previous item (wraps) |
| `Home` | Move focus to first item |
| `End` | Move focus to last item |
| `Escape` | Close menu; return focus to button |
| `Enter` (on item) | Execute action; close menu |
| `Space` (on menuitemcheckbox) | Toggle state without closing |
| `Tab` | Close menu; move focus to next element |

```html
<button aria-haspopup="menu" aria-expanded="false" id="menu-btn">
  Actions
</button>
<ul role="menu" aria-labelledby="menu-btn" hidden>
  <li role="menuitem">Edit</li>
  <li role="menuitem">Delete</li>
  <li role="separator"></li>
  <li role="menuitem">Export</li>
</ul>
```

---

### Radio Group

**Roles:** `radiogroup` (container), `radio` (items)

| Key | Behavior |
|-----|---------|
| `Tab` | Move focus into the radio group (to the checked radio or first if none checked) |
| `Down Arrow` / `Right Arrow` | Move focus to next radio AND select it (automatic selection) |
| `Up Arrow` / `Left Arrow` | Move focus to previous radio AND select it (automatic selection) |
| `Space` | Select focused radio if not already selected |

Note: Radio groups use automatic selection on arrow key navigation (unlike listboxes which require Enter/Space to select).

```html
<fieldset>
  <legend>Preferred notification method</legend>
  <div role="radiogroup" aria-labelledby="notif-legend">
    <label><input type="radio" name="notif" value="email"> Email</label>
    <label><input type="radio" name="notif" value="sms"> SMS</label>
  </div>
</fieldset>
```

Use native `<input type="radio">` whenever possible; the above ARIA pattern is for custom radio controls.

---

### Slider

**Role:** `slider`

| Key | Behavior |
|-----|---------|
| `Right Arrow` / `Up Arrow` | Increase value by one step |
| `Left Arrow` / `Down Arrow` | Decrease value by one step |
| `Page Up` | Increase by larger step (commonly 10%) |
| `Page Down` | Decrease by larger step |
| `Home` | Set to minimum value |
| `End` | Set to maximum value |

```html
<div
  role="slider"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-valuenow="50"
  aria-valuetext="50%"
  aria-label="Volume"
  tabindex="0"
>
</div>
```

---

### Switch

**Role:** `switch`

| Key | Behavior |
|-----|---------|
| `Space` | Toggle switch state |

States: `aria-checked="true"` (on), `aria-checked="false"` (off)

```html
<button role="switch" aria-checked="false">
  Dark mode
</button>
```

---

### Tab Panel

**Roles:** `tablist` (container), `tab` (items), `tabpanel` (content)

#### Tabs with Automatic Activation

| Key | Behavior |
|-----|---------|
| `Left Arrow` | Move focus to previous tab AND activate it |
| `Right Arrow` | Move focus to next tab AND activate it |
| `Home` | Move focus and activate first tab |
| `End` | Move focus and activate last tab |
| `Tab` | Move focus to active tabpanel content |
| `Shift + Tab` | Move focus back to active tab from tabpanel |

#### Tabs with Manual Activation

| Key | Behavior |
|-----|---------|
| `Left Arrow` | Move focus to previous tab (do NOT activate) |
| `Right Arrow` | Move focus to next tab (do NOT activate) |
| `Space` / `Enter` | Activate focused tab |

```html
<div role="tablist" aria-label="Product information">
  <button role="tab" aria-selected="true" aria-controls="panel-overview" id="tab-overview">Overview</button>
  <button role="tab" aria-selected="false" aria-controls="panel-specs" id="tab-specs" tabindex="-1">Specifications</button>
</div>
<div role="tabpanel" id="panel-overview" aria-labelledby="tab-overview">
  Overview content...
</div>
<div role="tabpanel" id="panel-specs" aria-labelledby="tab-specs" hidden>
  Specifications content...
</div>
```

---

### Toolbar

**Role:** `toolbar`

| Key | Behavior |
|-----|---------|
| `Left Arrow` | Move focus to previous control |
| `Right Arrow` | Move focus to next control |
| `Home` | Move focus to first control |
| `End` | Move focus to last control |
| `Tab` | Move focus to next element outside toolbar |

Toolbar uses roving tabindex — only one control has tabindex="0" at a time.

---

### Tooltip

**Role:** `tooltip`

| Key | Behavior |
|-----|---------|
| `Escape` | Dismiss the tooltip (required by SC 1.4.13) |
| Mouse hover | Show tooltip (pointer must be able to move into tooltip) |
| Focus | Show tooltip when trigger receives focus |

```html
<button aria-describedby="tip-1" id="btn-info">
  More info
</button>
<div role="tooltip" id="tip-1" hidden>
  This action cannot be undone.
</div>
```

---

### Tree View

**Roles:** `tree` (container), `treeitem` (items), `group` (child groups)

| Key | Behavior |
|-----|---------|
| `Down Arrow` | Move focus to next visible treeitem |
| `Up Arrow` | Move focus to previous visible treeitem |
| `Right Arrow` | If closed: expand; if open: move focus to first child |
| `Left Arrow` | If open: collapse; if closed: move focus to parent |
| `Enter` | Activate treeitem |
| `Home` | Move focus to first treeitem |
| `End` | Move focus to last visible treeitem |
| Type-ahead | Move focus to next matching item |

```html
<ul role="tree" aria-label="File explorer">
  <li role="treeitem" aria-expanded="false">
    <span>Documents</span>
    <ul role="group">
      <li role="treeitem">Report.pdf</li>
      <li role="treeitem">Notes.docx</li>
    </ul>
  </li>
</ul>
```

---

## Key Selection: Enter vs. Space

| Control type | Enter | Space |
|---|---|---|
| Link | Activate | Does nothing |
| Button | Activate | Activate |
| Checkbox | N/A | Toggle |
| Radio | N/A | Select (Arrow key also selects) |
| Select/Combobox | Select option | Select option |
| Menu item | Activate | Activate |
| Tab | Activate (manual) | Activate (manual) |
| Dialog button | Activate | Activate |

**Rule:** Links use Enter only. Buttons (and button-like controls) use both Enter and Space.
