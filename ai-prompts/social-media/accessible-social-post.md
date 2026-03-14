---
title: "Prompt Template: Create Accessible Social Media Post"
standard: "WCAG SC 1.1.1"
source_url: ""
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "template"
tags: ["ai-prompt", "social-media", "alt-text", "captions", "template"]
ai_context: "Ready-to-use prompt templates for creating accessible social media content. Load with platform-specific guide and alt-text-principles.md."
---

# Prompt Template: Create Accessible Social Media Post

## Context Files to Load

For any social media content creation task:
```
domains/social-media/alt-text/alt-text-principles.md
domains/social-media/writing-for-accessibility/hashtag-guide.md
domains/social-media/writing-for-accessibility/inclusive-language.md
domains/social-media/platforms/[platform]/[platform]-guide.md
```

---

## Template 1: Post with Image

```
Create an accessible [platform] post for the following image and context.

Platform: [Twitter/X | Instagram | LinkedIn | Facebook | Mastodon]
Character limit for post text: [280 | 2200 | 3000 | N/A | 500]
Alt text character limit: [1000 | ~300 | ~420 | N/A | 1500]

Image description: [Describe the image, including any visible text, people, objects, colors, setting]

Post topic/purpose: [What is this post communicating? Campaign, announcement, education, etc.]

Target audience: [Who will read this?]

Key message to convey: [What is the single most important point?]

Please provide:
1. Post text (within character limit)
   - Clear, accessible language
   - CamelCase hashtags at end of post
   - Emoji placed at end of sentences only (1-3 max)
2. Alt text for the image
   - [Platform] limit: [N] characters
   - Lead with most important information
   - Do not start with "Image of" or "Photo of"
   - Include any text visible in the image
3. Hashtag recommendations (CamelCase, placed at end)
```

---

## Template 2: Video Post

```
Create an accessible [platform] video post.

Platform: [YouTube | Instagram Reels | TikTok | LinkedIn | Twitter/X]
Video topic: [Describe what the video covers]
Video duration: [Length]
Key spoken content: [Summary of main points, key terms, speaker names]

Please provide:
1. Video caption script
   - Verbatim or clean-edited (specify: [verbatim | clean])
   - Speaker identification for each speaker
   - Sound effects that convey meaning in square brackets [sound effect]
   - Max 32 characters per line, max 2 lines per caption block
   - Format: [SRT | WebVTT | plain text]

2. Post text/description
   - Summary of video content
   - Timestamps/chapters (if YouTube)
   - Links mentioned in video
   - Note if captions are available

3. Thumbnail alt text (if applicable)
   - Describe what appears in the thumbnail
```

---

## Template 3: Platform-Specific Accessible Post

### Twitter/X

```
Write an accessible Twitter/X post about [topic].

Requirements:
- 280 character limit (including spaces)
- CamelCase hashtags at end: #LikeThis not #likethis
- Emoji at end of sentences only, max 2 emoji
- If this post includes an image, provide:
  - Alt text (max 1000 characters)
  - Do not start alt text with "Image of"
  - Include any text visible in the image

Topic: [topic]
Key point: [main message]
Image description (if applicable): [image details]
Hashtags to include: [suggested hashtags in CamelCase]
```

### Instagram

```
Write an accessible Instagram post about [topic].

Requirements:
- Caption: Up to 2,200 characters; hashtags at end
- CamelCase hashtags: #AccessibleDesign not #accessibledesign
- Use line breaks for readability
- Alt text: ~300 characters max for social media convention
  - Do not begin with "Image of" or "Photo of"

Topic: [topic]
Key point: [main message]
Image description: [describe all visual elements, text in image, context]
Target hashtags (CamelCase): [list]
```

### LinkedIn

```
Write an accessible LinkedIn post about [topic] for a professional audience.

Requirements:
- Professional tone
- Plain language (define technical terms)
- 3-5 CamelCase hashtags at end
- If image: alt text (~420 characters)

Topic: [topic]
Audience: [professionals in what field?]
Key insight: [what should readers take away?]
Call to action: [what should readers do?]
Image description (if applicable): [details]
```

---

## Template 4: Alt Text Only

```
Write accessible alt text for this image for use on [platform].

Character limit: [N characters]
Platform: [platform name]
Context: This image will be posted with a caption about [topic].
Purpose of the image in this post: [informative | decorative | functional]

Image details:
- Subject(s): [who/what is in the image]
- Setting/location: [where]
- Action: [what is happening]
- Visible text: [any text in the image — transcribe exactly]
- Colors/style: [relevant visual details]
- Mood/tone: [if relevant to the post]

Requirements:
- Do not start with "Image of" or "Photo of"
- Lead with the most important information
- Be concise: target [N] characters
- Include all visible text from the image
- [If people: describe what is relevant to the post context]
```

---

## Quality Check Prompts

After generating social media content, verify with:

```
Review this social media post for accessibility issues:

Post text: [generated text]
Alt text: [generated alt text]
Platform: [platform]

Check for:
1. Are hashtags in CamelCase?
2. Are emoji placed at end of sentences (not beginning or middle)?
3. Does the alt text start with "Image of" or "Photo of" (should not)?
4. Does the alt text include all visible text from the image?
5. Is the alt text within the [N] character limit for [platform]?
6. Does the post use any ableist language?
7. Are abbreviations spelled out on first use?
8. Is the language at an appropriate reading level?

[Post content and alt text here]
```
