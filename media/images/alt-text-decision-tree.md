---
title: "Alt Text Decision Tree and Image Types"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/tutorials/images/decision-tree/"
domain: ["web", "documents", "social-media", "general"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["alt-text", "images", "decision-tree", "1.1.1", "decorative", "complex-images"]
ai_context: "Decision tree and examples for writing alt text by image type. Load when writing or evaluating alt text for any context."
---

# Alt Text Decision Tree and Image Types

---

## Decision Tree

```
1. Does the image contain text?
   YES → alt = the text in the image (verbatim or as close as possible)
   NO → go to 2

2. Is the image used as a link or button (functional image)?
   YES → alt = the destination or action of the link/button
         NOT a description of the image
   NO → go to 3

3. Does the image contribute meaningful information to the content?
   NO → decorative → alt=""
   YES → go to 4

4. Is the image a chart, graph, or complex infographic?
   YES → short alt (topic + key data point) + long description
   NO → go to 5

5. Is the image a photograph or illustration?
   → alt = relevant content + context (not a catalog description)
   Limit: 150 characters for simple images
```

---

## By Image Type

### 1. Informative Images (Photographs, Illustrations)

Describe the content relevant to the surrounding context. The same image may need different alt text depending on use.

**Context 1: Article about a product**
```html
<img src="red-running-shoe.jpg"
     alt="Nike Air Zoom Pegasus 40 in red and white, side view">
```

**Context 2: Article about color trends in footwear**
```html
<img src="red-running-shoe.jpg"
     alt="Running shoe in bright red with white accents — an example of the bold color trend">
```

**Context 3: Decorative header image**
```html
<img src="red-running-shoe.jpg" alt="">
```

---

### 2. Decorative Images

Images that are purely visual, repeat information already in text, or are used for layout/design.

```html
<!-- Empty alt required — do NOT omit the alt attribute -->
<img src="divider-line.png" alt="">
<img src="background-pattern.png" alt="">

<!-- Icon that's adjacent to text labeling it -->
<img src="calendar-icon.png" alt=""> Appointments

<!-- CSS background images: no alt attribute needed -->
<style>.hero { background-image: url('hero.jpg'); }</style>
```

**NEVER** use `alt="decorative"` or `alt="image"` — these get read by screen readers. Use `alt=""` only.

---

### 3. Functional Images (Links and Buttons)

Alt text = the action or destination, NOT a description of the image.

```html
<!-- Link to homepage -->
<a href="/"><img src="company-logo.png" alt="Acme Corp — go to homepage"></a>

<!-- Search button -->
<button><img src="magnifying-glass.svg" alt="Search"></button>

<!-- Social share button -->
<a href="https://twitter.com/share?..."><img src="twitter-icon.svg" alt="Share on Twitter"></a>

<!-- Icon inside button with visible label — decorative -->
<button>
  <img src="print-icon.png" alt="">
  Print this page
</button>
```

---

### 4. Text Images

Alt = verbatim text in the image.

```html
<img src="sale-banner.png" alt="50% Off — Sale ends March 31">
<img src="warning-label.png" alt="WARNING: Keep out of reach of children">
<img src="signature.png" alt="John Smith (signature)">
```

For **logos with text**:

```html
<!-- Logo used as image: alt = company name -->
<img src="acme-logo.png" alt="Acme Corp">

<!-- Logo used as link: alt = company name + destination -->
<a href="/"><img src="acme-logo.png" alt="Acme Corp homepage"></a>
```

---

### 5. Complex Images (Charts, Graphs, Diagrams, Infographics)

Need both a short alt and a long description.

```html
<!-- Method 1: Long description in adjacent figure caption -->
<figure>
  <img src="bar-chart.png"
       alt="Bar chart: Q4 2025 revenue by region — see caption for data"
       aria-describedby="chart-desc">
  <figcaption id="chart-desc">
    Q4 2025 revenue: North America $4.2M (leading), Europe $2.9M (up 28% year-over-year),
    APAC $0.8M (flat). Total: $7.9M.
  </figcaption>
</figure>

<!-- Method 2: Linked text version -->
<img src="complex-infographic.png"
     alt="2025 global accessibility legislation map">
<p><a href="/accessibility-legislation-text">Text version of the legislation map</a></p>

<!-- Method 3: Expandable description -->
<img src="network-diagram.png"
     alt="Three-tier network architecture diagram"
     aria-describedby="net-desc">
<details>
  <summary>Expand diagram description</summary>
  <p id="net-desc">
    The diagram shows three tiers arranged vertically. Tier 1 (top):
    two web servers load-balanced behind a CDN. Tier 2 (middle): four
    application servers with a message queue. Tier 3 (bottom): primary
    database with read replica.
  </p>
</details>
```

---

### 6. Images of People (Photographs)

Include context-relevant details. Do not focus on physical appearance unless relevant to content.

**Wrong:** `alt="Man with brown hair sitting at a desk"`
**Correct (general):** `alt="Software developer reviewing code on dual monitors"`
**Correct (named person in article about them):** `alt="Tim Berners-Lee, inventor of the World Wide Web, at a conference"`

For group photos: describe the group context, not individuals unless relevant.
```html
<img src="team-photo.jpg" alt="Acme Corp engineering team at the 2025 annual company retreat">
```

---

### 7. Graphs and Data Visualizations

Alt text must convey the conclusion or key insight, not just what the chart looks like.

**Wrong:** `alt="Bar chart with blue and red bars"`
**Correct:** `alt="Revenue chart showing 34% year-over-year growth in Q4 2025, the highest quarter on record"`

For accessible data visualization, also consider:
- Providing the underlying data as an HTML table
- Including a brief textual summary of the chart's key finding
- Using color + patterns to distinguish data series (not color alone)

---

### 8. Maps

```html
<img src="us-map-with-offices.png"
     alt="US map showing Acme Corp office locations"
     aria-describedby="office-locations">
<div id="office-locations">
  <h3>Office locations:</h3>
  <ul>
    <li>San Francisco, CA (headquarters)</li>
    <li>New York, NY</li>
    <li>Austin, TX</li>
    <li>Chicago, IL</li>
  </ul>
</div>
```

---

### 9. Social Media Images

Platform-specific character limits apply. See platform guides for constraints.

**General rules for social media alt text:**
- Platform limits: 1000 chars (Twitter/X), 420 chars (Facebook), 500 chars (Instagram), 1500 chars (Mastodon)
- Describe what a sighted user would see and why it's relevant to the post
- Include any text visible in the image
- Describe the emotion/tone when it contributes to meaning
- Don't start with "Image of" or "Photo of"

---

## Common Alt Text Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Missing alt attribute | `<img src="photo.jpg">` | Always include `alt` attribute |
| "Image of" / "Photo of" | `alt="Image of sunset"` | `alt="Golden sunset over the Pacific Ocean"` |
| Filename as alt text | `alt="IMG_2045.jpg"` | Describe the content |
| Alt text for decorative image | `alt="decorative border"` | `alt=""` |
| Redundant with surrounding text | Image with `alt="Company logo"` beside "Acme Corp" heading | `alt=""` (let the heading describe it) |
| Too literal for charts | `alt="Bar chart"` | Include the key insight |
| Truncated URL | `alt="https://example.com/products/widget-x-pro-blue-large"` | `alt="Widget X Pro"` |
