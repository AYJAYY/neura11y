---
title: "Prompt Template: Audit HTML Snippet for WCAG AA"
standard: "WCAG"
source_url: ""
domain: ["web"]
last_fetched: "2026-03-13"
status: "template"
tags: ["ai-prompt", "audit", "wcag-2.2", "html", "template"]
ai_context: "Ready-to-use prompt template for auditing HTML snippets against WCAG AA. Load this with the WCAG quick-ref and relevant domain files."
---

# Prompt Template: Audit HTML Snippet for WCAG AA

## Context Files to Load

```
standards/wcag/wcag-2.2-quick-ref.md
standards/aria/aria-common-mistakes.md
standards/aria/wai-aria-1.2-roles.md
domains/web/html-semantics-guide.md
```

For component-specific audits, also load:
```
domains/web/component-patterns/[relevant-component].md
domains/web/focus-management.md  (if interactive elements present)
domains/web/forms-accessibility.md  (if form elements present)
```

---

## Prompt Template

```
You are an expert web accessibility auditor. I need you to audit the following HTML for WCAG Level AA conformance.

For each issue found:
1. State the WCAG SC number and title (e.g., "SC 1.1.1 Non-text Content")
2. State the conformance level (A or AA)
3. Describe the specific violation
4. Provide the exact fix (code or description)
5. Cite the relevant technique or failure code if known (e.g., F65, H37)

Mark issues as:
- [FAIL] — Definitive WCAG failure
- [WARN] — Potential issue requiring further testing (e.g., color contrast without hex codes, screen reader testing required)
- [BEST PRACTICE] — Not a WCAG failure but recommended improvement

Also note:
- Any success criteria that PASS (to confirm correct implementation)
- Any items that need manual testing (screen reader, keyboard)

HTML to audit:
[INSERT HTML HERE]
```

---

## Example Prompt (Filled)

```
You are an expert web accessibility auditor. Audit this HTML for WCAG Level AA conformance.

For each issue:
1. State the SC number and title
2. State the level (A or AA)
3. Describe the violation
4. Provide the fix
5. Cite the technique/failure code if known

Mark: [FAIL], [WARN], or [BEST PRACTICE]

HTML:
<div onclick="submitForm()">
  <span style="color:red">*</span>
  Enter your email:
  <input type="text" placeholder="email@example.com">
</div>
<div onclick="submitForm()" style="background:#0000ff; color:#ffffff; padding:10px">
  Submit
</div>
```

---

## Expected Output Format

```
ACCESSIBILITY AUDIT REPORT
WCAG Level AA

[FAIL] SC 4.1.2 Name, Role, Value (Level A)
Issue: The outer <div> with onclick has no role, no accessible name, and cannot receive keyboard focus.
Fix: Replace with <form onsubmit="..."> and a <button type="submit"> element, or add role="button", tabindex="0", and keyboard event handlers.
Technique: F59 — Using script to make div/span interactive without role

[FAIL] SC 2.1.1 Keyboard (Level A)
Issue: onclick on <div> without keyboard equivalent. Cannot be activated by keyboard.
Fix: Use native <button> element, or add onkeydown handler for Enter and Space keys.

[FAIL] SC 4.1.2 Name, Role, Value (Level A)
Issue: Submit <div> has no accessible role, no accessible name.
Fix: Use <button>Submit</button> instead. Button has implicit role="button" and text serves as accessible name.

[FAIL] SC 1.3.1 Info and Relationships (Level A)
Issue: <input type="text"> has no label. Placeholder text "email@example.com" is not a valid label.
Fix: Add <label for="email">Enter your email</label> and id="email" on the input.

[FAIL] SC 3.3.2 Labels or Instructions (Level A)
Issue: No label for the input field.
Fix: Add an explicit <label> element.

[FAIL] SC 1.4.1 Use of Color (Level A)
Issue: The asterisk (*) is marked red to indicate required, but color is the only differentiator.
Fix: Add text "(required)" or aria-required="true" in addition to the visual indicator.

[WARN] SC 1.4.3 Contrast (Minimum) (Level AA)
Issue: Blue (#0000FF) background with white (#FFFFFF) text — contrast ratio = 8.59:1. PASSES. However, verify the exact hex values in the rendered stylesheet.
Status: PASS if #0000ff/#ffffff as shown.

ITEMS REQUIRING MANUAL TESTING:
- Keyboard navigation: Tab to both interactive elements, activate with Enter/Space
- Screen reader: Verify announced roles and values match intent
- Error messages: Test what is announced when form submission fails
```

---

## Variations

### Audit Specific SC Only

```
Audit the following HTML only for WCAG SC 1.4.3 (Contrast Minimum) and SC 1.4.11 (Non-text Contrast). Provide exact hex values where determinable from the code.

HTML: [insert code]
```

### Audit for ARIA Correctness Only

```
Review the following HTML for correct ARIA usage. For each aria-* attribute and role:
1. Confirm it is used on an appropriate element
2. Confirm the value is valid
3. Flag any missing required states/properties

Reference: Load aria-common-mistakes.md and wai-aria-1.2-roles.md

HTML: [insert code]
```

### Audit for Keyboard Accessibility

```
Analyze the following HTML for keyboard accessibility issues (WCAG SC 2.1.1, 2.1.2, 2.4.3, 2.4.7). List every interactive element, its tab order position, how it can be activated by keyboard, and whether focus visibility is present.

HTML: [insert code]
```
