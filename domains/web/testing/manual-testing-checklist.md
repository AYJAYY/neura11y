---
title: "Manual Accessibility Testing Checklist"
standard: "WCAG"
source_url: "https://www.w3.org/WAI/test-evaluate/preliminary/"
domain: ["web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["testing", "manual", "checklist", "keyboard", "screen-reader", "visual"]
ai_context: "Step-by-step manual accessibility testing procedures for web pages. Load when writing testing instructions or planning an accessibility audit."
---

# Manual Accessibility Testing Checklist

Manual testing is essential — automated tools find only ~30-40% of WCAG failures. This checklist covers what must be tested manually.

---

## Quick Pre-Test Setup

1. Turn off CSS: `Ctrl/Cmd + Shift + I` → Console → `document.body.style.cssText = 'all:unset'` (or use Web Developer extension → Disable Styles)
2. Zoom browser to 400%
3. Set screen to 320px wide (or use DevTools responsive view)
4. These quick checks reveal structure, reading order, and reflow issues

---

## Phase 1: Keyboard-Only Testing

Test **without** a screen reader. Just keyboard + browser.

### Setup
- Close all DevTools
- Start at the top of the page
- Press Tab and follow focus through the entire page

### Checks

**Focus visible:**
- [ ] Every interactive element shows a visible focus indicator when Tab reaches it
- [ ] Focus indicator has at least 3:1 contrast against adjacent colors (SC 1.4.11)
- [ ] Focused elements are not entirely hidden behind sticky UI or overlays while tabbing (SC 2.4.11)
- [ ] Focus is never invisible (hidden outline, zero-width, off-screen)

**Focus order:**
- [ ] Tab sequence follows the logical reading order (left-to-right, top-to-bottom for English)
- [ ] Focus does not skip important interactive elements
- [ ] Focus does not jump to unexpected locations

**Keyboard activation:**
- [ ] All links activate with Enter
- [ ] All buttons activate with Enter AND Space
- [ ] All form fields accept keyboard input
- [ ] Checkboxes toggle with Space
- [ ] Radio buttons navigate with arrow keys; Space selects

**Skip navigation:**
- [ ] A skip link appears when you Tab from the top of the page
- [ ] Skip link leads to the main content

**Composite widgets:**
- [ ] Menus open with Enter/Space; items navigate with arrow keys; Escape closes
- [ ] Tab panels: arrow keys move between tabs; Tab enters the panel content
- [ ] Accordions open/close with Enter or Space
- [ ] Modals: focus moves inside on open; focus trapped inside; Escape closes; focus returns to trigger

**No keyboard traps:**
- [ ] You can Tab through the entire page without getting stuck anywhere
- [ ] If a widget captures keyboard input (e.g., text editor), there is a way to exit with keyboard

---

## Phase 2: Visual and Zoom Testing

**Text resize:**
- [ ] Zoom browser to 200% — no content overlap, no horizontal scroll except in tables/images
- [ ] Zoom to 400% — content reflows to single column; no content is lost (SC 1.4.10)

**Text spacing:**
Apply WCAG 1.4.12 test bookmarklet (see automated-testing.md) or manually set:
- `line-height: 1.5`
- `letter-spacing: 0.12em`
- `word-spacing: 0.16em`
- `margin-bottom: 2em` on all paragraphs

- [ ] No content is clipped, overlapping, or hidden
- [ ] No horizontal scrollbar appears (except in pre/tables)

**Color and contrast:**
- [ ] Check text contrast with Colour Contrast Analyser (minimum 4.5:1 for body, 3:1 for large text)
- [ ] Check UI component contrast (borders, icons) — minimum 3:1 (SC 1.4.11)
- [ ] Test with a grayscale filter (Chrome DevTools → Rendering → Emulate vision deficiencies → Achromatopsia)
- [ ] All information conveyed by color is also conveyed by another visual means

**Images and media:**
- [ ] Alt text appears for images (use axe or hover over images in some browsers)
- [ ] Decorative images have empty alt (`alt=""`)
- [ ] Videos have captions (look for CC button)
- [ ] Auto-playing video has a pause button visible
- [ ] Animated content: verify Escape or pause control works

---

## Phase 3: Forms and Errors

**Labels:**
- [ ] Every input field has a visible label
- [ ] Click the label — does focus move to the input? (confirms programmatic association)
- [ ] Groups of related inputs (checkboxes, radios) have a group label (`<legend>`)

**Instructions and hints:**
- [ ] Format requirements shown before the field (e.g., "MM/DD/YYYY")
- [ ] Required fields marked with indicator AND in label/instructions

**Errors:**
1. Submit the form with no data
- [ ] Error messages appear
- [ ] Error messages describe what went wrong and how to fix it
- [ ] Error messages are associated with their field (proximate)
2. Fill in invalid data; submit
- [ ] Field shows error state
- [ ] Error message is specific (not just "invalid")

**Autocomplete:**
- [ ] Personal data fields (name, email, address, payment) have correct `autocomplete` attribute
- [ ] Password fields allow paste (paste a copied password — should work)

---

## Phase 4: Content and Structure

**Headings (DevTools or Headings Map extension):**
- [ ] Page has a clear main heading (`<h1>`)
- [ ] Heading levels create a sensible outline and are not used only for visual styling
- [ ] Headings describe the content that follows
- [ ] Major sections of content have headings

**Links:**
- [ ] No links say only "click here," "here," "read more," "more," or show a bare URL
- [ ] Links that open in a new tab/window warn the user (visually or in link text)
- [ ] All links navigate somewhere (no `href="#"` dead links)

**Images:**
- [ ] Meaningful images have descriptive alt text (hover to check in browser, or use DevTools → Image element → `alt`)
- [ ] Decorative images: `alt=""` (check via DevTools)
- [ ] Complex images (charts, infographics) have adjacent text description

**Language:**
- [ ] `<html lang="en">` (or correct language code) is set — check DevTools → Elements

**Page title:**
- [ ] Browser tab shows a descriptive, unique title for each page

---

## Phase 5: Dynamic Content

**Live regions:**
After triggering dynamic updates (search results, loading states, notifications):
- [ ] Important status messages are in `role="status"` or `role="alert"` containers
- [ ] If audio available (or using a screen reader): check that updates are announced

**Modals and dialogs:**
1. Open a modal
- [ ] Browser focus moves inside the modal
- [ ] Tab stays within the modal
2. Close the modal (Escape or close button)
- [ ] Focus returns to the element that opened the modal

**SPAs (if applicable):**
- [ ] After navigating to a new route, the page title updates
- [ ] After navigating, focus moves to main content area (not stuck on the nav link)

---

## Phase 6: Device and Platform Checks

**Mobile (recommended: real device or emulator):**
- [ ] All content visible at 320px width (iPhone SE size)
- [ ] Touch targets are at least 44×44px
- [ ] Pinch-zoom is not blocked (`user-scalable=no` is NOT used in viewport meta)

**Print:**
- [ ] Print preview shows readable content (check if print.css hides important content)

---

## Severity Levels

When logging issues:

| Level | Criteria |
|-------|----------|
| Critical | Complete barrier — feature entirely inaccessible to AT users |
| Serious | Significant barrier — major difficulty; workaround not obvious |
| Moderate | Meaningful barrier — harder to use but can work around |
| Minor | Inconvenience — deviation from best practice; minimal impact |

---

## Issue Documentation Template

```
Issue: [brief description]
SC: [WCAG SC number, e.g., SC 1.1.1]
Level: [A / AA / AAA]
Severity: [Critical / Serious / Moderate / Minor]
Affected AT: [Screen readers / Keyboard-only / Voice control / Other]
Steps to reproduce:
  1.
  2.
  3.
Current behavior: [what happens]
Expected behavior: [what should happen]
Code snippet: [relevant HTML/CSS]
Fix recommendation: [suggested fix]
```
