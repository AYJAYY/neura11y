---
title: "YouTube Accessibility Guide"
standard: ""
source_url: "https://support.google.com/youtube/answer/2734796"
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "curated"
last_verified: "2026-03-13"
tags: ["youtube", "captions", "audio-description", "chapters", "platform", "social-media"]
ai_context: "Platform-specific accessibility guide for YouTube. Covers captions (upload and auto), audio descriptions, chapters, and video descriptions. The most mature platform for captioning."
---

# YouTube Accessibility Guide

YouTube has the most mature accessibility tools of any major social media platform, particularly for captions.

---

## Captions on YouTube

### Auto-Generated Captions

YouTube's automatic speech recognition (ASR) generates captions for most videos. ASR quality:
- **Accuracy:** 80–95% for clear speech, standard accent, low background noise
- **Error rate:** Higher for technical terms, proper nouns, non-English accents, poor audio
- **Availability:** Appears in YouTube Studio after processing (varies by video length)

**Auto-captions are NOT sufficient without review** for important content. They satisfy the "captions exist" criterion but often have errors that mislead.

### Uploading Manual Captions (Recommended)

Supported formats:
- `.srt` (SubRip) — Most common
- `.sbv` (SubViewer) — YouTube's native format
- `.vtt` (WebVTT) — Web standard
- `.ass` / `.ssa` — Advanced SubStation Alpha
- `.mpsub`, `.lrc` — Other formats

#### How to Upload Captions (YouTube Studio)

1. Go to YouTube Studio (studio.youtube.com)
2. Select "Content" from the left menu
3. Click the video you want to caption
4. Click "Subtitles" from the left menu
5. Click "Add" next to the language
6. Choose "Upload file"
7. Select your SRT/VTT file
8. Click "Save"

#### Auto-Sync Feature

If you have a transcript but no timestamps, YouTube can auto-sync:
1. In Subtitles menu, click "Add" → "Auto-sync"
2. Paste your plain text transcript
3. YouTube aligns timing automatically
4. Review sync accuracy and correct any errors

### Editing Captions in YouTube Studio

1. In Subtitles menu, click the pencil icon for the caption track
2. Video editor opens with caption timeline
3. Click any caption block to edit text
4. Drag blocks to adjust timing
5. Click "Publish" to save

### Reviewing Auto-Generated Captions

1. Open the video
2. Click CC button to verify auto-captions are present
3. In YouTube Studio → Subtitles, click the auto-generated track
4. Review in editor; correct errors in order of severity:
   - Proper nouns and names (highest error rate)
   - Technical terminology
   - Misheard words that change meaning
   - Punctuation (affects readability)

---

## Audio Descriptions

YouTube does not have a native audio description track feature. Workarounds:

### Approach 1: Separate AD Video

Create a separate video version with audio description narration mixed into the main audio:
1. Record audio description narration covering visual information
2. Mix AD narration with original audio (or use pauses for standard AD)
3. Upload as a separate unlisted/public video
4. Link the AD version in the video description

### Approach 2: Extended Audio Description

For extended audio description (video pauses while description plays):
1. Pause video at key visual moments
2. Insert AD narration during the pause
3. Resume video

### YouTube Audio Description Playlist

Create a playlist pairing original and AD versions:
- Playlist title: "[Video Name] — Including Audio Description"
- Pin the playlist link in the description of the original video

---

## Video Chapters

Chapters create navigable timestamps in the video progress bar and description.

### Accessibility Benefit

Chapters allow:
- Keyboard navigation to specific sections without scrubbing
- Screen reader navigation: YouTube reads chapter names when user scrubs
- Table of contents in description for text-based navigation

### How to Add Chapters

In the video description, add timestamps in this format:
```
0:00 Introduction
1:30 What is WCAG?
5:45 Level A Requirements
12:00 Level AA Requirements
18:30 How to Test
22:00 Summary and Resources
```

Rules:
- First timestamp must be 0:00
- At least 3 timestamps required for chapters to activate
- Format: `M:SS` or `H:MM:SS`
- Each timestamp followed by a space and chapter name

---

## Video Description Accessibility

The video description is indexed and read by screen readers. Best practices:

1. **Repeat the video title** in the first line of description
2. **Summarize key content** — Some users read descriptions before deciding to watch
3. **Include all links mentioned** — Viewers can't click what you say in a video
4. **Add chapter timestamps** — See above
5. **Include a transcript** — Either inline or linked
6. **Note accessibility features:** "This video includes captions and audio description"
7. **Credit music** — Titles, artists, and licensing

### Transcript in Description

For short videos (under 5 minutes), embedding the full transcript in the description is practical:

```
TRANSCRIPT:
Hi, welcome to our tutorial on web accessibility.
In this video, we'll cover...
```

For longer videos, link to a transcript document.

---

## Thumbnails

Video thumbnails are images without alt text on the YouTube platform. Best practices:
- Ensure text in thumbnails is large and high contrast (4.5:1 minimum)
- Don't rely on thumbnail text to convey essential information not in the video title
- YouTube's thumbnail alt text defaults to the video title — make titles descriptive

---

## YouTube Studio Accessibility Features

### Subtitle/Caption Settings (Studio)

- Review and edit auto-captions
- Add manual caption tracks
- Add translated subtitles
- Set default caption track

### Community Contributions (Deprecated)

YouTube removed community-contributed captions in 2020. Third-party contributions are no longer possible.

---

## Playlist Accessibility

1. Use descriptive playlist names and descriptions
2. Order videos logically (by date, topic progression, etc.)
3. Enable captions for all videos in series playlists
4. Mark playlists with content type in title when helpful: "[Course] Introduction to Web Accessibility"

---

## Live Streams

### Live Captions
- YouTube offers automatic live captions during streams
- Quality is lower than post-processing auto-captions
- For professional/educational live content: use a CART provider and integrate via encoder or OBS

### Post-Stream
- After a live stream ends, auto-captions generate (same as regular videos)
- Edit and publish clean captions on the recording

---

## YouTube Accessibility Settings (Viewer Side)

Viewers can:
- Toggle CC on/off
- Resize and style captions (in YouTube settings)
- Set default caption language
- Choose caption background color and opacity
- Set caption font size (up to 400% of default)

These viewer-controlled settings are why caption styling in uploaded files is often unnecessary — viewers can customize.
