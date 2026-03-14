---
title: "Twitter/X Accessibility Guide"
standard: ""
source_url: "https://help.twitter.com/en/using-x/add-image-descriptions"
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "curated"
last_verified: "2026-03-13"
tags: ["twitter", "x", "alt-text", "captions", "platform", "social-media"]
ai_context: "Platform-specific accessibility guide for Twitter/X. Covers alt text (1000 char limit), video captions, accessible writing. Verify currency — Twitter/X UI changes frequently."
---

# Twitter/X Accessibility Guide

**IMPORTANT:** Twitter/X UI and policies change frequently. Verify current UI flows before providing platform guidance. Last verified: 2026-03-13.

---

## Image Alt Text

### Character Limit
**1,000 characters** (increased from 420 in 2022)

### How to Add Alt Text (Web)
1. Start a new tweet
2. Click the photo icon to attach an image
3. After attaching, click "Add description" below the image thumbnail
4. Enter alt text in the dialog
5. Click "Done"

### How to Add Alt Text (iOS/Android App)
1. Start a new tweet
2. Tap the photo icon and select an image
3. After attaching, tap the image thumbnail
4. Tap "Add alt text" (pencil icon)
5. Enter description
6. Tap "Save"

### AI Auto Alt Text
Twitter/X offers automatic alt text generation via AI:
- Settings → Accessibility, display, and languages → Accessibility → Compose image descriptions → "Automatically generate descriptions"
- AI descriptions are often generic (e.g., "Person smiling" without context)
- Always review and edit AI-generated alt text

### Alt Text Visibility
- Alt text is not shown in the tweet interface to regular users
- Screen reader users and users with image loading disabled see the alt text
- The "ALT" badge appears on images that have alt text (helps sighted users know it's present)
- Some third-party Twitter clients display alt text on hover

### API Alt Text
For posting via API:
```json
{
  "media_id": "12345",
  "alt_text": {
    "text": "Your alt text here (max 1000 characters)"
  }
}
```

---

## Video Captions

### Supported Formats
- **SRT** (.srt)
- **WebVTT** (.vtt)

### How to Upload Captions (Web)
1. Start a tweet with a video
2. After attaching the video, click the "Captions" option
3. Upload your SRT or VTT file
4. Verify captions display correctly in preview

### Auto-Generated Captions
- Twitter/X has auto-caption generation for some videos
- Quality varies; technical terms and proper nouns are error-prone
- Auto-captions cannot be edited before publishing on Twitter/X (download, edit, re-upload as SRT)

### Live Stream Captions
- Twitter/X Spaces: No built-in live captioning as of 2026
- Workaround: Use a third-party live caption service; post a transcript after

---

## Accessible Tweet Writing

### Character Limit Considerations
- Standard: 280 characters (verified accounts may have higher limits)
- URLs count as 23 characters regardless of length
- Images, polls, and cards don't count toward character limit
- Alt text does NOT count toward character limit

### Writing Practices

**CamelCase hashtags:** #AccessibilityMatters, not #accessibilitymatters

**Emoji placement:** Put emoji at end of sentences
```
// Accessible
We're launching our accessible design system today! 🎉

// Inaccessible
🎉 We're launching our accessible design system today!
```

**Avoid emoji as bullets:**
```
// Accessible
Our features:
- Dark mode
- High contrast
- Screen reader support

// Inaccessible
⚫ Dark mode
⬛ High contrast
📖 Screen reader support
```

**Limit emoji count:** 1-3 per tweet max for accessibility

**Spell out abbreviations** on first use in a thread

**Avoid "RT for [cause]"** — engagement bait is often unclear to screen reader users

### Thread Accessibility
- Number tweets: "1/5", "2/5"
- Each tweet should be understandable without reading previous tweets when possible
- Use reply threading, not quote-tweet threading, for accessibility (reply threading maintains thread context in most AT)

---

## Links and URLs

- Twitter/X auto-shortens URLs to t.co links (23 chars)
- Short URLs don't describe destination — use text before the link that describes it
- "Read our accessibility report: [t.co/xxx]" is better than just "[t.co/xxx]"

---

## Polls

Twitter/X polls are keyboard accessible and screen reader friendly.
- Keep option text clear and concise
- Avoid poll options that depend on context not in the tweet

---

## Screen Reader Behavior on Twitter/X

| Element | Screen Reader Announcement |
|---------|---------------------------|
| Image with alt text | "[alt text], image" |
| Image without alt text | "Image" (no description) |
| Video with captions | Captions displayed; no special SR announcement |
| Emoji | Full Unicode name (e.g., "fire" for 🔥) |
| @mention | "at [username]" |
| #hashtag | "[hashtag word]" or spelled-out letters if no CamelCase |
| RT/Retweet | Varies by client |
| Like count | "[number] likes" |

---

## Known Accessibility Issues (as of 2026)

- Tweet compose box: `aria-label` may not be consistently announced across all AT configurations
- Notifications timeline: mixed screen reader support for notification types
- Explore/trending tab: layout changes frequently; screen reader navigation may be inconsistent
- Spaces (audio rooms): limited accessibility features; no live captions
- Communities: same accessibility level as main timeline

---

## Settings for Accessibility

Path: Settings and Support → Settings → Accessibility, display, and languages → Accessibility

Key settings:
- **Increase color contrast** — Higher contrast UI
- **Reduce motion** — Reduces animations
- **Autoplay** — Control auto-playing video (default: On cellular: off, On Wi-Fi: on)
- **Image descriptions** — Auto-generate descriptions setting
- **Keyboard shortcuts** — Enabled by default on web
