---
title: "Forms Accessibility"
standard: "WCAG"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["forms", "labels", "errors", "validation", "autocomplete", "input", "fieldset"]
ai_context: "Comprehensive guide to accessible forms. Covers labels, error handling, grouping, input purpose, and validation. Load when generating or auditing HTML forms."
---

# Forms Accessibility

---

## Labels

Every form control must have an accessible label. In order of preference:

### 1. `<label>` (Preferred)

```html
<label for="email">Email address</label>
<input type="email" id="email" name="email">
```

The `for` attribute must match the input's `id`. This creates a programmatic association satisfying SC 4.1.2 and SC 1.3.1.

Benefits:
- Clicking the label moves focus to the input
- Screen readers announce the label when the input receives focus
- Works across all AT

### 2. Implicit Label (Wrapping)

```html
<label>
  Email address
  <input type="email" name="email">
</label>
```

Valid but less maintainable than explicit `for`/`id` association.

### 3. `aria-labelledby`

```html
<span id="email-label">Email address</span>
<input type="email" aria-labelledby="email-label" name="email">
```

Use when the label text exists elsewhere in the DOM and cannot use a `<label>`. Takes precedence over `aria-label`.

### 4. `aria-label`

```html
<input type="search" aria-label="Search products" name="q">
```

Use when no visible label is possible (search field with visible icon). The aria-label text must match or contain any visible text (SC 2.5.3).

### 5. `title` (Last Resort)

```html
<input type="text" title="First name" name="fname">
```

Avoid. `title` is not reliably announced by all AT as a label. Use only when no other option exists.

### What NOT to Use as a Label

- **`placeholder` alone** — Disappears when typing, insufficient contrast (SC 1.4.3 applies), not reliably read as label
- **Adjacent text** without programmatic association — Screen readers won't know the text is the label

---

## Required Fields

Required fields must be communicated to AT AND visually.

### Minimum Required Pattern

```html
<label for="email">
  Email address
  <span aria-hidden="true">*</span>
  <span class="sr-only">(required)</span>
</label>
<input type="email" id="email" name="email" required aria-required="true">
```

Explanation:
- `<span aria-hidden="true">*</span>` — Shows the asterisk visually but hides it from AT (prevents "asterisk" announcement)
- `<span class="sr-only">(required)</span>` — AT-only text indicating required
- HTML `required` — Browser validates and prevents submission without value
- `aria-required="true"` — Redundant with HTML `required` but increases AT compatibility

### Page-Level Note

Add a note before the form:
```html
<p>Fields marked with an asterisk (<span aria-hidden="true">*</span>) are required.</p>
```

### Visual Indicator Rules

Per SC 1.4.1: don't use color alone. An asterisk, the word "(required)", or bold text all work. Red color alone fails.

---

## Grouping Related Controls

Group related fields with `<fieldset>` and `<legend>`.

### Radio Button Groups

```html
<fieldset>
  <legend>Preferred contact method</legend>
  <label>
    <input type="radio" name="contact" value="email"> Email
  </label>
  <label>
    <input type="radio" name="contact" value="phone"> Phone
  </label>
  <label>
    <input type="radio" name="contact" value="mail"> Mail
  </label>
</fieldset>
```

Screen readers announce: "Preferred contact method — Email, radio button"

### Checkbox Groups

```html
<fieldset>
  <legend>Notification preferences</legend>
  <label>
    <input type="checkbox" name="notify" value="email"> Email notifications
  </label>
  <label>
    <input type="checkbox" name="notify" value="sms"> SMS notifications
  </label>
</fieldset>
```

### Address Fields (Multi-field Groups)

```html
<fieldset>
  <legend>Mailing address</legend>
  <label for="street">Street address</label>
  <input type="text" id="street" name="street" autocomplete="street-address">

  <label for="city">City</label>
  <input type="text" id="city" name="city" autocomplete="address-level2">

  <label for="state">State</label>
  <select id="state" name="state" autocomplete="address-level1">...</select>

  <label for="zip">ZIP code</label>
  <input type="text" id="zip" name="zip" inputmode="numeric" autocomplete="postal-code">
</fieldset>
```

---

## Input Purpose (SC 1.3.5)

Personal information inputs must have `autocomplete` attribute with the appropriate token. This allows password managers, AT, and browsers to fill values automatically.

### autocomplete Values for Personal Data

```html
<!-- Name fields -->
<input autocomplete="name" />             <!-- Full name -->
<input autocomplete="given-name" />       <!-- First name -->
<input autocomplete="additional-name" />  <!-- Middle name -->
<input autocomplete="family-name" />      <!-- Last name -->
<input autocomplete="honorific-prefix" /> <!-- Mr., Dr., etc. -->

<!-- Contact fields -->
<input autocomplete="email" />
<input autocomplete="tel" />
<input autocomplete="tel-national" />

<!-- Address fields -->
<input autocomplete="street-address" />
<input autocomplete="address-line1" />
<input autocomplete="address-line2" />
<input autocomplete="address-level1" />   <!-- State/Province -->
<input autocomplete="address-level2" />   <!-- City -->
<input autocomplete="postal-code" />
<input autocomplete="country-name" />

<!-- Date of birth -->
<input autocomplete="bday" />
<input autocomplete="bday-day" />
<input autocomplete="bday-month" />
<input autocomplete="bday-year" />

<!-- Account fields -->
<input autocomplete="username" />
<input autocomplete="current-password" />
<input autocomplete="new-password" />
<input autocomplete="one-time-code" />

<!-- Payment fields -->
<input autocomplete="cc-name" />
<input autocomplete="cc-number" />
<input autocomplete="cc-exp" />
<input autocomplete="cc-csc" />

<!-- Other -->
<input autocomplete="sex" />
<input autocomplete="url" />
<input autocomplete="photo" />
```

Use `autocomplete="off"` sparingly — it blocks password managers (SC 3.3.8 implication).

---

## Error Handling

### Error Identification (SC 3.3.1)

Errors must:
1. Identify the specific field in error
2. Describe the error in text
3. Not use color alone to indicate error state

### Error Suggestion (SC 3.3.3)

When the error can be corrected in a known way, suggest the correction.

### Inline Error Pattern

```html
<div class="form-field">
  <label for="email">Email address</label>
  <input
    type="email"
    id="email"
    name="email"
    aria-required="true"
    aria-invalid="true"
    aria-describedby="email-error"
  >
  <span id="email-error" class="error-message" role="alert">
    Please enter a valid email address (e.g., name@example.com)
  </span>
</div>
```

Key elements:
- `aria-invalid="true"` — Tells AT the field has an error
- `aria-describedby="email-error"` — Links error message to field (read after label)
- `role="alert"` on error span — Announces error to live region listeners (for dynamic validation)
- Error message near the field — Not just in a banner at the top of the page

### Error State on Submit

When the form is submitted with errors:

1. Set `aria-invalid="true"` on each errored field
2. Add `aria-describedby` pointing to each field's error message
3. Either:
   - Move focus to the first error field, OR
   - Move focus to an error summary at the top of the form
4. Update page `<title>` to indicate errors: `<title>Error: Please correct the form — Site Name</title>`

### Error Summary Pattern

```html
<div role="alert" id="error-summary" tabindex="-1">
  <h2>Please correct the following errors:</h2>
  <ul>
    <li><a href="#email">Email address: Please enter a valid email</a></li>
    <li><a href="#phone">Phone number: This field is required</a></li>
  </ul>
</div>
```

Links in the error summary jump to the specific field.

### When NOT to Validate

- **On keystroke:** Do not show errors while the user is still typing (exception: password strength meter is acceptable)
- **Preferred timing:** Validate on blur (leaving a field) or on form submit
- If validating on blur, do not remove errors on refocus — remove them when the error is corrected

---

## Instructions

Provide instructions before the field that needs them:

```html
<label for="dob">Date of birth</label>
<p id="dob-hint">Enter in MM/DD/YYYY format</p>
<input type="text" id="dob" name="dob"
       aria-describedby="dob-hint"
       placeholder="MM/DD/YYYY">
```

- Instructions come before the input (not after) — screen readers read top-to-bottom
- Use `aria-describedby` to programmatically link instructions to the field
- Do not put instructions in placeholder text alone

---

## Submit Buttons

```html
<!-- Clear action label -->
<button type="submit">Submit application</button>

<!-- Not just "Submit" if context is ambiguous -->
<button type="submit">Place order</button>
<button type="submit">Create account</button>
<button type="submit">Send message</button>
```

Rules:
- Use `type="submit"` on the submit button (default `type` is `submit` in `<form>`, but explicit is clearer)
- Label should describe the specific action, not just "Submit"
- For multi-step forms, "Next" with an `aria-label` for context: `aria-label="Next: Shipping information"`

---

## Autocomplete and Datalist

```html
<label for="country">Country</label>
<input type="text" id="country" name="country"
       list="country-list"
       autocomplete="country-name">
<datalist id="country-list">
  <option value="United States">
  <option value="Canada">
  <option value="United Kingdom">
</datalist>
```

Datalist is natively accessible in modern browsers. For custom autocomplete components (combobox), use the APG combobox pattern with correct ARIA.

---

## Password Fields

```html
<label for="password">Password</label>
<input type="password" id="password" name="password" autocomplete="current-password">
<button type="button" aria-pressed="false" onclick="togglePassword(this)">
  Show password
</button>
```

Rules:
- Do NOT use `autocomplete="off"` on password fields — blocks password managers (fails SC 3.3.8)
- Show/hide password button must have accessible name and use `aria-pressed` for state
- Do NOT prevent paste in password fields (fails SC 3.3.8 Accessible Authentication)

---

## Custom Select and Dropdowns

Native `<select>` is preferred. If a custom select is required:

See `domains/web/component-patterns/combobox.md` for the full APG combobox implementation.

Key ARIA for custom select:
```html
<div role="combobox"
     aria-expanded="false"
     aria-haspopup="listbox"
     aria-controls="options-list"
     tabindex="0">
  Select a country
</div>
<ul id="options-list" role="listbox" hidden>
  <li role="option" aria-selected="false">United States</li>
  <li role="option" aria-selected="false">Canada</li>
</ul>
```
