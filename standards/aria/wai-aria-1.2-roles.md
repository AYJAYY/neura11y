---
title: "WAI-ARIA 1.2 Roles Reference"
standard: "WAI-ARIA 1.2"
source_url: "https://www.w3.org/TR/wai-aria-1.2/#role_definitions"
domain: ["web"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["aria", "roles", "wai-aria", "semantics"]
ai_context: "Complete WAI-ARIA 1.2 roles reference. Use when generating or auditing ARIA role usage. Each role entry includes required/supported states and properties, and HTML implicit mapping."
---

# WAI-ARIA 1.2 Roles Reference

WAI-ARIA roles classify elements by their function in the accessibility tree. Roles are divided into abstract, widget, composite widget, document structure, and landmark categories. Abstract roles are never used directly in markup; they form the inheritance hierarchy.

---

## Widget Roles

Widget roles identify interactive user interface components.

### `alert`
A live region containing a brief, important message that does not require user interaction. Implicitly has `aria-live="assertive"` and `aria-atomic="true"`.

- **Superclass:** `section`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** none
- **Usage notes:** Do not use `aria-live` on an `alert`; the implicit value is already `assertive`. Inject alert content dynamically — the element should exist in DOM before content is added. Do not use for error messages on form fields; use `aria-errormessage` instead.

---

### `alertdialog`
A type of dialog containing an alert message that requires user acknowledgment before the workflow can continue.

- **Superclass:** `alert`, `dialog`
- **Required states/properties:** none (accessible name via `aria-label` or `aria-labelledby` is required in practice)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-modal`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** none
- **Usage notes:** Focus must be moved inside the dialog on open. Must have an accessible name. Combine with `aria-modal="true"` when rendering as a modal. At least one focusable element must be inside.

---

### `button`
An interactive element activated by user input (click, Enter, Space) that triggers an action.

- **Superclass:** `command`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-pressed`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** `<button>`, `<input type="button">`, `<input type="image">`, `<input type="reset">`, `<input type="submit">`, `<summary>`
- **Usage notes:** Toggle buttons use `aria-pressed` (`true`/`false`/`mixed`). Use `aria-haspopup` when button opens a menu, listbox, tree, grid, or dialog. Prefer native `<button>` element.

---

### `checkbox`
A checkable input that has three possible values: `true`, `false`, or `mixed`.

- **Superclass:** `input`
- **Required states/properties:** `aria-checked` (`true` | `false` | `mixed`)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`
- **HTML implicit role:** `<input type="checkbox">`
- **Usage notes:** `aria-checked="mixed"` represents an indeterminate/tri-state checkbox. Authors must manage `aria-checked` state on custom checkboxes. Native `<input type="checkbox">` is strongly preferred.

---

### `combobox`
An input widget that can show a popup (listbox, grid, tree, or dialog) for selecting a value.

- **Superclass:** `select`
- **Required states/properties:** `aria-controls` (ID of the popup), `aria-expanded` (`true` | `false`)
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-autocomplete`, `aria-busy`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-multiline`, `aria-owns`, `aria-placeholder`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`
- **HTML implicit role:** `<select>` (when `size` attribute is absent or 1 and `multiple` is absent)
- **Usage notes:** ARIA 1.2 places `role="combobox"` on the text input itself (not a container). Use `aria-haspopup` to indicate the popup type. The popup container must have `role="listbox"`, `role="grid"`, `role="tree"`, or `role="dialog"`.

---

### `dialog`
A window overlaid on either the primary window or another dialog, rendering the parent content inert.

- **Superclass:** `window`
- **Required states/properties:** none (accessible name required in practice)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-modal`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** `<dialog>`
- **Usage notes:** Add `aria-modal="true"` when the dialog is modal to communicate to assistive technologies that background content is inert. Focus must move into the dialog when opened and return to the trigger when closed. Escape key should close the dialog.

---

### `feed`
A scrollable list of articles where new articles can be added when the user scrolls to the end.

- **Superclass:** `list`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **Owned elements:** `article`
- **HTML implicit role:** none
- **Usage notes:** Each article must have `aria-posinset` and `aria-setsize`. When the set size is unknown, set `aria-setsize="-1"`. Articles should be navigable with Page Down / Page Up within the feed container.

---

### `gridcell`
A cell in a grid or treegrid. May contain interactive content.

- **Superclass:** `cell`, `widget`
- **Required states/properties:** none
- **Supported states/properties:** `aria-colindex`, `aria-colspan`, `aria-disabled`, `aria-errormessage`, `aria-expanded`, `aria-haspopup`, `aria-invalid`, `aria-readonly`, `aria-required`, `aria-rowindex`, `aria-rowspan`, `aria-selected` — plus all global states/properties
- **HTML implicit role:** none (use `<td>` in a grid)
- **Usage notes:** Unlike `cell`, `gridcell` may be focusable. Use `aria-selected` to indicate selection. Use `aria-readonly="true"` if the cell cannot be edited.

---

### `link`
An interactive reference to an internal or external resource.

- **Superclass:** `command`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** `<a href="...">`, `<area href="...">`
- **Usage notes:** Activated with Enter key. A link without an `href` has the `generic` implicit role, not `link`. Do not use `role="link"` on a `<button>`; use the appropriate element for the action type.

---

### `listbox`
A widget containing a list of options from which the user can select.

- **Superclass:** `select`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-multiselectable`, `aria-orientation`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`
- **Owned elements:** `option`, `group` (containing `option`)
- **HTML implicit role:** `<select>` (when `size > 1` or `multiple` present), `<datalist>`
- **Usage notes:** Must contain `role="option"` elements. Use `aria-multiselectable="true"` for multi-select listboxes. Use `aria-activedescendant` to track focus within the listbox (roving tabindex is an alternative).

---

### `log`
A live region where new information is added in meaningful order and old information may disappear.

- **Superclass:** `section`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** none
- **Usage notes:** Implicitly has `aria-live="polite"`. Common examples: chat logs, error logs. For content that must interrupt immediately, use `role="alert"` instead.

---

### `marquee`
A type of live region where non-essential information changes frequently.

- **Superclass:** `section`
- **Required states/properties:** none
- **Supported states/properties:** Global states/properties
- **HTML implicit role:** none
- **Usage notes:** Implicitly `aria-live="off"` — changes are not announced automatically. Primarily exists for legacy content. Avoid for important information. Note: this is unrelated to the deprecated `<marquee>` HTML element.

---

### `menuitem`
A single choice in a menu.

- **Superclass:** `command`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-posinset`, `aria-relevant`, `aria-roledescription`, `aria-setsize`
- **HTML implicit role:** none
- **Usage notes:** Must be an owned element of `menu` or `menubar`. Activated with Enter or Space. Use `aria-haspopup` if it opens a submenu.

---

### `menuitemcheckbox`
A checkable menuitem that can be toggled on or off.

- **Superclass:** `menuitem`, `checkbox`
- **Required states/properties:** `aria-checked` (`true` | `false` | `mixed`)
- **Supported states/properties:** Same as `menuitem` plus `aria-checked`
- **HTML implicit role:** none
- **Usage notes:** Must be owned by `menu` or `menubar`. Toggled with Space key in addition to Enter. Unlike standard checkboxes, typically uses `aria-checked="mixed"` sparingly.

---

### `menuitemradio`
A checkable menuitem in a group where only one item can be checked at a time.

- **Superclass:** `menuitem`, `radio`
- **Required states/properties:** `aria-checked` (`true` | `false`)
- **Supported states/properties:** Same as `menuitem` plus `aria-checked`, `aria-posinset`, `aria-setsize`
- **HTML implicit role:** none
- **Usage notes:** Must be owned by `menu` or `menubar`. Only one item in a radio group can have `aria-checked="true"` at a time.

---

### `option`
A selectable item in a listbox.

- **Superclass:** `input`
- **Required states/properties:** `aria-selected` (`true` | `false`)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-checked`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-posinset`, `aria-relevant`, `aria-roledescription`, `aria-setsize`
- **HTML implicit role:** `<option>`
- **Usage notes:** Must be owned by a `listbox`. `aria-selected` must always be explicitly set; the default is `false`. Not to be confused with `menuitem`.

---

### `progressbar`
Displays the completion progress of a task. May be determinate or indeterminate.

- **Superclass:** `range`, `widget`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`, `aria-valuemax`, `aria-valuemin`, `aria-valuenow`, `aria-valuetext`
- **HTML implicit role:** `<progress>`
- **Usage notes:** For determinate progress, set `aria-valuenow`, `aria-valuemin` (default 0), and `aria-valuemax` (default 100). For indeterminate progress, omit `aria-valuenow`. Use `aria-valuetext` to provide a human-readable description (e.g., "Step 3 of 5").

---

### `radio`
A checkable input in a group where only one can be checked at a time.

- **Superclass:** `input`
- **Required states/properties:** `aria-checked` (`true` | `false`)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-posinset`, `aria-relevant`, `aria-required`, `aria-roledescription`, `aria-setsize`
- **HTML implicit role:** `<input type="radio">`
- **Usage notes:** Group radio buttons in a `radiogroup`. Use arrow keys to navigate within the group. Only one item should have `aria-checked="true"` within a group at a time.

---

### `scrollbar`
A graphical range object that controls scrolling of content within a viewport.

- **Superclass:** `range`
- **Required states/properties:** `aria-controls` (ID of scrollable element), `aria-orientation`, `aria-valuenow`, `aria-valuemax` (default 100), `aria-valuemin` (default 0)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`, `aria-valuetext`
- **HTML implicit role:** none
- **Usage notes:** Rarely needed since native scrollbars are accessible. Only use for custom scrollbar implementations. `aria-orientation` defaults to `vertical`.

---

### `searchbox`
A text field used for entering search queries.

- **Superclass:** `textbox`
- **Required states/properties:** none
- **Supported states/properties:** Same as `textbox`
- **HTML implicit role:** `<input type="search">`
- **Usage notes:** Prefer native `<input type="search">` over `role="searchbox"`. Combine the search input with a `search` landmark role on the containing element.

---

### `separator` (when focusable)
A divider that separates and distinguishes sections of content. When focusable, it is a widget role.

- **Superclass:** `structure`, `widget`
- **Required states/properties:** `aria-valuenow` (when focusable/resizable)
- **Supported states/properties:** `aria-orientation`, `aria-valuemax`, `aria-valuemin`, `aria-valuenow`, `aria-valuetext` — plus global states/properties
- **HTML implicit role:** `<hr>` (as non-focusable separator)
- **Usage notes:** Non-focusable `<hr>` has implicit role `separator` as a structure role. As a focusable widget, it acts as a splitter bar that can be moved.

---

### `slider`
An input where the user selects a value from within a given range by moving a thumb control.

- **Superclass:** `input`, `range`
- **Required states/properties:** `aria-valuenow`
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-orientation`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`, `aria-valuemax`, `aria-valuemin`, `aria-valuetext`
- **HTML implicit role:** `<input type="range">`
- **Usage notes:** `aria-valuemin` defaults to 0, `aria-valuemax` defaults to 100. Arrow keys increase/decrease value. Home/End go to min/max. Provide `aria-valuetext` for non-numeric value representations.

---

### `spinbutton`
An input that allows the user to select a value from a discrete range by typing or clicking increment/decrement buttons.

- **Superclass:** `composite`, `input`, `range`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`, `aria-valuemax`, `aria-valuemin`, `aria-valuenow`, `aria-valuetext`
- **HTML implicit role:** `<input type="number">`
- **Usage notes:** Arrow Up/Down keys increase/decrease value. Page Up/Down change by a larger step. Home/End go to min/max values. If a step is fractional, `aria-valuetext` should present the formatted value.

---

### `status`
A live region whose content is advisory information but not important enough to warrant an alert.

- **Superclass:** `section`
- **Required states/properties:** none
- **Supported states/properties:** Global states/properties
- **HTML implicit role:** `<output>`
- **Usage notes:** Implicitly `aria-live="polite"` and `aria-atomic="true"`. Common use: "3 results found", "Saving...", "Form submitted successfully". Do not use for critical errors — use `role="alert"`.

---

### `switch`
A type of checkbox that represents on/off values rather than checked/unchecked.

- **Superclass:** `checkbox`
- **Required states/properties:** `aria-checked` (`true` | `false`)
- **Supported states/properties:** Same as `checkbox`
- **Prohibited states/properties:** `aria-checked="mixed"` is not supported
- **HTML implicit role:** none
- **Usage notes:** Semantically identical to `checkbox` but communicates an on/off concept. Screen readers announce "on" or "off" instead of "checked" or "unchecked". Space key toggles the switch.

---

### `tab`
An interactive element in a tablist that activates its associated tabpanel when selected.

- **Superclass:** `sectionhead`, `widget`
- **Required states/properties:** none
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-posinset`, `aria-relevant`, `aria-roledescription`, `aria-selected`, `aria-setsize`
- **HTML implicit role:** none
- **Usage notes:** Use `aria-selected="true"` on the active tab. Tabs should be children of a `tablist`. The associated panel is referenced via `aria-controls` (or `aria-owns`). Arrow keys navigate between tabs.

---

### `tabpanel`
A container for the resources associated with a tab.

- **Superclass:** `section`
- **Required states/properties:** none (accessible name required in practice)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **HTML implicit role:** none
- **Usage notes:** Should be labelled by its associated tab using `aria-labelledby`. Inactive tabpanels may use `hidden` attribute or `aria-hidden="true"` to hide from all users. Tabpanel receives focus when Tab is pressed from within its tab.

---

### `textbox`
A text entry widget.

- **Superclass:** `input`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-autocomplete`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-multiline`, `aria-owns`, `aria-placeholder`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`
- **HTML implicit role:** `<input type="text">`, `<input type="email">`, `<input type="tel">`, `<input type="url">`, `<textarea>`
- **Usage notes:** `aria-multiline="true"` indicates a multi-line text field. Use `aria-placeholder` for placeholder text (but always include a label). Use `aria-autocomplete` to describe autocomplete behavior.

---

### `timer`
A live region containing a numerical counter that indicates elapsed or remaining time.

- **Superclass:** `section`
- **Required states/properties:** none
- **Supported states/properties:** Global states/properties
- **HTML implicit role:** none
- **Usage notes:** Implicitly `aria-live="off"` — time updates are not automatically announced. When the timer expires, use a more assertive notification method. Avoid creating timers that force users to act quickly.

---

### `tooltip`
A contextual popup providing a description for an element when it receives keyboard focus or pointer hover.

- **Superclass:** `section`
- **Required states/properties:** none
- **Supported states/properties:** Global states/properties
- **HTML implicit role:** none
- **Usage notes:** Reference the tooltip from its owner using `aria-describedby`. Tooltips should not contain focusable content. They are shown on focus and hover; they must be dismissible with Escape. Do not use to convey the accessible name — that is `aria-label`/`aria-labelledby`.

---

### `treeitem`
An option in a tree widget that may be expanded or collapsed.

- **Superclass:** `listitem`, `option`
- **Required states/properties:** none (but `aria-expanded` required if the item has children)
- **Supported states/properties:** `aria-atomic`, `aria-busy`, `aria-checked`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-haspopup`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-level`, `aria-live`, `aria-owns`, `aria-posinset`, `aria-relevant`, `aria-roledescription`, `aria-selected`, `aria-setsize`
- **HTML implicit role:** none
- **Usage notes:** Must be owned by `tree` or `group` (within a tree). Use `aria-level`, `aria-setsize`, and `aria-posinset` for positioning. `aria-expanded` toggles with Space or Enter. Arrow keys navigate the tree.

---

## Composite Widget Roles

Composite widget roles manage a set of owned interactive children.

### `combobox`
See Widget Roles section above.

---

### `grid`
A composite widget containing a collection of one or more rows with one or more cells; can be editable.

- **Superclass:** `composite`, `table`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-colcount`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-multiselectable`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-roledescription`, `aria-rowcount`
- **Owned elements:** `row`, `rowgroup` (containing `row`)
- **HTML implicit role:** none
- **Usage notes:** Unlike `table`, `grid` is interactive. Cells may be focusable and editable. Use arrow keys for 2D navigation. Rows may be selectable. Consider `aria-multiselectable` for multi-row selection.

---

### `listbox`
See Widget Roles section above.

---

### `menu`
A widget that offers a list of choices to the user.

- **Superclass:** `select`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-orientation`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **Owned elements:** `menuitem`, `menuitemcheckbox`, `menuitemradio`, `group` (of above)
- **HTML implicit role:** none
- **Usage notes:** Menus are opened by a trigger (button or menuitem). Arrow keys navigate items. Escape closes the menu and returns focus to trigger. Tab closes menu. Menus are transient — they do not replace page navigation.

---

### `menubar`
A presentation of menu that usually remains visible.

- **Superclass:** `menu`
- **Required states/properties:** none
- **Supported states/properties:** Same as `menu`
- **Owned elements:** `menuitem`, `menuitemcheckbox`, `menuitemradio`
- **HTML implicit role:** none
- **Usage notes:** Typically horizontal. Left/Right arrows navigate items in the menubar; Down arrow opens a submenu. Used for application-style menu bars, not for site navigation (use `nav` for that).

---

### `radiogroup`
A group of radio buttons.

- **Superclass:** `select`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`
- **Owned elements:** `radio`
- **HTML implicit role:** `<fieldset>` (partially — `fieldset` maps to `group`, not `radiogroup`)
- **Usage notes:** Arrow keys navigate between radio buttons within the group. Only one radio should be `aria-checked="true"`. Prefer native `<fieldset>` + `<legend>` + `<input type="radio">`.

---

### `tablist`
A container for a set of tab elements.

- **Superclass:** `composite`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-multiselectable`, `aria-orientation`, `aria-owns`, `aria-relevant`, `aria-roledescription`
- **Owned elements:** `tab`
- **HTML implicit role:** none
- **Usage notes:** `aria-orientation` can be `horizontal` (default) or `vertical`. Arrow keys navigate between tabs. Tab key moves focus out of the tablist into the active tabpanel.

---

### `tree`
A widget that presents a hierarchical list.

- **Superclass:** `select`
- **Required states/properties:** none
- **Supported states/properties:** `aria-activedescendant`, `aria-atomic`, `aria-busy`, `aria-controls`, `aria-current`, `aria-describedby`, `aria-details`, `aria-disabled`, `aria-dropeffect`, `aria-errormessage`, `aria-expanded`, `aria-flowto`, `aria-hidden`, `aria-invalid`, `aria-keyshortcuts`, `aria-label`, `aria-labelledby`, `aria-live`, `aria-multiselectable`, `aria-orientation`, `aria-owns`, `aria-readonly`, `aria-relevant`, `aria-required`, `aria-roledescription`
- **Owned elements:** `treeitem`, `group` (containing `treeitem`)
- **HTML implicit role:** none
- **Usage notes:** Top-level treeitems are direct children of `tree`. Nested treeitems are in a `group` element owned by a parent `treeitem`. Right arrow expands; Left arrow collapses or moves to parent.

---

### `treegrid`
A grid with rows that can be expanded or collapsed like a tree.

- **Superclass:** `grid`, `tree`
- **Required states/properties:** none
- **Supported states/properties:** Same as `grid` plus `aria-expanded` on rows
- **Owned elements:** `row` (with `aria-expanded`)
- **HTML implicit role:** none
- **Usage notes:** Combines tree and grid keyboard interactions. Rows have `aria-expanded` to show/hide child rows. Cells use `role="gridcell"` or `role="rowheader"`/`role="columnheader"`.

---

## Document Structure Roles

Document structure roles describe the structure of content but are not interactive.

### `application`
A region of the page declared as a web application rather than a document. Disables most virtual cursor/browse mode behavior.

- **Superclass:** `structure`
- **HTML implicit role:** none
- **Usage notes:** WARNING — use sparingly. Overrides reading mode in most screen readers. Only appropriate for embedded applications where all keyboard interactions are managed by the author. Prefer landmark roles for normal page regions.

---

### `article`
A self-contained composition in a document, page, or application that can be independently distributed.

- **Superclass:** `document`
- **HTML implicit role:** `<article>`
- **Usage notes:** Examples: blog post, forum post, news article. Nested articles are related to outer article. Screen readers announce "article" on entry. May be used within `feed` with `aria-posinset` and `aria-setsize`.

---

### `blockquote`
A section of content quoted from another source.

- **Superclass:** `section`
- **HTML implicit role:** `<blockquote>`
- **Usage notes:** New in ARIA 1.2. Use `aria-describedby` or visible text to cite the source. Prefer native `<blockquote>` which has this implicit role.

---

### `caption`
Visible content that names a table, figure, or other containing element.

- **Superclass:** `section`
- **HTML implicit role:** `<caption>`, `<figcaption>`
- **Usage notes:** New in ARIA 1.2. Should be the first child of the structure it names. Equivalent to `<caption>` in a table or `<figcaption>` in a figure.

---

### `cell`
A cell in a tabular container (table).

- **Superclass:** `section`
- **HTML implicit role:** `<td>`
- **Supported states/properties:** `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan`
- **Usage notes:** Parent must be `row`. For interactive cells, use `gridcell` instead.

---

### `columnheader`
A cell containing header information for a column.

- **Superclass:** `cell`, `gridcell`, `sectionhead`
- **HTML implicit role:** `<th scope="col">` or `<th>` in `<thead>`
- **Supported states/properties:** `aria-sort`, `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan`, `aria-selected`
- **Usage notes:** Use `aria-sort` to indicate sort direction: `ascending`, `descending`, `none`, or `other`.

---

### `definition`
A definition of a term or concept.

- **Superclass:** `section`
- **HTML implicit role:** `<dd>`
- **Usage notes:** Pair with `role="term"`. For definition lists, prefer `<dl>` / `<dt>` / `<dd>` which have implicit roles.

---

### `deletion`
Content that has been deleted or marked for deletion.

- **Superclass:** `section`
- **HTML implicit role:** `<del>`, `<s>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<del>`. Pair with `role="insertion"` for track-changes-style markup.

---

### `directory` (deprecated)
A list of references to members of a group. Deprecated in WAI-ARIA 1.2.

- **Usage notes:** Do not use. Was intended for reference lists like a table of contents. Use `role="list"` instead.

---

### `document`
A region containing content that is relevant to a specific, author-specified purpose.

- **Superclass:** `structure`
- **HTML implicit role:** `<html>`
- **Usage notes:** Rarely set explicitly. Use within `role="application"` regions to restore reading mode for specific sub-regions that should be consumed as a document.

---

### `emphasis`
Content to be emphasized.

- **Superclass:** `section`
- **HTML implicit role:** `<em>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<em>`.

---

### `feed`
See Widget Roles section above.

---

### `figure`
A perceivable section of content that can contain an optional caption.

- **Superclass:** `section`
- **HTML implicit role:** `<figure>`
- **Usage notes:** Use `role="caption"` or `aria-labelledby` pointing to a `<figcaption>` for the figure's accessible name.

---

### `generic`
A nameless container element with no specific semantic meaning.

- **Superclass:** `structure`
- **HTML implicit role:** `<div>`, `<span>`, `<b>`, `<i>`, `<u>`, `<pre>`, `<bdi>`, `<bdo>`, `<data>`, `<samp>`, `<small>`, `<a>` (without href), `<header>` / `<footer>` (in sectioning content, not body)
- **Usage notes:** New in ARIA 1.2. `role="generic"` cannot have an accessible name (prohibited `aria-label` and `aria-labelledby`). Used to describe the implicit role of presentational containers.

---

### `group`
A set of user interface objects that authors consider related but are not important enough for the document structure.

- **Superclass:** `section`
- **HTML implicit role:** `<fieldset>`, `<details>`, `<optgroup>`
- **Usage notes:** Not announced as a landmark. Use for grouping related form controls without the weight of a landmark. `<fieldset>` with `<legend>` is the preferred approach for groups of form controls.

---

### `heading`
A heading for a section of the page.

- **Superclass:** `sectionhead`
- **Required states/properties:** `aria-level` (1–6)
- **HTML implicit role:** `<h1>` (level 1) through `<h6>` (level 6)
- **Usage notes:** `aria-level` is required for custom heading elements. Prefer native heading elements `<h1>`–`<h6>`. Do not skip heading levels.

---

### `img`
A container for a collection of elements that together form an image.

- **Superclass:** `section`
- **HTML implicit role:** `<img alt="non-empty text">`, `<img>` (with non-empty alt)
- **Usage notes:** When composing images from multiple elements, wrap them in an element with `role="img"` and an accessible name via `aria-label` or `aria-labelledby`. `<img alt="">` has implicit role `presentation`/`none`.

---

### `insertion`
Content that has been inserted.

- **Superclass:** `section`
- **HTML implicit role:** `<ins>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<ins>`.

---

### `list`
A section containing `listitem` elements.

- **Superclass:** `section`
- **HTML implicit role:** `<ul>`, `<ol>`, `<menu>`
- **Usage notes:** Requires `role="listitem"` children. Note: some screen readers (VoiceOver with Safari) do not announce list semantics when CSS `list-style: none` is applied, making `role="list"` occasionally necessary.

---

### `listitem`
A single item in a list or directory.

- **Superclass:** `section`
- **HTML implicit role:** `<li>` (when a child of `<ul>`, `<ol>`, or `<menu>`)
- **Supported states/properties:** `aria-level`, `aria-posinset`, `aria-setsize`
- **Usage notes:** Must be owned by `list`. Position and set size are typically computed automatically.

---

### `mark`
Content that is marked/highlighted for reference purposes.

- **Superclass:** `section`
- **HTML implicit role:** `<mark>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<mark>`. Can be used with CSS `::before`/`::after` content to announce the marking to screen readers, or simply relied upon for screen readers that support the role.

---

### `math`
Content representing a mathematical expression.

- **Superclass:** `section`
- **HTML implicit role:** `<math>`
- **Usage notes:** Use MathML inside `<math>` or the `math` role. Provide an accessible text alternative via `aria-label` when MathML rendering may not be supported by the AT.

---

### `meter`
A scalar measurement within a known range.

- **Superclass:** `range`
- **Required states/properties:** `aria-valuenow`
- **Supported states/properties:** `aria-valuemax`, `aria-valuemin`, `aria-valuetext`
- **HTML implicit role:** `<meter>`
- **Usage notes:** Unlike `progressbar`, `meter` represents a static measurement (e.g., disk usage, score), not progress toward completion. Always set `aria-valuemin` and `aria-valuemax` with meaningful values.

---

### `none` / `presentation`
An element whose implicit native role semantics are to be removed and have no corresponding accessible role.

- **HTML implicit role:** `<img alt="">` (none/presentation)
- **Usage notes:** `none` and `presentation` are synonyms; `none` is preferred (less ambiguous). Removes the element and its children from the accessibility tree structure (though content remains readable). All focusable children are still exposed. Cannot be applied to elements with required children or that are referenced via `aria-labelledby`.

---

### `note`
A section of content that is parenthetic or ancillary to the main content.

- **Superclass:** `section`
- **HTML implicit role:** none
- **Usage notes:** Equivalent to an aside that is of lower importance. May be announced as "note" by screen readers. Not a landmark role — does not appear in landmark navigation.

---

### `paragraph`
A paragraph of content.

- **Superclass:** `section`
- **HTML implicit role:** `<p>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<p>`. Prohibited from having an accessible name (`aria-label`/`aria-labelledby` not allowed).

---

### `row`
A row of cells in a table, grid, or treegrid.

- **Superclass:** `group`, `widget`
- **Supported states/properties:** `aria-colindex`, `aria-expanded`, `aria-level`, `aria-posinset`, `aria-rowindex`, `aria-selected`, `aria-setsize`
- **HTML implicit role:** `<tr>`
- **Usage notes:** In a `treegrid`, rows can have `aria-expanded`. In a `grid`, rows can have `aria-selected`.

---

### `rowgroup`
A group of rows in a table, grid, or treegrid.

- **Superclass:** `structure`
- **HTML implicit role:** `<thead>`, `<tbody>`, `<tfoot>`
- **Usage notes:** Wraps rows to indicate header, body, or footer grouping.

---

### `rowheader`
A cell containing header information for a row.

- **Superclass:** `cell`, `gridcell`, `sectionhead`
- **HTML implicit role:** `<th scope="row">`
- **Supported states/properties:** `aria-sort`, `aria-colindex`, `aria-colspan`, `aria-rowindex`, `aria-rowspan`, `aria-selected`
- **Usage notes:** Identifies the row. Can have `aria-sort` if rows are sortable.

---

### `section`
A perceivable structural containment unit in a document or application. Abstract role — do not use directly.

---

### `sectionhead`
A structure that labels or summarizes the topic of its related section. Abstract role — do not use directly.

---

### `strong`
Content with strong importance.

- **Superclass:** `section`
- **HTML implicit role:** `<strong>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<strong>`. Most screen readers do not announce strong/em roles by default.

---

### `subscript`
Content that is subscript.

- **Superclass:** `section`
- **HTML implicit role:** `<sub>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<sub>`.

---

### `superscript`
Content that is superscript.

- **Superclass:** `section`
- **HTML implicit role:** `<sup>`
- **Usage notes:** New in ARIA 1.2. Prefer native `<sup>`.

---

### `table`
A section containing data arranged in rows and columns, similar to an HTML table.

- **Superclass:** `section`
- **Supported states/properties:** `aria-colcount`, `aria-rowcount`
- **Owned elements:** `row`, `rowgroup`, `caption`
- **HTML implicit role:** `<table>`
- **Usage notes:** Unlike `grid`, `table` is not interactive. Use `aria-colcount`/`aria-rowcount` when not all rows/columns are present in DOM. Prefer native `<table>` which carries this role implicitly.

---

### `term`
A word or phrase that has a definition.

- **Superclass:** `section`
- **HTML implicit role:** `<dt>`, `<dfn>`
- **Usage notes:** Pair with `role="definition"`. Prefer native `<dt>` / `<dd>` within `<dl>`.

---

### `time`
Content representing a specific time or date.

- **Superclass:** `section`
- **HTML implicit role:** `<time>`
- **Usage notes:** New in ARIA 1.2. Use `aria-label` or `aria-description` to provide a human-readable date/time. Prefer native `<time datetime="...">`.

---

### `toolbar`
A collection of commonly used function buttons or controls represented in a compact visual form.

- **Superclass:** `group`
- **Supported states/properties:** `aria-activedescendant`, `aria-orientation`
- **HTML implicit role:** none
- **Usage notes:** Typically horizontal (default `aria-orientation="horizontal"`). Arrow keys navigate between items; Tab moves out of the toolbar. Only one item in the toolbar should be in the tab sequence at a time (roving tabindex).

---

### `tooltip`
See Widget Roles section above.

---

## Landmark Roles

Landmark roles identify regions of the page that users might want to navigate to directly.

### `banner`
The main header of the page, typically containing the site logo, name, and primary navigation.

- **Superclass:** `landmark`
- **Supported states/properties:** Global states/properties
- **HTML equivalent:** `<header>` (when a direct child of `<body>`, not in `<article>`, `<aside>`, `<main>`, `<nav>`, `<section>`, or a sectioning element)
- **Usage notes:** There should be only one `banner` landmark per page. Do not place another `banner` inside `<article>` or `<section>`; in those contexts `<header>` maps to `generic`.

---

### `complementary`
Supporting content that complements the main content of the document.

- **Superclass:** `landmark`
- **HTML equivalent:** `<aside>`
- **Usage notes:** If there are multiple `complementary` landmarks, each should have a unique label via `aria-label` or `aria-labelledby`. Related but not essential to the main content.

---

### `contentinfo`
The main footer of the page, typically containing metadata, legal information, and links.

- **Superclass:** `landmark`
- **HTML equivalent:** `<footer>` (when a direct child of `<body>`, not inside sectioning elements)
- **Usage notes:** There should be only one `contentinfo` landmark per page. Like `banner`, `<footer>` inside `<article>` or `<section>` maps to `generic`.

---

### `form`
A landmark region containing a collection of items and objects that combine to create a form.

- **Superclass:** `landmark`
- **HTML equivalent:** `<form>` (only when the form has an accessible name via `aria-label`, `aria-labelledby`, or `title`)
- **Usage notes:** The `form` role is only a landmark when the element has an accessible name. An anonymous `<form>` without a name does not create a landmark. Use the `search` landmark role for search forms.

---

### `main`
The main content of the document.

- **Superclass:** `landmark`
- **HTML equivalent:** `<main>`
- **Usage notes:** There should be only one `main` landmark per page (though multiple are technically allowed). Should not be nested. Most pages should have exactly one.

---

### `navigation`
A collection of navigational elements (usually links) for navigating the document or related documents.

- **Superclass:** `landmark`
- **HTML equivalent:** `<nav>`
- **Usage notes:** Label multiple navigation landmarks to distinguish them (e.g., "Primary navigation", "Footer navigation"). Only use for major navigation blocks — not every set of links needs a navigation landmark.

---

### `region`
A perceivable section containing content relevant to a specific, author-specified purpose.

- **Superclass:** `landmark`
- **HTML equivalent:** `<section>` (only when it has an accessible name via `aria-label`, `aria-labelledby`, or `title`)
- **Usage notes:** `<section>` without an accessible name maps to `generic`, not `region`. Label the region meaningfully. Use when no other landmark role is appropriate.

---

### `search`
A landmark region that contains a search facility.

- **Superclass:** `landmark`
- **HTML equivalent:** `<search>` (HTML element added in HTML living standard)
- **Usage notes:** Wrap the search input and button in the `search` landmark. Distinct from `role="searchbox"` which is the input itself. New `<search>` HTML element provides this implicitly.

---

## Abstract Roles (Reference Only — Do Not Use in Markup)

Abstract roles form the ARIA inheritance hierarchy. They are never used directly in HTML.

| Abstract Role | Description |
|---|---|
| `command` | Superclass for actionable widgets (button, link, menuitem) |
| `composite` | Superclass for widgets with managed focus (grid, listbox, menu, tree) |
| `input` | Superclass for data entry widgets |
| `landmark` | Superclass for all landmark roles |
| `range` | Superclass for range-based widgets (progressbar, scrollbar, slider, spinbutton) |
| `roletype` | Root of the role taxonomy |
| `section` | Superclass for container roles |
| `sectionhead` | Superclass for section header roles |
| `select` | Superclass for selection widgets |
| `structure` | Superclass for document structure roles |
| `widget` | Superclass for interactive user interface objects |
| `window` | Superclass for windowed sub-documents (dialog) |
