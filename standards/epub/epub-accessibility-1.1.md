---
title: "EPUB Accessibility 1.1"
standard: "EPUB Accessibility 1.1"
source_url: "https://www.w3.org/TR/epub-a11y-11/"
domain: ["documents"]
last_fetched: "2026-03-13"
status: "normative"
tags: ["epub", "ebooks", "accessibility", "wcag", "documents"]
ai_context: "EPUB Accessibility 1.1 specification overview. Load when creating or auditing accessible ebooks."
---

# EPUB Accessibility 1.1

**Standard:** W3C Recommendation, May 2023
**Source:** https://www.w3.org/TR/epub-a11y-11/

EPUB Accessibility 1.1 defines requirements for accessible EPUB publications. It builds on WCAG 2.x and adds ebook-specific requirements for discovery metadata.

---

## Conformance Levels

### EPUB Accessibility 1.1 — WCAG 2.0 Level A
- All WCAG 2.0 Level A criteria met in all EPUB content documents
- Required discovery metadata present

### EPUB Accessibility 1.1 — WCAG 2.0 Level AA
- All WCAG 2.0 Level A and AA criteria met
- Required discovery metadata present

### EPUB Accessibility 1.1 — WCAG 2.1 Level AA (Recommended)
- Best practice; most current requirements
- Required when targeting modern reading systems

---

## Core Requirements

### 1. WCAG 2.x Compliance in Content Documents

All EPUB content documents (HTML files within the EPUB container) must meet the required WCAG level. The same HTML accessibility rules apply as for web pages.

### 2. Page Navigation

If the print version has page numbers, the EPUB must include page break markers and a page list. This allows coordination between print and digital editions (classroom use, citations).

```xml
<!-- In content document -->
<span epub:type="pagebreak" id="page23" role="doc-pagebreak" aria-label="23"/>

<!-- In navigation document (nav.xhtml) -->
<nav epub:type="page-list">
  <ol>
    <li><a href="chapter1.xhtml#page23">23</a></li>
  </ol>
</nav>
```

### 3. Navigation Document (TOC)

Every EPUB must include a navigation document with a table of contents (`epub:type="toc"`).

```xml
<nav epub:type="toc">
  <h2>Table of Contents</h2>
  <ol>
    <li><a href="chapter1.xhtml">Chapter 1</a></li>
  </ol>
</nav>
```

### 4. Reading Order

The spine (reading order defined in the package document) must match the logical reading order.

### 5. Language

`xml:lang` must be set on the root `<html>` element. The language must match the publication language specified in the package metadata.

---

## Discovery Metadata (Package Document)

EPUB Accessibility 1.1 requires accessibility metadata in the OPF package document so reading systems and catalogues can communicate the publication's accessibility features.

### Required Metadata

```xml
<meta property="schema:accessMode">textual</meta>
<meta property="schema:accessModeSufficient">textual</meta>
<meta property="schema:accessibilityFeature">...</meta>
<meta property="schema:accessibilityHazard">none</meta>
<meta property="schema:accessibilitySummary">...</meta>
<meta property="dcterms:conformsTo">
  EPUB Accessibility 1.1 - WCAG 2.1 Level AA
</meta>
```

### schema:accessMode Values

Describes the sensory modes required to consume the content:

| Value | When to use |
|-------|-------------|
| `textual` | Contains text content |
| `visual` | Contains meaningful visual content (images, charts) |
| `auditory` | Contains meaningful audio |
| `chartOnVisual` | Charts require visual perception |
| `colorDependent` | Color conveys information |
| `diagramOnVisual` | Diagrams require visual perception |
| `mathOnVisual` | Math requires visual perception (unless MathML) |
| `textOnVisual` | Text embedded in images |

### schema:accessModeSufficient Values

Describes the access mode(s) sufficient to consume all content:

| Value | When to use |
|-------|-------------|
| `textual` | All content accessible as text (images have alt text, etc.) |
| `textual,visual` | Both text and visual required |
| `visual` | Content is visual only |

### schema:accessibilityFeature Values

Documents accessibility features present in the publication:

| Feature | Description |
|---------|-------------|
| `alternativeText` | Images have alt text |
| `annotations` | Accessible annotations |
| `audioDescription` | Audio descriptions for video |
| `bookmarks` | Bookmarks present |
| `braille` | Braille-ready |
| `captions` | Captions for audio/video |
| `ChemML` | Chemistry markup |
| `describedMath` | Math described in text |
| `displayTransformability` | User can control font/layout |
| `fullRubyAnnotations` | Full ruby annotations |
| `highContrastAudio` | High contrast audio available |
| `highContrastDisplay` | High contrast CSS available |
| `horizontalWriting` | Horizontal script |
| `index` | Index present |
| `largePrint` | Large print available |
| `latex` | LaTeX math |
| `longDescription` | Long descriptions for complex images |
| `MathML` | Math in MathML |
| `none` | No accessibility features |
| `pageBreakMarkers` | Print page breaks marked |
| `pageNavigation` | Page list navigation present |
| `printPageNumbers` | Print page numbers present |
| `readingOrder` | Logical reading order |
| `rubyAnnotations` | Partial ruby annotations |
| `signLanguage` | Sign language video |
| `structuralNavigation` | Headings, lists, tables for navigation |
| `synchronizedAudioText` | Read aloud synchronization |
| `tableOfContents` | TOC present |
| `tactileGraphic` | Tactile graphic available |
| `tactileObject` | Tactile object available |
| `timingControl` | User controls timing |
| `transcript` | Transcripts for audio/video |
| `ttsMarkup` | TTS pronunciation hints |
| `unlocked` | No DRM restrictions |
| `verticalWriting` | Vertical script |
| `withAdditionalWordSegmentation` | Word segmentation added |

### schema:accessibilityHazard Values

| Value | Description |
|-------|-------------|
| `flashing` | Contains flashing content |
| `motionSimulation` | Contains motion simulation |
| `sound` | Contains sounds |
| `noFlashingHazard` | No flashing hazard |
| `noMotionSimulationHazard` | No motion simulation hazard |
| `noSoundHazard` | No sound hazard |
| `none` | No hazards |
| `unknown` | Hazards unknown |

---

## Exempt Content

Prerecorded audio and video do not need to meet WCAG time-based media requirements within the EPUB content documents IF the publication's primary content is accessible without the media AND appropriate alternatives are provided.

---

## Testing EPUB Accessibility

| Tool | Function | URL |
|------|----------|-----|
| EPUBCheck | Validates EPUB structure and metadata | https://github.com/w3c/epubcheck |
| Ace by DAISY | Accessibility checker (runs axe on content) | https://daisy.github.io/ace/ |
| Thorium Reader | AT-compatible reading system for testing | https://www.edrlab.org/software/thorium-reader/ |
| NVDA + any reading system | Manual screen reader testing | — |

---

## Key Resources

- EPUB Accessibility 1.1 spec: https://www.w3.org/TR/epub-a11y-11/
- Accessibility Metadata: https://www.w3.org/2021/a11y-discov-vocab/latest/
- Ace by DAISY: https://daisy.github.io/ace/
- EPUB Accessibility Techniques: https://www.w3.org/TR/epub-a11y-tech-11/
