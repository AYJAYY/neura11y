---
title: "Mastodon Accessibility Guide"
standard: ""
source_url: "https://docs.joinmastodon.org/"
domain: ["social-media"]
last_verified: "2026-03-13"
status: "curated"
tags: ["mastodon", "fediverse", "alt-text", "content-warning", "platform", "social-media"]
ai_context: "Platform-specific accessibility guide for Mastodon. Covers alt text (1500 char limit), content warnings, accessible writing. Mastodon has strong accessibility culture."
---

# Mastodon Accessibility Guide

Mastodon is part of the federated Fediverse network. Accessibility practices are a strong cultural norm in the Mastodon community, with some instances enforcing alt text as a requirement for image posts.

---

## Image Alt Text

### Character Limit
**1,500 characters** — The most generous of any major social platform.

### How to Add Alt Text

**Web (mastodon.social and most instances):**
1. Compose a new post
2. Attach an image using the paperclip/image icon
3. After image loads, click "Edit" or the pencil icon on the image thumbnail
4. Enter alt text in the text field
5. Click "Apply"

**Mastodon Apps (iOS/Android):**
Most apps support alt text:
- **Ivory (iOS):** Tap the image after attachment; "Alt Text" field appears
- **Elk (web):** Tap edit button on image thumbnail
- **Ice Cubes (iOS):** Tap image → "Edit Media"
- **Fedilab (Android):** Long press on attached image

### Alt Text Culture on Mastodon

- Many Mastodon users will not boost/reblog posts without alt text on images
- Some instances have bots (e.g., @alt_text_reminder) that remind users to add alt text
- The community treats alt text as basic courtesy, not optional
- Some instance moderators will ask users to add alt text to posts

### Image Visibility Settings

Images can be marked as "sensitive" (content warning for visual content), which hides them behind a click/tap. This is separate from alt text.

---

## Content Warnings (CW)

Mastodon's content warning feature is unique among major social platforms.

### What CW Does

- Hides the post body behind a "Show more" button
- Shows only the CW summary text by default
- Images attached to a CW post are automatically marked sensitive

### When to Use CW

Mastodon community norms for using content warnings:

| Content | CW Convention |
|---------|---------------|
| Flashing images / GIFs | "flashing images" or "gif with motion" |
| Mental health content | "mental health", "depression", "anxiety" |
| Violence or gore | "violence", "blood" |
| Death or injury news | "death", "injury" |
| Political content (on some instances) | "politics", "uspol", "ukpol" |
| Food photos (on some instances) | "food" |
| Spoilers | "[Show Name] spoilers" |
| NSFW content | "NSFW" |
| Trauma/abuse topics | "abuse cw", "trauma" |
| Medical content | "medical", "health" |

CW norms vary by instance. Check your instance's community guidelines.

### CW Format

The summary text should clearly describe what the post contains so users can make an informed choice to expand it.

```
CW: Flashing gif, accessibility discussion

[Post body with the flashing content and discussion]
```

### Accessibility Value of CW

- Users with photosensitive epilepsy can avoid flashing content
- Users managing trauma triggers can choose when to engage
- Users with cognitive disabilities can limit unexpected content
- Mental health content can be filtered from feeds

---

## Video Captions

Mastodon supports video uploads but has limited captioning features:
- No built-in auto-captioning
- Some apps support embedding VTT/SRT directly in video files
- Best practice: burn captions into the video before uploading
- Or provide a text transcript in the post body

---

## Accessible Post Writing

### Post Length
Default character limit: **500 characters** (most instances). Some instances allow much longer posts.

### Hashtags
- CamelCase is especially important on Mastodon
- Hashtags are the primary discovery mechanism on the federated timeline
- Use 5-8 relevant hashtags per post for discoverability
- Federated timeline browsing depends on hashtags
- Example: `#Accessibility #A11y #WebDev #WCAG #InclusiveDesign`

### Thread Accessibility
- Number toots: "1/5", "2/5"
- Use "reply" to thread (not quote-post)
- End threads with "End." or "/end"

### Content Formatting
- Line breaks work well in Mastodon posts
- No markdown support in most clients (some custom CSS)
- Use plain text formatting: dashes for bullets, numbers for lists

---

## Instance-Specific Considerations

Mastodon is federated — accessibility features and expectations vary by instance:

| Instance Type | Accessibility Notes |
|---|---|
| Mastodon.social (flagship) | Standard features; large user base |
| Fosstodon.org | Tech-focused; strong alt text culture |
| Scholar.social | Academic focus; detailed alt text expected |
| Disabled.social | Disability-focused; alt text strongly enforced |
| Aus.social | AU accessibility community active |

Some instances have server-side settings that:
- Require alt text before posting
- Add reminder notices if images lack alt text
- Filter content without CW from local timeline

### Checking Your Instance's Guidelines

Look for your instance's "About" or "Rules" page:
```
https://[your-instance]/about
```

---

## Mastodon Accessibility Settings

Settings → Preferences → Appearance:
- **Reduce motion:** Limits animation in the web interface
- **Disable swiping motions:** Accessibility option for some clients
- **Slow mode:** In some instances, limits fast-moving feeds

Settings → Filters:
- Create content filters to hide specific words/phrases from your timeline
- This is a personal accessibility tool for managing information overload or trauma triggers
