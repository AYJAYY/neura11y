---
title: "Video Captions and Audio Description Guide"
standard: "WCAG"
source_url: "https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html"
domain: ["web", "media", "social-media"]
last_fetched: "2026-03-13"
status: "prescriptive"
tags: ["captions", "audio-description", "webvtt", "srt", "video", "1.2.2", "1.2.5"]
ai_context: "Complete guide to video captions and audio description including WebVTT format, SRT format, quality standards, and platform requirements. Load for any video accessibility question."
---

# Video Captions and Audio Description Guide

---

## WCAG Requirements for Video

| SC | Requirement | Level | Applies To |
|----|------------|-------|-----------|
| 1.2.1 | Audio-only and video-only: transcript OR description | A | Pre-recorded |
| 1.2.2 | Captions | A | Pre-recorded video+audio |
| 1.2.3 | Audio description OR media alternative | A | Pre-recorded video+audio |
| 1.2.4 | Captions (live) | AA | Live video |
| 1.2.5 | Audio description | AA | Pre-recorded video+audio |
| 1.2.6 | Sign language | AAA | Pre-recorded |
| 1.2.7 | Extended audio description | AAA | Pre-recorded |
| 1.2.8 | Media alternative (text) | AAA | Pre-recorded |
| 1.2.9 | Audio-only (live) | AAA | Live |

**For most organizations targeting current WCAG Level AA:**
- Pre-recorded video with audio: captions (1.2.2) + audio description (1.2.5)
- Live video: captions (1.2.4)

---

## Captions vs. Subtitles

| Feature | Captions | Subtitles |
|---------|----------|-----------|
| Includes non-speech audio | Yes (`[applause]`, `[phone rings]`) | No |
| Intended audience | Deaf/hard of hearing + others | Hearing viewers in a different language |
| WCAG requirement | Yes (1.2.2) | No |
| Same-language text | Yes | Usually translation |

---

## Caption Quality Standards

### Accuracy

- Verbatim transcription (word-for-word) for most content
- Paraphrasing allowed only when verbatim is technically impossible (rapid speech)
- Names spelled correctly
- Technical terms accurate
- Industry target: ≥98% accuracy

### Timing

- Captions synchronized within 2 seconds of speech
- Short enough duration that text can be read before changing
- Minimum display time: 1.5 seconds per caption block
- Maximum: 7 seconds per caption block

### Readability

- Maximum 32 characters per line
- Maximum 2 lines per caption block
- Break lines at grammatical boundaries (not mid-phrase)

### Speaker Identification

When multiple speakers appear or when speaker is off-screen:
```
[John]: Good morning, everyone.
[Mary]: Thanks for joining us today.
```

Or use descriptive labels:
```
[Narrator]: The following footage was captured in 2019.
[Interviewer]: How did you feel when it happened?
```

### Non-Speech Audio

Include sound effects that are meaningful to understanding content:
```
[upbeat music playing]
[phone ringing]
[door slams]
[audience laughing]
[explosion in distance]
```

Do NOT include every background sound — only sounds meaningful to understanding.

---

## WebVTT Format

WebVTT (Web Video Text Tracks) is the web standard for captions on the web. Used with the HTML `<track>` element.

### Basic Structure

```
WEBVTT

00:00:01.000 --> 00:00:04.500
Welcome to our accessibility tutorial.

00:00:05.000 --> 00:00:09.000
Today we'll cover the key principles
of creating accessible web content.

00:00:10.500 --> 00:00:13.000
[Upbeat music playing]

00:00:14.000 --> 00:00:18.000
[Narrator]: Let's start with the
most fundamental principle: structure.
```

### Timestamp Format

```
HH:MM:SS.mmm --> HH:MM:SS.mmm
```

- HH: hours (optional if 0)
- MM: minutes (00–59)
- SS: seconds (00–59)
- mmm: milliseconds (000–999)

### WebVTT with Positioning

```
WEBVTT

00:00:01.000 --> 00:00:05.000 position:10% align:left
Text in bottom-left of video.

00:00:06.000 --> 00:00:10.000 position:90% align:right
Text in bottom-right of video.
```

### WebVTT Cue Identifiers

```
WEBVTT

intro
00:00:01.000 --> 00:00:04.500
Welcome to our tutorial.

greeting
00:00:05.000 --> 00:00:08.000
Good to have you here.
```

---

## SRT Format

SRT (SubRip Text) is widely supported across platforms (YouTube, Vimeo, Twitter/X, LinkedIn, etc.).

### Basic Structure

```
1
00:00:01,000 --> 00:00:04,500
Welcome to our accessibility tutorial.

2
00:00:05,000 --> 00:00:09,000
Today we'll cover the key principles
of creating accessible web content.

3
00:00:10,500 --> 00:00:13,000
[Upbeat music playing]

4
00:00:14,000 --> 00:00:18,000
[Narrator]: Let's start with structure.
```

**Key difference from WebVTT:** Milliseconds separated by comma (`,`) not period (`.`). Each caption block has an integer sequence number.

---

## Converting Between Formats

Simple conversion (no positioning):

```python
import re

def srt_to_vtt(srt_content):
    """Convert SRT to WebVTT format."""
    vtt = "WEBVTT\n\n"
    # Replace comma millisecond separator with period
    vtt += re.sub(r'(\d{2}:\d{2}:\d{2}),(\d{3})', r'\1.\2', srt_content)
    # Remove sequence numbers
    vtt = re.sub(r'^\d+\n', '', vtt, flags=re.MULTILINE)
    return vtt

def vtt_to_srt(vtt_content):
    """Convert WebVTT to SRT format."""
    # Remove WEBVTT header
    srt = re.sub(r'^WEBVTT.*\n\n', '', vtt_content)
    # Replace period millisecond separator with comma
    srt = re.sub(r'(\d{2}:\d{2}:\d{2})\.(\d{3})', r'\1,\2', srt)
    # Add sequence numbers
    lines = srt.strip().split('\n\n')
    numbered = [f"{i+1}\n{block}" for i, block in enumerate(lines) if block.strip()]
    return '\n\n'.join(numbered)
```

---

## Audio Description

Audio description provides narration of important visual information not conveyed in the main audio.

### What Requires Audio Description

- Speaker names shown on screen but not spoken
- On-screen text (titles, labels, URLs) not read aloud
- Visual actions essential to understanding (demonstrations, diagrams, charts)
- Scene changes and settings important to context
- Facial expressions or physical actions conveying meaning

### What Does NOT Require Audio Description

- Visual elements already described in the audio
- Background settings not essential to understanding
- Decorative visual elements

### Types of Audio Description

| Type | Description |
|------|------------|
| Standard AD | Narration added in natural pauses during main audio |
| Extended AD | Video pauses to allow longer description (WCAG AAA, SC 1.2.7) |
| Open description | Integrated into main audio track (content designed with AD in mind) |

### Audio Description Example

**Without AD:**
Video shows a presenter clicking on a diagram. Audio: "As you can see here, the process has three stages."

**With AD:**
Video shows a presenter clicking on a diagram. Audio: "As you can see here — [AD: The presenter points to a circular diagram labeled 'Research, Design, Launch'] — the process has three stages."

### Delivering Audio Description on the Web

**Option 1: Separate video with AD audio track**
```html
<video controls>
  <source src="video-main.mp4" type="video/mp4">
  <track kind="descriptions" src="audio-desc.vtt" srclang="en" label="Audio description">
</video>
```

**Option 2: Two video versions (more compatible)**
```html
<p>
  <a href="/video-with-ad">Watch with audio description</a>
  |
  <a href="/video-without-ad">Watch standard version</a>
</p>
```

**Option 3: Described video integrated into main audio**
The narrator describes visual content as part of their narration. This is the most accessible and requires production planning.

---

## Auto-Caption Review Workflow

Auto-captions (YouTube, Teams, Zoom, etc.) require review before publishing.

### Minimum Review Checklist

1. **Names** — Proper names of people and places often misheard
2. **Technical terms** — Industry-specific vocabulary often wrong
3. **Homophones** — "there/their/they're", "your/you're"
4. **Sentence boundaries** — Often missing punctuation
5. **Speaker IDs** — Multi-speaker content needs identification
6. **Non-speech audio** — Significant sounds need manual addition
7. **Timing** — Long delays (> 2 seconds) need correction

### Common Auto-Caption Errors

- Names: "John Smith" → "Jon Smythe"
- Technical: "ARIA" → "area"; "WCAG" → "way cag"
- Acronyms: "UI" → "you eye"; "API" → "a pee eye"
- Numbers: "2.2" → "two point two" (check format)
- Pauses: long pauses may cause premature caption block breaks
