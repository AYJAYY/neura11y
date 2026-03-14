---
title: "Caption Writing Guide for Social Media"
standard: "WCAG 2.2 SC 1.2.2"
source_url: "https://www.w3.org/TR/WCAG22/#captions-prerecorded"
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["captions", "video", "1.2.2", "social-media", "srt", "webvtt", "quality"]
ai_context: "Guide to writing and implementing quality captions for social media video. Covers caption quality standards, SRT/VTT format, speaker identification, and audio descriptions."
---

# Caption Writing Guide for Social Media

---

## Captions vs. Subtitles

| Feature | Captions | Subtitles |
|---------|---------|----------|
| Purpose | Accessibility for deaf/HoH | Translation for hearing viewers |
| Content | Dialogue + sound effects + music | Dialogue only |
| Assumption | Viewer cannot hear audio | Viewer can hear but not understand language |
| WCAG SC | 1.2.2 (required) | Not required by WCAG |

Always use "captions" (not "subtitles") when the content is meant to make audio accessible. The terms are often conflated in platform UIs.

---

## Who Uses Captions

- People who are deaf or hard of hearing (primary accessibility use)
- People watching in loud environments (commuting, gym)
- People in quiet environments (offices, libraries, without headphones)
- Non-native speakers of the content language
- People with auditory processing disorders
- People who are learning to read or have reading disabilities (captions help reinforce audio)
- Estimated 80%+ of caption usage is by hearing viewers (per research)

---

## WCAG Requirements

**SC 1.2.2 — Captions (Prerecorded) — Level A:** Captions for all prerecorded audio content in synchronized media.

**SC 1.2.4 — Captions (Live) — Level AA:** Live captions for all live audio content in synchronized media.

**Key point:** Automated/AI-generated captions are NOT sufficient to satisfy SC 1.2.2 without human review and correction. They are a starting point only.

---

## Caption Quality Standards

### Verbatim vs. Edited Captions

- **Verbatim:** Transcribes every word spoken, including filler words ("um", "uh"), false starts
  - Required for legal/news/educational content
  - Harder to read; can be overwhelming

- **Edited/Clean:** Removes filler words, corrects minor grammar, condenses without changing meaning
  - Preferred for social media and general video content
  - Improves readability without losing meaning

### Required Elements

1. **All dialogue** — Every word spoken by every speaker
2. **Speaker identification** — When multiple speakers: "[SPEAKER NAME]: text" or `[NAME]`
3. **Sound effects** — Non-speech audio that conveys meaning: `[doorbell]`, `[explosion]`, `[laughter]`
4. **Music** — When music is meaningful: `[upbeat music playing]`, `[piano melody]`
5. **Tone/manner** — When not apparent from content: `[whispering]`, `[shouting]`, `[sarcastically]`

### What NOT to Include

- Pure background noise that doesn't convey meaning
- Every utterance of filler words (in edited captions)
- Visual descriptions (those belong in audio description, not captions)

---

## Caption Formatting Standards

### Line Length

- Maximum: **32 characters** per line (recommended by BBC, Netflix standards)
- Industry allows up to 42 characters, but shorter is more readable
- Never split a line mid-word

### Lines Per Caption Block

- Maximum: **2 lines** per caption block
- Prefer 1 line for short dialogue

### Duration

- Minimum: **1 second** per caption block (enough to register)
- Maximum: **7 seconds** per caption block
- Match caption timing to when words are spoken (not before or after)

### Timing Synchronization

- Captions should appear within **100 milliseconds** of the corresponding audio
- Don't pre-cue captions before words are spoken
- Don't let captions linger after words are spoken

### Line Break Rules

- Break at natural speech pause: end of sentence, clause
- Do not break: subject from verb, verb from object, preposition from its object
  - **Wrong:** "The quick brown fox / jumped over the fence"
  - **Right:** "The quick brown fox jumped / over the fence"

---

## SRT Format

SRT (SubRip Text) is the most widely supported caption format.

```
[sequence number]
[HH:MM:SS,mmm] --> [HH:MM:SS,mmm]
[Caption text line 1]
[Caption text line 2 if needed]
[blank line]
```

### SRT Example

```
1
00:00:00,000 --> 00:00:02,500
Welcome to our accessibility tutorial.

2
00:00:02,700 --> 00:00:05,200
Today we'll cover three key topics:

3
00:00:05,200 --> 00:00:08,000
alt text, captions, and color contrast.

4
00:00:09,500 --> 00:00:12,000
[door opens]

5
00:00:12,000 --> 00:00:15,500
[NARRATOR]: Before we begin,
let's review the basics.
```

### SRT Rules

- Sequence numbers start at 1 and increment
- Timestamp format: HH:MM:SS,mmm (note comma, not period, for milliseconds)
- Single blank line between blocks
- No styling markup in SRT (use WebVTT for styling)

---

## WebVTT Format

WebVTT (Web Video Text Tracks) is the web standard format, used with HTML5 `<track>` element.

```
WEBVTT

[optional NOTE comments]

[optional cue identifier]
[HH:MM:SS.mmm] --> [HH:MM:SS.mmm] [optional settings]
[Caption text]
```

### WebVTT Example

```
WEBVTT

NOTE Created for ACME Accessibility Tutorial

intro
00:00:00.000 --> 00:00:02.500
Welcome to our accessibility tutorial.

00:00:02.700 --> 00:00:05.200
Today we'll cover three key topics:

00:00:05.200 --> 00:00:08.000
alt text, captions, and color contrast.

00:00:09.500 --> 00:00:12.000
<v Narrator>Before we begin,
let's review the basics.
```

### WebVTT vs. SRT

| Feature | WebVTT | SRT |
|---------|--------|-----|
| Millisecond separator | Period (.) | Comma (,) |
| Voice tags | `<v SpeakerName>` | N/A |
| Bold/italic | `<b>`, `<i>` | N/A |
| Ruby text | Yes | No |
| Position/align settings | Yes | No |
| HTML5 `<track>` | Yes | Browser dependent |
| Platform support | Most | Universal |

---

## Speaker Identification

When multiple speakers appear in a video:

```
[JANE]: I think the new design is more accessible.

[MIKE]: Agreed. The color contrast has improved significantly.
```

Or in VTT voice tags:
```
<v Jane>I think the new design is more accessible.

<v Mike>Agreed. The color contrast has improved significantly.
```

Rules:
- Identify speaker on first appearance of their dialogue
- Re-identify when speaker changes after a gap of > 5 seconds
- Use consistent names throughout

---

## Sound Effects and Non-Dialogue Audio

```
[applause]
[phone ringing]
[elevator ding]
[crowd cheering]
[dramatic music building]
[notification sound]
[thunder]
[baby laughing]
```

Format: Lowercase description in square brackets. Be specific when the sound is meaningful.

For music:
- `[upbeat electronic music playing]` — enough for most contexts
- `[♪ song title by artist ♪]` — when the specific song is meaningful (news segment, music video)

---

## Auto-Caption Review Workflow

1. **Enable auto-captions** on your platform
2. **Wait for processing** (5–30 minutes typically)
3. **Download the auto-generated file** if possible (SRT)
4. **Review and correct:**
   - Names (proper nouns are most error-prone)
   - Technical terminology
   - Homophones
   - Punctuation and capitalization
   - Timing synchronization
5. **Upload corrected file** or edit in platform's caption editor
6. **View captions on video** in a different browser session to verify

### Common Auto-Caption Errors

- Proper nouns and names: "Accessibility" → "a sex ability"
- Technical terms: "ARIA" → "area" or "aria" (correct but wrong context)
- Homophones: "there" / "their" / "they're"
- Missing punctuation causing run-on sentences
- Speaker cross-talk incorrectly transcribed
- Background noise mistranscribed as words

---

## Audio Description

Audio description is narration of visual content not conveyed in the existing audio track. It is separate from captions.

**WCAG SC 1.2.5 (Level AA):** Audio description for prerecorded video.

Social media platform support for audio description:
- No major platform provides native audio description track support as of 2026
- Workaround: Create a separate version of the video with audio description mixed into the main audio track

Audio description should include:
- Scene changes and new locations
- Actions not mentioned in dialogue
- Text appearing on screen
- Facial expressions and gestures when relevant to meaning

---

## Caption Editing Tools

| Tool | Type | Cost |
|------|------|------|
| CapCut | App (iOS/Android/desktop) | Free / paid |
| Descript | Desktop/web | Paid |
| Rev | Professional service | Per-minute fee |
| Otter.ai | Web/mobile | Free tier + paid |
| YouTube Studio | Web (for YouTube) | Free |
| Kapwing | Web | Free tier + paid |
| 3Play Media | Professional service | Paid |
| Verbit | Professional service | Paid |
