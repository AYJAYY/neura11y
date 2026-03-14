---
title: "Mobile Web Accessibility Patterns"
standard: "WCAG + EN 301 549"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["mobile", "touch", "responsive", "viewport", "gestures", "screen-readers"]
ai_context: "Patterns for accessible mobile web experiences. Load when advising on touch targets, gestures, orientation, zoom, mobile SR behavior, or responsive interaction."
---

# Mobile Web Accessibility Patterns

Mobile accessibility is not a separate WCAG mode. The same success criteria apply, but mobile use amplifies issues around touch targets, gestures, zoom, screen size, virtual keyboards, and screen reader navigation.

---

## Mobile-Specific Risk Areas

| Area | Common Risk | Relevant SCs |
|------|-------------|--------------|
| Small screens | content requires horizontal scrolling | `1.4.10` |
| Touch targets | controls too small or too close | `2.5.8` |
| Gestures | drag, pinch, or path gestures required | `2.5.1`, `2.5.7` |
| Orientation lock | landscape or portrait blocked without need | `1.3.4` |
| Zoom disabled | user cannot magnify content | `1.4.4`, `1.4.10` |
| Sticky UI | fixed headers or bottom bars obscure focus | `2.4.11`, `2.4.12` |
| Virtual keyboard | focus and layout break when keyboard opens | `1.4.10`, `2.4.3` |

---

## Core Patterns

### Allow Rotation Unless Essential

- Do not force portrait-only or landscape-only layouts unless the interaction genuinely requires it.
- Ensure both orientations retain core content and controls.

### Support Zoom and Reflow

- Never disable pinch zoom with `user-scalable=no`.
- Test at 320 CSS px width and high text zoom.
- Avoid fixed-width containers that force two-dimensional scrolling.

### Use Generous Targets

- Prefer at least 44px tap areas even though WCAG AA minimum is 24px with spacing exceptions.
- Add padding around icon-only controls.
- Ensure adjacent targets do not create accidental activation.

### Provide Gesture Alternatives

- If a carousel supports swipe, it also needs buttons.
- If an interface uses drag-and-drop, add move buttons or menus.
- Do not require complex multipoint gestures for core tasks.

### Respect the Virtual Keyboard

- Keep labels visible when the keyboard opens.
- Scroll focused fields into view.
- Avoid overlays or fixed buttons covering the active input.

### Keep Focus and Announcements Stable

- After client-side navigation, move focus to the new page heading or landmark.
- Announce important updates with live regions where needed.
- Ensure mobile screen readers can reach menus, dialogs, and disclosures in a predictable order.

---

## Mobile Screen Reader Considerations

- VoiceOver and TalkBack often expose headings, links, form controls, and landmarks differently than desktop SRs.
- Native HTML usually performs better than custom widgets.
- The visible label should match the accessible name because touch exploration and speech control rely on consistency.

---

## Testing Checklist

- [ ] Works at 320 CSS px width without content loss
- [ ] Orientation can change unless essential
- [ ] Zoom is not disabled
- [ ] Targets are large enough and not crowded
- [ ] Swipe/drag interactions have button or tap alternatives
- [ ] Focused fields remain visible when the virtual keyboard opens
- [ ] Sticky UI does not hide focused controls
- [ ] Tested with VoiceOver iOS and/or TalkBack Android for core flows

---

## Recommended Pairings

- `domains/web/focus-management.md`
- `domains/web/keyboard-navigation-patterns.md`
- `domains/web/spa-accessibility.md`
- `screen-readers/talkback-guide.md`
- `screen-readers/voiceover-guide.md`
