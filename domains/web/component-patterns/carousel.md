---
title: "Accessible Carousel (Slider) Component Pattern"
standard: "WAI-ARIA APG + WCAG SC 2.2.2"
source_url: "https://www.w3.org/WAI/ARIA/apg/patterns/carousel/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["carousel", "slider", "auto-play", "2.2.2", "aria", "component-pattern", "live-region"]
ai_context: "Complete accessible carousel pattern. Covers auto-play pause controls, slide navigation, and ARIA markup. Load when implementing a carousel or slider component."
---

# Accessible Carousel (Slider) Component Pattern

---

## WCAG Requirements for Carousels

| SC | Requirement | Level | How it applies |
|----|------------|-------|----------------|
| SC 2.2.2 — Pause, Stop, Hide | Auto-rotating carousels must be pausable | A | Pause/play button required |
| SC 1.3.1 — Info and Relationships | Slide content has meaningful structure | A | Slides need headings or labels |
| SC 2.1.1 — Keyboard | All controls keyboard accessible | A | Tab to each button; arrow navigation |
| SC 4.1.2 — Name, Role, Value | All controls have accessible names | A | Labeled buttons; labeled container |

---

## Required Controls

For any auto-rotating carousel:
1. **Pause/Play button** — toggles automatic rotation
2. **Previous button** — go to previous slide
3. **Next button** — go to next slide
4. **(Optional) Slide picker buttons** — jump to specific slide

For manual-only carousels (no auto-rotation): only Previous/Next buttons are required.

---

## HTML Structure

```html
<section
  aria-roledescription="carousel"
  aria-label="Featured products"
  class="carousel"
>
  <!-- Auto-rotation controls (above slides) -->
  <div class="carousel-controls">
    <button
      type="button"
      class="carousel-pause"
      aria-label="Pause automatic slide show"
    >
      ⏸ Pause
    </button>
  </div>

  <!-- Slide container -->
  <div aria-live="polite" aria-atomic="false" class="carousel-slides">
    <div
      role="group"
      aria-roledescription="slide"
      aria-label="1 of 4"
      class="carousel-slide active"
    >
      <h3>Product A</h3>
      <img src="product-a.jpg" alt="Product A — ergonomic desk chair in grey">
      <p>Starting at $299</p>
      <a href="/products/a">Shop Product A</a>
    </div>

    <div
      role="group"
      aria-roledescription="slide"
      aria-label="2 of 4"
      class="carousel-slide"
      hidden
    >
      <h3>Product B</h3>
      <img src="product-b.jpg" alt="Product B — standing desk in walnut">
      <p>Starting at $599</p>
      <a href="/products/b">Shop Product B</a>
    </div>

    <!-- Additional slides... -->
  </div>

  <!-- Navigation controls (below slides) -->
  <div class="carousel-nav">
    <button type="button" class="carousel-prev" aria-label="Previous slide">
      ‹ Previous
    </button>
    <button type="button" class="carousel-next" aria-label="Next slide">
      Next ›
    </button>
  </div>

  <!-- Slide picker (optional) -->
  <div role="group" aria-label="Choose slide to display" class="carousel-picker">
    <button
      type="button"
      aria-label="Slide 1"
      aria-current="true"
      class="picker-btn active"
    ></button>
    <button type="button" aria-label="Slide 2" class="picker-btn"></button>
    <button type="button" aria-label="Slide 3" class="picker-btn"></button>
    <button type="button" aria-label="Slide 4" class="picker-btn"></button>
  </div>
</section>
```

---

## Key ARIA Notes

### `aria-roledescription="carousel"`

Applied to the container. This replaces the generic "region" or "section" announcement with "carousel" for screen reader users.

### `aria-roledescription="slide"`

Applied to each slide group. Tells screen readers each item is a "slide" not just a "group."

### `aria-live="polite"` on slide container

When a new slide becomes active, screen readers will announce its content after the user finishes their current interaction. Use `aria-atomic="false"` so individual slide content is read, not the entire container.

### Auto-rotation and `aria-live`

When auto-rotation is active, the `aria-live` attribute will cause announcements on every rotation — potentially disruptive. Some implementations set `aria-live="off"` while rotating and restore it when rotation is paused.

```javascript
// Remove live region while auto-rotating; restore when paused
function toggleRotation(paused) {
  const slideContainer = document.querySelector('.carousel-slides');
  if (paused) {
    slideContainer.setAttribute('aria-live', 'polite');
  } else {
    slideContainer.removeAttribute('aria-live'); // Or set to 'off'
  }
}
```

---

## JavaScript

```javascript
class Carousel {
  constructor(element) {
    this.carousel = element;
    this.slides = [...element.querySelectorAll('[role="group"][aria-roledescription="slide"]')];
    this.currentIndex = 0;
    this.isPlaying = true;
    this.interval = null;

    const pauseBtn = element.querySelector('.carousel-pause');
    const prevBtn = element.querySelector('.carousel-prev');
    const nextBtn = element.querySelector('.carousel-next');
    const pickerBtns = [...element.querySelectorAll('.picker-btn')];

    pauseBtn?.addEventListener('click', () => this.togglePlay(pauseBtn));
    prevBtn?.addEventListener('click', () => this.previous());
    nextBtn?.addEventListener('click', () => this.next());
    pickerBtns.forEach((btn, i) => btn.addEventListener('click', () => this.goTo(i)));

    // Pause on focus within carousel (WCAG recommendation)
    element.addEventListener('focusin', () => this.pauseRotation());
    element.addEventListener('focusout', e => {
      if (!element.contains(e.relatedTarget)) {
        if (this.isPlaying) this.startRotation();
      }
    });

    // Pause on hover
    element.addEventListener('mouseenter', () => this.pauseRotation());
    element.addEventListener('mouseleave', () => {
      if (this.isPlaying) this.startRotation();
    });

    this.startRotation();
  }

  togglePlay(btn) {
    this.isPlaying = !this.isPlaying;
    if (this.isPlaying) {
      btn.setAttribute('aria-label', 'Pause automatic slide show');
      btn.textContent = '⏸ Pause';
      this.startRotation();
    } else {
      btn.setAttribute('aria-label', 'Start automatic slide show');
      btn.textContent = '▶ Play';
      this.pauseRotation();
    }
  }

  startRotation() {
    this.pauseRotation();
    this.interval = setInterval(() => this.next(), 5000);
  }

  pauseRotation() {
    clearInterval(this.interval);
    this.interval = null;
  }

  goTo(index) {
    this.slides[this.currentIndex].hidden = true;
    this.slides[this.currentIndex].classList.remove('active');

    this.currentIndex = (index + this.slides.length) % this.slides.length;

    this.slides[this.currentIndex].hidden = false;
    this.slides[this.currentIndex].classList.add('active');

    // Update picker button states
    this.carousel.querySelectorAll('.picker-btn').forEach((btn, i) => {
      btn.setAttribute('aria-current', i === this.currentIndex ? 'true' : 'false');
    });
  }

  next() { this.goTo(this.currentIndex + 1); }
  previous() { this.goTo(this.currentIndex - 1); }
}

document.querySelectorAll('[aria-roledescription="carousel"]').forEach(el => {
  new Carousel(el);
});
```

---

## `prefers-reduced-motion`

Always respect the user's motion preference. Auto-rotation counts as motion.

```javascript
// Check before starting auto-rotation
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReduced) {
  this.startRotation();
} else {
  this.isPlaying = false;
  // Update pause button label to reflect non-playing state
  pauseBtn.setAttribute('aria-label', 'Start automatic slide show');
}
```

```css
@media (prefers-reduced-motion: reduce) {
  .carousel-slide {
    transition: none;
    animation: none;
  }
}
```

---

## Common Carousel Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| No pause button | Fails SC 2.2.2 | Add pause/play button |
| Auto-rotation continues on focus | Keyboard users can't read content before it changes | Pause on focusin; resume on focusout |
| "Next" button announces slide content | Confusing screen reader experience | The button label should not include slide content |
| Slide content not in `aria-live` | Screen reader doesn't announce new slides | Wrap slides in `aria-live="polite"` container |
| Slide picker buttons unlabeled | "button" only announced | Add `aria-label="Slide 1"` etc. |
| Slides not hidden | All slides read linearly | Use `hidden` attribute on inactive slides |
| No visible focus indicator | Keyboard users can't see focus | Ensure `:focus-visible` styles on all buttons |
