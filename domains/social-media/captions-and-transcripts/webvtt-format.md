---
title: "WebVTT Format Reference"
standard: "WCAG + WebVTT"
source_url: "https://www.w3.org/TR/webvtt1/"
domain: ["social-media", "web", "media"]
last_fetched: "2026-03-14"
status: "prescriptive"
tags: ["webvtt", "captions", "video", "vtt", "transcripts"]
ai_context: "Focused WebVTT reference for accessible caption files. Load when the user is writing or debugging .vtt caption files."
---

# WebVTT Format Reference

WebVTT is the standard caption and text-track format used with HTML video and many modern media workflows.

---

## Basic Structure

```text
WEBVTT

00:00:01.000 --> 00:00:04.500
Welcome to our accessibility tutorial.
```

---

## Core Rules

- File starts with `WEBVTT`
- Use `HH:MM:SS.mmm --> HH:MM:SS.mmm`
- Separate cue blocks with a blank line
- Milliseconds use a period, not a comma

---

## Useful Features

### Voice Tags

```text
<v Narrator>Welcome to our tutorial.
```

### Cue Identifiers

```text
intro
00:00:01.000 --> 00:00:04.500
Welcome to our tutorial.
```

### Positioning

```text
00:00:01.000 --> 00:00:04.500 position:10% align:left
Caption text
```

---

## WebVTT vs. SRT

| Feature | WebVTT | SRT |
|---------|--------|-----|
| Header | `WEBVTT` required | none |
| Millisecond separator | `.` | `,` |
| Cue settings | supported | not supported |
| Voice tags | supported | not supported |

---

## Common Mistakes

- missing `WEBVTT` header
- comma milliseconds copied from SRT
- overlapping timestamps
- captions too long to read comfortably
- no speaker identification when speakers change
