---
title: "Facebook Accessibility Guide"
standard: ""
source_url: "https://www.facebook.com/help/accessibility"
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "curated"
last_verified: "2026-03-13"
tags: ["facebook", "meta", "alt-text", "captions", "reels", "stories", "platform", "social-media"]
ai_context: "Platform-specific accessibility guide for Facebook. Covers alt text, video captions, Reels, and Stories. Verify currency — Facebook UI changes frequently across surfaces."
---

# Facebook Accessibility Guide

**IMPORTANT:** Facebook has multiple content surfaces (Feed, Stories, Reels, Groups, Pages) with varying accessibility features. UI changes frequently with app updates. Last verified: 2026-03-13.

---

## Image Alt Text

### Auto Alt Text

Facebook uses AI (Meta's object detection) to generate automatic alt text for all images. The AI describes objects in images using a standard format: "May be an image of [objects detected]."

Examples of auto alt text:
- "May be an image of 2 people, sky, and grass"
- "May be an image of a person smiling and outdoor"
- "May be an image of text that says 'Opening soon'"

**Limitations:** Auto alt text lacks context about the post's purpose, doesn't describe relationships or activities, and may misidentify people.

### Custom Alt Text — Photo Posts

**Web (facebook.com):**
1. When creating a post, click the photo icon to attach an image
2. After the image loads in the composer, hover over the image
3. Click "Edit" or the pencil icon
4. Click "Alternative Text"
5. The auto-generated text is shown in an "Auto-generated alt text" box
6. Click "Override generated alt text"
7. Enter your custom description
8. Click "Save"

**Facebook App (iOS/Android):**
1. Create a post and attach a photo
2. Tap "Edit" on the photo
3. Tap "Accessibility" or "Alt Text"
4. Enter custom alt text
5. Tap "Done"

### Custom Alt Text — Pages (Professional Accounts)

Page photo alt text works similarly through the compose interface. Facebook Business Suite may have a different workflow.

### Character Limit

Facebook does not publish a hard character limit for alt text. Practical recommendation: 125-420 characters.

---

## Video Captions

### Uploading Captions

**Supported format:** SRT (.srt)

**Web:**
1. After uploading a video in composer, click the video thumbnail
2. Click "Edit video" or the video settings icon
3. Select "Captions"
4. Click "Upload" and select your SRT file
5. The language is detected automatically; confirm or correct
6. Preview and save

**Facebook Pages:** In Creator Studio or Meta Business Suite, more robust captioning options are available.

### Auto-Generated Captions

Facebook generates automatic captions for most videos. To review and edit:
1. Go to the published video
2. Click the three-dot menu (···)
3. Click "Edit video"
4. Click "Captions"
5. Review auto-captions; edit errors
6. Save

### Live Video (Facebook Live)

Facebook Live has automatic captioning available:
- Enable during broadcast setup: "Add captions" option
- Captions appear as overlaid text during the live broadcast
- Auto-captions for the recording are generated after the broadcast ends
- Quality varies; cannot be pre-edited like a recorded video

---

## Reels Accessibility

### Reels Captions
- Facebook Reels have auto-captioning (similar to Instagram Reels, as both are Meta products)
- Edit captions in the Reels creator after recording/uploading
- No SRT upload option for Reels as of 2026

### Reels Alt Text / Thumbnail
- No dedicated alt text for Reels video
- Write descriptive post text to provide context

---

## Stories Accessibility

### Stories Limitations
- No native alt text for Stories images
- No caption upload for Stories video
- Auto-captions available for video Stories in some regions

### Stories Accessibility Workarounds
- Add large, high-contrast text overlays using the Stories text tool
- Include critical information in the Stories caption (tap to see text)
- For video Stories: use the auto-caption sticker if available

---

## Accessible Post Writing for Facebook

### Post Text
- Facebook posts can be long (up to 63,206 characters); use structure for readability
- Use paragraph breaks — blank line between paragraphs
- Line breaks aid screen reader navigation
- Don't rely on visual formatting in images; repeat key information in post text

### Hashtags
- CamelCase: #AccessibilityMatters not #accessibilitymatters
- Hashtags are less critical for Facebook reach than on Instagram
- 1-3 hashtags per post is standard for Facebook

### Links
- Facebook de-prioritizes posts with external links in the algorithm
- Some organizations post link in comments rather than the post body
- Either way, ensure linked page is accessible

---

## Facebook Groups and Pages

### Group Posts
- Same alt text and caption features as personal feed posts
- Group admins can enforce alt text as a community standard (not technically enforced by platform)

### Facebook Pages (Business)
- More captioning options through Meta Business Suite / Creator Studio
- Can schedule posts with captions
- Bulk video caption management

---

## Accessibility Settings on Facebook

Path: Settings → Accessibility

Available settings:
- **Automatic Alt Text** — Turn on/off platform's AI alt text generation
- **Profile video** — Accessibility options for profile videos
- **Motion and moving things** — Reduce or remove motion effects
- **Large text** — Increase text size in the app

---

## Known Accessibility Issues (as of 2026)

- **Stories:** No built-in alt text or caption upload
- **Reels:** No SRT upload; auto-captions only
- **Messenger:** Varied accessibility across features
- **Marketplace:** Limited alt text support for listing images
- **Live video:** Auto-captions not available in all regions
- **React emoji reactions:** Screen reader support has improved but varies
- **Watch parties / group video:** Limited captioning in collaborative watch features
