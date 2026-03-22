---
ai_context: WCAG2ICT interpretations for Principles 3 and 4 in non-web documents and
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
- understandable
- robust
- guideline-comments
title: 'WCAG2ICT 2.2 Guideline Comments: Understandable and Robust'
---

# WCAG2ICT 2.2 Guideline Comments: Understandable and Robust

## Guideline Comments for Principles 3 and 4

### 3. Understandable

> Information and the operation of the user interface must be understandable.

#### Applying Principle 3 Understandable to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 3 applies directly as written.

#### 3.1 Readable

> Make text content readable and understandable.

##### Applying Guideline 3.1 Readable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 3.1 applies directly as written.

##### 3.1.1 Language of Page

(Level A)

> The default [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s "language that is spoken, written or signed (through visual or tactile means) to communicate with humans") of each [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities").

###### Applying SC 3.1.1 Language of Page to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.1.1](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page#intent) replacing “each web page” with “non-web documents or software”.

With this substitution, it would read:

**3.1.1 Language of Page:** The default [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s) of [**[non-web documents](#document)** or **[software](#software)**] can be [programmatically determined](#dfn-programmatically-determinable).

Note 1 (Added) (for non-web software)

Where software platforms provide a “locale / language” setting, applications that use that setting and render their interface in that “locale / language” would satisfy this success criterion. Applications that do not use the platform “locale / language” setting but instead use an [accessibility-supported](#dfn-accessibility-supported) method for exposing the human language of the [non-web software](#software) would also satisfy this success criterion. Applications implemented in technologies where [assistive technologies](#dfn-assistive-technologies) cannot determine the human language and that do not support the platform “locale / language” setting may not be able to satisfy this success criterion in that locale / language.

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 3.1.2 Language of Parts

(Level AA)

> The [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s "language that is spoken, written or signed (through visual or tactile means) to communicate with humans") of each passage or phrase in the content can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") except for proper names, technical terms, words of indeterminate language, and words
> or phrases that have become part of the vernacular of the immediately surrounding
> [text](https://www.w3.org/TR/WCAG22/#dfn-text "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language").

###### Applying SC 3.1.2 Language of Parts to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.1.2](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts#intent) replacing “content” with “non-web document or software”.

With this substitution, it would read:

**3.1.2 Language of Parts:** The [human language](https://www.w3.org/TR/WCAG22/#dfn-human-language-s) of each passage or phrase in the [**[non-web document](#document)** or **[software](#software)**] can be [programmatically determined](#dfn-programmatically-determinable) except for proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the immediately surrounding [text](https://www.w3.org/TR/WCAG22/#dfn-text).

Note 1 (Added)

Examples of programmatic identification include language metadata or markup. There are some [non-web software](#software) and [non-web document](#document) technologies where there is no assistive technology supported method for marking the language for the different passages or phrases in the non-web document or software, and it would not be possible to satisfy this success criterion with those technologies.

Note 2 (Added) (for non-web documents)

Inheritance is one common method. For example, where the primary language of a non-web document is programmatically determinable, it can be assumed that all of the text or user interface elements within that document will be using the same language unless it is indicated.

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

#### 3.2 Predictable

> Make web pages appear and operate in predictable ways.

##### Applying Guideline 3.2 Predictable to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 3.2 applies directly as written, replacing “web pages” with “non-web documents or software”.

With this substitution, it would read:

**Guideline 3.2 Predictable:** Make [**[non-web documents](#document)** or **[software](#software)**] appear and operate in predictable ways.

##### 3.2.1 On Focus

(Level A)

> When any [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") receives focus, it does not initiate a [change of context](https://www.w3.org/TR/WCAG22/#dfn-change-of-context "major changes that, if made without user awareness, can disorient users who are not able to view the entire page simultaneously").

###### Applying SC 3.2.1 On Focus to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.2.1](https://www.w3.org/WAI/WCAG22/Understanding/on-focus#intent).

Note (Added)

Some compound documents and their user agents are designed to provide significantly different viewing and editing functionality depending upon what portion of the compound document is being interacted with (e.g. a presentation that contains an embedded spreadsheet, where the menus and toolbars of the user agent change depending upon whether the user is interacting with the presentation content, or the embedded spreadsheet content). If the user uses a mechanism other than putting focus on that portion of the compound document with which they mean to interact (e.g. by a menu choice or special keyboard gesture), any resulting [change of context](#dfn-change-of-context) wouldn't be subject to this success criterion because it was not caused by a change of focus.

##### 3.2.2 On Input

(Level A)

> Changing the setting of any [user interface component](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") does not automatically cause a [change of context](https://www.w3.org/TR/WCAG22/#dfn-change-of-context "major changes that, if made without user awareness, can disorient users who are not able to view the entire page simultaneously") unless the user has been advised of the behavior before using the component.

###### Applying SC 3.2.2 On Input to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.2.2](https://www.w3.org/WAI/WCAG22/Understanding/on-input#intent).

##### 3.2.3 Consistent Navigation

(Level AA)

> Navigational mechanisms that are repeated on multiple [web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization") occur in the [same relative order](https://www.w3.org/TR/WCAG22/#dfn-same-relative-order "same position relative to other items") each time they are repeated, unless a change is initiated by the user.

###### Applying SC 3.2.3 Consistent Navigation to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 3.2.3](https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation#intent), replacing "on multiple web pages within a set of web pages" with "in multiple non-web documents within a set of non-web documents, or in multiple non-web software programs within a set of software programs”.

With these substitutions, it would read:

**3.2.3 Consistent Navigation:** Navigational mechanisms that are repeated [in multiple **[non-web documents](#document)** within a **[set of non-web documents](#set-of-documents)**, or in multiple **[software programs](#software)** within a **[set of software programs](#set-of-software-programs)**] occur in the [same relative order](https://www.w3.org/TR/WCAG22/#dfn-same-relative-order) each time they are repeated, unless a change is initiated by the user.

Note 1 (Added)

See [set of documents](#set-of-documents) and [set of software programs](#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

Although not required by this success criterion, ensuring that navigation elements have consistent order when repeated within non-web documents or software programs directly addresses user needs identified in the Intent section for this success criterion, and is generally considered best practice.

Note 3 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 3.2.4 Consistent Identification

(Level AA)

> Components that have the [same functionality](https://www.w3.org/TR/WCAG22/#dfn-same-functionality "same result when used") within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization") are identified consistently.

###### Applying SC 3.2.4 Consistent Identification to Non-Web Documents and Software

This applies directly as written and described in [Intent from Understanding Success Criterion 3.2.4](https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification#intent), replacing “set of web pages” with “set of non-web documents or a set of software programs”.

With these substitutions, it would read:

**3.2.4 Consistent Identification:** Components that have the [same functionality](#dfn-same-functionality) within a [**[set of non-web documents](#set-of-documents)** or a **[set of software programs](#set-of-software-programs)**] are identified consistently.

Note 1 (Added)

See [set of documents](#set-of-documents) and [set of software programs](#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](#interpretation-of-web-terminology-in-a-non-web-context).

Note 2 (Added)

Although not required by this success criterion, ensuring that component identification be consistent when they occur more than once *within* non-web documents or software programs directly addresses user needs identified in the Intent section for this success criterion, and is generally considered best practice.

Note 3 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 3.2.6 Consistent Help

(Level A)

> If a [web page](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") contains any of the following help [mechanisms](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result"), and those mechanisms are repeated on multiple web pages within a [set of web pages](https://www.w3.org/TR/WCAG22/#dfn-set-of-web-pages "collection of web pages that share a common purpose and that are created by the same author, group or organization"), they occur in the same order relative to other page content, unless a change is initiated by the user:
>
> - Human contact details;
> - Human contact mechanism;
> - Self-help option;
> - A fully automated contact mechanism.
>
> Note 1
>
> Help mechanisms may be provided directly on the page, or may be provided via a direct link to a different page containing the information.
>
> Note 2
>
> For this success criterion, "the same order relative to other page content" can be thought of as how the content is ordered when the page is serialized. The visual position of a help mechanism is likely to be consistent across pages for the same page variation (e.g., CSS break-point). The user can initiate a change, such as changing the page's zoom or orientation, which may trigger a different page variation. This criterion is concerned with relative order across pages displayed in the same page variation (e.g., same zoom level and orientation).

###### Applying SC 3.2.6 Consistent Help to Non-Web Documents and Software

This applies directly as written and as described in [Intent from Understanding Success Criterion 3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help#intent), replacing "web page(s)" and "page(s)" with "non-web document(s) or software program(s)", "set of web pages" with "set of non-web documents or set of software programs", "page content" with "content", "on the page" with "in the non-web document or software", "page is serialized" with "non-web document or software content is serialized", "different page" with "different non-web document, software, or web page", and "page variation" with "content layout variation".

With these substitutions, it would read:

**3.2.6 Consistent Help:** If a [**[non-web document](#document)** or **[software](#software)**] contains any of the following help [mechanisms](https://www.w3.org/TR/WCAG22/#dfn-mechanism), and those mechanisms are repeated [in multiple non-web documents or software] within a [**[set of non-web documents](#set-of-documents)** or **[set of software programs](#set-of-software-programs)**], they occur in the same order relative to other [**[content](#content-on-and-off-the-web)**], unless a change is initiated by the user:

- Human contact details;
- Human contact mechanism;
- Self-help option;
- A fully automated contact mechanism

Note 1

Help mechanisms may be provided directly [in the non-web document or software], or may be provided via a direct link to a [different non-web document, software, or web page] containing the information.

Note 2

For this success criterion, "the same order relative to other [content]" can be thought of as how the content is ordered when the [non-web document or software content is serialized]. The visual position of a help mechanism is likely to be consistent across [non-web documents or software] for the same [content layout variation] (e.g., CSS break-point). The user can initiate a change, such as changing the [non-web document’s or software's] zoom or orientation, which may trigger a different [content layout variation]. This criterion is concerned with relative order across [non-web documents or software] displayed in the same [content layout variation] (e.g., same zoom level and orientation).

Note 3 (Added)

See [set of documents](#set-of-documents) and [set of software programs](#set-of-software-programs) in the Key Terms section to determine when a group of documents or software programs is considered a set for this success criterion. Those implementing this document (WCAG2ICT) will need to consider if this success criterion is appropriate to apply to non-web documents and software. See the [Interpretation of Web Terminology in a Non-web Context](#interpretation-of-web-terminology-in-a-non-web-context).

Note 4 (Added) (for non-web software)

Sets of software that meet this definition appear to be extremely rare.

#### 3.3 Input Assistance

> Help users avoid and correct mistakes.

##### Applying Guideline 3.3 Input Assistance to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 3.3 applies directly as written.

##### 3.3.1 Error Identification

(Level A)

> If an [input error](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") is automatically detected, the item that is in error is identified and the error
> is described to the user in text.

###### Applying SC 3.3.1 Error Identification to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification#intent).

Note (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 3.3.2 Labels or Instructions

(Level A)

> [Labels](https://www.w3.org/TR/WCAG22/#dfn-labels "text or other component with a text alternative that is presented to a user to identify a component within web content") or instructions are provided when content requires user input.

###### Applying SC 3.3.2 Labels or Instructions to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.2](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions#intent).

##### 3.3.3 Error Suggestion

(Level AA)

> If an [input error](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") is automatically detected and suggestions for correction are known, then the suggestions
> are provided to the user, unless it would jeopardize the security or purpose of the
> content.

###### Applying SC 3.3.3 Error Suggestion to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion#intent).

##### 3.3.4 Error Prevention (Legal, Financial, Data)

(Level AA)

> For [web pages](https://www.w3.org/TR/WCAG22/#dfn-web-page-s "a non-embedded resource obtained from a single URI using HTTP plus any other resources that are used in the rendering or intended to be rendered together with it by a user agent") that cause [legal commitments](https://www.w3.org/TR/WCAG22/#dfn-legal-commitments "transactions where the person incurs a legally binding obligation or benefit") or financial transactions for the user to occur, that modify or delete [user-controllable](https://www.w3.org/TR/WCAG22/#dfn-user-controllable "data that is intended to be accessed by users") data in data storage systems, or that submit user test responses, at least one of
> the following is true:
>
> Reversible
> :   Submissions are reversible.
>
> Checked
> :   Data entered by the user is checked for [input errors](https://www.w3.org/TR/WCAG22/#dfn-input-error "information provided by the user that is not accepted") and the user is provided an opportunity to correct them.
>
> Confirmed
> :   A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available for reviewing, confirming, and correcting information before finalizing the submission.

###### Applying SC 3.3.4 Error Prevention (Legal, Financial, Data) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.4](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data#intent) replacing “web pages” with “non-web documents or software”.

With this substitution, it would read:

**3.3.4 Error Prevention (Legal, Financial, Data):** For [**[non-web documents](#document)** or **[software](#software)**] that cause [legal commitments](https://www.w3.org/TR/WCAG22/#dfn-legal-commitments) or financial transactions for the user to occur, that modify or delete [user-controllable](https://www.w3.org/TR/WCAG22/#dfn-user-controllable) data in data storage systems, or that submit user test responses, at least one of the following is true:

Reversible
:   Submissions are reversible.

Checked
:   Data entered by the user is checked for input errors and the user is provided an opportunity to correct them.

Confirmed
:   A mechanism is available for reviewing, confirming, and correcting information before finalizing the submission.

##### 3.3.7 Redundant Entry

(Level A)

> Information previously entered by or provided to the user that is required to be entered again in the same [process](https://www.w3.org/TR/WCAG22/#dfn-processes "series of user actions where each action is required in order to complete an activity") is either:
>
> - auto-populated, or
> - available for the user to select.
>
> Except when:
>
> - re-entering the information is [essential](https://www.w3.org/TR/WCAG22/#dfn-essential "if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform"),
> - the information is required to ensure the security of the content, or
> - previously entered information is no longer valid.

###### Applying SC 3.3.7 Redundant Entry to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry#intent).

##### 3.3.8 Accessible Authentication (Minimum)

(Level AA)

> A [cognitive function test](https://www.w3.org/TR/WCAG22/#dfn-cognitive-function-test "New") (such as remembering a password or solving a puzzle) is not required for any step in an authentication [process](https://www.w3.org/TR/WCAG22/#dfn-processes "series of user actions where each action is required in order to complete an activity") unless that step provides at least one of the following:
>
> Alternative
> :   Another authentication method that does not rely on a cognitive function test.
>
> Mechanism
> :   A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism "process or technique for achieving a result") is available to assist the user in completing the cognitive function test.
>
> Object Recognition
> :   The cognitive function test is to recognize objects.
>
> Personal Content
> :   The cognitive function test is to identify [non-text content](https://www.w3.org/TR/WCAG22/#dfn-non-text-content "any content that is not a sequence of characters that can be programmatically determined or where the sequence is not expressing something in human language") the user provided to the website.
>
> Note 1
>
> "Object recognition" and "Personal content" may be represented by images, video, or audio.
>
> Note 2
>
> Examples of mechanisms that satisfy this criterion include:
>
> - support for password entry by password managers to reduce memory need, and
> - copy and paste to reduce the cognitive burden of re-typing.

###### Applying SC 3.3.8 Accessible Authentication (Minimum) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html), replacing “the website” with “a website, non-web document, or software”.

With this substitution, it would read:

**3.3.8 Accessible Authentication (Minimum):** A [cognitive function test](#dfn-cognitive-function-test) (such as remembering a password or solving a puzzle) is not required for any step in an authentication [process](https://www.w3.org/TR/WCAG22/#dfn-processes) unless that step provides at least one of the following:

Alternative
:   Another authentication method that does not rely on a cognitive function test.

Mechanism
:   A [mechanism](https://www.w3.org/TR/WCAG22/#dfn-mechanism) is available to assist the user in completing the cognitive function test.

Object Recognition
:   The cognitive function test is to recognize objects.

Personal Content
:   The cognitive function test is to identify [non-text content](https://www.w3.org/TR/WCAG22/#dfn-non-text-content) the user provided to [a website, **[non-web document](#document)**, or **[software](#software)**].

Note 1

"Object recognition" and "Personal content" may be represented by images, video, or audio.

Note 2

Examples of mechanisms that satisfy this criterion include:

1. support for password entry by password managers to reduce memory need, and
2. copy and paste to reduce the cognitive burden of re-typing.

Note 3 (Added) (for non-web software)

Any passwords used to unlock underlying [platform software](#platform-software) (running below the non-web software) are out of scope for this requirement since these are not under control of the non-web software’s author.

Note 4 (Added) (for non-web software)

There are cases where non-web software has an authentication process and no alternative or assistance mechanism is feasible, for example when entering a password when starting, powering on / turning on an ICT (device or otherwise). In such situations, it may not be possible for the non-web software to satisfy this success criterion.

Note 5 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

### 4. Robust

> Content must be robust enough that it can be interpreted by a wide variety of user agents, including assistive technologies.

#### Applying Principle 4 Robust to Non-Web Documents and Software

In WCAG 2, the Principles are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Principle 4 applies directly as written replacing “user agents, including assistive technologies” with “assistive technologies and accessibility features of software”.

With this substitution, it would read:

**Principle 4 Robust:** Content must be robust enough that it can be interpreted by a wide variety of [**[assistive technologies](#dfn-assistive-technologies)** and accessibility features of software].

#### 4.1 Compatible

> Maximize compatibility with current and future user agents, including assistive technologies.

##### Applying Guideline 4.1 Compatible to Non-Web Documents and Software

In WCAG 2, the Guidelines are provided for framing and understanding the success criteria under them but are not used for conformance to WCAG. Guideline 4.1 applies directly as written, replacing “user agents, including assistive technologies” with “assistive technologies and accessibility features of software”.

With this substitution, it would read:

**Guideline 4.1 Compatible:** Maximize compatibility with current and future [**[assistive technologies](#dfn-assistive-technologies)** and accessibility features of software].

##### 4.1.1 Parsing (WCAG 2.1)

(Level A)

> In content implemented using markup languages, elements have complete start and end
> tags, elements are nested according to their specifications, elements do not contain
> duplicate attributes, and any IDs are unique, except where the specifications allow
> these features.
>
> Note 1
>
> This success criterion should be considered as always satisfied for any content using HTML or XML.
>
> Note 2
>
> Since this criterion was written, the HTML Living Standard has adopted specific requirements governing how user agents must handle incomplete tags, incorrect element nesting, duplicate attributes, and non-unique IDs. [[HTML](https://www.w3.org/TR/WCAG21/#bib-html "HTML Standard")]
>
> Although the HTML standard treats some of these cases as non-conforming for authors, it is considered to "allow these features" for the purposes of this success criterion because the specification requires that user agents support handling these cases consistently. In practice, this criterion no longer provides any benefit to people with disabilities in itself.
>
> Issues such as missing roles due to inappropriately nested elements or incorrect states or names due to a duplicate ID are covered by different success criteria and should be reported under those criteria rather than as issues with 4.1.1.

###### Applying SC 4.1.1 Parsing (WCAG 2.0 and 2.1) to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 4.1.1](https://www.w3.org/WAI/WCAG21/Understanding/parsing#intent), replacing “In content implemented using markup languages” with “For non-web documents or software that use markup languages, in such a way that the markup is separately exposed and available to assistive technologies and accessibility features of software or to a user-selectable user agent” and replacing the WCAG notes with notes applicable to non-web documents and software.

With this substitution, it would read:

**4.1.1 Parsing:** [For **[non-web documents](#document)** or **[software](#software)** that use markup languages, in such a way that the markup is separately exposed and available to **[assistive technologies](#dfn-assistive-technologies)** and accessibility features of software or to a user-selectable **[user agent](#user-agent)**], elements have complete start and end tags, elements are nested according to their specifications, elements do not contain duplicate attributes, and any IDs are unique, except where the specifications allow these features.

Note 1 (Added)

Markup is not always available to [assistive technologies](#dfn-assistive-technologies) or to user selectable [user agents](#user-agent) such as browsers. Software sometimes uses markup languages internally for persistence of the software user interface, in ways where the markup is never available to assistive technology (either directly or through a document object model (DOM)), or to a user agent (such as a browser). In such cases, conformance to this provision would have no impact on accessibility as it can have for web content where it is exposed.

Accessibility issues introduced through poor markup would surface as errors in the programmatic information and would be reported using success criteria that rely on that information, such as 1.3.1 Info and Relationships and 4.1.2 Name, Role, Value.

Note 2 (Added)

This success criterion would be satisfied in cases where:

- Content is implemented using HTML or XML (as outlined in the [WCAG 2.1 note on 4.1.1](https://www.w3.org/TR/WCAG21/#h-note-27) and the [WCAG 2.0 editorial errata](https://www.w3.org/WAI/WCAG20/errata/#editorial) in the thirteenth list item)
- Non-web documents or software are not authored using a markup language.
- Non-web documents or software are authored using a markup language, but accessibility information is exposed via platform accessibility APIs, not by making the markup itself available to assistive technologies.

Example (Added): Examples where 4.1.1 Parsing would be satisfied:

- An HTML page embedded inside a desktop application (as outlined in the [WCAG 2.1 note on 4.1.1](https://www.w3.org/TR/WCAG21/#h-note-27) and the [WCAG 2.0 editorial errata](https://www.w3.org/WAI/WCAG20/errata/#editorial) in the thirteenth list item)
- A PDF document (not authored using a markup language)
- Android or iOS apps which use a markup language to specify UI layout (accessibility information is exposed via platform accessibility APIs, not the markup)

Examples of markup that might be separately exposed and available to assistive technologies and to user agents include:

- LaTeX documents
- Markdown documents

Note 3 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 4.1.1 Parsing (WCAG 2.2)

(Obsolete and removed)

> Note
>
> This criterion was originally adopted to address problems that assistive technology had directly parsing HTML. Assistive technology no longer has any need to directly parse HTML. Consequently, these problems either no longer exist or are addressed by other criteria. This criterion no longer has utility and is removed.

###### Applying SC 4.1.1 Parsing (Obsolete and removed) (WCAG 2.2) to Non-Web Documents and Software

Note (Added)

WCAG 2.2 has made this success criterion obsolete and removed it as a requirement in the standard. Therefore, the interpretation of this success criterion for [non-web documents](#document) and [software](#software) has been removed.

##### 4.1.2 Name, Role, Value

(Level A)

> For all [user interface components](https://www.w3.org/TR/WCAG22/#dfn-user-interface-components "a part of the content that is perceived by users as a single control for a distinct function") (including but not limited to: form elements, links and components generated by scripts),
> the [name](https://www.w3.org/TR/WCAG22/#dfn-name "text by which software can identify a component within web content to the user") and [role](https://www.w3.org/TR/WCAG22/#dfn-role "text or number by which software can identify the function of a component within Web content") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities"); [states](https://www.w3.org/TR/WCAG22/#dfn-states "dynamic property expressing characteristics of a user interface component that may change in response to user action or automated processes"), properties, and values that can be set by the user can be [programmatically set](https://www.w3.org/TR/WCAG22/#dfn-programmatically-set "set by software using methods that are supported by user agents, including assistive technologies"); and notification of changes to these items is available to [user agents](https://www.w3.org/TR/WCAG22/#dfn-user-agents "any software that retrieves and presents web content for users"), including [assistive technologies](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents").
>
> Note
>
> This success criterion is primarily for web authors who develop or script their own
> user interface components. For example, standard HTML controls already meet this success
> criterion when used according to specification.

###### Applying SC 4.1.2 Name, Role, Value to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value#intent), replacing “user agents, including assistive technologies", with “assistive technologies and accessibility features of underlying software” and the note with: “This success criterion is primarily for software developers who develop or use custom user interface components. For example, standard user interface components on most accessibility-supported platforms already satisfy this success criterion when used according to specification.”

With this substitution, it would read:

**4.1.2 Name, Role, Value:** For all [user interface components](#dfn-user-interface-components) (including but not limited to: form elements, links and components generated by scripts), the [name](#dfn-name) and [role](#dfn-role) can be [programmatically determined](#dfn-programmatically-determinable); [states](https://www.w3.org/TR/WCAG22/#dfn-states), properties, and values that can be set by the user can be [programmatically set](#dfn-programmatically-set); and notification of changes to these items is available to [**[assistive technologies](#dfn-assistive-technologies)** and accessibility features of underlying **[software](#software)**].

Note 1 (Added) (for non-web documents)

For non-web document formats that support interoperability with assistive technology, standard user interface components often satisfy this success criterion when used according to the general design and accessibility guidance for the document format.

Note 2 (Replaced) (for non-web software)

This success criterion is primarily for software developers who develop or use custom user interface components. Standard user interface components on most [accessibility-supported](#dfn-accessibility-supported) platforms already satisfy this success criterion when used according to specification.

Note 3 (Added) (for non-web software)

For conforming to this success criterion, it is usually best practice for software user interfaces to use the [accessibility services of platform software](#accessibility-services-of-platform-software). These accessibility services enable interoperability between software user interfaces and both assistive technologies and accessibility features of software in standardized ways. Most platform accessibility services go beyond programmatic exposure of name and role, and programmatic setting of states, properties and values (and notification of same), and specify additional information that could be exposed and / or set (for instance, a list of the available actions for a given user interface component, and a means to programmatically execute one of the listed actions).

Note 4 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).

##### 4.1.3 Status Messages

(Level AA)

> In content implemented using markup languages, [status messages](https://www.w3.org/TR/WCAG22/#dfn-status-messages "change in content that is not a change of context, and that provides information to the user on the success or results of an action, on the waiting state of an application, on the progress of a process, or on the existence of errors") can be [programmatically determined](https://www.w3.org/TR/WCAG22/#dfn-programmatically-determinable "determined by software from author-supplied data provided in a way that different user agents, including assistive technologies, can extract and present this information to users in different modalities") through [role](https://www.w3.org/TR/WCAG22/#dfn-role "text or number by which software can identify the function of a component within Web content") or properties such that they can be presented to the user by [assistive technologies](https://www.w3.org/TR/WCAG22/#dfn-assistive-technologies "hardware and/or software that acts as a user agent, or along with a mainstream user agent, to provide functionality to meet the requirements of users with disabilities that go beyond those offered by mainstream user agents") without receiving focus.

###### Applying SC 4.1.3 Status Messages to Non-Web Documents and Software

This applies directly as written, and as described in [Intent from Understanding Success Criterion 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html#intent).

Note 1 (Added)

For [non-web documents](#document) and [software](#software) where status messages are not implemented using markup languages, there is still a user need to have status messages be programmatically exposed so that they can be presented to the user by assistive technologies without receiving focus. This is typically enabled through the use of accessibility services of the [user agent](#user-agent) or other [platform software](#platform-software).

Note 2 (Added) (for non-web software)

See also the [Comments on Closed Functionality](#comments-on-closed-functionality).