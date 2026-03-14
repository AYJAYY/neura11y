---
title: "EPUB Accessibility Metadata Schema"
standard: "EPUB Accessibility 1.1 + Schema.org Accessibility Vocabulary"
source_url: "https://www.w3.org/2021/a11y-discov-vocab/latest/"
domain: ["documents", "epub"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["epub", "metadata", "schema.org", "accessibility", "discovery"]
ai_context: "Reference for EPUB accessibility metadata properties using the Schema.org Accessibility Vocabulary. Load when creating or auditing EPUB metadata for accessibility conformance."
---

# EPUB Accessibility Metadata Schema

---

## Overview

EPUB Accessibility 1.1 requires publishers to declare accessibility properties using the **Schema.org Accessibility Vocabulary**. This metadata enables discovery tools, libraries, and assistive technologies to surface accessibility information to readers.

Metadata is declared in the **OPF package document** (`content.opf`) using `<meta>` elements with `property` attributes.

---

## Core Schema.org Properties for EPUB Accessibility

### `schema:accessMode`

Describes the senses or faculties required to access the content.

| Value | Meaning |
|-------|---------|
| `textual` | Text content present (can be accessed auditorily via TTS) |
| `visual` | Visual content (images, video, layout-dependent) |
| `auditory` | Audio content required |
| `tactile` | Tactile content (e.g., braille-specific) |
| `colorDependent` | Color used to convey information |

**Example:**
```xml
<meta property="schema:accessMode">textual</meta>
<meta property="schema:accessMode">visual</meta>
```

---

### `schema:accessModeSufficient`

Declares the minimum set of access modes sufficient to consume the content meaningfully. Multiple `accessModeSufficient` elements represent alternatives.

| Value | Meaning |
|-------|---------|
| `textual` | Textual alone is sufficient (fully accessible via TTS) |
| `textual,visual` | Both text and visual needed |
| `visual` | Visual alone sufficient (layout-critical content) |

**Example:**
```xml
<!-- Reading the text alone is sufficient -->
<meta property="schema:accessModeSufficient">textual</meta>
<!-- OR: both text and visual needed for full comprehension -->
<meta property="schema:accessModeSufficient">textual,visual</meta>
```

---

### `schema:accessibilityFeature`

Describes specific accessibility features present in the publication.

| Value | Meaning |
|-------|---------|
| `alternativeText` | All images have alt text |
| `longDescription` | Complex images have long descriptions |
| `structuralNavigation` | Document has structural markup (headings, lists, etc.) |
| `tableOfContents` | NCX/Nav TOC present |
| `index` | Index provided |
| `readingOrder` | Logical reading order maintained |
| `MathML` | Math expressions encoded in MathML |
| `latex` | Math in LaTeX |
| `annotations` | Annotations present |
| `audioDescription` | Audio descriptions for video |
| `captions` | Captions/subtitles for audio/video |
| `printPageNumbers` | Print page numbers present (for hybrid navigation) |
| `pageBreakMarkers` | Page break markers present |
| `displayTransformability` | User can modify font, spacing, etc. |
| `highContrastDisplay` | High contrast display available |
| `largePrint` | Large print edition |
| `tactileGraphic` | Tactile graphics available |
| `braille` | Braille content present |
| `synchronizedAudioText` | Text synchronized with audio (media overlays) |
| `timingControl` | User can control timing of content |
| `unlocked` | DRM does not restrict assistive technology |

**Example:**
```xml
<meta property="schema:accessibilityFeature">alternativeText</meta>
<meta property="schema:accessibilityFeature">structuralNavigation</meta>
<meta property="schema:accessibilityFeature">tableOfContents</meta>
<meta property="schema:accessibilityFeature">readingOrder</meta>
<meta property="schema:accessibilityFeature">printPageNumbers</meta>
```

---

### `schema:accessibilityHazard`

Declares potential hazards in the content.

| Value | Meaning |
|-------|---------|
| `flashing` | Contains flashing content (risk for photosensitive users) |
| `noFlashingHazard` | Confirmed no flashing |
| `motionSimulation` | Contains motion simulation |
| `noMotionSimulationHazard` | Confirmed no motion simulation |
| `sound` | Contains unexpected sounds |
| `noSoundHazard` | Confirmed no unexpected sounds |
| `none` | No known hazards |
| `unknown` | Hazards not evaluated |

**Example:**
```xml
<meta property="schema:accessibilityHazard">noFlashingHazard</meta>
<meta property="schema:accessibilityHazard">noMotionSimulationHazard</meta>
<meta property="schema:accessibilityHazard">noSoundHazard</meta>
```

---

### `schema:accessibilitySummary`

Human-readable description of the accessibility of the publication. Should summarize key features and known gaps.

```xml
<meta property="schema:accessibilitySummary">
  This publication meets WCAG 2.1 Level AA. All images have alt text.
  Math is encoded in MathML. Print page numbers are included for
  hybrid navigation. No audio or video content is present.
</meta>
```

---

### `dcterms:conformsTo` (EPUB Accessibility Conformance)

Declares conformance to the EPUB Accessibility specification.

```xml
<!-- EPUB Accessibility 1.1 + WCAG 2.0 Level A -->
<meta property="dcterms:conformsTo">
  EPUB Accessibility 1.1 - WCAG 2.0 Level A
</meta>

<!-- EPUB Accessibility 1.1 + WCAG 2.1 Level AA (recommended) -->
<meta property="dcterms:conformsTo">
  EPUB Accessibility 1.1 - WCAG 2.1 Level AA
</meta>
```

---

## Complete OPF Metadata Example

```xml
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" xml:lang="en"
  unique-identifier="uid">

  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:dcterms="http://purl.org/dc/terms/">

    <dc:title>Example Accessible Publication</dc:title>
    <dc:language>en</dc:language>

    <!-- Access Modes -->
    <meta property="schema:accessMode">textual</meta>
    <meta property="schema:accessMode">visual</meta>

    <!-- Sufficient Access Modes -->
    <meta property="schema:accessModeSufficient">textual</meta>

    <!-- Accessibility Features -->
    <meta property="schema:accessibilityFeature">alternativeText</meta>
    <meta property="schema:accessibilityFeature">structuralNavigation</meta>
    <meta property="schema:accessibilityFeature">tableOfContents</meta>
    <meta property="schema:accessibilityFeature">readingOrder</meta>
    <meta property="schema:accessibilityFeature">printPageNumbers</meta>

    <!-- Hazards -->
    <meta property="schema:accessibilityHazard">noFlashingHazard</meta>
    <meta property="schema:accessibilityHazard">noMotionSimulationHazard</meta>
    <meta property="schema:accessibilityHazard">noSoundHazard</meta>

    <!-- Summary -->
    <meta property="schema:accessibilitySummary">
      This publication conforms to EPUB Accessibility 1.1 with WCAG 2.1 Level AA.
      All images include alternative text. Structural navigation is provided
      through heading markup and a table of contents. Print page numbers are
      included to support hybrid reading environments.
    </meta>

    <!-- Conformance -->
    <meta property="dcterms:conformsTo">
      EPUB Accessibility 1.1 - WCAG 2.1 Level AA
    </meta>

    <!-- Certifier (optional — for third-party audit) -->
    <meta property="a11y:certifiedBy">Accessibility Auditor Name</meta>
    <meta property="a11y:certifierCredential">IAAP CPACC</meta>

  </metadata>
  ...
</package>
```

---

## Metadata Completeness by Use Case

### Minimum Required (EPUB Accessibility 1.1 Conformance)

Per the EPUB Accessibility 1.1 spec, conforming publications **must include**:
- At least one `schema:accessMode`
- At least one `schema:accessModeSufficient`
- `schema:accessibilityFeature` (at least one, or `none`)
- `schema:accessibilityHazard` (at least one, or `none` or `unknown`)
- `schema:accessibilitySummary`
- `dcterms:conformsTo` (the conformance claim itself)

### Recommended for Discovery

Libraries and retail platforms (Amazon, Apple Books, Google Play Books, Kobo) use these metadata fields for accessibility filtering. Complete and accurate metadata improves discoverability for users who filter for accessible titles.

---

## Validation

### EPUBCheck
```
epubcheck mybook.epub
```
EPUBCheck validates OPF metadata schema values and warns about missing required accessibility metadata (v5.0+).

### Ace by DAISY
```
ace mybook.epub --outdir ace-report/
```
Ace validates EPUB Accessibility conformance claims, checks WCAG criteria, and generates an HTML report. The report includes metadata completeness checks.

---

## Key Resources

- Schema.org Accessibility Vocabulary: w3.org/2021/a11y-discov-vocab/latest/
- EPUB Accessibility 1.1: w3.org/TR/epub-a11y-11/
- Ace by DAISY (validator): inclusivepublishing.org/ace/
- EPUBCheck: github.com/w3c/epubcheck
- Inclusive Publishing metadata guide: inclusivepublishing.org/epub/metadata/
