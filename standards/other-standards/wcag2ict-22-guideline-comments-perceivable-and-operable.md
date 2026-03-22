---
ai_context: WCAG2ICT interpretations for Principles 1 and 2 in non-web documents and
  software contexts.
domain:
- documents
- mobile
- physical-ict
- general
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/wcag2ict-22/
standard: WCAG2ICT 2.2
status: prescriptive
tags:
- wcag2ict
- non-web
- perceivable
- operable
- guideline-comments
title: 'WCAG2ICT 2.2 Guideline Comments: Perceivable and Operable'
---

# WCAG2ICT 2.2 Guideline Comments: Perceivable and Operable

## Guideline Comments for Principles 1 and 2

### 1. Perceivable

> Information and user interface components must be presentable to users in ways they can perceive.

#### Applying Principle 1 Perceivable to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 1 applies directly as written.

#### 1.1 Text Alternatives

> Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language.

##### Applying Guideline 1.1 Text Alternatives to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.1 applies directly as written.

##### 1.1.1 Non-text Content

(Level A)

> All [non-text content](https://www.w3.org/TR/WCAG22/#dfn-non-text-content "any content that is not a sequence of characters that can be programmatically determined or where the sequence is not expressing something in human language") that is presented to the user has a [text alternative](https://www.w3.org/TR/WCAG22/#dfn-text-alternative "Text that is programmatically associated with non-text content or referred to from text that is programmatically associated with non-text content. Programmatically associated text is text whose location can be programmatically determined from the non-text content.") that serves the equivalent purpose, except for the situations listed below.
>
> Controls, Input
> :   If non-text content is a control or accepts user input, then it has a [name](https://www.w3.org/TR/WCAG22/#dfn-name "text by which software can identify a component within web content to the user") that describes its purpose. (Refer to [Success Criterion 4.1.2](https://www.w3.org/TR/WCAG22/#name-role-value) for additional requirements for controls and content that accepts user input.)
>
> Time-Based Media
> :   If non-text content is time-based media, then text alternatives at least provide descriptive
>     identification of the non-text content. (Refer to [Guideline 1.2](https://www.w3.org/TR/WCAG22/#time-based-media) for additional requirements for media.)
>
> Test
> :   If non-text content is a test or exercise that would be invalid if presented in [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language"), then text alternatives at least provide descriptive identification of the non-text
>     content.
>
> Sensory
> :   If non-text content is primarily intended to create a [specific sensory experience](https://www.w3.org/TR/WCAG22/#dfn-specific-sensory-experience "a sensory experience that is not purely decorative and does not primarily convey important information or perform a function"), then text alternatives at least provide descriptive identification of the non-text
>     content.
>
> [CAPTCHA](https://www.w3.org/TR/WCAG22/#dfn-captcha "initialism for \"Completely Automated Public Turing test to tell Computers and Humans Apart\"")
> :   If the purpose of non-text content is to confirm that content is being accessed by
>     a person rather than a computer, then text alternatives that identify and describe
>     the purpose of the non-text content are provided, and alternative forms of CAPTCHA
>     using output modes for different types of sensory perception are provided to accommodate
>     different disabilities.
>
> Decoration, Formatting, Invisible
> :   If non-text content is [pure decoration](https://www.w3.org/TR/WCAG22/#dfn-pure-decoration "serving only an aesthetic purpose, providing no information, and having no functionality"), is used only for visual formatting, or is not presented to users, then it is implemented
>     in a way that it can be ignored by [assistive technology](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents").

###### Applying SC 1.1.1 Non-text Content to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content#intent).

Note 1 (Added)

CAPTCHAs do not currently appear outside of the Web. However, if they do appear, this guidance is accurate.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

#### 1.2 Time-based Media

> Provide alternatives for time-based media.

##### Applying Guideline 1.2 Time Based Media to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.2 applies directly as written.

##### 1.2.1 Audio-only and Video-only (Prerecorded)

(Level A)

> For [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live")
> [audio-only](https://www.w3.org/TR/WCAG22/#dfn-audio-only "a time-based presentation that contains only audio (no video and no interaction)") and prerecorded [video-only](https://www.w3.org/TR/WCAG22/#dfn-video-only "a time-based presentation that contains only video (no audio and no interaction)") media, the following are true, except when the audio or video is a [media alternative for text](https://www.w3.org/TR/WCAG22/#dfn-media-alternative-for-text "media that presents no more information than is already presented in text (directly or via text alternatives)") and is clearly labeled as such:
>
> Prerecorded Audio-only
> :   An [alternative for time-based media](https://www.w3.org/TR/WCAG22/#dfn-alternative-for-time-based-media "document including correctly sequenced text descriptions of time-based visual and auditory information and providing a means for achieving the outcomes of any time-based interaction") is provided that presents equivalent information for prerecorded audio-only content.
>
> Prerecorded Video-only
> :   Either an alternative for time-based media or an audio track is provided that presents
>     equivalent information for prerecorded video-only content.

###### Applying SC 1.2.1 Audio-only and Video-only (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.1](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded#intent).

Note 1 (Added)

The alternative can be provided directly in the [non-web document](#document) or [software](#software) – or provided in an alternate version that satisfies the success criterion.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.2.2 Captions (Prerecorded)

(Level A)

> [Captions](https://www.w3.org/TR/WCAG22/#dfn-captions "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content") are provided for all [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live")
> [audio](https://www.w3.org/TR/WCAG22/#dfn-audio "the technology of sound reproduction") content in [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such"), except when the media is a [media alternative for text](https://www.w3.org/TR/WCAG22/#dfn-media-alternative-for-text "media that presents no more information than is already presented in text (directly or via text alternatives)") and is clearly labeled as such.

###### Applying SC 1.2.2 Captions (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded#intent).

Note (Added)

The WCAG 2 definition of “[captions](https://www.w3.org/TR/WCAG22/#dfn-captions)” notes that “in some countries, captions are called subtitles”. They are also sometimes referred to as “subtitles for the hearing impaired". Per the definition in WCAG 2, to satisfy this success criterion, whether called captions or subtitles, they would have to provide “synchronized visual and/or [text alternative](https://www.w3.org/TR/WCAG22/#dfn-text-alternative) for both speech and non-speech audio information needed to understand the media content” where non-speech information includes “sound effects, music, laughter, speaker identification and location”.

##### 1.2.3 Audio Description or Media Alternative (Prerecorded)

(Level A)

> An [alternative for time-based media](https://www.w3.org/TR/WCAG22/#dfn-alternative-for-time-based-media "document including correctly sequenced text descriptions of time-based visual and auditory information and providing a means for achieving the outcomes of any time-based interaction") or [audio description](https://www.w3.org/TR/WCAG22/#dfn-audio-descriptions "narration added to the soundtrack to describe important visual details that cannot be understood from the main soundtrack alone") of the [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live")
> [video](https://www.w3.org/TR/WCAG22/#dfn-video "the technology of moving or sequenced pictures or images") content is provided for [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such"), except when the media is a [media alternative for text](https://www.w3.org/TR/WCAG22/#dfn-media-alternative-for-text "media that presents no more information than is already presented in text (directly or via text alternatives)") and is clearly labeled as such.

###### Applying SC 1.2.3 Audio Description or Media Alternative (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.3](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded#intent).

Note 1 (Added)

Audio descriptions (also called "video descriptions", "descriptive narration", and "described videos") describe important visual information needed to understand the video content, including text displayed in the video. Where the main audio track of the video fully describes important visual information, audio descriptions would not be needed at all as the requirement would already be met. When audio descriptions are needed, one way to implement them is by providing a second audio track within the synchronized media.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.2.4 Captions (Live)

(Level AA)

> [Captions](https://www.w3.org/TR/WCAG22/#dfn-captions "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content") are provided for all [live](https://www.w3.org/TR/WCAG22/#dfn-live "information captured from a real-world event and transmitted to the receiver with no more than a broadcast delay")
> [audio](https://www.w3.org/TR/WCAG22/#dfn-audio "the technology of sound reproduction") content in [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such").

###### Applying SC 1.2.4 Captions (Live) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.4](https://www.w3.org/WAI/WCAG22/Understanding/captions-live#intent).

Note (Added)

The WCAG 2 definition of “[captions](https://www.w3.org/TR/WCAG22/#dfn-captions)” notes that “In some countries, captions are called subtitles”. They are also sometimes referred to as “subtitles for the hearing impaired". Per the definition in WCAG 2, to satisfy this success criterion, whether called captions or subtitles, they would have to provide “synchronized visual and/or [text alternative](https://www.w3.org/TR/WCAG22/#dfn-text-alternative) for both speech and non-speech audio information needed to understand the media content” where non-speech information includes “sound effects, music, laughter, speaker identification and location”.

##### 1.2.5 Audio Description (Prerecorded)

(Level AA)

> [Audio description](https://www.w3.org/TR/WCAG22/#dfn-audio-descriptions "narration added to the soundtrack to describe important visual details that cannot be understood from the main soundtrack alone") is provided for all [prerecorded](https://www.w3.org/TR/WCAG22/#dfn-prerecorded "information that is not live")
> [video](https://www.w3.org/TR/WCAG22/#dfn-video "the technology of moving or sequenced pictures or images") content in [synchronized media](https://www.w3.org/TR/WCAG22/#dfn-synchronized-media "audio or video synchronized with another format for presenting information and/or with time-based interactive components, unless the media is a media alternative for text that is clearly labeled as such").

###### Applying SC 1.2.5 Audio Description (Prerecorded) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.2.5](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded#intent).

Note (Added)

Audio descriptions (also called "video descriptions", "descriptive narration", and "described videos") describe important visual information needed to understand the video content, including text displayed in the video. Where the main audio track of the video fully describes important visual information, audio descriptions would not be needed at all as the requirement would already be met. When audio descriptions are needed, one way to implement them is by providing a second audio track within the synchronized media.

#### 1.3 Adaptable

> Create content that can be presented in different ways (for example simpler layout) without losing information or structure.

##### Applying Guideline 1.3 Adaptable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.3 applies directly as written.

##### 1.3.1 Info and Relationships

(Level A)

> Information, [structure](https://www.w3.org/TR/WCAG22/#dfn-structure "The way the parts of a web page are organized in relation to each other; and The way a collection of web pages is organized"), and [relationships](https://www.w3.org/TR/WCAG22/#dfn-relationships "meaningful associations between distinct pieces of content") conveyed through [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation "rendering of the content in a form to be perceived by users") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") or are available in text.

###### Applying SC 1.3.1 Info and Relationships to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships#intent).

Note 1 (Added) (for non-web documents)

Where non-web documents contain non-standard structure types (roles), it is best practice to map them to a standard structure type as a fall-back solution for the reader.

Note 2 (Added) (for non-web software)

In non-web software, programmatic determinability is best achieved by using the [accessibility services of platform software](#accessibility-services-of-platform-software) to enable interoperability between the software and assistive technologies and accessibility features of software.

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.3.2 Meaningful Sequence

(Level A)

> When the sequence in which content is presented affects its meaning, a [correct reading sequence](https://www.w3.org/TR/WCAG22/#dfn-correct-reading-sequence "any sequence where words and paragraphs are presented in an order that does not change the meaning of the content") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities").

###### Applying SC 1.3.2 Meaningful Sequence to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.3.3 Sensory Characteristics

(Level A)

> Instructions provided for understanding and operating content do not rely solely on
> sensory characteristics of components such as shape, color, size, visual location, orientation,
> or sound.
>
> Note
>
> For requirements related to color, refer to [Guideline 1.4](https://www.w3.org/TR/WCAG22/#distinguishable).

###### Applying SC 1.3.3 Sensory Characteristics to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.3](https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics#intent).

##### 1.3.4 Orientation

(Level AA)

> Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform").
>
> Note
>
> Examples where a particular display orientation may be essential are a bank check, a piano application, slides for a projector or television, or virtual reality content where content is not necessarily restricted to landscape or portrait display orientation.

###### Applying SC 1.3.4 Orientation to Non-Web Documents

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.4](https://www.w3.org/WAI/WCAG22/Understanding/orientation#intent), except for non-web documents that will never be displayed on hardware that is reoriented in typical use.

Example (Added) (for non-web documents): Examples of non-web documents that will never be displayed on hardware that is reoriented in typical use include but are not limited to:

- a building directory that is only displayed on displays (of any type including tablets) that are all fixed to the wall in one orientation,
- reports of results of a test that are displayed only on the screen of the testing device, and
- the status report sent to the screen of a copy machine (but not the status report that would be sent to a web interface to the same machine).

###### Applying SC 1.3.4 Orientation to Non-Web Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.4](https://www.w3.org/WAI/WCAG22/Understanding/orientation#intent), except for non-web software that will never be displayed on hardware that is reoriented in typical use.

Note 1 (Added) (for non-web software)

Non-web software that is only used on hardware that supports a single display orientation, or where it is an application that is displayed only on hardware that is physically fixed in one orientation (e.g. a digital building directory) is excluded by the precondition and therefore does not need to provide support for orientation changes.

Example (Added) (for non-web software): Examples of non-web software that will never be displayed on hardware that is reoriented in typical use include but are not limited to:

- software for a typical calculator that does not support screen re-orientation,
- software menus and controls on a copier or other device that is not intended to be viewed in more than one orientation (but not any remote control software or app for the same device that runs on computers or mobile devices),
- software on a wristwatch that is not intended to be viewed when the watch is not on the wrist, and
- special applications such as software for displays around a building that will only be used on a known set of displays that are all permanently affixed in the same orientation.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.3.5 Identify Input Purpose

(Level AA)

> The purpose of each input field collecting information about the user can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") when:
>
> - The input field serves a purpose identified in the [Input Purposes for user interface components section](https://www.w3.org/TR/WCAG22/#input-purposes); and
> - The content is implemented using technologies with support for identifying the expected meaning for form input data.

###### Applying SC 1.3.5 Identify Input Purpose to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.3.5](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html#intent).

Note 1 (Added)

[Non-web software](#software) and [non-web document](#document) technologies that do not provide attributes that support identifying the expected meaning for the form input data are not in scope for this success criterion.

Note 2 (Added)

For non-web software and non-web documents that present input fields, the terms for the input purposes would be the equivalent terms to those listed in the WCAG 2 section [Input Purposes for User Interface Components](https://www.w3.org/TR/WCAG22/#input-purposes) that are supported by the technology used.

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

#### 1.4 Distinguishable

> Make it easier for users to see and hear content including separating foreground from background.

##### Applying Guideline 1.4 Distinguishable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 1.4 applies directly as written.

##### 1.4.1 Use of Color

(Level A)

> Color is not used as the only visual means of conveying information, indicating an
> action, prompting a response, or distinguishing a visual element.
>
> Note
>
> This success criterion addresses color perception specifically. Other forms of perception are covered in [Guideline 1.3](https://www.w3.org/TR/WCAG22/#adaptable) including programmatic access to color and other visual presentation coding.

###### Applying SC 1.4.1 Use of Color to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color#intent).

##### 1.4.2 Audio Control

(Level A)

> If any audio on a web page plays automatically for more than 3 seconds, either a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to [pause](https://www.w3.org/TR/WCAG22/#dfn-pause "stopped by user request and not resumed until requested by user") or stop the audio, or a mechanism is available to control audio
> volume independently from the overall system volume level.
>
> Note
>
> Since any content that does not meet this success criterion can interfere with a user's
> ability to use the whole page, all content on the web page (whether or not it is used
> to meet other success criteria) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).

###### Applying SC 1.4.2 Audio Control to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.2](https://www.w3.org/WAI/WCAG22/Understanding/audio-control#intent), replacing “on a web page” with “in the non-web document or software”, “whole page” with “whole non-web document or software”, and “on the web page” with “in the non-web document or software”; removing “See Conformance Requirement 5: Non-Interference”; and adjusting Note 1 to avoid the use of the normative term "must".

With these substitutions, it would read:

**1.4.2 Audio Control:** If any audio [in the **[non-web document](#document)** or **[software](#software)**] plays automatically for more than 3 seconds, either a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to pause or stop the audio, or a mechanism is available to control audio volume independently from the overall system volume level.

Note 1

Since any content that does not meet this success criterion can interfere with a user's ability to use the [whole non-web document or software], [it would be necessary for] all content [in the non-web document or software] (whether or not it is used to meet other success criteria) [to] meet this success criterion.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.3 Contrast (Minimum)

(Level AA)

> The visual presentation of [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") and [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect") has a [contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio "(L1 + 0.05) / (L2 + 0.05), where") of at least 4.5:1, except for the following:
>
> Large Text
> :   [Large-scale](https://www.w3.org/TR/WCAG22/#dfn-large-scale "with at least 18 point or 14 point bold or font size that would yield equivalent size for Chinese, Japanese and Korean (CJK) fonts") text and images of large-scale text have a contrast ratio of at least 3:1;
>
> Incidental
> :   Text or images of text that are part of an inactive [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function"), that are [pure decoration](https://www.w3.org/TR/WCAG22/#dfn-pure-decoration "serving only an aesthetic purpose, providing no information, and having no functionality"), that are not visible to anyone, or that are part of a picture that contains significant
>     other visual content, have no contrast requirement.
>
> Logotypes
> :   Text that is part of a logo or brand name has no contrast requirement.

###### Applying SC 1.4.3 Contrast Minimum to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.4 Resize Text

(Level AA)

> Except for [captions](https://www.w3.org/TR/WCAG22/#dfn-captions "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content") and [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect"), [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") can be resized without [assistive technology](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents") up to 200 percent without loss of content or functionality.

###### Applying SC 1.4.4 Resize Text to Non-Web Documents

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text#intent).

Note 1 (Added)

It is best practice to use only fonts that allow for scaling without loss of quality (e.g. pixelized presentation). This applies in particular to embedded fonts.

Note 2 (Added) (for non-web documents)

[Content](#content-on-and-off-the-web) for which there are viewers or editors with a 200 percent zoom feature would automatically satisfy this success criterion when used with such viewers or editors, unless the content will not work with that zoom feature.

###### Applying SC 1.4.4 Resize Text to Non-Web Software

This success criterion is problematic to apply directly to non-web software because not all platforms provide text enlargement features that increase all displayed text to 200%. Non-web software needs to work with platform capabilities where they exist, but when the platform has text resizing support up to 200%, but not all text types scale to 200%, it is unreasonable for all apps on a particular platform to be required to build in their own text resizing. Where the platform has text resizing support up to 200%, but where not all text resizes to 200% (because some of the text is already 200% of the default body text size), and provided semantic meaning indicated through differences in text size is maintained, the non-web software should work with the text sizing features to the extent the platform provides. Doing so would still address the user needs identified in the [Intent from Understanding Success Criterion 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text#intent). The following criterion is recommended as a substitute for the WCAG language:

Except for captions and images of text, text can be resized without loss of content or functionality and without assistive technology either up to 200 percent or, if the platform provides text resizing capabilities but it does not reach 200 percent for all text, up to the text sizing capabilities of the platform.

Note 1 (Added)

It is best practice to use only fonts that allow for scaling without loss of quality (e.g. pixelized presentation). This applies in particular to embedded fonts.

Note 2 (Added) (for non-web software)

The [Intent section in Understanding 1.4.4 Resize Text](http://section) refers to the ability to allow users to enlarge the text on screen at least up to 200% without needing to use [assistive technologies](#dfn-assistive-technologies). This means that the [non-web software](#software) provides some means for enlarging the text 200% (zoom or otherwise) without loss of [content](#content-on-and-off-the-web) or functionality, or that the non-web software works with the platform features to satisfy this success criterion.

Note 3 (Added) (for non-web software)

For non-web software, sometimes the platform provides text scaling to 200% for most, but not all text (e.g. headings, which are naturally large, may not be increased in size to 200%, but other text does increase to 200%). In such cases, authors would only need to support text scaling to the extent provided by user settings in the platform, without losing text-size semantics, content or functionality, to satisfy this success criterion.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.5 Images of Text

(Level AA)

> If the technologies being used can achieve the visual presentation, [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") is used to convey information rather than [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect") except for the following:
>
> Customizable
> :   The image of text can be [visually customized](https://www.w3.org/TR/WCAG22/#dfn-visually-customized "the font, size, color, and background can be set") to the user's requirements;
>
> Essential
> :   A particular presentation of text is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") to the information being conveyed.
>
> Note
>
> Logotypes (text that is part of a logo or brand name) are considered essential.

###### Applying SC 1.4.5 Images of Text to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.5](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.10 Reflow

(Level AA)

> Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:
>
> - Vertical scrolling content at a width equivalent to 320 [CSS pixels](https://www.w3.org/TR/WCAG22/#dfn-css-pixels "visual angle of about 0.0213 degrees");
> - Horizontal scrolling content at a height equivalent to 256 [CSS pixels](https://www.w3.org/TR/WCAG22/#dfn-css-pixels "visual angle of about 0.0213 degrees").
>
> Except for parts of the content which require two-dimensional layout for usage or meaning.
>
> Note 1
>
> 320 CSS pixels is equivalent to a starting [viewport](https://www.w3.org/TR/WCAG22/#dfn-viewport "object in which the user agent presents content") width of 1280 CSS pixels wide at 400% zoom. For web content which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.
>
> Note 2
>
> Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

###### Applying SC 1.4.10 Reflow to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html#intent), replacing “web content” with “content”.

With this substitution, it would read:

**1.4.10 Reflow:** Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:

- Vertical scrolling content at a width equivalent to 320 [CSS pixels](#dfn-css-pixels);
- Horizontal scrolling content at a height equivalent to 256 [CSS pixels](#dfn-css-pixels).

Except for parts of the content which require two-dimensional layout for usage or meaning.

Note 1

320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom. For [**[content](#content-on-and-off-the-web)**] which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.

Note 2

Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

Note 3 (Added)

In technologies where CSS is not used, the definition of 'CSS pixel' applies as described in [Applying “CSS pixel” to Non-Web Documents and Software](#applying-css-pixel-to-non-web-documents-and-software).

Note 4 (Added) (for non-web documents)

If a [non-web document](#document) type and its available [user agents](#user-agent) do not support reflow, it may not be possible for a document of that type to satisfy this success criterion.

Note 5 (Added) (for non-web software)

The intent section refers to the ability for content to reflow (for vertical scrolling content at a width equivalent to 320 CSS pixels, or for horizontal scrolling content at a height equivalent to 256 CSS pixels) when user agent zooming is used to scale content or when the [viewport](#dfn-viewport) changes in width. For [non-web software](#software), this means that when users scale content, adjust the size of a window, dialog, or other resizable content area, or change the screen resolution, the content will reflow without loss of information or functionality, and without requiring scrolling in two dimensions; or that the non-web software works with platform features that satisfy this success criterion.

Note 6 (Added) (for non-web software)

Non-web software will have more frequent cases where two-dimensional layout is relied upon for usage or meaning than what occurs on the Web. For example:

- When the non-web software has a complex user interface with toolbars that need to be visible while manipulating content, as explained in the Intent from Understanding 1.4.10 Reflow.

Note 7 (Added) (for non-web software)

As written, this success criterion can only be met by non-web software where the underlying user agent or platform software can present content at a width equivalent to 320 CSS pixels for vertical scrolling content and a height equivalent to 256 CSS pixels for horizontal scrolling content.

When the underlying user agent or platform software does not support these dimensions for scrolling, reflow is encouraged as this capability is important to people with low vision. As a reasonable benchmark, evaluate at the nearest size to what the Reflow success criterion specifies.

When users modify zoom, scaling, and/or display resolution at the platform software level (e.g. Operating System), it impacts the size of all applications and the [platform software](#platform-software) itself. This can result in improved readability in some applications but unwanted consequences in others.

Note 8 (Added) (for non-web software)

Some non-web software applications provide a mode of operation where reflow is possible, while other modes are unable to reflow. An example is a document authoring tool, which includes both a "print preview mode" (without reflow, for users to view the spatial formatting) and a "drafting view mode" where reflow is supported. Such software would satisfy this success criterion as long as there is no loss of information or functionality in the drafting view.

Note 9 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.11 Non-text Contrast

(Level AA)

> The visual [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation "rendering of the content in a form to be perceived by users") of the following have a [contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio "(L1 + 0.05) / (L2 + 0.05), where") of at least 3:1 against adjacent color(s):
>
> User Interface Components
> :   Visual information required to identify [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") and [states](https://www.w3.org/TR/WCAG22/#dfn-states "dynamic property expressing characteristics of a user interface component that may change in response to user action or automated processes"), except for inactive components or where the appearance of the component is determined by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and not modified by the author;
>
> Graphical Objects
> :   Parts of graphics required to understand the content, except when a particular presentation of graphics is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") to the information being conveyed.

###### Applying SC 1.4.11 Non-text Contrast to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html#intent), replacing "user agent" with "user agent or other platform software".

With this substitution, it would read:

**1.4.11 Non-text Contrast:** The visual [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation) of the following have a [contrast ratio](#dfn-contrast-ratio) of at least 3:1 against adjacent color(s):

User Interface Components
:   Visual information required to identify [user interface components](#dfn-user-interface-components) and [states](https://www.w3.org/TR/WCAG22/#dfn-states), except for inactive components or where the appearance of the component is determined by the [**[user agent](#user-agent)** or other **[platform software](#platform-software)**] and not modified by the author;

Graphical Objects
:   Parts of graphics required to understand the content, except when a particular presentation of graphics is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential) to the information being conveyed.

Note 1 (Added)

An example of appearance modification by the author is content that sets the visual style of a control, such as a color or border, to differ from the default style for the user agent or platform.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.12 Text Spacing

(Level AA)

> In content implemented using markup languages that support the following [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") [style properties](https://www.w3.org/TR/WCAG22/#dfn-style-properties "property whose value determines the presentation (e.g. font, color, size, location, padding, volume, synthesized speech prosody) of content elements as they are rendered (e.g. onscreen, via loudspeaker, via braille display) by user agents"), no loss of content or functionality occurs by setting all of the following and by changing no other style property:
>
> - Line height (line spacing) to at least 1.5 times the font size;
> - Spacing following paragraphs to at least 2 times the font size;
> - Letter spacing (tracking) to at least 0.12 times the font size;
> - Word spacing to at least 0.16 times the font size.
>
> Exception: [Human languages](https://www.w3.org/TR/WCAG22/#dfn-human-language-s "language that is spoken, written or signed (through visual or tactile means) to communicate with humans") and scripts that do not make use of one or more of these text style properties in written text can conform using only the properties that exist for that combination of language and script.
>
> Note 1
>
> Content is not required to use these text spacing values. The requirement is to ensure that when a user overrides the authored text spacing, content or functionality is not lost.
>
> Note 2
>
> Writing systems for some languages use different text spacing settings, such as paragraph start indent. Authors are encouraged to follow locally available guidance for improving readability and legibility of text in their writing system.

###### Applying SC 1.4.12 Text Spacing to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html#intent).

Note 1 (Added)

This success criterion only applies to [non-web documents](#document) and [software](#software) that are implemented using markup languages and allow the user to modify these text spacing properties.

Note 2 (Added) (for non-web documents)

There are several mechanisms that allow users to modify a document's text spacing properties of content implemented in markup languages. For example, an eBook technology may have an available user agent that allows users to override document text styles. When such a mechanism is available, the success criterion requires that the content responds appropriately to it.

Note 3 (Added) (for non-web software)

There are several mechanisms that allow users to modify software's text spacing properties of content implemented in markup languages. For example, a software application may provide a "user style sheet" facility to modify the appearance of the software's own user interface. This success criterion does not mean that non-web software needs to implement their own mechanisms to allow users to set text spacing; however, when such a mechanism is available, the success criterion requires that the content responds appropriately to it.

Note 4 (Added) (for non-web software)

"Content implemented using markup languages" includes parts of software that use markup internally to define a user interface. Examples of markup languages that are used internally to define a software user interface include but are not limited to: HTML (e.g., in [Electron](https://www.electronjs.org/) applications or iOS application web views), XAML, XML (e.g., in Android application layouts), and XUL.

Note 5 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 1.4.13 Content on Hover or Focus

(Level AA)

> Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:
>
> Dismissible
> :   A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an [input error](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") or does not obscure or replace other content;
>
> Hoverable
> :   If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;
>
> Persistent
> :   The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.
>
> Exception: The visual presentation of the additional content is controlled by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and is not modified by the author.
>
> Note 1
>
> Examples of additional content controlled by the user agent include browser tooltips created through use of the HTML [`title` attribute](https://html.spec.whatwg.org/multipage/dom.html#the-title-attribute) [[HTML](https://www.w3.org/TR/WCAG22/#bib-html "HTML Standard")].
>
> Note 2
>
> Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.
>
> Note 3
>
> This criterion applies to content that appears in addition to the triggering component itself. Since hidden components that are made visible on keyboard focus (such as links used to skip to another part of a page) do not present additional content they are not covered by this criterion.

###### Applying SC 1.4.13 Content on Hover or Focus to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html), replacing "user agent" with "user agent or other platform software", "browser tooltips" with "tooltips", "the HTML title attribute" with "user interface object attributes", "links" with "links or other UI controls that behave like a link", and "a page" with "the non-web document or software".

With these substitutions, it would read:

**1.4.13 Content on Hover or Focus:** Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:

Dismissible
:   A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an [input error](#dfn-input-error) or does not obscure or replace other content;

Hoverable
:   If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;

Persistent
:   The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.

Exception: The visual presentation of the additional content is controlled by the [**[user agent](#user-agent)** or other **[platform software](#platform-software)**] and is not modified by the author.

Note 1

Examples of additional content controlled by the [user agent or other platform software] include [tooltips] created through use of [user interface object attributes].

Note 2

Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.

Note 3

This criterion applies to content that appears in addition to the triggering component itself. Since hidden components that are made visible on keyboard focus (such as [links or other UI controls that behave like a link] used to skip to another part of [the non-web document or software]) do not present additional content they are not covered by this criterion.

### 2. Operable

> User interface components and navigation must be operable.

#### Applying Principle 2 Operable to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 2 applies directly as written.

#### 2.1 Keyboard Accessible

> Make all functionality available from a keyboard.

##### Applying Guideline 2.1 Keyboard Accessible to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.1 applies directly as written.

##### 2.1.1 Keyboard

(Level A)

> All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") of the content is operable through a [keyboard interface](https://www.w3.org/TR/WCAG22/#dfn-keyboard-interface "interface used by software to obtain keystroke input") without requiring specific timings for individual keystrokes, except where the underlying
> function requires input that depends on the path of the user's movement and not just
> the endpoints.
>
> Note 1
>
> This exception relates to the underlying function, not the input technique. For example,
> if using handwriting to enter text, the input technique (handwriting) requires path-dependent
> input but the underlying function (text input) does not.
>
> Note 2
>
> This does not forbid and should not discourage providing mouse input or other input
> methods in addition to keyboard operation.

###### Applying SC 2.1.1 Keyboard to Non-Web Documents

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard#intent).

###### Applying SC 2.1.1 Keyboard to Non-Web Software

Where ICT is or includes non-web software that can be run on a software platform that provides a device-independent keyboard interface service, this applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard#intent).

Note 1 (Added) (for non-web software)

Keyboard interface does not refer to a physical device but to the service of [platform software](#platform-software) (e.g. operating system, browser, etc.) that provides the software with keystrokes from any keyboard or keyboard substitute. When the [non-web software](#software) supports such a device-independent service of the platform software, and the non-web software functionality is made fully operable through the service, then this success criterion would be satisfied.

Note 2 (Added) (for non-web software)

A "device-independent keyboard interface service" refers to the platform service that provides keystrokes to any software running on the platform.

Note 3 (Added) (for non-web software)

Inclusion of an on-screen keyboard can be done as well but does not satisfy this requirement since it does not allow for the use of keyboard alternatives whereas support of input from the device-independent keyboard interface service does.

Note 4 (Added) (for non-web software)

This success criterion does not imply that non-web software always needs to directly support a keyboard or “keyboard interface” if one is not provided by the platform software. But if one is provided, the software needs to make all functionality available through it - unless the exception applies.

Note 5 (Added) (for non-web software)

This success criterion also does not imply that non-web software always needs to provide its own [virtual keyboard](#virtual-keyboard). But if it does, then the non-web software still needs to support keyboard input from any keyboard interface provided by the platform software.

Note 6 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.1.2 No Keyboard Trap

(Level A)

> If keyboard focus can be moved to a component of the page using a [keyboard interface](https://www.w3.org/TR/WCAG22/#dfn-keyboard-interface "interface used by software to obtain keystroke input"), then focus can be moved away from that component using only a keyboard interface,
> and, if it requires more than unmodified arrow or tab keys or other standard exit
> methods, the user is advised of the method for moving focus away.
>
> Note
>
> Since any content that does not meet this success criterion can interfere with a user's
> ability to use the whole page, all content on the web page (whether it is used to
> meet other success criteria or not) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).

###### Applying SC 2.1.2 No Keyboard Trap to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.2](https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap#intent), replacing “page” with “non-web document or software” and “on the web page” with "in the non-web document or software"; removing “See Conformance Requirement 5: Non-Interference”; and adjusting Note 1 to avoid the use of the normative term "must".

With these substitutions, it would read:

**2.1.2 No Keyboard Trap:** If keyboard focus can be moved to a component of the [**[non-web document](#document)** or **[software](#software)**] using a [keyboard interface](#dfn-keyboard-interface), then focus can be moved away from that component using only a keyboard interface, and, if it requires more than unmodified arrow or tab keys or other standard exit methods, the user is advised of the method for moving focus away.

Note 1

Since any content that does not meet this success criterion can interfere with a user's ability to use the whole [**[non-web document](#document)** or **[software](#software)**], [it would be necessary for] all content [in the non-web document or software] (whether it is used to meet other success criteria or not) [to] meet this success criterion.

Note 2 (Added)

Standard exit methods may vary by platform. For example, on many desktop platforms, the Escape key is a standard method for exiting.

Note 3 (Added) (for non-web software)

This criterion applies when focus can be moved using a keyboard interface. Some software may accept input from a keyboard, keypad, or controller, yet not offer any mechanism for focus; for example, the keys are mapped directly to functions without moving focus between on-screen controls. In this case, there is no concept of focus, and therefore keyboard traps cannot exist and this success criterion would be satisfied.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.1.4 Character Key Shortcuts

(Level A)

> If a [keyboard shortcut](https://www.w3.org/TR/WCAG22/#dfn-keyboard-shortcuts "alternative means of triggering an action by the pressing of one or more keys") is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:
>
> Turn off
> :   A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to turn the shortcut off;
>
> Remap
> :   A mechanism is available to remap the shortcut to include one or more non-printable keyboard keys (e.g., Ctrl, Alt);
>
> Active only on focus
> :   The keyboard shortcut for a [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") is only active when that component has focus.

###### Applying SC 2.1.4 Character Key Shortcuts to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.1.4](https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html).

Note 1 (Added) (for non-web software)

The WCAG2ICT interpretation is that a long press of a key (2 seconds or more) and other accessibility features provided by the platform do not meet the WCAG definition of a keyboard shortcut. See the [keyboard shortcut](#dfn-keyboard-shortcuts) definition for more details.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

#### 2.2 Enough Time

> Provide users enough time to read and use content.

##### Applying Guideline 2.2 Enough Time to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.2 applies directly as written.

##### 2.2.1 Timing Adjustable

(Level A)

> For each time limit that is set by the content, at least one of the following is true:
>
> Turn off
> :   The user is allowed to turn off the time limit before encountering it; or
>
> Adjust
> :   The user is allowed to adjust the time limit before encountering it over a wide range
>     that is at least ten times the length of the default setting; or
>
> Extend
> :   The user is warned before time expires and given at least 20 seconds to extend the
>     time limit with a simple action (for example, "press the space bar"), and the user
>     is allowed to extend the time limit at least ten times; or
>
> Real-time Exception
> :   The time limit is a required part of a [real-time event](https://www.w3.org/TR/WCAG22/#dfn-real-time-events "event that a) occurs at the same time as the viewing and b) is not completely generated by the content") (for example, an auction),
>     and no alternative to the time limit is possible; or
>
> Essential Exception
> :   The time limit is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") and extending it would invalidate the activity; or
>
> 20 Hour Exception
> :   The time limit is longer than 20 hours.
>
> Note
>
> This success criterion helps ensure that users can complete tasks without unexpected
> changes in content or context that are a result of a time limit. This success criterion
> should be considered in conjunction with [Success Criterion 3.2.1](https://www.w3.org/TR/WCAG22/#on-focus), which puts limits on changes of content or context as a result of user action.

###### Applying SC 2.2.1 Timing Adjustable to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable#intent), replacing “ content” with “non-web document or software”.

With this substitution, it would read:

**2.2.1 Timing Adjustable:** For each time limit that is set by the [**[non-web document](#document)** or **[software](#software)**], at least one of the following is true:

Turn off
:   The user is allowed to turn off the time limit before encountering it; or

Adjust
:   The user is allowed to adjust the time limit before encountering it over a wide range that is at least ten times the length of the default setting; or

Extend
:   The user is warned before time expires and given at least 20 seconds to extend the time limit with a simple action (for example, “press the space bar”), and the user is allowed to extend the time limit at least ten times; or

Real-time Exception
:   The time limit is a required part of a real-time event (for example, an auction), and no alternative to the time limit is possible; or

Essential Exception
:   The time limit is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential) and extending it would invalidate the activity; or

20 Hour Exception
:   The time limit is longer than 20 hours.

Note

This success criterion helps ensure that users can complete tasks without unexpected changes in content or context that are a result of a time limit. This success criterion should be considered in conjunction with [Success Criterion 3.2.1](https://www.w3.org/TR/WCAG22/#on-focus), which puts limits on changes of content or context as a result of user action.

##### 2.2.2 Pause, Stop, Hide

(Level A)

> For moving, [blinking](https://www.w3.org/TR/WCAG22/#dfn-blinking "switch back and forth between two visual states in a way that is meant to draw attention"), scrolling, or auto-updating information, all of the following are true:
>
> Moving, blinking, scrolling
> :   For any moving, blinking or scrolling information that (1) starts automatically, (2)
>     lasts more than five seconds, and (3) is presented in parallel with other content,
>     there is a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") for the user to [pause](https://www.w3.org/TR/WCAG22/#dfn-pause "stopped by user request and not resumed until requested by user"), stop, or hide it unless the movement, blinking, or scrolling is part of an activity
>     where it is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform"); and
>
> Auto-updating
> :   For any auto-updating information that (1) starts automatically and (2) is presented
>     in parallel with other content, there is a mechanism for the user to pause, stop,
>     or hide it or to control the frequency of the update unless the auto-updating is part
>     of an activity where it is essential.
>
> Note 1
>
> For requirements related to flickering or flashing content, refer to [Guideline 2.3](https://www.w3.org/TR/WCAG22/#seizures-and-physical-reactions).
>
> Note 2
>
> Since any content that does not meet this success criterion can interfere with a user's
> ability to use the whole page, all content on the web page (whether it is used to
> meet other success criteria or not) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).
>
> Note 3
>
> Content that is updated periodically by software or that is streamed to the user agent
> is not required to preserve or present information that is generated or received between
> the initiation of the pause and resuming presentation, as this may not be technically
> possible, and in many situations could be misleading to do so.
>
> Note 4
>
> An animation that occurs as part of a preload phase or similar situation can be considered
> essential if interaction cannot occur during that phase for all users and if not indicating
> progress could confuse users or cause them to think that content was frozen or broken.

###### Applying SC 2.2.2 Pause, Stop, Hide to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide#intent), replacing “page” with “non-web document or software” and “on the web page” with “in the non-web document or software”; removing “See Conformance Requirement 5: Non-Interference” in Note 2 of the success criterion; and adjusting Note 2 to avoid the use of the normative term "must".

With these substitutions, it would read:

**2.2.2 Pause, Stop, Hide:** For moving, [blinking](https://www.w3.org/TR/WCAG22/#dfn-blinking), scrolling, or auto-updating information, all of the following are true:

Moving, blinking, scrolling
:   For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content, there is a mechanism for the user to [pause](https://www.w3.org/TR/WCAG22/#dfn-pause)), stop, or hide it unless the movement, blinking, or scrolling is part of an activity where it is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential); and

Auto-updating
:   For any auto-updating information that (1) starts automatically and (2) is presented in parallel with other content, there is a mechanism for the user to pause, stop, or hide it or to control the frequency of the update unless the auto-updating is part of an activity where it is essential.

Note 1

For requirements related to flickering or flashing content, refer to [Guideline 2.3](https://www.w3.org/TR/WCAG22/#seizures-and-physical-reactions).

Note 2

Since any content that does not meet this success criterion can interfere with a user's ability to use the whole [**[non-web document](#document)** or **[software](#software)**], [it would be necessary for] all content [in the non-web document or software] (whether it is used to meet other success criteria or not) [to] meet this success criterion.

Note 3

Content that is updated periodically by software or that is streamed to the user agent is not required to preserve or present information that is generated or received between the initiation of the pause and resuming presentation, as this may not be technically possible, and in many situations could be misleading to do so.

Note 4

An animation that occurs as part of a preload phase or similar situation can be considered essential if interaction cannot occur during that phase for all users and if not indicating progress could confuse users or cause them to think that content was frozen or broken.

Note 5 (Added)

While the success criterion uses the term “information”, the WCAG 2 [Intent from Understanding Success Criterion 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide#intent) makes it clear that this is to be applied to all content. Any [content](#content-on-and-off-the-web), even if just decorative, that is updated automatically, blinks, or moves may create an accessibility barrier.

#### 2.3 Seizures and Physical Reactions

> Do not design content in a way that is known to cause seizures or physical reactions.

##### Applying Guideline 2.3 Seizures and Physical Reactions to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.3 applies directly as written.

##### 2.3.1 Three Flashes or Below Threshold

(Level A)

> [Web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") do not contain anything that flashes more than three times in any one second period,
> or the [flash](https://www.w3.org/TR/WCAG22/#dfn-flashes "a pair of opposing changes in relative luminance that can cause seizures in some people if it is large enough and in the right frequency range") is below the [general flash and red flash thresholds](https://www.w3.org/TR/WCAG22/#dfn-general-flash-and-red-flash-thresholds "a flash or rapidly changing image sequence is below the threshold (i.e., content passes) if any of the following are true:").
>
> Note
>
> Since any content that does not meet this success criterion can interfere with a user's
> ability to use the whole page, all content on the web page (whether it is used to
> meet other success criteria or not) must meet this success criterion. See [Conformance Requirement 5: Non-Interference](https://www.w3.org/TR/WCAG22/#cc5).

###### Applying SC 2.3.1 Three Flashes or Below Threshold to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold#intent), replacing “web pages” with “non-web documents or software” , “page” with “non-web document or software”, and “on the web page” with “in the non-web document or software”; removing “See Conformance Requirement 5: Non-Interference”; and adjusting Note 1 to avoid the use of the normative term "must".

With these substitutions, it would read:

**2.3.1 Three Flashes or Below Threshold:** [**[Non-web documents](#document)** or **[software](#software)**] do not contain anything that flashes more than three times in any one second period, or the [flash](https://www.w3.org/TR/WCAG22/#dfn-flashes) is below the [general flash and red flash thresholds](#dfn-general-flash-and-red-flash-thresholds).

Note 1

Since any content that does not meet this success criterion can interfere with a user's ability to use the whole [**[non-web document](#document)** or **[software](#software)**], [it would be necessary for] all content [in the non-web document or software] (whether it is used to meet other success criteria or not) [to] meet this success criterion.

Note 2 (Added) (for non-web software)

This requirement applies to flashing of content on a screen and flashing of any other type caused by the ICT.

Note 3 (Added) (for non-web software)

This requirement applies to those visual elements produced by the ICT itself. Content from an external source that is presented through the ICT, is the responsibility of the source. The requirement does not require the ICT to examine or modify such externally supplied content in any way.

Example (Added) (for non-web software): Examples of ICT that presents content from an external source include TVs playing broadcast programs and media players that are playing content provided by the user.

#### 2.4 Navigable

> Provide ways to help users navigate, find content, and determine where they are.

##### Applying Guideline 2.4 Navigable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.4 applies directly as written.

##### 2.4.1 Bypass Blocks

(Level A)

> A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to bypass blocks of content that are repeated on multiple [web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent").

###### Applying SC 2.4.1 Bypass Blocks to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 2.4.1](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks#intent), replacing “on multiple web pages” with “in multiple non-web documents in a set of non-web documents, or in multiple software programs in a set of software programs” to explicitly state that the multiple documents (or software programs) are part of a set rather than any two documents or pieces of software.

With these substitutions, this success criterion would read:

**2.4.1 Bypass Blocks:** A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to bypass blocks of content that are repeated [in multiple **[non-web documents](#document)** in a **[set of non-web documents](#set-of-documents)**, or in multiple **[software programs](#software)** in a **[set of software programs](#set-of-software-programs)**].

Note 1 (Added)

See [set of documents](#set-of-documents) and [set of software programs](#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

Individual documents or software programs (not in a set) would automatically satisfy this success criterion because this success criterion applies only to things that appear in a set.

Note 3 (Added)

Although not required by the success criterion, being able to bypass blocks of content that are repeated *within* non-web documents or software directly addresses user needs identified in the Intent section for this success criterion, and is generally considered best practice.

Note 4 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 5 (Added) (for non-web software)

Many software user interface components have built-in mechanisms to navigate directly to / among them, which also have the effect of skipping over or bypassing blocks of content.

Note 6 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.4.2 Page Titled

(Level A)

> [Web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") have titles that describe topic or purpose.

###### Applying SC 2.4.2 Page Titled to Non-Web Documents

This success criterion is problematic to apply directly to non-web documents through simple word substitution because not all document formats provide support for a programmatically determinable Title property, and document titles don't always describe the topic or purpose of the document. File names, as the WCAG 2 Understanding document specifies, also rarely describe the topic or purpose of the document – especially where the document names are not under the author’s control. However, where the document authoring tool or technology provides the capability to supply a title or name for a document, when the non-web document utilizes the Title property to provide a unique title or name inside of each document, and/or when a meaningful file name can be supplied, the user can more easily find it or understand its purpose. This would address the user needs identified in the [Intent from Understanding Success Criterion 2.4.2](https://www.w3.org/WAI/WCAG22/Understanding/page-titled#intent). The following criterion is recommended as a substitute for the WCAG language:

**2.4.2 Non-web Document Titled:** In non-web documents implemented in a format that supports a programmatically determinable Title property that is editable using common authoring tools for that document format, the non-web document has a title that describes the name, topic, or purpose.

Note (Added) (for non-web documents)

The Title property is specified as "editable through that document format’s common authoring tools" so that authors can view and edit the Title without requiring specialized or external metadata utilities. “Common authoring tools" are the most readily available tools used for editing a particular document type.

###### Applying SC 2.4.2 Page Titled to Non-Web Software

This success criterion is problematic to apply directly to non-web software through simple word substitution because application titles rarely describe the topic or purpose of the software. However, where the platform supports a programmatic title or name for a software window or screen, when a software application utilizes that feature to provide a unique title or name for each window or screen, the user can more easily find it or understand its purpose. This would address the user needs identified in the [Intent from Understanding Success Criterion 2.4.2](https://www.w3.org/WAI/WCAG22/Understanding/page-titled#intent). The following criterion is recommended as a substitute for the WCAG language:

**2.4.2 Non-web Software Titled:** In non-web software implemented on a platform that supports a Title property for windows or screens, the non-web software provides titles that describe the name, topic or purpose of each window or screen.

##### 2.4.3 Focus Order

(Level A)

> If a [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") can be [navigated sequentially](https://www.w3.org/TR/WCAG22/#dfn-navigated-sequentially "navigated in the order defined for advancing focus (from one element to the next) using a keyboard interface") and the navigation sequences affect meaning or operation, focusable components receive
> focus in an order that preserves meaning and operability.

###### Applying SC 2.4.3 Focus Order to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.3](https://www.w3.org/WAI/WCAG22/Understanding/focus-order#intent) replacing “a web page” with “non-web documents or software”.

With this substitution, it would read:

**2.4.3 Focus Order:** If [**[non-web documents](#document)** or **[software](#software)**] can be [navigated sequentially](https://www.w3.org/TR/WCAG22/#dfn-navigated-sequentially) and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability.

##### 2.4.4 Link Purpose (In Context)

(Level A)

> The [purpose of each link](https://www.w3.org/TR/WCAG22/#dfn-purpose-of-each-link "nature of the result obtained by activating a hyperlink") can be determined from the link text alone or from the link text together with its
> [programmatically determined link context](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determined-link-context "additional information that can be programmatically determined from relationships with a link, combined with the link text, and presented to users in different modalities"), except where the purpose of the link would be [ambiguous to users in general](https://www.w3.org/TR/WCAG22/#dfn-ambiguous-to-users-in-general "the purpose cannot be determined from the link and all information of the web page presented to the user simultaneously with the link (i.e., readers without disabilities would not know what a link would do until they activated it)").

###### Applying SC 2.4.4 Link Purpose (In Context) to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context#intent).

Note 1 (Added)

In non-web documents or software, a “link” is any user interface control that behaves like a hypertext link.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.4.5 Multiple Ways

(Level AA)

> More than one way is available to locate a [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization") except where the web page is the result of, or a step in, a [process](https://www.w3.org/TR/WCAG22/#dfn-processes "series of user actions where each action is required in order to complete an activity").

###### Applying SC 2.4.5 Multiple Ways to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 2.4.5](https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways#intent), replacing “web page within a set of web pages” with “non-web document within a set of non-web documents, or a set of software programs within a set of software programs” and "the web page" with "the non-web document or software program".

With these substitutions, this success criterion would read:

**2.4.5 Multiple Ways:** More than one way is available to locate a [**[non-web document](#document)** within a **[set of non-web documents](#set-of-documents)**, or a **[software program](#software)** within a **[set of software programs](#set-of-software-programs)**] except where [the non-web document or software program] is the result of, or a step in, a [process](https://www.w3.org/TR/WCAG22/#dfn-processes).

Note 1 (Added)

See [set of documents](#set-of-documents) and [set of software programs](#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

The definitions of “[set of documents](#set-of-documents)” and “[set of software programs](#set-of-software-programs)” in the Key Terms section are predicated on the ability to navigate from each element of the set to each other, and navigation is a type of locating. So the mechanism used to navigate between elements of the set will be one way of locating information in the set. Non-web environments, generally major operating systems with browse and search capabilities, often provide infrastructure and tools that provide mechanisms for locating content in a set of non-web documents or a set of software programs. For example, it may be possible to browse through the files or programs that make up a set, or search within members of the set for the names of other members. A file directory would be the equivalent of a site map for documents in a set, and a search function in a file system would be equivalent to a web search function for web pages. Such facilities may provide additional ways of locating information in the set.

Note 3 (Added)

While some users may find it useful to have multiple ways to locate some groups of user interface elements within a non-web document or software program, this is not required by the success criterion (and may pose difficulties in some situations).

Note 4 (Added)

The definitions of “[set of documents](#set-of-documents)” and “[set of software programs](#set-of-software-programs)” in WCAG2ICT require every item in the set to be independently reachable, and so nothing in such a set can be a “step in a process” that can't be reached any other way. The purpose of the exception—that items in a process are exempt from satisfying this success criterion—is achieved by the definition of set.

Note 5 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 6 (Added) (for non-web software)

An example of the use of “a software program that is part of process”, that would meet the exception for this success criterion, would be one where programs are interlinked but the interlinking depends on program A being used before program B, for validation or to initialize the dataset, etc.

Note 7 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.4.6 Headings and Labels

(Level AA)

> Headings and [labels](https://www.w3.org/TR/WCAG22/#dfn-labels "text or other component with a text alternative that is presented to a user to identify a component within web content") describe topic or purpose.

###### Applying SC 2.4.6 Headings and Labels to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.6](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels#intent).

Note (Added) (for non-web software)

In non-web [software](#software), headings and labels are used to describe sections of [content](#content-on-and-off-the-web) and controls respectively. In some cases it may be unclear whether a piece of static text is a heading or a label. But whether treated as a label or a heading, the requirement is the same: that if they are present they describe the topic or purpose of the item(s) they are associated with.

##### 2.4.7 Focus Visible

(Level AA)

> Any keyboard operable user interface has a mode of operation where the keyboard [focus indicator](https://www.w3.org/TR/WCAG22/#dfn-focus-indicator "New") is visible.

###### Applying SC 2.4.7 Focus Visible to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.4.11 Focus Not Obscured (Minimum)

(Level AA)

> When a [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") receives keyboard focus, the component is not entirely hidden due to author-created content.
>
> Note 1
>
> Where content in a configurable interface can be repositioned by the user, then only the initial positions of user-movable content are considered for testing and conformance of this success criterion.
>
> Note 2
>
> Content opened by the *user* may obscure the component receiving focus. If the user can reveal the focused component without advancing the keyboard focus, the component with focus is not considered visually hidden due to author-created content.

###### Applying SC 2.4.11 Focus not Obscured to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum#intent).

#### 2.5 Input Modalities

> Make it easier for users to operate functionality through various inputs beyond keyboard.

##### Applying Guideline 2.5 Input Modalities to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 2.5 applies directly as written.

##### 2.5.1 Pointer Gestures

(Level A)

> All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that uses multipoint or path-based gestures for operation can be operated with a [single pointer](https://www.w3.org/TR/WCAG22/#dfn-single-pointer "an input modality that only targets a single point on the page/screen at a time – such as a mouse, single finger on a touch screen, or stylus.") without a path-based gesture, unless a multipoint or path-based gesture is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform").
>
> Note
>
> This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

###### Applying SC 2.5.1 Pointer Gestures to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.1](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures#intent), making changes to the notes for non-web documents by replacing “web content” with "content", for non-web software by replacing "web content that interprets" with "non-web software that interprets" and "user agent" with "underlying platform software".

With these substitutions, the notes would read:

Note 1 (for non-web documents)

This requirement applies to [**[content](#content-on-and-off-the-web)**] that interprets pointer actions (i.e., this does not apply to actions that are required to operate the [user agent](#user-agent) or [assistive technology](#dfn-assistive-technologies)).

Note 2 (Added) (for non-web documents)

Multipoint and path-based gestures are less common in non-web documents. An example where a non-web document author could add such gestures is an interactive prototype document created in a software design tool.

Note 3 (for non-web software)

This requirement applies to [non-web **[software](#software)** that interprets] pointer actions (i.e., this does not apply to actions that are required to operate the [underlying **[platform software](#platform-software)**] or assistive technology).

Note 4 (Added) (for non-web software)

This requirement also applies to platform software, such as user agents, assistive technology software, and operating systems. Each layer is responsible for its own pointer actions only, not for those in an underlying layer.

##### 2.5.2 Pointer Cancellation

(Level A)

> For [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that can be operated using a [single pointer](https://www.w3.org/TR/WCAG22/#dfn-single-pointer "an input modality that only targets a single point on the page/screen at a time – such as a mouse, single finger on a touch screen, or stylus."), at least one of the following is true:
>
> No Down-Event
> :   The [down-event](https://www.w3.org/TR/WCAG22/#dfn-down-event "platform event that occurs when the trigger stimulus of a pointer is depressed") of the pointer is not used to execute any part of the function;
>
> Abort or Undo
> :   Completion of the function is on the [up-event](https://www.w3.org/TR/WCAG22/#dfn-up-event "platform event that occurs when the trigger stimulus of a pointer is released"), and a [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to abort the function before completion or to undo the function after completion;
>
> Up Reversal
> :   The up-event reverses any outcome of the preceding down-event;
>
> Essential
> :   Completing the function on the down-event is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform").
>
> Note 1
>
> Functions that emulate a keyboard or numeric keypad key press are considered essential.
>
> Note 2
>
> This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

###### Applying SC 2.5.2 Pointer Cancellation to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.2](https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html#intent), making changes to the notes for non-web documents by replacing “web content” with "content", for non-web software by replacing "web content that interprets" with "non-web software that interprets" and "user agent" with "underlying platform software".

With these substitutions, the notes would read:

Note 1 (for non-web documents)

Functions that emulate a keyboard or numeric keypad key press are considered essential.

Note 2 (for non-web documents)

This requirement applies to [**[content](#content-on-and-off-the-web)**] that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

Note 3 (Added) (for non-web documents)

Content that interprets pointer actions and controls which events are used for executing functionality is less common in non-web documents. An example where a non-web document author could add such functionality is an interactive prototype document created in a software design tool.

Note 4 (for non-web software)

Functions that emulate a keyboard or numeric keypad key press are considered essential.

Example (Added) (for non-web software): Examples of essential functionality for non-web software are features for meeting environmental energy usage requirements (like waking a device from sleep, power saver mode, and low power state).

Note 5 (for non-web software)

This requirement applies to [non-web **[software](#software)** that interprets] pointer actions (i.e., this does not apply to actions that are required to operate the [underlying **[platform software](#platform-software)**] or assistive technology).

Note 6 (Added) (for non-web software)

This requirement also applies to platform software, such as user agents, assistive technology software, and operating systems. Each layer is responsible for its own pointer actions only, not for those in an underlying layer.

Note 7 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.5.3 Label in Name

(Level A)

> For [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") with [labels](https://www.w3.org/TR/WCAG22/#dfn-labels "text or other component with a text alternative that is presented to a user to identify a component within web content") that include [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language") or [images of text](https://www.w3.org/TR/WCAG22/#dfn-images-of-text "text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect"), the [name](https://www.w3.org/TR/WCAG22/#dfn-name "text by which software can identify a component within web content to the user") contains the text that is presented visually.
>
> Note
>
> A best practice is to have the text of the label at the start of the name.

###### Applying SC 2.5.3 Label in Name to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 2.5.4 Motion Actuation

(Level A)

> [Functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that can be operated by device motion or user motion can also be operated by [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") and responding to the motion can be disabled to prevent accidental actuation, except when:
>
> Supported Interface
> :   The motion is used to operate functionality through an [accessibility supported](https://www.w3.org/TR/WCAG22/#dfn-accessibility-supported "supported by users' assistive technologies as well as the accessibility features in browsers and other user agents") interface;
>
> Essential
> :   The motion is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") for the function and doing so would invalidate the activity.

###### Applying SC 2.5.4 Motion Actuation to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.4](https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html#intent).

##### 2.5.7 Dragging Movements

(Level AA)

> All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality "processes and outcomes achievable through user action") that uses a [dragging movement](https://www.w3.org/TR/WCAG22/#dfn-dragging-movements "New") for operation can be achieved by a [single pointer](https://www.w3.org/TR/WCAG22/#dfn-single-pointer "an input modality that only targets a single point on the page/screen at a time – such as a mouse, single finger on a touch screen, or stylus.") without dragging, unless dragging is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") or the functionality is determined by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and not modified by the author.
>
> Note
>
> This requirement applies to web content that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

###### Applying SC 2.5.7 Dragging Movements to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html#intent), replacing "user agent" with "user agent or other platform software" and by making changes to the notes for non-web documents by replacing “web content” with "content", and for non-web software by replacing "web content that interprets" with "non-web software that interprets" and "user agent" with "underlying platform software".

With these substitutions, it would read:

**2.5.7 Dragging Movements:** All [functionality](https://www.w3.org/TR/WCAG22/#dfn-functionality) that uses a [dragging movement](https://www.w3.org/TR/WCAG22/#dfn-dragging-movements) for operation can be achieved by a [single pointer](https://www.w3.org/TR/wcag22/#dfn-single-pointer) without dragging, unless dragging is [essential](https://www.w3.org/TR/wcag22/#dfn-essential) or the functionality is determined by the [**[user agent](#user-agent)** or other **[platform software](#platform-software)**] and not modified by the author.

Note 1 (for non-web documents)

This requirement applies to [**[content](#content-on-and-off-the-web)**] that interprets pointer actions (i.e., this does not apply to actions that are required to operate the user agent or assistive technology).

Note 2 (Added) (for non-web documents)

Dragging movements for operation are less common in non-web documents. An example where a document author could add dragging functionality is an interactive prototype document created in a software design tool.

Note 3 (for non-web software)

This requirement applies to [non-web **[software](#software)** that interprets] pointer actions (i.e., this does not apply to actions that are required to operate the [underlying platform software] or assistive technology).

Note 4 (Added) (for non-web software)

This requirement also applies to platform software, such as user agents, assistive technology software, and operating systems. Each layer is responsible for its own pointer actions only, not for those in an underlying layer.

##### 2.5.8 Target Size (Minimum)

(Level AA)

> The size of the [target](https://www.w3.org/TR/WCAG22/#dfn-targets "region of the display that will accept a pointer action, such as the interactive area of a user interface component") for [pointer inputs](https://www.w3.org/TR/WCAG22/#dfn-pointer-inputs "input from a device that can target a specific coordinate (or set of coordinates) on a screen, such as a mouse, pen, or touch contact") is at least 24 by 24 [CSS pixels](https://www.w3.org/TR/WCAG22/#dfn-css-pixels "visual angle of about 0.0213 degrees"), except when:
>
> Spacing
> :   Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the [bounding box](https://www.w3.org/TR/WCAG22/#dfn-bounding-boxes "New") of each, the circles do not intersect another target or the circle for another undersized target;
>
> Equivalent
> :   The function can be achieved through a different control on the same page that meets this criterion;
>
> Inline
> :   The target is in a sentence or its size is otherwise constrained by the line-height of non-target text;
>
> User Agent Control
> :   The size of the target is determined by the [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users") and is not modified by the author;
>
> Essential
> :   A particular [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation "rendering of the content in a form to be perceived by users") of the target is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform") or is legally required for the information being conveyed.
>
> Note 1
>
> Targets that allow for values to be selected spatially based on position within the target are considered one target for the purpose of the success criterion. Examples include sliders, color pickers displaying a gradient of colors, or editable areas where you position the cursor.
>
> Note 2
>
> For inline targets the line-height should be interpreted as perpendicular to the flow of text. For example, in a language displayed vertically, the line-height would be horizontal.

###### Applying SC 2.5.8 Target Size (Minimum) to Non-Web Documents and Software:

This applies directly as written, and as described in [Intent from Understanding Success Criterion 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html#intent), replacing "user agent" with "user agent or other platform software" and "on the same page" with "in the same non-web document or software".

With these substitutions, it would read:

**2.5.8 Target Size (Minimum):** The size of the [target](#dfn-targets) for [pointer inputs](https://www.w3.org/TR/WCAG22/#dfn-pointer-inputs) is at least 24 by 24 [CSS pixels](#dfn-css-pixels), except when:

Spacing
:   Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the [bounding box](https://www.w3.org/TR/WCAG22/#dfn-bounding-boxes) of each, the circles do not intersect another target or the circle for another undersized target;

Equivalent
:   The function can be achieved through a different control [in the same **[non-web document](#document)** or **[software](#software)**] that meets this criterion.

Inline
:   The target is in a sentence or its size is otherwise constrained by the line-height of non-target text;

[User agent or other platform software] control
:   The size of the target is determined by the [**[user agent](#user-agent)** or other **[platform software](#platform-software)**] and is not modified by the author;

Essential
:   A particular [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation) of the target is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential) or is legally required for the information being conveyed.

Note 1

Targets that allow for values to be selected spatially based on position within the target are considered one target for the purpose of the success criterion. Examples include sliders, color pickers displaying a gradient of colors, or editable areas where you position the cursor.

Note 2

For inline targets the line-height should be interpreted as perpendicular to the flow of text. For example, in a language displayed vertically, the line-height would be horizontal.

Note 3 (Added)

In technologies where CSS is not used, the definition of 'CSS pixel' applies as described in [Applying “CSS pixel” to Non-Web Documents and Software](#applying-css-pixel-to-non-web-documents-and-software).

Note 4 (Added) (for non-web documents)

Some non-web document formats are designed for viewing at a wide range of zoom levels provided by the user agent. However, the commonly available user agents for these formats may lack a consistent base zoom level from which to evaluate this criterion. For such documents, evaluate target sizes at a zoom level that aligns with the intended usage of the content.

Note 5 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).