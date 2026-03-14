---
title: "Single-Page Application (SPA) Accessibility"
standard: "WCAG 2.2 + WAI-ARIA"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["spa", "react", "angular", "vue", "routing", "live-regions", "focus-management", "history-api"]
ai_context: "Accessibility patterns for single-page applications. Covers route changes, live regions, focus management, and framework-specific patterns. Load when generating SPA code."
---

# Single-Page Application (SPA) Accessibility

SPAs create accessibility challenges because browser behaviors that happen automatically on full page loads — focus reset, page title update, reading new content — must be implemented manually.

---

## Page/Route Change Management

### The Problem

When a SPA navigates to a new route:
1. The URL changes (History API)
2. Content updates in the DOM
3. **BUT:** Focus stays on the element that triggered the navigation
4. **AND:** Screen readers don't know a "page change" happened

### The Solution: Focus Management on Route Change

After a route change, move focus to:
- The `<main>` element (if it has `tabindex="-1"`)
- The new page `<h1>`
- A skip-to-content link at the top

```javascript
// React — using useEffect after route change
import { useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';

function App() {
  const location = useLocation();
  const mainRef = useRef(null);

  useEffect(() => {
    // Update document title first
    // Then move focus after DOM update
    setTimeout(() => {
      if (mainRef.current) {
        mainRef.current.focus();
      }
    }, 0);
  }, [location.pathname]);

  return (
    <main ref={mainRef} tabIndex={-1} id="main-content">
      {/* page content */}
    </main>
  );
}
```

```javascript
// Angular — using Router events
import { Router, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({ selector: 'app-root', template: '<main #mainContent tabindex="-1"><router-outlet></router-outlet></main>' })
export class AppComponent implements OnInit {
  @ViewChild('mainContent') mainContent: ElementRef;

  constructor(private router: Router) {}

  ngOnInit() {
    this.router.events
      .pipe(filter(event => event instanceof NavigationEnd))
      .subscribe(() => {
        setTimeout(() => this.mainContent.nativeElement.focus(), 0);
      });
  }
}
```

### Document Title Updates

Update `document.title` on every route change. The title is the first thing screen readers announce.

```javascript
// React Router — in each page component
useEffect(() => {
  document.title = 'Products — Acme Shop'; // Page name first, site name last
}, []);

// Or with react-helmet
import { Helmet } from 'react-helmet';
<Helmet><title>Products — Acme Shop</title></Helmet>
```

**Title format:** `[Page name] — [Site name]` (page first, so the unique part is read first).

---

## Live Regions

Live regions announce dynamic content changes to screen readers without moving focus.

### aria-live Values

| Value | When to use | Behavior |
|-------|-------------|----------|
| `aria-live="polite"` | Most dynamic updates | Announces after user stops interacting |
| `aria-live="assertive"` | Urgent errors, alerts | Interrupts current speech immediately |
| `aria-live="off"` | Updates that shouldn't be announced | No announcement |

### Route Announcer Pattern

Many SPA frameworks include a route announcer that announces the page title when navigating.

```html
<!-- Visually hidden live region; placed early in DOM -->
<div
  id="route-announcer"
  role="status"
  aria-live="polite"
  aria-atomic="true"
  class="sr-only"
></div>
```

```javascript
// Update on route change
function announceRouteChange(pageName) {
  const announcer = document.getElementById('route-announcer');
  announcer.textContent = ''; // Clear first
  // Must be in separate tick to re-trigger announcement
  setTimeout(() => {
    announcer.textContent = `Navigated to ${pageName}`;
  }, 100);
}
```

### Status Messages (SC 4.1.3 — Level AA)

Status messages that appear without receiving focus must be announced to screen readers. Use `role="status"` or `role="alert"`.

```html
<!-- Success message after form submit -->
<div role="status" aria-live="polite" aria-atomic="true">
  <!-- Inject message text dynamically -->
</div>

<!-- Error alert (interrupts) -->
<div role="alert" aria-live="assertive" aria-atomic="true">
  <!-- Inject error text dynamically -->
</div>
```

**Important:** The live region container must exist in the DOM before content is injected. Don't create and inject simultaneously.

```javascript
// WRONG: Create and populate at same time — may not announce
const el = document.createElement('div');
el.setAttribute('role', 'status');
el.textContent = 'Item saved';
document.body.appendChild(el);

// CORRECT: Container exists; inject content
const statusEl = document.getElementById('status-region');
statusEl.textContent = ''; // Clear
setTimeout(() => { statusEl.textContent = 'Item saved'; }, 50);
```

### Common Live Region Use Cases

```html
<!-- Search results count -->
<div role="status" aria-live="polite" aria-atomic="true" id="results-count">
  <!-- "14 results found for 'keyboard'" -->
</div>

<!-- Loading state -->
<div role="status" aria-live="polite" aria-atomic="true" id="loading-status">
  <!-- "Loading..." → "" (clear when done) → "Content loaded" -->
</div>

<!-- Form validation -->
<div role="alert" aria-live="assertive" id="form-errors">
  <!-- "3 errors found. Please correct before submitting." -->
</div>

<!-- Shopping cart count -->
<div role="status" aria-live="polite" aria-atomic="false" id="cart-count">
  <!-- Updates individually without interrupting -->
</div>
```

---

## Modal and Dialog Focus Management

See `domains/web/component-patterns/modal-dialog.md` for complete implementation.

Key rules for SPAs:
1. When a modal opens: move focus to the first focusable element inside, or to the modal container
2. Trap focus inside the modal while open
3. When a modal closes: return focus to the element that opened it

```javascript
class FocusTrap {
  constructor(container) {
    this.container = container;
    this.focusableSelector = 'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex="0"]';
    this.handleKeydown = this.handleKeydown.bind(this);
  }

  activate() {
    this.triggerElement = document.activeElement; // Save for restoration
    const focusable = this.container.querySelectorAll(this.focusableSelector);
    if (focusable.length) focusable[0].focus();
    this.container.addEventListener('keydown', this.handleKeydown);
  }

  deactivate() {
    this.container.removeEventListener('keydown', this.handleKeydown);
    if (this.triggerElement) this.triggerElement.focus(); // Restore focus
  }

  handleKeydown(e) {
    if (e.key !== 'Tab') return;
    const focusable = [...this.container.querySelectorAll(this.focusableSelector)];
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
}
```

---

## Dynamic Content: Loading States

```jsx
// React: accessible loading state
function DataList({ isLoading, items }) {
  return (
    <section aria-label="Search results" aria-busy={isLoading}>
      {isLoading ? (
        <p role="status">Loading results...</p>
      ) : (
        <>
          <p role="status">{items.length} results found</p>
          <ul>
            {items.map(item => <li key={item.id}>{item.name}</li>)}
          </ul>
        </>
      )}
    </section>
  );
}
```

**`aria-busy="true"`** on the container tells screen readers the region is being updated; don't read it yet.

---

## Infinite Scroll and Pagination

Infinite scroll is problematic for keyboard and screen reader users. Prefer pagination or a "Load more" button.

```html
<!-- Preferred: Load more button -->
<ul id="results-list" aria-label="Articles">
  <!-- items -->
</ul>
<button id="load-more" aria-controls="results-list">
  Load more articles (showing 10 of 47)
</button>
```

```javascript
// After loading more: move focus to first new item
document.getElementById('load-more').addEventListener('click', () => {
  const previousCount = items.length;
  loadMoreItems().then(() => {
    const allItems = document.querySelectorAll('#results-list li');
    allItems[previousCount].focus(); // Focus first new item
    // Update button text
    document.getElementById('load-more').textContent =
      `Load more articles (showing ${allItems.length} of ${total})`;
  });
});
```

---

## Forms in SPAs

### Inline Validation

```javascript
// Validate on blur, not on every keystroke
input.addEventListener('blur', () => {
  if (!isValid(input.value)) {
    input.setAttribute('aria-invalid', 'true');
    errorEl.textContent = 'Please enter a valid email address.';
    input.setAttribute('aria-describedby', 'email-error');
  } else {
    input.removeAttribute('aria-invalid');
    errorEl.textContent = '';
  }
});
```

### Server-Side Errors

When a form submits and the server returns errors:

```javascript
// 1. Announce the error count
statusRegion.textContent = `${errors.length} errors found. Please correct before submitting.`;

// 2. Move focus to the error summary or first invalid field
document.getElementById('error-summary').focus();
// or: document.querySelector('[aria-invalid="true"]').focus();

// 3. Link each error to its field
// <a href="#email-input">Email: invalid format</a>
```

---

## React-Specific Patterns

### Refs for Focus Management

```jsx
import { useRef, useEffect } from 'react';

function Notification({ message, onDismiss }) {
  const dismissRef = useRef(null);

  useEffect(() => {
    // Move focus to dismiss button when notification appears
    dismissRef.current?.focus();
  }, []);

  return (
    <div role="alert">
      <p>{message}</p>
      <button ref={dismissRef} onClick={onDismiss}>Dismiss</button>
    </div>
  );
}
```

### aria-live in React

```jsx
function LiveRegion({ message }) {
  const [announced, setAnnounced] = useState('');

  useEffect(() => {
    setAnnounced(''); // Clear
    const timer = setTimeout(() => setAnnounced(message), 100);
    return () => clearTimeout(timer);
  }, [message]);

  return (
    <div role="status" aria-live="polite" aria-atomic="true" className="sr-only">
      {announced}
    </div>
  );
}
```

---

## Visually Hidden Class

Used throughout SPA patterns to show text only to screen readers.

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Allow element to become visible when focused (skip links) */
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
```

---

## Common SPA Accessibility Failures

| Failure | Symptom | Fix |
|---------|---------|-----|
| No route announcer | Screen reader users don't know page changed | Add live region route announcer |
| Focus stays on nav link after route change | User must re-navigate from old position | Focus `<main>` or `<h1>` on route change |
| Title not updated | All pages have same title | Update `document.title` in route handler |
| Modals don't trap focus | Focus escapes modal | Implement focus trap |
| Focus lost after modal closes | User is disoriented | Return focus to trigger element |
| Status messages not in live region | Form submissions give no feedback | Use `role="status"` for success messages |
| Errors not announced | Validation fails silently | Use `role="alert"` + `aria-describedby` |
| `aria-hidden` on active content | Content invisible to AT | Only aria-hidden inactive/offscreen content |
