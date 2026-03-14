---
title: "Accessible Design-to-Development Handoff"
standard: "WCAG + WAI-ARIA 1.2"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["design", "development", "handoff", "tokens", "components"]
ai_context: "Guide for preserving accessibility requirements from design artifacts into implemented interfaces."
---

# Accessible Design-to-Development Handoff

## What Designers Must Specify

- semantic intent for each component
- visible labels and any non-visible supporting text
- focus order and focus-return behavior
- keyboard interaction model
- error, success, loading, and disabled states
- contrast-approved color tokens

## What Developers Need in the Handoff

- component variants and state definitions
- minimum target sizes
- responsive behavior at mobile and zoomed layouts
- annotation for dialogs, menus, tooltips, and live updates
- writing guidance for alt text, helper text, and error copy

## Failure Patterns

- mockups show hover states but not focus states
- screen designs imply drag-only or swipe-only interactions
- contrast is approved on artboards but not against real component states
- copy decks omit accessible names for icon-only controls

## Handoff Deliverables

- design tokens with approved contrast pairings
- component behavior notes
- content requirements for names, descriptions, and status messages
- QA acceptance criteria mapped to WCAG checks
