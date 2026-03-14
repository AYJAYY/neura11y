---
title: "WCAG 2.2 Quick Reference — All Success Criteria"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/WCAG22/quickref/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["wcag", "wcag-2.2", "quick-ref", "success-criteria", "all-sc", "pour"]
ai_context: "Complete reference for all 87 WCAG 2.2 success criteria with levels, intent, and key techniques. The most important single file in this repository. Always load this for accessibility auditing or content generation tasks."
---

# WCAG 2.2 Quick Reference

All 87 success criteria from WCAG 2.2 (W3C Recommendation, October 5, 2023). Organized by the four POUR principles and 13 guidelines. [NEW 2.2] indicates criteria added in WCAG 2.2.

---

## Principle 1: Perceivable

Information and user interface components must be presentable to users in ways they can perceive.

### Guideline 1.1 — Text Alternatives

Provide text alternatives for any non-text content so that it can be changed into other forms people need.

#### SC 1.1.1 — Non-text Content — Level A

**Intent:** All non-text content has a text alternative that serves the equivalent purpose.

**Applies to:** Images, image buttons, image maps, CAPTCHA, audio/video, charts, decorative images.

**Key requirements:**
- Informative images: `alt` text that conveys the same information
- Functional images (e.g., image buttons): `alt` text describes the function
- Decorative images: `alt=""` (empty alt) or CSS background image
- CAPTCHA: text alternative identifies it as CAPTCHA + provides alternative accessible form
- Complex images (charts, diagrams): short alt + long description

**Sufficient techniques:** G94 (short text alternative), G95 (supplemental description for complex), H36 (alt for input type=image), H37 (img alt attribute), H53 (using body of object), H86 (providing text alternatives for ASCII art), ARIA6 (aria-label), ARIA10 (aria-labelledby)

**Common failures:** F3 (CSS background image without text), F13 (alt does not match image function), F20 (alt text does not include all text in image), F30 (placeholder alt), F38 (alt="" on functional image), F65 (alt omitted entirely), F67 (null alt on content image)

---

### Guideline 1.2 — Time-based Media

Provide alternatives for time-based media.

#### SC 1.2.1 — Audio-only and Video-only (Prerecorded) — Level A

**Intent:** Prerecorded audio-only and video-only content has an equivalent text or audio alternative.

- Audio-only: provide a text transcript
- Video-only (no audio): provide either a text transcript OR an audio track that presents equivalent information

**Sufficient techniques:** G158 (audio-only transcript), G159 (video-only alternative), G166 (audio track for video-only)

#### SC 1.2.2 — Captions (Prerecorded) — Level A

**Intent:** Captions are provided for all prerecorded audio content in synchronized media.

**Key requirements:**
- Captions must be synchronized with the audio
- Captions include all dialogue, speaker identification, sound effects, music descriptions
- Auto-generated captions are NOT sufficient without human review and correction

**Sufficient techniques:** G87 (closed captions), G93 (open captions), SM11 (SMIL 1.0), SM12 (SMIL 2.0)
**Common failures:** F8 (captions omit dialogue), F74 (captions not synchronized), F75 (automated captions used as-is)

#### SC 1.2.3 — Audio Description or Media Alternative (Prerecorded) — Level A

**Intent:** An audio description or text alternative is provided for video content.

- Either provide audio description OR a full text alternative that includes all visual information
- Level A allows text alternative as an option; Level AA (SC 1.2.5) requires audio description

**Sufficient techniques:** G69 (text alternative for synchronized media), G78 (audio description track), G173 (audio description version)

#### SC 1.2.4 — Captions (Live) — Level AA

**Intent:** Captions are provided for all live audio content in synchronized media.

- Live captions must be provided for live video/audio broadcasts
- CART (Communication Access Realtime Translation) or live captioning service required
- Quality standard is lower than prerecorded; some lag and minor errors acceptable

**Sufficient techniques:** G9 (create captions for live synchronized media), G87 (closed captions for live)

#### SC 1.2.5 — Audio Description (Prerecorded) — Level AA

**Intent:** Audio description is provided for all prerecorded video content in synchronized media.

- Audio description narrates visual information not conveyed in the existing audio
- Must be synchronized with the video
- Text alternative alone does NOT satisfy this criterion (unlike SC 1.2.3)

**Sufficient techniques:** G78 (second audio track), G173 (described video version), SM6/SM7 (SMIL audio description)

#### SC 1.2.6 — Sign Language (Prerecorded) — Level AAA

**Intent:** Sign language interpretation is provided for all prerecorded audio content.

#### SC 1.2.7 — Extended Audio Description (Prerecorded) — Level AAA

**Intent:** Extended audio description (with video pauses) provided where standard audio description insufficient.

#### SC 1.2.8 — Media Alternative (Prerecorded) — Level AAA

**Intent:** Full text alternative provided for synchronized media including video.

#### SC 1.2.9 — Audio-only (Live) — Level AAA

**Intent:** Text alternative that presents equivalent information for live audio-only content.

---

### Guideline 1.3 — Adaptable

Create content that can be presented in different ways without losing information or structure.

#### SC 1.3.1 — Info and Relationships — Level A

**Intent:** Information, structure, and relationships conveyed visually can be programmatically determined or available in text.

**Key requirements:**
- Headings marked with heading elements, not just bold/large text
- Lists marked with `<ul>`, `<ol>`, `<dl>`
- Tables use `<th>` with scope for headers
- Required fields identified programmatically, not just visually
- Form grouping uses `<fieldset>`/`<legend>`
- ARIA used where native HTML insufficient

**Sufficient techniques:** H42 (heading elements), H43 (table headers), H44 (label for), H48 (lists), H49 (semantic markup), H51 (table markup), H71 (fieldset/legend), ARIA11 (landmark regions), ARIA12 (using role=heading), ARIA16 (aria-labelledby for field label)

**Common failures:** F2 (only visual formatting to convey structure), F33 (multiple spaces to create layout), F34 (whitespace for formatting), F42 (using scripting to make span/div a link), F43 (non-list use of li), F46 (layout table)

#### SC 1.3.2 — Meaningful Sequence — Level A

**Intent:** The correct reading sequence can be programmatically determined when sequence affects meaning.

- DOM order must match visual/logical reading order
- CSS that changes visual order (flexbox `order`, absolute positioning) must match logical DOM order for AT

**Common failures:** F34 (whitespace characters for layout), F33 (spaces for alignment), F32 (using white space characters for layout)

#### SC 1.3.3 — Sensory Characteristics — Level A

**Intent:** Instructions do not rely solely on sensory characteristics (shape, color, size, visual location, orientation, sound).

**Failures:** "Click the round button," "See the information in red," "Use the button on the right"
**Passes:** "Click the Search button" (uses label, not just location)

#### SC 1.3.4 — Orientation — Level AA

**Intent:** Content does not restrict its view and operation to a single display orientation unless essential.

- Do not lock content to portrait or landscape only
- Exceptions: ATM machines, musical keyboard apps
- `<meta name="viewport">` must not prevent rotation

**Common failure:** CSS `orientation: portrait` media query that hides critical content in landscape

#### SC 1.3.5 — Identify Input Purpose — Level AA

**Intent:** The purpose of each input field collecting personal information can be programmatically determined.

**Requirement:** Use `autocomplete` attribute with the correct token for personal data inputs.

**Key autocomplete values:**
- `name`, `given-name`, `family-name`, `additional-name`
- `email`, `tel`, `tel-national`
- `street-address`, `address-line1`, `address-line2`, `address-level1`, `address-level2`, `postal-code`, `country-name`
- `bday`, `bday-day`, `bday-month`, `bday-year`
- `sex`, `url`, `photo`
- `cc-name`, `cc-number`, `cc-exp`, `cc-csc`
- `current-password`, `new-password`
- `username`

**Sufficient techniques:** H98 (using autocomplete attribute)

#### SC 1.3.6 — Identify Purpose — Level AAA

**Intent:** The purpose of UI components, icons, and regions can be programmatically determined.

---

### Guideline 1.4 — Distinguishable

Make it easier for users to see and hear content including separating foreground from background.

#### SC 1.4.1 — Use of Color — Level A

**Intent:** Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

**Examples that fail:**
- Required fields marked only by red text
- Error messages identified only by red color
- Links distinguished from body text only by color (no underline, no other visual cue)
- Charts where data series are differentiated only by color

**Fixes:** Add underline to links, use icons/symbols alongside color, add patterns to chart elements, use text labels

#### SC 1.4.2 — Audio Control — Level A

**Intent:** If audio plays automatically for more than 3 seconds, either a mechanism to pause/stop it exists, or volume can be controlled independently of system volume.

**Common failure:** Auto-playing background music without a mute or stop control

#### SC 1.4.3 — Contrast (Minimum) — Level AA

**Intent:** Text and images of text have sufficient contrast against their background.

**Exact thresholds:**
- Normal text: contrast ratio ≥ **4.5:1**
- Large text (≥18pt / ≥24px regular, OR ≥14pt / ≥18.67px bold): contrast ratio ≥ **3:1**
- Incidental text (inactive UI, decorative, logo): no requirement
- Logotypes: no requirement

**Contrast ratio formula:** (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter color's relative luminance and L2 is the darker color's relative luminance. L = 0 is black, L = 1 is white.

**Sufficient techniques:** G18 (4.5:1), G145 (3:1 large text), G148 (no background image on text)
**Tools:** WebAIM Contrast Checker, browser DevTools, Colour Contrast Analyser

#### SC 1.4.4 — Resize Text — Level AA

**Intent:** Text can be resized without assistive technology up to 200% without loss of content or functionality.

- Use relative units (rem, em, %) not px for font sizes
- Don't use `user-scalable=no` in viewport meta tag
- Layout must not break at 200% text size (horizontal scrolling acceptable within a 2D layout failure)

**Common failures:** F69 (loss of content at 200%), F80 (text-based form control that does not resize)

#### SC 1.4.5 — Images of Text — Level AA

**Intent:** If the visual presentation can be achieved with text, use text rather than images of text.

- Logos and essential images of text are exempt
- Customizable images of text (user can adjust) are exempt

#### SC 1.4.6 — Contrast (Enhanced) — Level AAA

**Thresholds:** Normal text ≥ **7:1**, large text ≥ **4.5:1**

#### SC 1.4.7 — Low or No Background Audio — Level AAA

**Intent:** Prerecorded audio-only content contains no background audio, or background audio is 20dB lower than foreground speech.

#### SC 1.4.8 — Visual Presentation — Level AAA

**Intent:** For blocks of text: foreground/background selectable, width ≤80 chars, not fully justified, line spacing ≥1.5×, paragraph spacing ≥1.5× line spacing, no horizontal scrolling at 256% resize.

#### SC 1.4.9 — Images of Text (No Exception) — Level AAA

**Intent:** Images of text used only for decoration or where specific presentation is essential.

#### SC 1.4.10 — Reflow — Level AA

**Intent:** Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
- Vertical scrolling content at width equivalent to 320 CSS pixels
- Horizontal scrolling content at height equivalent to 256 CSS pixels

**Key points:**
- 320 CSS pixels = 1280px viewport at 400% zoom
- 2D scrolling layouts (data tables, maps, code blocks) are exempt
- Mobile-first responsive design satisfies this

**Common failure:** Fixed-width layouts that require horizontal scrolling at 320px width

#### SC 1.4.11 — Non-text Contrast — Level AA

**Intent:** UI components and graphical objects have a contrast ratio of at least 3:1 against adjacent colors.

**Applies to:**
- Form control borders (input, select, textarea outlines)
- Focus indicators (see also SC 2.4.7, 2.4.11)
- Icons that convey information (not purely decorative)
- Chart lines, data points
- Video controls

**Exact threshold:** **3:1** contrast ratio

**Common failures:** Gray input borders on white background (often fails), light gray icons on white background, light blue links without underline

#### SC 1.4.12 — Text Spacing — Level AA

**Intent:** No loss of content when these text spacing properties are overridden:
- Line height: at least **1.5×** font size
- Letter spacing: at least **0.12×** font size
- Word spacing: at least **0.16×** font size
- Spacing following paragraphs: at least **2×** font size

**Key point:** Content must be readable when ALL four overrides are applied simultaneously. Fixed-height containers that clip text commonly fail.

**Bookmarklet test:** The Text Spacing bookmarklet (Pave/ADP) applies these overrides for testing.

#### SC 1.4.13 — Content on Hover or Focus — Level AA

**Intent:** Content that appears on hover or keyboard focus is dismissible, hoverable, and persistent.

**Three conditions, all required:**
1. **Dismissible:** Can be dismissed without moving pointer/focus (e.g., Escape key dismisses tooltip)
2. **Hoverable:** Pointer can move to the appearing content without it disappearing
3. **Persistent:** Content remains until hover/focus removed, user dismisses, or it becomes invalid

**Applies to:** Custom tooltips, hover menus, dropdown content triggered by hover/focus

---

## Principle 2: Operable

User interface components and navigation must be operable.

### Guideline 2.1 — Keyboard Accessible

Make all functionality available from a keyboard.

#### SC 2.1.1 — Keyboard — Level A

**Intent:** All functionality is operable through a keyboard interface without requiring specific timing for individual keystrokes.

**Exceptions:** Path-dependent input (freehand drawing, calligraphy) is exempt

**Common failures:** Custom JS-only controls (div, span used as buttons), drag-only functionality, mouse-hover-triggered dropdowns that can't be reached by keyboard, click handlers only (no keydown/keyup equivalents)

**Sufficient techniques:** G202 (keyboard accessible), H91 (native HTML form controls), SCR20 (using keyboard and device-independent handlers), SCR35 (using onclick with keyboard)

#### SC 2.1.2 — No Keyboard Trap — Level A

**Intent:** Keyboard focus can be moved away from a component using only the keyboard. If non-standard keys are needed, the user is informed.

**Most important SC for keyboard users.** A keyboard trap prevents users from escaping a section of the page.

**Exception:** Modals may trap focus intentionally but must allow Escape to close.

**Common failure:** Flash objects, PDF embeds, custom widgets that capture all key events

#### SC 2.1.3 — Keyboard (No Exception) — Level AAA

**Intent:** All functionality is keyboard accessible with no path-dependent input exceptions.

#### SC 2.1.4 — Character Key Shortcuts — Level A

**Intent:** If a keyboard shortcut uses only letter, punctuation, number, or symbol characters, there is a mechanism to turn it off, remap it, or the shortcut is only active when the relevant component has focus.

**Reason:** Single-key shortcuts conflict with screen reader key commands and voice control.

---

### Guideline 2.2 — Enough Time

Provide users enough time to read and use content.

#### SC 2.2.1 — Timing Adjustable — Level A

**Intent:** For time limits, user can turn off, adjust (to at least 10× the default), or extend (at least 20 seconds notice with 10× extension).

**Exceptions:** Real-time events (auctions), security timeouts with notice, >20 hours

#### SC 2.2.2 — Pause, Stop, Hide — Level A

**Intent:** Moving, blinking, scrolling, auto-updating content can be paused, stopped, or hidden. Auto-updating info can be controlled.

**Applies to:** Carousels, marquees, auto-playing video, news tickers, live social media feeds

#### SC 2.2.3 — No Timing — Level AAA

**Intent:** Timing is not an essential part of the event or activity, with the exception of non-interactive synchronized media and real-time events.

#### SC 2.2.4 — Interruptions — Level AAA

**Intent:** Interruptions can be postponed or suppressed except for emergencies.

#### SC 2.2.5 — Re-authenticating — Level AAA

**Intent:** Data is preserved after authentication expiry so users can re-authenticate without data loss.

#### SC 2.2.6 — Timeouts — Level AAA

**Intent:** Users are warned of the duration of any user inactivity that could cause data loss, unless data is preserved for more than 20 hours.

---

### Guideline 2.3 — Seizures and Physical Reactions

Do not design content in a way that is known to cause seizures or physical reactions.

#### SC 2.3.1 — Three Flashes or Below Threshold — Level A

**Intent:** Content does not flash more than 3 times per second, or the flash is below the general flash and red flash thresholds.

**Threshold:** 3 flashes per second. Any content that flashes more rapidly and exceeds the area threshold must be remediated.

#### SC 2.3.2 — Three Flashes — Level AAA

**Intent:** No content flashes more than 3 times per second (no area threshold exception).

#### SC 2.3.3 — Animation from Interactions — Level AAA

**Intent:** Motion animation triggered by interaction can be disabled unless essential.

**Recommendation:** Respect `prefers-reduced-motion` media query (CSS level advisory, not in WCAG 2.x normative but widely adopted as best practice).

---

### Guideline 2.4 — Navigable

Provide ways to help users navigate, find content, and determine where they are.

#### SC 2.4.1 — Bypass Blocks — Level A

**Intent:** A mechanism to bypass blocks of content that are repeated on multiple pages.

**Common implementation:** Skip navigation link (`<a href="#main-content">Skip to main content</a>`) as first focusable element. May be visually hidden until focused.

**Alternative:** Properly structured landmarks (`<nav>`, `<main>`) allow screen reader users to bypass via landmark navigation.

#### SC 2.4.2 — Page Titled — Level A

**Intent:** Web pages have titles that describe topic or purpose.

**Requirement:** `<title>` element is descriptive and unique per page. Format: "Page Name — Site Name"

**Common failures:** Generic titles ("Home," "Untitled"), duplicate titles across pages, empty `<title>`

#### SC 2.4.3 — Focus Order — Level A

**Intent:** If a web page can be navigated sequentially and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operation.

**Note:** Focus order must be logical, not necessarily top-left to bottom-right. The DOM order determines default tab order; `tabindex` values > 0 disrupt this.

#### SC 2.4.4 — Link Purpose (In Context) — Level A

**Intent:** The purpose of each link can be determined from the link text alone, or from link text + programmatically determinable context (sentence, list item, table cell, heading).

**Failures:** "Click here," "Read more," "Learn more" (without context), "Download" (without identifying the file)

**Techniques:** G91 (descriptive link text), H30 (a[href] text), H33 (supplementing with title attribute), ARIA7 (aria-labelledby), ARIA8 (aria-label)

#### SC 2.4.5 — Multiple Ways — Level AA

**Intent:** More than one way is available to locate a web page within a set, except where the page is the result of a process.

**Examples:** Site search + site map, navigation + table of contents, navigation + search
**Exception:** Checkout step 3 of 5 does not need alternate ways to reach it

#### SC 2.4.6 — Headings and Labels — Level AA

**Intent:** Headings and labels describe topic or purpose.

**Note:** Does not require headings or labels to exist (that's SC 1.3.1); requires that those that do exist are descriptive.

#### SC 2.4.7 — Focus Visible — Level AA

**Intent:** Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible.

**Note:** WCAG 2.2 adds SC 2.4.11 with specific minimum appearance requirements. SC 2.4.7 requires only that some focus indicator is visible.

#### SC 2.4.8 — Location — Level AAA

**Intent:** Information about the user's location within a set of web pages is available (breadcrumbs, site maps).

#### SC 2.4.9 — Link Purpose (Link Only) — Level AAA

**Intent:** A mechanism allows link purpose to be identified from link text alone (no context needed).

#### SC 2.4.10 — Section Headings — Level AAA

**Intent:** Section headings organize content.

#### SC 2.4.11 — Focus Appearance (Minimum) — Level AA [NEW in WCAG 2.2]

**Intent:** Keyboard focus indicator meets minimum area and contrast requirements.

**Requirements:**
- Area ≥ perimeter of unfocused component × 2 CSS pixels
- Contrast ratio ≥ 3:1 between focused and unfocused state color

See `wcag-2.2-new-criteria.md` for full specification.

#### SC 2.4.12 — Focus Not Obscured (Minimum) — Level AA [NEW in WCAG 2.2]

**Intent:** Focused component is not entirely hidden by author-created content (sticky headers, banners, overlays).

#### SC 2.4.13 — Focus Appearance (Enhanced) — Level AAA [NEW in WCAG 2.2]

**Intent:** Focus indicator fully encloses focused component; contrast ≥ 3:1 (focused/unfocused) and ≥ 4.5:1 against adjacent colors.

---

### Guideline 2.5 — Input Modalities

Make it easier for users to operate functionality through various inputs beyond keyboard.

#### SC 2.5.1 — Pointer Gestures — Level A

**Intent:** All functionality using multi-point or path-based gestures can be operated with a single pointer.

**Applies to:** Pinch-to-zoom (must have + / - buttons), swipe carousels (must have prev/next buttons), drawing paths

#### SC 2.5.2 — Pointer Cancellation — Level A

**Intent:** For single pointer functionality, at least one of: no down-event activation; can abort/undo; up-event reverses; down-event essential.

**Practical meaning:** Activation happens on `mouseup`/`pointerup`, not `mousedown`/`pointerdown`. Users can cancel by moving pointer away before releasing.

#### SC 2.5.3 — Label in Name — Level A

**Intent:** For UI components with visible text labels, the accessible name contains the visible text.

**Requirement:** `aria-label` or `aria-labelledby` must include the visible label text (exact match or begins with).

**Failures:** A button labeled "Submit" with `aria-label="Send form"` — voice control users saying "Submit" won't activate it. Fix: `aria-label="Submit form"` (starts with visible text "Submit").

#### SC 2.5.4 — Motion Actuation — Level A

**Intent:** Functionality operated by device motion or user motion can also be operated through user interface components, and response to motion can be disabled.

**Applies to:** Shake to undo, tilt to scroll, gyroscope-based interaction

#### SC 2.5.5 — Target Size (Enhanced) — Level AAA

**Threshold:** At least **44×44 CSS pixels** (no spacing exception)

#### SC 2.5.6 — Concurrent Input Mechanisms — Level AAA

**Intent:** Content does not restrict use of input modalities available on a platform (touch + keyboard + mouse must all work).

#### SC 2.5.7 — Dragging Movements — Level AA [NEW in WCAG 2.2]

**Intent:** All functionality using dragging has a single-pointer alternative.

See `wcag-2.2-new-criteria.md` for full specification.

#### SC 2.5.8 — Target Size (Minimum) — Level AA [NEW in WCAG 2.2]

**Threshold:** At least **24×24 CSS pixels** (with spacing exception)

See `wcag-2.2-new-criteria.md` for full specification.

---

## Principle 3: Understandable

Information and the operation of user interface must be understandable.

### Guideline 3.1 — Readable

Make text content readable and understandable.

#### SC 3.1.1 — Language of Page — Level A

**Intent:** The default human language of each web page can be programmatically determined.

**Requirement:** `<html lang="en">` (or appropriate language code). BCP 47 language tags.

**Common failures:** Missing `lang` attribute, wrong language code

#### SC 3.1.2 — Language of Parts — Level AA

**Intent:** The human language of each passage or phrase can be programmatically determined.

**Requirement:** `lang` attribute on elements containing text in a different language: `<span lang="fr">bonjour</span>`

**Exception:** Proper nouns, technical terms, indeterminate language

#### SC 3.1.3 — Unusual Words — Level AAA

**Intent:** Mechanism for identifying definitions of unusual words, idioms, jargon.

#### SC 3.1.4 — Abbreviations — Level AAA

**Intent:** Mechanism for identifying expanded form of abbreviations.

#### SC 3.1.5 — Reading Level — Level AAA

**Intent:** When content requires more than lower secondary education reading ability, supplemental content or a version requiring lower reading ability is available.

#### SC 3.1.6 — Pronunciation — Level AAA

**Intent:** Mechanism for identifying pronunciation of ambiguous words.

---

### Guideline 3.2 — Predictable

Make web pages appear and operate in predictable ways.

#### SC 3.2.1 — On Focus — Level A

**Intent:** When any UI component receives focus, it does not initiate a change of context.

**Failures:** Select menu that automatically navigates on focus change (without user confirmation); page redirect on focus; opening new window on focus

#### SC 3.2.2 — On Input — Level A

**Intent:** Changing a UI component setting does not automatically cause a change of context unless user is advised.

**Failures:** Form that auto-submits when all fields complete; select that navigates immediately on selection without Submit button

**Exception:** A submit button is a change of context; the warning requirement does not apply

#### SC 3.2.3 — Consistent Navigation — Level AA

**Intent:** Navigational mechanisms that are repeated on multiple pages occur in the same relative order.

#### SC 3.2.4 — Consistent Identification — Level AA

**Intent:** Components with the same functionality are identified consistently throughout a set of web pages.

**Example:** A search icon button must always have the same accessible name ("Search") across all pages

#### SC 3.2.5 — Change on Request — Level AAA

**Intent:** Changes of context are initiated only by user request, or a mechanism to turn off automatic changes is available.

#### SC 3.2.6 — Consistent Help — Level A [NEW in WCAG 2.2]

**Intent:** Help mechanisms (contact details, help links) appear in the same relative position across pages.

See `wcag-2.2-new-criteria.md` for full specification.

---

### Guideline 3.3 — Input Assistance

Help users avoid and correct mistakes.

#### SC 3.3.1 — Error Identification — Level A

**Intent:** If an input error is automatically detected, the item in error is identified and the error is described to the user in text.

**Requirements:**
- Error must be described in text (not only color, not only icon)
- The specific field in error must be identified
- The error message must describe what is wrong

**Sufficient techniques:** G83 (text description of errors), ARIA18 (aria-describedby for error), ARIA19 (aria-live for error announcements), SCR18 (validation on server and return)

**Common failures:** F81 (color-only error indication), F82 (no error description), F83 (email error says only "invalid format")

#### SC 3.3.2 — Labels or Instructions — Level A

**Intent:** Labels or instructions are provided when content requires user input.

**Requirements:**
- Every input must have a label
- If data format is important, describe it (e.g., "Date (MM/DD/YYYY)")
- Required fields must be indicated

#### SC 3.3.3 — Error Suggestion — Level AA

**Intent:** If an error is detected and suggestions for correction are known, the suggestion is provided (unless it jeopardizes security/purpose).

**Example:** "Please enter a valid email address" (not "Invalid input")

#### SC 3.3.4 — Error Prevention (Legal, Financial, Data) — Level AA

**Intent:** For legal commitments, financial transactions, test responses, and user-controlled data, at least one of: reversible, checked (user can review/correct before submitting), confirmed (explicit confirmation step).

#### SC 3.3.5 — Help — Level AAA

**Intent:** Context-sensitive help is available.

#### SC 3.3.6 — Error Prevention (All) — Level AAA

**Intent:** Same as 3.3.4 but for all form submissions (not just legal/financial).

#### SC 3.3.7 — Redundant Entry — Level A [NEW in WCAG 2.2]

**Intent:** Previously entered information does not need to be re-entered in same process.

See `wcag-2.2-new-criteria.md` for full specification.

#### SC 3.3.8 — Accessible Authentication (Minimum) — Level AA [NEW in WCAG 2.2]

**Intent:** No cognitive function test required for authentication (with limited exceptions).

See `wcag-2.2-new-criteria.md` for full specification.

#### SC 3.3.9 — Accessible Authentication (Enhanced) — Level AAA [NEW in WCAG 2.2]

**Intent:** No cognitive function test required for authentication (no object recognition exception).

---

## Principle 4: Robust

Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.

### Guideline 4.1 — Compatible

Maximize compatibility with current and future user agents, including assistive technologies.

#### SC 4.1.1 — Parsing — Level A [Obsolete in WCAG 2.2]

**Status:** Always passes in WCAG 2.2 context. HTML error correction by browsers means parsing errors no longer cause AT failures. HTML validation is still good practice but is not a WCAG 2.2 requirement.

#### SC 4.1.2 — Name, Role, Value — Level A

**Intent:** All UI components have an accessible name and role; states, properties, and values are programmatically determinable and can be set by user agents.

**Requirements:**
- Every interactive element must have an accessible name
- Role must be conveyed programmatically (HTML semantics or ARIA role)
- States must be conveyed (aria-expanded, aria-checked, aria-selected, etc.)
- User-settable values must be settable by AT (aria-valuenow, aria-checked)

**Sufficient techniques:** H44 (label for), H64 (title for iframe), H65 (title for input), H91 (native HTML), ARIA14 (aria-label), ARIA16 (aria-labelledby)

**Common failures:** F15 (custom controls without accessible name), F59 (non-interactive element with onclick), F68 (associated label not present), F79 (focus lost when element disabled)

#### SC 4.1.3 — Status Messages — Level AA

**Intent:** Status messages can be programmatically determined through role or property so they can be presented by AT without receiving focus.

**Requirements:**
- Success messages: `role="status"` (equivalent to `aria-live="polite"`)
- Error/alert messages: `role="alert"` (equivalent to `aria-live="assertive"`)
- Progress: `role="log"`, `role="progressbar"`
- Do NOT move focus to status messages — use live regions instead

**Common failures:** F103 (status change not exposed to AT), displaying status messages in elements without live region roles

---

## Conformance Levels Summary

| Level | Meaning | Count in WCAG 2.2 |
|-------|---------|-------------------|
| A | Minimum — must satisfy for any conformance claim | 30 criteria |
| AA | Standard — required by Section 508, EN 301 549, most legal frameworks | 20 additional criteria (50 total) |
| AAA | Enhanced — aspirational; not required for conformance | 28 additional criteria (78 total) |

**Note:** Conformance is all-or-nothing per level. Satisfying 49 of 50 AA criteria does NOT constitute AA conformance. All criteria at the claimed level must be satisfied on the entire page.

**WCAG 2.2 vs 2.1:** WCAG 2.2 adds 9 new criteria (+6 AA, +1 A, +2 AAA) and makes SC 4.1.1 always passing. All WCAG 2.1 criteria remain in WCAG 2.2. Organizations conforming to WCAG 2.1 AA must add 6 new AA criteria to conform to WCAG 2.2 AA.
