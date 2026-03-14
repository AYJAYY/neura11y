---
title: "Automated Accessibility Testing"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/test-evaluate/tools/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["testing", "automated", "axe", "lighthouse", "wave", "ci", "jest", "playwright"]
ai_context: "Automated accessibility testing tools and integration patterns. Load when writing test code or CI/CD pipeline instructions for accessibility."
---

# Automated Accessibility Testing

Automated tools detect approximately 30–40% of WCAG 2.2 Level AA failures. They are a filter, not a certification. Always supplement with manual and screen reader testing.

---

## Tool Comparison

| Tool | Use Case | Free? | API/CI? |
|------|----------|-------|---------|
| axe-core | Integration into test frameworks | Yes (core) | Yes |
| Lighthouse | Browser DevTools + CI | Yes | Yes (CLI) |
| WAVE | Visual browser inspection | Yes (extension) | Paid API |
| Deque axe DevTools | In-browser + guided | Paid | Yes |
| Pa11y | CLI for batch URL testing | Yes | Yes |
| Playwright + axe | E2E test integration | Yes | Yes |
| Jest + jest-axe | Unit/component testing | Yes | Yes |

---

## axe-core

Axe is the most widely integrated accessibility testing engine. It runs as:
- Browser extension (axe DevTools)
- NPM package (`axe-core`)
- Integrated into test frameworks via `@axe-core/playwright`, `jest-axe`, `cypress-axe`

### Axe Rules (What it checks)

Axe classifies rules by WCAG SC and impact level (critical, serious, moderate, minor).

Key rules:
- `color-contrast` — SC 1.4.3
- `image-alt` — SC 1.1.1
- `label` — SC 1.3.1 / 4.1.2
- `button-name` — SC 4.1.2
- `link-name` — SC 2.4.4
- `heading-order` — best practice
- `landmark-one-main` — best practice
- `aria-required-children` — SC 1.3.1
- `frame-title` — SC 4.1.2
- `html-has-lang` — SC 3.1.1

---

## Jest + jest-axe (Component Testing)

```bash
npm install --save-dev jest-axe
```

```javascript
// Example: React component test
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

test('Button has no accessibility violations', async () => {
  const { container } = render(<Button>Submit</Button>);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});

// Test with specific axe configuration
test('Form has no violations', async () => {
  const { container } = render(<ContactForm />);
  const results = await axe(container, {
    rules: {
      'color-contrast': { enabled: false } // disable if not testing contrast in jsdom
    }
  });
  expect(results).toHaveNoViolations();
});
```

---

## Playwright + axe (End-to-End Testing)

```bash
npm install --save-dev @axe-core/playwright
```

```javascript
// playwright.config.js — standard setup

// test file
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('Homepage has no WCAG 2.2 AA violations', async ({ page }) => {
  await page.goto('http://localhost:3000');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])
    .analyze();

  expect(results.violations).toEqual([]);
});

// Test specific component in context
test('Modal dialog is accessible', async ({ page }) => {
  await page.goto('http://localhost:3000/dashboard');
  await page.click('#open-modal-button');

  const results = await new AxeBuilder({ page })
    .include('#modal-dialog')
    .analyze();

  expect(results.violations).toEqual([]);
});

// Exclude known violations (document and track resolution)
test('Page minus known issues', async ({ page }) => {
  await page.goto('/checkout');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .exclude('#legacy-widget') // Document why this is excluded
    .analyze();
  expect(results.violations).toEqual([]);
});
```

---

## Cypress + cypress-axe

```bash
npm install --save-dev cypress-axe
```

```javascript
// cypress/support/commands.js
import 'cypress-axe';

// test file
describe('Homepage', () => {
  it('has no accessibility violations', () => {
    cy.visit('/');
    cy.injectAxe();
    cy.checkA11y(null, {
      runOnly: {
        type: 'tag',
        values: ['wcag2a', 'wcag2aa', 'wcag22aa']
      }
    });
  });

  it('modal is accessible when open', () => {
    cy.visit('/products');
    cy.injectAxe();
    cy.get('#view-details-btn').click();
    cy.checkA11y('#product-modal');
  });
});
```

---

## Pa11y (CLI / CI Batch Testing)

Pa11y is useful for testing many URLs in CI pipelines without a full test framework.

```bash
npm install -g pa11y
pa11y https://example.com
pa11y --standard WCAG2AA https://example.com/products
```

### pa11y-ci for Multiple URLs

```bash
npm install --save-dev pa11y-ci
```

```json
// .pa11yci
{
  "defaults": {
    "standard": "WCAG2AA",
    "timeout": 30000,
    "wait": 500
  },
  "urls": [
    "http://localhost:3000",
    "http://localhost:3000/about",
    "http://localhost:3000/contact",
    {
      "url": "http://localhost:3000/login",
      "actions": [
        "set field #username to testuser",
        "set field #password to testpass",
        "click element #login-btn",
        "wait for url to be http://localhost:3000/dashboard"
      ]
    }
  ]
}
```

```bash
pa11y-ci
```

---

## Lighthouse CLI (CI Integration)

```bash
npm install -g lighthouse
lighthouse https://example.com --only-categories=accessibility --output=json --output-path=./a11y-report.json
```

```yaml
# GitHub Actions example
- name: Run Lighthouse accessibility audit
  run: |
    npx lighthouse http://localhost:3000 \
      --only-categories=accessibility \
      --output=json \
      --output-path=./lighthouse-a11y.json \
      --chrome-flags="--headless"

- name: Check accessibility score
  run: |
    SCORE=$(cat lighthouse-a11y.json | jq '.categories.accessibility.score')
    echo "Accessibility score: $SCORE"
    if (( $(echo "$SCORE < 0.9" | bc -l) )); then
      echo "Accessibility score below 90"
      exit 1
    fi
```

---

## Axe Rule Tags

When calling axe, specify which standards to test against:

| Tag | Meaning |
|-----|---------|
| `wcag2a` | WCAG 2.x Level A |
| `wcag2aa` | WCAG 2.x Level AA |
| `wcag2aaa` | WCAG 2.x Level AAA |
| `wcag22aa` | WCAG 2.2 new Level AA criteria |
| `best-practice` | Highly recommended non-WCAG rules |
| `section508` | Section 508 requirements |

**Recommended tag set:** `['wcag2a', 'wcag2aa', 'wcag22aa', 'best-practice']`

---

## CI/CD Integration Strategy

### Stage 1: Build-time (jest-axe / vitest)
- Run on every component render test
- Fast; catches obvious issues immediately
- Fails the build early

### Stage 2: Integration (Playwright / Cypress)
- Run in PR check on critical paths: home, product pages, checkout, forms
- Use axe WCAG 2.2 AA tags
- Fail on new violations; track existing ones

### Stage 3: Scheduled full site scan (Pa11y-CI)
- Weekly scan of all URL patterns
- Report to accessibility backlog
- Compare to previous scan to track regressions

### Violation Triage Strategy

```javascript
// Don't silently ignore violations; log and track them
test('Page accessibility', async ({ page }) => {
  const results = await new AxeBuilder({ page }).analyze();

  // Categorize by impact
  const critical = results.violations.filter(v => v.impact === 'critical');
  const serious = results.violations.filter(v => v.impact === 'serious');

  // Fail on critical and serious
  expect(critical).toEqual([]);
  expect(serious).toEqual([]);

  // Log moderate/minor for tracking
  if (results.violations.length > 0) {
    console.warn('Moderate/minor violations:', results.violations.map(v => v.id));
  }
});
```

---

## What Automated Testing Cannot Check

These items require manual review:

- **Alt text quality** — Is the alt text meaningful and accurate? (Axe can only detect missing alt)
- **Focus order logic** — Does tab sequence match visual/logical reading order?
- **Screen reader announcements** — Is content correctly announced in context?
- **Color contrast in images** — Text overlaid on images
- **Cognitive accessibility** — Plain language, complexity, memory load
- **Timing** — Is 2 seconds enough to read content?
- **Session timeout** — Does the page warn before timeout?
- **Error message quality** — Are errors descriptive enough to fix?
- **Animation/motion** — Is motion avoidable by users?
