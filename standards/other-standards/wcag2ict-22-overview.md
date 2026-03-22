---
ai_context: Overview of WCAG2ICT scope, terminology, closed functionality, text interfaces,
  and conformance notes.
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
- overview
- documents
- software
- ict
title: WCAG2ICT 2.2 Overview
---

# WCAG2ICT 2.2 Overview

## Abstract

This document describes how the Web Content Accessibility Guidelines (WCAG) versions 2.0 [[WCAG20](#bib-wcag20 "Web Content Accessibility Guidelines (WCAG) 2.0")], 2.1 [[WCAG21](#bib-wcag21 "Web Content Accessibility Guidelines (WCAG) 2.1")], and 2.2 [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")] principles, guidelines, and success criteria can be applied to non-web Information and Communications Technologies (ICT), specifically to non-web documents and software. It provides informative guidance (guidance that is not normative and does not set requirements).

This document is part of a series of technical and educational documents published by the [W3C Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/) and available from the [WCAG2ICT Overview](https://www.w3.org/WAI/standards-guidelines/wcag/non-web-ict/).

## Status of This Document

*This section describes the status of this
document at the time of its publication. A list of current W3C
publications and the latest revision of this technical report can be found
in the
[W3C standards and drafts index](https://www.w3.org/TR/).*

This is a W3C Group Note on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT). The purpose of this work is to update the previous WCAG2ICT Note's guidance to include changes made in WCAG 2.1 and 2.2, as well as to address public feedback received after first publication of this updated Note.

To comment, file an issue in the [W3C WCAG2ICT](https://github.com/w3c/wcag2ict/) GitHub repository. Create separate GitHub issues for each topic, rather than commenting on multiple topics in a single issue. It is free to create a GitHub account to file issues. If filing issues in GitHub is not feasible, send email to [public-wcag2ict-comments@w3.org](mailto:public-wcag2ict-comments@w3.org) (comment archive).

This document was published by the [Accessibility Guidelines Working Group](https://www.w3.org/groups/wg/ag) as
a Group Note using the
[Note track](https://www.w3.org/policies/process/20250818/#recs-and-notes).

This Group Note is endorsed by
the [Accessibility Guidelines Working Group](https://www.w3.org/groups/wg/ag), but is not endorsed by
W3C itself nor its
Members.

The
[W3C Patent
Policy](https://www.w3.org/policies/patent-policy/)
does not carry any licensing requirements or commitments on this
document.

This document is governed by the
[18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/).

## Introduction

### Background

This document is an update to a W3C [Working Group Note](https://www.w3.org/2005/10/Process-20051014/tr#WGNote) to incorporate new guidelines, success criteria, and definitions added in WCAG 2.1 and 2.2.

[Guidance on Applying WCAG 2.0 to Non-Web Information and Communications Technologies (WCAG2ICT)](https://www.w3.org/TR/2013/NOTE-wcag2ict-20130905/), approved in September 2013, described how WCAG 2.0 could be applied to non-web documents and software. WCAG2ICT was organized to mirror WCAG's sections: Perceivable, Operable, Understandable, and Robust. WCAG2ICT clarified when and how WCAG success criteria could be applied to non-web documents and software. Some were applicable without modification and some were applicable with edits and/or notes. Glossary terms were also reviewed. Level AAA success criteria were not addressed in the 2013 WCAG2ICT Working Group Note.

The 2013 version of WCAG2ICT has been relied upon in regulations and legislation. An example is [[etsi-en-301-549](#bib-etsi-en-301-549 "ETSI EN 301 549 V3.2.1 (2021-03): Accessibility requirements for ICT products and services")] (Europe) as well as other standards that reference or incorporate EN 301 549 (e.g., India, Kenya, Australia). Another example is the U.S. Section 508’s [Application of WCAG 2.0 to Non-Web ICT](https://www.federalregister.gov/documents/2017/01/18/2017-00395/information-and-communication-technology-ict-standards-and-guidelines#h-36), where WCAG was incorporated by reference into Section 508 as the [accessibility standard applicable to non-web documents](https://www.access-board.gov/ict/#E205.4) and which also requires [WCAG conformance for non-web software](https://www.access-board.gov/ict/#E207.2).

These standards looked to WCAG2ICT for detailed direction and guidance on how to apply WCAG non-web technology. The WCAG2ICT guidance also led to a few exceptions where specific success criteria are not required in non-web contexts.

### Guidance in This Document

This document provides informative guidance (guidance that is not [normative](https://www.w3.org/TR/WCAG22/#dfn-normative) and does not set requirements) with regard to the interpretation and application of Web Content Accessibility Guidelines (WCAG) to non-web information and communications technologies (ICT). This document is a [Working Group Note](https://www.w3.org/2021/Process-20211102/#WGNote) (in contrast to WCAG 2.0, WCAG 2.1, and WCAG 2.2, which are W3C Recommendations). Specifically, this document provides informative guidance on applying WCAG 2.0, 2.1, and 2.2 Level A and AA success criteria to non-web ICT, specifically to non-web documents and software.

Note 1

Hereafter, the use of WCAG 2 means all WCAG 2.x versions — 2.0, 2.1, and 2.2.

This document is intended to help clarify how to use WCAG 2 to make non-web documents and software more accessible to people with disabilities. Addressing accessibility involves addressing the needs of people with auditory, cognitive, neurological, physical, speech, and visual impairments, as well as the accessibility needs of people caused by the effects of aging. Although WCAG 2 addresses some user needs for people with cognitive and learning disabilities, as well as those with mental health-related disabilities, following the WCAG supplement [Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) is recommended for non-web ICT in order to address the user needs of these groups. Developers are also encouraged to obtain testing input from people with disabilities who use their applications and content.

Although this document covers a wide range of issues, it is not able to address all the needs of all people with disabilities. Since WCAG 2 was developed for the Web, addressing accessibility for non-web documents and software may involve requirements and considerations beyond those included in this document. Authors and developers are encouraged to seek relevant advice about current best practices to ensure that non-web documents and software are as accessible as possible to people with disabilities. The following supporting documents contain helpful information for learning about the user needs, intent, and generalized implementation techniques to support a wider range of people with disabilities:

- [WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [Techniques for WCAG 2.2](https://www.w3.org/WAI/WCAG22/Techniques/) [[WCAG22-TECHS](#bib-wcag22-techs "Techniques for WCAG 2.2")]
- [How to Meet WCAG (Quick Reference)](https://www.w3.org/WAI/WCAG22/quickref/)
- [Additional Accessibility Guidelines Working Group - Publications](https://www.w3.org/groups/wg/ag/publications/)

While WCAG 2 was designed to be technology neutral, it assumes the presence of a “user agent” such as a browser, media player, or assistive technology that is used as a means to access web content. As a result, the application of WCAG 2 to documents and software in non-web contexts necessitates some interpretation in order to determine how the intent of each WCAG 2 success criterion could be met in these different contexts of use. Therefore, the bulk of the WCAG2ICT Task Force's work involved evaluating how each WCAG 2 success criterion would apply in the context of non-web ICT.

The WCAG2ICT Task Force found that the majority of WCAG 2 success criteria can be applied to non-web documents and software with either no or minimal changes. Since many of the Level A and Level AA success criteria do not include any web-related terms, they apply directly as written and as described in the “Intent” sections from the [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/) [[UNDERSTANDING-WCAG22](#bib-understanding-wcag22 "Understanding Web Content Accessibility Guidelines 2.2")] resource. Additional notes were provided, as needed, to increase understanding about applying WCAG success criteria to non-web documents and software.

#### Interpretation of Web Terminology in a Non-Web Context

When certain web-specific terms or phrases like “web page(s)” were used in success criteria, those were replaced with non-web terms or phrases like “non-web document(s) and software”. Additional notes were also provided to explain the terminology replacements.

A small number of success criteria are written to apply to “a set of web pages” or “multiple web pages” and depend upon all pages in the set to share some characteristic or behavior. Since the unit of conformance in WCAG 2 is a single web page, the task force agreed that the equivalent unit of conformance for non-web documents is a single document. It follows that an equivalent unit of evaluation for a “set of web pages” would be a “set of documents”. Since it isn't possible to unambiguously carve up non-web software into discrete pieces, a single “web page” was equated to a “software program” and a “set of web pages” was equated to a “set of software programs”.  Both of these terms are defined in the Key Terms section of this document. See “[set of documents](#set-of-documents)” and “[set of software programs](#set-of-software-programs)” to determine when a group of documents or pieces of software are considered a set.

Note

Sets of non-web software that meet this definition appear to be extremely rare.

Not all success criteria have been fully adopted in all local regulations and legislation, and may not be applicable to all technologies. WCAG2ICT has been used in some regulations to determine whether or not to apply certain success criteria. For example, some local standards such as Section 508 in the U.S., and EN 301 549 in Europe, state that WCAG 2.0 Success Criteria 2.4.1 Bypass Blocks, 2.4.5 Multiple Ways, 3.2.3 Consistent Navigation, and 3.2.4 Consistent Identification do not apply to non-web documents and non-web software. In addition, EN 301 549 states that 2.4.2 Page Titled and 3.1.2 Language of Parts do not apply to non-web software. In contrast, the U.S. Department of Justice regulation, Nondiscrimination on the Basis of Disability; Accessibility of Web Information and Services of State and Local Government Entities (89 FR 31320, 24 April 2024), directs implementers to utilize the guidance in this document to determine the applicability of success criteria and how to apply the requirements to mobile applications. Since this document does not specifically say which criteria can or should apply, those implementing this document (WCAG2ICT) should consider the applicability of individual success criteria to non-web documents and software.

The glossary terms in WCAG 2 were also reviewed and most of them applied to non-web documents and software, as written. Some applied with additional notes or edits (largely related to phrases like “web page(s)”), and a small number of terms were only used in Level AAA success criteria, which are not addressed by the WCAG2ICT Note at this time.

### Excluded from Scope

The following are out of scope for this document:

- This document does not seek to determine which WCAG 2 provisions (principles, guidelines, or success criteria) should or should not apply to non-web documents and software, but rather — if applied — *how* they would apply.
- This document does not propose changes to WCAG 2 or its supporting documents. However, during the development of this document, the WCAG2ICT Task Force did seek clarification on the intent of a number of the success criteria, which led to clarifications in the Understanding WCAG 2 document.
- This document does not include interpretations for implementing WCAG 2 in web technologies.
- This document is not sufficient by itself to ensure accessibility in non-web documents and software. This is because this document does not address accessibility requirements beyond those covered by WCAG which, as a web standard, does not fully cover all accessibility requirements for non-user interface aspects of platforms, user-interface components as individual items, or ICT with closed functionality (where there is no assistive technology to communicate programmatic information).
- This document does not comment on hardware aspects of products because the basic constructs on which WCAG 2 is built do not apply to hardware.
- This document does not provide supporting techniques for implementing WCAG 2 in non-web documents and software.
- This document is purely an informative Note about non-web ICT. It is not a standard — so it does not describe how non-web ICT should conform to it.

### Document Overview

This document includes text quoted from the WCAG 2.2 principles, guidelines, success criteria, and glossary definitions without any changes. The guidance provided by this document for each principle, guideline, success criterion, and definition is preceded by a heading beginning with “Applying…”. This guidance was created by the WCAG2ICT Task Force, then reviewed and approved by the Accessibility Guidelines Working Group.

### Document Conventions

The following stylistic conventions are used in this document:

- Quotes from WCAG 2 are in `<blockquote>` elements and visually styled with a gray bar on the left, and immediately follow the heading for the principle, guideline, or success criterion.
- Additional guidance provided by this document begins with the phrase “Applying” and has no special visual styling.
- Replacement text that is presented to show how a success criterion would read as modified by the advice in this document are in `<ins>` elements that are visually styled as green text with a dotted underline.
- Links that are contained in the word replacement text are also styled with bold text.
- Notes are slightly inset and begin with the phrase “NOTE” — each note is in its own inset box that is styled in pale green with a darker green line on the left side of the box.
- Where WCAG Notes have been replaced or significantly rewritten in the guidance, they are notated with "(REPLACED)"; and where WCAG2ICT added new notes, they are notated with "(ADDED)".
- References to glossary items from WCAG 2 are presented in `<cite>` elements that are visually styled as ordinary text with a dotted underline, and contain title attributes noting these are WCAG definitions — they turn blue with a yellow background when mouse or keyboard focus is placed over them.
- References to glossary items in this document are presented in `<cite>` elements that are visually styled as ordinary text with a dark gray underline.
- Hereafter, the short title “WCAG2ICT” is used to reference this document.
- In headings, the term "Success Criterion" has been shortened to “SC” for brevity.

### Comparison with the 2013 WCAG2ICT Note

The following changes and additions have been made to update the 2013 WCAG2ICT document to incorporate the [new features in WCAG 2.1](https://www.w3.org/TR/WCAG21/#new-features-in-wcag-2-1), the [new features in WCAG 2.2](https://www.w3.org/TR/WCAG22/#new-features-in-wcag-2-2), and the change to 4.1.1 Parsing listed in the [Comparison with WCAG 2.1](https://www.w3.org/TR/WCAG22/#comparison-with-wcag-2-1) section:

- New [Background](#background) section to explain the history and known uses of WCAG2ICT
- New key terms introduced by WCAG2ICT:
  - [closed functionality](#closed-functionality)
  - [menu-driven interface](#menu-driven-interface)
  - [platform software](#platform-software)
  - [virtual keyboard](#virtual-keyboard)
- New WCAG 2.1 success criteria and guidelines:
  - [Success Criterion 1.3.4 Orientation](#orientation)
  - [Success Criterion 1.3.5 Identify Input Purpose](#identify-input-purpose)
  - [Success Criterion 1.4.10 Reflow](#reflow)
  - [Success Criterion 1.4.11 Non-text Contrast](#non-text-contrast)
  - [Success Criterion 1.4.12 Text Spacing](#text-spacing)
  - [Success Criterion 1.4.13 Content on Hover or Focus](#content-on-hover-or-focus)
  - [Success Criterion 2.1.4 Character Key Shortcuts](#character-key-shortcuts)
  - [Guideline 2.5 Input Modalities](#input-modalities)
  - [Success Criterion 2.5.1 Pointer Gestures](#pointer-gestures)
  - [Success Criterion 2.5.2 Pointer Cancellation](#pointer-cancellation)
  - [Success Criterion 2.5.3 Label in Name](#label-in-name)
  - [Success Criterion 2.5.4 Motion Actuation](#motion-actuation)
  - [Success Criterion 4.1.3 Status Messages](#status-messages)
- New WCAG 2.2 success criteria:
  - [Success Criterion 2.4.11 Focus Not Obscured (Minimum)](#focus-not-obscured-minimum)
  - [Success Criterion 2.5.7 Dragging Movements](#dragging-movements)
  - [Success Criterion 2.5.8 Target Size (Minimum)](#target-size-minimum)
  - [Success Criterion 3.2.6 Consistent Help](#consistent-help)
  - [Success Criterion 3.3.7 Redundant Entry](#redundant-entry)
  - [Success Criterion 3.3.8 Accessible Authentication (Minimum)](#accessible-authentication-minimum)
- Obsolete and Removed WCAG 2.2 success criteria that have errata for WCAG 2.0 and 2.1:
  - [Success Criterion 4.1.1 Parsing](#parsing22)
- New terms from WCAG 2.1 and 2.2:
  - added to [Glossary Items that Apply to All Technologies](#glossary-items-that-apply-to-all-technologies):
    - dragging movements, focus indicator, minimum bounding box, pointer input, process, single pointer, state, and status message
  - added to [Glossary Items Used only in AAA Success Criteria](#glossary-items-used-only-in-aaa-success-criteria):
    - motion animation, perimeter, region, and user inactivity
  - added to [Glossary Items with Specific Guidance](#glossary-items-with-specific-guidance):
    - [cognitive function test](#dfn-cognitive-function-test)
    - [css pixel](#dfn-css-pixels)
    - [down event](#dfn-down-event)
    - [keyboard shortcut](#dfn-keyboard-shortcuts)
    - [style property](#dfn-style-properties)
    - [target](#dfn-targets)
    - [up event](#dfn-up-event)
- Updated terms:
  - [large scale](#dfn-large-scale)
  - [set of web pages](#dfn-set-of-web-pages)
  - [set of non-web documents](#set-of-documents)
  - [set of software programs](#set-of-software-programs)
- Updated sections:

  Note

  - All of the existing sections have undergone WCAG2ICT Task Force review to identify the necessary updates.
  - Many sections needed only minor editorial and link URL updates, such as the guidance for the WCAG 2.0 success criteria.

## Key Terms

WCAG2ICT provides some key glossary terms to address differences between web and non-web contexts and to introduce terms that are nonexistent in WCAG but important to define for a non-web context. “Content” and “user agent” are glossary terms from WCAG 2 that need to be interpreted significantly differently when applied to non-web ICT. The glossary term “web page” in WCAG 2 is replaced with the defined terms “document” and “software”, and both “set of web pages” and “multiple web pages” are replaced with the defined terms “set of documents” and “set of software programs”. The terms introduced by WCAG2ICT are “accessibility services of platform software” because non-web software doesn't leverage the WCAG notion of a user agent, and "closed functionality" which is specific to non-web software. The remaining glossary terms from WCAG 2 are addressed in [Chapter 7 Comments on Definitions in WCAG 2 Glossary](#comments-on-definitions-in-wcag-2-glossary). Terms defined and used in WCAG2ICT are applicable only to the interpretation of the guidance in this document. The particular definitions should not be interpreted as having applicability to situations beyond the scope of WCAG2ICT. Further information on usage of these terms follows.

### Accessibility Services of Platform Software

The term **accessibility services of platform software**, as used in WCAG2ICT, has the meaning below:

accessibility services of platform software (as used in WCAG2ICT)
:   services provided by an operating system, [user agent](#user-agent), or other [platform software](#platform-software) that enable non-web [documents](#document) or [software](#software) to expose information about the user interface and events to assistive technologies and accessibility features of software

Note

These services are commonly provided in the form of accessibility APIs (application programming interfaces), and they provide two-way communication with assistive technologies, including exposing information about objects and events.

### Closed Functionality

The term **closed functionality**, as used in WCAG2ICT, has the meaning below:

closed functionality (as used in WCAG2ICT)
:   a property or characteristic that prevents users from attaching, installing, or using [assistive technology](#dfn-assistive-technologies)

Note 1

To support users with disabilities, ICT with closed functionality might instead provide built-in features that function as assistive technology or use other mechanisms to make the technology accessible.

Example: Examples of technology that may have closed functionality include but are not limited to:

- self-service transaction machines or kiosks — examples include machines used for retail self-checkout, point of sales (POS) terminals, ticketing and self-check-in, and Automated Teller Machines (ATMs).
- telephony devices such as internet phones, feature phones, smartphones, and phone-enabled tablets
- educational devices such as interactive whiteboards and smart boards
- entertainment technologies including gaming platforms or consoles, smart TVs, set-top boxes, smart displays, smart speakers, smart watches, and tablets
- an ebook reader or standalone ebook software that allows assistive technologies to access all of the user interface controls of the ebook program (open functionality) but does not allow the assistive technologies to access the actual content of book (closed functionality).
- medical devices such as digital blood pressure monitors, glucose meters, or other wearable devices
- an operating system that makes the user provide login credentials before it allows any assistive technologies to be loaded. The login portion would be closed functionality.
- other technology devices, such as printers, displays, and Internet of Things (IoT) devices

Note 2

Some of these technologies, though closed to some external assistive technologies, often have extensive internal accessibility features that serve as assistive technology that can be used by applications on these devices in the same way assistive technology is used on fully open devices, such as desktop computers. Others are open to some types of assistive technology but not others.

### Content (on and off the web)

WCAG 2 defines **content** as:

> information and sensory experience to be communicated to the user by means of a [user agent](https://www.w3.org/TR/WCAG22/#dfn-user-agents), including code or markup that defines the content's [structure](https://www.w3.org/TR/WCAG22/#dfn-structure), [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation), and interactions

For non-web content it is necessary to view this a bit more broadly. Within WCAG2ICT, the term “content” is used as follows:

content (non-web content) (as used in WCAG2ICT)
:   information and sensory experience to be communicated to the user by means of **[[software](#software)]**, including code or markup that defines the content's [structure](#dfn-structure), [presentation](https://www.w3.org/TR/WCAG22/#dfn-presentation), and interactions

Note 1

Non-web content occurs in two places; documents and software. When content occurs in a non-web document, a user agent is needed in order to communicate the content's information and sensory experience to the user. When content occurs in non-web software, a separate user agent isn't needed — the software itself performs that function.

Note 2

Content from a third party needs special consideration since sometimes it may be under the control of the author (e.g. contracted and therefore may not be considered 3rd party) and sometimes it is completely out of the control of the author (e.g. email in an email client).

Note 3

For non-web software, content also includes the user interface.

Note 4

Within WCAG2ICT wherever “content” or “web content” appears in a success criterion it is replaced with “content” using the definition above.

### Document

The term **document**, as used in WCAG2ICT, has the meaning below:

document (as used in WCAG2ICT)
:   assembly of [content](#content-on-and-off-the-web), such as a file, set of files, or streamed media that functions as a single item rather than a collection, that is not part of software and that does not include its own user agent

Note 1

A document always depends upon a user agent to present its content to the user.

Note 2

Letters, spreadsheets, emails, books, pictures, presentations, and movies are examples of documents.

Note 3

Software configuration and storage files such as databases and virus definitions, as well as computer instruction files such as source code, batch/script files, and firmware, are examples of files that function as part of [software](#software) and thus are not examples of documents. If and where software retrieves “information and sensory experience to be communicated to the user” from such files, it is just another part of the content that occurs in software and is covered by WCAG2ICT like any other parts of the software. Where such files contain one or more embedded documents, the embedded documents remain documents under this definition.

Note 4

A collection of files zipped together into an archive, stored within a single virtual hard drive file, or stored in a single "encrypted file system" file, do not constitute a single document.

Note 5

Anything that can present its own content without involving a user agent, such as a self-playing book, is not a document but is software.

Note 6

A single document may be composed of multiple files such as the video content, closed caption text, etc. This fact is not usually apparent to the end-user consuming the document / content. This is similar to how a single web page can be composed of content from multiple URIs (e.g. the page text, images, the JavaScript, a CSS file etc.).

Example: An assembly of files that represented the video, audio, captions, and timing files for a movie would be a document.

Counterexample: A binder file used to bind together the various exhibits for a legal case would not be a document.

### Menu-driven Interface

The term **menu-driven interface**, as used in WCAG2ICT, has the meaning below:

menu-driven interface (as used in WCAG2ICT)
:   an interface composed of menus and sub-menus which the user accesses by pressing buttons or using a touch-screen

Example: Products that have a menu-driven interface include, but are not limited to, self-service transaction machines, printers, and IP-based telephones.

### Platform Software

The term **platform software**, as used in WCAG2ICT, has the meaning below:

platform software
:   software that runs on an underlying software or hardware layer and that provides a set of software services to other software components

Note 1

Platform software may run or host other software, and may isolate them from underlying software or hardware layers.

Note 2

A single software component may have both platform and non-platform aspects.

Example: Examples of platforms are: desktop operating systems; embedded operating systems, including mobile systems; web browsers; plug-ins to web browsers that render a particular media or format; and sets of components that allow other applications to execute, such as applications which support macros or scripting.

This definition is based on the definition of "platform software" found in [[ISO\_9241-171](#bib-iso_9241-171 "Ergonomics of human-system interaction Part 171: Guidance on software accessibility")] and [[ISO/IEC\_13066-1](#bib-iso/iec_13066-1 "Information technology - Interoperability with assistive technology (AT) Part 1: Requirements and recommendations for interoperability")].

### Set of Documents

The term **set of documents**, as used in WCAG2ICT, has the meaning below:

set of documents (non-web) (as used in WCAG2ICT)
:   collection of **[[documents](#document)]** that share a common purpose; are created by the same author, group or organization; **[are published together; and all refer to each other by name or link]**

Note 1

Republishing or bundling previously published documents as a collection does not constitute a set of documents.

Note 2

If a set is broken apart, the individual parts are no longer part of a set, and would be evaluated as any other individual document is evaluated.

Example: One example of a set of documents would be a three-part report where each part is a separate file. The table of contents is repeated at the beginning of each file to enable navigation to the other parts.

### Set of Software Programs

The term **set of software programs**, as used in WCAG2ICT, has the meaning below:

set of software programs (as used in WCAG2ICT)
:   collection of **[[software](#software) programs]** that share a common purpose; are created by the same author, group or organization; **[and are distributed together and can be launched and used independently from each other, but are interlinked each with every other one such that users can navigate from one program to another via a consistent method that appears in each member of the set]**

Note 1

Although "sets of web pages" occur frequently, "sets of software programs" appear to be extremely rare.

Note 2

Redistributing or bundling previously distributed software as a collection does not constitute a set of software programs.

Note 3

Consistent does not mean identical. For example, if a list of choices is provided it might not include the name of the current program.

Note 4

If a member of the set is separated from the set, it is no longer part of a set, and would be evaluated as any other individual software program.

Note 5

Any software program that is not part of a set, per this definition, would automatically [satisfy any success criterion](#dfn-satisfies) that is specified to apply to “sets of” software (as is true for any success criterion that is scoped to only apply to some other type of content).

Note 6

If there is any ambiguity whether the group is a set, then the group is not a set.

Note 7

If there is no independent method to launch the software programs (as is common in ICT with closed functionality), those programs would not meet the definition of a “set of software programs”.

Note 8

Although the term “software” is used throughout this document because this would apply to stand-alone software programs as well as individual software components and the software components in software-hardware combinations, the concept of “set of software programs” would only apply (by definition) to programs that can be launched separately from each other. Therefore, in the WCAG2ICT guidance for the provisions that use the phrase “set of” (success criteria 2.4.1, 2.4.5, 3.2.3, 3.2.4, and 3.2.6), the phrase “set of software programs” is used.

Example: One example of a set of software programs would be a group of programs that can be launched and used separately but are distributed together and all have a menu that allows users to launch, or switch to, each of the other programs in the group.

Counterexamples: Examples of things that are **not** sets of software programs:

- A suite of programs for authoring different types of documents (text, spreadsheets, presentations, etc.) where the programs don't provide an explicit, consistent means to launch, or switch to, each of the other programs in the group.
- An office package consisting of multiple programs that launches as a single program that provides multiple functionalities such as writing, spreadsheet, etc., but the only way to navigate between programs is to open a document in one of the programs.
- A bundle of software programs that is sold together but the only way to navigate between the programs in the bundle is to use a platform software level menu to navigate between them (and not via a menu provided by each program that allows you to navigate to just the other programs in this bundle).
- A group of programs that was a set, but the programs have been moved to separate locations so that their “set” behaviors were disrupted and no longer work. Even though they *were* a set at one time, because they are no longer installed as a set they no longer *are* a set and would not need to meet any success criteria that apply to sets of software.

### Software

The term **software** as used in WCAG2ICT, has the meaning below:

software (as used in WCAG2ICT)
:   software products, or software aspects of hardware-software products, that have a user interface and do not depend upon a separate [user agent](#user-agent) to present any of its [content](#content-on-and-off-the-web)

Note 1

For software, the user interface and any other embedded content is covered by these guidelines. The software provides a function equivalent to a user agent for the embedded content.

Note 2

Software without a user interface does not have content and is not covered by these guidelines. For example, driver software with no user interface would not be covered.

Note 3

Because software with a user interface provides a function equivalent to a user agent in addition to content, the application of some WCAG 2 success criteria would be different for content embedded in software versus content in a document, where it is viewed through a separate user agent (e.g. browser, player, viewer, etc.).

### User Agent

WCAG 2 defines **user agent** as:

> any software that retrieves and presents web content for users
>
> Example: Web browsers, media players, plug-ins, and other programs — including [assistive technologies](https://www.w3.org/TR/wcag22/#dfn-assistive-technologies) — that help in retrieving, rendering, and interacting with web content.

For non-web ICT, “user agent” needs to be viewed differently. In WCAG 2, the term “user agent” only refers to retrieval and display of web content. For non-web ICT, the term “user agent” refers to retrieval and display of separate content that is *not on the web*, which WCAG2ICT refers to as a “document”. Within WCAG2ICT, the term “user agent” is used as follows:

user agent (as used in WCAG2ICT)
:   any [software](#software) that retrieves and presents **[documents]** for users

Note 1

Software that only displays the [content](#content-on-and-off-the-web) contained within it is not considered to be a user agent. It is just considered to be software.

Note 2

An example of software that is not a user agent is a calculator application that doesn't retrieve the calculations from outside the software to present it to a user. In this case, the calculator software is not a user agent, it is simply software with a user interface.

Note 3

Software that only shows a preview of content, such as a thumbnail or other non-fully functioning presentation, is not providing full user agent functionality.

### Virtual Keyboard

The term **virtual keyboard**, as used in WCAG2ICT, has the meaning below:

virtual keyboard (as used in WCAG2ICT)
:   any software that acts as a keyboard and generates output that is treated by other software as keystrokes from a keyboard

Note

Eye-gaze, morse code, speech, and switches (e.g. sip-and-puff) have all been used by virtual keyboards as input that generates "keystroke" output.

## Comments on Closed Functionality

As noted in the Introduction, WCAG 2 assumes the presence of a “user agent” such as a browser, media player, or assistive technology as a means to access web content. Many of the success criteria in WCAG 2 assume web content will be accessed by ICT where assistive technologies can be connected to it or installed on it. The assistive technologies then present the web content to people with disabilities in an accessible form.

ICT with [closed functionality](#closed-functionality) does not allow the use of some assistive technologies for some or all of the ICT's functions. In many cases, such ICT also lacks a “user agent” or its equivalent. To the extent the ICT is closed, following the WCAG success criteria by themselves will not ensure that non-web software is accessible. Where the wide range of assistive technologies or user agents are not available, as they are for web content, to address the intent of these success criteria, something else needs to be provided or be required to facilitate accessibility as intended by WCAG 2. It is outside the [WCAG2ICT Task Force Work Statement](https://www.w3.org/WAI/about/groups/task-forces/wcag2ict/work-statement/) to say what additional measures are needed, but WCAG2ICT points out which success criteria depend on assistive technologies — and therefore which success criteria would be problematic in the context of ICT with closed functionality.

Example: In developing guidance for ICT with closed functionality, the task force has considered specific examples of ICT that historically have been partially or fully closed to assistive technologies:

- self-service transaction machines or kiosks (e.g. retail self-checkout, point of sales (POS) terminals, and Automated Teller Machines (ATMs))
- telephony devices (e.g. internet phones, feature phones, and smartphones)
- entertainment technologies (e.g. smart TV, set-top box, smart watches)
- ebook reader
- computer that is locked down due to a policy so that users may not adjust settings or install software
- other technology devices (e.g. printers, displays, and Internet of Things (IoT) devices).

These examples are explained more fully in the definition of [closed functionality](#closed-functionality) in the Key Terms section.

Note

Some of these technologies, though closed to some external assistive technologies, often have extensive internal accessibility features that serve as assistive technology that can be used by applications on these devices in the same way assistive technology is used on fully open devices, such as desktop computers. Others are open to some types of assistive technology but not others.

There are existing standards that specify accessibility requirements for both hardware and software aspects of ICT with closed functionality. This document does not comment on those standards, but does note that WCAG success criteria should not be applied to hardware aspects of ICT with closed functionality. WCAG2ICT does provide considerations for applying WCAG success criteria to non-web software on ICT with closed functionality. WCAG2ICT also indicates where and why success criteria might be problematic for non-web software due to the underlying assumptions built into the WCAG success criteria. See [Appendix A: Success Criteria Problematic for Closed Functionality](#success-criteria-problematic-for-closed-functionality) for a list of success criteria for which this is relevant.

## Text / Command-Line / Terminal Applications and Interfaces

Text applications are a class of software ICT that appeared decades ago, prior to the emergence of the graphical user interface (GUI) and the Web. The interface of a text application is generated using only text characters, and either a hardware terminal or a software terminal application handles the rendering of the text application—similar to how a web user agent handles the rendering of a web application. Text applications only accept text input, though some may also support the use of a mouse or other input devices. More recently, terminal applications that render text applications in the GUI may utilize spoken input through Automated Speech Recognition (ASR). Both GUI and native text environment interfaces also now commonly support word-completion prediction technologies. Command-line applications are a subset of text applications with further specific properties.

Historically, assistive technologies developed alongside text applications, making it possible for text applications to be accessible. Although there are far fewer new text applications being developed compared to new GUI or web applications, text applications remain in use today. In fact, command-line interfaces have seen a resurgence in recent years, especially in popular programming and revision-tracking environments with continued development and greater functionality. In some cases this has precipitated renewed developments in assistive technology support for text applications.

Assistive technology support continues to evolve in today's text applications. Key examples include:

- In command line interfaces (CLI), support often includes context-sensitive help, so that help output following one command argument is different from the help provided following two arguments, and different still after three arguments. This helps users be more efficient and places no new requirements on assistive technologies.
- Output options generally include machine-readable structured text formats (such as JSON), in addition to the still powerful and widely used options of input/output redirection and piping. In these scenarios the assistive technology user can make use of the same range of output options as anyone else who finds the CLI environment compelling.

As noted in [Appendix B. Background on Text / Command-Line / Terminal Applications and Interfaces](#background-on-text-command-line-terminal-applications-and-interfaces), applying WCAG to text / command-line applications involves understanding how text applications are rendered, how text applications have been made accessible via assistive technologies, and how to apply the concepts of “accessibility supported” and “programmatically determined” to text applications.

## Comments on Conformance

WCAG2ICT is not a standard, so it is not possible to conform to WCAG2ICT. However, some entities may wish to use the information in WCAG2ICT to help establish standards or regulations regarding accessibility in ICT that are based on WCAG 2. While such standards or regulations will need to address matters of conformance themselves, the following notes may be of assistance to those wishing to apply WCAG 2 to non-web documents and software:

1. The WCAG 2 success criteria and the conformance requirements were designed to work together, such that the language of the success criteria is based on the nature of the conformance requirements. The choice of what level to use for a given criteria (A vs. AA vs. AAA) was further influenced by a number of factors specific to the web domain, as set forth in [Understanding Levels of Conformance](https://www.w3.org/WAI/WCAG22/Understanding/conformance#levels).
2. In the WCAG 2 conformance model, a [success criterion is satisfied](#dfn-satisfies) if the item being evaluated does not fail it. If the success criterion is in relation to something that does not exist for the item being evaluated (e.g. a success criterion is about captioning audio and there is no audio), where some might consider the criterion "not applicable", the success criterion is automatically met. This approach is central to the way the success criteria in WCAG are structured and worded.
3. WCAG 2 conformance is applied to the item being evaluated (i.e., a web page) as a whole, except when a process includes use of several items, in which case all of the items that are needed in order to complete the process must conform.
4. In WCAG 2, when conformance depends upon accessibility features of the platform (i.e., a browser for web content) or on assistive technologies, WCAG 2 requires that there are assistive technologies, etc. that work with the product (web page). That is, conformance with WCAG 2 requires that [only accessibility-supported ways of using technologies](https://www.w3.org/TR/WCAG22/#cc4) are relied upon to satisfy the success criteria.
5. WCAG 2 allows information on part of a page to not conform if the same information is available elsewhere on the page in a conforming fashion. However, WCAG 2 identifies four success criteria that must be met on all areas of the page because they can interfere with the user's ability to access and use other parts of the page:
   - [1.4.2 Audio Control](https://www.w3.org/TR/WCAG22/#audio-control);
   - [2.1.2 No Keyboard Trap](https://www.w3.org/TR/WCAG22/#no-keyboard-trap);
   - [2.2.2 Pause, Stop, Hide](https://www.w3.org/TR/WCAG22/#pause-stop-hide);
   - [2.3.1 Three Flashes or Below Threshold](https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold).

Also, as noted in the Introduction, it wasn't possible to unambiguously carve up software into discrete pieces, and so the unit of evaluation for non-web software is the whole software program. As with any software testing, this can be a very large unit of evaluation, and methods similar to standard software testing may be needed.

## Comments by Guideline and Success Criterion

The sections that follow are organized according to the principles, guidelines, and success criteria from WCAG 2. The text of each success criterion from WCAG 2 is copied as quoted text. Following that, the WCAG2ICT guidance is provided. The WCAG2ICT guidance can be found in the sections where the headings begin with "Applying..." to highlight that this is the content specific to this document. Within these sections custom notes added by WCAG2ICT are marked with the text "ADDED".