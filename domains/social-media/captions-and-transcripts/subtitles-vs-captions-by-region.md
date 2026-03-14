---
title: "Subtitles vs. Captions by Region"
standard: "WCAG"
source_url: "https://www.w3.org/TR/WCAG22/"
domain: ["social-media", "media", "web"]
last_fetched: "2026-03-14"
status: "curated"
tags: ["captions", "subtitles", "terminology", "regional", "video", "social-media"]
ai_context: "Terminology note explaining how 'captions' and 'subtitles' vary by region and product UI. Load when writing requirements or social/video guidance where the label matters."
---

# Subtitles vs. Captions by Region

---

## Purpose-First Rule

When requirements matter, describe the function, not only the label.

Use wording like:

- `captions that include dialogue, speaker identification, and meaningful sound cues`
- `translated subtitles for viewers who can hear the audio but do not understand the language`

This avoids ambiguity when product teams, vendors, or platforms use different terminology.

---

## WCAG Baseline

WCAG uses `captions` for the accessibility feature that includes dialogue plus relevant non-speech audio.

It also notes that in some countries captions are called subtitles.

That means the UI label on a platform is not enough to tell you whether the track meets accessibility needs.

---

## Practical Regional Differences

| Context | "Captions" usually means | "Subtitles" usually means |
|---------|---------------------------|---------------------------|
| US accessibility and legal work | Same-language accessibility text including sound cues | Translation or dialogue-only text |
| Many broadcast and streaming contexts outside the US | Accessibility text may still be labeled subtitles | Translation or same-language text depending on platform |
| Social platform UI labels | Inconsistent; often a generic label for any timed text track | Inconsistent; verify actual content and settings |

Do not assume a regional label guarantees speaker identification or sound-effect coverage.

---

## Safer Requirement Language

### Use These

- `Closed captions`
- `Open captions`
- `Same-language captions`
- `Translated subtitles`
- `SDH / subtitles for deaf and hard of hearing` if that term is used by the vendor

### Avoid Using Alone

- `Add subtitles`
- `Turn on captions/subtitles`
- `Provide accessibility text`

The vague version creates production mistakes and procurement ambiguity.

---

## Examples

### Ambiguous Request

`Please add subtitles to the launch video.`

Possible bad result:

- Dialogue-only English text
- No speaker identification
- No `[music]` or `[applause]`

### Clear Request

`Please add English closed captions with speaker labels and meaningful sound cues, plus Spanish translated subtitles.`

This separates accessibility text from translation text.

---

## Platform and Vendor Review Questions

Ask these before approving deliverables:

1. Does the track include non-speech audio cues?
2. Are speaker changes identified when needed?
3. Is the track same-language accessibility text or translation?
4. Is the final output open-burned, closed-toggleable, or both?

---

## Recommendation for This Repository

When generating guidance:

- Prefer `captions` when you mean accessibility text
- Add a note that some regions or platform UIs may call them `subtitles`
- Specify whether translated subtitles are also needed
