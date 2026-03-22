---
title: "Accessibility Testing Tools Reference"
standard: "WCAG + Tooling"
source_url: "https://www.w3.org/WAI/test-evaluate/tools/list/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-21"
last_reviewed: "2026-03-21"
status: "curated"
tags: ["tools", "testing", "axe", "lighthouse", "wave", "screen-readers", "color-contrast", "cli", "checkers"]
ai_context: "Broad catalog of accessibility testing tools by category. For AI-first checker and CLI routing, prefer reference/accessibility-checkers-and-cli-tools.md."
---

# Accessibility Testing Tools Reference

---

For AI-first tool selection and command routing, load `reference/accessibility-checkers-and-cli-tools.md` first. This file remains the broader catalog by category.

---

## Automated Web Testing

| Tool | Type | Cost | Notes |
|------|------|------|-------|
| axe DevTools (browser extension) | Browser extension | Free (basic) | Deque; most widely used; good rule coverage |
| WAVE | Browser extension + web | Free | Visual overlay of errors; easy to understand |
| Lighthouse | Chrome DevTools + CLI | Free | Built into Chrome; includes accessibility score |
| Axe-core (npm) | Library | Free | Integration into jest, Playwright, Cypress |
| IBM Equal Access Checker | Browser extension | Free | IBM; includes AAA rules |
| Deque axe DevTools Pro | Browser extension | Paid | Guided testing + intelligent guided tests |
| Siteimprove Accessibility | Browser extension + SaaS | Paid | Enterprise scanning |
| Tenon.io | API + SaaS | Paid | API-first accessibility testing |
| Pa11y | CLI + Node.js | Free | Good for CI batch URL testing |

---

## Color and Contrast

| Tool | Platform | Cost | Notes |
|------|----------|------|-------|
| WebAIM Contrast Checker | Web | Free | Industry standard; simple input |
| Colour Contrast Analyser | Windows/macOS app | Free | TPGi; eyedropper to pick colors from screen |
| Stark (Figma plugin) | Figma | Free (limited) | Color blind simulation + contrast check |
| Contrast (Figma plugin) | Figma | Free | WCAG AA/AAA checker for designs |
| APCA contrast checker | Web | Free | For WCAG 3.0 / APCA evaluation |
| Who Can Use | Web | Free | Shows how many people can read your color pair |

---

## Screen Readers

| Screen Reader | Platform | Cost | Browser |
|---|---|---|---|
| NVDA | Windows | Free | Chrome (recommended), Firefox |
| JAWS | Windows | Paid (free trial) | Chrome (recommended), Edge |
| VoiceOver | macOS, iOS | Free (built-in) | Safari |
| TalkBack | Android | Free (built-in) | Chrome |
| Narrator | Windows | Free (built-in) | Edge |
| Orca | Linux | Free | Firefox, Chromium |

---

## Document Accessibility

| Tool | Document Type | Cost | Notes |
|------|--------------|------|-------|
| Microsoft Accessibility Checker | Word, Excel, PowerPoint | Free (built-in) | Review tab → Check Accessibility |
| Adobe Acrobat Accessibility Checker | PDF | Acrobat Pro | Tools → Accessibility → Full Check |
| PAC 3 (PDF Accessibility Checker) | PDF | Free | Windows; validates against Matterhorn Protocol |
| CommonLook PDF Validator | PDF | Paid | Most thorough PDF/UA validation |
| PAVE (web-based) | PDF | Free | Upload and auto-tag PDFs |
| Tingtun Checker | PDF | Free | Web-based; validates PDF/UA |
| Grackle Docs | Google Docs/Slides/Sheets | Paid | Chrome extension; checks and fixes Google docs |
| axesWord | Word | Paid | Deep Word accessibility remediation |

---

## Browser Extensions for Manual Testing

| Extension | Purpose | Browser |
|-----------|---------|---------|
| axe DevTools | Automated rule checking | Chrome, Firefox, Edge |
| WAVE | Visual overlay + screen reader simulation | Chrome, Firefox |
| Accessibility Insights for Web | Microsoft; tab stops + automated | Chrome, Edge |
| NoCoffee | Vision simulator (color blindness, low vision) | Chrome |
| Funkify | Disability simulator (vision, motor, cognitive) | Chrome |
| Headings Map | Visual heading hierarchy | Chrome, Firefox |
| ANDI | Section 508; used by US government | Chrome |
| Landmarks extension | Visualize ARIA landmarks | Chrome, Firefox |

---

## Color Blindness Simulation

| Tool | Platform | Cost |
|------|----------|------|
| Chrome DevTools → Rendering → Emulate vision deficiencies | Chrome | Free (built-in) |
| NoCoffee extension | Chrome | Free |
| Coblis (Color Blindness Simulator) | Web | Free |
| Colour Contrast Analyser | Windows/macOS | Free |
| Stark plugin | Figma, Sketch | Free (limited) |

---

## Readability and Plain Language

| Tool | Purpose | Cost |
|------|---------|------|
| Hemingway App (hemingwayapp.com) | Readability grade level | Free (web) |
| Readable.io | Flesch-Kincaid + other scores | Paid |
| WebFX Readability Test | Multiple readability formulas | Free |
| Microsoft Word readability stats | Flesch-Kincaid built in | Free (Word) |
| Grammarly | Grammar + clarity | Free/Paid |

---

## Design Tool Plugins

| Tool | Application | Checks |
|------|-------------|--------|
| Stark | Figma, Sketch, XD, IntelliJ | Contrast, color blindness, alt text, focus order |
| Able — Friction Free Accessibility | Figma | Contrast, APCA |
| A11y Annotation Kit | Figma | Annotation templates for developers |
| Accessibility Checker | Figma | Various checks |
| Color Contrast | Figma Community | Quick contrast ratios |

---

## Screen Reader Testing Virtualisation / Services

| Service | Use | Cost |
|---------|-----|------|
| BrowserStack Accessibility Testing | Remote screen reader testing | Paid |
| Assistiv Labs | Cloud-based AT testing | Paid |
| WebAIM Screen Reader Survey | Research data on SR usage | Free |

---

## Mobile Testing

| Tool | Platform | Notes |
|------|----------|-------|
| Accessibility Scanner | Android | Google; surface-level checks |
| A11yUITests (iOS library) | iOS | Unit testing for iOS accessibility |
| VoiceOver (iOS) | iOS (built-in) | Gesture-based; standard test required |
| TalkBack (Android) | Android (built-in) | Gesture-based; standard test required |
| Accessibility Insights for Android | Android | Tab stops and accessibility checks |
| Espresso + Android Accessibility | Android | Automated testing framework |
| XCTest + iOS Accessibility | iOS | Automated testing framework |

---

## Link Validation (Related to Link Accessibility)

| Tool | Notes |
|------|-------|
| W3C Link Checker | Free; checks all links on a page |
| Screaming Frog | Paid; crawl entire site for broken links |
| broken-link-checker (npm) | Free CLI tool |

---

## Linters for Development

| Tool | Purpose | Language/Framework |
|------|---------|-------------------|
| eslint-plugin-jsx-a11y | Lints React/JSX for accessibility | JavaScript/React |
| eslint-plugin-vuejs-accessibility | Vue.js accessibility lint rules | Vue |
| svelte-check | Includes some a11y rules | Svelte |
| angular-eslint/template-accessibility | Angular template rules | Angular |
| html-validate | Full HTML validation with a11y rules | HTML |
| Webhint | Browser DevTools + CLI accessibility hints | HTML/CSS/JS |
