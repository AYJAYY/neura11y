---
title: "Instagram Accessibility Guide"
standard: ""
source_url: "https://help.instagram.com/503708446705527"
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "curated"
last_verified: "2026-03-13"
tags: ["instagram", "alt-text", "captions", "reels", "platform", "social-media"]
ai_context: "Platform-specific accessibility guide for Instagram. Covers alt text for feed posts and carousels, Reels captions, Stories. Verify currency — Instagram UI changes frequently."
---

# Instagram Accessibility Guide

**IMPORTANT:** Instagram UI changes frequently with app updates. Verify current workflows before providing guidance. Last verified: 2026-03-13.

---

## Image Alt Text

### What Instagram Supports
- Alt text on single image posts
- Alt text on each image in carousel/gallery posts (each image separately)
- Alt text on video thumbnails (limited)

### Auto Alt Text
Instagram automatically generates alt text using AI (launched 2018). The AI describes objects in images but lacks context about the post topic.

Auto alt text is often generic: "Photo by [username]" or "May be an image of [objects]"

**Always write custom alt text** for important content.

### Character Limit
No published hard character limit for custom alt text. AI auto-text is typically under 100 characters. Practical recommendation: ~125 characters for social media conventions; up to 300 for complex images.

### How to Add Alt Text — New Post

**iOS:**
1. Select image and edit
2. Tap "Next" to caption screen
3. Scroll down, tap "Advanced Settings"
4. Tap "Write Alt Text"
5. Enter description
6. Tap "Done"

**Android:**
1. Select image and edit
2. Tap "Next" to caption screen
3. Tap "Advanced Settings"
4. Tap "Add Alt Text"
5. Enter description
6. Tap "Save"

**Web (instagram.com):**
1. Create new post
2. On caption/location screen, click "Accessibility"
3. Click "Write alt text" under the image
4. Enter text
5. Click "Done"

### How to Edit Alt Text — Existing Post

1. Open the post
2. Tap the three-dot menu (···)
3. Tap "Edit"
4. Tap "Edit Alt Text" (bottom of the image, or in Advanced Settings)
5. Update text and save

### Carousel Posts

Each image in a carousel gets individual alt text.
- Add alt text to each image separately during the posting process
- Alt text is added per-image in the "Advanced Settings" → "Alt Text" for each image in the carousel

---

## Reels Captions

### Auto-Generated Captions
Instagram auto-generates captions for Reels:
- Toggle on during reel creation: "Captions" option in the editing screen
- Style options include font, color, and position customization
- Auto-captions can be reviewed and edited before publishing

### Editing Auto-Captions
1. After recording/uploading reel
2. Tap "Captions" in the editing tools
3. Toggle captions on
4. Review auto-generated text
5. Tap any word to edit it
6. Tap words marked uncertain (often highlighted) and correct them

### Reels Caption Quality
- Instagram auto-captions are AI-generated
- Accuracy varies; technical terms, names, and accents are error-prone
- Always review before publishing
- There is no option to upload an SRT file for Reels as of 2026

### Caption Styling
- Choose high-contrast text styles for readability
- Avoid placing captions where they overlap with important visual content
- Test caption visibility against varied video backgrounds

---

## Stories Accessibility

### Stories Limitations
- No native alt text for Stories images
- No caption upload for Stories video
- Stories disappear after 24 hours (saved to Highlights)

### Stories Accessibility Workarounds
- **Text overlay:** Add text in Stories editor describing the visual content
- **Stickers:** Use Instagram's built-in text sticker for important information
- **Question sticker:** If asking a question, ensure the question text is readable, not just implied by the image
- **For video stories:** Enable automatic captions in the Stories creator

### Auto-Captions in Stories (Video)
1. Create or upload a video Story
2. Tap the sticker icon
3. Select "Captions" sticker
4. Instagram generates captions automatically
5. Review and edit as needed
6. Position captions away from other overlays

---

## Caption/Post Text Accessibility

### Hashtag Placement
Put hashtags at the end of your caption, after the main content:
```
Your accessible post content here, describing what you're sharing
and why it matters.

#Accessibility #InclusiveDesign #A11y
```

Some accounts put hashtags in the first comment instead of the caption — this is accessible either way, since screen readers can navigate to comments.

### Emoji in Captions
- Place emoji at the end of sentences
- Don't use emoji as bullet points
- Screen readers read full emoji names (🔥 = "fire")
- Limit to 1-3 emoji for meaningful content

### Line Breaks
Instagram allows line breaks in captions. Use them for readability:
- Blank line between paragraphs
- Short lines of text are easier to read

### ALT text in Caption
If you cannot add alt text through the interface, you can include an image description in the caption:
```
[Image description: Two women examining accessibility audit results on a laptop screen, sitting at a conference table]

Our latest audit revealed 3 critical accessibility issues...
```

This is a workaround, not a replacement for proper alt text.

---

## Known Accessibility Limitations

- **No SRT upload for Reels** — Only auto-generated captions
- **Stories have no alt text** — Text overlay is the workaround
- **Live video** — No live captioning (third-party CART not integrable)
- **Auto-generated alt text** — Often generic and context-free
- **Story polls/quizzes** — Limited screen reader support
- **Link in bio** — Only one link natively; Linktree-style tools add complexity for AT users
- **Shopping tags** — Screen reader support varies
