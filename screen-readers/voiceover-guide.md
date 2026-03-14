---
title: "VoiceOver Screen Reader Guide for Testing"
standard: ""
source_url: "https://support.apple.com/guide/voiceover/welcome/mac"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["voiceover", "screen-reader", "testing", "macos", "ios", "apple", "keyboard-commands"]
ai_context: "VoiceOver key commands and testing workflow for macOS and iOS. Load when writing VoiceOver testing instructions."
---

# VoiceOver Screen Reader Guide for Testing

---

## About VoiceOver

VoiceOver is Apple's built-in screen reader, available on macOS, iOS, iPadOS, watchOS, and tvOS at no additional cost. **Required test combination: VoiceOver + Safari on macOS and iOS.**

VoiceOver is the only screen reader fully supported on Apple platforms. Always test web content with VoiceOver + Safari for Apple user coverage.

---

## VO Key (VoiceOver Modifier)

The **VO key** = `Control + Option` on macOS keyboard.

In this guide, **VO** = Control + Option.

---

## Enabling VoiceOver

**macOS:**
- Keyboard shortcut: `Command + F5`
- Settings → Accessibility → VoiceOver → Enable VoiceOver

**iOS/iPadOS:**
- Settings → Accessibility → VoiceOver → Turn On
- Or: Triple-click side button (if set up in Accessibility Shortcut)

---

## macOS VoiceOver — Essential Commands

### Basic Navigation

| Action | Key |
|--------|-----|
| Enable/disable VoiceOver | `Command + F5` |
| Read from top | `VO + Home` |
| Read all | `VO + A` |
| Stop reading | `Control` |
| Read current item | `VO + F3` |
| Move to next item | `VO + Right Arrow` |
| Move to previous item | `VO + Left Arrow` |
| Interact with group | `VO + Shift + Down Arrow` |
| Stop interacting | `VO + Shift + Up Arrow` |
| Activate item | `VO + Space` |
| Go to linked item | `VO + J` |

### Web Navigation

| Action | Key |
|--------|-----|
| Open Web Rotor | `VO + U` |
| Next heading | `VO + Command + H` |
| Previous heading | `VO + Command + Shift + H` |
| Next link | `VO + Command + L` |
| Next visited link | `VO + Command + V` |
| Next form control | `VO + Command + J` |
| Next table | `VO + Command + T` |
| Next landmark | `VO + Command + M` |
| Next image | `VO + Command + G` |

### Web Rotor (`VO + U`)

The Rotor is a circular menu that filters by element type. Use left/right arrow to choose the category, then up/down to navigate to items.

Rotor categories: Headings, Links, Form Controls, Tables, Landmarks, Images, Frames, and more.

### Table Navigation

| Action | Key |
|--------|-----|
| Move between table cells | `VO + Arrow Keys` |
| Read column header | VoiceOver announces header as you navigate |

---

## VoiceOver Verbosity

`VoiceOver Utility (VO + F8) → Verbosity`

Key settings for testing:
- **Announcements** — What VoiceOver announces for various element types
- **Speech** — Rate, pitch for different content types
- **Hints** — Whether usage hints are announced ("Press VO+Space to activate")

For testing at default verbosity, leave settings at default to replicate typical user experience.

---

## iOS VoiceOver — Gestures

| Action | Gesture |
|--------|---------|
| Read next item | Swipe right with 1 finger |
| Read previous item | Swipe left with 1 finger |
| Activate item | Double tap with 1 finger |
| Scroll up | Three-finger swipe up |
| Scroll down | Three-finger swipe down |
| Open Rotor | Rotate two fingers (like turning a dial) |
| Cycle Rotor option | Swipe up/down (after opening Rotor) |
| Read from top | Two-finger swipe up |
| Pause/continue reading | Two-finger tap |
| Go back | Two-finger Z gesture |
| Dismiss notification | Two-finger scrub (Z) |

### iOS Rotor

Common Rotor categories for web:
- Headings
- Links
- Form Controls
- Tables
- Landmarks
- Words (for character/word navigation)
- Lines

---

## Common VoiceOver Announcements (Expected)

| Element | Expected Announcement (macOS) |
|---------|-------------------------------|
| `<h2>Products</h2>` | "Products — heading level 2" |
| `<button aria-expanded="false">Menu</button>` | "Menu — collapsed — button" |
| `<input type="text" aria-label="Search">` | "Search — text field" |
| `<input type="checkbox" checked>` (with label) | "Subscribe — checked — checkbox" |
| `<a href="/about">About us</a>` | "About us — link" |
| `<img alt="Company logo">` | "Company logo — image" |
| `<img alt="">` | (Silent) |
| `role="alert"` content | Immediately: text of alert |
| `role="status"` update | After pause: status text |

---

## VoiceOver vs. NVDA/JAWS Key Differences

| Behavior | VoiceOver | NVDA/JAWS |
|---------|-----------|-----------|
| Modifier key | Control + Option | Insert |
| Quick keys (H for heading, etc.) | Not available; use Rotor | Available in Browse Mode |
| Rotor/Elements List | Rotor (VO + U) | Elements List (NVDA + F7) |
| Browser pairing | Must use Safari for full support | Any browser works |
| Platform | macOS/iOS only | Windows only |
| Mode switching | Automatic | Browse/Forms Modes |

---

## VoiceOver + Safari vs. VoiceOver + Chrome

**Always use Safari for iOS VoiceOver testing.** VoiceOver on iOS only works correctly with Safari for web content.

On macOS:
- VoiceOver + Safari is the primary supported combination
- VoiceOver + Chrome works but has more inconsistencies with custom ARIA
- Test in Safari as primary; Chrome as secondary

---

## Common Testing Pitfalls

| Issue | Symptom | What to Check |
|-------|---------|--------------|
| Focus doesn't move to modal | Open dialog; VoiceOver stays on page | `focus()` call after modal opens |
| Rotor shows no headings | No headings listed | Check that elements have heading roles/tags |
| No landmark in Rotor | Can't navigate by landmark | Verify `<main>`, `<nav>`, `<header>` in markup |
| Incorrect tab order | Tab sequence doesn't match visual | DOM order vs. visual order mismatch |
| aria-live not announced | Status messages silent | Check live region exists before content update |
| Custom widget not interactive | Can't activate with VO + Space | Missing role or tabindex |

---

## Testing Custom Interactive Components

For each widget, test:
1. Navigate to widget with Tab
2. VoiceOver should announce: name + role + state (e.g., "Menu button, collapsed, button")
3. Activate with `VO + Space`
4. VoiceOver should announce state change or new content
5. Navigate internal items
6. Close/dismiss; focus should return to trigger
