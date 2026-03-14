---
title: "Kiosk and Embedded Systems Accessibility Playbook"
standard: "EN 301 549 + Section 508 + ISO 9241-171"
source_url: "https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf"
domain: ["general"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["kiosk", "embedded", "physical-ict", "closed-functionality", "self-service", "playbook"]
ai_context: "Implementation playbook for accessible kiosks and embedded touch systems. Load when advising on self-service terminals, closed functionality, speech output, controls, timing, and recovery."
---

# Kiosk and Embedded Systems Accessibility Playbook

---

## Scope

This playbook covers:

- Self-service kiosks
- Check-in terminals
- Ticketing and ordering machines
- Embedded touch interfaces with limited or closed functionality

It focuses on practical implementation, not detailed hardware measurements. Verify local legal reach-range and operable-part requirements separately.

---

## Core Accessibility Risks

Kiosks fail when they assume all users can:

- Stand directly in front of the screen
- Use touch accurately
- Hear audio prompts in a noisy space
- Read small text quickly
- Complete a transaction before a short timeout expires

Closed-functionality products need built-in accessibility because users may not be able to bring their own assistive technology into the interaction.

---

## High-Value Requirements Mapping

| Need | Relevant Reference |
|------|--------------------|
| Closed functionality support | EN 301 549 Chapter 5 |
| Hardware controls and tactile operation | EN 301 549 Chapter 8 |
| Software interaction and UI access | EN 301 549 Chapter 11 |
| Clear software accessibility principles | ISO 9241-171 overview |

---

## Minimum Interaction Patterns

Every kiosk or embedded system should have:

- A clearly discoverable start point
- Speech output or equivalent non-visual guidance when the interface is otherwise visual
- A way to use headphones or private audio when sensitive information is involved
- Keyboard, tactile, or alternative input when fine touch is not enough
- A consistent `Back`, `Help`, `Repeat`, and `Start over` pattern
- Sufficient time or time extension for each transaction step

---

## Start Screen Pattern

### Better Pattern

- High-contrast welcome screen
- Obvious primary action such as `Start`
- Persistent accessibility entry point such as `Accessibility options`
- Visual and audio instruction for how to begin

### Failure Pattern

- Auto-rotating attract screen with no pause
- Accessibility features hidden behind several steps
- Instructions only visible at the top of the screen

Accessibility options should be available at the start, not only after a failure.

---

## Non-Visual Access Pattern

For touch-first kiosks, provide a predictable way to activate speech or non-visual mode.

### Better Pattern

- Dedicated tactile button or clearly labeled hardware control
- Spoken orientation when mode starts
- Audio prompts that name the current screen and available actions
- Repeat prompt available at every step

### Example Spoken Orientation

`Welcome. Headphones connected. To begin, press the lower right button or say Start.`

Avoid forcing users to explore an unlabeled glass screen to discover where audio mode lives.

---

## Transaction Flow Pattern

Keep each step narrow and recoverable.

### Better Flow

1. Choose task
2. Confirm selection
3. Enter required information
4. Review summary
5. Confirm or cancel

### Required Controls

- `Back`
- `Repeat`
- `Help`
- `Cancel`
- `Start over`

Destructive actions such as payment submission or ticket purchase need a clear review step.

---

## Timing and Session Management

Public machines often expire sessions too quickly.

### Better Pattern

- Warn before timeout
- Allow extension
- Preserve already-entered information when reasonable
- Explain exactly what will happen if time expires

### Example

`Your session will expire in 30 seconds. Select More time to continue.`

Do not reset the entire task without warning.

---

## Input and Hardware Considerations

### Better Pattern

- Large touch targets
- Clear spacing between actions
- Tactilely distinguishable physical controls when present
- Volume adjustment that is reachable during the task
- Peripheral hardware such as card readers, printers, and scanners placed consistently

### Common Failure

- Touch targets clustered at screen edges
- Audio jack hard to locate
- Card reader positioned separately with no orientation cues

---

## Embedded System Notes

For appliances, panels, or other embedded interfaces:

- Keep navigation shallow
- Avoid icon-only controls without text or programmatic names
- Persist settings and state feedback clearly
- Provide equivalent access when companion apps or remote controls are required

If a companion app is necessary for accessibility, the base product still needs a usable path for critical functions such as setup, power, safety, and reset.

---

## Manual Test Checklist

1. Start the task without using vision
2. Complete the task using only one hand and imprecise touch
3. Trigger timeout warnings and verify recovery
4. Use headphones and confirm private audio mode
5. Intentionally make input errors and verify correction paths
6. Confirm payment, print, and completion steps are announced clearly

---

## Quick Checklist

- [ ] Accessibility options are available from the start screen
- [ ] Non-visual guidance exists for closed functionality
- [ ] Headphone or private audio support is available when needed
- [ ] Navigation includes Back, Help, Repeat, and Start over
- [ ] Timeouts warn and allow extension
- [ ] Critical actions include review and confirmation
- [ ] Peripheral devices are placed and labeled consistently
