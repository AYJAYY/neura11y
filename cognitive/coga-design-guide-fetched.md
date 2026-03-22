---
ai_context: Auto-fetched COGA design guide for cognitive accessibility.
domain:
- web
- documents
- general
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/coga-usable/
standard: COGA
status: normative
tags:
- coga
- cognitive
- accessibility
title: Making Content Usable for People with Cognitive Disabilities (Fetched)
---

[![W3C](https://www.w3.org/StyleSheets/TR/2016/logos/W3C)](https://www.w3.org/)

# Making Content Usable for People with Cognitive and Learning Disabilities

## W3C Working Group Note 29 April 2021

This version:
:   <https://www.w3.org/TR/2021/NOTE-coga-usable-20210429/>

Latest published version:
:   <https://www.w3.org/TR/coga-usable/>

Latest editor's draft:
:   <https://w3c.github.io/coga/content-usable/>

Previous version:
:   <https://www.w3.org/TR/2020/WD-coga-usable-20201211/>

Editors:
:   [Lisa Seeman-Horwitz](mailto:lisa.seeman@zoho.com) (Invited expert)
:   [Rachael Bradley Montgomery](mailto:rachael@accessiblecommunity.org) (Invited expert)
:   [Steve Lee](mailto:stevelee@w3.org) (W3C)
:   [Ruoxi Ran](mailto:ran@w3.org) (W3C)

Feedback:
:   <https://github.com/w3c/coga/issues/new>
:   [public-cognitive-a11y-tf@w3.org](mailto:public-cognitive-a11y-tf@w3.org) ([archives](https://lists.w3.org/Archives/Public/public-cognitive-a11y-tf/))

This document is also available as [multiple pages](Overview-mutiple-pages.html), with separate pages for each section.

[Copyright](https://www.w3.org/Consortium/Legal/ipr-notice#Copyright)
©
2021
[W3C](https://www.w3.org/)® ([MIT](https://www.csail.mit.edu/),
[ERCIM](https://www.ercim.eu/), [Keio](https://www.keio.ac.jp/),
[Beihang](https://ev.buaa.edu.cn/)).
W3C [liability](https://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer),
[trademark](https://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks) and [permissive document license](https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document) rules
apply.

---

## Abstract

This document is for people who make web content (web pages) and web applications. It gives advice on how to make content usable for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). This includes, but is not limited to: cognitive disabilities, learning disabilities (LD), [neurodiversity](#dfn-neurodiversity "Neurodiversity is a term that refers to the different ways the brain can work and interpret information. It highlights that people naturally think about things differently. Autistic people, attention deficit (hyperactivity) disorder (AD(H)D), dyslexia, and people with other diagnoses or labels may prefer the term “neurodiverse” as they are part of normal and healthy variation in the human population, bringing diverse skills and perspectives."), intellectual disabilities, and specific learning disabilities.

This document has content about:

- people with cognitive and learning disabilities,
- aims and objectives for usable content,
- design patterns (ways) to make content usable,
- including users in design and testing activities, and
- personas (examples) and user needs.

The objectives and patterns presented here provide [supplemental guidance](https://www.w3.org/WAI/standards-guidelines/wcag/#supplement) beyond the requirements of the Web Content Accessibility Guidelines WCAG [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")]. Following this guidance is not required for conformance to WCAG [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")]. However, following this guidance will increase accessibility for people with cognitive and learning disabilities.

## Status of This Document

*This section describes the status of this
document at the time of its publication. Other documents may supersede
this document. A list of current W3C publications and the latest revision
of this technical report can be found in the
[W3C technical reports index](https://www.w3.org/TR/) at
https://www.w3.org/TR/.*

This document was published by the [Cognitive and Learning Disabilities Accessibility Task Force (Coga TF)](https://www.w3.org/WAI/GL/task-forces/coga/) of the [Accessible Platform Architectures Working Group](https://www.w3.org/WAI/APA/) and the [Accessibility Guidelines Working Group](https://www.w3.org/WAI/GL/) as a Working Group Note.

This document is for people who make web content, including web applications. It focuses on meeting the needs of people with cognitive and learning disabilities. It covers aims and objectives for usable content; design patterns (ways) to make content usable; including users in research, design, and testing activities; personas; and user needs. Details of changes are described in the [changelog](#changelog).

Comments regarding this document are welcome, input received and further evolution of technology may trigger additional updates. To comment, file an issue in the [W3C coga GitHub repository](https://github.com/w3c/coga/issues/new). If this is not feasible, send email to [public-cognitive-a11y-tf@w3.org](mailto:public-cognitive-a11y-tf@w3.org) ([archives](https://lists.w3.org/Archives/Public/public-cognitive-a11y-tf/)).

Publication as a Working Group Note does not imply endorsement
by the W3C Membership.

This is a draft document and may be updated, replaced
or obsoleted by other documents at any time. It is inappropriate to cite this
document as other than work in progress.

This document was produced by groups
operating under the
[1 August 2017 W3C Patent
Policy](https://www.w3.org/Consortium/Patent-Policy-20170801/).
The groups do not expect this document to become a W3C Recommendation.

This document is governed by the
[15 September 2020 W3C Process Document](https://www.w3.org/2020/Process-20200915/).

## 1. Summary (Easy to Understand Language)

This section is an easy to understand summary of the key points of this document. Also see [How to Use this Document](#how-to-use-this-document), for more orientation. To help web content providers meet the needs of people with cognitive and learning disabilities we have identified the following key topics:

### Help users understand what things are and how to use them.

Use icons, symbols, terms, and design patterns that are already familiar to users so that they do not have to learn new ones. People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") often need common behavior and design patterns. For example, use the standard convention for hyperlinks (underlined and blue for unvisited; purple for visited).

See also:

- [user needs](#objective-1-help-users-understand-what-things-are-and-how-to-use-them),
- [design patterns](#objective-1-help-users-understand-what-things-are-and-how-to-use-them-0),
- [mappings to scenarios](#objective-1-help-users-understand-what-things-are-and-how-to-use-them-1),
- and [user testing](#does-the-user-understand-what-things-are-and-how-to-use-them) for objective 1.

### Help users find what they need.

Make navigating the system easy. Use a clear and easy-to-follow layout with visual cues, such as icons. Clear headings, boundaries, and regions also helps people understand the page design.

See also:

- [user needs](#objective-2-help-users-find-what-they-need),
- [design patterns](#objective-2-help-users-find-what-they-need-0),
- [mappings to scenarios](#objective-2-help-users-find-what-they-need-1),
- and [user testing](#can-users-find-what-they-need) for objective 2.

### Use clear content (text, images and media).

This includes easy words, short sentences and blocks of text, clear images, and easy to understand video.

See also:

- [user needs](#objective-3-use-clear-and-understandable-content),
- [design patterns](#objective-3-use-clear-and-understandable-content-0),
- [mappings to scenarios](#objective-3-use-clear-and-understandable-content-1),
- and [user testing](#is-the-content-clear-and-understandable) for objective 3.

### Help users avoid mistakes.

A good design makes errors less likely. Ask the user only for what you need! When errors occur, make it easy for the user to correct them.

See also:

- [user needs](#objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them),
- [design patterns](#objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them-0),
- [mappings to scenarios](#objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them-1),
- and [user testing](#can-users-avoid-mistakes-and-easily-correct-them) for objective 4.

### Help users focus.

Avoid distracting the user from their tasks. If the user does get distracted, headings and breadcrumbs can help orientate the user and help the user restore the context when it is lost. Providing linked breadcrumbs can help the user undo mistakes.

See also:

- [user needs](#objective-5-help-users-focus),
- [design patterns](#objective-5-help-users-focus-0),
- [mappings to scenarios](#objective-5-help-users-focus-1),
- and [user testing](#can-users-maintain-focus) for objective 5.

### Ensure processes do not rely on memory.

Memory barriers stop people with cognitive disabilities from using content. This includes long passwords to log in and voice menus that involve remembering a specific number or term. Make sure there is an easier option for people who need it.

See also:

- [user needs](#objective-6-ensure-processes-do-not-rely-on-memory),
- [design patterns](#objective-6-ensure-processes-do-not-rely-on-memory-0),
- [mappings to scenarios](#objective-6-ensure-processes-do-not-rely-on-memory-1),
- and [user testing](#can-users-find-what-they-need) for objective 6.

### Provide help and support.

This includes:
**making it easy to get human help.** If users have difficulty sending feedback, then you will never know if they are able to use the content or when they are experiencing problems. In addition,
**support different ways to understand content.** Graphics, summaries of long documents, adding icons to headings and links, and alternatives for numbers are all examples of extra help and support.

See also:

- [user needs](#objective-7-provide-help-and-support),
- [design patterns](#objective-7-provide-help-and-support-0),
- [mappings to scenarios](#objective-7-provide-help-and-support-1),
- and [user testing](#is-there-enough-help-and-support) for objective 7.

### Support adaptation and personalization.

People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") often use add-ons or extensions as assistive technology. Sometimes, extra support requires minimal effort from the user via personalization that allows the user to select preferred options from a set of alternatives. Support personalization when you can. Do not disable add-ons and extensions! Sometimes users can receive extra support through personalization.

See also:

- [user needs](#objective-8-support-adaptation-and-personalization),
- [design patterns](#objective-8-support-adaptation-and-personalization-0),
- [mappings to scenarios](#objective-8-support-adaptation-and-personalization),
- and [user testing](#is-adaptation-and-personalization-supported) for objective 8.

### Test with real users!

Involve people with cognitive and learning disabilities in the research, design, and development process. They’re the experts in what works for them. This includes involving people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") in:

- focus groups.
- usability tests, and
- the design and research team.

See also:

- [working with users with cognitive and learning disabilities](#working-with-users-with-cognitive-and-learning-disabilities)
- and [section 5](#Building_in_the_user).

## 2. Introduction

Making web sites and applications usable by people with
cognitive and learning disabilities affects every part of design and development.

Traditionally, accessibility focused on making the interface usable for
people with sensory and physical impairments (vision, hearing, or mobility).
Some accessibility features will help people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").
Often the issues that affect people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:")
include:

- design,
- context,
- structure,
- language,
- usability, and
- other factors that are difficult to include in general guidelines.

Some common designs create barriers for people with cognitive and learning disabilities. The patterns presented in this
document have been designed to avoid such barriers for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").
While this guidance may improve usability for all, these patterns are essential for some people with cognitive
and learning impairments to be able to use content independently.

The objectives and patterns build on the:

- [Cognitive Accessibility User Research](https://www.w3.org/TR/coga-user-research/),
- [Cognitive Accessibility Issue Papers](https://w3c.github.io/coga/issue-papers/), and
- [Cognitive Accessibility Gap Analysis and Roadmap](https://www.w3.org/TR/coga-gap-analysis/).

The objectives and patterns presented here provide [supplemental guidance](https://www.w3.org/WAI/standards-guidelines/wcag/#supplement)
beyond the requirements of [WCAG](https://www.w3.org/TR/WCAG2). Following this guidance is not required for conformance to WCAG. They address accessibility barriers that were not included in the current normative WCAG 2.x and may not otherwise be addressed.

Following the advice in this document, as much as possible, will be particularly valuable for web content and applications that address:

- individual safety concerns,
- health,
- critical services,
- autonomy,
- caregiving,
- social integration, and
- work and the workplace.

Note that people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may also
have other impairments such as motor disabilities or visual
impairments. For
example, some people with [age related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") may also require
higher contrast. It is always important to follow Web Content Accessibility Guidelines WCAG [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")] and ensure the
needs
of all disabilities are addressed.

### 2.1 How to Use this Document

This document provides information on the development process and design options for making web sites and applications more usable and accessible for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

It is organized by high level objectives which are listed along with user stories in [section 3](#user_needs).

The high-level objectives outline key design goals that will help people with cognitive and learning disabilities. Each objective has associated:

- user needs and user stories, that show the user perspective,
- design patterns, that show what to do,
- personas with user scenarios, that help you to understand your users' experiences and challenges, and
- questions for user testing.

Mappings of objectives, user stories, patterns and personas are available in [Appendix A](#appendix-mapping-user-needs-personas-and-patterns). This provides a way to understand how to address the objective and why it is important. Some people may prefer to start with Appendix A.

This document is divided into parts. Each part can be used in different ways in the product development life cycle. This will help teams achieve the objectives in this document without significantly changing the way they work.

- [Section 3. User Stories](#user_needs): This section contains user stories for people with cognitive and learning disabilities. Each story includes related user needs. Teams may use these in different ways. For example, teams can:
  - incorporate them into user stories, or
  - use as part of user research to help you understand your users’ needs.
- [Section 4. Design Guide](#design_for_everyone): This section contains design patterns that support the objectives. Patterns are provided with rationale, how-to guidance, and examples. Teams can use design patterns in different ways, for example:
  - incorporate them into requirement specifications,
  - use in design guidelines,
  - use as solutions when users are dropping out,
  - use as inspiration for site design,
  - test designs against “use” and “avoid” examples,
  - include them in design libraries, and
  - use as content guidelines to promote [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") and communication.
- [Section 5. Usability Testing, Focus Groups, and Feedback](#Building_in_the_user): This section provides a brief introduction to including people with cognitive and learning disabilities in user research. It also includes test questions for each objective. Content from this section can, for example, help teams:
  - involve people with cognitive and learning disabilities in user research and user testing,
  - work with peer researchers,
  - build the user into the development process, or
  - incorporate guidance to support vulnerable users.
- [Section 6. Use Cases/ Personas](#persona): This section provides personas that relate to the user stories, objectives, and design patterns presented in the rest of the document. These personas can be used in user research and developer education.

It should be noted that all teams should try to involve users with cognitive and learning disabilities throughout the design and development process. Teams that are too small for user testing and focus groups can find affordable ways to involve the user by reading [Section 5](#Building_in_the_user).

#### 2.1.1 Testing Each Pattern

In many cases the “use” and “avoid” examples for each pattern can be used as a testable case. The pattern is probably applied if:

- For each pattern, a “use” example is implemented (unless it is not relevant for the content).
- For each pattern, the items identified as “avoid” examples are avoided (unless they are necessary or essential).

There are additional ongoing efforts to make testable statements for each design pattern with corresponding test processes and failure examples, that are always applicable. These are available at [Testable Statements for COGA Design Patterns](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Testable_Statements_for_Each_Pattern).

In some cases, the testable statements only cover part of the design pattern. The Cognitive Accessibility Task Force intends to continue working on these statements as a supplement to the design guide.

One can also test that the additional advice in this document is integrated into development and design processes. For example:

- Confirm that diverse users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") are included in the projects’ focus groups, research and user testing as per the advice in [Section 5](#Building_in_the_user).
- Confirm user needs and user stories for people with cognitive and learning disabilities are integrated into the project user needs, user stories, and requirements, as per [Section 3](#user_needs).
- Confirm that personas from [Section 6](#persona) are integrated into the research phase of the project.
- Confirm that the project user tests include testing for the objectives in this document as per [Section 5](#Building_in_the_user).

### 2.2 Background about People with Cognitive and Learning Disabilities, Accessibility and the Web

Cognitive and learning disabilities include long-term, short-term, and permanent difficulties relating to cognitive functions, such as:

- learning, communication, reading, writing, or math,
- ability to understand or process new or complex information and learn new skills, with a reduced ability to cope independently, and / or
- memory and attention or visual, language, or numerical thinking.

Design, structure, and language choices can make content inaccessible to people with cognitive and learning disabilities. Examples may include:

- People with impaired short-term memory may be unable to recall passwords or copy access codes. They may have trouble or be unable to remember new icons and interface paradigms.
- People with impaired working memory may only be able to hold one to three items in their memory at the same time. This can make it difficult to hold information temporarily or copy access codes.
- People with different processing speed capabilities may need additional time to understand the design relationships and information on the screen.
- People with language related disabilities may need simple clear language and instructions. Some may rely on supporting graphics, icons, and familiar symbols to understand content.
- People with social or communication disabilities may need clear literal language and may not understand metaphors or non-literal text and new icons.
- People with impairments that affect the comprehension of mathematical concepts may not understand or confuse numerical references such as percentages.
- People who have issues with keeping or regaining focus may have difficulty completing a simple task if there are a lot of distractions and interruptions. They may need headers and signposts to help them regain the context after their attention was lost (including in multimedia).
- People with cognitive and learning disabilities that impact learning may need more support or time to complete a new process or an authentication task.
- Many groups may struggle with cognitive fatigue when completing complex, multi-stage processes such as filling out forms or entering data correctly or finding the content or feature that they need. They will need support to minimize errors and complete their task.

These difficulties may sometimes also be experienced by the general population due to environmental or situational barriers. For example, when they are trying to use a web site when distracted or stressed. Working on a mobile device while in an unfamiliar or noisy situation can also place an additional cognitive load on users by splitting their attention. However, for users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"), these difficulties are likely to be persistent and significant. As a result, they may be unable to access content and complete these tasks independently.

[Cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") are difficult to diagnose and categorize. They are usually hidden and can be age related. Users are less likely to have a formal diagnosis of a disability than individuals with physical and sensory difficulties. Often, only some functions are impaired while other cognitive functions are unaffected. For example, someone with dyslexia may be a fantastic engineer. Sometimes, cognitive and learning disabilities may include intellectual impairments that affect comprehension, alongside written and spoken expression. People may also experience more than one type of cognitive and learning disability. Note that the terminology and definitions used for cognitive and learning disabilities varies between countries.

Other groups who will benefit include:

- people with [mental health](#dfn-mental-health "May include: mental heath impairments.") issues that cause cognitive difficulties,
  such as difficulty focusing, cognitive fatigue, or reduced memory,
- people under a temporary stress,
- people who do not know the language or culture of the country well,
- people with limited technical knowledge or are new to the Web.

### 2.3 Building the User into the Development Process

Some aspects of making web content and applications usable by
people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") should be dealt with as part of the
overall design process. Most organizations should include scope
for a user-centered design process. See [our developer resource page](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources) for related resources.

Key parts of this process for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") should be:

- Including the needs of users with cognitive and learning disabilities in the context of user needs and requirements.
- Including people with cognitive and learning disabilities in research methods such as usability testing.
- Including people with cognitive and learning disabilities in the design and development team.

Web sites that include people with cognitive and learning disabilities in usability testing and account for their feedback will be easier to use for everyone, including people who are experiencing stress, or [mental health](#dfn-mental-health "May include: mental heath impairments.") issues. (See [Section 5](#Building_in_the_user).)

### 2.4 Language Use

Language and terminology for cognitive and learning disabilities varies greatly between cultures and communities. Preferred language is also changing over time. We selected terms and defined them in the glossary for consistency within this document. We do not assert these are correct in all cases and for all groups.

When we were aware of conflicting opinions, we reached out to individuals that identify with each term. When preferences varied, we have used our best judgement to select a term based on the feedback. We have provided alternatives within the glossary definition.

When deciding on language and terminology to use when discussing cognitive and learning disabilities, we recommend reaching out to individuals with cognitive and learning disabilities to select the best terms within the specific situation and culture.

## 3. User Stories

This section contains user stories, followed by the user needs that relate to them. They are divided into the same objectives as the design guide above.

Note that for people with cognitive and learning disabilities, meeting these needs can be the difference between being able to use the site or not being able to use it at all. This may also be true for people with [mental health](#dfn-mental-health "May include: mental heath impairments.") issues or under temporary stress.

User needs for people with cognitive and learning disabilities often help other users, although they can usually manage to use the site without these user needs being met.

### 3.1 Objective 1: Help Users Understand What Things are and How to Use Them

#### 3.1.1 Clear Purpose (User Story)

As a user with a memory impairment, attention impairment, or [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") impairment or as a user with a communication disability who uses symbols, I need to know the purpose of the content so that I know if I am in the right place, and what I am doing, even if I lose attention and focus for a time.

This user story also includes the following user needs:

- I need to know what the web site offers, or if I should move on.
- I need to know what features and content are on this page or if I should move on.
- I need to recognize where I am in the architecture of the web site, application, or multi-step process, even after I get distracted.
- I need to know the relationship between this page and the site/task, even after I get distracted.
- I need to know the context and purpose of the page.
- In videos and multimedia: I need to know what is in the video, I can jump to the content I need, and I can restore context if I get distracted.

**Related Personas:**
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Maria](#maria-a-user-who-has-memory-loss),
[Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

#### 3.1.2 Clear Operation (User Story)

As a user with a memory impairment, a learning disability, or a communication disability who uses symbols, or [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") impairment, I find it hard to learn new interface design patterns. I need to know which controls are available and how to use them so that the site is usable for me.

This user story also includes the following user needs:

- I need to understand my options and the tasks I can perform and I can identify the controls I can interact with to complete actions.
- I need to know how to use all the controls and the effects of each action.
- I need the controls to be easy to correctly activate. The interface is designed so that I rarely activate controls by accident.
- I need to know what are controls and what are not controls. I do not try to activate elements that are not controls. Otherwise I think the site is broken.
- I need to know where things are. Controls and content do not move unexpectedly as I am using them.
- I need to know what happens when I touch things. I know the consequence of each action, such as sending information, changing settings, changing the context or closing the application.

**Related Personas:** [Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Amy](#amy-an-autistic-computer-scientist),
[George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination)

#### 3.1.3 Symbols (pictographic or ideographic that represent concepts) (User Story)

As a user with complex communication needs that may include a mild language impairment, I want symbols that help me understand the content.

This user story also includes the following user needs:

- I need symbols to help understand essential content, such as controls and section headings.
- I need symbols that I understand and are familiar to me (recognizable, personalizable or commonly used symbols).
- I need symbols placed above the text to link the meaning of the words with the images.

**Related Persona:** [George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome), [Gopal](#gopal-a-retired-lawyer-with-dementia)

As a user with a severe language impairment, who has managed to learn a symbol vocabulary, I need to have symbols on top of each phrase and very simplified language. Of course, it is best if I understand the symbols and they are the ones I have learnt (via personalization).

**Related Persona:** [George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome)

### 3.2 Objective 2: Help Users Find What They Need

#### 3.2.1 Findable (User Story)

As a user with a memory impairment, impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), or impaired language processing skills who has trouble finding the features they need, I need to identify important information and critical functions on a page, so that I can find things in a reasonable amount of time.

This user story also includes the following user needs:

- I can identify important information and critical functions on a page, quickly and easily.
- I need to reach important information and the controls I need without scrolling or carrying out other actions. They are not hidden or off screen.
- I need to find it easy to identify the content that I need, and do not need. Information I need to know and important information stands out, or is the first thing I read and does not get lost in the noise of less important information.
- I need to get to the feature I need using the minimum number of easy steps.
- I need to know the starting point for each specific task, such as applying for a job.
- I need to find the design and user interface elements familiar. Menus, buttons, design components, and common elements such as help and search are easy to recognize and where I expect them to be.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Amy](#amy-an-autistic-computer-scientist),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Maria](#maria-a-user-who-has-memory-loss),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination),
[Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

#### 3.2.2 Searchable (User Story)

As a user with a cognitive or learning disability and who learnt how to use search to find things, I need to be able use search, so that I can find things on a web site.

This user story also includes the following user needs:

- I need to be able to find features and content easily.
- I need to find what I have searched for before.
- I need to easily navigate through the menu structure and organization of the site.
- I need to easily navigate through the page structure.

**Related Persona:** [Kwame](#kwame-a-traumatic-brain-injury-survivor)

#### 3.2.3 Clear Navigation (User Story)

As a user with a cognitive or learning disability and who likes to browse on the Web, I need the structure and menu categories to make sense to me, so that I find what I am looking for, without looking in the wrong place.

This user story also includes the following user needs:

- I need to easily understand, navigate, and browse both the site and page structure.
- I need to scan the page and understand the priority and structure of the content.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Amy](#amy-an-autistic-computer-scientist),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Maria](#maria-a-user-who-has-memory-loss),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia)

#### 3.2.4 Media (User Story)

As a user with impaired [executive functioning](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") and attention impairments, I want media presented in small chunks of understandable content, so that I can understand the main points and not lose focus.

This user story also includes the following user needs:

- I need to easily navigate to what I want, take breaks and easily jump back a step if I do not follow or get distracted.
- I need small segments of multimedia that have navigable text or labels that describe the segment.
- I need [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") to be used
- I need to use a clear structure to help me navigate and understand different parts of the media.
- I need to use visual aids and pictures to help me understand the media content.
- I need to be able to find the transcript, if a transcript is available.

**Related Persona:** [Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

### 3.3 Objective 3: Use Clear and Understandable Content

#### 3.3.1 Clear Language (Written or Audio) (User Story)

As a user with a language, processing, or memory impairment, I need the language used to be clear and easy for me to understand so that I can understand the content.

This user story also includes the following user needs:

- I need to understand the language used, including vocabulary, syntax, tense, and other aspects of language.
- I need to easily distinguish the content from the background distractions.
- I need words to include accents, characters, and diacritics that are necessary to phonetically read the words. This is often needed for speech synthesis and phonetic readers in languages like Arabic and Hebrew.
- I need to understand the meaning of the text. I do not want unexplained, implied or ambiguous information because I may misunderstand jokes and metaphors.
- I need an easy to understand, short summary for long pieces of content or an option for an [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") version.
- I need images, diagrams, or video clips to help me understand ideas (more than a lot of words).
- I need explanations of implied or ambiguous information, like body gestures and facial expressions seen in images and animations.

**Related Personas:**
[George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia),
[Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

#### 3.3.2 Visual Presentation (User Story)

As a user with a language or communication impairment, dyslexia, or an impaired memory, I want a page layout that helps me follow and understand the content without getting overwhelmed.

This user story also includes the following user needs:

- I need small or short chunks of content, sections, or boxes.
- I need a good use of white space, so that the chunks are clear and the page does not get overwhelming.

**Related Personas:**
[Amy](#amy-an-autistic-computer-scientist),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination),
[Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

#### 3.3.3 Math Concepts (User Story)

As a user who does not understand numerical concepts, I need content to be usable without understanding math concepts.

This user story also includes the following user needs:

- I need content without math concepts.
- I need content that provides alternatives like a non-math textual explanation.
- I need words rather than numbers and numerical concepts.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Jonathan](#jonathan-a-therapist-with-dyscalculia)

### 3.4 Objective 4: Help Users Avoid Mistakes and Know How to Correct Them

#### 3.4.1 Assistance and Support (User Story)

As a user who has difficulty with organization ([executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.")), typing, and putting letters and numbers in the right order, I want an interface that stops me from making mistakes, and helps me complete forms and perform other similar tasks successfully.

This user story also includes the following user needs:

- I need an interface that helps me avoid mistakes.
- I need to enter as little information as possible, so the task is more manageable.
- I need the interface to only give valid options, so I can select the ones I want.
- I need an interface that helps ensure I rarely touch controls by accident.
- I need long numbers that often have spaces, like credit card numbers, divided into chunks. That way I find it easier to check them.
- I need inputs to accept different formats and not mark them as mistakes.
- I need interfaces to use metrics I know, and that are common in my location (such as feet or meters), otherwise I get confused. I do not always know what metric they are talking about or notice when the number looks wrong.
- I need to use applications (or standard application programming interfaces - APIs) that help me. For example, by remembering my information so I do not need to enter it again and helping with spelling.
- I need clear labels, step-by-step instructions, and clear error messages, so I know exactly what to do.
- I need examples that make it easy to understand what I need to do.
- I need clear and simple explanations of options or choices to help me know what they mean.
- I need help managing my time, such as letting me know how long a task will take.
- I need time to complete my work. I do not want a session to timeout while I try to find the information needed, such as my postal/zip code or social security number.
- I need to save my work as I go or be sure all my work is saved automatically. I do not want to start over again, which can create a cycle of reentering my data. This makes me tire easily and more likely to make mistakes.
- I need support to manage the task, such as letting me know what information I will need (credit card, full address, etc.) before I start.
- I need to understand the consequences of what I do online.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Jonathan](#jonathan-a-therapist-with-dyscalculia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor)
[Maria](#maria-a-user-who-has-memory-loss),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination),
[Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

#### 3.4.2 Undo (User Story)

As a user who often makes mistakes or touches the wrong thing, I want to undo what I just did quickly and easily so that I can manage to use applications.

This user story also includes the following user needs:

- I need to check my work and go back without losing the work I have just done.
- I need to go back to where I was in one simple step, when I touch the wrong control.
- I need predictable back or undo features so that I know exactly where I was previously, before I made a mistake.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Maria](#maria-a-user-who-has-memory-loss),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination)

### 3.5 Objective 5: Help Users Focus

#### 3.5.1 Distractions (User Story)

As a user with an attention impairment and impaired memory, I need to avoid distraction. If I lose focus and forget what I am doing, I need reminders of what I was doing, so that I can complete my task.

This user story also includes the following user needs:

- I need tasks to not have distractions.
- I need to turn distractions off easily, if there are distractions.
- I need to know where a task starts and finishes to help with switching attention so that I can focus on the task.
- I need to know the context, where I am, what I just did, or what just happened to me after I lost cognitive focus and then needed to come back to the task.
- I need to be able to go back or see information about where I am in a site so that I can reorient myself.
- I need to know where I am in a process to avoid disorientation, including what I have done and what my next step will be.

**Related Personas:**
[Amy](#amy-an-autistic-computer-scientist),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia),
[Yuki](#yuki-a-yoga-teacher-who-has-ad-h-d)

### 3.6 Objective 6: Ensure Processes Do Not Rely on Memory

#### 3.6.1 Remembering from Previous Steps (User Story)

As a user with short-term and working memory difficulties, I need processes that do not rely on memory and access to information I entered during previous steps in a process.

**Related Personas:** [Maria](#maria-a-user-who-has-memory-loss)

#### 3.6.2 Accessible Authentication (User Story)

As a user who has [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:") and often forgets passwords, and has impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), I need a method of secure web site authentication that I can use.

This user story also includes the following user needs:

- I need to be able to use a site without remembering or transcribing passwords, codes, and usernames.
- I need to understand the content. I cannot decipher a lot of words or unfamiliar icons.
- I need a login process to be simple, and not multi-step.
- I need a login process that I can use that does not rely on a lot of words.
- I need a login process that does not have puzzles or calculations.

**Related Personas:**
[Jonathan](#jonathan-a-therapist-with-dyscalculia),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination)

#### 3.6.3 Voice Menus (User Story)

As a user who has [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:") and impaired language processing skills, I need to get human help, without going through a complex menu system (VoiceXML [[voicexml21](#bib-voicexml21 "Voice Extensible Markup Language (VoiceXML) 2.1")]) or a complex voice recognition menu system that relies on memory and [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), so that I can set an appointment or find out some information.

This user story also includes the following user needs:

- I need to easily find a human by pressing a reserved digit that I know (typically the number 0).
- I need simple-to-navigate voice-menu systems with limited options that make sense to me, so I don’t struggle with multiple steps and can identify options quickly.
- I need to hear the option before the number to select, so I do not have to remember the number while processing the words.
- I need pauses between each option so I can process what was said. (As a user with impaired cognitive processing speed.)
- I need the system to wait for my response. (I am a slow speaker.)
- I need to easily go back every time I make a mistake, without having to start at the beginning.
- I need the usability best practices for voice menus. (As a user who often finds menus unusable.)
- I need to easily find a process to select simple help, and not multi-step help.
- I need to spend my energy completing my task. I do not want to waste my energy while I struggle to understand other material, such as special offers or promotions.
- I need help identifying the right words to say in a voice menu and the words should be the ones I would use.

**Related Personas:**
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Maria](#maria-a-user-who-has-memory-loss)

### 3.7 Objective 7: Provide Help and Support

#### 3.7.1 Help (User Story)

As a user who finds some web sites hard to use, I need to get help and give feedback easily from every place where I get stuck. This ensures I am not excluded and the site is aware of my needs.

This user story also includes the following user needs:

- I need to give feedback from any point in the process.
- I need to give feedback, ask questions, and get feedback:
  - in a similar timeframe to everyone else,
  - using my preferred communication method (form, email, chat, phone support, etc.) and it is accessible to me, and
  - I know how to get help or information, such as from context-sensitive help or tooltips.
- I need to know how to get human help and can manage the process easily.

**Related Persona:** [Alison](#alison-an-aging-user-with-mild-cognitive-impairment)

#### 3.7.2 Support (User Story)

As a user who finds some web sites hard to use and struggles with text and words, I sometimes need in-page and inline support so that I can use the content. However, with an attention impairment any support required needs to be in my control to avoid distractions.

This user story also includes the following user needs:

- I need any help and support content to include symbols or enable me to personalize content using my own.
- I need help and main content to be clearly differentiated so I do not confuse them.
- I need contextually-relevant graphs and pictures to supplement text.
- I need text-to-speech support, with synchronized highlighting, so I can follow along as words are read aloud.
- I need rapid feedback or visual cues to show when an event is successfully triggered. For example, I need to know when an email is sent, otherwise it looks as if it has just disappeared.
- I need reminders integrated into my calendar, otherwise I will forget appointments and when I am meant to do things. Sometimes I need reminders to revisit a web site to complete the next task.
- I need to control when reminders are sent, the frequency and type of reminders so that I do not become distracted by too many reminders.

#### 3.7.3 Directions (User Story)

As a user with cognitive and learning disabilities that affect navigation and sequencing, I need help understanding and using directions and navigation.

**Related Personas:**
[George](#george-a-user-who-works-in-a-supermarket-and-has-down-syndrome),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor)

#### 3.7.4 Cognitive Stress (User Story)

As a user with sensitivities that can be affected by content (e.g. content that is busy, confusing, depressing, or has loud noises), I need content that I can cope with so that I can be successful.

This user story also includes the following user needs:

- I need simple, consistent content.
- I need to avoid and recover from mental fatigue.
- I need to sometimes avoid types of content, such as social media, distractions, noises, or triggers.
- I need to make less mistakes and errors.
- I need to know I am safe and secure when using a web site, especially if providing information or communicating with others.

**Related Persona:**
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination)

#### 3.7.5 Task Management (User Story)

As a user who struggles using web content due to [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") impairment, or struggles with numerical concepts, I want to be confident that I can manage my tasks.

This user story also includes the following user needs:

- I need explanations for unusual controls in a form I find easy to use (such as a video or text).
- I need support and explanations for any choices. The advantages or disadvantages are clear to me and I understand the effects of the choice I might make. For example, when choosing a cheaper airline ticket, you often have to pay for a meal.
- I need to know how to start a task, and what is involved such as:
  - the steps involved,
  - a time estimate for completing the task and any time limits,
  - any materials I may need (such as a credit card number, passport number, questions that authenticate login such as "your mother's maiden name"),
  - support and instructions that I understand to help me organize the time and steps,
  - any limitations are clear to me before I begin.
- I need to turn off any distractions during a task, and help is available at any point.

**Related Personas:**
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Jonathan](#jonathan-a-therapist-with-dyscalculia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia)

### 3.8 Objective 8: Support Adaptation and Personalization

#### 3.8.1 Adapt (User Story)

As a user with short and medium-term memory impairment and impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), I need a familiar interface so that I do not need to figure out and remember new interfaces. This may take a few weeks of repetition and I may not manage to learn it all if I have a condition affecting learning new things, such as dementia.

This user story also includes the following user needs:

- I need (a version of) a familiar interface, that I recognize and know what will happen.
- I need the controls to be consistently positioned on the screen where I expect them to be.
- I need content delivered in [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") or an easy to understand mode (like short, understandable, video clips).
- I need to easily find and select the content format or version of the content that is easiest for me to understand.
- I need alternatives to spoken and written language, such as icons, symbols, or pictures.
- I need personalized symbols, icons, or pictures that I can recognize immediately, as learning new ones takes a long time.
- When I do not know a word, I need symbols and pictures that I know and recognize.
- I need videos and pictures that help me understand the content without so much reading of text.
- I need “easy to use” gestures on a touch screen that do not confuse me (or the possibility of alternative access).
- I need to express my ideas without so many words, such as using speech recognition or pictures (I have a program, where I select a word and it gives me a picture).
- I need to be able to add more white space between lines, sentences, phrases, and chunks.
- I need alternatives for mathematical content, that do not rely on mathematical concepts.
- I need less content without extra options and features as I cannot function at all when there is too much cognitive overload.
- I need to find the extra features when I want them.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Amy](#amy-an-autistic-computer-scientist),
[Gopal](#gopal-a-retired-lawyer-with-dementia),
[Jonathan](#jonathan-a-therapist-with-dyscalculia),
[Sam](#sam-a-librarian-who-has-a-hemiplegia-and-aphasia)

#### 3.8.2 Extensions and APIs (User Story)

As a user with cognitive and learning disabilities, who uses add-ons and extensions as assistive technology, I need my add-ons, application programming interface (API), and extensions to work with the content so that I can use it.

This user story also includes the following user needs:

- I need to use additional support features from widgets or extensions. For example, I have an extension that helps me correctly enter words, grammar, and use punctuation as well as reading the page to me.
- I need to use my password manager.
- I need to use my toolbar that adds symbols and reformats the page.

**Related Personas:**
[Alison](#alison-an-aging-user-with-mild-cognitive-impairment),
[Jonathan](#jonathan-a-therapist-with-dyscalculia),
[Kwame](#kwame-a-traumatic-brain-injury-survivor),
[Tal](#tal-a-student-who-has-dyslexia-and-impaired-eye-hand-coordination)

## 4. Design Guide

### 4.1 Introduction

This guide provides assistance making web sites and applications friendly for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). The patterns in this guide provide practical guidance to improve the accessibility of designs and the design process.

The objectives and patterns presented here provide [supplemental guidance](https://www.w3.org/WAI/standards-guidelines/wcag/#supplement) beyond the requirements of The Web Content Accessibility Guidelines WCAG [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")]. They are intended to address barriers that could not be included in the normative WCAG [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")] specification and may not otherwise be addressed.

This guide is divided into design objectives. An outline of these objectives can also be found in the [summary section](#summary). Simply understanding the objectives and related user stories may help designers make content more accessible to some users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

Each objective contains a number of practical patterns (repeated designs for controls and other elements) that describe what to do to address user needs. Implementing these patterns is **essential** for some people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") to be able to use content independently.

### 4.2 Objective 1: Help Users Understand What Things are and How to Use Them

Users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may have trouble with orientation and learning. This can mean people get disoriented in a site.

Learning new things and remembering new information is especially difficult for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). They can also struggle or be unable to learn new design patterns. Make controls, icons and elements simple and conventional to help.

Make it clear to users what things are and how to use them. This includes clearly indicating the purpose of:

- a site,
- section of a site,
- page,
- section of a page, and
- controls.

Use headers, labels, and other signposts to help users know the purpose of the page, region, or control.

Help users understand how to use controls and elements on each page.

Use familiar design patterns, terms, and icons to help users who struggle to remember new designs. Ensure the look, location, and interaction of controls and other elements are familiar and consistent across the site.

Show a clear relationship between controls and the content they effect to help users understand the effect of possible actions and reduce potential confusion.

#### 4.2.1 Make the Purpose of Your Page Clear (Pattern)

##### 4.2.1.1 User Need

> I need to know the context and purpose of the page.

Related User Story: [Clear Purpose](#clear-purpose-user-story).

##### 4.2.1.2 What to Do

Help the user know the purpose of the content. Use:

- a clear title or heading that summarizes the purpose of a page, or
- other clear signposts that have been tested by users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

##### 4.2.1.3 How it Helps

This helps many people, including those with impaired memory and attention as well as anyone who is easily distracted due to [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") and [AD(H)D](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.").

For example, someone with mild dementia is using online shopping. They get distracted and then when they look at the screen again they have forgotten what they were doing. A clear heading at the top of each page shows clearly **what the page is about and what they are doing**.

In another example, a user with [AD(H)D](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.") is looking for information in a video. They can tell by the video title that this video has the information they need.

##### 4.2.1.4 More Details

Headings clarify the purpose of this specific page.

When possible, provide information to help users understand how they got to the page. For example: clearly indicating breadcrumbs on main navigation, highlighting currently selected tab, etc.

##### 4.2.1.5 Examples

**Use:**

1. Page headings that tell the user where they are.

**Avoid:**

1. Pages without clear headings or signposts that tell the user where they are. For example:
   - Page headings that do not tell the user where they are, such as a page heading that reads “Service not available”. The user has to remember what the service relates to.
   - Page headings that do not clarify the steps in a form.

#### 4.2.2 Use a Familiar Hierarchy and Design (Pattern)

##### 4.2.2.1 User Need

> I need to understand my options and the tasks I can perform and I can identify the controls I can interact with to complete actions. (I find it hard to learn new interface design patterns.)

Related User Story: [Clear Operation](#clear-operation-user-story).

##### 4.2.2.2 What to Do

Use common designs that are familiar to most users. This includes:

- design elements,
- affordances (visual hints about how to a control),
- patterns, and
- the layout and visual hierarchy (arrangement of elements to show the order of importance).

##### 4.2.2.3 How it Helps

Many users cannot easily learn and remember new design metaphors. Without these skills, it can be much harder or impossible to locate desired items with which to interact, and to know what interactions may do. Users can feel lost or overwhelmed.

Users are more likely to find and recognize common design elements that are repeated often over a long period of use, across many sites.

For example, a user with a [mild cognitive impairment](#dfn-mild-cognitive-impairment-mci "Mild cognitive impairment (MCI) can involve problems with memory, language, thinking, and judgment that are greater than normal age-related challenges. It is sometimes considered the stage between the common and expected age related forgetfulness and the more serious decline of dementia, although many or most people with MCI will not develop dementia.") or dementia, goes to a site to buy a product. They cannot find where to pay for the item that they want. They may think the site does not allow shopping and the site just provides information.

##### 4.2.2.4 More Details

Common design elements, affordances, and patterns include:

- A standard layout and visual hierarchy (arrangement of elements to show the order of importance). Place elements where the user is expecting them. For example, in an English site:
  - search in the top right hand corner in a web site,
  - link to the home page in the top left hand corner,
  - link to “contact us” in the top navigation area,
  - link to the site map in the footer area, and
  - submit button at the bottom of a form.
- Common design patterns (repeated designs for controls and other elements), such as:
  - WAI-ARIA authoring best practices [[wai-aria-practices-1.2](#bib-wai-aria-practices-1.2 "WAI-ARIA Authoring Practices 1.2")],
  - patterns used in the most popular sites,
  - very common navigation design patterns and common icons,
  - platform specific (operating system) user interface design for navigation mechanisms and icons, and
  - adaptive user interface design that can be personalized (see above).
- User interface (design) from a prior version. Allow users to revert back to a prior version of the application with which they are familiar.
- Links that look like links and buttons that look and act like buttons. For example:
  - underline links with a standard style throughout a page,
  - links generally navigate to a new page, and
  - buttons generally perform an action.

##### 4.2.2.5 Getting Started

1. When designing web pages, select standard components that look and behave the way users expect. Use standard conventions for layout such as:
   - home link in the upper left corner,
   - navigation at the top, and
   - search in the upper right.
2. Create an obvious visual hierarchy in the page.

##### 4.2.2.6 Examples

**Use:**

1. Common web layouts.

**Avoid:**

1. Unfamiliar layouts.
2. Unfamiliar visual hierarchies.

#### 4.2.3 Use a Consistent Visual Design (Pattern)

##### 4.2.3.1 User Need

> I need to understand my options and the tasks I can perform and I can identify the controls I can interact with in order to complete actions.

Related User Story: [Clear Operation](#clear-operation-user-story).

##### 4.2.3.2 What to Do

Use a consistent visual design across groups of pages.

##### 4.2.3.3 How it Helps

Many users take a long time to learn new designs and recognize elements. Once learned, the elements should be used throughout the site.

For example, an older user with [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") takes a long time to learn new designs. When they come to a site, the first page takes time to understand, but then they know what to do on the next page. If the next page is different from the first and also difficult to learn, they become tired and make more mistakes. As they move to a third difficult page the cognitive load becomes too much and they cannot complete the task.

##### 4.2.3.4 More Details

This includes:

- Consistent design themes, including heading styles, font choices, icons, colors, visual appearance of controls, buttons and links.
- Headings with the same structural level have the same font and visual style.
- Icons, controls, and menu items that have same function and role have the same look and style.
- State and focus for elements with similar function and roles have the same style across a site.
- Layout is consistent across blocks of content. This includes the position of interactive elements and navigational controls.
- Structure of content and style of presenting information is consistent. This includes the organization of blocks of text, icons, images, and bullet points.

##### 4.2.3.5 Getting Started

Plan the design for your information before adding content. Think about the colors, font choices, and areas where text and images will appear.

##### 4.2.3.6 Examples

**Use:**

1. Headings at the same level look similar, across the site.
2. A consistent look across the site for controls. For example:
   - Two submit buttons in a web site, both look and function the same way.
   - All selected radio buttons on the site look the same.
   - When an item is tabbed to, it has focus and can be activated. The keyboard focus indicator (outline that shows which element has focus) for all links look the same.
3. A consistent location for common features. For example:
   - The search box is always in the same place in the entire site.

**Avoid:**

1. Elements with similar functions looking different. For example:
   - There are six heading level 2s on a page. Four are styled using Times New Roman and two using Helvetica.
2. Elements with similar functions presented in different locations. For example:
   - Three pages have a submit button. One is located at the top of the form. One is located at the bottom. One is located in a sidebar.

#### 4.2.4 Make Each Step Clear (Pattern)

##### 4.2.4.1 User Need

> I need to recognize where I am in the architecture of the web site, application, or multi-step process, even after I get distracted.

Related User Story: [Clear Purpose](#clear-purpose-user-story).

##### 4.2.4.2 What to Do

Provide breadcrumbs, a “how I got here” button, or heading to help the user orientate themselves inside a site or task.

In a multi-step process, this includes showing:

- the steps completed,
- the current step,
- the steps pending, and
- any important choices.

##### 4.2.4.3 How it Helps

This pattern helps a user who loses focus, forget what they are doing or gets distracted reorient themselves to their current activity. Clearly indicating the current location and progress helps the user continue after they lose focus without reading a great deal of content or restarting.

Providing information about the steps that need to complete a task helps users determine if they can successfully finish the task. This is especially important for users who often find processes difficult to complete.

Examples include:

- Someone with [early stage dementia](#dfn-early-stage-dementia) is interrupted in their task or loses focus and then cannot remember what they were doing. By seeing the bread crumbs they can remind themselves where they are and continue their task.
- Someone with an attention disability gets distracted and then needs to pick up where they left off.
- Someone with a processing difficulty is not sure if this application has too many steps and if they will manage. By seeing they are half-way through they can gauge if they can cope with the entire process.

##### 4.2.4.4 Examples

**Use:**

1. Breadcrumbs that indicate the current step in the process, important choices, as well as past and future steps.
2. Headings that clarify exactly were the user is inside the content.
3. A “how I got here” button. When the user clicks the button they receive orientation information about:
   - the page,
   - how they got here, and
   - where they are inside the content.

**Avoid:**

1. Completed steps and choices that are hard to find and check. For example:
   - Placing completed steps on previous pages.
   - Placing selected choices in a control that hides and reveals content (such as an accordion).

#### 4.2.5 Clearly Identify Controls and Their Use (Pattern)

##### 4.2.5.1 User Need

> I need to understand my options and the tasks I can perform and I can identify the controls I can interact with in order to complete actions.

Related User Story: [Clear Operation](#clear-operation-user-story).

##### 4.2.5.2 What to Do

Use a clear and recognizable design for controls. Make it clear what elements are controls and how to use them.

This includes:

- Using a common style on controls (for example, links being underlined).
- Using common design patterns on links and controls (for example, clicking on a link takes you to the page).
- Making the borders of controls clear. Links in text do not need borders if identified properly (for example, a help icon has a border).
- Making controls large enough so that users can click on it and not the item next to it.
- Ensuring items that are not clickable do not look like links or controls.

When this is not possible, provide instructions that explain how to use the control. Instructions should be on the same page or one click away and written in [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.").

##### 4.2.5.3 How it Helps

Controls are parts of web pages that do something, e.g. a link, button, checkbox. Common style and design patterns on controls are easier to recognize and understand how to use it.

The goal of these controls is to allow someone to use them. As soon as the user needs to discover the control or work out how to use it, some users will fail.

For example, an older user with [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") takes longer to learn new designs. They go to an ecommerce site that has boxes around the headers such as “sale”. It also has simple large text for controls such as the “add to cart” button. The user clicks on the headings and not on the “add to cart” button (that looks like text). After a few failures they assume they cannot manage it and leave the site.

Some users have trouble when controls have a different look, color, or shape than they have used before. For example, when links do not have underlines and blue or purple text some users will not know there is a link (even if this appears with focus).

If you have difficulty with memory, it can be harder to use unique controls. It may take longer to find controls on the page. Even if they work just a little differently than similar ones, some users may need to relearn how to use them each time.

Using typical controls on the page will help people know how to use them. When using more unique controls, include easy to follow instructions and make them easy to find. It should be easy to identify, understand, and use the controls, regardless of how a user uses the page (vision, auditory, voice input).

##### 4.2.5.4 Getting Started

Use standard controls and design patterns.

If you are designing a new control, make them easy to:

- identify (I know they are there),
- understand (I know what they do), and
- use (I know how to use them).

Use a simple style or have easy to follow instructions that explain their use. Test with people with different [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

##### 4.2.5.5 Examples

**Use:**

1. Standard blue and purple link colors or links with an underline and distinct text color (the link text color used is not used for static text on the site).
2. Buttons with a standard button design (3D rectangles) that support the standard user actions and make it clear when they are pressed.
3. Tabs that look like tabs and make it clear when they are selected.

**Avoid:**

1. Links without an underline.
2. Links that have the same color as static text on the site, even if the links have a clear focused state.

#### 4.2.6 Make the Relationship Clear Between Controls and the Content They Affect (Pattern)

##### 4.2.6.1 User Need

> I need to know how to use all the controls and the effects of each action.

Related User Story: [Clear Operation](#clear-operation-user-story).

##### 4.2.6.2 What to Do

The relationship between controls and affected content should be completely clear and unambiguous.

This can be achieved through:

- visually grouping controls with the content they relate to,
- including controls within the region they affect,
- using clear dividers or white space between regions in a page that may have separate controls or a scroll bar,
- avoiding multiple or nested scrolling areas.

##### 4.2.6.3 How it Helps

If a control on a page operates only on part of the page, it can be hard to tell what it will affect and what it will not. Users may try the wrong control. Many users will try again, and discover the correct control or scrollbar. However, many people with cognitive or learning disabilities may not be able to work out what to do. Others will feel cognitive overload, and stop as a result. They may assume the application is broken, or that it is too complicated for them. For these users, the application will not be usable.

Clear borders and groupings on the page can help indicate what element the control effects. Having a border or other visual cue around the controls and the relevant section can help make it more understandable. Check with user testing that users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") find all the page relationships clear and quickly know how to use the controls. Testing is essential when the controls cannot be in the area they affect.

For example, consider a user living with dementia trying to work out which scrollbar to use for embedded scrollable regions. When they try the wrong scrollbar, they do not get the effect they desire and their content may seem to disappear.

##### 4.2.6.4 More Details

- **Separate Interactive Elements**. For example: Do not have two scroll bars close together. Some users may find it difficult to determine which one to use with a particular section of content. Instead:
  - use clear visual layout and placement of the scroll bars,
  - break the content into two separate pages, or
  - consider removing unnecessary information from the page.
- **Associate elements and their controls**. Place interactive elements like scroll bars and buttons close to the content they can impact. Keep interactive elements further from content to which they do not apply. This makes it easier to identify which elements will impact each section of content.
- **Use dividers**. Examples of clear dividers include high contrast borders or white space. A change in background color can be a clear divider if the contrast is strong enough.
- **Help the user see the right control**. Use large clear buttons and scroll bars.

##### 4.2.6.5 Examples

**Use:**

1. Controls clearly associated with the section they control. Place the control inside the section, and have clear borders around the section. Label the controls to match the section heading. For example:
   - On a library site, a search box for the whole site is located in the upper right of the site’s main navigation. A second search box searches the library catalog. It is located within a section with a clear border, different background color, and a heading “Library Catalog”. The go button reads “search catalog”.
   - A page needs a scrollbar for one section. The scrollbar look like it is inside the section.

**Avoid:**

1. Multiple scrollable sections where it is unclear which scrollbar to use for each section.
2. Controls for one section that look like they might affect the whole page or another section. For example: The search box relates to one area of a page, and not for another area. It is unclear which area the search is for.
3. Multiple nested scrolling regions.

#### 4.2.7 Use Icons that Help the User (Pattern)

##### 4.2.7.1 User Need

> I need to know what features and content are on this page or if I should move on.

Related User Story: [Use Symbols](#symbols-pictographic-or-ideographic-that-represent-concepts-user-story).

##### 4.2.7.2 What to Do

Add familiar icons, images, and symbols to important content such as controls and section headings. Each icon or symbol should convey a single meaning and be next to the content it relates to.

##### 4.2.7.3 How it Helps

People who have language comprehension, learning, or reading difficulties may rely on symbols to understand content and navigate to content they need. Symbols also help people who struggle with language and attention to navigate content, including media.

For example, a person with aphasia, has the intellectual ability to understand concepts, but struggles with language. They may be dependent on the use of symbols to browse pages for information.

It can also help the elderly population who can find cluttered pages with dense text hard to read on a screen. Clear symbols, icons, and images that act as signposts to the text content can be very helpful.

##### 4.2.7.4 More Details

- Use clear and unambiguous icons or symbols that are easy to see and enlarge.
- Be aware of cultural differences.
- In left-to-right languages, when adding a few icons or symbols to a page place the image to the left of the text.
- When adding multiple symbols to a paragraph or section of text, place the symbols above the text.
- Use personalization semantics such as [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")] to help the user load familiar symbols.

##### 4.2.7.5 Getting Started

Use common icons that the user is likely to understand.

Provide common icons next to key texts, headings, media sections, “contact us” buttons, and "help" buttons.

##### 4.2.7.6 Examples

**Use:**

1. Instructions and important lists where each bullet point starts with an icon that relates to the content within that point. For example, see the summary of this document.
2. Icons next to help, contact information, and search.
3. Icons in call out boxes.

**Avoid:**

1. Important instructions without icons or images to guide the reader.
2. Cluttered, dense pages full of icons that can confuse or overwhelm the user.

### 4.3 Objective 2: Help Users Find What They Need

Users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may have trouble finding the content they need. They may also struggle to orient themselves inside the content or task. Users should be able to quickly and easily locate what they are looking for. Use a clear and easy layout to help users navigate the system easily. For example:

- Make anything related to safety or that the user needs to know easy to identify without reading a lot of text!
- Provide a clear site structure and hierarchy will help users navigate to the page they need.
- Make the most important things easy to find in the site and on each page.
- Use good visual cues (like icons) with clear headings, boundaries, and regions to help users understand the page design. This makes the page navigation easier.
- Provide a search facility or breadcrumbs to help users find things on the site.
- Break media into chunks to allow users to easily find sections.

#### 4.3.1 Make it Easy to Find the Most Important Tasks and Features of the Site (Pattern)

##### 4.3.1.1 User Need

> I need to find it easy to identify the content that I need, and do not need. Information I need to know and important information stands out, or is the first thing I read and does not get lost in the noise of less important information.

Related User Story: [Findable](#findable-user-story).

##### 4.3.1.2 What to Do

Make important tasks and features on the site stand out and easy to find.

This includes:

- On the home page, calling out key tasks for the web site.
- Using call out boxes or sections of the home page for these tasks and features.
- Giving the most important tasks/features visual weight.
- Placing the tasks/features towards the top of the page so the user does not have to scroll to see them.
- Placing the tasks/features toward the top of the content so assistive technology finds them quickly.
- Providing useful headings for each key task or feature.
- Including key tasks at a top level of the main navigation.

##### 4.3.1.3 How it Helps

People with impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), impaired memory, and other [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may have difficulty determining what they can do on a site. By calling out important tasks and features, people can more quickly determine whether the site will meet their needs.

For example, a user goes to a web site to buy tickets. He sees many reviews and other information but cannot see how to buy the tickets. The user leaves the site.

##### 4.3.1.4 More Details

Make important features and tasks both visually and programmatically prominent. See The Web Content Accessibility Guidelines WCAG [[WCAG22](#bib-wcag22 "Web Content Accessibility Guidelines (WCAG) 2.2")].

##### 4.3.1.5 Getting started

Start by thinking about what are the key tasks for the user.

Include:

- The most common tasks users want to perform.
- Tasks that may affect users’ health or well-being.

Usage data can normally identify the most common tasks. Focus groups and surveys are also useful for identifying what users want.

##### 4.3.1.6 Examples

**Use:**

1. The most important tasks are directly on the main page and in visually distinct boxes. For example, important tasks on a library site might be: searching, signing up for a library card, locating a branch, and reserving a conference room.
2. The most used features are near the top of the page.

**Avoid:**

1. Items that the team wish to promote more prominently placed than the main reason for users coming to the site. For example: A library web site only includes upcoming events on the main page. Users have to click through non obvious links to search for books, signing up for a library card, locating a branch, or reserving a conference room.
2. Positioning information users are likely to want so they have to scroll, or page down, to find it.

#### 4.3.2 Make the Site Hierarchy Easy to Understand and Navigate (Pattern)

##### 4.3.2.1 User Need

> I need to easily understand, navigate, and browse both the site and page structure.

Related User Story: [Clear Navigation](#clear-navigation-user-story).

##### 4.3.2.2 What to do

Make it easy to understand and use the site hierarchy and the menu structure.

This includes:

- Think about the topics covered in your content. Then organize the site into logical, cohesive sections.
- Use the site organization in the main menu structure.
- Create sub-menu items that are clearly and logically associated with the main menu items under which they fall. It should be easy to know that sub-menu items are there and how to get to them. Users should guess correctly, the first time, where to find sub menu items.

Make it easy to identify:

- the site organization,
- the menu and content structure,
- that there are sub-menus and,
- if there are sub-menu items, how to reach them.

##### 4.3.2.3 How it Helps

Users often become confused and lost when they do not understand the visual hierarchy of the site, menus, and structure. Clear sub-menus and a well-defined structure will help the user know what is on the site and how to find it.

Users often are confused when:

- organization is unclear,
- menu terms are hard to understand, and
- menus and sub-menus are hard to find.

Dividing the site into clear logical sections can help. Make sections clear and subsections easy to find. Make the category structure and headings easy to understand. Create an outline that could serve as a summary of what is on the site.

The terms used in the menu need to make sense to the user. It needs to be obvious to the user what category the page they are looking for would fall under. Using common words that are familiar to the user is very important.

Make the levels in the content hierarchy easy to perceive and understand. Minimal type size or type weight differences or color differences may not be perceived or understood. Hierarchy solely dependent on small unique design elements creates confusion.

For example, a drop down accordion menu of additional sub-menu items may not be viewable without understanding it needs to be clicked (or “rolled over”) as indicated by a small unique design element.

When opening a web page for the first time, the sub-menus are typically collapsed. Some designs may make it difficult to know that there are sub-menus. Some users with cognitive disabilities may not guess that sub-menus are present. Even if they see a menu expand by accident, they may not generalize that this structure may be present for other items in a menu. Making it easy to notice that there are sub-menu items by adding a visual indicator to ensure users can use all of the site.

There are times when opening the sub-menu item may not be easy for some people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). For example, the control to expand a menu item relies on a particular gesture or way of rolling over the area with a mouse. The end user may not figure out how to expand the sub-menu and may abandon the task. For example, a menu that expands only after moving the mouse over a particular side of the menu text.

##### 4.3.2.4 More Details

- Small design elements that indicate sub-menu items are not always meaningful to the user. Test designs with a diverse user set whenever possible to make sure they are clear.
- Consistently use best practices to make it understandable to the user.
- Series of nested elements that depend on interpreting small design elements are also confusing, and users may not understand the hierarchy.
- Clearly indicate when text is hidden or when it can be hidden or revealed.

##### 4.3.2.5 Getting Started

1. Think about the types of content and categories of content in your site.
2. Divide the content into clear categories.
3. Build the main navigation from the important categories.
4. If you have sub-menus, add a clear symbol that show when sub-menus are closed and when they are open.

##### 4.3.2.6 Examples

**Use:**

1. A visually clear and logical site hierarchy.
2. Clear indicators when text is hidden. For example:
   - Consistently using “+” sign to show that additional information will be shown when pressed.
   - Consistently using triangles next to hidden sub-menu items in menus.

**Avoid:**

1. A site hierarchy where users do not correctly guess what item is under each menu item.
2. Unclear logic for the menu categories.
3. No visual indication of sub-menu items next to the menu item. For example:
   - The only way to discover the presence of the sub-menu item with a mouse is to move the mouse over the sub-menu item.
   - Opening a sub-menu requires putting the mouse on part of the menu item, and this area is not clear and visually distinguished.

#### 4.3.3 Use a Clear and Understandable Page Structure (Pattern)

##### 4.3.3.1 User Need

> I need to easily understand, navigate, and browse both the site and page structure.

Related User Story: [Clear Navigation](#clear-navigation-user-story).

##### 4.3.3.2 What to Do

Carefully design the layout of the page. Make sure it has a clear structure and hierarchy so that it is easy to understand.

This can be achieved by:

- organizing the page content into logical sections,
- clearly differentiating regions using dividing lines, whitespace, and background colors,
- providing headings and other visual cues to indicate the structure and purpose of the regions,
- making any relationship between regions of the page clear, and
- using visual indicators to help people understand:
  - structure and relative importance of the page content,
  - the grouping and association of items, and
  - when items have a different purpose to surrounding information.

##### 4.3.3.3 How it Helps

People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may not be able to use content and applications when the page structure and relationships are unclear. The user may not complete tasks and miss key information. The user may not return to pages that are complicated to use and understand.

Clear, well organized page layouts enable users to easily find key information. They can focus on their tasks instead of working out what is on the page. Using a standard visual layout, and positioning elements consistently, will help users rely on muscle memory and use them. This supports people with disabilities that impact their problem solving skills, slow readers, or people who get overwhelmed when presented with a lot of text. This includes:

**A good structure:** Organization of page content into sections, each with an obvious purpose, allows users to more easily locate and focus on the sections they need. Content that is not directly relevant to the main purpose of a page should be distinctly separated.

**Use borders and shading to group:** Grouping information using a border or color shading makes it easier for people to identify groups.

For example:

![3 rows of 8 evenly spaced circles divided into two blue rectangles.  The blue backgrounds make the two groupings visually apparent.](img/common-region-1.png)
![4 circles divided into two sets of two by a contrasting border. Each set has a blue and a white circle. The white circles are adjacent but border clearly indicates the sets.](img/common-region-2.png)

Figure: Example of grouping with shading and borders.

**Visual cues:** People who have difficulty recognizing or comprehending written language or concentrating, can find graphical cues easier to process. Examples of common graphical indicators and visual cues include:

- grouping summaries of content,
- using a card design using colors or white space,
- flagging important information, such as using call out boxes, and
- indicating different types of information, such as placing quotes in speech bubbles.

##### 4.3.3.4 More Details

If pages have a lot of content, check that content is grouped and you can see what is related.

Making regions and a clear page structure can include:

- Clearly label content categories, and use familiar visual cues and icons. This will help recognition and retrieval rather than rely on memory. The background color can be a clear divider if the contrast is strong enough.
- The heading structure should create an outline of the document that could serve as an abstract of the whole document.

Icons should be used consistently. It is also important the graphical indicators do not clutter the interface. Too many icons can add to the cognitive load for users to process. Examples of clear dividers include high contrast borders or white space. A change in background color can be a clear divider if the contrast is strong enough.

##### 4.3.3.5 Examples

**Use:**

1. Well separated sections of content. White space, borders, or call outs are used to separate sections.
2. Headings and icons to help define sections of content. This organizes the information on the page so it is easier to understand the layout and find specific information.
3. Call outs boxes.

**Avoid:**

1. Dense text, with little white space.
2. Unclear page structure and hierarchy.
3. Lack of visually differentiated sections.
4. Sections without headings or icons that define sections. For example: A web page has chunks of content run into each other with a “flat design”. Many users with cognitive disabilities will find it challenging or impossible to work out which chunks belong together. Thus, all the benefits of chunking content are lost.
5. Groups and page sections that are not logical.

#### 4.3.4 Make it easy to find the most important actions and information on the page (Pattern)

##### 4.3.4.1 User Need

> I need to reach important information and the controls I need without scrolling or carrying out other actions. They are not hidden or off screen.

Related User Story: [Findable](#findable-user-story).

##### 4.3.4.2 What to Do

Make key content visually stand out. Key content should be visible to users without needing to scroll the page or hover over content. This includes:

- critical tasks and the controls needed to complete them,
- interactions for critical features (e.g. login forms, send buttons), and
- important information (e.g. health warnings or information that can affect safety).

##### 4.3.4.3 How it Helps

Slow readers, people with impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), impaired memory, and other [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may not be able to find the information and features on a page. For example, content that requires a lot of reading or the use of the scroll bar or pointer hovers may be hard to find. Other users cannot find content that requires paging through different screens

Users who are unfamiliar with the page (or common design patterns) may rely on prominent visual styling aids to find important information. A clear heading structure can also help with this by reducing what needs to be read.

For example, an elementary school publishes a weekly newsletter with stories, activities, and important announcements. One important announcement is that school will end early one day. The newsletter has less important information before the early school dismissal, and does not have a warning symbol next to the important information. A parent who reads slowly may need to stop before the important information and does not find out that the school is ending early one day. The parent is not home for the child on time.

In another example, a user is writing a comment, but the send button is not visible when the focus is on the text area. As a result, she cannot see how to send her feedback. The company will then not receive any feedback from groups who unable to find the feedback button.

##### 4.3.4.4 More Details

The amount of page visible before scrolling is dependent on a wide range of factors such as physical device size and resolution. Where possible, use site statistics to understand what technology users are using. Keep this in mind when designing the page.

Consider the most constrained user experience first (e.g., a 240px wide mobile phone) and then design upwards from there. This will account for the widest range of scenarios. Adopting responsive development practices can improve the flexibility of the page for more devices and situations.

##### 4.3.4.5 Getting Started

Make it easy to find the most important things on the page. Identify
key content and its placement early in the design process.

Space at the top of the document is most likely to be visible to
users without scrolling. Place key content at the top of the page to give the best experience to the widest range of users.

##### 4.3.4.6 Examples

**Use:**

1. Important controls and features that are visible without the need to scroll the page.
2. Important controls, such as a submit button, that stand out from less important links and buttons.
3. Critical information (such as information about health and safety) that is highlighted and visible without scrolling.
4. Critical information that visually stands out from other less important information on the page.

**Avoid:**

1. Important information, controls, or features that the user cannot find straight away. For example: Warnings about user safety that are not visually distinct and above the fold.

#### 4.3.5 Break Media into Chunks (Pattern)

##### 4.3.5.1 User Need

> I need to easily navigate to what I want, take breaks and easily jump back a step if I do not follow or get distracted.

Related User Story: [Media](#media-user-story).

##### 4.3.5.2 What to Do

Provide a logical organization and structure that is easy to navigate.

Divide long pieces of media into segments that are:

- logical,
- short,
- labeled,
- easy to identify, and
- easy to reach or jump to.

##### 4.3.5.3 How it Helps

Using a clear, logical structure, with headings allows users to orient and navigate through the content easily even if they get distracted or lose focus. This is particularly important for people with an attention impairment.

Providing short logical segments help users find and focus on a specific topic. If the user loses concentration they can find their place in the material and start again from the last point that they remember. This is especially important for educational content or instructions.

Chunking media also allows for each segment to be given a unique URI. It can then be easily referenced and shared.

For example:

- Some videos can be naturally organized into chapters or segments.
- A podcast can be split into segments rather than a single one-hour recording.

##### 4.3.5.4 More Details

- **Six minutes or less:** Media should typically be divided into segments that are 6 minutes or less in duration.
- **Navigable:** Provide navigation to each media segment, and a unique, descriptive label.
- **Logical order:** Present the links to media segments in a logical order.
- **Exception:** Media that has no logical breaking points, do not need to be subdivided.

Note that if a transcript is available, it should be easy to find and navigate.

##### 4.3.5.5 Examples

**Use:**

1. Media that is divided into short logical segments. Each section is labeled and easy to get to. For example: A 30-minute video is divided into 5 sections, each with a descriptive link to play from that point onwards.

**Avoid:**

1. Media that is not divided into segments. For example: A 30-minute video contains no subdivisions or descriptions of sections. A user has to play it from the beginning or guess starting locations within the video.
2. Media sections that are not labeled.
3. Media sections that are not linked to in the summary or table of contents.

#### 4.3.6 Provide Search (Pattern)

##### 4.3.6.1 User Need

> I need to be able to find features and content easily.

Related User Story: [Searchable](#searchable-user-story).

##### 4.3.6.2 What to Do

Provide a friendly search capability. Ideally search should include:

- autocomplete,
- grouping of results when appropriate with headings for each group,
- ability to easily find previous searches, and
- spell-checking.

##### 4.3.6.3 How it Helps

Having a search capability allows users to find the content they need even if they cannot use the site menus. A user can learn how to use search and reuse that skill on many sites.

Menu systems and most site navigation require the user to understand the menu categories. Users with impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") may be unable to identify the correct categories.

In some cases, users know the correct category via memory, rather than logic. For example, most users remember that the print function is often found under the file menu. Users with impaired memory may not be able to find these menu items based on recall.

Users with impaired short-term memory, [age related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)"), or who are easily distracted may also find navigating a site and going to many pages to look for content difficult. If it takes too long they may lose focus and forget what they are looking for.

Search is most useful when it corrects misspellings, finds appropriate or related content, and provides suggested auto-corrected versions of the search terms.

If there are many results from related topics, it helps if search results are presented under the appropriate heading and categories. This helps the user find the search results they are looking for.

##### 4.3.6.4 More Details

Search is less important on small sites where every page is no more than
two clicks away from the main page.

##### 4.3.6.5 Examples

**Use:**

1. Search with spell check or suggested terms.

**Avoid:**

1. Search that presents many results that are not grouped or ordered by their relationship to the original request.

### 4.4 Objective 3: Use Clear and Understandable Content

Some users have impaired language skills. More of these users understand content which uses [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well."). For example, someone with a language impairment may be able to understand simple sentences and common words. However, complex language with uncommon words may be inaccessible to them.

Help users understand the message and purpose of the page by using:

- easy to understand words,
- short sentences,
- simple tense,
- short blocks of text,
- unambiguous content,
- clear images, and
- easy to understand videos.

A good visual layout and small chunks of text makes content easier to understand. Use whitespace and good separation of foreground from background to help comprehension. Also, avoid relying on numerical or mathematical skills.

#### 4.4.1 Use Clear Words (Pattern)

##### 4.4.1.1 User Need

> I need to understand the language used, including vocabulary, syntax, tense, and other aspects of language.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.1.2 What to Do

- Use common and clear words in all content. Look at the most common 1500 words or phrases. These are the terms that people with severe language impairments are most likely to know.
- Remove unnecessary or vague words (such as: “and so forth”).
- Remove or explain uncommon acronyms, abbreviations, and jargon.
- Do not invent new words or give words new meanings in your application. Do not expect people to learn new meanings for words just to use your content. If you must create new terms, make sure the user has access to an explanation within one click or event.

##### 4.4.1.3 How it Helps

This benefits many people such as those with language impairments, processing difficulties, or a memory impairment. Using uncommon words can make text and media difficult to understand.

People with language impairments often have a reduced vocabulary. Learning new terms is a very slow, difficult process. For other groups, such as people living with dementia, learning new terms is not realistic or possible. Using uncommon words, that they do not already know, will make the content incomprehensible (unable to be understood) and unusable.

For example, someone with mild dementia is trying to turn on an ICT heating and air conditioning unit. The menu item for selecting heat or air conditioning is labeled “mode”. The user cannot use the whole unit because of this one term. This type of design has caused emergencies such as hypothermia.

Using common words and terms, with their most common meanings will help avoid these problems.

See [our developer resource page](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources) for pages of common words and related resources.

##### 4.4.1.4 More Details

When using uncommon words, provide an explanation by:

- adding a simple language term in brackets next to it,
- providing a pop up definition, or
- using supported markup (see [easylang](https://w3c.github.io/personalization-semantics/help/index.html#easylang-explanation)). Note that [easylang](https://w3c.github.io/personalization-semantics/help/index.html#easylang-explanation) is being introduced into the new personalization specifications [[personalization-semantics-help-1.0](#bib-personalization-semantics-help-1.0 "Personalization Help and Support 1.0")]. At the time of publication more support is needed.

##### 4.4.1.5 Getting Started

Start using clear words in headings, labels, navigational
elements, instructions, and error messages. This will increase the
usability without a large time commitment.

##### 4.4.1.6 Examples

**Use:**

1. Common, clear, and easy to understand words and definitions of terms. For example:

   Your landlord must follow the law.

   - Your landlord can only use your security deposit (promise money), for certain things, such as unpaid rent (rent that you owe) and to fix things that you damage.
   - Your landlord must return your security deposit (promise money) to you by a clear date. This is usually 30 days after you leave the apartment.

2. Abbreviations that are explained the first time they are used, unless the abbreviation is more common than the full term. Abbreviations are in an abbreviation tag with a title after the first use.
3. Acronyms that are not in common use, are explained the first time they are used, and are in an acronym tag with a title after that.
4. Jargon that is avoided or explained.

**Avoid:**

1. Uncommon words without explanations. For example:

   A Landlord’s Right to Deduct. When a tenant moves into a rental property, he or she will pay the landlord a security deposit. Depending on the jurisdiction, this deposit will be returned to the tenant within a specific time period at the cessation of the lease term, as long as the tenant follows all the terms and tenants of the lease agreement or contract. Select links below to read the laws that pertain to your situation.

2. Abbreviations, acronyms, and jargon that the user may not know and are not explained.

#### 4.4.2 Use a Simple Tense and Voice (Pattern)

##### 4.4.2.1 User Need

> I need to understand the language used, including vocabulary, syntax, tense, and other aspects of language.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.2.2 What to Do

Use the tense and the voice that is easiest to understand. In English, this is usually the present tense and active voice. Speak directly to the user, and use the simplest form of verbs and sentence structure.

Use local [plain language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") guidance to find the tense and the voice that is easiest to understand in different languages.

##### 4.4.2.3 How it Helps

Using simple tense and voice benefits many people such as people with language impairments, dyslexia, or a memory impairment. For example, more people will understand “press the on button” (present tense and active voice) than “the on button should be pressed.” (passive voice).

Active voice makes it clear who is supposed to take action. For example, “It must be done.” is passive voice ad does not say who must act. “You must do it.” is active voice and clearly states who has the action.

Putting the aim of the sentence at the beginning can also make English sentences easier to follow. Local language experts may have additional linguistic advice that helps make content easy to understand.

##### 4.4.2.4 More Details

- Use other voices or tenses when they will be easier to understand or friendlier.
- In languages where present tense and active voice do not exist or are not the clearest option, use the tense and the voice that are easiest to understand.
- If you are writing about past or future events, do not use the present tense. It will be confusing.

##### 4.4.2.5 Examples

**Use:**

1. Simple tense and language. For example: “Your stocks went up this month.”

**Avoid:**

1. Complex language and tense. For example: “Over the last month, we saw your stocks increasing.”

#### 4.4.3 Avoid Double Negatives or Nested Clauses (Pattern)

##### 4.4.3.1 User Need

> I need to understand the language used, including vocabulary, syntax, tense, and other aspects of language.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.3.2 What to Do

Use a simple sentence structure.

This includes:

- do not use a double negative to express a positive, and
- do not use clauses inside clauses.

##### 4.4.3.3 How it Helps

Simple sentence structure benefits many people, including those with language impairments, dyslexia, or a memory impairment. Both double negatives and nested clauses can be confusing.

For example, more people will understand “You must get the agency’s approval before we can answer your claim”, rather than “No approval of any claims can be achieved without the agency’s approval.”

Simple language allows more people to understand. For example, a person with [early stage dementia](#dfn-early-stage-dementia) can manage their own affairs when the language is clear and understandable.

##### 4.4.3.4 Examples

**Use:**

1. Short text without double negatives. For example: “Write clearly”.

**Avoid:**

1. Double negatives that can be replaced by a positive. For example:
   - Do not write unclearly.
   - Time is not unlimited.

2. Long sentences with lots of commas and conjunctions. For example:
   - Usually, clauses will be separated by two commas, one before and one after or the word “or”, or the word “and”, so you could replace the sentence with a list of options or even more than one paragraph.

#### 4.4.4 Use Literal Language (Pattern)

##### 4.4.4.1 User Need

> I need to understand the meaning of the text. I do not want unexplained, implied or ambiguous information because I may misunderstand jokes and metaphors.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.4.2 What to Do

Use literal and concrete language. When possible, use concrete terms
and examples that refer to objects or events that you can see, hear or
touch.

Do not use metaphors and similes unless you include an explanation.

##### 4.4.4.3 How it Helps

Many people do not understand non-literal content. For example, an [autistic](#dfn-autistic "Sometimes called “autism spectrum disorder”, “ASD”, “autism”, “asperger syndrome”, and “pervasive developmental disorder”.") person may not understand jokes and similes. Sometimes instructions have jokes and similes to make the content friendlier. However, this confuses the user who now cannot do her job as needed.

You can explain any non-literal language by:

- adding a simple language term in brackets next to any non-literal text such as metaphors and similes,
- providing a pop up definition, or
- using supported markup (such as personalization semantics [[personalization-semantics-help-1.0](#bib-personalization-semantics-help-1.0 "Personalization Help and Support 1.0")]).

In non-text media, explain non-literal content as part of the media or include it in a separate file or track. See best practices.

##### 4.4.4.4 More Details

Make sure the meaning remains clear when you replace non-literal text with
literal text. Check this when providing literal text
in a popup or other alternative.

##### 4.4.4.5 Getting Started

Start by putting clear literal text on headings, labels, navigational elements, instructions, error messages, and any content that may affect the user’s rights or wellbeing. This will increase the usability in critical places without changing your writing style.

##### 4.4.4.6 Example

**Use:**

1. Literal text and concrete language. For example:
   - If you are experiencing anxiety disorders before starting take a deep breath, tell yourself you can do it and get started. Anxiety can include nervousness, fear, dizziness, or shortness of breath.

**Avoid:**

1. Non-literal text. For example:
   - If you are experiencing cold feet before starting, take a deep breath and jump in.

#### 4.4.5 Keep Text Succinct (Pattern)

##### 4.4.5.1 User Need

> I need to understand the language used, including vocabulary, syntax, tense, and other aspects of language.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.5.2 What to Do

Use short blocks of text

This includes:

- Keep paragraphs short. Have only one topic in each paragraph.
- Try to have the aim of the paragraph or chunk at the beginning.
- Use short sentences. Have only one point per sentence.
- Use bulleted or numbered lists.
- Use short descriptive headings.

##### 4.4.5.3 How it Helps

Chunking text content makes it easier to read and understand. This helps people with learning or cognitive disabilities related to processing speed or language. People with a memory impairment or anyone who is easily distracted will also benefit. Chunking is also helpful to anyone who is multitasking. Try to put the aim or purpose at the beginning of each chunk or paragraph.

For example, a graduate student with [AD(H)D](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.") may need to teach themselves a new software skill. The software documentation is broken up into short paragraphs and lists by topic. The student finds the documentation easy to read and understand.

##### 4.4.5.4 More Details

- **What is a short paragraph?** In English, if you have a paragraph of more than 50 words, try breaking it up into two paragraphs.
- **How can I avoid writing a sentence with more than one point?** Sentences that have more than one point usually have more than one linking word such as “and” or “but”.
- **Can a long sentence ever be clearer than two short sentences?** Double-check if a long sentence is clearer than two short sentences. Do usability testing to see if people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") find the long sentence easier to understand.
- **When should I use lists?** Lists are great when you have three or more things in a row. Think about using an unordered list (with bullet points) for items, requirements, and exceptions. A series of three or more steps is easier to follow as a numbered list.

##### 4.4.5.5 Examples

**Use:**

1. Short chunks of text. For example:
   - Calgary will have a lot of snow and hail this weekend. Try not to drive. If you must drive:
     - Use the rules for driving in winter to keep safe.
     - Before you leave, check what roads are safe at the Traveler’s Information web site.

**Avoid:**

1. Long chunks of text. For example:
   - DOTD Issues Winter Weather Travel Advisory for Calgary. With the possibility of snow and rain in the forecast throughout the holiday weekend, the Department of Transportation and Development (DOTD) announced that department staff is prepared to deal with winter weather. Maintenance forces will be on standby to apply sand and salt over any affected bridges and roadways, to remove fallen trees from the roadway, and to close any roads as needed. Interim Secretary Jane Doe urges motorists to take the threat of winter weather seriously. “In the event of adverse weather conditions, the department will strive to maintain access to highways and interstates; however, we encourage the motoring public to avoid traveling during snow and ice, if at all possible,” said Doe.

#### 4.4.6 Use Clear, Unambiguous Formatting and Punctuation (Pattern)

##### 4.4.6.1 User Need

> I need words to include accents, characters, and diacritics that are necessary to phonetically read the words.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.6.2 What to Do

Use punctuation and format for text, numbers, and symbols that reduce ambiguity and improve
readability and comprehension.

##### 4.4.6.3 How it Helps

For some readers, decoding words, numbers, and symbols does not happen automatically and can be demanding on working memory and [executive functions](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."). If they find content too demanding they are at risk of losing its meaning.

Some users may use assistive technology or personalization tools to help understand content such as text-to-speech that reads aloud the content. However, sometimes the punctuation or format makes it more likely that the screen reader will read it incorrectly. For example, Roman numerals may be read as text.

A user with a learning disability may be unable to manipulate letters, numbers, and words to correct mistakes that occur because of formatting or punctuation errors. They also need to focus on understanding the meaning of the content in order to use it.

For example, a user with a communication disability may listen to content using text-to-speech. If the content is phrased correctly, they can understand it. Sometimes they hear content read incorrectly or skipped, particularly numbers and symbols, and they cannot understand it. If text, numbers or symbols are in an unfamiliar layout, the user may become confused.

In contrast, a blind person listening to the content, is likely to be able to figure out the correct meaning even when words are not pronounced correctly. However, the word manipulations necessary to work out the correct meaning are not achievable by someone with a communications or language impairment.

##### 4.4.6.4 More Details

**Use language tags.** Language tags are the key means to achieve the goal of unambiguous text formatting. See HTML [[HTML](#bib-html "HTML Standard")] language tags and [BCP 47 Language Codes](https://tools.ietf.org/html/bcp47).

**Use punctuation correctly** for the language you are
writing in, as it will affect how the stress and intonation (known
as prosody) patterns from the text are heard, when converted into
speech. For example, in English, commas and semicolons will result
in a short pause in the speech, whereas a hyphen - will generally be
ignored. Question marks, exclamation marks, and speech marks can
result in changes in intonation, such as a rise in the pitch of the
voice.

**Avoid the use of Roman Numerals and unfamiliar symbols**
in text were possible. These can confuse readers and are likely to
be read incorrectly by text-to-speech tools. If these symbols are
necessary then ensure they are marked up correctly, using techniques
such as MathML and abbreviation expansions to provide additional
support. Roman Numerals should be presented in upper case if used in
isolation as they are likely to be read as individual letters.

Long numbers may be read as single digits or phrased as a single number. This is a particular problem for phone numbers or zip codes. While it is difficult to control exactly how these numbers are read aloud, content creators can help by:

- Displaying the content of the number and using HTML semantics to ensure users and assistive technologies are aware of the number’s purpose. In addition, the following recommendations can assist with improving text-to-speech rendering:
- For phone numbers, use the correct layout for the locality of the phone number and ensure users can select the whole phone number (including area code), so that text-to-speech voices can recognize the format and phrase it correctly.
- For Zip / Postal codes, include state or address information close to the number so that speech voices can expand known abbreviations (such as state names) and listeners can perceive the context.
- When writing long numbers, consider what separators will be familiar to your readers and how it will be read aloud. In general, English speaking countries will use commas between thousands and a period as the decimal separator whereas German and other European countries do the opposite. For example, 1,245 would represent one thousand two hundred and forty-five in English, but one point two four five in German. Text-to-speech output will assume the separators are being used in the format of the language of its voice. If this does not match the content, then listeners can become easily confused. While replacing thousand separators with a space has become a common convention to avoid confusion, it leads to difficulties with text-to-speech with long numbers being read out in a disjointed fashion. For example, 120 034 943 can be read as one hundred and twenty, zero three four, nine hundred and forty-three.

##### 4.4.6.5 Examples

**Use:**

1. Dates that can be read and understood in any culture.

   Consider how you write dates, because once again the text-to-speech will use the format associated with the language of the voice. A date such as 04/03/2019 will be read as “April 3rd 2019” by a US English voice and “4th of March 2019” by a British English voice. Writing out the month in words can avoid confusion.

**Avoid:**

1. Dates and numbers that are not clear or read differently based on culture.

#### 4.4.7 Include Symbols and Letters Necessary to Decipher the Words (Pattern)

##### 4.4.7.1 User Need

> I need words to include accents, characters, and diacritics that are necessary to phonetically read the words. This is often needed for speech synthesis and phonetic readers in languages like Arabic and Hebrew.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.7.2 What to Do

Include vowels, letters, or diacritic marks that users need to decipher words correctly.
This is often needed in languages like Arabic and Hebrew.

##### 4.4.7.3 How it Helps

Some languages, such as Hebrew and Arabic, have optional vowels and diacritic marks. Without these marks, most words with the same characters have between two (Hebrew) and seven (Arabic) different ways of being pronounced with different meanings. Most readers can read the word based on the context, and use their visual memory to guess the correct pronunciation. People with impaired visual memory, slow readers, and text-to-speech may often guess the incorrect term or pronunciation.

For example, a user with a language disability is trying to sound out a word. They guess three different pronunciations until they find one that makes sense. Unfortunately, many people with language impairments cannot work out the meaning as words out of context may only provide an idea rather than a specific meaning. Text-to-speech often requires these characters to speak the correct word.

Note that not all diacritic marks are necessary to pronounce the word correctly. Only letters and diacritic marks that are necessary for the unambiguous pronunciation need to be included.

##### 4.4.7.4 More Details

Words can be deciphered and pronounced to have the correct meaning.

##### 4.4.7.5 Getting Started

In Hebrew add additional Yud (י) and Vav (ו) that enables correct pronunciation.

##### 4.4.7.6 Examples

**Use:**

1. Additional letters or diatric marks that enable correct pronunciation. For example:
   - He says: אֹמַר /אומר (Hebrew)
   - He wrote:  كَتَب (Arabic)
   - Books: كُتُبْ (Arabic)
   - It was written: كُتِبَ (Arabic)

**Avoid:**

1. Words without needed letters or diatric marks so the user must guess the pronunciation based on memory and context. For example:
   - אמר (Hebrew)
   - كتب (Arabic)

#### 4.4.8 Provide Summary of Long Documents and Media (Pattern)

##### 4.4.8.1 User Need

> I need an easy to understand, short summary for long pieces of content or an option for an [Easy to Understand](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") version.

Related User Story: [Clear Language](#clear-language-written-or-audio-user-story).

##### 4.4.8.2 What to Do

Provide a brief summary for a long document and media.

Emphasize any important keywords to help people understand the purpose and content of the document, and determine if it might contain information they need.

Summaries should use common words, short sentences, and be written in an easy to understand style and tense.

##### 4.4.8.3 How it Helps

Providing an easy to understand summary helps many people to quickly decide if the content is relevant to them and their current goal. A high level outline in a few sentences or bullet points is most effective. Abstracts and executive summaries are usually much longer and more detailed as they are designed to summarize the entire document.

For media, summaries help users with short attention
span find the exact file they need and jump to correct content. All media files should have a summary description.

##### 4.4.8.4 More Details

Provide a text summary that can be understood by people with lower secondary education level reading ability.

In pieces of content with less than 300 words, headings can act as a summary.

Summaries of each segment should include the main points from the content. Users should be able to use the summary to uniquely identify the content and know what it will contain.

##### 4.4.8.5 Examples

**Use:**

1. Short summaries with bullet points that clearly state the main points.

**Avoid:**

1. Long texts, documents, or media without summaries.
2. Unclear summaries. For example:
   - In multimedia, the segments are summarized as Chapter 1, part 1. Chapter 1, part 2, etc.

#### 4.4.9 Separate Each Instruction (Pattern)

##### 4.4.9.1 User Need

> I need short boxes or chunks of content or sections

Related User Story: [Support](#support-user-story).

##### 4.4.9.2 What to Do

In instructions, separate each step. State each step clearly. This includes:

- including all steps, even those you think are “obvious”,
- using numbers and lists can also help,
- providing complex instructions in an if/then table, which can be easier to follow, or
- using friendly graphics can help make instructions less scary.

##### 4.4.9.3 How it Helps

Step-by-step instructions benefit many people such as people with language impairments, processing difficulties, or a memory impairment.

For example, a person with an impaired working memory cannot hold onto many pieces of information at the same time. They are more likely to make mistakes if they need to remember what they are doing, divide the steps, and track what they have done. When instructions are clearly separated and laid out, they can follow them without making mistakes.

##### 4.4.9.4 Examples

**Use:**

1. Bullet points to separate each step.
2. An if/then table to separate steps based on conditions. For example:

   | **If** | **Then** |
   | --- | --- |
   | If you want to work in programing: | - Make a resume. - Get some sample code that you wrote. - Send them to programing@example.com. |
   | If you want to work in design: | - Make a resume. - Get some sample pages that you designed. - Send them to design@example.com. |

**Avoid:**

1. More than one step in the same block of text without separation. For example:
   - If you want to work in programing, write to programing@example.com with a resume and sample code that you wrote. If you want to work in design, write to design@example.com with a resume and sample pages.

#### 4.4.10 Use White Spacing (Pattern)

##### 4.4.10.1 User Need

> I need a good use of white space, so that the chunks are clear and the page does not get overwhelming.

Related User Story: [Visual Presentation](#visual-presentation-user-story).

##### 4.4.10.2 What to Do

Put white space around objects and text, including boxes, paragraph
headings, and content, so that each section is clearly separated.

##### 4.4.10.3 How it Helps

White space (also called negative space or the background color)
reduces clutter and provides definition to content. This gives the
viewer a clear overview of a web page. It is used by designers to
enhance text and the position of objects on a page.

Using white space aids navigation through a page and helps people read it. It can help the user find important elements on a page. For those with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"), white space has been shown to ease reading difficulties and improve understanding of content.

Make sure users can also adjust the amount of white space around
objects and text via a web extension or user setting. This supports
the ability to identify important elements in the content of a web
page.

##### 4.4.10.4 More Details

Use clear spacing between letters, words, sentences lines,
paragraphs, and blocks of text.

Allow for the ability to easily adjust white space around objects and text, including boxes, paragraph headings, and content, to a degree that suits the user and does not disrupt the overall integrity of a web page. Do not add so much white space that important content cannot be seen above the scroll.

Note that “white space” is a term that means the background color. It does not always need to be always white!

##### 4.4.10.5 Examples

**Use:**

1. White space around separate sections of the content.

**Avoid:**

1. Dense pages.

#### 4.4.11 Ensure Foreground Content is not Obscured by Background (Pattern)

##### 4.4.11.1 User Need

I need to easily perceive the content, for example:

- Text is clear because the background is plain.
- Media does not have distracting background noise.

Related User Story: [Visual Presentation](#visual-presentation-user-story).

##### 4.4.11.2 What to Do

Do not overlay words on busy backgrounds. Provide an option to remove background
noise behind auditory content or ensure background sounds do not interfere with
the main auditory content.

For text:

- Use solid backgrounds for blocks of text.
- Use thick outlines with solid fills for text that is overlaid on background that has designs running through it.
- Use strong color contrast.

For auditory content:

- Avoid fast changing background content behind foreground auditory content (such as background conversations or unnecessary traffic noise).
- Provide an option to remove background noise behind auditory content.

##### 4.4.11.3 How it Helps

Reading a sentence phrase by phrase conveys more meaning than reading individual words. Phrases are also easier to comprehend. The more words an individual can process in one glance, the faster they can read, the easier they can understand what’s written, and the more they stay interested. Most people can take in a whole line of text, or more at once. Fixating on many words at a time is necessary for comprehension for many people. A slow reader may read a sentence slowly using 6 to 9 eye fixations, sometimes taking in only a single word (or part of a word) at a time. Adding backgrounds reduces the number of words readers can fixate on. Removing backgrounds helps users comprehend more words at the same time.

Also, automatic word recognition is often used for reading comprehension. For example, approximately 200 words exist in the English language that do not fit traditional letter sound patterns. These words must be memorized and automatically recognized. If a user can’t recognize these words, the text is harder to understand. Backgrounds can increase the amount of time it takes users to recognize words.

Similarly, background noise in an audio track can make it harder to process and understand the main content.

##### 4.4.11.4 Examples

**Use:**

1. Easy to recognize words and content that can be easily distinguished from the background.

**Avoid:**

1. Backgrounds that might make it difficult to read text, such as “Backgrounds behind text that make it difficult to recognize words and process text.”

#### 4.4.12 Explain Implied Content (Pattern)

##### 4.4.12.1 User Need

> I need to understand the meaning of the text. I do not want unexplained, implied, or ambiguous information because I may misunderstand jokes and metaphors.

Related User Story: [Visual Presentation](#visual-presentation-user-story).

##### 4.4.12.2 What to Do

Provide definitions or explanations for implied or ambiguous information such:

- body gestures,
- emotions,
- jokes,
- sarcasm,
- metaphors and simile, and
- facial expressions.

These definitions and explanations should be provided in text close to the implied content or in the markup (see best practices).

##### 4.4.12.3 How it Helps

Implied content can be difficult for some users because the meaning is not clear. This includes abstract content, sarcasm, or metaphors. The meaning is not clear and requires the user to have additional knowledge to understand.

When using body gestures, emotional communication, and facial expressions as the only way to communicate something, it is important to include this in another way to ensure all users understand. One way this can be done is through supplementary text.

For example, an image is used in a social media post to communicate a person’s true feelings. Some individuals may not be able to understand the emotion being demonstrated by the image. They miss the point the author is trying to make without more context.

Similarly, a research study asked [autistic](#dfn-autistic "Sometimes called “autism spectrum disorder”, “ASD”, “autism”, “asperger syndrome”, and “pervasive developmental disorder”.") people to watch a movie that had a lot of implied content. They were watching the actors’ mouths, but information such as sarcasm is communicated by their facial expressions. When asked what happened in the movie, some missed the implied communication and the point of the dialogue.

##### 4.4.12.4 More Details

This includes:

- graphics used alone to identify that something is important, or should be remembered,
- sarcasm in text, and
- animations used to add importance or communicate something contrary to the literal meaning of the paired text.

Note that standard emojis often come with an explanation or alternative text.

##### 4.4.12.5 Examples

**Use:**

1. Supplementary text such as (sarcasm) when writing sarcastic comments in emails and social media posts to help readers understand the intent of the communication.
2. Personalization semantics (once it is mature) to add non-literal text alternatives. See [[personalization-semantics-help-1.0](#bib-personalization-semantics-help-1.0 "Personalization Help and Support 1.0")].

**Avoid:**

1. Unexplained metaphors and similes. For example: “You are my sunshine.” rather than saying “You make me happy.”

#### 4.4.13 Provide Alternatives for Numerical Concepts (Pattern)

##### 4.4.13.1 User Need

> I need words rather than numbers and numerical concepts.

Related User Story: [Math Concepts](#math-concepts-user-story).

Provide alternatives for numbers and numerical concepts.

##### 4.4.13.2 What to Do

Provide alternatives for numbers and numerical concepts.

##### 4.4.13.3 How it Helps

Not all people can understand numbers and numerical concepts.

For example, some people have dyscalculia, a learning disability
specifically-related to mathematics. People with dyscalculia have
significant problems with numbers and mathematical concepts, but
often excel in other intellectual areas.

For example, a user with dyscalculia may have difficulty processing
temperature data when presented only in a numeric format. However,
if non-numeric alternatives are provided (cold, warm, hot etc.) then
they are able to understand the content.

Numeracy issues can occur due to a range of disabilities, the most
severe being the inability to read or understand numbers. Other
people have challenges with any calculations such as relative sizes
or times.

For example, a user may understand the concept of 90cms as a length but find it hard to cope with the fact that 0.9m and 900mm are the same length.

In another example, a train schedule has a list of relative times that the train leaves on the hour. The user cannot calculate when the next train leaves from their location.

##### 4.4.13.4 More Details

Where an understanding of mathematics is not a primary requirement
for using this content use one of the following:

- Reinforce numbers with non-numerical concepts, e.g., very cold, cold, cool, mild, warm, hot, very hot.
- Once it is mature you can also use personalization semantics to add non-numerical concepts. See [[personalization-semantics-help-1.0](#bib-personalization-semantics-help-1.0 "Personalization Help and Support 1.0")].

Note that other users may find math easier to
understand than long text.

Where some math skills are essential for the content:

- Move towards digital math that can be extended (not numbers in
  images).
- Enable highlighting of sections as they are being discussed.
- Link sections of numbers to extra help that can be read together.
- Enable replacing math sections with words or summaries for users
  who prefer this.

##### 4.4.13.5 Examples

**Use:**

1. Extra support for numerical content such as:
   - sizes
   - quantity
   - distance
   - time
   - date
   - temperature
   - positive/negative
   - calculations
   - sequencing
   - percentages.

   For the above, there is a description or representation of what the number means as a concept.

**Avoid:**

1. Numerical content without extra support

### 4.5 Objective 4: Help Users Avoid Mistakes and Know How to Correct Them

Users should be able to avoid mistakes and correct them easily if mistakes occur.

It is difficult for many users to complete forms, especially people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). A good design makes errors less likely.

Users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") are more likely to make mistakes. This can include entering information incorrectly or accidently touching the wrong control. Help the user notice form errors and make it easy to correct them. Always let users go back and recover if they accidentally touch a control.

Completing forms and similar tasks is often overwhelming for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). Many users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") cannot remember numbers, such as zip or post codes or their social security number. Many users even need to check their phone numbers. This makes entering information slow, and they may need to leave their desks or take breaks. Help them by providing a design that reduces mistakes. Give them the time they need without annoying timeouts and data loss.

#### 4.5.1 Ensure Controls and Content Do Not Move Unexpectedly (Pattern)

##### 4.5.1.1 User Need

> I need to know where things are. Controls and content do not move unexpectedly as I am using them.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.1.2 What to Do

Make sure controls and content remain in place and do not move, unless the user initiates the movement.

A user may initiate a movement by triggering an action or by altering a property of the device, such as window size.

This can usually be achieved by:

- ensuring controls and content do not move about as the page loads or refreshes,
- displaying a clear “loading” indicator if content moves or changes during a page load,
- not updating or moving content, such as an item’s position in a list, unless the user causes it.

##### 4.5.1.3 How it Helps

If a control moves, users with slow hand-eye coordination or impaired cognitive processing speed may hit the wrong control. This causes unwanted actions and errors. The user may experience disorientation, confusion or even incorrect understanding of the content.

For example, a user moves to press a button on a video. The user accidentally nudges the device. The orientation changes to landscape and the control moves. Because the user has slow eye tracking or hand-eye coordination, they end up pressing a link to a new video.

Shifting controls and content can also cause cognitive overload and increase mental fatigue. For example, as a user with Traumatic [Brain Injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments.") reads content, the content refreshes and an additional article appears above the current content. The article the user is reading moves down. The user becomes disoriented and the application becomes very hard to use or understand.

##### 4.5.1.4 More Details

Controls moving unexpectedly includes:

- links in a list shifting positions,
- orientation changes, and
- slow loading of a page that the user thinks is complete.

##### 4.5.1.5 Examples

**Use:**

1. Controls and content that do not move about as the page loads or refreshes.
2. A loading icon, that is clearly visible while the page is loading. After the content is finished loading and there is no further movement, the icon is removed.
3. Controls and content that only move when the user initiates a change.

**Avoid:**

1. Controls and content that move without the user’s request. For example: The user is about to select a phone number to call. As the user is about to touch the phone number, it shifts down. The user presses the wrong phone number and calls the wrong person.
2. Links in a list shifting positions.
3. Orientation changes that cannot be easily turned off.
4. Slow loading pages that the user thinks are complete.

#### 4.5.2 Let Users Go Back (Pattern)

##### 4.5.2.1 User Need

> I need predictable back or undo features so that I know exactly where I was previously, before I made a mistake.

Related User Story: [Undo](#undo-user-story).

##### 4.5.2.2 What to Do

Always let the user return to a previous point.

The standard back button is the best way to do this as it is familiar
to the user. Many users will try the back button first.

The user should never lose their work if they press back.

##### 4.5.2.3 How it Helps

Allowing users to return to a previous point helps prevent mistakes and makes it easy to
correct mistakes when they happen.

Examples of mistakes include:

- touching a control by accident,
- opening a new link by accident, and
- closing a window the user intended to keep open.

If a person easily makes mistakes or makes them often, it is
important that they can go back and make changes without having
their work or previous choices deleted.

For example, a user is watching a video. They try to increase the
volume but touch a different link instead. A new video now loads.
The user can press the back button and return to the video they were
watching before. They now know they can try and increase the volume
and if they make a mistake, they can easily go back and try again.

In another example, the back button did not work as expected, but took them somewhere else (such as the home page). When they try to change the volume or add a comment they often lose the video they were watching and cannot find the way to get back to it. The user now feels they cannot use any of the web site’s features in case they lose their main content again. They do not expand the screen, change the volume, or leave comments.

In forms, each time the user has to re-enter data presents a new chance for mistakes to occur. Entering and re-entering data can be stressful and tiring for some people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). This increases the likelihood of mistakes and may make it impossible to submit correct data and complete the intended task.

For those with anxiety, memory challenges, and difficulty following
directions, the ability to go back and review information they have
entered is very important. For example, for some people the task of
following directions and reviewing their answers works best as two
separate tasks. Being able to enter information with their focus
being on following the directions, and later going back to review
their answers, helps them be more effective.

##### 4.5.2.4 Getting Started

When the user has an opportunity to go back and review the data they entered, even if submitted by mistake. The back button always works as expected.

##### 4.5.2.5 More Details

Options for supporting users going back include:

- Going back steps in a user journey via a clearly labeled
  action.
- Using clickable breadcrumbs with clickable previous steps
  and no loss of data.
- Using back and undo features without unwanted data loss.
- Once it is mature you can also use personalization semantics to log the steps and return to
  a step in the process. See [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")].
- Reopening a closed window or option.

##### 4.5.2.6 Examples

**Use:**

1. Designs that make it easy to go back. For example:
   - The user is watching a video. They touch a control accidentally. Pressing back can take them back to the video at the same position.
   - A user is completing an online form when applying for a job. The user accidentally hits the home icon and navigates away from the form. The back button takes them back to where they were without any loss of data.
   - The user is also able to go back through all the screens to be sure they did not misunderstand a section or skip an answer. The user can edit any data they mistyped.

**Avoid:**

1. Designs that make it hard to go back. For example:
   - The user is watching a video. They touch a control accidentally and go to a new video. Pressing back makes the new video smaller and does not take them back to the original video.
   - Completing an online form when applying for a job. The user goes back to a screen to check if they have forgotten to answer a question. When they use the back button all data previously entered has been cleared/deleted.

#### 4.5.3 Notify Users of Fees and Charges at the Start of a Task (Pattern)

##### 4.5.3.1 User Need

> I need support to manage the task, such as letting me know what information I will need (credit card, full address, etc.) before I start.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.3.2 What to Do

Tell the user about all charges at the start of a transaction
including typical values. Any conditions and terms should also be
available at the start of the transaction in easy language.

##### 4.5.3.3 How it Helps

Users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") who have trouble with memory, attention to detail, or reading comprehension may not be aware of charges unless they are explicitly noted at the start of a transaction task. Terms and conditions can be under a link, but charges must be clearly displayed and available in [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.").

Clearly identifying charges at the start of a sale benefits all users. Those with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") will particularly benefit because some groups are less likely to have inferred or guessed the charges would be included. They may not know to look in other places in the user flow, such as on the homepage, or on a designated rates page.

People with impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") or memory need to have all the consequences presented in an orderly form to be able to make an informed decision. When charges are not clear, the consent of the transaction is unclear.

It also can take much longer for users with disabilities to go through the process of making a purchase. If a person has spent hours making an online purchase, it is much more difficult and upsetting to find out that they cannot afford it. They will often blame themselves for not understanding the price and may experience a loss of confidence. They may stop trusting themselves with online, day-to-day activities.

For example, a person who has challenges with [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") may be trying to order a plane ticket, and not realize that there are extra fees not quoted in the original price, such as taxes, international fees, baggage fees, etc. They may spend hours booking a holiday only to find that they cannot afford it. Alternatively, sometimes they end up purchasing something they cannot afford. Also, even if they have completed this process in the past, they may not be not able to use their experience to anticipate the final price. The result is the user loses confidence in their ability to independently purchase a holiday online. They may have a debt they are unable to pay, may not attempt again, or only with the help of a hired professional (e.g. travel agent or assistant).

##### 4.5.3.4 Examples

**Use:**

1. Clearly stated charges. Users are aware of all charges and can make an informed decision when they decide to purchase an item and put it in a shopping cart.
2. Clearly stated of ranges of possible charges. For items with shipping charges that vary, list the range of shipping charges and the issues that change the rate, along with a link to where more details can be found. For example, weight and speed of shipping may impact your shipping fees which can be between $4 and $400 depending on location.
3. There are no surprise conditions.

**Avoid:**

1. Final transactions that include new charges or hidden fees, that result in higher-than-expected total charges.
2. Final transactions that include conditions of purchase that are not clear to users from the beginning of the task.
3. Transactions that contain charges or conditions that the user did not know about until they had invested a lot of effort into the sale.
4. Completed transactions that surprise the user with the total cost.

#### 4.5.4 Design Forms to Prevent Mistakes (Pattern)

##### 4.5.4.1 User Need

> I need an interface that helps me avoid mistakes.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.4.2 What to Do

Choose a form design that reduces the chance that the user will make a mistake. This includes:

- Requiring the user to enter as little information as possible.
- Clearly indicating required fields.
- In a text field, accepting as many formats as possible. For example, accepting different formats of phone numbers.
- Dividing long numbers into chunks (supporting autocomplete across fields).
- Using an interface where only valid input can be selected.
- Using autocomplete and personalization of form controls.
- Accepting voice prompts when supported by the operating system.
- Automatically correcting input errors when possible and reliable.
- Providing the user with known suggestions and corrections.

##### 4.5.4.3 How it Helps

After making many errors, people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") and users with [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") often abandon their tasks and believe they cannot complete them. Error messages may be confusing. Correcting errors is often difficult and frustrating for users and increases cognitive fatigue. Many users need to stop when they get successive errors.

For example, while registering for an online banking account a form requires the input of the user’s birthdate. The required input format is xx/xx/xxxx with a leading zero for single digits. If a single input field with no input correction is presented, a user with a cognitive disability may enter 1/3/1996 triggering an error notification. It may not be clear to the user that the required format is 01/03/1996 (even if the format is shown below the input field or in the error notification).

A well-designed form makes it easier to fill in the information and prevents the user from making mistakes by automatically correcting or suggesting the correct date format.

Minimizing user generated errors by automatically correcting them will also minimize error notifications. Error notifications may be tiring and distracting, taking focus away from tasks and task completion.

##### 4.5.4.4 More Details

- Clearly mark required content.
- Only correct errors if the correction is reliable. Otherwise, if
  suggestions for corrections are known, give the suggestions to the
  user.
  - For example, “Did you mean the first of February (01/02) or the second of January (02/01)?”
- Calendars and dates.
  - Calendars should default to the first relevant day. Work calendars should default to the first working day of a user’s locale.
  - Calendar-based booking systems must prevent the user from booking the
    return date before the departure date.
- Temperature.
  - Use the default temperature format of the user’s location.

##### 4.5.4.5 Examples

**Use:**

Designs that make mistakes less likely. For example:

- Correcting errors of the post code being written in the text field
  with the city or state information.
- Preventing the user from selecting inappropriate dates and providing a simple
  explanation if the user attempts to do so.

**Avoid:**

Designs that make mistakes more likely. For example:

- The booking form provides two calendars without clear labels and
  instructions. The form allows the user to select dates without warning as to
  whether they are possible e.g. flight out on June 1st - flight
  return May 30th.
- The system allows the user to select inappropriate dates without warning. The calendar
  merely grays out inappropriate dates which may not be noticed. No
  warnings are provided.

#### 4.5.5 Make it Easy to Undo Form Errors (Pattern)

##### 4.5.5.1 User Need

> I need to check my work and go back without losing the work I have just done.

Related User Story: [Undo](#undo-user-story).

##### 4.5.5.2 What to Do

Always allow the user to check their work and correct any mistakes.
Once the user has fixed their mistake it should be easy to get back to
the place they were at without redoing additional steps.

For financial transactions and important information, allow the user
to easily cancel the transactions. Provide clear information and
simple instructions for important information such as the amount of
time the user has to cancel a transaction.

##### 4.5.5.3 How it Helps

People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") make many more
mistakes filling out forms than the general population. When
mistakes cannot be easily corrected they cannot complete the task.

The ability to undo errors helps people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") safely use forms
and reduces the consequences that result from a mistake.

For example, a user with a memory impairment may not remember that
they have already added an item to their shopping cart and may add
the item a second time. They may confuse the dates when booking a
trip or make other mistakes.

It is essential that people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") have the
opportunity to check their work and fix their mistakes easily.

For people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"), mistakes being theoretically
reversible is not enough. Often the process of reversing a
transaction is too complex for them to manage without help. They may
not have access to that help meaning they have to live with all the
mistakes they have made. In
addition, if the process of correcting mistakes is too difficult,
users may stop, either losing the transaction or buying unwanted
items.

The effect of this happening multiple times is devastating. As a result,
many users with disabilities may stop using
the Internet for many tasks.

Allowing the user to change the number of items in the shopping cart
at any time can significantly reduce mistakes.

A summary of the order, including product quantities and other costs
before the final submission, gives the user the chance to identify
any errors and make changes to the order. In this example given, a
summary of the purchase helps the user see the error in quantity as
well as a higher than expected order total.

In some cases, a user may realize that a mistake has been made after
the final submission of data. Provide simple language instructions on how to
cancel transactions and help the user understand the amount of
time needed to cancel a transaction. This makes them less
susceptible to scams.

For example, a user with Attention-Deficit/Hyperactivity
Disorder purchasing a travel ticket on a web site may struggle with
details and may have an impaired attention span. The successful completion
of the order relies on the information provided at multiple steps in
the process. An error
such as an incorrect street number or zip code in the billing
address will result in the order not going though. If a summary is
not provided before submitting the final order, the
user may not understand the reason for the declined payment and give
up on the order. The user may also stop if there is not a clear and achievable
way to make a correction.

##### 4.5.5.4 More Details

This typically includes:

- Change: It is simple for the user to review all the data and
  correct mistakes, including mistakes that might not be
  automatically identified. The user can change information via
  clearly labeled actions and get back to the place they were at, in
  one clearly labeled action without unwanted loss of data. (Some
  data may need to be entered if it is dependent on the item that
  was changed.)
- Confirmed: A summary is provided before submitting important
  information and the user is told when they are about to submit the
  final information.
- Time frames and instruction for canceling transactions are clear
  and easy to follow.

##### 4.5.5.5 Getting Started

Start with forms where a mistake can have serious consequences such
as financial loss or vulnerability.

##### 4.5.5.6 Examples

**Use:**

- A summary provided before submitting important information. It allows the user to correct information and return to the summary with a single click.
- Clickable breadcrumbs that allow the user to see the previous steps, go back, and change them.

**Avoid:**

- A summary provided before submitting important information, but the user cannot make corrections without losing other data entered.

#### 4.5.6 Use Clear Visible Labels (Pattern)

##### 4.5.6.1 User Need

> I need clear labels, step-by-step instructions, and clear error messages.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.6.2 What to Do

Use clear labels. Labels should:

- use common words and [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well."),
- be visible and next to the relevant control, and
- be readable by assistive technologies, including those used by people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

##### 4.5.6.3 How it Helps

When labels are missing or unclear, users often do not know that the feature is available or what the control is. Although many users can guess what a control is for users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") with impaired memory or [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") are less likely to be able to remember the design pattern or work out what it is. A clear label that uses familiar terms and is located next to the control, helps people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

Similarly, if a label is not next to a control it is confusing for some users. When a label cannot be next to a control, there should be clear visual indicators that visibly and unambiguously associate the label with the control. This will need user testing with users who have learning and [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") to ensure it is usable.

For example, a user living with [early stage dementia](#dfn-early-stage-dementia) is using an application. Some controls do not have visual labels. A caregiver shows them what the control is for and they can use the application. The next day they try to use it again, but cannot remember what the control is for. This application is not usable for them.

In another example, the label disappears when the focus is removed. The user cannot remember what the control is and does not know how to make it reappear.

Labels need to be visible, readable by assistive technology, and be nearby the labeled content.

##### 4.5.6.4 More Details

Many people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") use web extensions and simple text-to-speech. These assistive technologies often do not read WAI-ARIA [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] or titles. Until that changes, or an extension displays them, labels should not rely on these attributes for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

##### 4.5.6.5 Examples

**Use:**

1. Visible labels that use simple common words and are next to the control. For example:
   - first name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Avoid:**

1. Hidden labels or labels that use uncommon words that are not easy to understand. It is unclear what action is needed. For example:
   - given name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### 4.5.7 Use Clear Step-by-step Instructions (Pattern)

##### 4.5.7.1 User Need

> I need clear labels, step-by-step instructions and clear error messages, so I know exactly what to do.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.7.2 What to Do

Write clear instructions that are:

- located before, or next to, the field or activity,
- broken down by steps (ensure that steps are not omitted)
- clear, concise, and accessible, and
- available with examples or illustrations that make it easy to understand what to do.

##### 4.5.7.3 How it Helps

Clear instructions help prevent user errors. This reduces frustration and enhances users’ autonomy and independence because they can avoid asking for help. This helps many people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") as well as people from different cultures, emerging markets, and new users who may not be familiar with web forms or may miss cultural context.

For example, a person with [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") is trying to complete a form. They put the whole address and zip or postal code in one line (as one would do when writing a letter). They are given an error message. After a few error messages, they are exhausted and cannot complete the form.

##### 4.5.7.4 More Details

Provide instructions at the start of the process, not simply in an
error message.

Provide instructions needed to enable the user to complete the task. When multiple formats are accepted or errors are automatically corrected, less instructions are needed for the user to complete the task.

Note that instructions can be hidden behind a familiar icon.

##### 4.5.7.5 Getting Started

In a system with common errors, tackle the most impactful errors
first and add guidance as needed.

##### 4.5.7.6 Examples

**Use:**

1. Clear and easy to understand instructions. For example:
   - Provide an image of a passport with the number highlighted to indicate the number that the user should enter.
   - Explicitly say which day of the week is the start (e.g., Sunday or Monday) in calendar controls.

**Avoid:**

1. No clear instructions for complex tasks. For example:
   - Request a passport number, but do not indicate which of several numbers on the passport is needed.
   - A site does not clarify the first day of the week and assumes the work week starts on Monday. A user from a different culture assumes the work week begins on Sunday, and makes a mistake.

#### 4.5.8 Accept different input formats (Pattern)

##### 4.5.8.1 User Need

> I need inputs to accept different formats and not mark them as mistakes.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.8.2 What to Do

Accept all format variations in text inputs for values such as currency, time zone, locale, address, or credit card number.

##### 4.5.8.3 How it Helps

Forgiving form entry processes help the user fill out forms, without an overwhelming amount of errors. They can avoid asking for help when errors cause them problems. This reduces frustration while enhancing the user’s autonomy and independence.

This benefits anybody with a learning and cognitive disability or [age related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)"). It will also help anyone who is used to a different format.

For example, a user with [age related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") enters their phone number with hyphens inserted. They receive an error message, because the system does not accept that format. They wonder if they have forgotten their phone number or made a different mistake. They stop trying to use the form.

##### 4.5.8.4 Examples

**Use:**

1. Platform facilities for flexible input types and validation.
2. Research and support for different formats that might be entered, including international variations.
3. Minimal required fields.
4. Flexible input fields that accept different formats. For example, an input field that accepts:
   - various currency symbols,
   - a credit card number with or without spaces,
   - telephone numbers as written in many regions, including country code, region code, and number using optional brackets, and
   - international characters such as those with accents.

**Avoid:**

1. Restricting entries to arbitrary lengths.
2. Insisting on specific separator characters if they are not required and can be ignored.
3. Input fields that do not accept the format that the user may use. For example:
   - Forcing users to use a specific currency value that they may not be their currency.
   - A credit number field that requires no spaces even though cards have numbers printed with spaces.
   - Telephone number field will not accept + codes or brackets.

#### 4.5.9 Avoid Data Loss and “Timeouts” (Pattern)

##### 4.5.9.1 User Need

> I need time to complete my work. I do not want a session to timeout while I try to find the information needed, such as my postal/zip code or social security number.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.9.2 What to do

Avoid timeouts and let the user save their work as they go.

When this is not possible, inform the user when they initiate the process:

- the amount of time available to complete the process,
- if the user will lose entered data if a timeout occurs.

##### 4.5.9.3 How it Helps

Timed events can present significant barriers for users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). These users may require more time to read content or to perform functions, such as completing an online form. They may need to read help or look at notes.

Users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") may need additional time to look up the information required to complete a transaction. They may need a break, without losing their place in the process, and without losing data that has already been entered.

For example, while making a purchase on an e-commerce web site, a user does not remember required information. This may be a date, a phone number, or a zip code that may seem easy to remember for users without a cognitive or learning disability. They need to look up this information, which takes them time away from the screen. Then they need to copy it carefully into the form.

In another example, a user is completing an online process for reserving a hotel room and purchasing a plane ticket. They become overwhelmed with the amount of instruction and data input required to complete the process. The user cannot complete the process in one sitting, and takes a break.

Users’ cognitive skills may diminish as they get tired. They then must stop the task for that day. When users know that their data won’t be lost, they can recover from mental fatigue and return to successfully complete the task.

It is important to note that many people need time to read the “timeout” notice. Often, the session ends before the user has finished reading about how to extend the time. If the user is looking up information, they will not see the timeout notice.

##### 4.5.9.4 More Details

When a web site must timeout because sensitive information (such as credit card information) is entered or displayed, the web site should ask for the sensitive information at the last stage.

The web site should also warn the user that once they give the credit card information they should complete the process quickly as the session can timeout.

##### 4.5.9.5 Examples

**Use:**

1. Unlimited time, when possible.
2. Timeouts that users with learning and cognitive disabilities find it easy to avoid. For example: At the start of the task the user is told that they have a day to complete the task. They have an option to set it to longer.
3. When the timeout is needed:
   1. **Timeout warnings at the start of the task.** For example: In an auction, there is a time limit on the amount of time a user has to submit a bid. At the start of the task, the user is warned about the time limit, and how long they have until the time ends.
   2. **When possible and safe, the user’s work is not lost.** For example: A web site with sensitive information uses a client-side time limit to help protect users who may step away from their computers. When the user logs in again all the work is still in place. The user is warned ahead of time how long they have for inactive sessions and is told that their data will not be lost.

**Avoid:**

1. System timeouts that are not necessary for security.
2. System timeouts without warning the user at the start of the process.
3. System timeouts where the user loses their work, without it being a security or privacy risk.

#### 4.5.10 Provide Feedback (Pattern)

##### 4.5.10.1 User Need

> I need rapid feedback or visual cues to indicate an event was successfully triggered. For example, I need to know when an email has been sent, otherwise it looks as if it has just disappeared.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.10.2 What to Do

For each step in a process let the user know of its status and if it
was successfully completed.

##### 4.5.10.3 How it Helps

Making the result of each user action clear helps people with a
variety of [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). This includes:

- understand that their actions were processed (e.g., the click did
  something),
- prevent uncertainty or doubt regarding the outcome, and
- remember what they just did.

For example, a user with [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)"), may have difficulty remembering how the interface worked. So when they press the send button they may not feel confident that the form was submitted. Feedback, such as a thank you message, will tell them submission occurred and make them feel confident in the process.

During a multi-step task this feedback (user-action feedback) can also assist people with attention or short-term [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") to remember what they are doing. For example, a user with early dementia may get distracted and then forget exactly where they were in the task. This user-action feedback helps re-orient them. It also helps them avoid leaving a task by reminding them that they are in a process, and where in the process they currently are.

Provide easily-recognizable success or failure feedback with every
user action. When possible, the feedback should use consistent and
familiar design patterns. For example:

- After a step in a multi-step task is completed, breadcrumbs display a tick, or a checkmark next to that step’s name; and, if applicable, the title or the name of the next step is readily apparent.
- After a button is clicked, it should look depressed. (Note that if
  it is a toggle button, the state should also be programmatically
  determinable).
- After a form is submitted or an email message is sent, feedback communicating what just happened is provided, such as “Your application was submitted, thank you” or “Your email message was sent”.

##### 4.5.10.4 More Details

The success or failure of every user initiated action is clearly
indicated to the user by visual, programmatically-determinable,
rapid feedback in the primary modalities of the content. Audio
feedback is supported.

##### 4.5.10.5 Examples

**Use:**

1. Visual state feedback. Use CSS and WAI-ARIA [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] states such as aria-pressed and aria-selected, to gives a visual change that shows the change in state. For example: Buttons and tabs with a visually clear state when selected.
2. Messages that let the user know if a task is completed. For example:
   - Confirmation messages when an email message is
     successfully sent, or a form is successfully submitted.
   - Visible and programmatically-determinable information to
     show that a new password is set.

**Avoid:**

1. State changes without visual feedback.
2. Task succeeds or fails without feedback.

#### 4.5.11 Help the user stay safe (Pattern)

##### 4.5.11.1 User Need

> I need to know I am safe and secure when using a web site, especially if providing information or communicating with others.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.11.2 What to Do

Keep the user safe. This includes:

- Understand risks for people with learning and cognitive disabilities when providing personal information or communicating with others.
- Checking how safety and security techniques work with a wide range of customized profiles including aging users and users with learning and cognitive disabilities.
- Using known techniques to keep sensitive user information safe.
- Helping all users understand any relevant known risks. Explain any known risks in easy to understand and friendly language.
- This helps them make an informed decision and stay in control.

##### 4.5.11.3 How it Helps

Users need to know they are safe and secure when using a web site, especially when providing information or communicating with others.

Users with impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") are less likely to identify risks correctly so clearly identifying potential risks helps the user stay **safe and in control**. Add helpful tips for staying safe while using your content and provide help in case of problems.

To help identify risks, we suggest holding research and focus groups with people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") and to work with people with cognitive and learning disabilities to solve potential and existing problems. Groups should have people with learning and cognitive disabilities in mind when working on security and risk mitigation.

For example, many people who cannot copy and paste passwords or use two-step authorization codes ask a caregiver to help them. As caregivers are often just temporary employees, this leaves the user exposed. Making passwords longer or requiring users change them regularly increases these unsafe practices and can actually make the application less secure. This type of design error is common when people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") are left out of the user research and analysis.

##### 4.5.11.4 Examples

**Use:**

1. Alternative login options that have been tested with people who have learning or cognitive disabilities that are approved security techniques, in your jurisdiction, for sensitive data.
2. Talking to a wide range of people with learning and cognitive disabilities, to understand the risks and how they may relate to personal information.
3. COGA persona and use case in the research, development and requirements phases.
4. Industry best practices for storing and securing user information.
5. Consent forms in [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") that have been tested with people with learning and cognitive disabilities to ensure they understand the risks.
6. Warnings to users each time personal information may be given, in [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.").

**Avoid:**

1. Users sharing information without understanding all the risks.
2. Hidden and confusing information about risks.
3. Users giving consent one time, and forgetting about the risks they are currently facing.
4. Consent forms that users may not understand.

#### 4.5.12 Use Familiar Metrics and Units (Pattern)

##### 4.5.12.1 User Need

> I need interfaces to use metrics I know, and that are common in my location (such as feet or meters) otherwise I get confused. I do not always know what metric they are talking about or notice that the number looks wrong.

Related User Story: [Assistance and Support](#assistance-and-support-user-story).

##### 4.5.12.2 What to Do

Provide metrics in units that users will be familiar with.

##### 4.5.12.3 How it Helps

Most people are familiar with a single set of units that are commonly used for metrics in their location or culture. When the metrics are in other units they need to perform a conversion in order to understand them. Even tools such as a calculator can be hard to manage. Provide an option to change units and default the units to the users’ location. Common examples are the units used for distance, weight, area, currency, and temperature.

For example, a user may know the temperature in Centigrade. When it is given in Fahrenheit, they think it is going to become very warm.

##### 4.5.12.4 More Details

Sometimes metrics are commonly declared in a specific unit even when localized alternatives are available. For example, TV or monitor sizes are usually given in inches even when centimeters are the common unit. However, even, in these cases, providing alternatives are still useful as users may not be familiar with the metrics given.

##### 4.5.12.5 Getting Started

Provide a mechanism to select a different set of metrics that are more meaningful to the user, or provide common alternatives in the text

##### 4.5.12.6 Examples

**Use:**

1. Metrics in different units that different users understand. For example:
   - The Eiffel Tower is 1,063 feet (324 meters) tall, including the antenna at the top.

**Avoid:**

1. Only one unit for metrics. For example:
   - The Eiffel Tower is 1,063 feet tall.

### 4.6 Objective 5: Help Users Focus

Distractions can prevent users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") from completing their tasks.

Once users become distracted, they may find it difficult to remember what they were doing. Then they can no longer complete their task. This is especially problematic for users with both impaired attention and impaired memory, such as users with dementia.

Avoid using any content or elements that distract users or interrupt them. Also, consider removing content the user will find unnecessary. Provide clear headings and breadcrumbs to help users reorient and refocus if they lose focus.

Also, help users maintain focus on their task by telling them what information they may need to prepare at the beginning of the task, so that they can collect all required information before starting.

#### 4.6.1 Limit Interruptions (Pattern)

##### 4.6.1.1 User Need

> I need tasks to not have distractions.

Related User Story: [Distractions](#distractions-user-story).

##### 4.6.1.2 What to Do

Avoid interruptions. This includes:

- Providing an easy way to control interruptions, reminders, and changes in content unless they are started by the user or involve an emergency.
- Allowing the user to control and limit types of content which could cause them distraction or an undesirable reaction.

This content includes: Social media, violent content, advertisements, distracting backgrounds and images, moving content, soft and loud noises, or triggers.

##### 4.6.1.3 How it Helps

Interruptions stop people with memory or attention impairments from completing their task. This can include individuals with Dementia, those that have had a stroke or [brain injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments."), and those taking medications with side effects impacting memory or attention. Certain types of interruptions or a certain number may cause them to stop, even if the task is very important. Interruptions can include sounds, content that visually appears or changes (such as advertisements on a page). Interruptions can be as simple as text notifications about the presence of new changes while working in a shared online document.

A site will work best for those with memory or attention challenges
if they have:

- a quiet and simple environment,
- no interruptions at all,
- an easy to use pause option so interruptions and moving content can be viewed later, or
- a setting where users can select which types of interruptions they can manage and when.

Many news web sites have a lot of interruptions that can cause
challenges for people needing to read important information, such as
school closures due to bad weather. They may encounter breaking news
text, advertisements, and pop-up windows. For those with difficulty
focusing and sifting through the school names, or have two or three
they need to check, these distractions may make the task impossible.
By letting the user pause these distractions, and ideally
temporarily remove them from the page, they will better be able to
complete the task.

Some people are sensitive to noise and can easily become overwhelmed by too many stimuli.

Sometimes, noises and different types of content may adversely affect [mental health](#dfn-mental-health "May include: mental heath impairments."). For example, noises, distractions, or distressing content may make the user more anxious or possibly trigger post-traumatic stress disorder (PTSD). There has also been research to suggest that too many interruptions and use of social media may aggravate depression and difficulty focusing. Allowing users to control this content could help them be more productive online.

Where standard techniques exist to remove or control distractions, they should be used.

For example, a person with traumatic [brain injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments.") is filling out their taxes online.
The social media application pings them with notifications. They try to turn notifications
off and then they try to turn off the application, but it is too complex. They are unable
to submit their taxes without help.

##### 4.6.1.4 Examples

**Use:**

1. Tasks without interruptions.
2. An easy way to control interruptions that may be needed. For example:
   - An application lets the user decide how they want to be notified about reminders and emails. Users can choose visual reminders, sounds, or none. They can flag users as essential contacts who can interrupt in most cases. These settings are easy to find from every screen. For some users, not having any notifications enables them to focus on a task and then go to their emails or calendar when the task is completed.

**Avoid:**

1. Distracting content that is hard to turn off, or cannot be turned off. For example:
   - There are advertisements on a magazine article page that constantly change, interrupting a reader’s focus.
2. Content that interrupts the user from completing their task. For example:
   - A pop up suggesting the user subscribers to the site. The pop up must be closed for the user to continue.

#### 4.6.2 Make Short Critical Paths (Pattern)

##### 4.6.2.1 User Need

> I need to be able to find features and content easily.

Related User Story: [Distractions](#distractions-user-story).

##### 4.6.2.2 What to Do

Streamline processes and workflows so that they include only the minimally
necessary steps. Separate out optional steps that are supplemental but not required. Do not
require the user to go through optional steps.

##### 4.6.2.3 How it Helps

Streamlining processes and workflows reduces distractions, mistakes, and mental fatigue. Using short critical paths increases the chance that users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") can successfully and accurately complete a process or task and navigate a workflow.

For example, a user with [early stage dementia](#dfn-early-stage-dementia) is trying to buy a new phone. Before they can pay, steps are added offering them headphones and other items. They become overwhelmed and confused. They leave the site without buying the phone.

##### 4.6.2.4 Examples

**Use:**

1. Processes that only require necessary steps.
   - For example: The steps included in the online process to buy movie tickets are:
     - select a movie,
     - select the date and time,
     - select seats,
     - pay,
     - print or save tickets.

     The movie theater allows the user to view descriptions about the movie and ratings, buy snacks ahead of time, and donate to a charity. These actions, or steps, are not required in order for the user to complete the task of purchasing a movie ticket. Instead of requiring the user make these selections as part of the purchasing process, the user is given these options before the process is started and after it is complete.
2. Short navigation to key features. For example, for the most used function in an app:
   - open the app,
   - run the most used function.

**Avoid:**

1. Adding unnecessary steps. For example, the steps included in the online process to buy movie tickets are:
   - select a movie,
   - select the date and time,
   - select seats,
   - purchase snacks ahead of time or opt out,
   - make a charitable donation or opt out,
   - create an account,
   - pay,
   - print tickets.

The movie theater forces users to decide on snacks and make a charitable donation before paying for their tickets. While an opt out option is available, it is somewhat hidden on the screen, particularly on mobile devices, and users often stop when they cannot figure out how to pay.

2. Long navigation for the most used features. For example, for the most used function in an app:
   - go to the applications introduction page, press continue,
   - go to the applications main page,
   - go to a sub page,
   - select an option,
   - select another option,
   - run the most used function.

#### 4.6.3 Avoid Too Much Content (Pattern)

##### 4.6.3.1 User Need

> I need to find it easy to identify the content that I need, and do not need. Information I need to know and important information stands out, or is the first thing I read and does not get lost in the noise of less important information.

Related User Story: [Findable](#distractions-user-story).

##### 4.6.3.2 What to Do

Keep the interface simple. Provide users with five or less main choices on each screen and remove unnecessary content. This can be provided via a simplified version, as an alternative that is generated in real time from the same code base as the main content.

Extra links that do not relate to the main purpose of the page should be limited to the footer section. Extra choices can also be hidden under a “more” link or other clear and descriptive titles.

##### 4.6.3.3 How it Helps

Busy pages, too much text, too many images and too much other content can cause cognitive overload, anxiety and loss of focus. Keeping content down to a small number of important points reduces the clutter, calms the user, and allows for better understanding while aiding memory. For example, it can help slow readers or those with a short attention span, who may leave the page if it appears complex.

Simplified content and a consistent simple design helps reduce cognitive overload and decreases stress and mental fatigue. For example, a person with [early stage dementia](#dfn-early-stage-dementia) goes to their doctor’s application. There are five choices on the screen: appointments, ask your doctor a question, test results, approvals and more. Each option has an icon, clear text, and is separated by whitespace. In two clicks they have asked their doctor their question. They can easily select what they need without asking for help. More options are also available if they swipe left. However, they are unlikely to do so.

##### 4.6.3.4 More Details

Avoiding long paragraphs, lots of choices, and non-meaningful imagery ensures those with cognitive and learning disabilities can concentrate on the important points being made.

Keeping to a few short bullet points and limiting to one or two
images related to the main subject areas of a web site or service
allows the user to choose whether to explore the site further.

The intent of this pattern is not to clutter the page with
unnecessary information but to provide important cues and
instructions that will benefit people with cognitive and learning disabilities. Too much
information or instruction can be just as much of a hindrance as too
little. The goal is to make certain that enough information is
provided for the user to accomplish the task without undue confusion
or navigation.

##### 4.6.3.5 Examples

**Use:**

1. A simple interface. The main feature is much bigger than anything else. For example:
   - A search engine has its name and a large simple search box. All other content is smaller, lower down, and the user does not notice it unless looking for additional features.

**Avoid:**

1. Pages with unnecessary content. For example:
   - Too much text, long menus, and images set around long paragraphs of dense text. The message is lost in an overload of information.

#### 4.6.4 Provide Information So a User Can Complete and Prepare for a Task (Pattern)

##### 4.6.4.1 User Need

> I need to know how to start a task, and what is involved.

Related User Story: [Distractions](#distractions-user-story).

##### 4.6.4.2 What to Do

Emphasize the start of important tasks.

Before a user performs a task consisting of multiple steps, ensure they have an estimate of the
amount of effort required to complete the task. This should include:

- the time it might take,
- details of any resources needed to perform the task, and
- overview of the process and next step.

Once the user starts the task, ensure the user clearly understands when the task is still “in-process” and when it has been completed.

##### 4.6.4.3 How it Helps

Some users find distractions difficult especially when the distractions cause them to switch focus mid-task and subsequently return to where they left off. For example, a web site may have a large arrow pointing the way to the “book here” link. The arrow emphasizes the start of the booking task, and will help users know when they have started the task.

Often people need to manage their times of concentration so they can focus without interruptions. Prior advice on the time a task takes, its complexity, or working memory load enables them to better prepare and complete it. The list of required resources before starting the task, along with the number steps left until completion of the task, will help users avoid failures.

##### 4.6.4.4 Getting Started

Provide a generous estimate of time required and a list of all required resources at the start of a multi-step task or form. Break the task into steps.

##### 4.6.4.5 Examples

**Use:**

1. Visual cues when a user starts a task.
2. An overview of the process including the time it might take, and any resources needed. For example:
   - Before the user begins to book an airline ticket, a message is presented, “The average time for booking an airline ticket is 15-30 minutes. You will need your travel dates, the number of travelers, and each travelers’ passport to complete this process.”

**Avoid:**

1. Missing out important details about what the user may need. For example:
   - Another airline does not notify the user that they need their passport. The process times out when the user is trying to find their passport number. The user needs to start over or abandon the booking.

### 4.7 Objective 6: Ensure Processes Do Not Rely on Memory

Memory barriers stop many users from using products or accessing help or content.

People with any impairment that affects memory or language can find it difficult or impossible to overcome memory barriers.

For example, many users have an impaired short-term memory. On average people can remember 7 letters or items at the same time. A person with an impaired working memory may be able to remember one to four pieces of information at the same time (depending on the extent of the impairment). If they need to remember other tasks, such as track what they have done, they are likely to make mistakes.

Avoid barriers such as:

- navigating voice menus that involve remembering a specific number or term,
- remembering numbers while processing words on a voice menu,
- transcribing text, or
- remembering passwords.

Allow users access to content, services or help, without using processes that rely on memory. Make sure there is an easier option for people who need it.

#### 4.7.1 Provide a Login that Does Not Rely on Memory or Other Cognitive Skills (Pattern)

##### 4.7.1.1 User Need

> I need to be able to use a site without remembering or transcribing passwords and usernames.

Related User Story: [Accessible Authentication](#accessible-authentication-user-story).

##### 4.7.1.2 What to Do

Users can login, register, and reset credentials, without having more cognitive abilities then they need to use a simple web page. They do not have to:

- memorize character strings,
- perform calculations,
- copy content,
- answer puzzles,
- reliably reproduce gestures, or
- recognize characters presented on screen, and then enter them into an input field.

##### 4.7.1.3 How it Helps

People with [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:") often forget their passwords and are not able to login. Their solutions often are only sometimes helpful and have security risks:

- They may have to look at or listen to text several times to copy
  or type it into a form field.
- They may reuse a single password or use a simple-to-remember
  password, which they can remember.
- If they need to change their password or use a complicated
  password they may store passwords insecurely, such as written on
  pieces of paper which other people can see.

They may also struggle with other steps during login, such as:

- entering characters in the correct order,
- entering characters correctly with a limited number of tries (resulting in being locked out),
- finding a PIN,
- working out puzzles or distorted letters,
- copy characters correctly from another device.

Users can stop after getting frustrated with time-limited procedures or presentations of digital security tokens. Or they can be locked out of vital services because of their disability.

Without this design requirement, many people cannot use an application or content at all. See [Security and Privacy Technologies](https://w3c.github.io/coga/issue-papers/privacy-security.html) issue paper for the full description of this issue, and how it stops people from using web services that are often critical. For example, many people cannot make doctors’ appointments, etc., by themselves. This may be partly responsible for the reduced life expectancy of people with learning and cognitive disabilities.

##### 4.7.1.4 More Details

There are many ways to meet this design pattern:

- Use [Web Authentication: An
  API for accessing Public Key Credentials](https://www.w3.org/TR/webauthn/) [[webauthn-2](#bib-webauthn-2 "Web Authentication: An API for accessing Public Key Credentials - Level 2")] to support inclusive alternatives that do not rely on typical cognitive abilities. For example, hardware authentication devices, smartcard or FIDO.
- Provide automatic user authentication based upon the use of a trusted device (to which the user has already logged in with their own identity). The user does not have to transcribe characters, but may have to press a link to identify they have the device.
- Allow a biometrics option.
- Use a system the user is already logged into via third-party authentication services (e.g., OAuth etc.).

Methods of meeting requirements for alternative user
authentication would include:

- Clicking a link sent to an email address or a phone number.
  (Note that this is easy to implement and may be useful for
  minimal security, such as allowing comments on a blog.)
- Logging in by using information present in users’ personal documentation, such as the total number of a current account balance, with explanation on how to find this information.

##### 4.7.1.5 Examples

**Use:**

1. [Web Authentication: An
   API for accessing Public Key Credentials](https://www.w3.org/TR/webauthn/) [[webauthn-2](#bib-webauthn-2 "Web Authentication: An API for accessing Public Key Credentials - Level 2")].
2. Single Sign-on (SSO) that allow users to access many sites with a single login (federated login).
3. Two step authentication with Bluetooth links (no copying).
4. Quick Response Codes (QR Code).

**Avoid:**

1. Using two-step authentication that requires copying.
2. Using a password and not allowing pasting into the field.

#### 4.7.2 Allow the User a Simple, Single Step, Login (Pattern)

> I need the login process to be simple, and not multi-step.

Related User Story: [Accessible Authentication](#accessible-authentication-user-story).

##### 4.7.2.1 What to Do

Provide a simple, single-step alternative for logins.

##### 4.7.2.2 How it Helps

A simple login allows people with impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") or impaired memory to use applications. This is especially important for users who become confused or overwhelmed with multi-step processes. For example, a user with traumatic [brain injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments.") wishes to use a site for online banking. They may have put their finger on a fingerprint scanner to authenticate who they are. Other examples include some third party logins.

##### 4.7.2.3 Examples

**Use:**

1. Easy third party logins as an option.
2. The web authentication protocol [[webauthn-2](#bib-webauthn-2 "Web Authentication: An API for accessing Public Key Credentials - Level 2")] with a single step method that matches your security needs.

**Avoid:**

1. All login methods involving multiple steps.

#### 4.7.3 Provide a Login Alternative with Less Words (Pattern)

##### 4.7.3.1 User Need

> I need a login process I can use that does not rely on a lot of words (as someone with a severe language impairment).

Related User Story: [Accessible Authentication](#accessible-authentication-user-story).

##### 4.7.3.2 What to Do

Provide at least one login alternative that does not require reading or writing a lot of words

##### 4.7.3.3 How it Helps

This pattern allows people with language and communication disabilities to login without being overwhelmed by blocks of text.

For example, someone with a severe language impairment using an [AAC](#dfn-alternative-and-augmentative-communication-system "Any method, device, or application that can be used to help those who cannot use spoken language and need additional support by means of symbols, images, and/or text. For example, a screen with symbols that the user can select to speak the appropriate words or add them to a document.") device wants to send a message to their doctor. They can press the login with the icon they know and send a message without having to read text.

##### 4.7.3.4 Examples

**Use:**

1. Third party logins which have well known icons.
2. The web authentication protocol [[webauthn-2](#bib-webauthn-2 "Web Authentication: An API for accessing Public Key Credentials - Level 2")] along with an easy login option.

**Avoid:**

1. Logins that requires answering security questions.
2. Logins without a simple, word free, login option, or alternative.

#### 4.7.4 Let Users Avoid Navigating Voice Menus (Pattern)

##### 4.7.4.1 User Need

> I need to get human help, without going through a complex menu system.

Related User Story: [Voice Menus](#voice-menus-user-story).

##### 4.7.4.2 What to Do

Let people easily reach a human who can help. Do not require navigating menu systems to reach a human.

Design helpful voice menus by:

- Providing a known word or reserved digit (such as “0” or “help”) that can be used at any time to skip the voice menu and go directly to a person.
- Avoiding unnecessary steps or options.
- Avoiding unnecessary or distracting information such as promotional information.
- Using words normally used by people with a wide range of [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").
- Waiting for a slow speaker to respond.
- Allowing for a quiet speaker, repetition, and stutters.
- Supporting forgetfulness and [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:").
- Allow for easy error recovery.
- Following usability best practices.

##### 4.7.4.3 How it Helps

Many people cannot use voice menu systems. This often stops people from completing critical tasks by themselves. Often this can include making doctors’ appointments, getting health insurance, reaching social services, getting their water turned back on, etc.

If people cannot manage voice menus by themselves, they have to ask someone else to help them. This means the service is not accessible to them. Sometimes tasks are not done. For example, they may delay making a doctor’s appointment or other critical task as not to bother their helper. People often do not get the help they need or get it too late. (This may be partly responsible for the lower life expectancy of people with learning and cognitive disabilities.)

Why can’t people use complex menus?

- A good short-term and working memory (several seconds) is essential so that the user can remember the number or the term for the menu. Without these functions the user is likely to select the wrong number.
- Many users have an impaired working memory. For example, if you can remember 7 letters or items in your head at the same time they may be able to remember one or two. This makes them less likely to manage a menu system correctly.
- For example, a phone menu system (voice markup system) may have an option: “Press 3 for internal services”. To use this option the user must remember a digit 3 while figuring out if they need an internal service. Many people cannot do this. It also requires them to press the correct digit.
- When a lot of irrelevant information is given before the correct option, the user may have cognitive overload and stop. This is especially true if they did not understand all the earlier options and information.
- They may not understand the terms used. Having focused on the menu, they may forget why they are calling.
- Alternative routes, such as web menus, may be provided but are also complex. They are therefore not helpful.

The 0 digit, the word “help” or other culturally appropriate term, should be reserved for reaching a person. Consistently set the first option for each menu to: “to wait for a person who can help you press 0”. This can help everyone reach the support they need.

Test any system with a wide range of users with different learning and cognitive disabilities. Involving a wide range of users has made many voice systems accessible to the extent that they become an aid people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

##### 4.7.4.4 More Details

Follow best practices in general [voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") (VUIs) design. Standard best practices in [voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") apply to users with cognitive disabilities, and should be followed. These practices are improving as more designs focus on [conversational interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa."). Some examples of generally accepted best practices in [voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") design:

- Pauses are important between phrases in order to allow processing time of language and options.
- Options in text should be given before the digit to select, or the instruction to select that option. This will mean that the user does not need to remember the digit or instruction whilst processing the term. For example: The prompt “press 1 for the secretary,” requires the user to remember the digit 1 while interpreting the term “secretary”. A better prompt is “for the secretary (pause): press 1” or “ for the secretary (pause) or for more help (pause): press 1”.
- Error recovery should be simple, and take the user to a human operator if the error persists. Error responses should not end the call or send the user to a more complex menu.
- Advertisements and other extraneous information should not be read as it can confuse the user and can make it harder to retain attention.
- Terms used should be as simple and jargon-free as possible.
- Use Tapered prompts. Best practices in [voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") design include providing several different prompts for each point in the interaction. The different prompts are used based on the user’s behavior. For example, if the user takes a long time to respond to a prompt, a simpler or more explanatory version of the prompt can be used instead of the default. They should be used to increase the level of prompt detail when the user does not respond as expected.

**User settings**

User-specific settings can be used to customize the [voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") (such as menus, and options). Keep in mind that if it is difficult to set user preferences, they won’t be used. Setting preferences by natural language is the most natural (”slow down!”), but is not currently very common.

- Extra time should be a user setting for both the speed of speech and ability for the user to define if they need a slower speech or more input time etc. Timed text should be adjustable (as with all accessible media).
- The user should be able to extend or disable timeouts as a system default on their device.
- Error recovery should be simple, and take you to a human operator. Error responses should not throw the user off the line or send them to a more complex menu. Preferably they should use a reserved digit for support and human help.
- Advertisement and other information should not be read as it can confuse the user and can make it harder to retain attention.
- Terms used should be as simple as possible.
- Examples and advice should be given on how to build a prompt that reduces the cognitive load
  - Example 1: Reducing cognitive load: The prompt “press 1 for the secretary,” requires the user to remember the digit 1 while interpreting the term secretary. It is less good then the prompt “for the secretary (pause): press 1” or “ for the secretary (pause) or for more help (pause): press 1”.
  - Example 2: Setting a default for a human operator as the number 0.

**Considerations for Speech Recognition**

- For speech recognition based systems, standards for voice commands for many languages exists and should be used where possible, such as the ETSI standard [ETSI 202 076](https://www.etsi.org/deliver/etsi_es/202000_202099/202076/02.01.01_50/es_202076v020101m.pdf). Keep in mind that expecting people to learn more than a few commands places a cognitive burden on the user.
- Natural language understanding systems allow users to state their requests in their own words. This can be useful for users who have difficulty remembering menu options, or who have difficulty mapping the offered menu options to their goals. However, natural language interfaces can be difficult to use for users who have difficulty producing speech or language. Directed dialog (menu-based) fallback or transfer to an agent should be provided. Such fallbacks should be easy to use and conform to this document.

Follow requirements of legislation.

For example, the U.S. Telecommunications Act Section 255 Accessibility Guidelines [[Section255](#bib-section255 "Telecommunications Access for People with Disabilities")] paragraph 1193.41 Input, control, and mechanical functions, clauses (g), (h), and (i) apply to cognitive disabilities and require that equipment should be operable without time-dependent controls, the ability to speak, and should be operable by persons with limited cognitive skills.

See [Voice Menu Systems](https://w3c.github.io/coga/issue-papers/voice-menus.html) issue paper for a full discussion.

##### 4.7.4.5 Getting Started

Ensure this pattern is included in important systems that affect health, finance, communication, water, and government services.

##### 4.7.4.6 Examples

**Use:**

- User interaction dialogs in which the first option takes you directly to a human. For example: “To reach for a person who can help you, press 0 or say help”.
- Error recovery from each point, allowing the user to fix errors easily.
- The user can easily go back or repeat the list at any point.
- A user-interaction dialog, such as the standard “0” from any point, where there is easy access to a human operator who can help users achieve their goals.
- Speech is clear, with pauses.
- Common words are used.
- State the option before giving them the key to press or term to use.
- Advisory technique: Cueing users to record something that may be useful at a later point, and give them time to do so.

**Avoid:**

- Long menu systems that make it hard to find a person.
- Unclear error recovery.
- Complex language and uncommon terms.
- Unnecessary content, such as promotions.
- Fast speech, or expecting fast inputs from the user.
- Systems that were not tested with a wide range of users with different [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

#### 4.7.5 Do Not Rely on Users Calculations or Memorizing Information (Pattern)

##### 4.7.5.1 User Need

> I need navigation and processes that do not rely on memory.

Related User Story: [Previous Steps](#remembering-from-previous-steps-user-story).

##### 4.7.5.2 What to Do

Create a process that does not require:

- remembering digits to select for a short time,
- performing calculations,
- copying,
- clear speech or fast responses,
- memorizing characters, strings, or pin numbers,
- using [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") to work out the category of the service they need,
- recalling information over multiple steps. When going through multiple steps, each step in a process must contain the information needed to allow a user to proceed. They must not rely on memory from prior steps.

Instructions and labels should be located before a call to action or activation mechanism.
When appropriate, provide a summary of information from previous steps, and a mechanism for traversing the process.

##### 4.7.5.3 How it Helps

Often content has barriers which prevent users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") from completing a step or process, and as a result, prevents them from achieving whatever they wished to achieve.

To increase security when making a purchase, sometimes puzzles or calculations are required. For example: To finalize a purchase, a user is asked to enter the result of multiplying positions 1 and 2 of a number. This type of statement cannot be understood by some people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). Both security and cognitive accessibility should be guaranteed.

Many users have an impaired working memory. They cannot remember many details at the same time. However, systems, such as dialog menus, rely on all users using working memory to make choices. They expect the user to remember several choices and to select one choice, whether by speaking or through a key press. The user needs to hold multiple pieces of transitory information in the mind.

Users with an impaired [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") may need more time to complete a task. But there can also be problems if the system response is too slow. For example, some people may need longer to compare similar options such as “billing”, “accounts”, and “sales” and decide which is the service they need. Using clear language will also help.

##### 4.7.5.4 More Details

Good practice that reduces the reliance on memory skills include:

- Each step in a process should contain the information necessary to allow a user to proceed. They must **not** rely on memory from prior steps.
- Providing a simple way to go back without having to start at the beginning.
- Inform users of where they are in the process, for example, through a step indicator.
- If users make a mistake or error, provide help to fix it rather than restarting the process.
- When useful, provide a summary of information from previous steps, and an easy mechanism for traversing the process is available.

For voice interfaces:

- Pause between each option.
- Waiting for a slow speaker to respond.
- Listen for a quiet or hesitant speaker.
- Allow simple, one word responses
- State the option before the number to command to be selected.
- Support forgetfulness and [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:").

Note that this is essential for critical systems such as health, finance, communication, water, and government services.

##### 4.7.5.5 Examples

**Use:**

Processes that do not rely on memory. For example:

- Using user interaction dialogs in which the first option “to wait for a person who can help you press 0 or say help”.
- Using a user-interaction dialog, such as the standard “help” from any point, where there is easy access to a human operator who can help users achieve their goals.
- Good error recovery so that the user knows how to go back from any point.
- Advisory technique: Cue users to write something that may be useful at a later point, and give them time to do so.

**Avoid:**

1. Processes that rely on memory. For example:
   - Requiring the user remember a code or a category from a previous step.
   - Long menu systems that make it hard to find a person.
   - Systems that require use of specific words that the user has to remember.

### 4.8 Objective 7: Provide Help and Support

Support different ways of understanding content. Provide extra help and support such as:

- graphics,
- summaries of long documents,
- icons with headings and links, and
- alternatives for numbers.

Explain choices to help the user successfully complete their tasks.

Make it easy for users get help when they run into difficulties and give feedback. If users have difficulty sending feedback, they cannot tell you if they are unable to use the content. You will not know when they are experiencing problems.

Some applications depend on user data, such as smart cities. Data from users who cannot use the system can be missing from data driven systems. The problem is worse when they cannot even give feedback about their problems. They become invisible and their needs are not met.

#### 4.8.1 Provide Human Help (Pattern)

##### 4.8.1.1 User Need

> I need to know how to get human help and can manage the process easily.

Related User Story: [Help](#help-user-story).

##### 4.8.1.2 What to Do

Many people rely on human help. When possible, there is human help available, and it is easy to use. This includes:

- Easy to find on each page and at each step of a process.
- Easy to use via the mechanism the user prefers.
- Requires as few steps as possible, such as:
  - a form with two fields,
  - an email address, or
  - a phone number that goes directly to a human.

Access to human help should never require the user to manage complex menu systems such as a voice menu with many different options.

Organizations mechanisms should be in place to ensure support staff effectively help people with learning and cognitive disabilities and provide a good experience.

##### 4.8.1.3 How it Helps

When a user gets stuck or confused for any reason, getting help from a human is usually the most effective solution. In reality many sites provide this option only to users who can navigate complex systems.

Examples of complex system include a process where a user needs to follow many links to get to the human contact information. It could also be a phone number requiring the user to answer many questions before connecting with a person. With a complex system, the people who need it most will not have access to the human help option. They may the user may have cognitive overload and stop trying to complete the process. They may also leave with a negative attitude towards the service or supplier.

For example, a user with an intellectual disability wants to use a coupon. They cannot find the instructions for applying the coupon to their online purchase, and they cannot find the phone number for support. They effectively cannot use the coupon.

##### 4.8.1.4 Examples

**Use:**

1. A phone number, ideally with a feature to automatically call via an interoperable [Voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") (VUIs) specification.
2. A number that goes directly to a human or an available standard to get human help for example, using the 0 digit on voice menu systems.
3. An email link using the “mailto” protocol [[mailto](#bib-mailto "The 'mailto' URI Scheme")] with prefilled “to” and “subject” fields. Note that this will not work on all platforms or mail clients.
4. An option for live chat or video call help. Note: It must be fully accessible and easy to close new windows that open as part of live help functionality. Ensure live chats do not distract users from their task.

**Avoid:**

1. Long contact forms the user must fully complete to get human help.
2. Multi-step menus to reach help.
3. Including the contact information on a single page that is only linked to from a few pages on the site.
4. Forcing users to go through multiple steps to get to human help.

#### 4.8.2 Provide Alternative Content for Complex Information and Tasks (Pattern)

##### 4.8.2.1 User Need

> I need contextually-relevant graphs and pictures to supplement text.

Related User Story: [Help](#help-user-story).

##### 4.8.2.2 What to Do

Provide content that helps users understand complex information.

This should include redundant information for different user groups such as:

- summaries of long documents and step-by-step information in [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well."),
- explanation of choices and any disadvantages,
- tables and charts,
- symbols that are familiar to the user,
- well-structured video content,
- pictures and informational graphics, and
- alternatives for numeric content.

Where there is alternative or supplemental content:

- Provide an easy, single action mechanism for the user to be able to find and select the content format or version that is easiest for them to understand.
- Dedicated help and alternative content should be clearly differentiated from primary content.
- Make the relationship between the alternative content and the primary content clear.

##### 4.8.2.3 How it Helps

The use of complex information, long documents, and complex data formats can present significant barriers to users with cognitive accessibility needs. Users should be able to understand the information and successfully complete described tasks without requiring further external assistance as much as possible.

Sometimes the content’s subject matter is complex. In this case, it is likely to need careful explanation, organization, and presentation so as many users as possible are able to understand without any mistakes, confusion, or need of assistance.

The way information is presented, such as a graph, diagram, or table, may make it more complex for some users. Here, a supporting description and guided interpretation will highlight the key features the user needs to understand.

Different people find different types of information easier to understand. This is particularly true for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). For example, some people have an impairment that affects numbers but not language, and other people have a language impairment but may intuitively understand numbers. Help may be provided in various forms, to support different users, for example:

- Text “asides” providing explanation and help for diagrams.
- A supporting chart or graph to illuminate text content.
- Video clips that show the tasks being completed in steps.
- A supplemental table, that is not complex.
- Popup on hover explanations of keywords, possibly linked to a
  glossary.
- A flow chart of steps in a process.

##### 4.8.2.4 More Details

Recommended techniques for content relating to numbers and complex
information (use whichever apply).

- Charts or graphics are provided where they aid the comprehension
  of complex information.
- Tables are provided where they aid the comprehension of
  information.
- Where an understanding of mathematics is not a primary requirement
  for using this content, use one of the following:
  - Reinforce numbers with non-numerical concepts, e.g., Very
    Cold, Cold, Cool, Mild, Warm, Hot, Very Hot.
  - Once it is mature you can also use personalization semantics to add non-numerical concepts. See [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")].
- For content with sections use one of the following:
  - Enable semantics to add symbols to sections.
  - Add icons as an addition to headings, key short sentences
    and phrases to aid understanding.
  - However, as some people have difficulty remembering icons,
    use text with the icons.
    - Use clear icons or symbols that can easily be seen and expanded.
    - Use images understood by different users.
    - In left to right languages place the image to the left of
      the text.
- Recommended techniques for content with more than 300 words
  - Provide an Easy to Understand summary using common terms and short blocks of text. For pieces of content with less than 300 words the heading
    may act as a summary.
  - Semantic headings are used to break the information down into
    a more manageable size and provide structure to the
    information being presented. This particularly benefits users
    of Assistive Technology.
  - The content owner identifies at least two keywords that aid comprehension for the user and these keywords are programmatically determinable and emphasized in the preferred modality of the user.

##### 4.8.2.5 Getting Started

Provide explanatory content for complex information that is
important for successful completion of a task including tasks in the
real world.

##### 4.8.2.6 Examples

**Use:**

1. The techniques in the “more details” section above for long documents, documents with multiple sections, complex information, and numeric information. For example:
   - The explanation of a medical procedure and success rate statistics is amplified through the use of an additional text aside, a diagram, and a graph.
   - The multi-step process for applying for a visa is made easier to use by adding a flow chart of all the steps that are always visible. Each step in the flowchart has links to extra help and the current step is clearly highlighted.

**Avoid:**

1. Long documents without a good structure and summary.
2. Complex information and numeric information without extra support. For example:
   - A long text and data table of sales figures is shown without any explanation of the key features that relate to the content.

#### 4.8.3 Clearly State the Results and Disadvantages of Actions, Options, and Selections (Pattern)

##### 4.8.3.1 User Need

> I need support and explanations for any choices. The advantages or disadvantages are clear to me and I understand the effects of the choice I might make.

Related User Story: [Cognitive Stress](#cognitive-stress-user-story).

##### 4.8.3.2 What to Do

When presenting users with actions and selections, clearly explain the benefits, risks and consequences of each option. This includes any:

- changes from what the user asked for,
- disadvantages from the standard product or offering,
- features that may be a risk to users wellbeing or finances.

##### 4.8.3.3 How it Helps

Clearly stating benefits and consequences of each action and selection option helps individuals avoid mistakes.
This is particularly important when the results cannot be easily corrected, lead to safety risks, or may never be known.

For example, a user of a travel site is booking a trip to Geneva. They see an option at a good time, but this ticket is to a different city. They assume the options given are to the location they asked for. They check the dates and times, but, because they can only read by spelling out words, they do not notice the changed destination. They are taken to a different location than their hotel, and the vulnerable user arrives at night in an unfamiliar city without accommodation.

In another example, a user sees a laptop for sale at a good price. They do not see the refurbished word in the long description. The laptop is not actually a good price.

##### 4.8.3.4 Getting Started

Whenever you ask the user to make a selection or take an action, consider whether there are any implied or hidden results that the user should be aware of. Clearly indicate those results within the user interface and confirm the user is aware of them.

##### 4.8.3.5 Examples

**Use:**

1. Clear lists of what is included and what is not included. For example:
   - When choosing an airline ticket. Next to each option, there is a clear list of what is included.
2. Warnings about any changes or risks. For example:
   - When choosing an airline ticket, if a ticket option is to a different destination or there is another unusual action or change that could be unwanted or have risks, the user is asked to confirm the change.

**Avoid:**

1. Details that are not clear when the user selects an option.
   - For example: Meal options from an online menu have fun names. The meal contents, side items, allergy information and ability to customize each option is not visible until two steps later in the process. A customer must go several screens down on each item in order to make a decision.
2. Changing items from the original request without warning the user.
3. Risks to the user without warnings.

#### 4.8.4 Provide Help for Forms and Non-standard Controls (Pattern)

##### 4.8.4.1 User Need

> I need explanations for unusual controls in a form I find easy to use (such as a video or text).

Related User Story: [Task Management](#task-management-user-story).

##### 4.8.4.2 What to Do

Provide help for any complex forms, particularly when there are
multiple steps, unusual interactions, non-standard controls, and
required fields that do not support autocomplete. Give examples
that make it easy to understand what to do.

##### 4.8.4.3 How it Helps

Users often find forms and related tasks to be the most complex experience with web sites. They can easily become confused, unsure, or even completely lost. Providing extra help can make the difference between being able to successfully complete a task and giving up. This is especially true if any part of the form is complex or requires nonstandard interactions.

Many standard form controls provide support automatically. For example, many fields can be automatically filled in with information using autocomplete or personalization semantics [[personalization-semantics-content-1.0](#bib-personalization-semantics-content-1.0 "Personalization Semantics Content Module 1.0")]. Then the user will not make mistakes filling it out.

When you require additional fields and nonstandard controls many users will have difficulty using them. Many users with disabilities will get the information incorrect or be unable to work out how to complete the task. Often this results in the task being completely abandoned. In other cases, the user asks a caregiver for help to complete the form or work the control. In either case, they have not been able to complete the task because of their disability.

The standard [[HTML](#bib-html "HTML Standard")] forms and controls have been carefully specified for maximum usability and accessibility. They are usually understood by users, especially if they are familiar with web interactions. However, users are likely to experience difficulties if the standard form behavior has been altered or completely new controls are provided. Assuming the new behaviors have been carefully designed and user tested, users may still require help in order to successfully use them.

##### 4.8.4.4 More Details

Examples of forms and controls that are likely to require additional help:

- Password fields that require certain character types of characters to be entered.
- Surveys with complex interactions, for example, where buttons only appear depending on previous answers.
- Date entry where there could be some ambiguity about the required format.
- Custom controls like date pickers where some dates may be grayed out.

##### 4.8.4.5 Examples

**Use:**

1. Standard controls
2. Non-standard controls and form fields with instructions or help. For example:
   - An accessible help button next to a nonstandard control.
   - A standard mechanism for context sensitive help. This can include using personalization semantics for context sensitive help.
   - Clear and unambiguous instructions that are easy to find.

**Avoid:**

1. Non-standard controls and unusual form fields that do not have instructions or help. For example:
   - A form has a complex mechanism for enabling and disabling sections as you scroll or tab between them, but no help is provided.

#### 4.8.5 Make It Easy to Find Help and Give Feedback (Pattern)

##### 4.8.5.1 User Need

> I need to get help and give feedback easily from every place where I get stuck.

Related User Story: [Help](#help-user-story).

##### 4.8.5.2 What to Do

Make it easy for the user to ask for help or report issues at any point in a process. This
includes:

- Easy to Use: Feedback information and forms are simple and clear.
  (User testing with different user groups is highly recommended.)
- Easy to Find: Available from any place where the user may get stuck.
- Using a preferred communication method such as a form, email, chat, or phone support.

The option to provide feedback should never require the user to manage
complex menu systems such as [Interactive Voice Response](#dfn-interactive-voice-response "Interactive voice response (IVR) systems allow the user to interact with a computer system through the use of a telephone keypad and/or audio input. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Interactive voice response systems are often used to automate tasks by phone and in call centers. IVR systems often use standards such as VoiceXML [voicexml21].") (IVR) with many
different options.

##### 4.8.5.3 How it Helps

Providing an easy way for users to give feedback will help people be able to share problems, ask for help, make suggestions, and give positive comments. If users cannot give feedback easily, problems will continue to exist without the site owner being aware of the problems. It is essential to allow users to provide feedback from any point in the process so that people do not get lost when trying to explain why they are stuck. Ideas for improvements and positive feedback will also be missed.

For example, a user with a cognitive and learning disability struggles to use an ecommerce site. They have an idea about how to make it much easier to use. They spend an hour trying to give the feedback and then they stop trying. The site continues to lose customers.

##### 4.8.5.4 More Details

Make sure the feedback option is:

- simple to use,
- available in all stages of the process,
- a process that responds helpfully to any feedback submitted,
- easy to complete and does not make the user provide unnecessary information, and
- not reliant on complex menu systems.

Providing multiple methods for gathering feedback is recommended.
For example, on a web site, consider providing all 4 options for
feedback including live chat, a phone number, a web form, and a
feedback email address.

Note that chat bots may not be appropriate for this particular type
of feedback other than to start the feedback process. These can be
extremely frustrating if you cannot easily get to the area you are
trying to reach.

##### 4.8.5.5 Examples

**Use:**

1. Simple feedback mechanisms that are available on each screen. For example:
   - A banking web site had a major accessibility problem that blocked some customers from paying their bills online. A feedback form was on the page where the customer got stuck. A customer was able to report the problem and a help desk employee reached out to help them complete their bill payment successfully. That help desk employee also reported the accessibility problem to the software team.

2. Multiple feedback mechanisms such as:
   - Web Chat or Web Call - An option to provide feedback using live chat or a video call. Note: The live chat or video call feature must be fully accessible. Web chat should not be a distraction and easy to close. Check usability with user testing.
   - Phone - A feedback phone number, ideally with a feature to automatically call via [Voice user interfaces](#dfn-voice-user-interfaces "Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.") (VUIs) . Make sure there are no complex voice menus.
   - Web Form - A simple site contact form with no more than 3 required fields.
   - Email - An email link using the “mailto [[mailto](#bib-mailto "The 'mailto' URI Scheme")]” protocol with prefilled “to” and “subject” fields. Note that this will not work on all platforms or all mail clients.
   - [Interactive Voice Response](#dfn-interactive-voice-response "Interactive voice response (IVR) systems allow the user to interact with a computer system through the use of a telephone keypad and/or audio input. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Interactive voice response systems are often used to automate tasks by phone and in call centers. IVR systems often use standards such as VoiceXML [voicexml21].") (IVR) - Provide an automatic option at the end of an IVR to give feedback by pressing a specific digit on the phone.

**Avoid:**

1. Complex feedback mechanisms.
2. A single way to give feedback that not everyone can use.

#### 4.8.6 Provide Help with Directions (Pattern)

##### 4.8.6.1 User Need

> I need help understanding and using directions and navigation.

Related User Story: [Help](#help-user-story).

##### 4.8.6.2 What to Do

Content is provided that helps users understand and use directions or
navigational systems. This can include:

- Providing landmarks that are easily recognized.
- Providing cardinal directions (general or global) that can be related to a static object such as north of the tower.
- Helping people avoid changes that confuse them, such as a change of orientation or routing.
- Facilitating reorientation when leaving the route.
- Supporting different ways people are aware of distances.
- Allowing personalization of terms such as directions and measurements.

##### 4.8.6.3 How it Helps

People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") experience different levels of difficulty with wayfinding directions or wayfinding applications. The help needed to address wayfinding issues can be different for indoor navigation, where there are more stimuli, and outdoors, where there can be more demands on memory. The help needed also varies with the individual.

Wayfinding requires many cognitive functions. Designs should accommodate a wide range of cognitive and learning disabilities including those supported by other design patterns. For example:

- memory,
- [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."),
- spatial orientation,
- visual/spatial attention, perception, and processing,
- spatial disorientation anxiety,
- language processing,
- intellectual,
- attention.

Some users may need more detailed help, such as step-by-step directions. Many users need to preview a route before following it. Then landmarks can help with recognition and orientation as well as reducing anxiety. Alternative relative directional terms and cardinal directions matching a user’s preferences are most effective. For example, the application could refer to “the driver’s side” or “the East Wing”. Helping people imagine relative and absolute distances can help, for example, “you’ve travelled half way”.

Due to the wide variation in personal requirements, personalization mechanisms can be very useful. For example, the units used for distances.
Platforms or other technologies often provide personalization options for relative and cardinal directions and terms which can be used. For
example, the platform locale settings.

Changes can be very confusing. A user may be prepared to change the route to save hours of traffic, but this will involve them pulling into a gas station to learn the new route. They may not want to change routes to avoid a small amount of traffic. Help the user to find the option that works for them.

For example, a person with traumatic [brain injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments.") is using a Global Positioning System (GPS). They review the route before leaving, and look at pictures of the turns. These preparations will enable them to follow the route. While driving, the route changes to avoid three minutes of traffic. They are no longer able to follow it and become lost.

##### 4.8.6.4 Examples

**Use:**

1. A second way to indicate left and right that is always available or a way to personalize the indication.
2. Directions that use landmarks. For example, images of local landmarks are provided or can be added to help with orientation during wayfinding.
3. Options that are available to avoid unwanted changes.
4. Extra support that is available.

**Avoid:**

1. Consistent reference to points of the compass including less well known ones (e.g. N by NE).
2. Instructions that always assume that the person is at the expected location. They do not have an easy way to recover.
3. Content that changes automatically in ways that the user does not want or control.

#### 4.8.7 Provide Reminders (Pattern)

##### 4.8.7.1 User Need

> I need reminders integrated into my calendar, otherwise I will forget appointments and when I am meant to do things. Sometimes I need reminders to revisit a web site to complete the next task.

Related User Story: [Support](#support-user-story).

##### 4.8.7.2 What to Do

Make it easy for the user to set a reminder for date and time sensitive events. Use standard application programming interfaces (APIs) when possible.

Reminders must be set only at the user’s request and the user must be able to personalize the remainder method.

##### 4.8.7.3 How it Helps

People with cognitive and learning disabilities often have challenges managing events and time. (In fact, being unable to correctly manage events and time without support is a diagnostic criterion for some groups of disabilities.) This results in missing meetings, not submitting a request by a certain date or a form within a specified time period and missed opportunities. For example:

- When the user copies information into a calendar they often copy
  the day or time incorrectly.
- The user is challenged processing and retaining time based
  information.
- The user may find it hard to sequence time-bound events.
- The user’s skills decrease when tired to such an extent that they have to stop a task. They may wish to reschedule the task.

Using calendar
APIs (or task manager) that allow the user to
automatically add events and deadlines to their own calendar can
help.

For example, a user with a cognitive and learning disability sets a doctor’s appointment online. Often they copy the details incorrectly into their calendar. However, in this case, the web site gives them an option to add the appointment to the calendar and sets a reminder an hour before. The user now comes to the correct place at the correct time with the correct papers.

The benefit to users with cognitive accessibility needs is that they
can independently manage appointments, deadlines, and schedules. The
ability to set reminders can reduce the cognitive load associated
when processing time bound tasks. Time dependent activities may be
monitored and tracked by the user to ensure that they are completed
in a timely manner.

Always give the option to set a reminder at the end of the task so
that the user does not get interrupted.

It is essential not to add unwanted reminders, as this makes the user’s calendar too full. This can even prevent them from being able to use their calendar at all. The user is the best person to know how many reminders, and which type, will best meet their needs.

##### 4.8.7.4 More Details

Where a standard mechanism exists for the platform or technologies,
it must be used. See:

- [Web Notification API](https://developer.mozilla.org/en/docs/Web/API/notification)
- [Using the Notifications API](https://www.html5rocks.com/en/tutorials/notifications/quick/)
- [Reminders and Notifications](https://developers.google.com/google-apps/calendar/concepts/reminders)

Date and time sensitive events are any event that has to be
completed by a certain time. The time constraints on such an event
may be defined by a calendar date and time or by the total elapsed
time.

Variables that could be considered include:

- Time - at a logical time.
- Location - prompted when at an appropriate location.
- Context - on computer vs. mobile, on specific a site, etc.

##### 4.8.7.5 Examples

**Use:**

1. Options for the user to add the event to their calendar and set a reminder. For example:
   - A health care site allows you to set a local medical appointment. Once the appointment is set the user is given the option to add it to their calendar (automatically) with a reminder three hours before. They are also given the option to add or edit the reminder.

**Avoid:**

1. Events that are added to the user’s calendar that the user does not want to attend.
2. The user cannot automatically add the events and appointments they just set to their calendar. For example:
   - A health care site allows you to set a local medical appointment. The user is not given the option to automatically add it to their calendar or set a reminder.

### 4.9 Objective 8: Support Adaptation and Personalization

Many users need products that support adaptation and personalization. Users should be able to use add-ons and extensions as assistive technology. This includes spell checkers, passwords support, support for text-to-speech, and synchronized highlighting of the phrase being read.

Personalization can allow the user to select preferred, familiar options from a set of alternatives.

Support personalization and simplification when you can. Do not disable add-ons and extensions.

#### 4.9.1 Let Users Control When the Content Moves or Changes (Pattern)

##### 4.9.1.1 User Need

> I need to know where things are. Controls and content do not move unexpectedly as I am using them.

Related User Story: [Adapt](#adapt-user-story).

##### 4.9.1.2 What to Do

Ensure that changes of context, functionality, settings, route, and
orientation are initiated only by user request or an easily available
mechanism is available to turn off such changes. Also provide an easily available
mechanism to go to previous context, functionality,
settings, route, and orientation.

##### 4.9.1.3 How it Helps

Any content, settings, or functionality which changes unexpectedly, without user initiation can result in significant problems for users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). Unexpected changes in any of these areas can result in loss of focus, anxiety, or confusion in understanding or using a user interface (such as menus, buttons, and design components). Examples include, but are not limited to:

- The automatic launching of new windows or pop-ups.
- Submission of forms through mechanisms other than a button that is clearly labeled (using simple language to submit the form).
- The opening of new content or a feature.
- Unexpected changes when selecting an option.
- Rerouting automatically by a Global Positioning System (GPS).
- Changing the direction of a map in a GPS.

For example, a user may not have a sense of direction or know their
left and right. Before using a GPS, they may study the route so that
they know approximately what they are doing and can augment the
directions of the GPS with their own context, using the GPS for
cues. The GPS automatically reroutes them because of a small traffic
delay. They become completely lost and disoriented and can no
longer use the application.

In another example, a user is watching a video and wants to press “like”. As they are about to press the button, the controls shift and they load a different video instead of pressing “like”. They are now less likely to press “like” because they do not want to lose their content. As a result, their preferences are not taken into account.

Letting users control when content changes gives users with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") more control over how web sites and applications behave. This gives them the opportunity to make choices that enable them to use the content and complete the task.

##### 4.9.1.4 More Details

Exception: The changes are part of an activity where it is essential
(e.g. a game).

Route: This is the directions and flow such as a GPS route.

Orientation: perspective or view such as map direction.

Easily available (or easily available mode or setting), is when one or more of the following is true:

- It can be set one time with as a wide a scope as possible (such as
  using the standards of the Operating System (OS), From [[ISO 9241-112](#bib-iso-9241-112 "Ergonomics of human-system interaction — Part 112: Principles for the presentation of information")] or [[GPII](#bib-gpii "The Global Public Inclusive Infrastructure")] when
  available).
- It has the option to save or to change the setting for the scope of the set of web pages.
- It is reachable from each screen where it may be needed, and the path
  and the control conforms to all of this document.

##### 4.9.1.5 Examples

**Use:**

1. User control when content changes. For example:
   - The user can set to change the route if more than a specific amount of time is saved. They can add more information such as how many extra turns are acceptable for saving 5 minutes. When the GPS finds a new route that saves time, the GPS tells the user about the change including how many extra turns were added and how much time will be saved. The GPS asks the user if they want to change the route or if the GPS changed it, the user can go back to the original route in one touch or command.

**Avoid:**

1. Content that changes without the user having control.

#### 4.9.2 Enable APIs and Extensions (Pattern)

##### 4.9.2.1 User Need

> I need to use additional support features from widgets or extensions.

Related User Story: [Extensions and
APIs](#extensions-and-apis-user-story).

##### 4.9.2.2 What to Do

APIs and extensions work with your content.

##### 4.9.2.3 How it Helps

People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") are often using add-ons or extensions as assistive technology. For example:

- reading of the long form of acronyms,
- support for text-to-speech with synchronized highlighting of the
  phrase being read,
- content simplification,
- creating mind maps out of the heading structure,
- support for retaining content that has already been entered,
- password management,
- spell checking,
- changing the symbols or the interface,
- changing numbers from digits to words and words to digits,
- adding white space between lines, sentences, phrases, and chunks,
- alternative ways to input the content such as speech recognition,
- adding pictures.

However, sometimes a web site stops extensions and
APIs from working. The result is that these users cannot use this web site.

If these add-ons and
APIs are not supported, the author should provide support for all the functions of the add-ons used as assistive technology.

For example, a user with traumatic [brain injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments.") has executive
function and [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:") impacting their ability to remember
details such as:

- the icons or symbols on a Web of Things (WoT) interface,
- their username and password,
- what an acronym stands for,
- a phone number, or
- the meaning of uncommon words.

Supporting the use of an add-on that simplifies content and gives support (such as the long form of acronyms, and a popup dictionary) enables them to understand most content.

Supporting password management tools enables users to successfully login and avoid being locked out of secure sites.

Storing non-sensitive information and auto complete helps them fill out a form. This suggests common information, like a person’s phone number or address. It also helps them avoid making mistakes. It eliminates the need for accurately recalling this information from memory or having to copy and paste it, which is a task that often prevents them from successfully using a form.

When overwhelmed by textual content, they have an extension that
inserts symbols that they are familiar with that helps them find the
content they need.

Too many options may add to the complexity of interacting with IoT devices. Additional options should be easy to ignore and not require a lot of reading to understand that they are additional, as well as how to skip them.

Sometimes the Internet of Things (IoT) interfaces may confuse the user, such as a default “reading” on a meter being set to “2” and not “1.” The user would then need to reset it to “1.”

It is important in any proposed solution to make operational tasks, such as interacting with the IoT, as transparent as possible so that users can focus their attention on the functional aspects, such as relating to content.

##### 4.9.2.4 More Details

People with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") often use add-ons as assistive technology. It is essential that add-ons and similar tools work as expected, except when:

1. A security or safety requirement requires that these
   APIs need to be disabled. In this case they should be disabled only for the relevant field(s).
2. The add-on breaks the main function of the site, such as evaluation and testing applications.

When add-ons are automatically disabled by the code, the burden of supporting the extra functionality of the add-ons falls to the author.

##### 4.9.2.5 Getting Started

Content can be used with
APIs and extensions that support those with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

Testing verified through the use of some of the
APIs appropriate for
the content. For example:

- Testing with spell checker and password storage apps or
  extensions.
- Test with an extension that adds to menu items (the right click options for desktops).
- Test with a toolbar that enables simplification or personalization and is designed for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

##### 4.9.2.6 Examples

**Use:**

1. Support for browser extensions and features, and personalization tool bars. Users are able to apply their settings from a personalization toolbar to improve the usability for them of the page.
2. Extension that adds options to the right click work as expected.
3. The page can be formatted and simplified from the user’s preferences in the operating system or user agent.

**Avoid:**

1. Designs and code that stop browser extensions, settings and features, and personalization tool bars from working. For example:
   - Password storage applications do not work.
   - Distraction removing extensions do not work.
   - Spell checker extensions do not add options to the right click menu, or do not underline mistakes made by the user.
   - The correct symbols cannot be added by a simplification toolbar.
   - The page cannot be formatted or extra white space added.
   - The user cannot use their preferred font.

#### 4.9.3 Support Simplification (Pattern)

##### 4.9.3.1 User Need

> I need less content without extra options and features as I cannot function at all when there is too much cognitive overload.

Related User Story: [Adapt](#adapt-user-story).

##### 4.9.3.2 What to Do

Support simplification of your content. Often this includes allowing the user to:

- Remove or hide features that most users do not
  use or that are not essential.
- Get less text or more simple text.
- Select the content format or version that is easiest for them to understand, or
- Find the extra features when wanted.

##### 4.9.3.3 How it Helps

A user who has difficulty reading or using web content can be easily overwhelmed with too much information on a web page. They need to simplify the page to include the critical information that they need and not spend all their energy reading and understanding other content and features. This is also true for users who are easily distracted.

For example, an email program has lots of features and formatting options when drafting an email. This makes it too complex for a lot of people. With personalization the user can have a simple option with only send and cancel options. There is a “to” and subject line but no cc or bcc options. In this setting there is a clear heading (write an email) and they have icons that the user understands.

##### 4.9.3.4 More Details

Note that:

- Typically, a simple application has 3 to 6 functions.
- Make sure it is easy to get back to the full featured version.
- You can meet this design pattern by:
  - supporting simplified versions from the browser,
  - using of data-simplification on regions and controls,
  - using other attributes in personalization semantics (see [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")]),
  - adding a simplification toolbar, or
  - providing an alternative version.

##### 4.9.3.5 Getting Started

Add `data-simplification="critical"` on content that is in any critical
user testing paths.

##### 4.9.3.6 Examples

**Use:**

1. A simplified “reading” view that is available and easy to close.
2. Applications that have 3 large features. Other features are in the footer or under a “more” option.
3. A simplified version of the application is available.

**Avoid:**

1. Simplified modes have unnecessary extra content or are not supported.
2. Applications with lots of features and cannot be simplified. For example:
   - A busy email program has many control bars and features such as tagging, group tagging, start a new thread, etc. There is no easy way to simplify the page.

#### 4.9.4 Support a Personalized and Familiar Interface (Pattern)

##### 4.9.4.1 User Need

> I need (a version of) a familiar interface, that I recognize and know what will happen.

Related User Story: [Adapt](#adapt-user-story).

##### 4.9.4.2 What to Do

Provide users with a way to personalize their interface to make it familiar.

This can be done by:

1. Allowing user preferences on presentation such as font style, font size, line heights, margins, and contrast. (Note: The default version should still be readable and use clear fonts.)
2. Allowing a rollback to a previous interface that the user is familiar with and knows how to use.
3. Adding semantics on controls, links, and symbols that allow the user to control the experience. For example:
   - HTML5 autocomplete on common fields,
   - adding a toolbar that adds personalized images,
   - use attributes in [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")].

Ensure the user knows the personalization options and can easily configure them. Clear instructions can help.

##### 4.9.4.3 How it Helps

Personalization changes the interface to meet the needs of the user.

Having familiar terms and symbols is key to many users being able to use the web. However, what is familiar for one user may be unfamiliar to another requiring them to learn new symbols. Adding semantics allows symbols and support to be added by an extension or browser that is familiar to the individual user.

A stronger example is people using [AAC](#dfn-alternative-and-augmentative-communication-system "Any method, device, or application that can be used to help those who cannot use spoken language and need additional support by means of symbols, images, and/or text. For example, a screen with symbols that the user can select to speak the appropriate words or add them to a document."). These users usually only learn one symbol set. They cannot easily communicate with other people using [AAC](#dfn-alternative-and-augmentative-communication-system "Any method, device, or application that can be used to help those who cannot use spoken language and need additional support by means of symbols, images, and/or text. For example, a screen with symbols that the user can select to speak the appropriate words or add them to a document.") in a written format or may struggle to understand different symbols used in different applications. When using personalization, such as [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")] the user agents can load the symbols that are understandable by the individual user. The user can also access the Web and other applications.

Other support includes autocomplete and extensions that help the user fill out forms and understand the content. Many users with memory or [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.") impairments cannot fill in forms without asking someone to help copy over information or check their work. Autocomplete allows many more users to manage forms by themselves.

##### 4.9.4.4 Getting Started

- Use the HTML autocomplete tags on all common fields.
- Add a toolbar that adds personalized images.
- Add the semantics that can work with a toolbar for personalized
  images.

##### 4.9.4.5 Examples

**Use:**

1. [[HTML5](#bib-html5 "HTML5")] autocomplete tags on all common fields.
2. True text to support browser preferences for styles.
3. A toolbar that adds personalized images.
4. Semantics that can work with a toolbar for personalized images or [[personalization-semantics-1.0](#bib-personalization-semantics-1.0 "Personalization Semantics 1.0")].

**Avoid:**

1. Forms that do not support [[HTML5](#bib-html5 "HTML5")] autocomplete.
2. Default fonts that are not clear or readable such as a cartoon font or gothic.
3. Pages that cannot easily be personalized.

## 5. Usability Testing, Focus Groups, and Feedback

### 5.1 Working with Users with Cognitive and Learning Disabilities

This section aims to help people work with users with cognitive and learning disabilities. It focuses on:

- special considerations and support for professionals working with this group, and
- a brief introduction support for people who are new to usability testing (as any amount of user involvement can substantially improve accessibility).

Usability testing professionals should pay extra attention to ethical considerations, as this audience is potentially more vulnerable.

Note

It is beyond the scope of this document to provide a guide to usability testing and user-research. Note that you can find additional information about including users with disabilities at [Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/) and other useful resources on our [developer resource page](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources).

Usability testing is the best way to know if your content and design works for real people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:").

Usability is important for everyone. However, if someone cannot use the content or design without help because of their disability, then the content is not accessible for them. It is important to change the design so that users with cognitive and learning disabilities can use the content independently.

Including digital accessibility throughout a project, right from the beginning, improves accessibility for all users. Include people with cognitive and learning disabilities in focus groups, user needs, design patterns (repeated designs for controls and other elements) and usability testing.

Automated testing for accessibility focuses on more technical areas of accessibility. While important, automated testing often cannot assess if people with a cognitive or learning disability can use the content. It is vital for people with cognitive and learning disabilities that development teams do not rely solely on automated accessibility testing. Development teams should

- Perform usability tests with people who have cognitive and learning disabilities. Usability testing of wireframes, conceptual drawings of the interface, or template pages can be helpful to identify challenges early in the project. You probably know people with [age related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)"), or a cognitive and learning disability. Asking them to help find out if your design is usable is a good first step.
- Include people with cognitive and learning disabilities in their teams and the design and development process. This also includes research that has something to do with them. They are the experts in what works for them.

Sometimes designs and content are usable for some people, but not if they have cognitive or learning impairments. Sometimes content is usable by people with one cognitive and learning disability but not a different one. For example, content with fewer words and more numbers may be perfect for some [autistic](#dfn-autistic "Sometimes called “autism spectrum disorder”, “ASD”, “autism”, “asperger syndrome”, and “pervasive developmental disorder”.") and dyslexic users. However, the same content is inaccessible for people with dyscalculia who struggle with numeric information. It is important that usability testing includes a diverse set of users with different cognitive and learning disabilities, such as: people with a memory impairment, learning difficulty, attention impairment, numeric impairment, language and communication disability, and intellectual disability.

### 5.2 Finding People to Include

Finding people to include in usability testing who have different [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") is strongly encouraged and can be achievable, even for small groups on a low budget. If your organization already involves users, this section aims to expand that activity to include people with cognitive and learning disabilities. For developers without formal user involvement, even a small amount of user input and testing can make a large difference to usability and accessibility. Further links about user testing and usability can be on our [developer resource page](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources).

People sometimes recruit users from an organization or self-help group for people with learning difficulties. Social media groups can be a convenient resource. Small development groups can achieve a large improvement by asking people who they know, such as friends, colleagues, relatives or neighbors. Try to build a group of users who:

- are older and struggle to use computers, or have [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)"),
- may be at an early stage of dementia,
- have a specific learning disability such as those with dyslexia, dyscalculia, or [AD(H)D](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development."),
- have an intellectual disability, or
- have acquired cognitive issues (for example, due to neurological trauma).

People with acquired cognitive issues have the same challenges as people with other disabilities such as:

- having difficulty (asking a family member to help) with booking travel booking or hotel booking online,
- being unable to use online banking,
- coping with content forms and pop-up windows when errors occur.

It is helpful to find people with learning and cognitive difficulties who are also in your target group as customers or users.

If your organization has a more formal process, work with those that help employees or community members get assistive technology or other accommodations. They can put out a call for volunteers to their contacts. This helps individuals self-identify and opt-in to help.

Some organizations also use peer-researchers who have cognitive and learning disabilities. Peer-researchers understand the perspective of people with their disabilities. The researchers and developers work together with peer researchers to find solutions. Peer researchers are also involved in testing the solution with other people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). [Our developer resource page](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources#Easy_Reading_-_see:_easyreading.eu) references projects and resources with information on finding and working with persons with learning and cognitive difficulties as co-researchers or peer researchers.

### 5.3 Informed Consent

It is important to get a declaration of consent from all participants involved in testing and focus groups before they start. Before they sign up, participants must know and understand the details such as:

- What the project is for.
- What they will be doing and why it is helping you.
- Any risks that need to be explained and understood.
- What personal details are collected and how any personal data may be used. (Note that their comments should be anonymized before being used in any report.)
- They do not have to participate. Participation is always voluntary and they can always stop at any time.

If your tester has a guardian, you should get informed consent from **both** the tester and their guardian.

Using an understandable consent form is important. Our design patterns on clear content will help you use clear language and layout. Adding icons and symbols can also help.

Make sure users understand the consent form. This can be done by asking them some questions about the consent that tests that they understand the key points. You can also adapt the example consent forms from [our developer resource page](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources).

Throughout the process, remind them that participation is always voluntary and they can stop at any time. This is particularly important if they have [memory impairments](#dfn-memory-impairment "Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:") and may have forgotten that it is their choice to participate. Remember to thank them for their ideas and contribution.

Different areas may require consent for more items than others. Check the legal requirements in your jurisdiction and for your type of content.

### 5.4 Usability Testing

One approach to usability is to measure user efficacy, efficiency, and satisfaction for key tasks. This can be done by measuring or tracking:

- successes in completing tasks while noting any errors to measure efficacy,
- time taken per task to measure efficiency. Note that the relative time between tasks is often more useful than absolute numbers, and
- user’s mood and comments to measure satisfaction.

At the end of the evaluation you should be able to answer:

- What prevents the user from completing a task?
- What creates confusion? When and why do they misinterpret the interface?
- What produces an error and an incorrect action?
- When does the user get frustrated or upset?
- When does the user misunderstand navigation, menus, and controls?
- How can these problems be avoided?

#### 5.4.1 Differences from Usability Testing with the General Population

There are some differences when usability testing with people who have cognitive and learning disabilities:

- Ask ahead of time if they need any support for their needs. This could include a quiet room or frequent breaks.
- Ask what test methods work best for them, such as individual interviews or groups. Some people will prefer to have an interview in their home.
- Ensure participation forms are easy to understand. Confirm that they understand any key points.
- Inform the participant that they can request the information in a different format. If they make a request, ensure they receive it with enough time for them to review and ask questions.
- Have a copy of the participation forms at the session, in case questions come up before the session begins.
- Send participation forms to the participant in advance. Allow plenty of time for the participant to ask questions and fill in forms.
- Allow the participant to bring a caregiver, family member, or friend to attend with them.
- If your tester has a guardian, you should get consent from both the participant and their guardian.
- If they bring a guardian or caregiver, make sure they are not doing the tasks for them. If they give help, monitor closely what help they give, as this may be due to a design fault.
- Explain the testing method before the test.
- The questions should be short and easy to understand language.
- Provide easy methods of assessing mood, rather than just asking for the participant. Try asking them to select a smiley face, such as: *Figure 1 A simple mood selector*.  
    

  ![a set of 5 smiley faces from happy, through neutral, to sad.](img/faces-happy-to-sad.png)

  Figure 1 A simple mood selector
- Some individuals also have challenges identifying moods from faces. Other options to consider are simple mood selectors and text-based rating scales where an individual can point to their selection. For example, I really like this, it is fine, I really don’t like this.
- Check they understand the methods used to collect the data.
- Ensure the person does not feel like they are at fault for making mistakes. While this is always important during usability testing, this scenario is even more likely for people with cognitive and learning disabilities.
- Ask them for their ideas, such as, what features they would like to see, what design they prefer and what support they find most helpful. Thank them for their contribution.
- Make clear that the tester can end the user testing session at any time.

Here are some suggestions of what to look for when conducting usability testing with people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"):

1. Before you start, make sure the research team understands that the testers cannot do anything wrong. Research should never harm the user or make them feel bad.
2. Make sure the participants and researchers know they can leave at any time. No one should feel bad if they leave!
3. Check that the testers understand the task or question. Encourage your testers to “think out loud”.
4. Time the task takes to complete, and note any parts where users slow down or seem to struggle. Can your testers manage each task reasonably easily and quickly? Also, note any errors that they make, including clicking on the wrong item.
5. Find out if completing the task is frustrating or upsetting.
   1. You can ask users how they are feeling before and after the tasks or rate their mood such as selecting the smiley face which represents how they feel.
   2. Ask them if anything was annoying.
6. Ask how you can make it better for your users (people with cognitive and learning disabilities)?
7. Ask your users if they have suggestions about what would make the interface easier for them to use. This is often best at the end of the usability test.
8. If the user is struggling, remind them that you are reviewing the system not them and that their insights are really helpful. Thank them for helping. Remind them that it is helpful when they find issues because it helps the team make the product better. Stop the process if users are getting distressed.
9. Analyze the data collected and review the findings with the team. Remember to keep the names of individuals confidential (unless they have given permission for their identity and disability to be shared).

### 5.5 Test Objectives

You can test the objectives of the design guide. If they are successful, that section can be considered completed!

For each objective, make sure your user testing includes individuals with a range of cognitive and learning disabilities. Do not just ask questions, but ask the user to complete an action that demonstrates usability. Test for the following but set up the tests so that the user demonstrates their knowledge and understanding rather than answers a simple question:
Are enough user groups represented?

For example, a typical project may wish to include: People living with [early stage dementia](#dfn-early-stage-dementia), [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)"), intellectual disabilities, different specific cognitive and learning disabilities and communication disabilities.

#### 5.5.1 Does the User Understand What Things Are and How to Use Them?

- Does the user know what the page is about?
- Does the user know what actions they can take on a page?
- Does the user know where they are in a web site, an application or a
  multi-step process?
- Can the user easily find the different sections of content?
- Identify the different activities that the user may want to complete
  on the page:
  - Can the user achieve the activities without asking for help?
  - Does the user make errors trying to achieve the activities?
  - Does the user find them easy to achieve?

Related Design Objective: [Objective 1: Help Users Understand What Things are and How to Use Them](#objective-1-help-users-understand-what-things-are-and-how-to-use-them-0) .

#### 5.5.2 Can Users Find What They Need?

- Can the user easily identify all the important information and important interactive features on the site and each page?
- Can the user use both browse and search to find things? (Check for important and commonly used information or features.)
- Can the user revert or correct any action they take when interacting? Does it use a familiar and consistent action?

Related Design Objective: [Objective 2: Help Users Find What They Need](#objective-2-help-users-find-what-they-need-0).

#### 5.5.3 Is the Content Clear and Understandable?

- Can the user find a segment or a piece of key information quickly?
- Does the user understand the text?
- Does the user understand text immediately?
- Does the user know ambiguous language?
- Is the content usable without understanding math concepts?
- Is there any representation of math by words instead of numbers?
- Is the support for slow readers helpful?
- Does the user understand the use of (familiar) symbols?
- Does the user understand the use of images and multimedia?

Related Design Objective: [Objective 3: Use Clear and Understandable Content](#objective-3-use-clear-and-understandable-content-0).

#### 5.5.4 Can Users Avoid Mistakes and Easily Correct Them

- Can the user easily fill in the form without making mistakes?
- When the user goes to the wrong place can they easily get back in one click? (You can press something on the screen and ask them to go back.)
- Was it pleasant to fill out the form? Has the user’s mood changed?
- Did the user have to redo anything? Was correcting any mistakes easy?
- Ask the user if they would find this easy to do if under stress or tired.
- Ask the user if anything was hard.
- After they complete the form, ask the user to change a detail at the beginning. Did they manage without losing data? Was it hard or stressful?
- Ask the user how the form could be easier to fill out. Suggest some of the relevant design techniques from the design patterns section and ask if it would help them with this form.

Related Design Objective: [Objective 4: Help Users Avoid Mistakes and Know How to Correct Them](#objective-4-help-users-avoid-mistakes-and-know-how-to-correct-them-0).

#### 5.5.5 Can Users Maintain Focus?

- Can they achieve the activities easily without losing focus?
- Distract the user for a minute so that they lose focus. Can they get
  easily back to the task?
- Ask users if they would find this easy to do if under stress or
  tired?
- Ask the user what would help them remember what they are doing such
  as headers or breadcrumbs.
- Ask the user if anything was distracting.

Related Design Objective: [Objective 5: Help Users Focus](#objective-5-help-users-focus-0).

#### 5.5.6 Can Users Complete Processes without Relying on Memory?

Identify the different activities that the user may want to complete on the page:

- Can they achieve the activities without asking for help?
- Does the user make errors trying to achieve the activities?
- Does the user find the activities easy to achieve?
- Can the user do the same thing later (the password may have been
  forgotten)?
- Ask users if they would find this easy to do if under stress or
  tired.
- Ask users where they might have trouble if they are under stress.

Related Design Objective: [Objective 6: Ensure Processes Do Not Rely on Memory](#objective-6-ensure-processes-do-not-rely-on-memory-0).

#### 5.5.7 Is there Enough Help and Support?

- Can the user identify the different ways a user may “Report Issues and Problems”?
- Can the user find a way to submit their feedback without asking for help?
- Can the user submit feedback at each stage of the process? This should include the home page and any place they may get stuck.
- At each stage in the task, confirm that the feedback process is one click away (or less).
- Does the user make errors trying to submit their feedback?
- Does the user’s mood deteriorate when submitting feedback? (A sign of frustration.)
- Does the user find it easy to submit their feedback?
- Ask users if they would find this easy to do, when they are stressed or tired.
- Ask the user where they might have trouble giving feedback if they were under stress.
- Is the user able to complete the task after they give feedback?
- Does the user understand the feedback process? Use concrete ways to check that the user understands. For example: Is the user able to identify if/when they will receive a response back? Can they identify how a response may come back (e.g., email, phone)? Where the feedback goes/what happens to the feedback?
- Confirm that the feedback process does not require a lot of information that will prevent people from giving feedback.
- Confirm that when feedback is given, a process is in place for acting on it!

Related Design Objective: [Objective 7: Provide Help and Support](#objective-7-provide-help-and-support-0).

#### 5.5.8 Is Adaptation and Personalization Supported

- Are personalized versions of the content supplied?
- Do content modifications match the user preferences such as: less content, adding and changing icons and symbols, or simplified text?
- Check that content variations such as text simplification have kept:
  - the same meaning as the original,
  - content that the user wants, and
  - critical paths that still work.
- Check that autofill works correctly with all content versions.
- Do the user’s preferred extensions and tools work on the site?
- Are the personalization options easy to find and set?
- Do they find it easier with personalization options supplied?

Related Design Objective: [Objective 8: Support Adaptation and Personalization](#objective-8-support-adaptation-and-personalization-0).

## 6. Use Cases / Personas

Any time there is a “target audience”, there will be people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") in that audience. However, cognitive and learning disabilities are often invisible in day-to-day life. The personas below describe fictional people with cognitive and learning disabilities. They provide some context and understanding of the challenges they face.

For additional examples from other organizations, see [Persona Links](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources#Persona_Links) on the developer resources page.

### 6.1 Alison: An Aging User with Mild Cognitive Impairment

- Problem:" I’m not sure what I should press. I pressed something that looked like the “buy” button but it did nothing. I am not sure if it is me or if this web site just doesn’t work."
- Works well:" The “buy” button was clearly something I could click. The process was easy. I have now bought matching dresses for all the grandchildren."

Alison has a medical background, working in rehabilitation of physical injuries. She recently decided to work part-time to take up more hobbies and be with her grandchildren. She wants to try an online course to learn Chinese, in preparation for a special holiday. Alison considers 63 to be the new 36. However, she has difficulty concentrating and finding the word she wants to say. She often makes typos and has to correct sentences when she re-reads them. She becomes easily frustrated as she finds new technical things, like updated design patterns and applications, hard to learn and less intuitive than they used to be. Plus, navigation takes longer than in the past. Unfortunately, this includes learning how to use a new interface and this affects the way she works when swapping between her tablet, phone, and computer.

#### 6.1.1 Alison Scenario 1: Learning How to Use New Technologies and Interfaces

Alison took an evening course to learn how to use Windows and MS Word ten years ago and used to feel very comfortable with the interface. She has a new computer now and finds that most applications look very different. She realizes that links and buttons have changed appearance and does not know what to press. Sometimes she presses a picture or stylized heading that is not a control and is not sure if the internet is down, the site is broken or she has made a mistake. Sometimes she touches something accidentally and the focus moves to a different page or application. For example, she recently tried to enlarge some small text and activated a link instead of enlarging it! She misses the days when all links were in blue and underlined.

Alison loses self-confidence when things go wrong. For example, selecting an incorrect button or getting an error that she does not understand. She knows to try and press the back button to go back a step, but it does not always work as she thinks it will. She tends to think she cannot cope, so gives up, but with support to adapt the interface to suit her needs she can learn to use the new style.

Her children worked with her to reduce the number of menu items on the application toolbar so she can concentrate on the ones she regularly uses. They helped her change her settings so when searching for items on the Web, only a limited number appear at one time. They also found her a de-cluttering browser extension that takes away many of the advertisements and other items that clutter her social media pages when communicating with her grandchildren.

#### 6.1.2 Alison Scenario 2: Correcting Typos and Writing Fluently

When writing letters and messages on her computer, phone, and tablet, Alison pauses every so often and checks that what she is writing makes sense. She finds it very annoying having to work so slowly. However, by using text-to-speech to read out content she has found she can hear her mistakes more easily than noticing them on the screen. She has also discovered that this process can make reading web pages easier and less tiring. Nevertheless, she often has to go over instructions several times before completing tasks online. She depends on forms that do not timeout or have an option to allow her to extend the time to fill in the edit boxes.

#### 6.1.3 Alison Scenario 3: Coping with Online Banking and Shopping

Alison knows her math skills are not as sharp as they used to be. She is worried about making mistakes that will put her financially at risk. She is not sure she should be using her credit card online. Alison wants to feel safe and supported.

She finds that autocomplete helps when filling out forms. However, she tends to worry that what is entered may not be accurate. She has a paper card listing some commonly needed information such as her phone number, address, and postcode. She stores secure information in a special folder. She has also set up an agreement with the bank to limit spending on her credit card and mobile banking.

#### 6.1.4 Alison Scenario 4: Giving Feedback

Alison would like to give feedback and tell her bank what changes they can make to their web site to make it more usable for her and other mature customers. She struggles to find the feedback form and she has to type in a lot of information to send her suggestions. When she types in her phone number without the area code she receives an error. She tries to fix the error and send the suggestion but the send button becomes disabled, so she probably needs to correct something else as well. At this point Alison feels they do not want her feedback and gives up. She now uses the site much less often. She also finds it hard to reach a support person on the phone because of the confusing phone menu system, so drives into the bank instead. She is thinking of changing to her daughter’s bank, so her daughter can help her.

### 6.2 Amy: An Autistic Computer Scientist

- Problem:" Sometimes people use lots of words on web site links that do not seem to make sense. I think they are metaphors, but I’m not sure."
- Works well:" I put my mouse over items I do not understand and there is some clear text that explains what it did. I would rather they use clear text in the first place then at least I can use it."

Amy loved her computer science course and now programs in several languages. She has discovered she can visualize the outcome of her coding and is quick to find any errors even if they are not highlighted. Writing documentation is less fun and she is too concise. This means some users do not receive enough help using her applications.

#### 6.2.1 Amy Scenario 1: Coping with Poor Layouts and Illogical Navigation

Being able to code your own web sites can make you very critical of others! Amy copes best when important elements are consistently positioned where she can see them. She can then focus on the actual content and not on finding things. She often feels quite confused by some social media sites that have dynamically changing content with random messages and advertisements. She either avoids these sites or tends to try to personalize them by clearing away the clutter and choosing to hide sections. Navigation that does not follow a simple route across an entire site really annoys her, as she feels this does not help anyone. She also finds that she is missing important information on sites that have too much information on pages or have no clear and logical structure.

#### 6.2.2 Amy Scenario 2: Changing Color Schemes, Flashing, Blinking, and Automatic Playing Videos or Music

A page that loads automatically or animations and videos that play automatically cause problems for Amy. Sometimes, the movement can be very distracting and the sounds alarming. Amy has always found that sudden noises or something happening unintentionally has been a problem. When designing her own applications and web sites, she makes sure the controls for animated objects and videos are clearly visible and do not start until the user decides to play them.

#### 6.2.3 Amy Scenario 3: Designs that Make Use of Abstract Imagery and Metaphors

Amy is always concerned about communicating clearly. She finds it hard when people ask her to create a design that includes abstract imagery. Images that do not directly represent something make Amy feel uneasy. She tends to ask if there can be some explanatory text in case other users are confused. Figures of speech where someone has written something that is not literal make her wish that the writer would use [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") as it is hard to understand concepts such as, "the wheels of justice turn slowly".

### 6.3 George: A User who Works in a Supermarket and has Down Syndrome

- Problem:" I find it hard to understand and remember long and complex written instructions."
- Works well:" The instructions for scanning items are presented as a clear list of steps with pictures and [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.") next to them. If I get stuck I can quickly find a reminder of what to do with such ‘Easy to Understand’ content."

George enjoys his job and lives semi-independently in a small town, where he can easily find his way around. However, George finds it hard to use search engines and navigate around web sites because of the need to work with large blocks of text. He has problems using the online systems at work, and needs help to search for suitable videos or music.

#### 6.3.1 George Scenario 1: Using Symbols for Communication

George used symbols in a [alternative and augmentative communication system](#dfn-alternative-and-augmentative-communication-system "Any method, device, or application that can be used to help those who cannot use spoken language and need additional support by means of symbols, images, and/or text. For example, a screen with symbols that the user can select to speak the appropriate words or add them to a document.") and gestures when at school. He is able to communicate relatively easily now, although reading and writing remains a challenge. Surfing the Web is hard when most interactions require text input. Even with these challenges, George likes to watch videos, find images, and listen to music as well as playing games online. Friends have set up links with recognizable icons on his tablet and this has made it easy to visit his favorite sites. If recognizable symbols or icons are used, George feels he is able to reach more sites independently. There are search engines designed for children and these often use more images. However, these tend to be too childish for George's taste.

#### 6.3.2 George Scenario 2: Understanding Netiquette and its Impact on Social Media Sites

George was told about surfing safely and not giving out personal information. He is very lucky that his family has set up his social media and chat account with various privacy settings. However, George finds the way emojis change or new icons keep appearing on his message systems rather confusing. He does not always realize what some of them mean. He has sometimes selected an inappropriate symbol and then receives a rather short message from a friend in return that is upsetting. He finds it hard to explain what might have happened. He knows there are times when he really cannot choose the right symbol because it is too small and he finds it hard to accurately hit the spot. George is then very worried as he does not know how to 'unlike' or change his symbol choice. Interacting with emojis, icons and symbols is much easier for him with easy ways to enlarge these features on touch interfaces and to undo errors.

#### 6.3.3 George Scenario 3: Controls on Videos and Popup Windows

Using a mouse is not easy for everyone and double clicking can take time to learn. George has worked hard to improve his mouse skills by playing many onscreen games. However, he still finds it hard to move accurately enough to skip ads on videos or to track down the close/exit method offered by some pop-up windows. Once again friends have come to the rescue and enabled an ad blocker extension for his browser. However, this does not always capture all the ads or prevent George from selecting the submit button rather than a cross or exit button on a pop-up. There have been times when George has downloaded malware without any second warning appearing. Sometimes he is unable to reach a site because he cannot find the small cross on a transparent popup window that overlays the main page.

#### 6.3.4 George Scenario 4: Finding Ways to Read Instructions

George finds it very hard to read instructions unless they use very short and [easy to understand language](#dfn-easy-to-understand-language "Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well."). He needs text that has been simplified. The best option for George is when there is a summary of a paragraph with a well-known symbol, short bullet points and a clear diagram or image of what is required. He finds videos with instructions usually go too quickly. He has to stop them, going back time and time again. Helpful instructions with well broken up sets of phrases using easy to understand words can work well. He can then go back to them when he has to remember how to do a particular task.

### 6.4 Gopal: A Retired Lawyer with Dementia

- Problem:" I want to turn the volume up but there is no dial?"
- Works well:" There is a clear volume button with a label that makes sense, so I know what to press."

Gopal retired from his law firm in his early 60s when he found he was forgetting important items that needed to be discussed in his complex caseload. He found that he was forgetting material that he had just read, losing and misplacing objects, and having trouble planning or organizing events. Gopal is a very intelligent man and that has not changed. You will often find him reading an article about the law. However, he finds he cannot learn new things that rely on remembering new information. This can include new words or symbols.

#### 6.4.1 Gopal Scenario 1: Managing Dates and Booking Holidays

Gopal notices that he has trouble with online calendars, booking flights, and hotels when he plans his summer holiday. He can work out the way the dates have to be entered into the form, but makes mistakes with the month and day. If only there was a good example or tooltip!
He also finds that when he is booking a flight, the table with the various lists of airports automatically enters the initials. He finds this is very confusing when he is checking that everything is correct. Finally, Gopal can make sure he has booked the right number of nights for his hotel stay. He knows his arrival time at the airport is a day later than when he left, but it would help to have a calendar with color and clear markings for the days in the week, not just numbers.

#### 6.4.2 Gopal Scenario 2: Coping with Icons that are not Recognizable

Many web pages now have their own graphic icons and ways of indicating actions that need to be completed. Gopal is having problems searching for information about a care home that might help him in the future. He cannot work out what the various options are when he tries to fill out a form for his requirements. There appear to be a series of small images beside the edit boxes. However, the minute he begins to write in the form the text explanation disappears. He wants the instructions to remain in place above the area where he is writing and for the box to be highlighted when he misses some important sections.

#### 6.4.3 Gopal Scenario 3: Support when Using Search Engines

Gopal likes to surf the web for anything to do with fishing, his favorite hobby. However, he finds the sheer number of items that appear very confusing. Ideally he would like the number of search results to be reduced and perhaps have some way of seeing the items categorized in groups, so that he can work out which services he needs. In this case it might also be helpful to have icons appearing when the groups are listed, so that he can see articles about fly fishing in one section and sea fishing in another. Blocks of text with more white space around them are also helpful, so that he does not have to cope with such a mass of text.

#### 6.4.4 Gopal Scenario 4: Making a Medical Appointment

Gopal can be independent, but often finds unsuitable designs make him require help. For example, when he tries to make a doctor's appointment. He goes to the doctor's web site and clicks on "make an appointment". Then a popup opens asking him for the date. He is distracted by a phone call. When he returns to the screen he is not sure what he was doing. So he does not make the appointment. If a popup has a clear heading he can be reminded of what he was doing, but without this landmark he is just confused.

Later, Gopal tries calling to make an appointment. Unfortunately, the voice system is automated and asks him to "press 2 to make an appointment". Gopal typically cannot remember the digit, especially while he is processing the options. He usually gets lost in these systems or types the wrong digit. Gopal is reluctant to ask for help and as a result he is not getting the health care he needs.

#### 6.4.5 Gopal Scenario 5: Using the Heating

Eventually, Gopal moves to a smaller apartment that is easier to take care of. However, this means he is not used to the ICT interfaces for the heating and television system. He tries to turn on the heat. However, the menu item for selecting heat or air conditioning is labeled "mode" which does not mean anything to him. He cannot remember or learn new terms. Gopal cannot use the whole unit because of this one term. This has caused emergencies, such as hypothermia. Gopal now keeps the heating on at the same setting and temperature and will only change it when his helper comes.

The TV also has an ICT interface with a lot of icons that Gopal does not know. His helper puts an “on/off” sticker next to the button that he can use. However, he still cannot change the channel or change the volume.

When his microwave broke he bought a new one with controls that were similar to his old one. Because the controls are familiar, Gopal can use the microwave unaided, although he still needs help with the TV and heating.

### 6.5 Jonathan: A Therapist with Dyscalculia

- Problem:" It says there is a meeting at 15.34 UTH. Now is lunch time. Did I miss it?"
- Works well:" There is a line marker showing what time of day it is now, so I can see the meeting is soon."

Jonathan is a massage therapist with dyscalculia. Although he is very intelligent in other areas, he has trouble working with numbers and needs to count on his fingers to add very basic sums. He struggles with concepts like “greater than” and “less than” and understanding how numbers are related to each other, especially ones that end in a series of zeros such as 10, 100, 1000, etc. It’s hard for him to follow the logic behind mathematical concepts and to do everyday tasks that involve numbers or quantities, like measuring ingredients in a recipe or paying for things in cash.

#### 6.5.1 Jonathan Scenario 1: Coping with Quantities when Shopping Online

Jonathan struggles to understand how much the products in his cart will cost, especially when he is buying items like meat that are priced by weight. It’s also hard for him to know the right quantities to purchase. He often orders far too much or too little when using online shopping carts. It helps him when shopping web sites provide a way to know the size without numbers, such as showing pictures of the actual products or using terms like small, medium, and large. It also helps him to get a warning when he orders a very large quantity of a particular item so he can correct mistakes like ordering six bunches of bananas when he meant to buy one bunch of six bananas. He saves shopping lists that have been successful in terms of ordering the right quantity for each item so that he can re-use the lists on other occasions. He often ends up spending a lot more than he intended to because he is unaware of relative prices. His bank has helped by adding restrictions on the amount
he can spend online or using his mobile phone. This can be annoying, but has stopped him from overdrawing his account.

#### 6.5.2 Jonathan Scenario 2: Remembering Pin Numbers and Passwords

The use of pin numbers and passwords that insist on including a number has always been an issue and most of the time Jonathan uses a secure password application when online. When it comes to the number on the back of his credit card (Card Verification Code) that is always required at the end of a payment exercise, he has to look it up each time, though autofill has helped with completing the rest of the form. Jonathan made sure that what he originally entered and saved in his browser was correct. Too many times he has had to retrace his steps due to typos and not seeing that the entry was incorrect. When he has to return to the form to make corrections, he finds it essential that the corrections needed are clearly highlighted and the instructions provided are helpful. He also feels that it is important that the data he entered previously is not lost, as the more often he types in numbers etc. the more likely he is to make mistakes.

#### 6.5.3 Jonathan Scenario 3: Using Spreadsheets Shared with Colleagues

At work, there are times when Jonathan has to share a spreadsheet with a colleague to ensure that the group’s accounts are in order, suppliers have been correctly invoiced and fees collected. Looking at the massive grid of numbers makes Jonathan anxious and affects his ability to concentrate on specific parts of the spreadsheet. He has found that it helps to use color coding, increased spacing, and larger font sizes to pick out the various elements. He uses a tool for recording his hours where he can press start and stop to see how long he has worked without using math but he is not confident to add hours worked to the spreadsheet himself. He wishes it was integrated into the work spreadsheet. Jonathan will often use the comment feature to add something that he feels his colleague needs to check, rather than making the correction to the spreadsheet himself.

When Jonathan needs to give a presentation that involves numbers, he plans ahead by saving the document as a PDF or in another format he can use with his text-to-speech application. This tool helps him find out the correct way to pronounce a multi-digit number, like 1540. Sometimes the context is missing making the pronunciation of the text-to-speech unreliable, so he also checks with his partner. He annotates the document with the correct pronunciation.

#### 6.5.4 Jonathan Scenario 4: Reading Chart and Graphs

Jonathan is interested in reading about climate change, but has trouble understanding charts showing the expected rise in temperature over time. This happens when all the temperatures are shown as numbers. Jonathan finds it much easier when words such as cold, warm, or hot are used with color changes on a drawing to show the problem.

Jonathan also finds a graph, diagram, or table can be confusing if there is no summary beforehand. He spends far too long trying to work out what the content means. Jonathan also likes clear labels or short summaries to help explain the individual parts of the diagram, graph, or table. Although good use of color and shapes can help when numbers are represented visually, Jonathan finds clear written descriptions easier to understand.

### 6.6 Kwame: A Traumatic Brain Injury Survivor

- Problem:" I got lost making a shopping order and I wanted to go back to the previous step. I hit the back button on the browser navigation bar and it reloaded the home page. I had to start all over again."
- Works well:" There is a clear back button on each step and when I use the browser back button it also works."

Kwame was involved in a very serious car crash that left him with some physical, sensory, and cognitive and learning disabilities having sustained a [brain injury](#dfn-brain-injury "Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of executive function, memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments."). He has returned to work. However, he often finds conversations are strained due to difficulties with memory recollection and visual understanding.

Kwame learnt how to walk, talk, and live life all over again. Medical experts informed him that his greatest chances for recovery would take place within the first 2 years after his injury. After that he may continue to recover, but at a much slower, and incremental rate. His friends and family are amazed by how quickly he has regained his ability to speak, and perform his daily life functions. They are confused by all of the cognitive difficulties he says he is having, despite his ability to articulate and communicate. For example, he often cannot recognize images and faces. He gets disorientated in physical spaces. He often gets lost in rooms, as well as buildings, larger places, documents, and web sites.

He has returned to his old company as a researcher and is back using applications and the internet throughout his working day.

#### 6.6.1 Kwame Scenario 1: Using Speech Recognition to Navigate the Web

Kwame has dexterity difficulties, so he sometimes uses speech recognition to work through web pages and enter text. He finds this method the least tiring of all the possible input options. Although his speech is slow, he is able to control his computer using speech commands and dictation. It is quite easy to use simple commands to control web sites, although there are times when he forgets some of the commands and has to use his cheat sheet. Kwame likes the scroll commands that allow him to read slowly down a page without using any other input device and he often retraces his steps to reread items. However, there can be problems if the forms on the web site are not labeled correctly or if buttons do not have clear names. Kwame has help personalizing some aspects of form completion. However, if an element is inaccessible via the keyboard, he uses the mouse grid to interact with that part of the site. This is a slow process and can be frustrating as Kwame finds he loses concentration.

#### 6.6.2 Kwame Scenario 2: Finding the Right Words to Use for Searching

Kwame finds there are times when he spells words incorrectly. He appreciates error corrections, word completion, and systems that accept mistakes. He also has problems finding words when he is tired. He welcomes search suggestions, as these are ideas that might be related to his search. However, too many results can cause concern and Kwame admits he really cannot work his way through very long lists that are not broken up with headings and categories.

#### 6.6.3 Kwame Scenario 3: Being Confident that He Understands the Content

Kwame has difficulty understanding content when it is not explicitly clear, and without any ambiguity whatsoever. He takes a notably longer amount of time to read and process information to be certain that he is interpreting it correctly. His interpretation of information is almost always correct. However, even the slightest bit of ambiguity, or open interpretation creates sticking points that he must read over and over again. He questions every which way until he can assure himself that he understands it correctly. Examples and clear step-by-step instructions can help him have the confidence to complete his task. Simple, clear memorable graphics or large indicators of steps in a process increase Kwame’s understanding, confidence, and orientation in a process. Kwame also prefers larger fonts. Reading smaller text takes up mental energy that isn’t available for trying to understand what is being said.

#### 6.6.4 Kwame Scenario 4: Understanding where Information is in a Hierarchical Structure

Kwame tries to understand the outline of the page and site, so that he does not get lost in the content. Sometimes he dives into the web site, but then he does not know where he is in the content or task. For Kwame to understand the level of importance of content he needs clear and consistent headings in a hierarchical structure. A clear site structure lets him orient himself in the site.

He values simple, clear graphics that relate to the content and break it up. These help him orient as well as understand and remember the content. He needs icons that emphasize the structure and role of the content. Images that accompany the main text and make it memorable also help.

#### 6.6.5 Kwame Scenario 5: Cognitive Overload

Complex presentations of information (images, diagrams, content heavy web pages, etc.) overload Kwame’s cognitive functioning. This shuts his brain down and prevents him from progressing through processes, navigating, systems, and environments. He stops understanding the information presented, at both the micro and macro level.

Liberal use of white space helps Kwame when there is a considerable amount of content on one page.

He struggles to keep track of what he is doing in complex tasks. It is important for Kwame to have the steps of tasks clearly presented, and a mechanism like breadcrumbs that helps Kwame keep track of where he is in a task with multiple steps. Kwame appreciates it when tasks are as simple as possible. “It can’t ever be too simple,” he says.

#### 6.6.6 Kwame Scenario 6: Struggling with Directions

Kwame struggles to respond quickly to spoken directions when using a mapping program to find his way to a location. Kwame benefits from previewing the directions before he leaves. He finds route changes very difficult to adjust to. He changes the settings so that directions are given using the terms ‘driver’s side’ and ‘passenger’s side’ instead of left and right, and makes sure the route does not change automatically.

### 6.7 Maria: A User who has Memory Loss

- Problem:" When there are lots of buttons or menu items I often make mistakes and press the wrong ones and end up getting frustrated and wasting time."
- Works well:" I like web sites that allow me to work through a series of instructions and edit boxes one after the other with clear buttons moving me to the next stage."

Maria is 50 years old, married, and lives with her family in São Paulo, Brazil. Maria is beginning to lose her memory but still works part-time for a local company.

#### 6.7.1 Maria Scenario 1: Finding Key Information on web sites

Maria needs to gather specific types of online information for her job. She often has to run through reports about the company on the company’s web site. She is only able to easily read the headlines of web pages. The company’s web site looks fancy, has a modern user interface and a lot of elements that change when you hover the mouse over them. For Maria this site is a total nightmare! She finally finds the link to the data she needs as it appears when she happens to hover over a certain menu item with her mouse. The link is positioned so that she does not notice it at first. She has found that it really helps if important interactive items are placed in the usual menu areas on a screen and the icons are clearly defined and easily recognizable.

#### 6.7.2 Maria Scenario 2: Remembering Information Entered During a Previous Step

While ordering business cards (a multi-step process), Maria has difficulty remembering information that she enters into previous screens. On the first step she sees content choices that the process expects her to remember in later screens. Additionally, the prolonged mental stress that she experiences while navigating means it is hard for her to make new memories. Processes that require Maria to remember information from one step to another need to give her the information required, at the exact point of use, otherwise she will not be able to complete the process.

#### 6.7.3 Maria Scenario 3: Pressing the Correct Button

Maria has eye hand coordination difficulties, so precise movements are hard. She often touches the wrong button on her small phone screen. This means she presses the wrong letter or number when typing. With her letter recognition difficulties this also makes typing in codes or text very unreliable. She confuses left and right so she is pressing the off button in place of the volume. In most interactions on her phone she makes some form of mistake, such as loading a new video when she intends to expand the screen of the window she is watching. To use any application successfully it needs to have a consistent back or undo function.

### 6.8 Sam: A Librarian who has a Hemiplegia and Aphasia

- Problem:" Long sentences are hard, too many strange words, and I get lost."
- Works well:" I like simple short sentences with easy words."

Sam loved his work as a librarian. He spent his entire life surrounded by books in peaceful places where he could research his love for history. In recent years, he enjoyed using the web to explore how other people around the world saw the history of his own country and the changing views on famous people from the past. Now he is depressed and very frustrated due to a recent stroke. The right side of his body is paralyzed. He also has difficulty having conversations with friends and family due to aphasia. To him this means that some of his words are muddled and his understanding is not always as clear as it has been. Worst of all, he cannot read as fluently as he has in the past. One-handed typing is slow and he finds his word finding abilities often fail him.

#### 6.8.1 Sam Scenario 1: Having Well-spaced Text with Words that are Easy to Pick Out

Despite all the difficulties that Sam has with his beloved reading, he is determined to improve and finds that if a web site has no clutter or background imagery he can read the headings. He also finds that if there is adequate spacing and the text is not too complex, he can pick words out and with the help of text-to-speech understand the meaning. He does not like the sound of the synthesized speech, because he finds it distracting having always read silently. However, over time, he is learning to enlarge the fonts and if the page has left justified text with uneven right edges, he can find his way about by the different shapes of each paragraph. As he becomes more confident, he is beginning to use some browser tools and is able to increase the line spacing and change the font style on some of his old favorite online historical documents.

#### 6.8.2 Sam Scenario 2: Using Edit Boxes where the Instructions Disappear

Sam has to fill in so many online forms to receive benefits due to his disability. They cause immense frustration and feelings of self-doubt due to their lack of clarity. Every time he has to fill in an edit box, the instructions disappear the minute he begins to type and he cannot remember what is required. He often has to refresh the page and start again to see the label in the box. Sam spends so long on the task that the page times out. He has to print it out and get help. This is really upsetting as he wants to be independent and it often reduces him to tears. This is very unlike him, but as the doctor explains, this is linked to his stroke. He also finds it very frustrating when a form requires a particular way of formatting information with no example as to how to complete the action. Worse still is when the error is not clearly explained, making correction even harder. Dates, postal codes, and phone numbers are a particular nightmare.

#### 6.8.3 Sam Scenario 3: Trying to Activate Elements that are Mis-recognized

The effects of aphasia with acquired dyslexia can be exhausting and confusing but most worrying for Sam is the sense of getting lost on a web page that he thinks he knows. He admits to being nervous when he cannot pick out elements in a page that requires an interaction. Sometimes he dares not click on a button in case he does something wrong or is sent to somewhere without warning. Sam finds this aspect of his web surfing very alarming, as in the past he has been able to navigate with ease. He discovers that the edges of shapes do not appear as clear as they should when people use pale greys. He misses links unless expressly highlighted. If a pop-up window suddenly appears, there are times when he cannot close it to return to the page. Small crosses or “x”s to close popup windows become a nightmare. Sam stresses that the more things happen on a page, the more confused he becomes. He mentions the fact that some sites are easier on his tablet, as then it all seems to flow
one way. He can just scroll up and down until he feels happy with a decision.

#### 6.8.4 Sam Scenario 4: Coping with Complex Language

When text was written in the passive voice or in an academic manner with long complex words Sam struggled to sometimes understand their meaning even if they were in context. He also finds, if he is required to use the same type of language in a form, that he can copy the words as he cannot always spell them. At times he uses the wrong word. When he is able to use an application that enables the text to be read aloud, he can cope if the language is clear and the sentences are kept short. He likes articles that are written in the active tense so he can understand the main ideas straight away.

### 6.9 Tal: A Student who has Dyslexia and Impaired Eye Hand Coordination

- Problem:" As a slow reader it takes me ages to read through badly structured text and I often miss important information."
- Works well:" The newsletter has headings so I can find the important information quickly."

Tal has been a student in Israel for the past year. Tal's Fashion Design course is challenging but fun. Tal loves the creative aspect of the diploma where there is more drawing than writing. Tal has moderate dyslexia, resulting in times when it is hard to cope with complex text. Tal sometimes finds it a challenge working out how words are pronounced when they have many syllables. This can make it hard for Tal to grasp the meaning of some paragraphs. They often have to reread content. Tal has several projects to complete as part of the Fashion Design portfolio requirements. The one that worries Tal most involves a written assignment to research post-war fashions and their impact on today's designs.

#### 6.9.1 Tal Scenario 1: Logging In

Tal's use of the library catalogue when using the college computers often fails at the first attempt. This happens when Tal cannot remember the login password. Tal keeps putting in talb-61 rather than tald-16 and cannot see the mistakes. The error message on the web page does not help because it announces that the username or password are incorrect. Tal is not sure which one is wrong. Luckily, when Tal is on a family owned laptop, the browser settings allow Tal to save the password and automatically log in.

#### 6.9.2 Tal Scenario 2: Finding Accessible Content

Having navigated the online library system, Tal finds a paper about Post-war fashion. Tal downloads it in PDF format. Tal likes to use a text-to-speech application to read the content aloud, but when Tal tries to highlight the text nothing happens. Tal discovers the document is actually an image and yet there is no warning this is the case. Tal cannot find an alternative accessible version of the paper. This means Tal has to use optical character recognition to virtually scan the paper. It is not totally successful leaving Tal with gaps in the information. Tal finds the process makes it even harder to complete the assignment on time.

#### 6.9.3 Tal Scenario 3: Filling in a Form to Ask for an Online Journal Article

Finally, Tal finds an online journal that has another article, but there is a form that has to be completed in order to cite the paper. Tal starts the process, but realizes they do not know the author's name. Tal returns to the web page with the article to copy and paste the name. Sadly, when Tal comes back to the form, all that they filled in is lost. Tal has to retype the whole thing again.

#### 6.9.4 Tal Scenario 4: Overlooking Important Information

Tal is a very slow reader and often sounds out words. Tal has impaired auditory processing skills so cannot speed up the text-to-speech application. To manage a busy life, Tal tries to scan and skip through the massive amounts of content, emails, and newsletters to read the key parts. Sometimes however, Tal cannot find important content because it is buried inside lots of other content. The headers and visual layout of the content does not always guide Tal to the information needed.

This all means that Tal worries about missing something important and sometimes that happens. For example, Tal's daughter's elementary school published a weekly newsletter with interesting stories about activities and important announcements. It contained information that school was ending early one day, but it was buried under less important information about the school activities. Because it takes Tal so long to read each word, they did not manage to read the whole newsletter and did not know that their daughter was coming home earlier than usual. As a result, Tal was not home in time and their daughter was left waiting outside for over an hour.

#### 6.9.5 Tal Scenario 5: Pressing the Correct Button

Tal struggles with impaired eye hand coordination, so precise movements are hard. Tal often touches the wrong button or number when typing on a small phone screen. With Tal's letter recognition difficulties this makes typing in codes or text very unreliable. Tal also confuses left and right so often presses the off button in place of the volume. In most phone interactions, Tal makes some form of mistake. Tal relies on a consistent back or undo function to be able to use an application successfully.

### 6.10 Yuki: A Yoga Teacher who has AD(H)D

- Problem:" If I come to a web site that has lots of banners automatically flying by it really distracts me and I want to turn them off!"
- Works well:" I find an option on my computer to say I want less movement and the web site stops all the flying things."

Yuki found concentrating at school difficult. When she got into college and started taking a course in business studies life became even more stressful. She knew she could cope with the studies, but never seemed to get her work completed on time. She found it hard to start a report and even to create a plan for a project. When working with others she always had good ideas but somehow they were never taken up. She became frustrated, often failing to keep her feelings in check. Luckily, a tutor suggested she look for help. When a psychologist mentioned [Attention Deficit Hyperactive Disorder](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.") or AD(H)D, Yuki was relieved to have a reason for her planning and organizational difficulties and other [executive functions](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."). She did not want to draw attention to her difficulties, but knowing what caused the challenges helped her find solutions. She learnt that if she could make use of her constantly active brain and body as well as manage her time better, she could turn her hobby into a very successful Yoga business.

#### 6.10.1 Yuki Scenario 1: Gathering Key Points from a Heavy Text Based Document or Web Page

Yuki could not really explain her apparent forgetfulness and not being able to focus or complete tasks. She knew that if she came across a long document or web page with dense text she had to find the key points. If the web page failed to have a clear structure, well-spaced and highlighted headings she would be lost and lose concentration. Yuki also said that if she was reading her mobile screen, advertisements appearing between chunks of text upset her focus and she had to stop reading. However, when there was good use of white space, recognizable icons linking to simple bold text clarifying the important points, Yuki could target these areas and find out what she needed. A clear summary helped Yuki understand and she could remember much of what she had read.

#### 6.10.2 Yuki Scenario 2: Stopping Carousels and Banners from Scrolling

When setting up a new web site for her yoga business, Yuki found an attractive template with several different ways of being able to show images of her exercises. However, she could not make the carousel of photographs pause, or a banner with her latest news stop scrolling. This really annoyed her, as she found both items stopped her concentrating on the important content on the rest of the site. She thought that if it was upsetting her; what about her intended audience? She had to find a friend to add some code that not only added controls, but also stopped the automatic movement, giving her web site a calmness that she hoped her yoga teaching achieved.

#### 6.10.3 Yuki Scenario 3: Losing Focus when Completing Tasks

Yuki enjoyed her yoga teaching. However, she found that if she was developing some instructional materials for her web site, online tools often failed to provide sufficient guidance. Unless there was a clear pathway and a way to return to the place where she was working, she often deleted items by accident or could not make corrections. Saving endless previews with yet more tabs being open in her browser caused anxiety levels to rise. It was not until she found a web application that made each task clear with a submit button, that saved her work in stages, that she was able to cope. Yuki was able to see sections of her work in the correct order and could then manage the bite size chunks of instruction, rather than have to deal with it all at once. This made it so much easier for her to complete the exercise sheets. She became confident in her use of the application to the extent she was willing to purchase the pro version.

#### 6.10.4 Yuki Scenario 4: Learning Information from a Video

Yuki likes watching instructional videos, but starts to lose focus after a few minutes. It's especially hard for her to concentrate if there is more than a minute of content that she already knows. Sometimes she watches videos at high speed so that they are less boring, but she still quickly loses focus and has trouble locating information she missed. When a video is broken down into segments with clear headings, she can jump to the information she needs to learn. She can also jump forward over segments that she already knows. When she misses information that she needs, she can easily jump to the correct location and focus. If a video transcript is available, she likes to search it for key terms. Watching the video and reading parts of the transcript helps her learn new information.

## 7. Glossary

Age Related Forgetfulness
:   Sometimes called "Age Appropriate Forgetfulness" or "Age Related Memory Loss".

    People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)

Alternative and Augmentative Communication System
:   Sometimes called “AAC”.

    Any method, device, or application that can be used to help those who cannot use spoken language and need additional support by means of symbols, images, and/or text. For example, a screen with symbols that the user can select to speak the appropriate words or add them to a document.

Anxiety Disorders
:   People who have anxiety disorders struggle with intense and uncontrollable feelings of anxiety, fear, worry, and/or panic. This is more than just feeling worried once in a while. This may last for a long time and can interfere with daily activities, such as concentration and [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.").

Attention Deficit (Hyperactivity) disorder, AD(H)D
:   Sometimes called “attention deficit disorder”, “ADD”, and “attention deficit hyperactivity disorder”, “ADHD”.

    Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.

Autistic
:   Sometimes called “autism spectrum disorder”, “ASD”, “autism”, “asperger syndrome”, and “pervasive developmental disorder”.

    Autistic people have some degree of impaired social behavior, communication and language abilities. This may also impact the person’s ability to regulate behavior and attention. Individuals can have a narrow range of interests and activities and they may rely on alternative communication methods. Some individuals may also experience episodes of sensory overload. See neurodiversity for an alternative approach to autism and learning and cognitive disabilities.

Brain Injury
:   Brain injury including, traumatic brain injury (TBI) and acquired brain injury (ABI), are caused by damage to the brain which can lead to long-term impairment of [executive function](#dfn-executive-function "The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems."), memory, learning, coordination, speech, and emotions as well as other physical and sensory impairments.

    Brain injury can have many different causes such as a concussion or stroke, and can happen at any stage of life.

Cognitive and Learning Disabilities
:   May include: cognitive disabilities, learning disabilities (LD), intellectual disabilities and specific learning disability.

    Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:

    - significantly reduced ability in one or more areas of cognitive function that affect learning, such as communication, reading, writing, or math. Note overall intelligence is often not affected and people may function any level in other areas of learning. (Sometimes called learning disability or specific learning disability), and / or
    - significantly reduced ability to understand new or complex information and learn new skills, with a reduced ability to cope independently. (Sometimes called cognitive disability, learning disability or intellectual disability), and / or
    - significantly reduced memory and attention or visual, language, or numerical thinking.

Early Stage Dementia
:   Common impairments of early stage dementia include memory loss, difficulty concentrating, and struggling to follow a conversation or find the right word. These may appear before a diagnosis of dementia. At this stage, these symptoms are often mild.

Easy to Understand Language
:   Sometimes called: “easy reading”, “easy to read”, “plain language”, “easy to understand”.

    Easy to Understand Language refers to text content that is in an accessible, easy to understand, form. It is often useful for people with learning disabilities, and is easier for many other people as well.

Executive Function
:   The group of cognitive processes and skills required for planning, fulfilling tasks, and goals. It includes working memory and remembering details, impulse inhibition, organizing tasks, managing time, fluid reasoning, and solving problems.

Interactive Voice Response
:   Interactive voice response (IVR) systems allow the user to interact with a computer system through the use of a telephone keypad and/or audio input. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Interactive voice response systems are often used to automate tasks by phone and in call centers. IVR systems often use standards such as VoiceXML [[voicexml21](#bib-voicexml21 "Voice Extensible Markup Language (VoiceXML) 2.1")].

Memory Impairment
:   Memory impairment refers to an inability to recognize or recall pieces of information or skills that are usually remembered. It can affect:

    - Working memory that holds information while it is processed. For example, we rely on working memory for tasks such as copying a number.
    - Short-term Memory that stores information for a short time before it is stored in long-term memory. For example, we may rely on short-term memory to remember the location of menus items between web pages.
    - Long-term Memory that holds information long term, such as information from personal events, language, and information. For example, we may rely on long-term memory to recall past events.

Mental Health
:   May include: mental heath impairments.

    Mental health refers to our emotional, psychological, and social well-being. A mental health impairment/condition generally has some combination of disturbed thoughts, emotions, and ability to relate to others that impairs daily functioning. Examples include depression, anxiety, and post-traumatic stress disorder. These conditions may cause temporary or long term issues with accessing information, such as difficulty focusing on information, processing information, or understanding it.

Mild Cognitive Impairment (MCI)
:   Mild cognitive impairment (MCI) can involve problems with memory, language, thinking, and judgment that are greater than normal age-related challenges. It is sometimes considered the stage between the common and expected [age related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") and the more serious decline of dementia, although many or most people with MCI will not develop dementia.

Neurodiversity
:   Neurodiversity is a term that refers to the different ways the brain can work and interpret information. It highlights that people naturally think about things differently. [Autistic](#dfn-autistic "Sometimes called “autism spectrum disorder”, “ASD”, “autism”, “asperger syndrome”, and “pervasive developmental disorder”.") people, [attention deficit (hyperactivity) disorder](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.") ([AD(H)D](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d "Attention deficit (hyperactivity) disorder or AD(H)D involves difficulty focusing on a single task, focusing for longer periods, or being easily distracted. It is marked by an ongoing pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development.")), dyslexia, and people with other diagnoses or labels may prefer the term “neurodiverse” as they are part of normal and healthy variation in the human population, bringing diverse skills and perspectives.

Voice User Interfaces
:   Sometimes called: Conversational interfaces.

    Voice user interfaces (VUIs) allow the user to interact with a computer system based on audio input and/or output. Audio input can include speech, non-speech vocalizations or audio produced by AAC or other devices. Audio-based interaction may include both input from the user, and output from the system in response to the input. Examples include: Siri, Google Assistant, and Alexa.

## A. Appendix: Mapping User Needs, Personas, and Patterns

### A.1 Objective 1: Help users understand what things are and how to use them

**Help users understand what things are and how to use them.** Use things that are familiar to the user so that they do not have to learn new icons, symbols, terms, or design patterns. People with cognitive and learning disabilities often need common behavior and design patterns. For example, they may know the standard convention for links (underlined and blue for unvisited; purple for visited).

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Clear Purpose](#clear-purpose-user-story) | - [Make the purpose of your page clear](#make-the-purpose-of-your-page-clear-pattern) - [Make it easy to find the most important tasks and features of the site](#make-it-easy-to-find-the-most-important-tasks-and-features-of-the-site-pattern) - [Make each step clear](#make-each-step-clear-pattern) - [Use icons that help the user](#use-icons-that-help-the-user-pattern)   Related Patterns   - [Make the site hierarchy easy to understand and navigate](#make-the-site-hierarchy-easy-to-understand-and-navigate-pattern) - [Use a clear and understandable page structure](#use-a-clear-and-understandable-page-structure-pattern) - [Make it easy to find the most important actions and information on the page](#make-it-easy-to-find-the-most-important-actions-and-information-on-the-page-pattern) - [Make the relationship clear between controls and the content they affect](#make-the-relationship-clear-between-controls-and-the-content-they-affect-pattern) | - [Yuki: Focus](#yuki-scenario-3-losing-focus-when-completing-tasks) - [Gopal: Making a medical appointment](#gopal-scenario-4-making-a-medical-appointment) - [Maria: Pressing the correct button](#maria-scenario-3-pressing-the-correct-button) - [Maria: Finding key information on web sites](#maria-scenario-1-finding-key-information-on-web-sites) - [Kwame: Understanding where information is in a hierarchical structure](#kwame-scenario-4-understanding-where-information-is-in-a-hierarchical-structure) |
| [Clear Operation](#clear-operation-user-story) | - [Use a familiar hierarchy and design](#use-a-familiar-hierarchy-and-design-pattern) - [Use a consistent visual design](#use-a-consistent-visual-design-pattern) - [Clearly identify controls and their use](#clearly-identify-controls-and-their-use-pattern) - [Make the relationship clear between controls and the content they affect](#make-the-relationship-clear-between-controls-and-the-content-they-affect-pattern)   Related Patterns   - [Make it easy to find the most important tasks and features of the site](#make-it-easy-to-find-the-most-important-tasks-and-features-of-the-site-pattern) - [Clearly state the results and disadvantages of actions, options, and selections](#clearly-state-the-results-and-disadvantages-of-actions-options-and-selections-pattern) | - [Alison: Learning how to use new technologies and interfaces](#alison-scenario-1-learning-how-to-use-new-technologies-and-interfaces) - [Amy: Coping with poor layouts and illogical navigation](#amy-scenario-1-coping-with-poor-layouts-and-illogical-navigation) - [Tal: Finding important information](#tal-scenario-4-overlooking-important-information) - [Gopal: Coping with icons that are not recognizable](#gopal-scenario-2-coping-with-icons-that-are-not-recognizable) - [Gopal: Using the heating](#gopal-scenario-5-using-the-heating) - [George: Controls on videos and popup windows](#george-scenario-3-controls-on-videos-and-popup-windows) - [Sam: Using edit boxes where the instructions disappear](#sam-scenario-2-using-edit-boxes-where-the-instructions-disappear) - [Sam: Trying to activate elements that are mis-recognized](#sam-scenario-3-trying-to-activate-elements-that-are-mis-recognized) |
| [Symbols (pictographic or ideographic that represent concepts)](#symbols-pictographic-or-ideographic-that-represent-concepts-user-story) | - [Use icons that help the user](#use-icons-that-help-the-user-pattern) - [Support a personalized and familiar interface](#support-a-personalized-and-familiar-interface-pattern) | - [Gopal: Coping with icons that are not recognizable](#gopal-scenario-2-coping-with-icons-that-are-not-recognizable) - [George: Using symbols for communication](#george-scenario-1-using-symbols-for-communication) |

### A.2 Objective 2: Help users find what they need

**Help users find what they need.** Navigating a system should be easy. Have a clear and easy to follow layout with visual cues, such as icons. Clear headings, boundaries, and regions also helps people understand the page design.

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Findable](#findable-user-story) | - [Make it easy to find the most important tasks and features of the site](#make-it-easy-to-find-the-most-important-tasks-and-features-of-the-site-pattern) - [Make it easy to find the most important actions and information on the page](#make-it-easy-to-find-the-most-important-actions-and-information-on-the-page-pattern)   Related Patterns   - [Provide search](#provide-search-pattern) - [Make short critical paths](#make-short-critical-paths-pattern) - [Notify users of fees and charges at the start of a task](#notify-users-of-fees-and-charges-at-the-start-of-a-task-pattern) - [Provide information so a user can complete and prepare for a task](#provide-information-so-a-user-can-complete-and-prepare-for-a-task-pattern) | - [Alison: Learning how to use new technologies and interfaces](#alison-scenario-1-learning-how-to-use-new-technologies-and-interfaces) - [Amy: Coping with poor layouts and illogical navigation](#amy-scenario-1-coping-with-poor-layouts-and-illogical-navigation) - [Tal: Finding important information](#tal-scenario-4-overlooking-important-information) - [Yuki: Gathering key points from a heavy text based document or web page](#yuki-scenario-1-gathering-key-points-from-a-heavy-text-based-document-or-web-page) - [Yuki: Learning information from a video](#yuki-scenario-4-learning-information-from-a-video) - [Maria: Finding key information on web sites](#maria-scenario-1-finding-key-information-on-web-sites) - [Kwame: Finding the right words to use for searching](#kwame-scenario-2-finding-the-right-words-to-use-for-searching) |
| [Searchable](#searchable-user-story) | - [Provide search](#provide-search-pattern) | - [Kwame: Finding the right words to use for searching](#kwame-scenario-2-finding-the-right-words-to-use-for-searching) |
| [Clear Navigation](#clear-navigation-user-story) | - [Make the site hierarchy easy to understand and navigate](#make-the-site-hierarchy-easy-to-understand-and-navigate-pattern) - [Use a clear and understandable page structure](#use-a-clear-and-understandable-page-structure-pattern) | - [Alison: Learning how to use new technologies and interfaces](#alison-scenario-1-learning-how-to-use-new-technologies-and-interfaces) - [Amy: Coping with poor layouts and illogical navigation](#amy-scenario-1-coping-with-poor-layouts-and-illogical-navigation) - [Gopal: Making a medical appointment](#gopal-scenario-4-making-a-medical-appointment) - [Gopal: Using the heating](#gopal-scenario-5-using-the-heating) - [Gopal: Support when using search engines](#gopal-scenario-3-support-when-using-search-engines) - [Maria: Finding key information on web sites](#maria-scenario-1-finding-key-information-on-web-sites) - [Maria: Access to information entered during previous step in process](#maria-scenario-2-remembering-information-entered-during-a-previous-step) - [Kwame: Understanding where information is in a hierarchical structure](#kwame-scenario-4-understanding-where-information-is-in-a-hierarchical-structure) - [Sam: Having well-spaced text with words that are easy to pick out](#sam-scenario-1-having-well-spaced-text-with-words-that-are-easy-to-pick-out) - [Kwame: Cognitive overload](#kwame-scenario-5-cognitive-overload) |
| [Media (Clear Navigation)](#media-user-story) | - [Break media into chunks](#break-media-into-chunks-pattern) | - [Yuki: Learning information from a video](#yuki-scenario-4-learning-information-from-a-video) |

### A.3 Objective 3: Use clear and understandable content

**Use clear content (text, images and media).** This includes easy words, short sentences and blocks of text, clear images, and easy to understand video.

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Clear Language (Written or Audio)](#clear-language-written-or-audio-user-story) | - [Use clear words](#use-clear-words-pattern) - [Use a simple tense and voice](#use-a-simple-tense-and-voice-pattern) - [Avoid double negatives or nested clauses](#avoid-double-negatives-or-nested-clauses-pattern) - [Use literal language](#use-literal-language-pattern) - [Keep text succinct](#keep-text-succinct-pattern) - [Use clear, unambiguous text formatting and punctuation](#use-clear-unambiguous-formatting-and-punctuation-pattern) - [Include symbols and letters necessary to decipher the words](#include-symbols-and-letters-necessary-to-decipher-the-words-pattern) - [Explain implied content](#explain-implied-content-pattern) - [Provide summary of long documents and media](#provide-summary-of-long-documents-and-media-pattern) | - [Yuki: Gathering key points from a heavy text based document or web page](#yuki-scenario-1-gathering-key-points-from-a-heavy-text-based-document-or-web-page) - [George: Finding ways to read instructions](#george-scenario-4-finding-ways-to-read-instructions) - [Sam: Having well-spaced text with words that are easy to pick out](#sam-scenario-1-having-well-spaced-text-with-words-that-are-easy-to-pick-out) - [Sam: Coping with complex language](#sam-scenario-4-coping-with-complex-language) - [Kwame: Using speech recognition to navigate the Web](#kwame-scenario-1-using-speech-recognition-to-navigate-the-web) - [Kwame: Being confident that he understands the content](#kwame-scenario-3-being-confident-that-he-understands-the-content) |
| [Visual Presentation](#visual-presentation-user-story) | - [Separate each instruction](#separate-each-instruction-pattern) - [Use white spacing](#use-white-spacing-pattern) - [Ensure foreground content is not obscured by background](#ensure-foreground-content-is-not-obscured-by-background-pattern)   Related Patterns   - [Use a clear and understandable page structure](#use-a-clear-and-understandable-page-structure-pattern) - [Use icons that help the user](#use-icons-that-help-the-user-pattern) - [Keep text succinct](#keep-text-succinct-pattern) | - [Amy: Coping with poor layouts and illogical navigation](#amy-scenario-1-coping-with-poor-layouts-and-illogical-navigation) - [Tal: Finding important information](#tal-scenario-4-overlooking-important-information) - [Yuki: Gathering key points from a heavy text based document or web page](#yuki-scenario-1-gathering-key-points-from-a-heavy-text-based-document-or-web-page) - [Yuki: Learning information from a video](#yuki-scenario-4-learning-information-from-a-video) - [Gopal: Support when using search engines](#gopal-scenario-3-support-when-using-search-engines) - [George: Finding ways to read instructions](#george-scenario-4-finding-ways-to-read-instructions) - [Sam: Having well-spaced text with words that are easy to pick out](#sam-scenario-1-having-well-spaced-text-with-words-that-are-easy-to-pick-out) - [Sam: Coping with complex language](#sam-scenario-4-coping-with-complex-language) - [Kwame: Finding the right words to use for searching](#kwame-scenario-2-finding-the-right-words-to-use-for-searching) |
| [Math Concepts](#math-concepts-user-story) | - [Provide alternatives for numerical concepts](#provide-alternatives-for-numerical-concepts-pattern)   Related Patterns   - [Enable APIs and extensions](#enable-apis-and-extensions-pattern) | - [Alison: Coping with online banking and shopping](#alison-scenario-3-coping-with-online-banking-and-shopping) - [Gopal: Managing dates and booking holidays](#gopal-scenario-1-managing-dates-and-booking-holidays) - [Jonathan: Coping with quantities when shopping online](#jonathan-scenario-1-coping-with-quantities-when-shopping-online) - [Jonathan: Spreadsheets](#jonathan-scenario-3-using-spreadsheets-shared-with-colleagues) |

### A.4 Objective 4: Help users avoid mistakes and know how to correct them

**Help users avoid mistakes.** A good design makes errors less likely. Do not ask the user for more things than you need! When errors occur, the user should find it easy to correct them.

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Assistance and Support](#assistance-and-support-user-story) | - [Ensure controls and content do not move unexpectedly](#ensure-controls-and-content-do-not-move-unexpectedly-pattern) - [Design forms to prevent mistakes](#design-forms-to-prevent-mistakes-pattern) - [Use clear visible labels](#use-clear-visible-labels-pattern) - [Accept different input formats](#accept-different-input-formats-pattern) - [Avoid data loss and “timeouts”](#avoid-data-loss-and-timeouts-pattern) - [Provide feedback](#provide-feedback-pattern) - [Notify users of fees and charges at the start of a task](#notify-users-of-fees-and-charges-at-the-start-of-a-task-pattern) - [Help the user stay safe](#help-the-user-stay-safe-pattern) - [Use familiar metrics and units](#use-familiar-metrics-and-units-pattern)   Related Patterns   - [Let users control when the content moves or changes](#let-users-control-when-the-content-moves-or-changes-pattern) - [Provide help for forms and non-standard controls](#provide-help-for-forms-and-non-standard-controls-pattern) - [Enable APIs and extensions](#enable-apis-and-extensions-pattern) | - [Alison: Learning how to use new technologies and interfaces](#alison-scenario-1-learning-how-to-use-new-technologies-and-interfaces) - [Alison: Giving feedback](#alison-scenario-4-giving-feedback) - [Tal: Logging in](#tal-scenario-1-logging-in) - [Tal: Filling in a form to ask for an online journal article](#tal-scenario-3-filling-in-a-form-to-ask-for-an-online-journal-article) - [Yuki: Losing focus when completing tasks](#yuki-scenario-3-losing-focus-when-completing-tasks) - [Gopal: Managing dates and booking holidays](#gopal-scenario-1-managing-dates-and-booking-holidays) - [George: Controls on videos and popup windows](#george-scenario-3-controls-on-videos-and-popup-windows) - [Jonathan: Coping with quantities when shopping online](#jonathan-scenario-1-coping-with-quantities-when-shopping-online) - [Maria: Pressing the correct button](#maria-scenario-3-pressing-the-correct-button) - [Sam: Using edit boxes where the instructions disappear](#sam-scenario-2-using-edit-boxes-where-the-instructions-disappear) - [Sam: Trying to activate elements that are mis-recognized](#sam-scenario-3-trying-to-activate-elements-that-are-mis-recognized) - [Kwame: Finding the right words to use for searching](#kwame-scenario-2-finding-the-right-words-to-use-for-searching) - [Kwame: Being confident that he understands the content](#kwame-scenario-3-being-confident-that-he-understands-the-content) |
| [Undo](#undo-user-story) | - [Let users go back](#let-users-go-back-pattern) - [Make it easy to undo form errors](#make-it-easy-to-undo-form-errors-pattern) | - [Alison: Learning how to use new technologies and interfaces](#alison-scenario-1-learning-how-to-use-new-technologies-and-interfaces) - [Tal: Filling in a form to ask for an online journal article](#tal-scenario-3-filling-in-a-form-to-ask-for-an-online-journal-article) - [Maria: Pressing the correct button](#maria-scenario-3-pressing-the-correct-button) |

### A.5 Objective 5: Help users focus

**Help users focus.** Avoid distracting the user from their task. If the user does get distracted, headings and breadcrumbs can help orientate the user and help the user restore the context when it is lost. Providing linked breadcrumbs can help the user undo mistakes.

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Distractions](#distractions-user-story) | - [Limit interruptions](#limit-interruptions-pattern) - [Avoid too much content](#avoid-too-much-content-pattern) - [Provide information so a user can complete and prepare for a task](#provide-information-so-a-user-can-complete-and-prepare-for-a-task-pattern) - [Make short critical paths](#make-short-critical-paths-pattern)   Related Patterns   - [Clearly state the results and disadvantages of actions, options, and selections](#clearly-state-the-results-and-disadvantages-of-actions-options-and-selections-pattern) - [Make the purpose of your page clear](#make-the-purpose-of-your-page-clear-pattern) - [Make each step clear](#make-each-step-clear-pattern) - [Use a clear and understandable page structure](#use-a-clear-and-understandable-page-structure-pattern) | - [Amy: Changing color schemes, flashing, blinking and automatic playing videos or music](#amy-scenario-2-changing-color-schemes-flashing-blinking-and-automatic-playing-videos-or-music) - [Yuki: Stopping Carousels and Banners from Scrolling](#yuki-scenario-2-stopping-carousels-and-banners-from-scrolling) - [Yuki: Losing focus when completing tasks](#yuki-scenario-3-losing-focus-when-completing-tasks) - [Gopal: Making a medical appointment](#gopal-scenario-4-making-a-medical-appointment) - [Sam: Trying to activate elements that are mis-recognized](#sam-scenario-3-trying-to-activate-elements-that-are-mis-recognized) - [Sam: Having well-spaced text with words that are easy to pick out](#sam-scenario-1-having-well-spaced-text-with-words-that-are-easy-to-pick-out) - [Kwame: Being confident that he understands the content](#kwame-scenario-3-being-confident-that-he-understands-the-content) - [Kwame: Understanding where information is in a hierarchical structure](#kwame-scenario-4-understanding-where-information-is-in-a-hierarchical-structure) - [Kwame: Cognitive overload](#kwame-scenario-5-cognitive-overload) |

### A.6 Objective 6: Ensure processes do not rely on memory

**Ensure processes do not rely on memory.** Memory barriers stop people with cognitive disabilities from using content. This includes long passwords to log in and voice menus that involve remembering a specific number or term. Make sure there is an easier option for people who need it.

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Remembering from Previous Steps](#remembering-from-previous-steps-user-story) | - [Do not rely on users calculations or memorizing information](#do-not-rely-on-users-calculations-or-memorizing-information-pattern) | - [Maria: Access to information entered during previous step in process](#maria-scenario-2-remembering-information-entered-during-a-previous-step) |
| [Accessible Authentication](#accessible-authentication-user-story) | - [Provide a login that does not rely on memory or other cognitive skills](#provide-a-login-that-does-not-rely-on-memory-or-other-cognitive-skills-pattern) - [Allow the user a simple, single step, login](#allow-the-user-a-simple-single-step-login-pattern) - [Provide a login alternative with less words](#provide-a-login-alternative-with-less-words-pattern)   Related Patterns   - [Do not rely on users calculations or memorizing information](#do-not-rely-on-users-calculations-or-memorizing-information-pattern) | - [Tal: Logging in](#tal-scenario-1-logging-in) - [Jonathan: Remembering pin numbers and passwords](#jonathan-scenario-2-remembering-pin-numbers-and-passwords) |
| [Voice Menus](#voice-menus-user-story) | - [Let users avoid navigating voice menus](#let-users-avoid-navigating-voice-menus-pattern) - [Do not rely on users calculations or memorizing information](#do-not-rely-on-users-calculations-or-memorizing-information-pattern)   Related Patterns   - [Limit interruptions](#limit-interruptions-pattern) | - [Gopal: Making a medical appointment](#gopal-scenario-4-making-a-medical-appointment) - [Maria: Access to information entered during previous step in process](#maria-scenario-2-remembering-information-entered-during-a-previous-step) |

### A.7 Objective 7: Provide help and support

**Provide help and support**. This includes:
**making it easy to get human help.** If users have difficulty sending feedback, then you will never know if they are able to use the content or when they are experiencing problems. In addition,
**support different ways to understand content.** Graphics, summaries of long documents, adding icons to headings and links, and alternatives for numbers are all examples of extra help and support.

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Help](#help-user-story) | - [Provide human help](#provide-human-help-pattern) - [Make it easy to find help and give feedback](#make-it-easy-to-find-help-and-give-feedback-pattern)   Related Patterns   - [Provide alternative content for complex information and tasks](#provide-alternative-content-for-complex-information-and-tasks-pattern) - [Provide help with directions](#provide-help-with-directions-pattern) | - [Alison: Giving feedback](#alison-scenario-4-giving-feedback) |
| [Support](#support-user-story) | - [Provide help with directions](#provide-help-with-directions-pattern) - [Provide reminders](#provide-reminders-pattern) - [Provide help for forms and non-standard controls](#provide-help-for-forms-and-non-standard-controls-pattern) - [Use icons that help the user](#use-icons-that-help-the-user-pattern) - [Provide feedback](#provide-feedback-pattern) - [Provide alternative content for complex information and tasks](#provide-alternative-content-for-complex-information-and-tasks-pattern) - [Enable APIs and extensions](#enable-apis-and-extensions-pattern)   Related Patterns   - [Support a personalized and familiar interface](#support-a-personalized-and-familiar-interface-pattern) - [Clearly state the results and disadvantages of actions, options, and selections](#clearly-state-the-results-and-disadvantages-of-actions-options-and-selections-pattern) | - [Gopal: Coping with icons that are not recognizable](#gopal-scenario-2-coping-with-icons-that-are-not-recognizable) - [George: Using symbols for communication](#george-scenario-1-using-symbols-for-communication) - [Sam: Using edit boxes where the instructions disappear](#sam-scenario-2-using-edit-boxes-where-the-instructions-disappear) |
| [Cognitive Stress](#cognitive-stress-user-story) | - [Help the user stay safe](#help-the-user-stay-safe-pattern) - [Limit interruptions](#limit-interruptions-pattern) - [Avoid too much content](#avoid-too-much-content-pattern) - [Provide information so a user can complete and prepare for a task](#provide-information-so-a-user-can-complete-and-prepare-for-a-task-pattern) - [Make short critical paths](#make-short-critical-paths-pattern) - [Clearly state the results and disadvantages of actions, options, and selections](#clearly-state-the-results-and-disadvantages-of-actions-options-and-selections-pattern) - [Make the purpose of your page clear](#make-the-purpose-of-your-page-clear-pattern) - [Make each step clear](#make-each-step-clear-pattern) - [Use a clear and understandable page structure](#use-a-clear-and-understandable-page-structure-pattern) - [Notify users of fees and charges at the start of a task](#notify-users-of-fees-and-charges-at-the-start-of-a-task-pattern) - [Separate each instruction](#separate-each-instruction-pattern) - [Use white spacing](#use-white-spacing-pattern) | - [Kwame: Being confident that he understands the content](#kwame-scenario-3-being-confident-that-he-understands-the-content) - [Kwame: Cognitive overload](#kwame-scenario-5-cognitive-overload) |
| [Task Management](#task-management-user-story) | - [Make it easy to find the most important tasks and features of the site](#make-it-easy-to-find-the-most-important-tasks-and-features-of-the-site-pattern) - [Notify users of fees and charges at the start of a task](#notify-users-of-fees-and-charges-at-the-start-of-a-task-pattern) - [Provide information so a user can complete and prepare for a task](#provide-information-so-a-user-can-complete-and-prepare-for-a-task-pattern) - [Make each step clear](#make-each-step-clear-pattern) - [Make short critical paths](#make-short-critical-paths-pattern) - [Clearly state the results and disadvantages of actions, options, and selections](#clearly-state-the-results-and-disadvantages-of-actions-options-and-selections-pattern) - [Provide help for forms and non-standard controls](#provide-help-for-forms-and-non-standard-controls-pattern) - [Provide alternative content for complex information and tasks](#provide-alternative-content-for-complex-information-and-tasks-pattern)   Related Patterns   - [Use clear visible labels](#use-clear-visible-labels-pattern) | - [Gopal: Using the heating](#gopal-scenario-5-using-the-heating). - [Jonathan: Coping with quantities when shopping online](#jonathan-scenario-1-coping-with-quantities-when-shopping-online) - [Sam: Using edit boxes where the instructions disappear](#sam-scenario-2-using-edit-boxes-where-the-instructions-disappear) - [Kwame: Being confident that he understands the content](#kwame-scenario-3-being-confident-that-he-understands-the-content) |

### A.8 Objective 8: Support adaptation and personalization

**Support adaptation and personalization.** People with cognitive and learning disabilities often use add-ons or extensions as assistive technology. Sometimes, extra support requires minimal effort from the user via personalization that allows the user to select preferred options from a set of alternatives. Support personalization when you can. Do not disable add-ons and extensions!

| User Stories | Patterns | Scenarios |
| --- | --- | --- |
| [Adapt](#adapt-user-story) | - [Let users control when the content moves or changes](#let-users-control-when-the-content-moves-or-changes-pattern) - [Support simplification](#support-simplification-pattern) - [Support a personalized and familiar interface](#support-a-personalized-and-familiar-interface-pattern)   Related Patterns   - [Use icons that help the user](#use-icons-that-help-the-user-pattern) - [Provide alternatives for numerical concepts](#provide-alternatives-for-numerical-concepts-pattern) - [Provide alternative content for complex information and tasks](#provide-alternative-content-for-complex-information-and-tasks-pattern) - [Enable APIs and extensions](#enable-apis-and-extensions-pattern) | - [Alison: Learning how to use new technologies and interfaces](#alison-scenario-1-learning-how-to-use-new-technologies-and-interfaces) - [Amy: Designs that make use of abstract imagery and metaphors](#amy-scenario-3-designs-that-make-use-of-abstract-imagery-and-metaphors) - [Gopal: Coping with icons that are not recognizable](#gopal-scenario-2-coping-with-icons-that-are-not-recognizable) - [Gopal: Using the heating](#gopal-scenario-5-using-the-heating) - [Jonathan: Coping with quantities when shopping online](#jonathan-scenario-1-coping-with-quantities-when-shopping-online) - [Jonathan: Sharing online spreadsheets with colleagues](#jonathan-scenario-3-using-spreadsheets-shared-with-colleagues) - [Sam: Trying to activate elements that are mis-recognized](#sam-scenario-3-trying-to-activate-elements-that-are-mis-recognized) |
| [Extensions and APIs](#extensions-and-apis-user-story) | - [Enable APIs and extensions](#enable-apis-and-extensions-pattern) | - [Alison: Correcting typos and writing fluently](#alison-scenario-2-correcting-typos-and-writing-fluently) - [Alison: Coping with online banking and shopping](#alison-scenario-3-coping-with-online-banking-and-shopping) - [Tal: Logging in](#tal-scenario-1-logging-in) - [Jonathan: Remembering pin numbers and passwords](#jonathan-scenario-2-remembering-pin-numbers-and-passwords) - [Kwame: Using speech recognition to navigate the Web](#kwame-scenario-1-using-speech-recognition-to-navigate-the-web) |

## B. Appendix: Considerations for Different Contexts and Policies

This Appendix provides guidance and considerations for building a policy or requirements for web content to meet the needs of individuals with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). Web content designed without consideration for the needs of individuals with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") often creates accessibility barriers for them.

Note that you can find information about general accessibility policies at [developing organizational policies on web accessibility](https://www.w3.org/WAI/planning/org-policies/).

### B.1 Why Make a Policy?

Many content providers want to reach user groups such as people with [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") and millennials with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"). This can be because:

- they have a commitment to inclusion,
- to enable growth in these high value, under-serviced, markets, and
- many services and agencies are required to use easy to understand language and to be usable by vulnerable groups.

Typically, there are many more people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") in the target audience than developers are aware of. Without a policy or requirements in place that address [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"), content providers lose this part of the target audience.

When deciding how and where to apply this document, consider how important the content is to the user. For example, web content and applications should follow as much of the advice in this document as possible, if they affect:

- individual safety concerns,
- health,
- critical services,
- autonomy,
- care-giving,
- social integration, and
- workplace needs.

It is also important to consider if content can help users save money in care-giving or cause individuals with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") to leave the workforce due to lack of appropriately designed content or interfaces.

Developing of a plan or policy can include the following steps:

1. **Define the scenarios** to be included in the policy by addressing the environments or situations in which the policy will apply.
2. **Review the different design pattern criteria and sections** and decide if they are relevant to the environmental or situational scenarios.
3. **Develop a policy** with requirements based on an analysis of the scenarios.

Policy makers should:

- Familiarize themselves with the sections of the document and design scenarios for which apply to their organizations.
- Determine how much user testing is possible, based on the scope or expense for the affected sites.
- Refer to the section on user testing for additional information and reducing costs.

**The following are examples of scenarios that may be covered by a policy:**

- Emergency services content - such as police, fire, emergency medical services, etc.
- Critical services content - such as water, health care, phone and internet services, and government services.
- Workplace content - including but not limited to professional sites and productivity tools.
- Individual content and autonomy - such as apps, interfaces to run home devices, book a cab, write an email; content that facilitates autonomy.
- General content - for widespread adoption of all web sites.

### B.2 Business Considerations

This document can help you meet the needs of underserved end-users such as:

- high net worth senior citizens, a 7.1 trillion-dollar growth market, and
- high potential impaired by [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:") and those impacted by situational impairments.

For example, one of the most reliable market projections is that the population is aging. A growing number of consumers are older. In many countries, more of the wealth lies with an older demographic.

As people age, disabilities increase. This includes [age-related forgetfulness](#dfn-age-related-forgetfulness "People with age related forgefulness have impaired memory issues that can be a normal part of healthy aging. They may take longer to learn new things, forget something but remember it later, or occasionally forget particular words. (This differs from dementia where forgetfulness is due to a disorder and is more pronounced.)") and a slower speed of learning new designs. This may make consumers feel excluded and that their needs are not considered. Accessibility can give the consumer the trust and feeling of being looked after. In contrast, if a site is difficult for people with [cognitive and learning disabilities](#dfn-cognitive-and-learning-disabilities "Cognitive disabilities and learning disabilities can mean different things in different locations. Taken together they refer to:"), the older population is likely to feel that the group is not interested in them as a market.

On the other hand, according to Georgia State University’s Center for Mature Consumer Studies, today’s mature market (those aged 55 and above) already controls 75 percent of America’s wealth and 70 percent (most) of its disposable income. Clearly, this expanding demographic is an important market for many organizations.

Additional studies have shown that the mature market is online. They may even be outpacing the use by younger user groups, when it comes to adopting new technologies and online media. However, their online needs are underserved. Research suggests that seniors manage to complete only 55.3% (about half) of attempted tasks online.

For additional information and sources see the [developer resources](https://www.w3.org/WAI/GL/task-forces/coga/wiki/Developer_resources) page. Note that more business information about general accessibility is available at [the business case for digital accessibility.](https://www.w3.org/WAI/business-case)

## C. Appendix: Change Log

The full [commit history for this document](https://github.com/w3c/coga/commits/main/content-usable) is available.

### C.1 Significant Editorial Changes since the [First Public Working Draft](https://www.w3.org/TR/2018/WD-coga-usable-20181211/)

- 2019-07-16: Added Design Guide to appendix.
- 2020-03-27: Coga TF changed the documents as follow:
  - conducted a mapping across the user needs, user stories, personas, and patterns and filled in the gaps,
  - removed duplicate content,
  - reorganized the content to focus the main portion on designers and developers and create a more cohesive flow,
  - conducted editorial cleanup (punctuation, grammar, etc) of the content to improve quality and readability,
  - added quotes to patterns and personas.
- 2020-07-13: Coga TF changed the documents as follows:
  - made the tone consistent across the document and fixed editing errors,
  - reorganized the sections to improve readability, and
  - removed appendixes that were still in process.
  - This version of document will be used for Wide Review.
- 2020-12-10: Added glossary section.
- 2021-04-21: Coga TF changed the document as follows:
  - changes to address issues from other working groups such as Education and Outreach (EO), including:
    - revised the introduction and summary,
    - revised the usability and policy sections,
    - revised the section on how to use this document,
    - improved internationalization,
    - added links to EO publications, and
    - reduced and merged appendix B and C.
  - updated the persona section to make it more diverse,
  - addressed issues and suggestions from the public, including editorial issues, clarifications, additional examples and plain language reviews and suggestions,
  - improved icons for understandability and internationalization,
  - clarified patterns and improved the consistency of their contents,
  - improved consistency of terminology and how words are used,
  - improved the consistency of user needs and stories,
  - added references and a "Language" section to the introduction.

## D. Appendix: Acknowledgments

### D.1 Key contributors, section editors and participants active in the Cognitive and Learning Disabilities Task Force at the time of publication

- Michael Cooper (W3C/MIT)
- Rachael Bradley Montgomery (Invited expert)
- Jennifer Delisi (Invited expert)
- E.A. Draffan (University of Southampton)
- David Fazio (Invited expert)
- Betsy Furler
- John Kirkwood (NYC Department of Education)
- Steve Lee (W3C/ERCIM)
- Abi James (University of Southampton)
- Justine Pascalides (Educational Testing Service)
- Ruoxi Ran (W3C/Beihang)
- John Rochford (Invited expert)
- Lisa Seeman-Horwitz (Invited expert)
- Glenda Sims (Deque Systems, Inc.)

### D.2 Significant contributors and previously active participants

- Thaddeus Cambron (Invited Expert)
- Alastair Campbell (Nomensa)
- Renaldo Bernard (University of Southampton)
- Frederick Boland
- Shari Butler (Pearson plc)
- Pietro Cirrincione (Invited expert)
- Deborah Dahl (Invited expert)
- Katherine Diebel (Invited expert)
- Chaohai Ding (University of Southampton)
- Anthony Doran (Invited expert)
- Michel Fitos (Invited expert)
- John Foliot (Invited expert)
- Katie Haritos-Shea
- Andy Heath (Invited expert)
- Joseph Karr O'Connor (Invited expert)
- Jamie Knight
- Kris Anne Kinney (Educational Testing Service)
- Dr Kinshuk (Invited expert)
- Barry Johnson (Deque Systems, Inc.)
- Katherine Mancuso (Invited expert)
- Kurt Mattes
- Jan McSorley (Pearson plc)
- Rain Breaw Michaels (Google LLC)
- Neil Milliken (Unify Software and Solutions)
- Mary Jo Mueller (IBM Corporation)
- Liddy Nevile (Invited expert)
- Allison Pelke
- Mike Pluke (Invited expert)
- Debra Ruh (Invited expert)
- Janina Sajka (Invited expert)
- Richard Schwerdtfeger (IBM Corporation)
- Ayelet Seeman (Invited expert)
- Mark Sadecki
- Leslie Tannahill
- Suzanne Taylor (Pearson plc)
- Elle Waters (Invited expert)
- Mark Wilcock (Unify Software and Solutions)

With additional thanks for significant contributions from:

- Easy Reading project (co-financed by the European Union under an EU Framework Programme for Research and Innovation – Horizon 2020, with grant agreement number 780529 and the European commission.)
- Smart4MD project (co-financed by the European Union under an EU Framework Programme for Research and Innovation – Horizon 2020, with grant agreement number 643399 and the European commission.)
- MOOCAP Erasmus + Persona CC-BY-4.0 http://gpii.eu/moocap/?page\_id=33

### D.3 Enabling funders

This publication has been funded in part with Federal funds from the U.S.
Department of Health and Human Services, National Institute on Disability
Independent Living and Rehabilitation Research (NIDILRR) under contract
HHSP23301500054. The content of this publication does not necessarily
reflect the views or official policies of the U.S. Department of Health
and Human Services, nor does mention of trade names, commercial products,
or organizations imply endorsement by the U.S. Government. Some of the
work on this project has also received funding from the European Union's
Horizon 2020 research and innovation programme under grant agreement
No.780529 and 643399.

## E. References

### E.1 Informative references

[GPII]
:   [The Global Public Inclusive Infrastructure](http://gpii.net/). URL: <http://gpii.net/>

[HTML]
:   [HTML Standard](https://html.spec.whatwg.org/multipage/). Anne van Kesteren; Domenic Denicola; Ian Hickson; Philip Jägenstedt; Simon Pieters. WHATWG. Living Standard. URL: <https://html.spec.whatwg.org/multipage/>

[HTML5]
:   [HTML5](https://www.w3.org/TR/html5/). Ian Hickson; Robin Berjon; Steve Faulkner; Travis Leithead; Erika Doyle Navara; Theresa O'Connor; Silvia Pfeiffer. W3C. 27 March 2018. W3C Recommendation. URL: <https://www.w3.org/TR/html5/>

[ISO 9241-112]
:   [Ergonomics of human-system interaction — Part 112: Principles for the presentation of information](https://www.iso.org/standard/64840.html). International Standards Organization. URL: <https://www.iso.org/standard/64840.html>

[mailto]
:   [The 'mailto' URI Scheme](https://tools.ietf.org/html/rfc6068). Internet Engineering Task Force (IETF). URL: <https://tools.ietf.org/html/rfc6068>

[personalization-semantics-1.0]
:   [Personalization Semantics 1.0](https://www.w3.org/TR/personalization-semantics-1.0/). W3C. URL: <https://www.w3.org/TR/personalization-semantics-1.0/>

[personalization-semantics-content-1.0]
:   [Personalization Semantics Content Module 1.0](https://www.w3.org/TR/personalization-semantics-content-1.0/). Lisa Seeman-Horwitz; Charles LaPierre; Michael Cooper; Ruoxi Ran; Richard Schwerdtfeger. W3C. 27 January 2020. W3C Working Draft. URL: <https://www.w3.org/TR/personalization-semantics-content-1.0/>

[personalization-semantics-help-1.0]
:   [Personalization Help and Support 1.0](https://www.w3.org/TR/personalization-semantics-help-1.0/). Lisa Seeman-Horwitz; Charles LaPierre; Michael Cooper; Ruoxi Ran; Richard Schwerdtfeger. W3C. 11 July 2019. W3C Working Draft. URL: <https://www.w3.org/TR/personalization-semantics-help-1.0/>

[Section255]
:   [Telecommunications Access for People with Disabilities](https://www.fcc.gov/consumers/guides/telecommunications-access-people-disabilities). Federal Communications Commission. URL: <https://www.fcc.gov/consumers/guides/telecommunications-access-people-disabilities>

[voicexml21]
:   [Voice Extensible Markup Language (VoiceXML) 2.1](https://www.w3.org/TR/voicexml21/). Matt Oshry; RJ Auburn; Paolo Baggia; Michael Bodell; David Burke; Daniel Burnett; Jerry Carter; Scott McGlashan; Alex Lee; Brandon Porter; Kenneth Rehor et al. W3C. 19 June 2007. W3C Recommendation. URL: <https://www.w3.org/TR/voicexml21/>

[wai-aria-1.2]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/). Joanmarie Diggs; James Nurthen; Michael Cooper. W3C. 2 March 2021. W3C Candidate Recommendation. URL: <https://www.w3.org/TR/wai-aria-1.2/>

[wai-aria-practices-1.2]
:   [WAI-ARIA Authoring Practices 1.2](https://www.w3.org/TR/wai-aria-practices-1.2/). Matthew King; JaEun Jemma Ku; James Nurthen; Zoë Bijl; Michael Cooper; Joseph Scheuhammer; Lisa Pappas; Richard Schwerdtfeger. W3C. 18 December 2019. W3C Working Draft. URL: <https://www.w3.org/TR/wai-aria-practices-1.2/>

[WCAG22]
:   [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). Charles Adams; Alastair Campbell; Rachael Bradley Montgomery; Michael Cooper; Andrew Kirkpatrick. W3C. 11 August 2020. W3C Working Draft. URL: <https://www.w3.org/TR/WCAG22/>

[webauthn-2]
:   [Web Authentication: An API for accessing Public Key Credentials - Level 2](https://www.w3.org/TR/webauthn-2/). Jeff Hodges; J.C. Jones; Michael Jones; Akshay Kumar; Emil Lundberg. W3C. 8 April 2021. W3C Recommendation. URL: <https://www.w3.org/TR/webauthn-2/>

[↑](#title)

[Permalink](#dfn-age-related-forgetfulness)

**Referenced in:**

- [§ 2. Introduction](#ref-for-dfn-age-related-forgetfulness-1 "§ 2. Introduction")
- [§ 4.2.1.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-2 "§ 4.2.1.3 How it Helps")
- [§ 4.2.3.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-3 "§ 4.2.3.3 How it Helps")
- [§ 4.2.5.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-4 "§ 4.2.5.3 How it Helps")
- [§ 4.3.6.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-5 "§ 4.3.6.3 How it Helps")
- [§ 4.5.4.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-6 "§ 4.5.4.3 How it Helps")
- [§ 4.5.7.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-7 "§ 4.5.7.3 How it Helps")
- [§ 4.5.8.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-8 "§ 4.5.8.3 How it Helps") [(2)](#ref-for-dfn-age-related-forgetfulness-9 "Reference 2")
- [§ 4.5.10.3 How it Helps](#ref-for-dfn-age-related-forgetfulness-10 "§ 4.5.10.3 How it Helps")
- [§ 5.1 Working with Users with Cognitive and Learning Disabilities](#ref-for-dfn-age-related-forgetfulness-11 "§ 5.1 Working with Users with Cognitive and Learning Disabilities")
- [§ 5.2 Finding People to Include](#ref-for-dfn-age-related-forgetfulness-12 "§ 5.2 Finding People to Include")
- [§ 5.5 Test Objectives](#ref-for-dfn-age-related-forgetfulness-13 "§ 5.5 Test Objectives")
- [§ 7. Glossary](#ref-for-dfn-age-related-forgetfulness-14 "§ 7. Glossary")
- [§ B.1 Why Make a Policy?](#ref-for-dfn-age-related-forgetfulness-15 "§ B.1 Why Make a Policy?")
- [§ B.2 Business Considerations](#ref-for-dfn-age-related-forgetfulness-16 "§ B.2 Business Considerations")

[Permalink](#dfn-alternative-and-augmentative-communication-system)

**Referenced in:**

- [§ 4.7.3.3 How it Helps](#ref-for-dfn-alternative-and-augmentative-communication-system-1 "§ 4.7.3.3 How it Helps")
- [§ 4.9.4.3 How it Helps](#ref-for-dfn-alternative-and-augmentative-communication-system-2 "§ 4.9.4.3 How it Helps") [(2)](#ref-for-dfn-alternative-and-augmentative-communication-system-3 "Reference 2")
- [§ 6.3.1 George Scenario 1: Using Symbols for Communication](#ref-for-dfn-alternative-and-augmentative-communication-system-4 "§ 6.3.1 George Scenario 1: Using Symbols for Communication")

[Permalink](#dfn-anxiety-disorders)

**Referenced in:**

- Not referenced in this document.

[Permalink](#dfn-attention-deficit-hyperactivity-disorder-ad-h-d)

**Referenced in:**

- [§ 4.2.1.3 How it Helps](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-1 "§ 4.2.1.3 How it Helps") [(2)](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-2 "Reference 2")
- [§ 4.4.5.3 How it Helps](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-3 "§ 4.4.5.3 How it Helps")
- [§ 5.2 Finding People to Include](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-4 "§ 5.2 Finding People to Include")
- [§ 6.10 Yuki: A Yoga Teacher who has AD(H)D](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-5 "§ 6.10 Yuki: A Yoga Teacher who has AD(H)D")
- [§ 7. Glossary](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-6 "§ 7. Glossary") [(2)](#ref-for-dfn-attention-deficit-hyperactivity-disorder-ad-h-d-7 "Reference 2")

[Permalink](#dfn-autistic)

**Referenced in:**

- [§ 4.4.4.3 How it Helps](#ref-for-dfn-autistic-1 "§ 4.4.4.3 How it Helps")
- [§ 4.4.12.3 How it Helps](#ref-for-dfn-autistic-2 "§ 4.4.12.3 How it Helps")
- [§ 5.1 Working with Users with Cognitive and Learning Disabilities](#ref-for-dfn-autistic-3 "§ 5.1 Working with Users with Cognitive and Learning Disabilities")
- [§ 7. Glossary](#ref-for-dfn-autistic-4 "§ 7. Glossary")

[Permalink](#dfn-brain-injury)

**Referenced in:**

- [§ 4.5.1.3 How it Helps](#ref-for-dfn-brain-injury-1 "§ 4.5.1.3 How it Helps")
- [§ 4.6.1.3 How it Helps](#ref-for-dfn-brain-injury-2 "§ 4.6.1.3 How it Helps") [(2)](#ref-for-dfn-brain-injury-3 "Reference 2")
- [§ 4.7.2.2 How it Helps](#ref-for-dfn-brain-injury-4 "§ 4.7.2.2 How it Helps")
- [§ 4.8.6.3 How it Helps](#ref-for-dfn-brain-injury-5 "§ 4.8.6.3 How it Helps")
- [§ 4.9.2.3 How it Helps](#ref-for-dfn-brain-injury-6 "§ 4.9.2.3 How it Helps")
- [§ 6.6 Kwame: A Traumatic Brain Injury Survivor](#ref-for-dfn-brain-injury-7 "§ 6.6 Kwame: A Traumatic Brain Injury Survivor")

[Permalink](#dfn-cognitive-and-learning-disabilities)

**Referenced in:**

- [§ Abstract](#ref-for-dfn-cognitive-and-learning-disabilities-1 "§ Abstract")
- [§ Help users understand what things are and how to use them.](#ref-for-dfn-cognitive-and-learning-disabilities-2 "§ Help users understand what things are and how to use them.")
- [§ Support adaptation and personalization.](#ref-for-dfn-cognitive-and-learning-disabilities-3 "§ Support adaptation and personalization.")
- [§ Test with real users!](#ref-for-dfn-cognitive-and-learning-disabilities-4 "§ Test with real users!")
- [§ 2. Introduction](#ref-for-dfn-cognitive-and-learning-disabilities-5 "§ 2. Introduction") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-6 "Reference 2") [(3)](#ref-for-dfn-cognitive-and-learning-disabilities-7 "Reference 3") [(4)](#ref-for-dfn-cognitive-and-learning-disabilities-8 "Reference 4")
- [§ 2.1 How to Use this Document](#ref-for-dfn-cognitive-and-learning-disabilities-9 "§ 2.1 How to Use this Document")
- [§ 2.1.1 Testing Each Pattern](#ref-for-dfn-cognitive-and-learning-disabilities-10 "§ 2.1.1 Testing Each Pattern")
- [§ 2.3 Building the User into the Development Process](#ref-for-dfn-cognitive-and-learning-disabilities-14 "§ 2.3 Building the User into the Development Process") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-15 "Reference 2")
- [§ 4.1 Introduction](#ref-for-dfn-cognitive-and-learning-disabilities-16 "§ 4.1 Introduction") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-17 "Reference 2") [(3)](#ref-for-dfn-cognitive-and-learning-disabilities-18 "Reference 3")
- [§ 4.2 Objective 1: Help Users Understand What Things are and How to Use Them](#ref-for-dfn-cognitive-and-learning-disabilities-19 "§ 4.2 Objective 1: Help Users Understand What Things are and How to Use Them") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-20 "Reference 2")
- [§ 4.2.1.2 What to Do](#ref-for-dfn-cognitive-and-learning-disabilities-21 "§ 4.2.1.2 What to Do")
- [§ 4.2.5.4 Getting Started](#ref-for-dfn-cognitive-and-learning-disabilities-22 "§ 4.2.5.4 Getting Started")
- [§ 4.2.6.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-23 "§ 4.2.6.3 How it Helps")
- [§ 4.3 Objective 2: Help Users Find What They Need](#ref-for-dfn-cognitive-and-learning-disabilities-24 "§ 4.3 Objective 2: Help Users Find What They Need")
- [§ 4.3.1.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-25 "§ 4.3.1.3 How it Helps")
- [§ 4.3.2.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-26 "§ 4.3.2.3 How it Helps")
- [§ 4.3.3.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-27 "§ 4.3.3.3 How it Helps")
- [§ 4.3.4.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-28 "§ 4.3.4.3 How it Helps")
- [§ 4.4.5.4 More Details](#ref-for-dfn-cognitive-and-learning-disabilities-29 "§ 4.4.5.4 More Details")
- [§ 4.4.10.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-30 "§ 4.4.10.3 How it Helps")
- [§ 4.5 Objective 4: Help Users Avoid Mistakes and Know How to Correct Them](#ref-for-dfn-cognitive-and-learning-disabilities-31 "§ 4.5 Objective 4: Help Users Avoid Mistakes and Know How to Correct Them") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-32 "Reference 2") [(3)](#ref-for-dfn-cognitive-and-learning-disabilities-33 "Reference 3") [(4)](#ref-for-dfn-cognitive-and-learning-disabilities-34 "Reference 4")
- [§ 4.5.2.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-35 "§ 4.5.2.3 How it Helps")
- [§ 4.5.3.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-36 "§ 4.5.3.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-37 "Reference 2")
- [§ 4.5.4.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-38 "§ 4.5.4.3 How it Helps")
- [§ 4.5.5.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-39 "§ 4.5.5.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-40 "Reference 2") [(3)](#ref-for-dfn-cognitive-and-learning-disabilities-41 "Reference 3") [(4)](#ref-for-dfn-cognitive-and-learning-disabilities-42 "Reference 4")
- [§ 4.5.6.2 What to Do](#ref-for-dfn-cognitive-and-learning-disabilities-43 "§ 4.5.6.2 What to Do")
- [§ 4.5.6.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-44 "§ 4.5.6.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-45 "Reference 2") [(3)](#ref-for-dfn-cognitive-and-learning-disabilities-46 "Reference 3")
- [§ 4.5.6.4 More Details](#ref-for-dfn-cognitive-and-learning-disabilities-47 "§ 4.5.6.4 More Details") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-48 "Reference 2")
- [§ 4.5.7.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-49 "§ 4.5.7.3 How it Helps")
- [§ 4.5.9.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-50 "§ 4.5.9.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-51 "Reference 2")
- [§ 4.5.10.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-52 "§ 4.5.10.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-53 "Reference 2")
- [§ 4.5.11.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-54 "§ 4.5.11.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-55 "Reference 2")
- [§ 4.6 Objective 5: Help Users Focus](#ref-for-dfn-cognitive-and-learning-disabilities-56 "§ 4.6 Objective 5: Help Users Focus")
- [§ 4.6.2.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-57 "§ 4.6.2.3 How it Helps")
- [§ 4.7.4.2 What to Do](#ref-for-dfn-cognitive-and-learning-disabilities-58 "§ 4.7.4.2 What to Do")
- [§ 4.7.4.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-59 "§ 4.7.4.3 How it Helps")
- [§ 4.7.4.6 Examples](#ref-for-dfn-cognitive-and-learning-disabilities-60 "§ 4.7.4.6 Examples")
- [§ 4.7.5.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-61 "§ 4.7.5.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-62 "Reference 2")
- [§ 4.8.2.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-63 "§ 4.8.2.3 How it Helps")
- [§ 4.8.6.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-64 "§ 4.8.6.3 How it Helps")
- [§ 4.9.1.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-65 "§ 4.9.1.3 How it Helps") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-66 "Reference 2")
- [§ 4.9.2.3 How it Helps](#ref-for-dfn-cognitive-and-learning-disabilities-67 "§ 4.9.2.3 How it Helps")
- [§ 4.9.2.4 More Details](#ref-for-dfn-cognitive-and-learning-disabilities-68 "§ 4.9.2.4 More Details")
- [§ 4.9.2.5 Getting Started](#ref-for-dfn-cognitive-and-learning-disabilities-69 "§ 4.9.2.5 Getting Started") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-70 "Reference 2")
- [§ 5.1 Working with Users with Cognitive and Learning Disabilities](#ref-for-dfn-cognitive-and-learning-disabilities-71 "§ 5.1 Working with Users with Cognitive and Learning Disabilities")
- [§ 5.2 Finding People to Include](#ref-for-dfn-cognitive-and-learning-disabilities-72 "§ 5.2 Finding People to Include") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-73 "Reference 2")
- [§ 5.4.1 Differences from Usability Testing with the General Population](#ref-for-dfn-cognitive-and-learning-disabilities-74 "§ 5.4.1 Differences from Usability Testing with the General Population")
- [§ 6. Use Cases / Personas](#ref-for-dfn-cognitive-and-learning-disabilities-75 "§ 6. Use Cases / Personas")
- [§ B. Appendix: Considerations for Different Contexts and Policies](#ref-for-dfn-cognitive-and-learning-disabilities-76 "§ B. Appendix: Considerations for Different Contexts and Policies") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-77 "Reference 2")
- [§ B.1 Why Make a Policy?](#ref-for-dfn-cognitive-and-learning-disabilities-78 "§ B.1 Why Make a Policy?") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-79 "Reference 2") [(3)](#ref-for-dfn-cognitive-and-learning-disabilities-80 "Reference 3") [(4)](#ref-for-dfn-cognitive-and-learning-disabilities-81 "Reference 4")
- [§ B.2 Business Considerations](#ref-for-dfn-cognitive-and-learning-disabilities-82 "§ B.2 Business Considerations") [(2)](#ref-for-dfn-cognitive-and-learning-disabilities-83 "Reference 2")

[Permalink](#dfn-early-stage-dementia)

**Referenced in:**

- [§ 4.2.4.3 How it Helps](#ref-for-dfn-early-stage-dementia-1 "§ 4.2.4.3 How it Helps")
- [§ 4.4.3.3 How it Helps](#ref-for-dfn-early-stage-dementia-2 "§ 4.4.3.3 How it Helps")
- [§ 4.5.6.3 How it Helps](#ref-for-dfn-early-stage-dementia-3 "§ 4.5.6.3 How it Helps")
- [§ 4.6.2.3 How it Helps](#ref-for-dfn-early-stage-dementia-4 "§ 4.6.2.3 How it Helps")
- [§ 4.6.3.3 How it Helps](#ref-for-dfn-early-stage-dementia-5 "§ 4.6.3.3 How it Helps")
- [§ 5.5 Test Objectives](#ref-for-dfn-early-stage-dementia-6 "§ 5.5 Test Objectives")

[Permalink](#dfn-easy-to-understand-language)

**Referenced in:**

- [§ 2.1 How to Use this Document](#ref-for-dfn-easy-to-understand-language-1 "§ 2.1 How to Use this Document")
- [§ 3.2.4 Media (User Story)](#ref-for-dfn-easy-to-understand-language-2 "§ 3.2.4 Media (User Story)")
- [§ 3.3.1 Clear Language (Written or Audio) (User Story)](#ref-for-dfn-easy-to-understand-language-3 "§ 3.3.1 Clear Language (Written or Audio) (User Story)")
- [§ 3.8.1 Adapt (User Story)](#ref-for-dfn-easy-to-understand-language-4 "§ 3.8.1 Adapt (User Story)")
- [§ 4.2.5.2 What to Do](#ref-for-dfn-easy-to-understand-language-5 "§ 4.2.5.2 What to Do")
- [§ 4.4 Objective 3: Use Clear and Understandable Content](#ref-for-dfn-easy-to-understand-language-6 "§ 4.4 Objective 3: Use Clear and Understandable Content")
- [§ 4.4.2.2 What to Do](#ref-for-dfn-easy-to-understand-language-7 "§ 4.4.2.2 What to Do")
- [§ 4.4.8.1 User Need](#ref-for-dfn-easy-to-understand-language-8 "§ 4.4.8.1 User Need")
- [§ 4.5.3.3 How it Helps](#ref-for-dfn-easy-to-understand-language-9 "§ 4.5.3.3 How it Helps")
- [§ 4.5.6.2 What to Do](#ref-for-dfn-easy-to-understand-language-10 "§ 4.5.6.2 What to Do")
- [§ 4.5.11.4 Examples](#ref-for-dfn-easy-to-understand-language-11 "§ 4.5.11.4 Examples") [(2)](#ref-for-dfn-easy-to-understand-language-12 "Reference 2")
- [§ 4.8.2.2 What to Do](#ref-for-dfn-easy-to-understand-language-13 "§ 4.8.2.2 What to Do")
- [§ 6.2.3 Amy Scenario 3: Designs that Make Use of Abstract Imagery and Metaphors](#ref-for-dfn-easy-to-understand-language-14 "§ 6.2.3 Amy Scenario 3: Designs that Make Use of Abstract Imagery and Metaphors")
- [§ 6.3 George: A User who Works in a Supermarket and has Down Syndrome](#ref-for-dfn-easy-to-understand-language-15 "§ 6.3 George: A User who Works in a Supermarket and has Down Syndrome")
- [§ 6.3.4 George Scenario 4: Finding Ways to Read Instructions](#ref-for-dfn-easy-to-understand-language-16 "§ 6.3.4 George Scenario 4: Finding Ways to Read Instructions")

[Permalink](#dfn-executive-function)

**Referenced in:**

- [§ 3.1.1 Clear Purpose (User Story)](#ref-for-dfn-executive-function-1 "§ 3.1.1 Clear Purpose (User Story)")
- [§ 3.1.2 Clear Operation (User Story)](#ref-for-dfn-executive-function-2 "§ 3.1.2 Clear Operation (User Story)")
- [§ 3.2.1 Findable (User Story)](#ref-for-dfn-executive-function-3 "§ 3.2.1 Findable (User Story)")
- [§ 3.2.4 Media (User Story)](#ref-for-dfn-executive-function-4 "§ 3.2.4 Media (User Story)")
- [§ 3.4.1 Assistance and Support (User Story)](#ref-for-dfn-executive-function-5 "§ 3.4.1 Assistance and Support (User Story)")
- [§ 3.6.2 Accessible Authentication (User Story)](#ref-for-dfn-executive-function-6 "§ 3.6.2 Accessible Authentication (User Story)")
- [§ 3.6.3 Voice Menus (User Story)](#ref-for-dfn-executive-function-7 "§ 3.6.3 Voice Menus (User Story)")
- [§ 3.7.5 Task Management (User Story)](#ref-for-dfn-executive-function-8 "§ 3.7.5 Task Management (User Story)")
- [§ 3.8.1 Adapt (User Story)](#ref-for-dfn-executive-function-9 "§ 3.8.1 Adapt (User Story)")
- [§ 4.3.1.3 How it Helps](#ref-for-dfn-executive-function-10 "§ 4.3.1.3 How it Helps")
- [§ 4.3.4.3 How it Helps](#ref-for-dfn-executive-function-11 "§ 4.3.4.3 How it Helps")
- [§ 4.3.6.3 How it Helps](#ref-for-dfn-executive-function-12 "§ 4.3.6.3 How it Helps")
- [§ 4.4.6.3 How it Helps](#ref-for-dfn-executive-function-13 "§ 4.4.6.3 How it Helps")
- [§ 4.5.3.3 How it Helps](#ref-for-dfn-executive-function-14 "§ 4.5.3.3 How it Helps") [(2)](#ref-for-dfn-executive-function-15 "Reference 2")
- [§ 4.5.6.3 How it Helps](#ref-for-dfn-executive-function-16 "§ 4.5.6.3 How it Helps")
- [§ 4.5.11.3 How it Helps](#ref-for-dfn-executive-function-17 "§ 4.5.11.3 How it Helps")
- [§ 4.7.2.2 How it Helps](#ref-for-dfn-executive-function-18 "§ 4.7.2.2 How it Helps")
- [§ 4.7.5.2 What to Do](#ref-for-dfn-executive-function-19 "§ 4.7.5.2 What to Do")
- [§ 4.7.5.3 How it Helps](#ref-for-dfn-executive-function-20 "§ 4.7.5.3 How it Helps")
- [§ 4.8.6.3 How it Helps](#ref-for-dfn-executive-function-21 "§ 4.8.6.3 How it Helps")
- [§ 4.9.4.3 How it Helps](#ref-for-dfn-executive-function-22 "§ 4.9.4.3 How it Helps")
- [§ 6.10 Yuki: A Yoga Teacher who has AD(H)D](#ref-for-dfn-executive-function-23 "§ 6.10 Yuki: A Yoga Teacher who has AD(H)D")
- [§ 7. Glossary](#ref-for-dfn-executive-function-24 "§ 7. Glossary") [(2)](#ref-for-dfn-executive-function-25 "Reference 2")

[Permalink](#dfn-interactive-voice-response)

**Referenced in:**

- [§ 4.8.5.2 What to Do](#ref-for-dfn-interactive-voice-response-1 "§ 4.8.5.2 What to Do")
- [§ 4.8.5.5 Examples](#ref-for-dfn-interactive-voice-response-2 "§ 4.8.5.5 Examples")

[Permalink](#dfn-memory-impairment)

**Referenced in:**

- [§ 3.6.2 Accessible Authentication (User Story)](#ref-for-dfn-memory-impairment-1 "§ 3.6.2 Accessible Authentication (User Story)")
- [§ 3.6.3 Voice Menus (User Story)](#ref-for-dfn-memory-impairment-2 "§ 3.6.3 Voice Menus (User Story)")
- [§ 4.7.1.3 How it Helps](#ref-for-dfn-memory-impairment-3 "§ 4.7.1.3 How it Helps")
- [§ 4.7.4.2 What to Do](#ref-for-dfn-memory-impairment-4 "§ 4.7.4.2 What to Do")
- [§ 4.7.5.4 More Details](#ref-for-dfn-memory-impairment-5 "§ 4.7.5.4 More Details")
- [§ 4.9.2.3 How it Helps](#ref-for-dfn-memory-impairment-6 "§ 4.9.2.3 How it Helps")
- [§ 5.3 Informed Consent](#ref-for-dfn-memory-impairment-7 "§ 5.3 Informed Consent")

[Permalink](#dfn-mental-health)

**Referenced in:**

- [§ 2.2 Background about People with Cognitive and Learning Disabilities, Accessibility and the Web](#ref-for-dfn-mental-health-1 "§ 2.2 Background about People with Cognitive and Learning Disabilities, Accessibility and the Web")
- [§ 2.3 Building the User into the Development Process](#ref-for-dfn-mental-health-2 "§ 2.3 Building the User into the Development Process")
- [§ 3. User Stories](#ref-for-dfn-mental-health-3 "§ 3. User Stories")
- [§ 4.6.1.3 How it Helps](#ref-for-dfn-mental-health-4 "§ 4.6.1.3 How it Helps")

[Permalink](#dfn-mild-cognitive-impairment-mci)

**Referenced in:**

- [§ 4.2.2.3 How it Helps](#ref-for-dfn-mild-cognitive-impairment-mci-1 "§ 4.2.2.3 How it Helps")

[Permalink](#dfn-neurodiversity)

**Referenced in:**

- [§ Abstract](#ref-for-dfn-neurodiversity-1 "§ Abstract")

[Permalink](#dfn-voice-user-interfaces)

**Referenced in:**

- [§ 4.7.4.4 More Details](#ref-for-dfn-voice-user-interfaces-1 "§ 4.7.4.4 More Details") [(2)](#ref-for-dfn-voice-user-interfaces-2 "Reference 2") [(3)](#ref-for-dfn-voice-user-interfaces-3 "Reference 3") [(4)](#ref-for-dfn-voice-user-interfaces-4 "Reference 4") [(5)](#ref-for-dfn-voice-user-interfaces-5 "Reference 5") [(6)](#ref-for-dfn-voice-user-interfaces-6 "Reference 6")
- [§ 4.8.1.4 Examples](#ref-for-dfn-voice-user-interfaces-7 "§ 4.8.1.4 Examples")
- [§ 4.8.5.5 Examples](#ref-for-dfn-voice-user-interfaces-8 "§ 4.8.5.5 Examples")

(() => {
// @ts-check
if (document.respec) {
document.respec.ready.then(setupPanel);
} else {
setupPanel();
}
function setupPanel() {
const listener = panelListener();
document.body.addEventListener("keydown", listener);
document.body.addEventListener("click", listener);
}
function panelListener() {
/\*\* @type {HTMLElement} \*/
let panel = null;
return event => {
const { target, type } = event;
if (!(target instanceof HTMLElement)) return;
// For keys, we only care about Enter key to activate the panel
// otherwise it's activated via a click.
if (type === "keydown" && event.key !== "Enter") return;
const action = deriveAction(event);
switch (action) {
case "show": {
hidePanel(panel);
/\*\* @type {HTMLElement} \*/
const dfn = target.closest("dfn, .index-term");
panel = document.getElementById(`dfn-panel-for-${dfn.id}`);
const coords = deriveCoordinates(event);
displayPanel(dfn, panel, coords);
break;
}
case "dock": {
panel.style.left = null;
panel.style.top = null;
panel.classList.add("docked");
break;
}
case "hide": {
hidePanel(panel);
panel = null;
break;
}
}
};
}
/\*\*
\* @param {MouseEvent|KeyboardEvent} event
\*/
function deriveCoordinates(event) {
const target = /\*\* @type HTMLElement \*/ (event.target);
// We prevent synthetic AT clicks from putting
// the dialog in a weird place. The AT events sometimes
// lack coordinates, so they have clientX/Y = 0
const rect = target.getBoundingClientRect();
if (
event instanceof MouseEvent &&
event.clientX >= rect.left &&
event.clientY >= rect.top
) {
// The event probably happened inside the bounding rect...
return { x: event.clientX, y: event.clientY };
}
// Offset to the middle of the element
const x = rect.x + rect.width / 2;
// Placed at the bottom of the element
const y = rect.y + rect.height;
return { x, y };
}
/\*\*
\* @param {Event} event
\*/
function deriveAction(event) {
const target = /\*\* @type {HTMLElement} \*/ (event.target);
const hitALink = !!target.closest("a");
if (target.closest("dfn:not([data-cite]), .index-term")) {
return hitALink ? "none" : "show";
}
if (target.closest(".dfn-panel")) {
if (hitALink) {
return target.classList.contains("self-link") ? "hide" : "dock";
}
const panel = target.closest(".dfn-panel");
return panel.classList.contains("docked") ? "hide" : "none";
}
if (document.querySelector(".dfn-panel:not([hidden])")) {
return "hide";
}
return "none";
}
/\*\*
\* @param {HTMLElement} dfn
\* @param {HTMLElement} panel
\* @param {{ x: number, y: number }} clickPosition
\*/
function displayPanel(dfn, panel, { x, y }) {
panel.hidden = false;
// distance (px) between edge of panel and the pointing triangle (caret)
const MARGIN = 20;
const dfnRects = dfn.getClientRects();
// Find the `top` offset when the `dfn` can be spread across multiple lines
let closestTop = 0;
let minDiff = Infinity;
for (const rect of dfnRects) {
const { top, bottom } = rect;
const diffFromClickY = Math.abs((top + bottom) / 2 - y);
if (diffFromClickY < minDiff) {
minDiff = diffFromClickY;
closestTop = top;
}
}
const top = window.scrollY + closestTop + dfnRects[0].height;
const left = x - MARGIN;
panel.style.left = `${left}px`;
panel.style.top = `${top}px`;
// Find if the panel is flowing out of the window
const panelRect = panel.getBoundingClientRect();
const SCREEN\_WIDTH = Math.min(window.innerWidth, window.screen.width);
if (panelRect.right > SCREEN\_WIDTH) {
const newLeft = Math.max(MARGIN, x + MARGIN - panelRect.width);
const newCaretOffset = left - newLeft;
panel.style.left = `${newLeft}px`;
/\*\* @type {HTMLElement} \*/
const caret = panel.querySelector(".caret");
caret.style.left = `${newCaretOffset}px`;
}
// As it's a dialog, we trap focus.
// TODO: when <dialog> becomes a implemented, we should really
// use that.
trapFocus(panel, dfn);
}
/\*\*
\* @param {HTMLElement} panel
\* @param {HTMLElement} dfn
\* @returns
\*/
function trapFocus(panel, dfn) {
/\*\* @type NodeListOf<HTMLAnchorElement> elements \*/
const anchors = panel.querySelectorAll("a[href]");
// No need to trap focus
if (!anchors.length) return;
// Move focus to first anchor element
const first = anchors.item(0);
first.focus();
const trapListener = createTrapListener(anchors, panel, dfn);
panel.addEventListener("keydown", trapListener);
// Hiding the panel releases the trap
const mo = new MutationObserver(records => {
const [record] = records;
const target = /\*\* @type HTMLElement \*/ (record.target);
if (target.hidden) {
panel.removeEventListener("keydown", trapListener);
mo.disconnect();
}
});
mo.observe(panel, { attributes: true, attributeFilter: ["hidden"] });
}
/\*\*
\*
\* @param {NodeListOf<HTMLAnchorElement>} anchors
\* @param {HTMLElement} panel
\* @param {HTMLElement} dfn
\* @returns
\*/
function createTrapListener(anchors, panel, dfn) {
const lastIndex = anchors.length - 1;
let currentIndex = 0;
return event => {
switch (event.key) {
// Hitting "Tab" traps us in a nice loop around elements.
case "Tab": {
event.preventDefault();
currentIndex += event.shiftKey ? -1 : +1;
if (currentIndex < 0) {
currentIndex = lastIndex;
} else if (currentIndex > lastIndex) {
currentIndex = 0;
}
anchors.item(currentIndex).focus();
break;
}
// Hitting "Enter" on an anchor releases the trap.
case "Enter":
hidePanel(panel);
break;
// Hitting "Escape" returns focus to dfn.
case "Escape":
hidePanel(panel);
dfn.focus();
return;
}
};
}
/\*\* @param {HTMLElement} panel \*/
function hidePanel(panel) {
if (!panel) return;
panel.hidden = true;
panel.classList.remove("docked");
}
})()