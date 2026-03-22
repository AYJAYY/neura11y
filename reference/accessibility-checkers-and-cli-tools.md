---
title: "Accessibility Checkers and CLI Tools"
standard: "WCAG + Tooling"
source_url: "https://www.w3.org/WAI/test-evaluate/tools/list/"
domain: ["web", "documents", "general"]
last_fetched: "2026-03-21"
last_reviewed: "2026-03-21"
status: "curated"
tags: ["tools", "testing", "checkers", "cli", "ci", "axe", "lighthouse", "pa11y", "html-validate", "linkinator"]
ai_context: "AI-first routing guide for accessibility checkers, browser extensions, linters, and command-line tools. Load when asked what tooling to use or how to automate accessibility checks."
---

# Accessibility Checkers and CLI Tools

---

## Load This File When

- The task asks which accessibility tool to use
- The task asks for command-line tooling or CI automation
- The task asks for a browser checker versus a linter versus a rendered-page scanner
- The task asks for a minimal accessibility testing stack

---

## Routing Rules

| Task | Prefer | Add | Do Not Rely On Alone |
|------|--------|-----|----------------------|
| Quick scan of a live page in browser | axe DevTools, WAVE, Accessibility Insights for Web, Lighthouse in DevTools | Manual keyboard and screen reader testing | Any single browser extension |
| Batch URL checks in CI | `pa11y`, `pa11y-ci`, Lighthouse CLI | Manual testing checklist, SR test matrix | Lighthouse score by itself |
| Component or app E2E testing | `@axe-core/playwright`, `cypress-axe` | Manual focus and announcement checks | Static linters alone |
| React or JSX source linting | `eslint-plugin-jsx-a11y` | Rendered DOM scan with axe | AST linting alone |
| Static HTML or template linting | `html-validate` | Rendered browser scan | Markup validation alone |
| Broken links in docs, HTML, or generated sites | `linkinator` | Accessibility scanner for rendered UI | Link checks as an accessibility audit |
| Manual guided review for WCAG 2.1 AA | Accessibility Insights Assessment, W3C Easy Checks | Automated scanner + SR testing | Automated checks alone |

---

## Human-in-the-Loop Checkers

| Tool | Interface | Best For | Key Limitation | Official URL |
|------|-----------|----------|----------------|--------------|
| W3C Easy Checks | WAI resource | First-pass manual review of titles, headings, alt text, contrast, zoom, and keyboard behavior | Guidance resource, not an automated scanner | https://www.w3.org/WAI/test-evaluate/preliminary/ |
| axe DevTools Extension | Browser extension | Fast page or component scan in Chrome, Edge, or Firefox DevTools | Still needs manual review for focus logic, alt text quality, and screen reader behavior | https://docs.deque.com/devtools-for-web/4/en/extensions-home |
| WAVE | Web app plus browser extensions | Visual overlay of issues directly on rendered pages | Better for surfacing patterns than for CI-scale automation unless you license the API | https://wave.webaim.org/index |
| Accessibility Insights for Web | Browser extension | Guided FastPass and assisted/manual WCAG assessment workflow | Browser-focused workflow, not a replacement for SR testing | https://accessibilityinsights.io/docs/web/overview/ |
| Lighthouse in Chrome DevTools | Built-in browser tooling | Lightweight accessibility audit during local development | Score can hide the distribution and severity of issues | https://developer.chrome.com/docs/lighthouse/accessibility |

---

## CLI and CI Tools

| Tool | Install / Entry Point | Primary Command Pattern | Best For | Key Limitation | Official URL |
|------|------------------------|-------------------------|----------|----------------|--------------|
| Lighthouse CLI | `npx lighthouse` | `npx lighthouse <url> --only-categories=accessibility --output=json` | CI audit for full rendered pages and regression tracking | Accessibility score is not a conformance result | https://developer.chrome.com/docs/lighthouse/accessibility |
| Pa11y | `npx pa11y` | `npx pa11y <url> --standard WCAG2AA` | One-off rendered-page CLI checks | Single-page checks only unless wrapped by another runner | https://pa11y.org/ |
| pa11y-ci | `npx pa11y-ci` | `npx pa11y-ci --config .pa11yci` | Multi-URL CI runs and sitemap-style checks | Needs browser/runtime setup and still covers only a subset of issues | https://github.com/pa11y/pa11y-ci |
| html-validate | `npx html-validate` | `npx html-validate \"src/**/*.html\"` | Offline HTML and template validation before render | Does not evaluate runtime state, focus behavior, or AT output | https://html-validate.org/usage/cli.html |
| linkinator | `npx linkinator` | `npx linkinator \"**/*.md\" --markdown` | Broken-link checks across docs and static sites | Checks link health, not accessibility semantics | https://github.com/JustinBeckwith/linkinator |
| webhint | `npx hint` | `npx hint <url>` or `npx hint .` | Combined web quality checks with accessibility hints | Broader web-quality scope means accessibility depth is limited compared with axe-focused tools | https://webhint.io/docs/user-guide/concepts/hints/ |

---

## Source-Level and Framework Tooling

| Tool | Layer | Typical Command Pattern | Best For | Key Limitation | Official URL |
|------|-------|-------------------------|----------|----------------|--------------|
| `eslint-plugin-jsx-a11y` | JSX / React AST linting | `npx eslint .` with `jsx-a11y` rules enabled | Catching common semantic and labeling errors before render | Static AST analysis cannot verify runtime DOM, focus movement, or computed names in all cases | https://github.com/jsx-eslint/eslint-plugin-jsx-a11y |
| `@axe-core/playwright` | Rendered DOM in E2E tests | Run through Playwright test suite | Route, modal, and workflow checks in app context | Needs a working test harness and manual follow-up for SR behavior | https://github.com/dequelabs/axe-core-npm |
| `jest-axe` | Component test layer | Run through Jest or Vitest test suite | Fast component-level checks in CI | JSDOM does not model the full browser and cannot reliably test everything, especially color contrast | https://github.com/NickColley/jest-axe |
| `cypress-axe` | Rendered DOM in Cypress | Run through Cypress test suite | App workflows when Cypress is already the team standard | Still requires manual accessibility review beyond DOM violations | https://github.com/component-driven/cypress-axe |

---

## Minimal Stacks

| Situation | Minimal Stack |
|-----------|---------------|
| Static marketing site | `html-validate` + Lighthouse CLI + manual keyboard test + one screen reader pass |
| React or component-library app | `eslint-plugin-jsx-a11y` + `jest-axe` + `@axe-core/playwright` + manual focus and SR testing |
| Docs or markdown-heavy repo | `linkinator` + `html-validate` for generated HTML + manual heading/link review |
| Enterprise web app | `@axe-core/playwright` or Cypress + axe + `pa11y-ci` on critical routes + manual SR matrix |
| Quick triage by a human tester | Accessibility Insights FastPass or axe DevTools + WAVE + manual keyboard check |

---

## Command Patterns to Prefer

```bash
# Rendered-page audit
npx lighthouse http://localhost:3000 --only-categories=accessibility --output=json

# Single URL WCAG AA scan
npx pa11y http://localhost:3000 --standard WCAG2AA

# Multiple URLs in CI
npx pa11y-ci --config .pa11yci

# Static HTML validation
npx html-validate "src/**/*.html"

# JSX accessibility linting
npx eslint .

# Markdown or site link health
npx linkinator "**/*.md" --markdown
```

---

## Limits of Automated Tooling

- No checker certifies WCAG conformance by itself
- Automated tools do not reliably judge alt text quality, reading order logic, or task clarity
- CLI output does not replace keyboard testing, zoom/reflow checks, or screen reader testing
- A Lighthouse accessibility score should be treated as one signal, not a release gate by itself
- Source linters catch authoring mistakes earlier, but rendered-page scanners are still required

---

## Internal Cross-References

- `domains/web/testing/automated-testing.md`
- `domains/web/testing/manual-testing-checklist.md`
- `domains/web/testing/screen-reader-testing-matrix.md`
- `reference/accessibility-tools.md`
