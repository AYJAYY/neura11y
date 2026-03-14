---
title: "Alt Text Principles for Social Media"
standard: "WCAG SC 1.1.1"
source_url: "https://www.w3.org/TR/WCAG22/#non-text-content"
domain: ["social-media", "web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["alt-text", "images", "social-media", "1.1.1", "principles", "non-text-content"]
ai_context: "Core principles for writing alt text for social media images. The most cross-cutting practical guide in this repository. Load for any task involving image descriptions."
---

# Alt Text Principles for Social Media

Alt text (alternative text) provides a text equivalent for images so people who cannot see the image — whether due to disability, slow connections, or image load failures — can understand the content.

**WCAG SC 1.1.1:** All non-text content has a text alternative that serves the equivalent purpose.

---

## Why Alt Text Matters on Social Media

- **Screen readers** read alt text aloud for users who are blind or have low vision
- **Voice assistants** use alt text to describe images
- **Search indexing** improves content discoverability
- **Failed image loading** shows alt text as fallback
- **Inclusive communication** reaches all audience members

---

## Platform Character Limits

| Platform | Alt Text Character Limit | Notes |
|----------|-------------------------|-------|
| Twitter/X | 1,000 characters | Added 2016; increased 2022 |
| Instagram | ~100 characters (auto AI) / manual | Custom text longer; AI auto-generates |
| LinkedIn | ~120 characters (recommended) | No hard limit documented |
| Facebook | Variable | No published hard limit |
| Mastodon | 1,500 characters | Most generous limit |
| TikTok | Not available for images | Captions cover video |
| YouTube | Not applicable | Use video captions and descriptions |

**Target length for social media:** 125 characters for brevity and compatibility. For complex images (charts, infographics), use platform maximum and link to full text description if needed.

---

## The 10 Core Principles

### Principle 1: Describe What Is There, Not What You Feel

Describe the content of the image objectively. Interpretations and emotions belong in the post caption, not the alt text.

- **Weak:** "Beautiful sunset photo"
- **Better:** "Orange and pink sunset sky reflected in a calm lake, with silhouette of pine trees along the horizon"

### Principle 2: Lead with the Most Important Information

Screen readers read alt text linearly. Put the subject of the image first.

- **Weak:** "At a conference last week, our CEO Jane Smith is pictured speaking on stage"
- **Better:** "Jane Smith speaking at a podium on the TechConf 2025 stage, microphone in hand, slide reading 'The Future of Accessibility' behind her"

### Principle 3: Be Concise

Target 125 characters for social media. Longer descriptions are harder to process and exceed some platform limits.

- Omit unnecessary words: "a photo of" → start with the subject
- Skip filler: "an image showing" → describe directly
- One strong sentence is usually enough for a simple image

### Principle 4: Do Not Start with "Image of" or "Photo of"

Screen readers already announce the element type. The alt text should start with the content.

- **Wrong:** "Image of two people shaking hands"
- **Correct:** "Two people shaking hands at a business meeting"

### Principle 5: Include Text That Appears in the Image

If text is visible in the image, transcribe it exactly (or summarize for long text). Screen readers cannot read text embedded in images.

- For a quote card: Alt text = the full quote text
- For a screenshot of a tweet: Alt text = the tweet text
- For a price tag in a product photo: Include the price if visible

### Principle 6: Context Determines Content

The same image may need different alt text in different posts. The alt text should match what the post is communicating.

- A photo of a burger in a food post: "Beef burger with lettuce, tomato, and brioche bun on a wooden board"
- The same photo in a post about food waste: "Uneaten burger and fries left on a restaurant table"

### Principle 7: Decorative Images Get Empty Alt or "Decorative" Option

If an image adds no informational value (purely aesthetic background, spacer), mark it as decorative:
- HTML: `alt=""`
- Platforms with "mark as decorative" option: use that option
- Do NOT omit alt text entirely on social platforms (differs from HTML)

### Principle 8: Describe Diversity When Relevant to Context

When people appear in images:
- Describe their apparent characteristics when relevant to the post's message
- Describe race, gender, age, disability if they are relevant and verifiable from the image
- Don't assume or over-interpret — describe what is visible
- When in doubt about a characteristic, omit it rather than guess

Example (diversity post): "Four colleagues sitting around a conference table: two Black women, one South Asian man, one white woman, all reviewing documents"

### Principle 9: Describe Mood and Tone When Relevant

Facial expressions, body language, and setting contribute to meaning. Include when they matter.

- "Person smiling and raising a trophy" — emotion matters here
- "Dog sitting in a park" — emotion less critical unless the post is about the dog's reaction

### Principle 10: Describe the Purpose of Functional Images

For images that are links or buttons (less common on social media), describe the action/destination, not just the appearance.

---

## Alt Text by Image Type

### Simple Object
Describe the object and relevant attributes (color, size, material, state).
> "Red ceramic coffee mug with a chip on the rim, sitting on a white surface"

### Person / People
Describe the action, context, and appearance details relevant to the post.
> "Young woman in a yellow hard hat on a construction site, reviewing blueprints"

### Text Screenshots
Transcribe the text exactly. If too long, summarize and note "[full text in comments]".
> "Tweet from @accessibility_news: 'Latest WCAG update officially published today with 9 new success criteria. Details at w3.org'"

### Charts and Graphs
State the type of chart, what it measures, and the key finding. Don't describe every data point.
> "Bar chart showing monthly website traffic Jan-Jun 2025. Traffic grew from 12K to 28K visitors, peaking in April at 31K"

### Infographic
Lead with the main message. List key points if space allows. Link to text version in caption.
> "Infographic: 5 steps to audit website accessibility: 1. Run automated scan 2. Test keyboard navigation 3. Test with screen reader 4. Check color contrast 5. Test with real users [Full details in thread]"

### Meme
Explain the meme format and the punchline.
> "SpongeBob Mocking meme. Top: 'Website needs to be accessible'. Bottom (mocking text): 'WeBsiTe nEEds tO Be AcCeSSibLe'"

### Product
Describe the product, its key features visible in the image, color, and context.
> "Wireless headphones in matte black with cushioned ear cups, on a wooden desk next to a laptop"

### Before / After
Clearly label both states.
> "Before: cluttered desk with papers, cords, and three monitors. After: clean desk with single ultrawide monitor, cable management, and plant"

### Logo
Name the organization and describe the logo design briefly.
> "ACME Corporation logo: stylized red rocket above the company name in bold sans-serif font"

---

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| "Photo" or "Image" | Screen reader already says it's an image | Start with content |
| "See image" or "See caption" | No information provided | Describe the image |
| Completely empty | Missing for non-decorative image | Write a description |
| Overly long (>300 chars) | Difficult to process; exceeds limits | Condense to key info |
| Irrelevant detail | Fills limit without helping | Describe what matters |
| Missing image text | Text in image inaccessible | Transcribe visible text |
| Generic ("people laughing") | Not meaningful | Add context: where, why |
| Over-interpreting emotion | Introduces bias/inaccuracy | Describe visible facts |

---

## Writing Alt Text for AI Generation

When asking AI to generate alt text, provide:
1. The image (or a detailed description if providing to text-only AI)
2. The post context/purpose
3. The target platform (for character limits)
4. Any text visible in the image

Prompt template:
```
Write alt text for this image for [platform] (character limit: [N]).
The post is about: [topic/context].
The image shows: [brief description if needed].
Any visible text: [text in image].
```
