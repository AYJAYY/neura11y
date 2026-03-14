---
title: "Images and Media Accessibility"
standard: "WCAG"
source_url: "https://www.w3.org/WAI/tutorials/images/"
domain: ["web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["images", "alt-text", "svg", "video", "audio", "captions", "audio-description", "transcripts"]
ai_context: "How to make images, video, and audio accessible on the web. Load when generating HTML with media or when asked about alt text, captions, or audio description."
---

# Images and Media Accessibility

---

## Images — SC 1.1.1 (Non-text Content, Level A)

Every non-decorative image must have a text alternative. The correct text alternative depends on the image's purpose.

### Decision Tree

```
Is the image decorative (purely visual, no informational purpose)?
  YES → alt=""  (empty alt; do NOT omit the attribute)
  NO →
    Does the image contain text?
      YES → alt = the text in the image
      NO →
        Is the image functional (a link or button)?
          YES → alt = the destination or action (not a description)
          NO →
            Is the image complex (chart, graph, infographic)?
              YES → alt = short description + long description via aria-describedby or adjacent text
              NO → alt = meaningful description of content and context
```

### Alt Text Rules

| Rule | Correct | Wrong |
|------|---------|-------|
| Describe function, not appearance, for functional images | `alt="Submit form"` | `alt="Blue button"` |
| Don't start with "Image of" or "Picture of" | `alt="Cat on a mat"` | `alt="Image of a cat on a mat"` |
| Match the text in text images | `alt="50% Off"` | `alt="Sale graphic"` |
| Empty alt for decorative images | `alt=""` | `alt=" "` or omitting `alt` |
| Context can shorten needed description | `alt="Sales chart showing 20% growth Q3"` | `alt="Bar chart"` |

### Alt Text Length

- **Short descriptions:** 150 characters or fewer for simple images
- **Complex images:** Short alt + long description (see Complex Images section)
- No hard maximum, but brevity is valued; screen readers don't paginate

---

## Decorative Images

An image is decorative when it:
- Adds visual style only (dividers, backgrounds, icons adjacent to text)
- Is described by adjacent text already
- Is part of a linked element already described by link text

```html
<!-- Decorative: adjacent text describes it -->
<img src="checkmark.png" alt="" aria-hidden="true"> Task completed

<!-- Decorative: icon inside a labeled button -->
<button>
  <img src="send-icon.svg" alt="">
  Send message
</button>

<!-- CSS background images: no alt needed -->
<div class="hero-banner" role="img" aria-label="Company headquarters at sunset">
  <!-- background image via CSS -->
</div>
```

---

## Functional Images (Links and Buttons)

When an image IS the only content of a link or button, the alt text must describe the action or destination, not the image itself.

```html
<!-- Link to home page -->
<a href="/"><img src="logo.png" alt="Acme Corporation home page"></a>

<!-- Search button -->
<button><img src="search-icon.png" alt="Search"></button>

<!-- Logo in nav: describes destination -->
<a href="/"><img src="logo.svg" alt="Acme Corp — return to homepage"></a>

<!-- Icon button with visible label: decorative alt -->
<button>
  <img src="edit-icon.svg" alt="">
  Edit profile
</button>
```

---

## Text Images (SC 1.4.5 — Level AA)

Use actual text instead of images of text except:
- Logos and brand marks
- When a specific visual presentation is essential (sample font display, historical document)

```html
<!-- WRONG: image of heading text -->
<img src="page-title.png" alt="About Our Company">

<!-- CORRECT: real text styled with CSS -->
<h1>About Our Company</h1>
```

---

## Complex Images

Charts, graphs, diagrams, maps, and infographics need both a short alt and a long description.

### Method 1: Long Description via aria-describedby

```html
<figure>
  <img
    src="sales-chart.png"
    alt="Bar chart: Q1–Q4 2025 revenue by region"
    aria-describedby="sales-chart-desc"
  >
  <figcaption id="sales-chart-desc">
    North America led in Q1 ($4.2M) and Q2 ($3.8M). Europe showed the
    strongest growth, rising from $1.1M in Q1 to $2.9M in Q4. APAC
    remained flat at approximately $0.8M per quarter.
  </figcaption>
</figure>
```

### Method 2: Adjacent Description in Text

```html
<img src="network-diagram.png" alt="Network architecture diagram — see description below">
<p>The diagram shows three tiers: presentation layer (web servers), application layer (API servers), and data layer (database cluster)...</p>
```

### Method 3: Linked Long Description

```html
<img src="complex-infographic.png" alt="Global accessibility legislation summary" aria-describedby="infographic-summary">
<p id="infographic-summary">
  <a href="infographic-text-version.html">Full text version of infographic</a>
</p>
```

---

## SVG Accessibility

SVG requires special handling for screen reader support.

### Inline SVG (Best Control)

```html
<svg role="img" aria-labelledby="svg-title svg-desc" focusable="false">
  <title id="svg-title">Quarterly revenue trend</title>
  <desc id="svg-desc">Line chart showing revenue increasing from $1M in Q1 to $4M in Q4 2025</desc>
  <!-- SVG paths and shapes -->
</svg>
```

### Decorative SVG

```html
<!-- Hide from screen readers completely -->
<svg aria-hidden="true" focusable="false">
  <!-- decorative icon -->
</svg>
```

### SVG as img

```html
<img src="icon.svg" alt="Settings" width="24" height="24">
```

### Common SVG Issues

- **focusable="false"** — required in IE11 and some older browsers to prevent SVG from receiving Tab focus
- **Don't use `<title>` alone** — add `aria-labelledby` pointing to the title element
- **Interactive SVG** — each interactive element needs `role`, `aria-label`, and `tabindex`

---

## Video — SC 1.2.1, 1.2.2, 1.2.3 (Level A) and 1.2.5 (Level AA)

### Requirements by Video Type

| Video type | Captions | Audio description | Transcript |
|---|---|---|---|
| Pre-recorded video with audio (1.2.2) | Required (AA) | — | — |
| Pre-recorded video-only (1.2.1) | — | Required OR transcript | Required OR audio desc |
| Pre-recorded video with audio (1.2.5) | — | Required (AA) | — |
| Live video with audio (1.2.4) | Required (AA) | — | — |

### Captions

Captions are synchronized text equivalents of the audio track, including dialogue, speaker IDs, and meaningful sound effects.

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <!-- WebVTT is the web standard -->
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English" default>
  <track kind="captions" src="captions-es.vtt" srclang="es" label="Español">
</video>
```

**Caption quality requirements:**
- Verbatim accuracy for dialogue
- Speaker identification when not visually clear
- Non-speech audio: `[applause]`, `[phone ringing]`
- Proper timing: captions match speech within 2 seconds
- Max 32 characters per line; max 2 lines per caption block

### Audio Description

Audio description describes important visual information that cannot be understood from the audio alone.

```html
<video controls>
  <source src="video-with-ad.mp4" type="video/mp4">
  <track kind="descriptions" src="audio-desc.vtt" srclang="en" label="Audio description">
</video>
```

**When audio description is needed:**
- Speaker name appears on screen but not spoken
- Actions, locations, or text on screen not described in audio
- Key visual changes that affect understanding

**Extended audio description (SC 1.2.7, AAA):** When there isn't enough pause in the main audio, the video pauses to allow the description to finish.

### Transcript

A transcript is a text version of all audio and visual information.

```html
<details>
  <summary>Video transcript</summary>
  <p>[Narrator]: Welcome to our accessible video tutorial.</p>
  <p>[Screen shows: Homepage with navigation menu]</p>
  <p>[Narrator]: Today we'll cover how to use our navigation...</p>
</details>
```

---

## Audio — SC 1.2.1 (Pre-recorded audio-only)

Pre-recorded audio-only content (podcasts, audio clips) requires a transcript.

```html
<audio controls>
  <source src="podcast.mp3" type="audio/mpeg">
</audio>

<section aria-label="Podcast transcript">
  <h2>Episode Transcript</h2>
  <p><strong>[Host]</strong>: Welcome to episode 42...</p>
  <!-- Full verbatim transcript -->
</section>
```

---

## Media Player Accessibility

HTML native `<video>` and `<audio>` controls are keyboard accessible in all modern browsers. Custom players must:

1. All controls are keyboard focusable (`tabindex="0"` or native buttons)
2. All controls have accessible names (`aria-label` for icon-only buttons)
3. Keyboard shortcuts: Space (play/pause), Left/Right arrows (rewind/forward), M (mute), F (fullscreen)
4. Volume slider uses `role="slider"` with `aria-valuemin`, `aria-valuemax`, `aria-valuenow`
5. Progress bar: either `role="slider"` (interactive) or `role="progressbar"` (display-only)
6. Caption toggle button: `aria-pressed="true|false"` or `aria-label="Captions on/off"`

```html
<div role="group" aria-label="Video player controls">
  <button aria-label="Play" id="play-btn">▶</button>
  <div
    role="slider"
    aria-label="Seek video position"
    aria-valuemin="0"
    aria-valuemax="180"
    aria-valuenow="45"
    aria-valuetext="45 seconds of 3 minutes"
    tabindex="0"
  ></div>
  <button aria-label="Mute">🔊</button>
  <button aria-pressed="false" aria-label="Captions off — click to enable">CC</button>
</div>
```

---

## Animated Content — SC 2.2.2 (Pause, Stop, Hide — Level A)

Auto-playing content that moves, blinks, or scrolls and lasts more than 5 seconds must be pauseable, stoppable, or hideable.

```html
<!-- Carousel with pause control -->
<section aria-label="Featured news" aria-roledescription="carousel">
  <button id="pause-btn" aria-pressed="false">Pause rotation</button>
  <!-- slides -->
</section>
```

**Prefers-reduced-motion:**

```css
@media (prefers-reduced-motion: reduce) {
  .carousel { animation: none; }
  .spinner { animation: none; }
  .fade-in { transition: none; }
}
```

This is not a WCAG requirement (it's a best practice) but respects user OS settings.

---

## Image Maps

```html
<img src="building-map.png" alt="Building floor plan" usemap="#floormap">
<map name="floormap">
  <area shape="rect" coords="10,10,100,100" href="/room/101" alt="Room 101 — Conference Room">
  <area shape="rect" coords="110,10,200,100" href="/room/102" alt="Room 102 — Break Room">
</map>
```

Each `<area>` must have an `alt` attribute.

---

## Responsive Images

Alt text does not change based on screen size. If different images are shown at different sizes (via `<picture>` or `srcset`), ensure the alt text remains valid for all images shown.

```html
<picture>
  <source media="(max-width: 600px)" srcset="small-team-photo.jpg">
  <source media="(min-width: 601px)" srcset="large-team-photo.jpg">
  <!-- The alt applies to whichever image is shown -->
  <img src="large-team-photo.jpg" alt="Acme Corp engineering team, 2025 annual retreat">
</picture>
```
