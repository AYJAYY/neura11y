---
title: "Accessible Email and Newsletter Guide"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["documents", "web"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["email", "newsletter", "html-email", "documents", "marketing"]
ai_context: "Guide for creating accessible marketing emails and newsletters across major email clients."
---

# Accessible Email and Newsletter Guide

## Scope

Use this guide for HTML email, newsletters, and campaign emails. Email clients have limited CSS and semantic support, so accessible authoring depends on conservative markup, clear copy, and strong fallback behavior.

## Structure and Reading Order

- Use one clear email title or opening heading
- Keep section headings short and descriptive
- Use a single-column layout where possible
- Make the visual order match the reading order in the HTML
- Do not rely on images to carry essential content

## Content Rules

- Subject line should describe the purpose of the email
- Preheader text should add useful context, not duplicate the subject line
- Link text must describe destination or action
- Lists should be real lists where client support allows; otherwise keep list copy simple and easy to parse
- Provide plain-language summaries before dense promotional or transactional details

## Images and Media

- Every meaningful image needs alt text
- Decorative spacer images should use empty alt text
- If the email uses a hero image with text embedded in it, repeat that text as real HTML
- Animated GIFs should expose the key message in the first frame

## Tables and Layout

- Use tables only for layout when client constraints require them
- Keep layout tables simple and avoid nested complexity where possible
- Mark data tables clearly and avoid merging cells when the content can be simplified

## Visual Design

- Body text should meet 4.5:1 contrast against the background
- Buttons and other controls should meet 3:1 non-text contrast
- Avoid text under 16px in marketing emails
- Do not communicate urgency, status, or discount information by color alone

## Interaction and Fallbacks

- Buttons should have clear action labels such as "View order status" or "Download report"
- Linked images should still make sense when images are blocked
- Do not require hover to reveal critical information
- If video is promoted, include a linked fallback image and transcript destination

## Client Testing

Test at minimum with:
- images blocked
- dark mode
- 200% zoom
- keyboard-only navigation in webmail clients
- a screen reader in a browser-based email client

Common problem areas:
- hidden preheader hacks
- image-only buttons
- low-contrast footer text
- side-by-side columns that collapse into confusing reading order on mobile
