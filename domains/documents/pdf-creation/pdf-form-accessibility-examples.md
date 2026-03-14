---
title: "PDF Form Accessibility Examples"
standard: "PDF/UA + WCAG + Section 508"
source_url: "https://pdfa.org/resource/pdf-ua/"
domain: ["documents"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["pdf", "forms", "acrobat", "pdf-ua", "examples", "remediation"]
ai_context: "Example-heavy guide for accessible PDF forms. Load when advising on PDF form fields, tooltips, tab order, validation, and remediation."
---

# PDF Form Accessibility Examples

---

## Core Requirements for PDF Forms

Accessible PDF forms need all of the following:

- Every field has a programmatic name exposed to assistive technology
- Visible labels match or closely align with the field name
- Tab order follows the visual and task order
- Instructions and required-state cues are available in text
- Errors are identified in text, not only by color or icons

### High-Value Standards Mapping

| Requirement | Primary Reference |
|-------------|-------------------|
| Labels and relationships | WCAG 1.3.1, 3.3.2 |
| Focus order | WCAG 2.4.3 |
| Name, role, value | WCAG 4.1.2 |
| Error identification | WCAG 3.3.1 |
| Form fields labeled in tagged PDF | PDF/UA 7.18 |

---

## Example 1: Single-Line Text Field

### Poor Pattern

- Visible text says `First name`
- Acrobat field name is auto-generated as `Text1`
- No tooltip or help text

### Better Pattern

- Visible label: `First name`
- Tooltip / accessible name: `First name`
- Help text nearby if formatting matters

### Acrobat Pro Steps

1. Open `Tools -> Prepare Form`
2. Right-click the field -> `Properties`
3. Set `Name` for authoring reference
4. Set `Tooltip` to the user-facing label read by screen readers

### Good Tooltip Examples

| Visible Label | Good Tooltip | Avoid |
|---------------|--------------|-------|
| First name | First name | Text1 |
| Email address | Email address | Email field |
| Phone number | Phone number, 10 digits | Enter value |

---

## Example 2: Required Field With Format Hint

### Failure Pattern

- Field border turns red after submission
- No text explains what was wrong
- Placeholder text disappears when the user starts typing

### Better Pattern

- Visible label: `Date of birth`
- Visible hint: `Use MM/DD/YYYY`
- Required cue in text: `Required`
- Error message in text near the field: `Enter date of birth in MM/DD/YYYY format`

### Recommended Structure

`Date of birth (Required)`

`Use MM/DD/YYYY`

Field

Error state when needed:

`Error: Enter date of birth in MM/DD/YYYY format.`

---

## Example 3: Radio Button Group

Radio buttons often fail when each option is tagged but the shared question is not exposed.

### Failure Pattern

- Buttons read as isolated choices: `Yes radio button`, `No radio button`
- The question text `Do you need accommodations?` is not connected to the group

### Better Pattern

- Group question appears immediately before the options
- Group and options are tagged in the correct order
- Tooltip or field naming preserves the question context

### Better Spoken Result

- `Do you need accommodations? Yes, radio button, not checked`
- `Do you need accommodations? No, radio button, checked`

### Authoring Notes

- Use one radio group, not separate unrelated fields
- Keep the question text adjacent in the tag tree
- Do not rely on visual spacing alone to imply grouping

---

## Example 4: Checkbox With Embedded Terms

### Risk

Checkbox labels are often too short when part of a longer legal sentence.

### Better Pattern

Visible text:

`I agree to the privacy notice and terms of service.`

Checkbox tooltip:

`I agree to the privacy notice and terms of service`

### Avoid

- `Agree`
- `Check here`
- `Box 7`

Short labels are ambiguous when the field is encountered out of context.

---

## Example 5: Combo Box / Drop-Down

### Better Pattern

- Visible label identifies the question
- Current value is obvious
- Empty default is explicit when selection is required

### Example

Visible label:

`Preferred contact method`

Options:

- `Select one`
- `Email`
- `Phone`
- `Text message`

### Avoid

- Starting with a real choice already selected when a deliberate decision is required
- Using unlabeled abbreviations such as `Txt`

---

## Tab Order Examples

### Correct Order

1. Name
2. Email
3. Phone
4. Preferred contact method
5. Submit

### Common Failure

1. Name
2. Phone
3. Submit
4. Email
5. Preferred contact method

This often happens when fields are copied visually rather than aligned to the logical task sequence.

### Acrobat Check

1. Open `Prepare Form`
2. Use the field list to review sequence
3. Press `Tab` in the saved PDF using Acrobat Reader
4. Confirm focus matches the visible flow

---

## Error Summary Pattern

For longer forms, add a text error summary near the top after submission.

### Example

`There are 3 errors in the form: Email address is required. Date of birth must use MM/DD/YYYY. Select a preferred contact method.`

This helps users find problems without hunting field-by-field.

---

## Signature and Submit Controls

### Submit Button

- Label the control with the actual action: `Submit application`
- Avoid generic labels like `Button1` or `Submit`

### Signature Fields

- Explain the signature method in text
- If an inaccessible signature widget is used, provide an alternate completion path
- Do not assume mouse-only signing is acceptable

---

## Manual Testing Workflow

1. Read the form with the Tags panel open and confirm labels precede controls logically
2. Tab through the entire form in Acrobat Reader
3. Trigger validation errors intentionally and verify the messages are text-based
4. Check required fields are identified before submission
5. Test with NVDA or VoiceOver for field names, role, value, and state

---

## Quick Checklist

- [ ] Each field tooltip matches the visible label or instruction
- [ ] Radio groups preserve the shared question
- [ ] Checkboxes are not labeled with vague text like `Agree`
- [ ] Required fields are marked in text
- [ ] Format instructions are visible before data entry
- [ ] Errors are presented in text
- [ ] Tab order matches the visual and task order
- [ ] Submit buttons describe the outcome
