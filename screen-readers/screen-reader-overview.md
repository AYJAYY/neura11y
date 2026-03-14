---
title: "Screen Reader Overview"
standard: ""
source_url: ""
domain: ["web", "general"]
last_fetched: "2026-03-13"
status: "curated"
last_reviewed: "2026-03-13"
tags: ["screen-readers", "jaws", "nvda", "voiceover", "talkback", "narrator", "at"]
ai_context: "Overview of major screen readers, their platforms, usage statistics, and browser pairings. Load when generating code that needs to work with specific AT."
---

# Screen Reader Overview

---

## Major Screen Readers

### JAWS (Job Access With Speech)

- **Platform:** Windows
- **Vendor:** Freedom Scientific (Vispero)
- **Cost:** Commercial ($90–$1,100+ per year depending on license)
- **Browser pairing:** Chrome (primary), Firefox, Edge
- **Usage:** ~30-40% of screen reader users (varies by survey)
- **Version cadence:** Major annual releases
- **Key features:** Most comprehensive AT support; widely used in enterprise and government

### NVDA (NonVisual Desktop Access)

- **Platform:** Windows
- **Vendor:** NV Access (nonprofit)
- **Cost:** Free (donations accepted)
- **Browser pairing:** Chrome (primary), Firefox
- **Usage:** ~30-40% of screen reader users
- **Version cadence:** ~4 releases per year
- **Key features:** Open source; widely used by individuals; excellent Chrome/Firefox support

### VoiceOver

- **Platform:** macOS, iOS, iPadOS, tvOS, watchOS
- **Vendor:** Apple
- **Cost:** Free (built into Apple devices)
- **Browser pairing:** Safari (primary on Apple); Chrome (secondary)
- **Usage:** ~15-20% on desktop; dominant on iOS/iPadOS
- **Key features:** Gesture-based navigation on mobile; integrated into OS

### TalkBack

- **Platform:** Android
- **Vendor:** Google
- **Cost:** Free (built into Android)
- **Browser pairing:** Chrome
- **Usage:** Dominant on Android
- **Key features:** Touch exploration; swipe gestures; integration with Android accessibility APIs

### Narrator

- **Platform:** Windows
- **Vendor:** Microsoft
- **Cost:** Free (built into Windows)
- **Browser pairing:** Edge (primary); Chrome
- **Usage:** ~5-10% (growing; improved significantly in Windows 10/11)
- **Key features:** Deep integration with Windows; accessible from login screen

### Orca

- **Platform:** Linux (GNOME)
- **Vendor:** GNOME Project
- **Cost:** Free (open source)
- **Browser pairing:** Firefox (primary)
- **Usage:** Small percentage; primarily Linux users
- **Key features:** Braille display support; flexible configuration

---

## Market Share (Approximate, 2024-2025)

Source: WebAIM Screen Reader User Survey (conducted periodically)

| Screen Reader | Approx. Share | Platform |
|---|---|---|
| JAWS | 40% | Windows |
| NVDA | 37% | Windows |
| VoiceOver | 10% | macOS |
| VoiceOver (iOS) | Separate metric | iOS |
| TalkBack | Separate metric | Android |
| Narrator | 5% | Windows |
| Other | 8% | Various |

**Important:** Most users use more than one screen reader. Mobile (iOS/Android) usage is tracked separately in WebAIM surveys.

---

## Recommended Testing Combinations

Minimum recommended for web testing:

| Priority | Screen Reader | Browser | Platform |
|----------|---|---|---|
| 1 (Critical) | NVDA | Chrome | Windows |
| 2 (Critical) | VoiceOver | Safari | macOS |
| 3 (Important) | JAWS | Chrome | Windows |
| 4 (Important) | VoiceOver | Safari | iOS |
| 5 (Nice to have) | TalkBack | Chrome | Android |

Test in this order because:
- NVDA + Chrome = most commonly tested AT pair; free to use
- VoiceOver + Safari = required for iOS testing; key Apple ecosystem
- JAWS = most common enterprise/government AT; commercial license required
- iOS VoiceOver = represents all iOS/iPadOS users

---

## Screen Reader Key Commands Quick Reference

### NVDA (Windows)

**NVDA modifier key:** Insert (or Caps Lock)

| Task | Command |
|------|---------|
| Start/stop reading | NVDA + Down Arrow |
| Stop reading | Control |
| Headings list | NVDA + F7 |
| Links list | NVDA + F7 |
| Next heading | H |
| Next link | K |
| Next form field | F |
| Next table | T |
| Next landmark | D |
| Next button | B |
| Navigate table cells | Control + Alt + Arrow keys |
| Toggle browse/focus mode | NVDA + Space |

### VoiceOver (macOS)

**VoiceOver modifier:** Control + Option (VO)

| Task | Command |
|------|---------|
| Start VoiceOver | Command + F5 |
| Next element | VO + Right Arrow |
| Previous element | VO + Left Arrow |
| Open rotor | VO + U |
| Click element | VO + Space |
| Next heading | VO + Command + H |
| Headings rotor | VO + U → Headings |
| Web item navigation | Navigate with rotor |
| Enter/exit web area | VO + Shift + Down / Up |

### VoiceOver (iOS)

| Task | Gesture |
|------|---------|
| Next element | Swipe right |
| Previous element | Swipe left |
| Activate element | Double tap |
| Scroll | Three-finger swipe |
| Rotor (navigation type) | Two-finger rotation |
| Navigate by headings | Set rotor to Headings; swipe up/down |

### JAWS (Windows)

**JAWS key:** Insert

| Task | Command |
|------|---------|
| Read page | JAWS + Down Arrow |
| Stop reading | Control |
| Headings list | JAWS + F6 |
| Links list | JAWS + F7 |
| Next heading | H |
| Next link | Enter (on link) |
| Virtual HTML features | JAWS + F3 |
| Toggle virtual/PC cursor | JAWS + Z |

---

## ARIA Support Differences

Screen readers have varying levels of ARIA support. See `screen-readers/sr-aria-support-matrix.md` for a detailed matrix.

Key general notes:
- Most ARIA roles are well-supported in JAWS, NVDA, VoiceOver
- New ARIA roles (ARIA 1.2 additions) may have patchy support in older SR versions
- `aria-live` support is generally good but timing varies
- Complex composite widgets (tree, treegrid, grid) have the most variation
- Mobile screen readers (VoiceOver/iOS, TalkBack) have different interaction models

---

## Screen Reader Testing Checklist

- [ ] All headings are announced with correct level (h1, h2, etc.)
- [ ] All form controls have accessible names announced
- [ ] Error messages are announced when they appear (live region or focus movement)
- [ ] Modal dialogs trap focus and are announced as dialogs
- [ ] Expanded/collapsed state is announced for accordions and menus
- [ ] Tables have headers announced for each cell
- [ ] Images have alt text announced (non-decorative)
- [ ] Decorative images are skipped
- [ ] Status messages are announced via live region
- [ ] Page title is announced on load/navigation
- [ ] Keyboard shortcuts work as expected
- [ ] Custom components (tabs, combobox, etc.) follow APG keyboard patterns
