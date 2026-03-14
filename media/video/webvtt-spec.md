---
title: "WebVTT 1.0 Specification Overview"
standard: "WebVTT 1.0"
source_url: "https://www.w3.org/TR/webvtt1/"
domain: ["media", "social-media"]
last_fetched: "2026-03-14"
status: "normative"
tags: ["webvtt", "captions", "timed-text", "video", "tracks"]
ai_context: "Normative overview of WebVTT file structure and cue syntax for caption and subtitle authoring."
---

# WebVTT 1.0 Specification Overview

## File Header

A WebVTT file begins with:

```text
WEBVTT
```

The header may be followed by optional text on the same line, then one or more blank lines before cues or metadata blocks.

## Cue Timing

Each cue uses a start and end timestamp joined by `-->`.

```text
00:00:01.000 --> 00:00:04.000
Caption text here.
```

Rules:
- end time must be greater than start time
- timestamps use `HH:MM:SS.mmm` or `MM:SS.mmm`
- cues are separated by blank lines

## Cue Payload

Cue payload may contain:
- plain text
- line breaks
- limited WebVTT markup such as voice spans, classes, italics, bold, and ruby annotations

Authors should keep payload readable and avoid styling that changes the semantic meaning of the caption.

## Cue Settings

Optional cue settings may follow the timing line, such as:
- `line`
- `position`
- `size`
- `align`
- `vertical`

Use settings only when layout control is necessary. Poor positioning can cover important video content or make captions harder to track.

## Notes and Regions

- `NOTE` blocks can store comments for authors and tools
- `REGION` blocks define reusable caption regions

These are useful in production pipelines but should not replace a clean default cue layout.

## Accessibility-Relevant Authoring Rules

- captions should preserve speaker changes and meaningful sound cues
- line lengths should remain readable and synchronized with speech
- files should be UTF-8 encoded
- timing should align with spoken content and significant audio events

For authoring practice, pair this file with:
- `domains/social-media/captions-and-transcripts/caption-guide.md`
- `domains/social-media/captions-and-transcripts/webvtt-format.md`
