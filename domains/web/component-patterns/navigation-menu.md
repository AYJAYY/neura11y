---
title: "Accessible Navigation Menu Patterns"
standard: "WAI-ARIA APG"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/menubar/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["navigation", "menu", "menubar", "dropdown", "aria", "component-pattern", "keyboard"]
ai_context: "Accessible navigation patterns including top nav, hamburger menu, and dropdown menus. Covers disclosure pattern vs. ARIA menu pattern. Load when building navigation components."
---

# Accessible Navigation Menu Patterns

There are two distinct patterns for navigation with dropdowns:

1. **Disclosure Navigation** — Uses `<nav>`, `<button>`, and `<ul>`. Simpler, preferred for most site navigation.
2. **ARIA Menubar** — Uses `role="menubar"`, `role="menu"`, `role="menuitem"`. Replicates desktop application menu behavior. Appropriate for app-like toolbars.

**Use Disclosure Navigation for websites. Use ARIA Menubar only for application menus.**

---

## Pattern 1: Disclosure Navigation (Recommended for Websites)

### HTML Structure

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>

    <!-- Dropdown item -->
    <li>
      <button
        type="button"
        aria-expanded="false"
        aria-controls="services-menu"
        id="services-btn"
      >
        Services
      </button>
      <ul id="services-menu" aria-labelledby="services-btn">
        <li><a href="/services/web">Web Design</a></li>
        <li><a href="/services/mobile">Mobile Apps</a></li>
        <li><a href="/services/consulting">Consulting</a></li>
      </ul>
    </li>

    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

### Keyboard Interaction (Disclosure)

| Key | Behavior |
|-----|----------|
| `Tab` | Move through top-level links and buttons |
| `Enter` / `Space` | Activate button: toggle dropdown open/closed |
| `Tab` (when dropdown open) | Navigate through dropdown links |
| `Escape` | Close dropdown; return focus to trigger button |

### JavaScript

```javascript
class DisclosureNav {
  constructor(nav) {
    this.nav = nav;
    this.buttons = [...nav.querySelectorAll('button[aria-controls]')];

    this.buttons.forEach(btn => {
      btn.addEventListener('click', this.handleButtonClick.bind(this));
    });

    // Close on Escape key
    nav.addEventListener('keydown', this.handleKeydown.bind(this));

    // Close when clicking outside
    document.addEventListener('click', this.handleOutsideClick.bind(this));
  }

  handleButtonClick(e) {
    const btn = e.currentTarget;
    const isExpanded = btn.getAttribute('aria-expanded') === 'true';

    // Close all other dropdowns first
    this.buttons.forEach(b => {
      if (b !== btn) {
        b.setAttribute('aria-expanded', 'false');
        document.getElementById(b.getAttribute('aria-controls')).hidden = true;
      }
    });

    // Toggle this dropdown
    btn.setAttribute('aria-expanded', String(!isExpanded));
    document.getElementById(btn.getAttribute('aria-controls')).hidden = isExpanded;
  }

  handleKeydown(e) {
    if (e.key === 'Escape') {
      const openBtn = this.buttons.find(b => b.getAttribute('aria-expanded') === 'true');
      if (openBtn) {
        openBtn.setAttribute('aria-expanded', 'false');
        document.getElementById(openBtn.getAttribute('aria-controls')).hidden = true;
        openBtn.focus(); // Return focus to button
      }
    }
  }

  handleOutsideClick(e) {
    if (!this.nav.contains(e.target)) {
      this.buttons.forEach(btn => {
        btn.setAttribute('aria-expanded', 'false');
        document.getElementById(btn.getAttribute('aria-controls')).hidden = true;
      });
    }
  }
}

new DisclosureNav(document.querySelector('nav[aria-label="Main navigation"]'));
```

---

## Pattern 2: Hamburger Menu (Mobile Navigation)

### HTML Structure

```html
<header>
  <a href="/" aria-label="Acme Corp homepage">
    <img src="logo.svg" alt="">
  </a>

  <button
    type="button"
    id="mobile-nav-toggle"
    aria-expanded="false"
    aria-controls="mobile-nav-menu"
    aria-label="Open navigation menu"
  >
    <!-- Hamburger icon (decorative) -->
    <svg aria-hidden="true" focusable="false" width="24" height="24">
      <rect y="4" width="24" height="2" fill="currentColor"/>
      <rect y="11" width="24" height="2" fill="currentColor"/>
      <rect y="18" width="24" height="2" fill="currentColor"/>
    </svg>
  </button>

  <nav id="mobile-nav-menu" aria-label="Main navigation" hidden>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/products">Products</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>
</header>
```

```javascript
const toggle = document.getElementById('mobile-nav-toggle');
const menu = document.getElementById('mobile-nav-menu');

toggle.addEventListener('click', () => {
  const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!isExpanded));

  // Update button label to reflect state
  toggle.setAttribute('aria-label', isExpanded ? 'Open navigation menu' : 'Close navigation menu');
  menu.hidden = isExpanded;
});

// Close on Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation menu');
    menu.hidden = true;
    toggle.focus();
  }
});
```

---

## Pattern 3: ARIA Menubar (Application Menus Only)

Use for application toolbars that mimic native desktop menus (File, Edit, View, Help). **Not recommended for standard website navigation.**

### HTML Structure

```html
<div role="menubar" aria-label="Application menu">
  <!-- Top-level menu buttons -->
  <button
    role="menuitem"
    aria-haspopup="menu"
    aria-expanded="false"
    id="file-menu-btn"
    tabindex="0"
  >
    File
  </button>
  <ul role="menu" aria-labelledby="file-menu-btn" hidden>
    <li role="menuitem" tabindex="-1">New</li>
    <li role="menuitem" tabindex="-1">Open</li>
    <li role="separator"></li>
    <li role="menuitem" tabindex="-1">Save</li>
    <li role="menuitem" tabindex="-1">Exit</li>
  </ul>

  <button
    role="menuitem"
    aria-haspopup="menu"
    aria-expanded="false"
    id="edit-menu-btn"
    tabindex="-1"
  >
    Edit
  </button>
  <!-- Edit submenu -->
</div>
```

### Keyboard Interaction (ARIA Menubar)

| Key | Context | Behavior |
|-----|---------|----------|
| `Left Arrow` / `Right Arrow` | Menubar | Move focus between menubar items |
| `Enter` / `Space` / `Down Arrow` | Menubar item | Open submenu; focus first item |
| `Up Arrow` / `Down Arrow` | Open menu | Move focus through menu items |
| `Enter` | Menu item | Activate item; close menu |
| `Escape` | Open menu | Close menu; return focus to menubar item |
| `Tab` | Menubar | Close open menu; move focus to next tab stop |
| Type a letter | Open menu | Move focus to next item starting with that letter |

---

## Skip Navigation

All navigations must be preceded by a skip link (WCAG SC 2.4.1).

```html
<!-- First child of <body> -->
<a class="skip-link" href="#main-content">Skip to main content</a>

<!-- If there are multiple nav areas -->
<a class="skip-link" href="#main-nav">Skip to navigation</a>
<a class="skip-link" href="#main-content">Skip to main content</a>
<a class="skip-link" href="#search">Skip to search</a>

<style>
.skip-link {
  position: absolute;
  top: -9999px;
  left: -9999px;
  background: #000;
  color: #fff;
  padding: 8px 16px;
  text-decoration: none;
  z-index: 9999;
  border-radius: 0 0 4px 0;
}

.skip-link:focus {
  position: absolute;
  top: 0;
  left: 0;
}
</style>
```

---

## Breadcrumb Navigation

```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li>
      <!-- Current page: aria-current, no link needed -->
      <span aria-current="page">Wireless Keyboard</span>
    </li>
  </ol>
</nav>
```

- Use `<ol>` (ordered list) — breadcrumbs are ordered
- Mark current page with `aria-current="page"`
- Wrap in `<nav aria-label="Breadcrumb">` to distinguish from main nav

---

## Pagination

```html
<nav aria-label="Pagination">
  <ul>
    <li>
      <a href="/products?page=1" aria-label="Previous page">‹ Previous</a>
    </li>
    <li>
      <a href="/products?page=1" aria-label="Page 1">1</a>
    </li>
    <li>
      <!-- Current page -->
      <a href="/products?page=2" aria-current="page" aria-label="Page 2, current">2</a>
    </li>
    <li>
      <a href="/products?page=3" aria-label="Page 3">3</a>
    </li>
    <li>
      <a href="/products?page=3" aria-label="Next page">Next ›</a>
    </li>
  </ul>
</nav>
```

---

## Common Navigation Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Keyboard-only: hover opens dropdowns | Inaccessible to keyboard | Require click/Enter on button |
| No Escape to close dropdown | Keyboard trap | Add `keydown` → Escape handler |
| `aria-haspopup` on `<nav>` | Invalid role usage | Use `aria-haspopup` on the `<button>` |
| `<div>` as nav container | Not a landmark | Use `<nav>` |
| No `aria-label` on multiple `<nav>` elements | Can't distinguish navs | Label each nav: "Main", "Footer", "Breadcrumb" |
| Active/current page not indicated | Users can't orient | Add `aria-current="page"` |
| Icon-only hamburger button, no label | "Button" announced only | Add `aria-label="Open menu"` |
