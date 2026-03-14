---
title: "Audio Description Guide for Social Media and Web Video"
standard: "WCAG"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html"
domain: ["social-media", "media", "web"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["audio-description", "video", "social-media", "1.2.5", "1.2.3", "accessibility"]
ai_context: "Practical guide to audio description for video content on social media and web. Covers what needs AD, workarounds, and platform support. Load for video accessibility questions."
---

# Audio Description Guide for Social Media and Web Video

---

## What Is Audio Description?

Audio description (AD) is narration added to a video's soundtrack that describes important visual information not conveyed in the main audio — things like on-screen text, speaker identification, actions, and scene changes.

**WCAG requirement:** SC 1.2.5 (Level AA) requires audio description for all pre-recorded video with audio.

---

## What Needs Audio Description

### Requires Description

| Visual element | Example |
|---------------|---------|
| On-screen text not read aloud | "Lower third" name/title labels, URLs, slide text |
| Speaker actions | "The presenter draws a diagram on the whiteboard" |
| Visual demonstrations | Showing steps of a process without verbal narration |
| Key facial expressions conveying meaning | "She shakes her head no" (when spoken audio is ambiguous) |
| Scene changes essential to understanding | "Cut to an exterior shot of the factory floor" |
| On-screen graphics with data | Charts shown without verbal data |

### Does NOT Require Description

| Visual element | Why exempt |
|---------------|-----------|
| Decorative b-roll | Background footage not essential to content |
| Actions already verbally described | "I'm going to click the Settings button" while doing it |
| Speaker's general appearance | Unless appearance is relevant to content |
| Background visuals | Wallpaper, office environment |

---

## Audio Description for Social Media Platforms

### Platform Support Summary (as of 2026)

| Platform | Native AD support | Best workaround |
|----------|-----------------|----------------|
| YouTube | Yes — secondary audio track or separate video | Upload AD audio track |
| Twitter/X | No native AD | Narrate visuals in main audio |
| Instagram | No native AD | Narrate visuals in main audio |
| LinkedIn | No native AD | Narrate visuals in main audio |
| Facebook | No native AD | Narrate visuals in main audio |
| TikTok | No native AD | Narrate visuals in main audio |

---

## Workarounds When Native AD Is Not Supported

### 1. Integrated Description (Best for Short Videos)

The most practical approach for social media: narrate visual content as part of the main audio. Plan for this during production.

**Without AD (fails SC 1.2.5):**
> Visual: Speaker points to a chart labeled "Q4 Results"
> Audio: "As you can see, our results exceeded expectations."

**With integrated description:**
> Audio: "As you can see on this Q4 Results chart — showing 34% year-over-year revenue growth — our results exceeded expectations."

### 2. Separate AD Version

Post two versions: one standard, one with AD audio.

```
Caption/description text:
🔊 Need audio description?
Audio description version: [link to AD version]
```

### 3. AD in Caption/Post Description

For short content, include visual information in the post text below the video.

```
Caption: In this video, I demonstrate the three most common ARIA mistakes.

Key visual details:
- Code editor showing bad example: <div onclick="..."> without role or tabindex
- DevTools panel showing accessibility tree with "generic" role
- Fixed example: <button onclick="..."> with no extra ARIA needed
```

### 4. VoiceOver Narration Built Into Production

When creating video content, build accessibility into the script:
- Read all slide text aloud
- Describe graphs and charts as you show them
- Introduce yourself by name at the start
- Describe your actions as you demonstrate them

---

## Audio Description for YouTube

YouTube has the best AD support of any major platform.

### Option 1: Separate Audio Track

YouTube supports multiple audio tracks (currently in beta for some creators).

### Option 2: Separate Video Upload

1. Create a version with AD integrated into the audio
2. Upload as a separate video
3. In the original video description, link to the AD version
4. Use cards or end screens to link between versions

### Option 3: Add a Described Video as a Playlist

Group the AD version and original in a playlist to keep them together.

---

## Writing Audio Description

### Style Guidelines

- Describe in present tense ("The presenter clicks" not "The presenter clicked")
- Be objective — describe what is seen, not interpretation
- Be concise — fit descriptions in natural pauses
- State the speaker's name when introducing them: "Dr. Maria Chen, Chief Accessibility Officer at Acme Corp"
- Don't describe what can be understood from the audio alone
- Prioritize: most important information first when time is limited

### Reading Rate for AD

Standard recorded AD: approximately 150–180 words per minute. Extended AD (when the video pauses) can be slower and more detailed.

### Voice and Tone

- Match the tone of the original video (formal, conversational, etc.)
- Be neutral and objective
- Use clear, simple language
- Don't editorialize

---

## AD Quality Checklist

- [ ] All on-screen text not read in main audio is described
- [ ] Speaker names and titles provided when shown on screen
- [ ] Key visual demonstrations described in enough detail to follow without sight
- [ ] Scene changes described when relevant to understanding
- [ ] AD does not overlap with main audio (fits in natural pauses or video is paused)
- [ ] Reading pace allows comfortable comprehension
- [ ] Visual descriptions are accurate and objective

---

## Section 508 and AD

Section 508 requires audio description for all pre-recorded videos with audio content used in federal contexts. This applies to:
- Training videos
- Instructional content
- Informational videos on government websites
- Webinar recordings

For federal agencies and contractors, both captions AND audio description are required for pre-recorded video.
