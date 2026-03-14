---
title: "COGA Design Guide — Patterns and Examples"
standard: "WCAG 2.2 + W3C COGA"
source_url: "https://www.w3.org/TR/coga-usable/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["cognitive", "coga", "design-patterns", "forms", "navigation", "plain-language", "authentication"]
ai_context: "Practical COGA design patterns and implementation examples. Supplements coga-overview.md. Load when designing for cognitive accessibility."
---

# COGA Design Guide — Patterns and Examples

Source: W3C COGA Usability Guidance (https://www.w3.org/TR/coga-usable/)

---

## SC 3.3.8 — Accessible Authentication (Minimum) — Level AA (WCAG 2.2)

Cognitive function tests must not be required for authentication unless an alternative is provided.

**Cognitive function tests include:**
- CAPTCHA (image recognition, audio puzzles)
- Memorizing a username/password combination without assistance
- Answering personal knowledge questions
- Solving puzzles

**Compliant authentication approaches:**
- Email magic links (one-click login)
- Biometric authentication (Face ID, fingerprint)
- Allow pasting into password fields (enables password managers)
- OAuth / social login (Google, Apple, GitHub)
- Allow copy-paste of one-time codes
- Object recognition CAPTCHAs where the user can identify which images they personally provided

**Failing patterns:**
```html
<!-- FAILS SC 3.3.8: Prevents pasting into password field -->
<input type="password" onpaste="return false;">

<!-- FAILS SC 3.3.8: Blocks password manager autocomplete -->
<input type="password" autocomplete="off">
```

```html
<!-- CORRECT: Allow autocomplete and paste -->
<label for="password">Password</label>
<input
  type="password"
  id="password"
  name="password"
  autocomplete="current-password"
>
```

---

## SC 3.3.7 — Redundant Entry — Level A (WCAG 2.2)

Information previously entered that is required again in the same process must be:
- Auto-populated, OR
- Available to select

**Common multi-step form scenarios:**

```html
<!-- Order form step 1: capture billing address -->
<form>
  <fieldset>
    <legend>Billing address</legend>
    <label for="bill-name">Full name</label>
    <input type="text" id="bill-name" autocomplete="name">
    <!-- ... -->
  </fieldset>
</form>

<!-- Order form step 2: shipping address — provide option to reuse -->
<form>
  <fieldset>
    <legend>Shipping address</legend>

    <!-- Option to reuse billing address -->
    <label>
      <input type="checkbox" id="same-as-billing" name="same-as-billing">
      Same as billing address
    </label>

    <!-- If unchecked, show shipping fields -->
    <div id="shipping-fields">
      <label for="ship-name">Full name</label>
      <input type="text" id="ship-name" autocomplete="name">
      <!-- ... -->
    </div>
  </fieldset>
</form>
```

**Exception:** Re-entering for security verification (e.g., "Confirm your email address", "Re-enter password") is allowed.

---

## SC 1.3.5 — Identify Input Purpose — Level AA

Autocomplete attributes reduce cognitive load by letting the browser fill in personal information.

```html
<!-- Name -->
<input type="text" autocomplete="name">
<input type="text" autocomplete="given-name">
<input type="text" autocomplete="family-name">

<!-- Contact -->
<input type="email" autocomplete="email">
<input type="tel" autocomplete="tel">

<!-- Address -->
<input type="text" autocomplete="street-address">
<input type="text" autocomplete="address-level2"> <!-- City -->
<input type="text" autocomplete="address-level1"> <!-- State/Province -->
<input type="text" autocomplete="postal-code">
<select autocomplete="country">

<!-- Payment -->
<input type="text" autocomplete="cc-name">
<input type="text" autocomplete="cc-number">
<input type="text" autocomplete="cc-exp">
<input type="text" autocomplete="cc-csc">

<!-- Authentication -->
<input type="text" autocomplete="username">
<input type="password" autocomplete="current-password">
<input type="password" autocomplete="new-password">
<input type="text" autocomplete="one-time-code">
```

---

## Cognitive Load Reduction Patterns

### Pattern: Progressive Disclosure

Show only what's needed at each step. Don't overwhelm with all options upfront.

```html
<!-- Collapsed: show summary with expand option -->
<div class="details-section">
  <button type="button" aria-expanded="false" aria-controls="advanced-options">
    Advanced options
  </button>
  <div id="advanced-options" hidden>
    <!-- More complex options revealed only when requested -->
  </div>
</div>
```

### Pattern: Confirmation Before Irreversible Actions

```html
<!-- Confirm destructive action -->
<button type="button" id="delete-btn" aria-haspopup="dialog">
  Delete account
</button>

<!-- Dialog -->
<div role="alertdialog" aria-modal="true" aria-labelledby="confirm-title" aria-describedby="confirm-msg" hidden>
  <h2 id="confirm-title">Delete your account?</h2>
  <p id="confirm-msg">This action is permanent. All your data will be deleted and cannot be recovered.</p>
  <button type="button" id="confirm-delete">Yes, delete my account</button>
  <button type="button" id="cancel-delete" autofocus>Cancel — keep my account</button>
</div>
```

**Note:** The Cancel/keep option receives initial focus — this prevents accidental deletion.

### Pattern: Visible Progress Indicator

```html
<nav aria-label="Checkout progress">
  <ol>
    <li aria-current="step">
      <span aria-hidden="true">1</span>
      Cart
    </li>
    <li>
      <span aria-hidden="true">2</span>
      <a href="/checkout/shipping">Shipping</a>
    </li>
    <li>
      <span aria-hidden="true">3</span>
      Payment
    </li>
    <li>
      <span aria-hidden="true">4</span>
      Confirm
    </li>
  </ol>
</nav>
```

### Pattern: Clear Error Messages

```html
<!-- BAD: Vague error -->
<p role="alert" class="error">Invalid input.</p>

<!-- GOOD: Specific, actionable error -->
<p role="alert" class="error" id="email-error">
  Please enter a valid email address in the format: name@example.com
</p>
<input
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
  value="john@invalid"
>
```

Error messages must:
1. Identify the field with the error
2. Describe what went wrong
3. Tell the user how to fix it

### Pattern: Error Summary

When a form has multiple errors on submission, show a summary at the top and move focus to it.

```html
<div
  role="alert"
  tabindex="-1"
  id="error-summary"
  class="error-summary"
>
  <h2>3 errors found — please correct before submitting</h2>
  <ul>
    <li><a href="#full-name">Full name: This field is required</a></li>
    <li><a href="#email">Email: Enter a valid email address</a></li>
    <li><a href="#card-number">Card number: Enter a 16-digit card number</a></li>
  </ul>
</div>
```

```javascript
form.addEventListener('submit', (e) => {
  const errors = validateForm();
  if (errors.length > 0) {
    e.preventDefault();
    showErrorSummary(errors);
    document.getElementById('error-summary').focus();
  }
});
```

---

## Timed Content and Sessions

### SC 2.2.1 — Timing Adjustable (Level A)

When sessions time out, warn the user beforehand and provide a way to extend.

```html
<!-- Session expiry warning dialog -->
<div
  role="alertdialog"
  aria-labelledby="session-title"
  aria-describedby="session-msg"
  aria-modal="true"
>
  <h2 id="session-title">Your session will expire soon</h2>
  <p id="session-msg">
    Your session expires in <span id="countdown">2 minutes</span>.
    Choose an option to continue.
  </p>
  <button id="extend-session">Continue session</button>
  <button id="logout">Log out now</button>
</div>
```

Minimum requirements:
- Warn at least 20 seconds before timeout
- Provide mechanism to extend time by at least 10×
- OR provide no time limit
- OR session timeout is essential (banking security)

---

## Clear Navigation and Labels

### Consistent Navigation (SC 3.2.3)

Navigation must appear in the same location on every page.

```html
<!-- Navigation in the same position (header) on every page -->
<header>
  <a href="/" class="logo-link">
    <img src="logo.svg" alt="Acme Corp">
  </a>
  <nav aria-label="Main navigation">
    <!-- Same items, same order, every page -->
  </nav>
</header>
```

### Consistent Help (SC 3.2.6 — WCAG 2.2, Level A)

Help mechanisms must appear in the same location across pages.

```html
<!-- Help in footer, same location on every page -->
<footer>
  <section aria-label="Help and support">
    <a href="/help">Help center</a>
    <a href="/contact">Contact us</a>
    <a href="tel:+18005551234">1-800-555-1234</a>
  </section>
</footer>
```

---

## Plain Language Checklist for UI Text

| Text element | Guideline | Example |
|--------------|-----------|---------|
| Button labels | Action verb + object | "Save document" not "Submit" |
| Error messages | Say what's wrong + how to fix | "Email must include @" not "Invalid email" |
| Success messages | Confirm what happened | "Email sent to john@example.com" |
| Placeholder text | Describe expected format | "DD/MM/YYYY" not "Date" |
| Instructions | Before the input, not after | Label says "Enter 8-digit order number" above field |
| Page titles | Unique, describes content | "Order History — Acme Shop" |
| Headings | Active, descriptive | "How to return an item" not "Returns" |
