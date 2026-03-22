---
ai_context: Auto-fetched W3C images tutorial. Supporting source for image purpose
  and text alternative guidance.
domain:
- web
- documents
- social-media
last_fetched: '2026-03-21'
source_url: https://www.w3.org/WAI/tutorials/images/
standard: WAI Tutorials
status: prescriptive
tags:
- images
- tutorial
- wai
- alt-text
title: WAI Images Tutorial (Fetched)
---

Images must have text alternatives that describe the information or function represented by them. This ensures that images can be used by [people with various disabilities](#why-is-this-important). This tutorial demonstrates how to provide appropriate text alternatives based on the purpose of the image:

- **[Informative images](/WAI/tutorials/images/informative/)**: Images that graphically represent concepts and information, typically pictures, photos, and illustrations. The text alternative should be at least a short description conveying the essential information presented by the image.
- **[Decorative images](/WAI/tutorials/images/decorative/)**: Provide a null text alternative (`alt=""`) when the only purpose of an image is to add visual decoration to the page, rather than to convey information that is important to understanding the page.
- **[Functional images](/WAI/tutorials/images/functional/)**: The text alternative of an image used as a link or as a button should describe the functionality of the link or button rather than the visual image. Examples of such images are a printer icon to represent the print function or a button to submit a form.
- **[Images of text](/WAI/tutorials/images/textual/)**: Readable text is sometimes presented within an image. If the image is not a logo, avoid text in images. However, if images of text are used, the text alternative should contain the same words as in the image.
- **[Complex images](/WAI/tutorials/images/complex/)** such as graphs and diagrams: To convey data or detailed information, provide a complete text equivalent of the data or information provided in the image as the text alternative.
- **[Groups of images](/WAI/tutorials/images/groups/)**: If multiple images convey a single piece of information, the text alternative for one image should convey the information for the entire group.
- **[Image maps](/WAI/tutorials/images/imagemap/)**: The text alternative for an image that contains multiple clickable areas should provide an overall context for the set of links. Also, each individually clickable area should have alternative text that describes the purpose or destination of the link.

For a quick overview on deciding which category a particular image fits into, see the [`alt` Decision Tree](/WAI/tutorials/images/decision-tree/). The text alternative needs to be determined by the author, depending on the usage, context, and content of an image. For example, the exact type and look of a bird in an image might be less relevant and described only briefly on a website about parks, but may be appropriate on a website specifically about birds.

## Why is this important?

Images and graphics make content more pleasant and easier to understand for many people, and in particular for those with cognitive and learning disabilities. They serve as cues that are used by people with visual impairments, including people with low vision, to orient themselves in the content.

However, images are used extensively on websites and can create major barriers when they are not accessible. Accessible images are beneficial in many situations, such as:

- **People using screen readers:** The text alternative can be read aloud or rendered as Braille
- **People using speech input software:** Users can put the focus onto a button or linked image with a single voice command
- **People browsing speech-enabled websites:** The text alternative can be read aloud
- **Mobile web users:** Images can be turned off, especially for data-roaming
- **Search engine optimization:** Images become indexable by search engines

Removing images from websites (so-called “text-only versions”) make them less accessible and functional for these users and situations.

These tutorials provide best-practice guidance on implementing accessibility in different situations. This page combined the following WCAG success criteria and techniques from different conformance levels:

**Success Criteria:**

- [**1.1.1** Non-text Content:](https://www.w3.org/WAI/WCAG21/quickref/#qr-text-equiv-all) All non-text content that is presented to the user has a text alternative that serves the equivalent purpose, except for the situations listed[…]. (Level A)
- [**1.4.5** Images of Text:](https://www.w3.org/WAI/WCAG21/quickref/#qr-visual-audio-contrast-text-presentation) If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except [for customizable and essential images] (Level AA)
- [**1.4.9** Images of Text (No Exception):](https://www.w3.org/WAI/WCAG21/quickref/#qr-visual-audio-contrast-text-images) Images of text are only used for pure decoration or where a particular presentation of text is essential to the information being conveyed (Level AAA)

Please share your ideas, suggestions, or comments via e-mail to the publicly-archived list [wai@w3.org](mailto:wai@w3.org?body=%5Binclude%20a%20relevant%20email%20Subject%5D%0A%0A%5Bput%20comment%20here...%5D%0A%0AI%20give%20permission%20to%20share%20this%20to%20a%20publicly-archived%20e-mail%20list.) or via GitHub.

[E-mail](mailto:wai@w3.org?body=%5Binclude%20a%20relevant%20email%20Subject%5D%0A%0A%5Bput%20comment%20here...%5D%0A%0AI%20give%20permission%20to%20share%20this%20to%20a%20publicly-archived%20e-mail%20list.)[Fork & Edit on GitHub](
https://github.com/w3c/wai-website/edit/main/pages/design-develop/tutorials/images/index.md
)[New GitHub Issue](https://github.com/w3c/wai-website/issues/new?template=content-issue.yml&wai-resource-id=wai-tutorials&wai-url=https://www.w3.org/WAI/tutorials/images/)

 [Back to Top](#top)