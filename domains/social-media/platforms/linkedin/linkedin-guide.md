---
title: "LinkedIn Accessibility Guide"
standard: ""
source_url: "https://www.linkedin.com/help/linkedin/answer/a536441"
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "curated"
last_verified: "2026-03-13"
tags: ["linkedin", "alt-text", "captions", "platform", "social-media"]
ai_context: "Platform-specific accessibility guide for LinkedIn. Covers alt text for images, video captions, accessible post writing."
---

# LinkedIn Accessibility Guide

---

## Image Alt Text

### Character Limit
No published hard character limit. LinkedIn recommends keeping descriptions concise. Practical maximum: ~420 characters (similar to Twitter's original limit).

### How to Add Alt Text — New Post

**Web:**
1. Start a new post
2. Click the image icon and attach an image
3. After image loads in composer, click "Edit" or the pencil icon on the image
4. Click "Add alt text"
5. Enter description in the text field
6. Click "Save"

**Mobile (iOS/Android):**
1. Start a new post, tap the image icon
2. After attaching, tap the image in the composer
3. Tap "Add alt text" option
4. Enter description
5. Tap "Done"

### Multiple Images
LinkedIn allows up to 20 images in a post. Add alt text to each image individually through the same process.

### Document Posts (LinkedIn Articles / PDF Carousels)

LinkedIn allows posting PDFs as "document" posts (carousel-style swipe-through):
- The PDF itself must be accessible (PDF/UA or well-tagged)
- Add a summary in the post text of key content from the document
- LinkedIn does not support alt text per-page for document carousels

---

## Video Captions

### Supported Format
- **SRT** (.srt) only

### How to Upload Captions — New Video Post

1. Start a new post, attach a video file
2. In the video preview, click "Cc" or "Add captions"
3. Upload your SRT file
4. Preview and verify timing
5. Post

### How to Add Captions — Existing Video Post

LinkedIn does not currently allow adding captions to already-published videos. Re-upload the video with captions if needed.

### Auto-Generated Captions
LinkedIn does not provide auto-caption generation for regular posts as of 2026.

### LinkedIn Live

LinkedIn Live (streaming) does not provide native live captioning. Use CART integration through your streaming encoder.

---

## Articles and Long-form Posts

### LinkedIn Articles (Long-form)

LinkedIn Articles have a rich text editor. Accessibility best practices:
- Use heading styles (H1, H2, H3) from the toolbar — don't use bold text as headings
- Add alt text to all images inserted in articles (right-click image → Edit alt text)
- Use descriptive link text (not "click here")
- Use the ordered/unordered list tools for lists
- Ensure sufficient text contrast if using colored text

### Newsletter Posts

LinkedIn Newsletters follow the same rules as Articles. Alt text for images and proper heading hierarchy are particularly important as newsletters are delivered to subscriber emails.

---

## Profile Accessibility

### Profile Photo
LinkedIn auto-generates alt text for profile photos. Custom alt text is not currently available for profile photos.

### Cover Photo / Background Image
No alt text for background images on profiles.

### Recommendations
- Keep profile name and headline clear and descriptive
- Job title and company in headline (not emoji-heavy descriptions)
- Featured section: add descriptive text alongside any images

---

## Accessible Post Writing

### Professional Tone and Plain Language
LinkedIn's audience generally tolerates more formal/technical language than consumer social platforms. However:
- Define technical acronyms on first use
- Break up long posts with line breaks
- Use numbered lists for multi-step processes

### Hashtag Practice
- CamelCase: #AccessibilityMatters, not #accessibilitymatters
- LinkedIn hashtags are less critical for reach than on Instagram
- 3-5 relevant hashtags at post end is standard

### Links in Posts
LinkedIn limits post reach for external links (the algorithm deprioritizes posts that take users off the platform). Options:
- Post without a link; add in first comment
- Include the URL in the post text (less algorithmic penalty than a preview card)
- Use descriptive text before any URL

### @Mentions
Mentions are read by screen readers as "@[name]". Keep mentions purposeful; avoid tagging people just for engagement.

---

## Known Accessibility Issues (as of 2026)

- **Document carousel posts:** No per-page alt text; alt text only on the cover
- **Profile background photo:** No alt text support
- **LinkedIn Live:** No auto-captioning
- **Stories (if active on account):** Limited accessibility compared to other platforms
- **Reactions:** Emoji reactions are accessible (screen readers announce reaction type)
- **Poll options:** Polls are generally keyboard accessible; option text should be descriptive
