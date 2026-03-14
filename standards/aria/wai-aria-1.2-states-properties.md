---
title: "WAI-ARIA 1.2 States and Properties Reference"
standard: "WAI-ARIA 1.2"
source_url: "https://www.w3.org/TR/wai-aria-1.2/#state_prop_def"
domain: ["web"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["aria", "states", "properties", "attributes", "wai-aria"]
ai_context: "All WAI-ARIA 1.2 states and properties with allowed values, applicable roles, and usage notes. Use to ensure ARIA attribute values are valid and attributes are used on appropriate roles."
---

# WAI-ARIA 1.2 States and Properties Reference

**States** are dynamic properties that change in response to user interaction or application events. **Properties** are attributes that are less likely to change but provide essential information to AT.

Both use the `aria-*` attribute syntax in HTML.

---

## Global States and Properties

These may be used on any HTML element with a role, or on any element that can receive focus.

| Attribute | Type | Values | Description |
|-----------|------|--------|-------------|
| `aria-atomic` | property | `true`, `false` (default) | When used in live region, whether AT presents entire region as a whole (`true`) or only changed nodes (`false`) |
| `aria-busy` | state | `true`, `false` (default) | Element is being updated — AT should wait before presenting changes |
| `aria-controls` | property | ID reference(s) | Identifies element(s) controlled by this element |
| `aria-current` | state | `page`, `step`, `location`, `date`, `time`, `true`, `false` (default) | Indicates this element is the current item within a container or set |
| `aria-describedby` | property | ID reference(s) | Identifies element(s) that describe this element (supplementary to label) |
| `aria-details` | property | ID reference | Identifies element providing a detailed description |
| `aria-disabled` | state | `true`, `false` (default) | Element is visible but not interactive. Different from HTML `disabled`: AT still reads the element |
| `aria-dropeffect` | property | *Deprecated in ARIA 1.1* | Do not use |
| `aria-errormessage` | property | ID reference | Identifies element containing error message; use with `aria-invalid="true"` |
| `aria-flowto` | property | ID reference(s) | Provides alternate reading order |
| `aria-grabbed` | state | *Deprecated in ARIA 1.1* | Do not use |
| `aria-haspopup` | property | `false` (default), `true`, `menu`, `listbox`, `tree`, `grid`, `dialog` | Indicates element will open a popup |
| `aria-hidden` | state | `true`, `false`, undefined (default) | `true` removes element and children from accessibility tree. **Never use on focusable elements.** |
| `aria-invalid` | state | `false` (default), `true`, `grammar`, `spelling` | Indicates field value is invalid. Use with `aria-errormessage` |
| `aria-keyshortcuts` | property | string | Documents keyboard shortcuts for element |
| `aria-label` | property | string | Provides accessible name when no visible label exists |
| `aria-labelledby` | property | ID reference(s) | Identifies element(s) that label this element. Takes precedence over `aria-label` |
| `aria-live` | property | `off` (default), `polite`, `assertive` | Indicates live region update behavior. `polite` = wait for idle; `assertive` = interrupt immediately |
| `aria-owns` | property | ID reference(s) | Identifies children not present in DOM hierarchy |
| `aria-relevant` | property | `additions`, `all`, `removals`, `text` (default: `additions text`) | What types of changes in a live region trigger announcements |
| `aria-roledescription` | property | string | Human-readable description of role. Use sparingly; only to clarify role purpose |

---

## Widget States and Properties

### aria-autocomplete

**Type:** Property
**Values:** `none` (default), `inline`, `list`, `both`
**Applicable roles:** `combobox`, `textbox`, `searchbox`

- `none`: no suggestion
- `inline`: suggestion appended in input
- `list`: dropdown list appears
- `both`: inline + list

### aria-checked

**Type:** State
**Values:** `true`, `false`, `mixed`, `undefined`
**Applicable roles:** `checkbox`, `menuitemcheckbox`, `option`, `radio`, `switch`, `treeitem`

- `mixed`: partially checked state (indeterminate) — valid for `checkbox`, `menuitemcheckbox` only
- `undefined` (omitting the attribute): not checkable

**Example:** `<div role="checkbox" aria-checked="false">Subscribe</div>`

### aria-disabled

**Type:** State
**Values:** `true`, `false` (default)
**Applicable roles:** All interactive roles

- AT reads disabled elements; keyboard focus behavior depends on implementation
- HTML `disabled` attribute removes element from accessibility tree entirely in some AT; `aria-disabled="true"` keeps it visible but inoperable
- Prefer HTML `disabled` for form controls; use `aria-disabled` for custom controls

### aria-expanded

**Type:** State
**Values:** `true`, `false`, `undefined` (not expandable)
**Applicable roles:** `button`, `combobox`, `listbox`, `section`, `select`, `rowgroup`, `treeitem`, `row`, `tab`

- Must be present on disclosure buttons, menu triggers, accordions, tree items
- `undefined` (omit attribute): element is not expandable

**Example:** `<button aria-expanded="false" aria-controls="menu">Menu</button>`

### aria-grabbed

**Type:** State — **DEPRECATED in ARIA 1.1**
Do not use. Use `aria-grabbed` only if supporting ARIA 1.0; prefer `draggable` + `aria-dropeffect` pattern (also deprecated) or custom drag-and-drop implementation with keyboard support per SC 2.5.7.

### aria-hidden

**Type:** State
**Values:** `true`, `false`, `undefined` (default)

**Critical rules:**
- `aria-hidden="true"` removes element AND all descendants from accessibility tree
- NEVER set `aria-hidden="true"` on an element that is focusable or contains focusable elements
- NEVER set on `<html>` or `<body>`
- Use to hide decorative icons, duplicate content, off-screen panels not in use

**Example:** `<span aria-hidden="true">★</span><span class="sr-only">5 stars</span>`

### aria-invalid

**Type:** State
**Values:** `false` (default), `true`, `grammar`, `spelling`
**Applicable roles:** `application`, `checkbox`, `combobox`, `gridcell`, `listbox`, `radiogroup`, `rowheader`, `searchbox`, `select`, `slider`, `spinbutton`, `textbox`, `columnheader`, `tree`, `treegrid`

- Set to `true` on fields that fail validation
- Always pair with `aria-errormessage` pointing to error text
- Set back to `false` (or remove) when error is corrected

### aria-modal

**Type:** Property
**Values:** `true`, `false` (default)
**Applicable roles:** `dialog`, `alertdialog`

- Tells AT that content behind the modal is inert
- Does NOT automatically make background content inoperable — must also manage focus and keyboard interactions programmatically
- Required on all modal dialogs

### aria-multiline

**Type:** Property
**Values:** `true`, `false` (default)
**Applicable roles:** `textbox`, `searchbox`

- `true`: Enter key inserts new line (like `<textarea>`)
- `false`: Enter key submits (like `<input type="text">`)

### aria-multiselectable

**Type:** Property
**Values:** `true`, `false` (default)
**Applicable roles:** `grid`, `listbox`, `tablist`, `tree`, `treegrid`

### aria-orientation

**Type:** Property
**Values:** `horizontal`, `vertical`, `undefined` (default)
**Applicable roles:** `scrollbar`, `select`, `separator`, `slider`, `tablist`, `toolbar`

- Affects keyboard interaction: horizontal → Left/Right arrows; vertical → Up/Down arrows
- Default for `tablist` is horizontal; for `listbox` and `tree` is vertical

### aria-placeholder

**Type:** Property
**Values:** string
**Applicable roles:** `textbox`, `searchbox`

- Provides hint text when field is empty
- NOT a substitute for a label
- Disappears when user types

### aria-pressed

**Type:** State
**Values:** `true`, `false`, `mixed`, `undefined`
**Applicable roles:** `button`

- Use for toggle buttons only
- `undefined` (omit): not a toggle button
- `mixed`: partially pressed (rare)

### aria-readonly

**Type:** Property
**Values:** `true`, `false` (default)
**Applicable roles:** `checkbox`, `combobox`, `grid`, `gridcell`, `listbox`, `radiogroup`, `slider`, `spinbutton`, `textbox`, `columnheader`, `rowheader`

- Value is not editable but is still operable (submittable, copyable)
- Differs from `aria-disabled`: readonly value participates in form submission

### aria-required

**Type:** Property
**Values:** `true`, `false` (default)
**Applicable roles:** `checkbox`, `combobox`, `gridcell`, `listbox`, `radiogroup`, `select`, `spinbutton`, `textbox`, `tree`

- **Prefer HTML `required` attribute** on native form controls
- Use `aria-required` only on custom controls
- Does not provide visual indicator — must add visual indicator separately

### aria-selected

**Type:** State
**Values:** `true`, `false`, `undefined` (not selectable)
**Applicable roles:** `gridcell`, `option`, `row`, `rowheader`, `tab`, `treeitem`, `columnheader`

- `undefined`: element is not selectable
- `false`: selectable but not selected
- `true`: currently selected

### aria-sort

**Type:** Property
**Values:** `ascending`, `descending`, `none`, `other`
**Applicable roles:** `columnheader`, `rowheader`

- Applied to sortable table column or row headers
- Only one header should have `ascending` or `descending` at a time; others should be `none`

---

## Range Properties

Used for sliders, spinbuttons, progress bars, scrollbars.

### aria-valuemax

**Type:** Property
**Values:** number
**Applicable roles:** `meter`, `progressbar`, `scrollbar`, `separator`, `slider`, `spinbutton`

### aria-valuemin

**Type:** Property
**Values:** number
**Applicable roles:** Same as aria-valuemax

### aria-valuenow

**Type:** Property
**Values:** number
**Applicable roles:** Same as aria-valuemax

### aria-valuetext

**Type:** Property
**Values:** string
**Applicable roles:** Same as aria-valuemax

- Human-readable text alternative for `aria-valuenow`
- Required when numeric value has non-obvious meaning (e.g., a slider for temperature: "72°F" instead of "72")

**Example:**
```html
<div role="slider"
     aria-valuemin="0"
     aria-valuemax="100"
     aria-valuenow="72"
     aria-valuetext="72 degrees Fahrenheit"
     tabindex="0">
</div>
```

---

## Relationship Properties

### aria-activedescendant

**Type:** Property
**Values:** ID reference
**Applicable roles:** `application`, `composite`, `group`, `textbox`, and widget roles

- Used in composite widgets (listbox, tree, grid) where the widget container has focus but a descendant is the "active" item
- Avoids moving actual DOM focus; the container remains focused
- AT reads the active descendant instead of the container

**Example:** `<ul role="listbox" tabindex="0" aria-activedescendant="opt2">...`

### aria-colcount / aria-colindex / aria-colspan

For tables and grids where not all columns are present in the DOM (virtualized tables).

- `aria-colcount`: Total column count
- `aria-colindex`: Column position (1-based) of cell or header
- `aria-colspan`: Number of columns the cell spans (replaces HTML `colspan` in custom grids)

### aria-rowcount / aria-rowindex / aria-rowspan

Same as above for rows.

### aria-posinset / aria-setsize

Used in virtualized or paginated lists where not all items are in the DOM.

- `aria-setsize`: Total number of items in the set
- `aria-posinset`: Position of this item in the set (1-based)

**Example:** For a virtualized listbox showing items 11-20 of 100:
```html
<li role="option" aria-setsize="100" aria-posinset="11">Item 11</li>
```

### aria-level

**Type:** Property
**Values:** integer ≥ 1
**Applicable roles:** `heading`, `listitem`, `row`, `tabitem`

- `role="heading" aria-level="2"` is equivalent to `<h2>`
- Prefer native `<h1>`–`<h6>` elements

---

## Live Region Properties

### aria-live

**Values:** `off`, `polite`, `assertive`

| Value | Behavior | When to Use |
|-------|----------|-------------|
| `off` | No announcement | Default; no live region |
| `polite` | Announces when user is idle | Status updates, notifications, search results |
| `assertive` | Interrupts current announcement | Errors, critical alerts, time-sensitive |

**Rules:**
- Use `polite` by default; `assertive` only for errors and urgent messages
- `assertive` interrupts screen reader users mid-sentence — use sparingly
- Role `alert` implies `aria-live="assertive"`; role `status` implies `aria-live="polite"`
- Add live region to DOM before content changes; don't inject the live region dynamically

### aria-atomic

**Values:** `true`, `false` (default)

- `true`: Announce the entire live region when any part changes
- `false`: Announce only the changed nodes

### aria-relevant

**Values:** `additions`, `removals`, `text`, `all` (default: `additions text`)

- What types of DOM changes trigger announcements
- `additions text` is the default (new child nodes or text changes)
- `removals` causes announcements when elements are removed — use with caution (noisy)

---

## New in WAI-ARIA 1.2

### aria-braillelabel

**Type:** Property
**Values:** string
**Applicable roles:** Any

- Provides a braille-specific label that overrides the accessible name for braille display output
- Use only when the visual text representation is inappropriate for braille rendering

### aria-brailleroledescription

**Type:** Property
**Values:** string
**Applicable roles:** Any with a role

- Braille-specific role description (overrides `aria-roledescription` for braille)

### aria-description

**Type:** Property (new in ARIA 1.2)
**Values:** string
**Applicable roles:** Any

- Provides an accessible description (like `aria-describedby` but as a string, not an ID reference)
- Use `aria-describedby` when the description text is visible on page; use `aria-description` for invisible descriptions

---

## Quick Validation Rules

1. `aria-label` and `aria-labelledby` define the accessible **name** — they override the element's text content as the name
2. `aria-describedby` provides supplementary **description** — read after the name
3. `aria-hidden="true"` removes from AT — never on focusable elements
4. `aria-disabled="true"` keeps in AT but marks as inactive — does not remove from tab order
5. `aria-required` is for custom controls; use HTML `required` for native form elements
6. `aria-invalid` must be paired with `aria-errormessage` pointing to visible error text
7. `aria-expanded` is required on all disclosure controls (menus, accordions, dropdowns)
8. `aria-live` regions must exist in DOM before content changes
9. `aria-label` on elements with no interactive role is only valid if it aids in identification (use sparingly)
10. All ID references (aria-labelledby, aria-describedby, etc.) must point to existing elements in the DOM
