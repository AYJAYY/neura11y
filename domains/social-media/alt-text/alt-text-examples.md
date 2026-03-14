---
title: "Alt Text Examples by Image Type"
standard: "WCAG 2.2"
source_url: "https://www.w3.org/WAI/tutorials/images/"
domain: ["social-media", "general"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["alt-text", "examples", "social-media", "before-after", "image-types"]
ai_context: "Before/after alt text examples by image type for social media and general use. Load when writing or evaluating alt text quality."
---

# Alt Text Examples by Image Type

---

## Product Images

| Image | Too Vague | Too Literal | Good Alt Text |
|-------|-----------|-------------|---------------|
| Running shoe | "shoe" | "A red and white athletic shoe photographed on a white background at a slight angle showing the sole" | "Nike Air Zoom Pegasus 40 running shoe in crimson red with white sole" |
| Coffee mug | "mug" | "A white ceramic cylindrical mug with a handle on a wooden table surface" | "White ceramic mug with company logo on a rustic wooden table" |
| Laptop | "computer" | "Silver laptop computer open at 120 degree angle showing a screen with a website on a white desk" | "MacBook Pro showing the Acme Corp homepage design" |

---

## People and Events

| Image | Bad Alt Text | Good Alt Text |
|-------|-------------|---------------|
| Speaker on stage | "person" | "Keynote speaker at the 2025 Accessibility Summit presenting to an audience of approximately 500" |
| Team photo | "team photo" | "Acme Corp engineering team of 12 people at the 2025 company retreat in Austin, TX" |
| Award ceremony | "award" | "Maria Chen receiving the Community Impact Award at the 2025 WebAIM ceremony" |
| Demonstration | "showing something" | "Presenter demonstrating VoiceOver navigation on an iPhone to a workshop audience" |
| Portrait (article about person) | "man" | "Tim Berners-Lee, inventor of the World Wide Web, speaking at a 2024 web conference" |

**Note on people photos:** Only include physical descriptions if directly relevant to the content. For a general team photo, names and roles are more useful than physical descriptions.

---

## Charts and Data Visualizations

| Chart Type | Bad Alt Text | Good Alt Text |
|------------|-------------|---------------|
| Bar chart | "bar chart" | "Bar chart showing NVDA (35%), JAWS (40%), and VoiceOver (10%) screen reader market share in 2024" |
| Line graph | "graph showing increase" | "Line graph showing web accessibility lawsuits increasing from 2,300 in 2018 to 4,600 in 2024, nearly doubling over six years" |
| Pie chart | "pie chart with different colors" | "Pie chart: 65% of accessibility issues detected by automated tools, 35% require manual testing" |
| Dashboard | "analytics dashboard" | "Analytics dashboard showing 92% accessibility score, 3 critical errors, and 12 warnings for the Acme Corp homepage" |
| Infographic | "infographic about accessibility" | "Infographic: 16% of people globally have a disability; 1 in 4 US adults has a disability; 98% of top 1M websites have WCAG failures" |

---

## Screenshots and UI

| Image | Bad Alt Text | Good Alt Text |
|-------|-------------|---------------|
| Website screenshot | "website screenshot" | "Acme Corp homepage showing a hero image of a mountain hike, navigation with Products, About, and Contact links, and a 'Get Started' call-to-action button" |
| Error message | "error" | "Browser showing error: 'Color contrast ratio is 2.1:1, must be at least 4.5:1 for normal text. Element: button.cta-primary'" |
| Form | "contact form" | "Contact form with fields for Name, Email, Message, and a Submit button; Email field shows red border with error text 'Please enter a valid email address'" |
| Code snippet | "code" | "JavaScript code showing an event listener on a button that sets aria-expanded to 'true' when clicked" |
| Accessibility checker | "scan results" | "Axe DevTools scan showing 4 critical errors: 2 missing form labels, 1 missing alt text, 1 button with no accessible name" |

---

## Social Media Specific Examples

### Twitter/X (1000 character limit)

**Product announcement image:**
> Product image showing the new Acme Widget Pro in matte black. Front view: a rounded rectangle device approximately 5×3 inches with a 4-inch circular display showing a spinning logo. The tagline "Designed for everyone" appears below in sans-serif type. Available March 28, 2026.

**Event poster:**
> Digital poster for the 2026 Web Accessibility Summit on April 12 in San Francisco. Text reads: "WAS 2026 | Building the Accessible Web | April 12-14, San Francisco Marriott | Keynotes, workshops, hands-on labs | Register by March 31 | was2026.org" Background is dark blue with geometric pattern. Acme Corp logo in upper right.

**Data visualization:**
> Bar chart from the 2025 State of Accessibility Report. Y-axis: percentage of websites. X-axis: WCAG error types. Results: Low contrast text 83%, Missing alt text 59%, Missing form labels 52%, Empty links 50%, Missing page language 17%, Empty buttons 27%. Source: WebAIM Million 2025.

---

### Instagram (up to 500 characters)

**Food/lifestyle photo:**
> Overhead view of a flat lay featuring an open laptop showing a WCAG checklist, a coffee mug, reading glasses, and a notebook with handwritten accessibility audit notes on a white marble surface.

**Before/after comparison:**
> Side-by-side comparison. Left (labeled "Before"): website with low contrast gray text on white background, no visible focus indicators, images without captions. Right (labeled "After"): same site with dark text, visible blue focus ring on active link, image with alt text tooltip visible.

---

### LinkedIn (up to 420 characters)

**Presentation slide:**
> Presentation slide titled "The Business Case for Accessibility." Three statistics in large text: $490B annual US spending power of adults with disabilities, 26% of US adults have a disability, 97.4% of top websites have WCAG failures. Acme Corp logo and "Q1 2026 Accessibility Workshop" footer.

---

## What to Avoid

### Too Short

| Image | Bad | Why it fails |
|-------|-----|--------------|
| Chart | "chart" | No data, no insight, no context |
| People photo | "people at a conference" | No context about why the image is in this post |
| Product | "headphones" | Could be any headphones; misses brand, features, context |

### Too Long / Catalog Description

| Image | Bad | Why it fails |
|-------|-----|--------------|
| Product | "White over-ear headphones with memory foam ear cushions, foldable design with rotating ear cups, detachable 3.5mm audio cable with inline microphone, USB-C charging port on left ear cup, volume control wheel on right ear cup, silver metallic headband with rubber non-slip interior, manufacturer markings on interior" | Reads like a product spec; misses the content purpose |

### Incorrect Focus

| Image | Context | Bad | Correct focus |
|-------|---------|-----|---------------|
| Speaker photo | Article about the event | "Woman with shoulder-length brown hair in a blue blazer" | "Dr. Sarah Kim opening the 2025 Accessibility Summit" |
| Chart | Post about growth | "Chart with bars in different heights" | "Revenue chart showing 34% year-over-year growth" |

---

## Alt Text for Memes and Humor

Memes require extra care:
- Describe the format of the meme template (context familiar to sighted users)
- Include all visible text verbatim
- Describe the image that makes the meme work

**Example:**
```
Alt text: "Distracted Boyfriend meme. Man looking at a woman labeled 'Adding new features' while his girlfriend labeled 'Fixing accessibility bugs' looks annoyed."
```
