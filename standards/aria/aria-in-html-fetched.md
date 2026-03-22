---
ai_context: Auto-fetched ARIA in HTML specification.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/html-aria/
standard: ARIA in HTML
status: normative
tags:
- aria
- html
- implicit-role
title: ARIA in HTML (Fetched)
---

[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

# ARIA in HTML

[W3C Recommendation](https://www.w3.org/standards/types#REC) 05 August 2025

More details about this document

This version:
:   <https://www.w3.org/TR/2025/REC-html-aria-20250805/>

Latest published version:
:   <https://www.w3.org/TR/html-aria/>

Latest editor's draft:
:   <https://w3c.github.io/html-aria/>

History:
:   <https://www.w3.org/standards/history/html-aria/>
:   [Commit history](https://github.com/w3c/html-aria/commits/)

Implementation report:
:   <https://w3c.github.io/html-aria/results/implementation-results.html>

Editors:
:   Scott O'Hara ([Microsoft](https://www.microsoft.com/))
:   Patrick H. Lauke ([TetraLogical](https://tetralogical.com/))

Former editor:
:   Steve Faulkner ([TPGi](https://www.tpgi.com/)) - Until 28 April 2023

Feedback:
:   [GitHub w3c/html-aria](https://github.com/w3c/html-aria/)
    ([pull requests](https://github.com/w3c/html-aria/pulls/),
    [new issue](https://github.com/w3c/html-aria/issues/new/choose),
    [open issues](https://github.com/w3c/html-aria/issues/))
:   [public-webapps@w3.org](mailto:public-webapps@w3.org?subject=%5Bhtml-aria%5D%20YOUR%20TOPIC%20HERE) with subject line `[html-aria] … message topic …` ([archives](https://lists.w3.org/Archives/Public/public-webapps))

Errata:
:   [Errata exists](https://github.com/w3c/html-aria/issues/new/).

See also
[**translations**](https://www.w3.org/Translations/?technology=html-aria).

[Copyright](https://www.w3.org/policies/#copyright)
©
2025
[World Wide Web Consortium](https://www.w3.org/).
W3C®
[liability](https://www.w3.org/policies/#Legal_Disclaimer),
[trademark](https://www.w3.org/policies/#W3C_Trademarks) and
[permissive document license](https://www.w3.org/copyright/software-license-2023/ "W3C Software and Document Notice and License") rules apply.

---

## Abstract

This specification defines the authoring rules (author conformance requirements) for the use
of [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/) and [Digital Publishing WAI-ARIA Module 1.0](https://www.w3.org/TR/dpub-aria-1.0/) attributes on [[HTML](#bib-html "HTML Standard")] elements.
This specification's primary objective is to define requirements for use
with conformance checking tools used by authors (i.e., web developers). These requirements will aid authors
in their development of web content, including custom interfaces and widgets, which make use of ARIA to
complement or extend the features of the host language [[HTML](#bib-html "HTML Standard")].

## Status of This Document

*This section describes the status of this
document at the time of its publication. A list of current W3C
publications and the latest revision of this technical report can be found
in the
[W3C standards and drafts index](https://www.w3.org/TR/).*

ARIA in HTML is an [[HTML](#bib-html "HTML Standard")] specification module. Any HTML features, conformance requirements, or terms that this specification
module makes reference to, but does not explicitly define, are defined by the [HTML Standard](#bib-html "HTML Standard").

Since this specification become a W3C Recommendation on 09 December 2021,
the following substantive additions and/or corrections have been proposed:

- [23 July 2025 - Addition:](https://github.com/w3c/html-aria/pull/556)
  Update the [`label`](#el-label) element to allow `role` and `aria-*` attributes
  to be specified when the element is not associated with a labelable element.
- [23 July 2025 - Addition:](https://github.com/w3c/html-aria/pull/528)
  Add the [`selectedcontent`](#el-selectedcontent) element and provide updated
  allowances for the [`button`](#el-button) element when it is used in the context
  of a customized `select` element.
- [23 July 2025 - Correction:](https://github.com/w3c/html-aria/pull/550)
  Clarify that the [`html`](#el-html) element is a `generic` element, and that
  neither the `document` or `generic` roles are recommended to be used on the element.
- [23 December 2024 - Addition:](https://github.com/w3c/html-aria/pull/525)
  Update the [`img`](#el-img) element to allow the `math` role.
- [13 December 2024 - Addition:](https://github.com/w3c/html-aria/pull/533)
  Update to include the `image` role as preferred synonym to the `img` role.
- [13 December 2024 - Addition:](https://github.com/w3c/html-aria/pull/507)
  Clarify the allowance for `aria-hidden` when used with the `hidden` attribute.
- [4 October 2023 - Addition:](https://github.com/w3c/html-aria/pull/489)
  Update the button element and input type=button,image,reset,submit elements to allow the `separator` role.
- [3 October 2023 - Correction:](https://github.com/w3c/html-aria/pull/453)
  Update the [`img`](#el-img) element allowances to be based on if the element has an accessible name or not.
- [21 August 2023 - Addition:](https://github.com/w3c/html-aria/pull/462)
  Update the [`address`](#el-address) and [`hgroup`](#el-hgroup) element allowances per their updated mapping to the `group` role.
- [9 July 2023 - Addition:](https://github.com/w3c/html-aria/pull/455)
  Update the [`aside`](#el-aside) element to allow the dpub `doc-glossary` role.
- [5 July 2023 - Addition:](https://github.com/w3c/html-aria/pull/446)
  Update the [`button`](#el-button), [`input type=button`](#el-input-button), [`input type=image`](#el-input-image)
  [`input type=reset`](#el-input-reset), and [`input type=submit`](#el-input-submit) elements to align their allowed roles.
- [29 June 2023 - Addition:](https://github.com/w3c/html-aria/pull/469)
  Update the [`s`](#el-s) element allowed roles to indicate use of `role=deletion` on the element would be considered redundnat.
- [31 May 2023 - Correction:](https://github.com/w3c/html-aria/pull/435)
  Conditionally revise allowed `aria-*` attributes and roles on [`summary`](#el-summary) element.
- [31 May 2023 - Correction:](https://github.com/w3c/html-aria/pull/410)
  Update [`li`](#el-li) element role allowances in context to the element's ancestral relationship, or lack of,
  to a list element parent.
- [24 March 2023 - Addition:](https://github.com/w3c/html-aria/pull/401)
  The [`search`](#el-search) element has been added.
- [6 March 2023 - Addition:](https://github.com/w3c/html-aria/pull/447)
  Disallow `aria-hidden=true` on the `body` element.
- [13 February 2023 - Addition:](https://github.com/w3c/html-aria/pull/415)
  Update `figure` element role allowances to include `doc-example`.
- [07 November 2022 - Correction:](https://github.com/w3c/html-aria/pull/437)
  Revisions to 'any role' term description.
- [14 July 2022 - Correction:](https://github.com/w3c/html-aria/pull/383)
  Disallow roles and `aria-*` attributes on the [`datalist`](#el-datalist) element.
- [16 April 2022 - Correction:](https://github.com/w3c/html-aria/pull/372)
  [`aria-checked`](#att-checked) is not to be used on elements that support the `checked` attribute.
- [03 April 2022 - Addition:](https://github.com/w3c/html-aria/pull/402)
  Identify [Naming Prohibited](#dfn-naming-prohibited) elements.
- [06 March 2022 - Addition:](https://github.com/w3c/html-aria/pull/404)
  Allow `none` and `presentation` roles on [`nav` element](#el-nav).
- [03 March 2022 - Addition:](https://github.com/w3c/html-aria/pull/403)
  Restrict role allowances for [`div` element](#el-div) when it is a child of a `dl` element.
- [12 February 2022 - Addition & Correction:](https://github.com/w3c/html-aria/pull/396)
  Allow `combobox` role on [`button` element](#el-button).
  Allow `combobox` and `checkbox` roles on [`input type=button` element](#el-input-button).
- [18 January 2022 - Addition:](https://github.com/w3c/html-aria/pull/391)
  Added [Requirements for deprecated ARIA role, state and property attributes](#docconformance-deprecated).
- [06 January 2022 - Addition:](https://github.com/w3c/html-aria/pull/369)
  Change allowances for `doc-biblioentry` and `doc-endnote` roles on the [`li` element](#el-li).
  These roles are deprecated in [Digital Publishing WAI-ARIA Module 1.1](https://www.w3.org/TR/dpub-aria-1.1/).
- [13 December 2021 - Correction:](https://github.com/w3c/html-aria/pull/381)
  Allow `radio` role on [`img alt="some text"` element](#el-img).
- [07 December 2021 - Correction:](https://github.com/w3c/html-aria/pull/353)
  Allow only `none` and `presentation` roles for [`wbr` element](#el-wbr).
  Allow only `aria-hidden` global attribute for [`br`](#el-br) and [`wbr`](#el-wbr) elements.
- [02 December 2021 - Addition:](https://github.com/w3c/html-aria/pull/367)
  Allow `group` role on [`section` element](#el-section).
- [16 November 2021 - Addition:](https://github.com/w3c/html-aria/pull/360)
  Allow `link` and `button` roles on [`area` without `href` element](#el-area-no-href).
- [26 October 2021 - Addition:](https://github.com/w3c/html-aria/pull/352)
  Allow `aria-hidden` attribute on the [`picture` element](#el-picture).

Reviewers of the document can identify candidate additions
and/or corrections by their distinctive styling in the document:

Candidate corrections are marked in the document.

Candidate additions are marked in the document.

This document was published by the [Web Applications Working Group](https://www.w3.org/groups/wg/webapps) as
a Recommendation using the
[Recommendation track](https://www.w3.org/policies/process/20231103/#recs-and-notes). It includes
[candidate amendments](https://www.w3.org/policies/process/20231103/#candidate-amendments),
introducing substantive changes and new features since the previous
Recommendation.

W3C recommends the wide deployment of this specification as a standard for
the Web.

A W3C Recommendation is a specification that, after extensive
consensus-building, is endorsed by
W3C and its Members, and
has commitments from Working Group members to
[royalty-free licensing](https://www.w3.org/policies/patent-policy/#sec-Requirements)
for implementations.
Future updates to this Recommendation may incorporate
[new features](https://www.w3.org/policies/process/20231103/#allow-new-features).

Candidate additions are marked in the document.

Candidate corrections are marked in the document.

This document was produced by a group
operating under the
[W3C Patent
Policy](https://www.w3.org/policies/patent-policy/).
W3C maintains a
[public list of any patent disclosures](https://www.w3.org/groups/wg/webapps/ipr)
made in connection with the deliverables of
the group; that page also includes
instructions for disclosing a patent. An individual who has actual
knowledge of a patent that the individual believes contains
[Essential Claim(s)](https://www.w3.org/policies/patent-policy/#def-essential)
must disclose the information in accordance with
[section 6 of the W3C Patent Policy](https://www.w3.org/policies/patent-policy/#sec-Disclosure).

This document is governed by the
[03 November 2023 W3C Process Document](https://www.w3.org/policies/process/20231103/).

## 1. Author requirements for use of ARIA in HTML

Authors *MAY* use the ARIA `role` and `aria-*` attributes to change
the exposed meaning ([semantics](https://html.spec.whatwg.org/multipage/dom.html#semantics-2)) of
[HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements), in accordance with the requirements defined by
[WAI-ARIA](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2"), except where ARIA features conflict with the
[strong native semantics](https://www.w3.org/TR/wai-aria-1.2/#host_general_conflict)
or are equal to the
[implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics)
of a given HTML element. The [implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics) for the features
of HTML are defined by the [HTML Accessibility API Mappings](#bib-html-aam-1.0 "HTML Accessibility API Mappings 1.0") specification.

Any constraints for the use of ARIA features in HTML defined by this specification
are intended to prevent authors from making assistive technology products report
nonsensical user interface (UI) information that does not represent the actual UI
of the document.

Authors *MUST NOT* use the ARIA `role` and `aria-*` attributes in a manner that conflicts
with the semantics described in the [4. 
Document conformance requirements for use of ARIA attributes in HTML](#docconformance) and [4.2 
Requirements for use of ARIA attributes in place of equivalent HTML attributes](#docconformance-attr)
tables. It is *NOT RECOMMENDED* for authors to set the ARIA `role` and `aria-*` attributes
to values that match the [implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics) defined in either table.
Doing so is unnecessary and can potentially lead to unintended consequences.

## 2. ARIA semantics that extend and diverge from HTML

*This section is non-normative.*

Through the use of ARIA, authors can specify semantics that go beyond the current
capabilities of native HTML. This can be very useful, as it provides authors the opportunity
to create widgets, or expose specific accessible states and properties to native HTML features
which would not be possible by the use of HTML alone.

For instance, a `button` element has no native HTML feature to expose a "pressed" state.
ARIA allows authors to extend the semantics of the element by specifying the `aria-pressed`
attribute, allowing for an aural UI that will match the visual presentation of the control.

In the following example, a `button` element allows for a user to toggle the state of a
setting within a web application. The `aria-pressed` attribute is used to
augment the `button` element. When in the "pressed" state that information can be
exposed to users of assistive technologies.

[Example 1](#example-communicate-a-button-s-pressed-state-with-aria): Communicate a button's pressed state with ARIA

```
<button aria-pressed=true>...</button>
```

There are also situations where certain `aria-*` attributes are allowed for use on elements
with specific `role`s, while the equivalent native attribute is currently not valid in HTML itself.

For instance, HTML has no direct concept of a disabled hyperlink (`a href` element).
Constructs such as `<a href="..." disabled> ... </a>` are not valid,
and will not be conveyed to assistive technologies.

ARIA diverges from HTML in this regard and does allow for an `aria-disabled`
attribute to be specified on an element with an explicit `role=link`. If an author were
to specify an `aria-disabled=true` on an HTML hyperlink, user agents would not functionally
treat the hyperlink any differently (it would still be clickable/operable), however it
would be exposed to assistive technologies as being in the disabled state.

Similarly, while native HTML `option` elements that are descendants of a `select` can
only be set as being `selected`, elements with an explicit `option` role can not only
allow the equivalent `aria-selected`, but also the `aria-checked` attribute, supporting
widgets/constructs that go beyond the capabilities of a native `select` element.

Unfortunately, in these situations where ARIA and HTML have feature parity, but diverge
in allowances, it can create for a misalignment in support, if not also user experiences.
In situations where ARIA allows a feature not supported by HTML, it will often
be in the author's and ultimately the user's best interest to instead implement as a
fully custom ARIA widget.

In the following example, a hyperlink needs to be communicated as being in the disabled
state. HTML does not allow for the use of the `disabled` attribute on a hyperlink,
and using `aria-disabled=true` would communicate the hyperlink as being disabled to
assistive technologies, but would not actually disable the element. The most effective way
to both communicate and actually disable a hyperlink would be to remove the `href` from
the `a` element, creating a placeholder. Then, ARIA can be applied to this
placeholder link to communicate the element's intended role and state.

[Example 2](#example-communicate-a-disabled-link-with-aria): Communicate a disabled link with ARIA

```
<a role=link aria-disabled=true>...</a>
```

## 3. Author guidance to avoid incorrect use of ARIA

*This section is non-normative.*

### 3.1 Avoid overriding interactive elements with non-interactive roles

ARIA is useful for revising or correcting the role of an element when a different role
is necessary to expose to users. However, it is rarely in the user or author's best interest
to try and use ARIA to override an interactive element, for instance a `button`, with a role
generally exposed by a non-interactive element. For instance, a heading.

As an example, the following uses a `role=heading` on a `button` element. This is
not allowed, because the `button` element has default functionality that conflicts with user
expectations for the heading role.

[Example 3](#example-wrong-role): Wrong role

```
<button role="heading">search</button>
```

An author would need to take additional steps to ensure the default functionality and presentation of
the `button` was removed, and even doing so may still not be enough to fully supress the element's
implicit features depending on how the user chooses to engage with the web page. E.g., by turning on
Windows high contrast themes, or viewing the web page in a browser's reader mode.

### 3.2 Avoid specifying redundant roles

The following example illustrates a `button` element which has also been
provided an explicit `role=button`. Specifying this role is unnecessary, as a "button"
element is already exposed with an implicit `button` role. In practice this particular
instance of redundancy will likely not have unforeseen side effects, other than
unnecessarily making the markup more verbose, and incorrectly signaling to other authors
that this practice is useful. Please review the section [3.3 
Be cautious of side effects](#side-effects)
for an example of where specifying unnecessary roles can be problematic.

[Example 4](#example-redundant-role-on-button): Redundant role on button

```
<!-- Avoid doing this! -->
<button role="button">...</button>
```

Similarly, the following uses a `role=group` on a `fieldset` element, and a `role=Main` on a `main` element.
This is unnecessary, because the `fieldset` element is implicitly exposed as a `role=group`, as is the `main` element
implicitly exposed as a `role=main`. Again, in practice this will likely not have any unforeseen side effects to users
of assistive technology, as long as the declaration of the `role` value uses [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase).
Please see [4.4 
Case requirements for ARIA role, state and property attributes](#case-sensitivity) for more information.

[Example 5](#example-redundant-role-on-fieldset-and-main): Redundant role on fieldset and main

```
<!-- Avoid doing this! -->
<fieldset role="group">...</fieldset>
<!-- or this! -->
<main role="Main">...</main>
```

The following uses a `role=list` on an `ul` element. As the `ul` element has an implicit role of `list`,
explicitly adding the role would generally be considered redundant. However, some user agents suppress a list's
implicit ARIA semantics if the list markers are removed from the visual presentation of the list items.
Generally the redundant declaration of an element's implicit role would not be recommended, but in specific situations
such as this, and where the role is necessary to expose, authors can explicitly add the role.

[Example 6](#example-redundant-role-on-list): Redundant role on list

```
<!-- Generally avoid doing this! -->
<ul role="list">...</ul>
```

### 3.3 Be cautious of side effects

The following uses a `role=button` on a `summary` element. This is
unnecessary and can result in cross-platform issues. For instance,
preventing the element from correctly exposing its state, and forcing
the role of `button`, when it might otherwise be exposed with a
platform or browser specific role.

[Example 7](#example-unintended-consequences): Unintended consequences

```
<details>
  <!-- Avoid doing this! -->
  <summary role="button">more information</summary>
  ...
</details>
```

### 3.4 Adhere to the rules of ARIA

[Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/) defines a number of roles which are not meant to be used
by authors. Many of these roles are categorized as [Abstract Roles](https://www.w3.org/TR/wai-aria-1.2/#isAbstract)
which are explicitly stated as not to be used by authors. The following example illustrates the invalid use of an
abstract `select` role, where an author likely meant to use the `combobox` role instead.

[Example 8](#example-abstract-roles-are-not-for-authors): Abstract roles are not for authors

```
<!-- Do not do this! -->
<div role="select" ...>...</div>
```

ARIA also defines a [`generic` role](https://www.w3.org/TR/wai-aria-1.2/#generic) which is meant to provide
feature parity with a number of HTML elements that do not have more specific ARIA semantics of their
own. For instance, HTML's `div` and `span` elements, among others. ARIA discourages authors from
using the `generic` role as its intended purpose is for use by implementors of user agents.

In the following example, rather than using a `generic` role, authors are advised to use a `div` in
place of the `article` element. If changing the HTML element is not possible, specifying a role of
`presentation` or `none` would be acceptable alternaties to remove the implicit role of the `article`.

[Example 9](#example-do-not-specify-elements-as-generic): Do not specify elements as generic

```
<!-- Avoid doing this! -->
<article role="generic" ...>...</article>
```

Additionally, ARIA specifically mentions in [Conflicts with Host Language Semantics](https://www.w3.org/TR/wai-aria-1.2/#host_general_conflict)
that if authors use both native HTML features for exposing states and properties as well as their ARIA counterparts, then
the host language features take priority over the explicit ARIA attributes that are also used.

For instance, in the following example an author is using HTML's `input type=checkbox` and has specified an `aria-checked=true`. However,
user agents are meant to ignore the `aria-checked` attribute. Instead user agents would expose the state based on the native features
of the form control.

[Example 10](#example-the-implicit-checked-state-takes-precedent-over-the-explicit-aria-attribute): The implicit checked state takes precedent over the explicit ARIA attribute

```
<!-- Do not do this! -->
<input type="checkbox" checked aria-checked="false">
```

### 3.5 Adhere to the rules of HTML

While ARIA can be used to alter the way HTML features are exposed to users of assistive technologies,
these modifications do not change the underlying parsing and allowed content models of HTML. For instance,
a `div` allows an author to specify any role on it. However, this does not mean that the element can then be
used in a way that deviates from the rules HTML has defined for the element.

For instance, in the following example an author has specified a role of `link` on a `div` element. While
HTML allows for a hyperlink (exposed as a `role=link`) to be a descendant of a `p` element, the HTML parser does not
allow a `div` to be a descendant of a `p` element.

[Example 11](#example-revised-aria-semantics-with-invalid-html-nesting): Revised ARIA semantics with invalid HTML nesting

```
<!-- Do not do this! -->
<p>
  ... <div role=link tabindex=0>...</div> ... 
</p>
```

The HTML parser will modify the above markup to be output as the following:

[Example 12](#example-unwanted-rendered-markup-with-valid-alternative-solution): Unwanted rendered markup with valid alternative solution

```
<!-- The previous example's markup will render as follows -->
<p>...</p>
<div role=link tabindex=0>...</div> 
... 
<p></p>

<!-- Instead of a div, use a span. Spans are allowed descendants of p elements! -->
<p>
  ... <span role=link tabindex=0>...</span> ...
</p>
```

While this specification indicates the allowed ARIA attributes that can be specified on each HTML element,
this example illustrates that even if a role is allowed, the context in which it is used can still result
in potential rendering and accessibility issues.

## 4. Document conformance requirements for use of ARIA attributes in HTML

The following table provides normative per-element document conformance requirements for the
use of ARIA markup in HTML documents. Additionally, it identifies the [implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics)
that apply to [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements). The [implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics) of these elements are defined
in [HTML AAM](#bib-html-aam-1.0 "HTML Accessibility API Mappings 1.0").

Each language feature (element) in a cell in the first column implies the ARIA semantics
(role, states, and properties) given in the cell in the second column of the same row.
The third cell in each row defines the ARIA `role` values and `aria-*` attributes which authors *MAY* specify
on the element. Where a cell in the third column includes the term **Any** `role`
it indicates that any `role` value *MAY* be used on the element. However,
it is *NOT RECOMMENDED* for authors to specify the implicit role of the element, the `generic` role, or a role
[deprecated by ARIA](#docconformance-deprecated) on these elements.
If a cell in the third column includes the term **No `role`** it indicates
that authors *MUST NOT* overwrite the implicit ARIA semantics, or native semantics of the HTML element.

[WAI-ARIA](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2") identifies roles which have
[prohibited states and properties](https://www.w3.org/TR/wai-aria-1.2/#prohibitedattributes).
These roles do not allow certain WAI-ARIA attributes to be specified by authors.
HTML elements which expose these implicit WAI-ARIA roles also prohibit authors from
specifying these WAI-ARIA attributes.

Elements which are identified as Naming prohibited are those which authors *MUST NOT* specify an
`aria-label` or `aria-labelledby` attribute, unless the element allows for its implicit role to be overwritten
by an explicit WAI-ARIA role which allows naming from authors. For more information see [4.1 
Requirements for use of ARIA attributes to name elements](#docconformance-naming).

Note

While setting an ARIA `role` and/or `aria-*` attribute that matches the implicit ARIA semantics
is *NOT RECOMMENDED*, in some situations explicitly setting these attributes can be helpful – for instance,
for user agents that do not expose implicit ARIA semantics for certain elements.

Note

While it is conforming to use [Digital Publishing WAI-ARIA Module 1.0](https://www.w3.org/TR/dpub-aria-1.0/) `role` values as outlined in the following table, the use of these roles
is not intended for implementation of websites. If using these role for purposes beyond the scope of the digital publishing
industry, further manual testing will be necessary to ensure the intended experience is provided to users.

Rules of ARIA attribute usage by HTML element

| HTML element | Implicit ARIA semantics (explicitly assigning these in markup is *NOT RECOMMENDED*) | ARIA role, state and property allowances |
| --- | --- | --- |
| `a` with `href` | `role=link` | Roles: [`button`](#index-aria-button), [`checkbox`](#index-aria-checkbox), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`option`](#index-aria-option), [`radio`](#index-aria-radio), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab) or [`treeitem`](#index-aria-treeitem). (`link` is also allowed, but *NOT RECOMMENDED*.)  DPub Roles: [`doc-backlink`](https://www.w3.org/TR/dpub-aria-1.0/#doc-backlink), [`doc-biblioref`](https://www.w3.org/TR/dpub-aria-1.0/#doc-biblioref), [`doc-glossref`](https://www.w3.org/TR/dpub-aria-1.0/#doc-glossref) or [`doc-noteref`](https://www.w3.org/TR/dpub-aria-1.0/#doc-noteref)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  It is *NOT RECOMMENDED* to use `aria-disabled="true"` on an `a` element with an `href` attribute.  Note  If a link needs to be programmatically communicated as "disabled", [remove the `href` attribute](#example-communicate-a-disabled-link-with-aria). |
| `a` without `href` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `abbr` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `address` | `role=group` | [**Any `role`**](#dfn-any-role), though [`group`](#index-aria-group) is *NOT RECOMMENDED*.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `area` with `href` | `role=link` | [**No `role`**](#dfn-no-role) other than `link`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the [`link`](#index-aria-link) role. |
| `area` without `href` | `role=generic` | Roles: [`button`](#index-aria-button) or [`link`](#index-aria-link). (`generic` is also allowed, but *SHOULD NOT* be used.)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `article` | `role=article` | Roles: [`application`](#index-aria-application), [`document`](#index-aria-document), [`feed`](#index-aria-feed), [`main`](#index-aria-main), [`none`](#index-aria-none), [`presentation`](#index-aria-presentation) or [`region`](#index-aria-region). (`article` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `aside` | `role=complementary` | Roles: [`feed`](#index-aria-feed), [`none`](#index-aria-none), [`note`](#index-aria-note), [`presentation`](#index-aria-presentation), [`region`](#index-aria-region) or [`search`](#index-aria-search). (`complementary` is also allowed, but *NOT RECOMMENDED*.)  DPub Roles: [`doc-dedication`](https://www.w3.org/TR/dpub-aria-1.0/#doc-dedication), [`doc-example`](https://www.w3.org/TR/dpub-aria-1.0/#doc-example), [`doc-footnote`](https://www.w3.org/TR/dpub-aria-1.0/#doc-footnote), [`doc-glossary`](https://www.w3.org/TR/dpub-aria-1.0/#doc-glossary), [`doc-pullquote`](https://www.w3.org/TR/dpub-aria-1.0/#doc-pullquote) or [`doc-tip`](https://www.w3.org/TR/dpub-aria-1.0/#doc-tip)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `audio` | [No corresponding role](#dfn-no-corresponding-role) | Role: [`application`](#index-aria-application)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the [`application`](#index-aria-application) role. |
| [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) | Role exposed from author defined [`ElementInternals`](https://html.spec.whatwg.org/multipage/custom-elements.html#elementinternals)  Otherwise `role=generic` | If role defined by `ElementInternals`, [**no `role`**](#dfn-no-role)  Otherwise, [**any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited) if exposed as the `generic` role, or if exposed as another role which prohibits naming.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `b` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `base` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `bdi` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `bdo` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `blockquote` | `role=blockquote` | [**Any `role`**](#dfn-any-role), though `blockquote` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `body` | `role=generic` | [**No `role`**](#dfn-no-role) other than `generic`, which *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states)  allowed for the `generic` role, with the exception that authors *MUST NOT* specify `aria-hidden=true` on the `body` element. |
| `br` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation)  Authors *MAY* specify the [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden) attribute on the `br` element. Otherwise, no other allowed `aria-*` attributes. |
| `button` | `role=button`  If the `button` is the first child of a `select` element, the element is `inert`. | Roles: [`checkbox`](#index-aria-checkbox), [`combobox`](#index-aria-combobox), [`gridcell`](#index-aria-gridcell), [`link`](#index-aria-link), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`option`](#index-aria-option), [`radio`](#index-aria-radio), [`separator`](#index-aria-separator), [`slider`](#index-aria-slider), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab), or [`treeitem`](#index-aria-treeitem). (`button` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.   ---   If the `button` is the first child of a `select` element: **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `canvas` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `caption` | `role=caption` | [**No `role`**](#dfn-no-role) other than `caption`, which is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states). |
| `cite` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `code` | `role=code` | [**Any `role`**](#dfn-any-role), though `code` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `col` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `colgroup` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `data` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `datalist` | `role=listbox` | [**No `role`**](#dfn-no-role) other than `listbox`, which is *NOT RECOMMENDED*.  **No `aria-*` attributes**. |
| `dd` | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `definition` role. |
| `del` | `role=deletion` | [**Any `role`**](#dfn-any-role), though `deletion` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `details` | `role=group` | [**No `role`**](#dfn-no-role) other than `group`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `group` role. |
| `dfn` | `role=term` | [**Any `role`**](#dfn-any-role), though `term` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `dialog` | `role=dialog` | Role: [`alertdialog`](#index-aria-alertdialog). (`dialog` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `dialog` role. |
| `div` | `role=generic` | If a direct child of a `dl` element, only [`presentation`](#index-aria-presentation) or [`none`](#index-aria-none). Otherwise, [**any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `dl` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`group`](#index-aria-group), [`list`](#index-aria-list), [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `dt` | [No corresponding role](#dfn-no-corresponding-role) | Role: [`listitem`](#index-aria-listitem)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `em` | `role=emphasis` | [**Any `role`**](#dfn-any-role), though `emphasis` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `embed` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`application`](#index-aria-application), [`document`](#index-aria-document), [`img`](#index-aria-img), [`image`](#index-aria-img), [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `fieldset` | `role=group` | Roles: [`none`](#index-aria-none), [`presentation`](#index-aria-presentation) or [`radiogroup`](#index-aria-radiogroup). (`group` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `figcaption` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`group`](#index-aria-group), [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `figure` | `role=figure` | If the `figure` has a valid `figcaption` descendant:   [**No `role`**](#dfn-no-role) other than `figure`, which is *NOT RECOMMENDED*.  DPub Role: [`doc-example`](https://www.w3.org/TR/dpub-aria-1.0/#doc-example).  Otherwise, if the `figure` has no `figcaption` descendant:   [**Any `role`**](#dfn-any-role), though `figure` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `footer` | If not a descendant of an `article`, `aside`, `main`, `nav` or `section` element, or an element with `role=article`, `complementary`, `main`, `navigation` or `region` then `role=contentinfo`  Otherwise, `role=generic` | Roles: [`group`](#index-aria-group), [`presentation`](#index-aria-presentation) or [`none`](#index-aria-none). (If not a descendant of an `article`, `aside`, `main`, `nav` or `section` element, or an element with `role=article`, `complementary`, `main`, `navigation` or `region`, then `role=contentinfo` is also allowed, but *NOT RECOMMENDED*. Otherwise, `role=generic` is also allowed, but *SHOULD NOT* be used.)  DPub Role: [`doc-footnote`](https://www.w3.org/TR/dpub-aria-1.0/#doc-footnote)  [Naming Prohibited](#dfn-naming-prohibited) if exposed as `generic`.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `form` | `role=form` | Roles: [`none`](#index-aria-none), [`presentation`](#index-aria-presentation) or [`search`](#index-aria-search). (`form` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Note  A `form` is not exposed as a landmark region unless it has been provided an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name). |
| [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) | Role exposed from author defined [`ElementInternals`](https://html.spec.whatwg.org/multipage/custom-elements.html#elementinternals)  Otherwise `role=generic` | If role defined by `ElementInternals`, [**no `role`**](#dfn-no-role)  Otherwise, form-related roles: [`button`](#index-aria-button), [`checkbox`](#index-aria-checkbox), [`combobox`](#index-aria-combobox), [`listbox`](#index-aria-listbox), [`progressbar`](#index-aria-progressbar), [`group`](#index-aria-group), [`radio`](#index-aria-radio), [`radiogroup`](#index-aria-radiogroup), [`searchbox`](#index-aria-searchbox), [`slider`](#index-aria-slider), [`spinbutton`](#index-aria-spinbutton), [`switch`](#index-aria-switch) or [`textbox`](#index-aria-textbox). (`generic` is also allowed, but *SHOULD NOT* be used.)  [Naming Prohibited](#dfn-naming-prohibited) if exposed as the `generic` role.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| [`h1 to h6`](https://html.spec.whatwg.org/multipage/sections.html#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements) | `role=heading`, `aria-level` = the number in the element's tag name | Roles: [`none`](#index-aria-none), [`presentation`](#index-aria-presentation) or [`tab`](#index-aria-tab). (`heading` is also allowed, but *NOT RECOMMENDED*.)  DPub Role: [`doc-subtitle`](https://www.w3.org/TR/dpub-aria-1.0/#doc-subtitle)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `head` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `header` | If not a descendant of an `article`, `aside`, `main`, `nav` or `section` element, or an element with `role=article`, `complementary`, `main`, `navigation` or `region` then `role=banner`  Otherwise, `role=generic` | Roles: [`group`](#index-aria-group), [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation). (If not a descendant of an `article`, `aside`, `main`, `nav` or `section` element, or an element with `role=article`, `complementary`, `main`, `navigation` or `region`, then `role=banner` is also allowed, but *NOT RECOMMENDED*. Otherwise, `role=generic` is also allowed, but *SHOULD NOT* be used.)  [Naming Prohibited](#dfn-naming-prohibited) if exposed as `generic`.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `hgroup` | `role=group` | [**Any `role`**](#dfn-any-role), though [`group`](#index-aria-group) is *NOT RECOMMENDED*.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `hr` | `role=separator` | Roles: [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation). (`separator` is also allowed, but *NOT RECOMMENDED*.)  DPub Role: [`doc-pagebreak`](https://www.w3.org/TR/dpub-aria-1.0/#doc-pagebreak)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `separator` role. |
| `html` | `role=generic` | [**No `role`**](#dfn-no-role) other than `document` or `generic`, which are *NOT RECOMMENDED*.  **No `aria-*` attributes**. |
| `i` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `iframe` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`application`](#index-aria-application), [`document`](#index-aria-document), [`img`](#index-aria-img), [`image`](#index-aria-img), [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `img` | If the `img` has non-empty `alt` (`alt="some text"`) or an accessible name is provided by another [`img` naming method](https://www.w3.org/TR/html-aam-1.0/#img-element-accessible-name-computation), or the `img` has no `alt` and has not been provided a name:  `role=img or image` | Roles: [`button`](#index-aria-button), [`checkbox`](#index-aria-checkbox), [`link`](#index-aria-link), [`math`](#index-aria-math), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`meter`](#index-aria-meter), [`option`](#index-aria-option), [`progressbar`](#index-aria-progressbar), [`radio`](#index-aria-radio), [`scrollbar`](#index-aria-scrollbar), [`separator`](#index-aria-separator), [`slider`](#index-aria-slider), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab) or [`treeitem`](#index-aria-treeitem). (`img or image` is also allowed, but *NOT RECOMMENDED*.)  DPub Role: [`doc-cover`](https://www.w3.org/TR/dpub-aria-1.0/#doc-cover)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `img` with no accessible name | If the `img` has an empty `alt` (`alt``=""`) and lacks any other [`img` naming methods](https://www.w3.org/TR/html-aam-1.0/#img-element-accessible-name-computation):  `role=none`, `role=presentation`  If the `img` [lacks an `alt` attribute](https://html.spec.whatwg.org/multipage/images.html#unknown-images) and lacks any other [`img` naming methods](https://www.w3.org/TR/html-aam-1.0/#img-element-accessible-name-computation):  `role=img or image` | If the `img` has no `alt` attribute or accessible name: [**No `role`**](#dfn-no-role) other than the `role=none` or `presentation` roles. (`role=img or image` is also allowed, but *NOT RECOMMENDED*.)  If the `img` has an empty `alt=""` attribute and no `aria-label` or `aria-labelledby` attributes to provide it an accessible name: [**No `role`**](#dfn-no-role) other than the `role=none` or `presentation` roles, which are *NOT RECOMMENDED*.  **No `aria-*` attributes** except [`aria-hidden="true"`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden).  Otherwise, if the `img` has an author defined accessible name, see [`img` with an accessible name](#el-img). |
| [`input type=button`](https://html.spec.whatwg.org/multipage/input.html#button-state-(type=button)) | `role=button` | Roles: [`checkbox`](#index-aria-checkbox), [`combobox`](#index-aria-combobox), [`gridcell`](#index-aria-gridcell), [`link`](#index-aria-link), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`option`](#index-aria-option), [`radio`](#index-aria-radio), [`separator`](#index-aria-separator), [`slider`](#index-aria-slider), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab), or [`treeitem`](#index-aria-treeitem). (`button` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| [`input type=checkbox`](https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox)) | `role=checkbox` | Roles: [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`option`](#index-aria-option) or [`switch`](#index-aria-switch); [`button` if used with `aria-pressed`](#index-aria-button). (`checkbox` is also allowed, but *NOT RECOMMENDED*.)  Authors [*MUST NOT* use the `aria-checked` attribute on `input type=checkbox` elements](#att-checked).  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Note  The HTML `checked` attribute can be used instead of the `aria-checked` attribute for `menuitemcheckbox`, `option` or `switch` roles when used on `type=checkbox`. |
| [`input type=color`](https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and `aria-disabled` attribute. |
| [`input type=date`](https://html.spec.whatwg.org/multipage/input.html#date-state-(type=date)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=datetime-local`](https://html.spec.whatwg.org/multipage/input.html#local-date-and-time-state-(type=datetime-local)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=email`](https://html.spec.whatwg.org/multipage/input.html#e-mail-state-(type=email)) with no `list` attribute | `role=textbox` | [**No `role`**](#dfn-no-role) other than `textbox`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=file`](https://html.spec.whatwg.org/multipage/input.html#file-upload-state-(type=file)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states), `aria-disabled`, `aria-invalid` and `aria-required` attributes. |
| [`input type=hidden`](https://html.spec.whatwg.org/multipage/input.html#hidden-state-(type=hidden)) | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| [`input type=image`](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) | `role=button` | The following roles are allowed, but are *NOT RECOMMENDED*: [`button`](#index-aria-button), [`checkbox`](#index-aria-checkbox), [`gridcell`](#index-aria-gridcell), [`link`](#index-aria-link), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`option`](#index-aria-option), [`radio`](#index-aria-radio), [`separator`](#index-aria-separator), [`slider`](#index-aria-slider), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab) or [`treeitem`](#index-aria-treeitem).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  If possible, authors *SHOULD* consider using a different HTML element which allows the specified role, such as the `button` element. |
| [`input type=month`](https://html.spec.whatwg.org/multipage/input.html#month-state-(type=month)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=number`](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)) | `role=spinbutton` | [**No `role`**](#dfn-no-role) other than `spinbutton`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `spinbutton` role. |
| [`input type=password`](https://html.spec.whatwg.org/multipage/input.html#password-state-(type=password)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=radio`](https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)) | `role=radio` | Role: [`menuitemradio`](#index-aria-menuitemradio). (`radio` is also allowed, but *NOT RECOMMENDED*.)  Authors [*MUST NOT* use the `aria-checked` attribute on `input type=radio` elements](#att-checked).  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Note  The HTML `checked` attribute can be used instead of the `aria-checked` attribute for the `menuitemradio` role when used on `type=radio`. |
| [`input type=range`](https://html.spec.whatwg.org/multipage/input.html#range-state-(type=range)) | `role=slider` | [**No `role`**](#dfn-no-role) other than `slider`, which is *NOT RECOMMENDED*.  Authors *SHOULD NOT* use the [`aria-valuemax`](#att-max) or [`aria-valuemin`](#att-min) attributes on `input type=range`.  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `slider` role. |
| [`input type=reset`](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)) | `role=button` | The following roles are allowed, but are *NOT RECOMMENDED*: [`button`](#index-aria-button), [`checkbox`](#index-aria-checkbox), [`combobox`](#index-aria-combobox), [`gridcell`](#index-aria-gridcell), [`link`](#index-aria-link), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`option`](#index-aria-option), [`radio`](#index-aria-radio), [`separator`](#index-aria-separator), [`slider`](#index-aria-slider), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab) or [`treeitem`](#index-aria-treeitem).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  If possible, authors *SHOULD* consider using a different HTML element which allows the specified role, such as the `button` element. |
| [`input type=search`](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), with no `list` attribute | `role=searchbox` | [**No `role`**](#dfn-no-role) other than `searchbox`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `searchbox` role. |
| [`input type=submit`](https://html.spec.whatwg.org/multipage/input.html#submit-button-state-(type=submit)) | `role=button` | The following roles are allowed, but are *NOT RECOMMENDED*: [`button`](#index-aria-button), [`checkbox`](#index-aria-checkbox), [`combobox`](#index-aria-combobox), [`gridcell`](#index-aria-gridcell), [`link`](#index-aria-link), [`menuitem`](#index-aria-menuitem), [`menuitemcheckbox`](#index-aria-menuitemcheckbox), [`menuitemradio`](#index-aria-menuitemradio), [`option`](#index-aria-option), [`radio`](#index-aria-radio), [`separator`](#index-aria-separator), [`slider`](#index-aria-slider), [`switch`](#index-aria-switch), [`tab`](#index-aria-tab) or [`treeitem`](#index-aria-treeitem).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  If possible, authors *SHOULD* consider using a different HTML element which allows the specified role, such as the `button` element. |
| [`input type=tel`](https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)), with no `list` attribute | `role=textbox` | [**No `role`**](#dfn-no-role) other than `textbox`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=text`](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)) or with a missing or invalid `type`, with no `list` attribute | `role=textbox` | Roles: [`combobox`](#index-aria-combobox), [`searchbox`](#index-aria-searchbox) or [`spinbutton`](#index-aria-spinbutton). (`textbox` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| [`input type=text`](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), [`search`](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), [`tel`](https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)), [`url`](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)), [`email`](https://html.spec.whatwg.org/multipage/input.html#e-mail-state-(type=email)), or with a missing or invalid `type`, **with a `list` attribute** | `role=combobox` | [**No `role`**](#dfn-no-role) other than `combobox`, which is *NOT RECOMMENDED*.  Authors *SHOULD NOT* use the `aria-haspopup` attribute on the indicated `input`s with a `list` attribute.  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `combobox` role. |
| [`input type=time`](https://html.spec.whatwg.org/multipage/input.html#time-state-(type=time)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=url`](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)) with no `list` attribute | `role=textbox` | [**No `role`**](#dfn-no-role) other than `textbox`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| [`input type=week`](https://html.spec.whatwg.org/multipage/input.html#week-state-(type=week)) | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| `ins` | `role=insertion` | [**Any `role`**](#dfn-any-role), though `insertion` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `kbd` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `label` | [No corresponding role](#dfn-no-corresponding-role) | If a `label` element is implicitly or explicitly associated with a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) then [**no `role`**](#dfn-no-role)  Otherwise, if the `label` is not associted with an element then [**any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited) if exposed as the `generic` role, or if exposed as another role which prohibits naming.  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states). |
| `legend` | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states). |
| `li` | If the `li` is a child of a list element ([`ul`](#el-ul), [`ol`](#el-ol), [`menu`](#el-menu)) `role=listitem`.  Otherwise, if the `li` is not a child of a list element it is exposed as a `role=generic`. | **[No `role`](#dfn-no-role)** other than `listitem`, which is *NOT RECOMMENDED*, if the parent list element has an implicit or explicit `list` role.  Otherwise, [**any `role`**](#dfn-any-role) if the parent list element does not expose an implicit or explicit `list` role.  Note  See [`ul`](#el-ul), [`ol`](#el-ol), or [`menu`](#el-menu) for allowed roles for list elements.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Authors *SHOULD NOT* use the following [deprecated](#docconformance-deprecated) DPub Roles: [`doc-biblioentry`](https://www.w3.org/TR/dpub-aria-1.1/#doc-biblioentry), [`doc-endnote`](https://www.w3.org/TR/dpub-aria-1.1/#doc-endnote). |
| `link` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `main` | `role=main` | [**No `role`**](#dfn-no-role) other than `main`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `main` role. |
| `map` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `mark` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| [`math`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#mathml) | `role=math` | [**No `role`**](#dfn-no-role) other than `math`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `math` role. |
| `menu` | `role=list` | Roles: [`group`](#index-aria-group), [`listbox`](#index-aria-listbox), [`menu`](#index-aria-menu), [`menubar`](#index-aria-menubar), [`none`](#index-aria-none), [`presentation`](#index-aria-presentation), [`radiogroup`](#index-aria-radiogroup), [`tablist`](#index-aria-tablist), [`toolbar`](#index-aria-toolbar) or [`tree`](#index-aria-tree). (`list` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Authors *SHOULD NOT* use [deprecated](#docconformance-deprecated) [`directory`](#index-aria-directory) role. |
| `meta` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `meter` | `role=meter` | [**No `role`**](#dfn-no-role) other than `meter`, which is *NOT RECOMMENDED*.  Authors *SHOULD NOT* use the [`aria-valuemax`](#att-max) or [`aria-valuemin`](#att-min) attributes on `meter` elements.  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `meter` role. |
| `nav` | `role=navigation` | Roles: [`menu`](#index-aria-menu), [`menubar`](#index-aria-menubar), [`none`](#index-aria-none), [`presentation`](#index-aria-presentation) or [`tablist`](#index-aria-tablist). (`navigation` is also allowed, but *NOT RECOMMENDED*.)  DPub Roles: [`doc-index`](https://www.w3.org/TR/dpub-aria-1.0/#doc-index), [`doc-pagelist`](https://www.w3.org/TR/dpub-aria-1.0/#doc-pagelist) or [`doc-toc`](https://www.w3.org/TR/dpub-aria-1.0/#doc-toc)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `noscript` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `object` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`application`](#index-aria-application), [`document`](#index-aria-document), [`img`](#index-aria-img) or [`image`](#index-aria-img).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `ol` | `role=list` | Roles: [`group`](#index-aria-group), [`listbox`](#index-aria-listbox), [`menu`](#index-aria-menu), [`menubar`](#index-aria-menubar), [`none`](#index-aria-none), [`presentation`](#index-aria-presentation), [`radiogroup`](#index-aria-radiogroup), [`tablist`](#index-aria-tablist), [`toolbar`](#index-aria-toolbar) or [`tree`](#index-aria-tree). (`list` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Authors *SHOULD NOT* use [deprecated](#docconformance-deprecated) [`directory`](#index-aria-directory) role. |
| `optgroup` | `role=group` | [**No `role`**](#dfn-no-role) other than `group`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `group` role. |
| `option` element that is in a [list of options](https://html.spec.whatwg.org/multipage/input.html#attr-input-list) or that represents a suggestion in a `datalist` | `role=option` | [**No `role`**](#dfn-no-role) other than `option`, which is *NOT RECOMMENDED*.  Authors *SHOULD NOT* use the `aria-selected` attribute on the `option` element.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `option` role. |
| `output` | `role=status` | [**Any `role`**](#dfn-any-role), though `status` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `p` | `role=paragraph` | [**Any `role`**](#dfn-any-role), though `paragraph` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `param` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `picture` | [No corresponding role](#dfn-no-corresponding-role) | [**No `role`**](#dfn-no-role)  Authors *MAY* specify the [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden) attribute on the `picture` element. Otherwise, no other allowed `aria-*` attributes. |
| `pre` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `progress` | `role=progressbar` | [**No `role`**](#dfn-no-role) other than `progressbar`, which is *NOT RECOMMENDED*.  Authors *SHOULD NOT* use the [`aria-valuemax`](#att-max) attribute on `progress` elements.  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `progressbar` role. |
| `q` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `rp` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `rt` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `ruby` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `s` | `role=deletion` | [**Any `role`**](#dfn-any-role), though `deletion` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `samp` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `script` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `search` | `role=search` | Roles: [`form`](#index-aria-form), [`group`](#index-aria-group), [`none`](#index-aria-none), [`presentation`](#index-aria-presentation) or [`region`](#index-aria-region). (`search` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `section` | `role=region` if the `section` element has an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name)  Otherwise, `role=generic` | Roles: [`alert`](#index-aria-alert), [`alertdialog`](#index-aria-alertdialog), [`application`](#index-aria-application), [`banner`](#index-aria-banner), [`complementary`](#index-aria-complementary), [`contentinfo`](#index-aria-contentinfo), [`dialog`](#index-aria-dialog), [`document`](#index-aria-document), [`feed`](#index-aria-feed), [`group`](#index-aria-group), [`log`](#index-aria-log), [`main`](#index-aria-main), [`marquee`](#index-aria-marquee), [`navigation`](#index-aria-navigation), [`none`](#index-aria-none), [`note`](#index-aria-note), [`presentation`](#index-aria-presentation), [`search`](#index-aria-search), [`status`](#index-aria-status) or [`tabpanel`](#index-aria-tabpanel). (`role=region` is also allowed, but *NOT RECOMMENDED*. `role=generic` *SHOULD NOT* be used.)  DPub Roles: [`doc-abstract`](https://www.w3.org/TR/dpub-aria-1.0/#doc-abstract), [`doc-acknowledgments`](https://www.w3.org/TR/dpub-aria-1.0/#doc-acknowledgments), [`doc-afterword`](https://www.w3.org/TR/dpub-aria-1.0/#doc-afterword), [`doc-appendix`](https://www.w3.org/TR/dpub-aria-1.0/#doc-appendix), [`doc-bibliography`](https://www.w3.org/TR/dpub-aria-1.0/#doc-bibliography), [`doc-chapter`](https://www.w3.org/TR/dpub-aria-1.0/#doc-chapter), [`doc-colophon`](https://www.w3.org/TR/dpub-aria-1.0/#doc-colophon), [`doc-conclusion`](https://www.w3.org/TR/dpub-aria-1.0/#doc-conclusion), [`doc-credit`](https://www.w3.org/TR/dpub-aria-1.0/#doc-credit), [`doc-credits`](https://www.w3.org/TR/dpub-aria-1.0/#doc-credits), [`doc-dedication`](https://www.w3.org/TR/dpub-aria-1.0/#doc-dedication), [`doc-endnotes`](https://www.w3.org/TR/dpub-aria-1.0/#doc-endnotes), [`doc-epigraph`](https://www.w3.org/TR/dpub-aria-1.0/#doc-epigraph), [`doc-epilogue`](https://www.w3.org/TR/dpub-aria-1.0/#doc-epilogue), [`doc-errata`](https://www.w3.org/TR/dpub-aria-1.0/#doc-errata), [`doc-example`](https://www.w3.org/TR/dpub-aria-1.0/#doc-example), [`doc-foreword`](https://www.w3.org/TR/dpub-aria-1.0/#doc-foreword), [`doc-glossary`](https://www.w3.org/TR/dpub-aria-1.0/#doc-glossary), [`doc-index`](https://www.w3.org/TR/dpub-aria-1.0/#doc-index), [`doc-introduction`](https://www.w3.org/TR/dpub-aria-1.0/#doc-introduction), [`doc-notice`](https://www.w3.org/TR/dpub-aria-1.0/#doc-notice), [`doc-pagelist`](https://www.w3.org/TR/dpub-aria-1.0/#doc-pagelist), [`doc-part`](https://www.w3.org/TR/dpub-aria-1.0/#doc-part), [`doc-preface`](https://www.w3.org/TR/dpub-aria-1.0/#doc-preface), [`doc-prologue`](https://www.w3.org/TR/dpub-aria-1.0/#doc-prologue), [`doc-pullquote`](https://www.w3.org/TR/dpub-aria-1.0/#doc-pullquote), [`doc-qna`](https://www.w3.org/TR/dpub-aria-1.0/#doc-qna), [`doc-toc`](https://www.w3.org/TR/dpub-aria-1.0/#doc-toc)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `select` (with NO `multiple` attribute and NO `size` attribute having value greater than `1`) | `role=combobox` | Role: [`menu`](#index-aria-menu). (`combobox` is also allowed, but *NOT RECOMMENDED*.)  Authors *SHOULD NOT* use the `aria-multiselectable` attribute on a `select` element.  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `combobox` or `menu` role. |
| `select` (with a `multiple` attribute or a `size` attribute having value greater than `1`) | `role=listbox` | [**No `role`**](#dfn-no-role) other than `listbox`, which is *NOT RECOMMENDED*.  Authors *SHOULD NOT* use the `aria-multiselectable` attribute on a `select` element.  Otherwise, any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any other `aria-*` attributes applicable to the `listbox` role. |
| `selectedcontent` | `role=generic` | If used as a valid descendant of a `select` element: **[no `role`](#dfn-no-role) or `aria-*` attributes**  Otherwise, [**any `role`**](#dfn-any-role) if the element is used outside of its intended context as a child of the `button` part of a customizable `select` element, though `generic` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `slot` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `small` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `source` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `span` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `strong` | `role=strong` | [**Any `role`**](#dfn-any-role), though `strong` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `style` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `sub` | `role=subscript` | [**Any `role`**](#dfn-any-role), though `subscript` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `summary` | [No corresponding role](#dfn-no-corresponding-role)  Note  Many, but not all, user agents expose the `summary` element with an implicit ARIA `role=button`. | [**No `role`**](#dfn-no-role) if the `summary` element is a [summary for its parent details](https://html.spec.whatwg.org/multipage/interactive-elements.html#summary-for-its-parent-details).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states), `aria-disabled`, and `aria-haspopup` attributes.  Otherwise, authors *MAY* specifiy [**Any `role`**](#dfn-any-role), and any [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `sup` | `role=superscript` | [**Any `role`**](#dfn-any-role), though `superscript` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| [`SVG`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#svg-0) | `role=graphics-document` as defined by [SVG AAM](https://www.w3.org/TR/svg-aam-1.0/#details-id-66) | [**Any `role`**](#dfn-any-role), though `graphics-document` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `table` | `role=table` | [**Any `role`**](#dfn-any-role), though `table` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `tbody` | `role=rowgroup` | [**Any `role`**](#dfn-any-role), though `rowgroup` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `td` | `role=cell` if the ancestor `table` element is exposed as a `role=table`  `role=gridcell` if the ancestor `table` element is exposed as a `role=grid` or `treegrid`  [No corresponding role](#dfn-no-corresponding-role) if the ancestor `table` element is not exposed as a `role=table`, `grid` or `treegrid` | If the ancestor `table` element has `role=table`, `grid`, or `treegrid`, [**no `role`**](#dfn-no-role) other than the following:   - If the ancestor `table` element is exposed as a `role=table`, then   `cell`   is allowed, but *NOT RECOMMENDED*. - If the ancestor `table` element is exposed as a `role=grid` or `treegrid`, then   `gridcell`   is allowed, but *NOT RECOMMENDED*.   Otherwise, if the ancestor `table` element is not exposed as a `role=table`, `grid` or `treegrid`, [**any `role`**](#dfn-any-role).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `template` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `textarea` | `role=textbox` | [**No `role`**](#dfn-no-role) other than `textbox`, which is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `textbox` role. |
| `tfoot` | `role=rowgroup` | [**Any `role`**](#dfn-any-role), though `rowgroup` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `th` | `role=columnheader`, [`rowheader`](#index-aria-rowheader) or [`cell`](#index-aria-rowheader) if the ancestor `table` element is exposed as a `role=table`  `role=columnheader`, [`rowheader`](#index-aria-rowheader) or [`gridcell`](#index-aria-rowheader) if the ancestor `table` element is exposed as a `role=grid` or `treegrid`  [No corresponding role](#dfn-no-corresponding-role) if the ancestor `table` element is not exposed as a `role=table`, `grid` or `treegrid` | If the ancestor `table` element has `role=table`, `grid`, or `treegrid`, [**no `role`**](#dfn-no-role) other than the following:   - If the ancestor `table` element is exposed as a `role=table`, then   `columnheader`,   [`rowheader`](#index-aria-rowheader) and   [`cell`](#index-aria-rowheader)   are allowed, but *NOT RECOMMENDED*. - If the ancestor `table` element is exposed as a `role=grid` or `treegrid`, then   `columnheader`,   [`rowheader`](#index-aria-rowheader) or   [`gridcell`](#index-aria-rowheader)   are allowed, but *NOT RECOMMENDED*.   Otherwise, if the ancestor `table` element is not exposed as a `role=table`, `grid` or `treegrid`, [**any `role`**](#dfn-any-role).  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `thead` | `role=rowgroup` | [**Any `role`**](#dfn-any-role), though `rowgroup` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `time` | `role=time` | [**Any `role`**](#dfn-any-role), though `time` is *NOT RECOMMENDED*.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `title` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `tr` | `role=row` | If the ancestor `table` element has `role=table`, `grid`, or `treegrid`, [**no `role`**](#dfn-no-role) other than `row`, which is *NOT RECOMMENDED*; otherwise [**any `role`**](#dfn-any-role), though `row` is *NOT RECOMMENDED*.  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `track` | [No corresponding role](#dfn-no-corresponding-role) | **[No `role`](#dfn-no-role) or `aria-*` attributes** |
| `u` | `role=generic` | [**Any `role`**](#dfn-any-role), though `generic` *SHOULD NOT* be used.  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `ul` | `role=list` | Roles: [`group`](#index-aria-group), [`listbox`](#index-aria-listbox), [`menu`](#index-aria-menu), [`menubar`](#index-aria-menubar), [`none`](#index-aria-none), [`presentation`](#index-aria-presentation), [`radiogroup`](#index-aria-radiogroup), [`tablist`](#index-aria-tablist), [`toolbar`](#index-aria-toolbar) or [`tree`](#index-aria-tree). (`list` is also allowed, but *NOT RECOMMENDED*.)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles.  Authors *SHOULD NOT* use the [deprecated](#docconformance-deprecated) [`directory`](#index-aria-directory) role. |
| `var` | [No corresponding role](#dfn-no-corresponding-role) | [**Any `role`**](#dfn-any-role)  [Naming Prohibited](#dfn-naming-prohibited)  Otherwise, [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the allowed roles. |
| `video` | [No corresponding role](#dfn-no-corresponding-role) | Role: [`application`](#index-aria-application)  [Global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) and any `aria-*` attributes applicable to the `application` role. |
| `wbr` | [No corresponding role](#dfn-no-corresponding-role) | Roles: [`none`](#index-aria-none) or [`presentation`](#index-aria-presentation)  Authors *MAY* specify the [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden) attribute on the `wbr` element. Otherwise, no other allowed `aria-*` attributes. |

The elements marked with No corresponding role, in the second column of
the table do not have any [implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics), but they do have meaning
and this meaning may be represented in roles, states and properties not provided
by ARIA, and exposed to users of assistive technology via accessibility APIs.
It is therefore recommended that authors add a `role` attribute to a semantically
neutral element such as a `div` or `span`, rather than overriding the semantics
of the listed elements.

Note

Authors are encouraged to make use of the following documents for
guidance on using ARIA in HTML beyond that which is provided here:

- [Using ARIA](https://www.w3.org/TR/using-aria/) - A practical guide for authors on how to
  add accessibility information to HTML elements using the Accessible
  Rich Internet Applications specification.
- [WAI-ARIA Authoring Practices 1.2](https://www.w3.org/TR/wai-aria-practices-1.2/) - An author's guide to
  understanding and implementing Accessible Rich Internet Applications.

[Example 13](#example-13)

These features can be used to make accessibility tools render content
to their users in more useful ways. For example, ASCII art, which is
really an image, appears to be text, and in the absence of
appropriate roles and properties would end up being rendered by
screen readers as a nonsensical string of punctuation characters.
Using the features described in this section, one can instead make
the ATs skip the ASCII art and just read the caption:

```
<figure>
  <pre role="img" aria-label="ASCII Fish">
  o           .'`/
    '      /  (
  O    .-'` ` `'-._      .')
      _/ (o)        '.  .' /
      )       )))     ><  <
      `\  |_\      _.'  '. \
        '-._  _ .-'       '.)
    jgs     `\__\
  </pre>
  <figcaption id="fish-caption">
    Joan G. Stark, "<cite>fish</cite>".
    October 1997. ASCII on electrons. 28×8.
  </figcaption>
</figure>
```

### 4.1 Requirements for use of ARIA attributes to name elements

Authors *MAY* use [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) and [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attributes to specify [accessible names](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) for elements which have an implicit or explicit ARIA role which allows naming from authors. [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/) defines [roles which allow naming from authors](https://www.w3.org/TR/wai-aria-1.2/#namefromauthor) as well as [roles where author naming is prohibited](https://www.w3.org/TR/wai-aria-1.2/#namefromprohibited).

Authors *MUST NOT* specify `aria-label` or `aria-labelledby` on elements with implicit WAI-ARIA roles which cannot be named. HTML elements whose implicit WAI-ARIA roles prohibit naming from authors are identified in [4. 
Document conformance requirements for use of ARIA attributes in HTML](#docconformance).

The following markup example demonstrates a selection of HTML elements with implicit ARIA roles that prohibit naming from authors.

[Example 14](#example-elements-with-implicit-aria-roles-which-prohibit-naming-from-authors): Elements with implicit ARIA roles which prohibit naming from authors

```
<!-- DO NOT do the following! -->
<p aria-label="...">...</p>

<span aria-label="...">...<span>

<code aria-label="...">...<code>

<div aria-labelledby="...">...</div>
```

The following markup example demonstrates elements which have explicit WAI-ARIA roles which allow naming from authors. Due to the explicit roles specified on these elements, `aria-label` and `aria-labelledby` attributes are allowed.

[Example 15](#example-elements-with-explicit-aria-roles-which-allow-naming-from-authors): Elements with explicit ARIA roles which allow naming from authors

```
<p role="link" tabindex="0" aria-label="...">...</p>

<span role="button" tabindex="0" aria-label="...">...<span>

<div role="article" aria-labelledby="...">...</div>
```

### 4.2 Requirements for use of ARIA attributes in place of equivalent HTML attributes

Unless otherwise stated, authors *MAY* use `aria-*` attributes in place of their HTML equivalents on HTML elements where the `aria-*` semantics would
be expected. For example, authors *MAY* specify `aria-disabled=true` on a `button` element, while also implementing the necessary scripting to functionally
disable the `button`, rather than the use `disabled` attribute.

As stated in [WAI-ARIA's Conflicts with Host Language Semantics](https://www.w3.org/TR/wai-aria-1.2/#host_general_conflict),
when HTML elements use *both* `aria-*` attributes and their host language (HTML) equivalents, user agents *MUST* ignore the WAI-ARIA attributes – the
native HTML attributes with the same [implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics) take precedence. For this reason, authors *SHOULD NOT* specify both the native HTML attribute
and the equivalent `aria-*` attribute on an element. Please review each attribute for any further author specific requirements.

The following table represents HTML elements and their attributes which have `aria-*` attribute parity.

Each language feature (element and attribute) in a cell in the first
column implies the ARIA semantics (states, and properties) given in
the cell in the second column of the same row. The third cell in each
row defines how authors can use the native HTML feature, along with
requirements for using the `aria-*` attributes that supply the same
[implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics).

Rules of ARIA attribute usage by HTML feature

| HTML feature | Implicit ARIA semantics | HTML feature and `aria-*` attribute author guidance |
| --- | --- | --- |
| Any element where the `checked` attribute is allowed | `aria-checked="true"` | Use the `checked` attribute on any element that is allowed the `checked` attribute in HTML. Use the [`indeterminate`](https://html.spec.whatwg.org/multipage/input.html#dom-input-indeterminate) IDL attribute to indicate the "mixed" state for [`input type=checkbox`](https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox)) elements.  Authors *MUST NOT* use the [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked) attribute on any element where the [checkedness](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-checked), or the indeterminate checked value of the element can be in opposition to the current value of the `aria-checked` attribute.  Authors *MAY* use the `aria-checked` attribute on any other element with a WAI-ARIA role which allows the attribute. |
| Any element where the `disabled` attribute is allowed, including `option` `disabled` and `optgroup` `disabled` | `aria-disabled="true"` | Use the `disabled` attribute on any element that is allowed the `disabled` attribute in HTML.  Authors *MAY* use the [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled) attribute on any element that is allowed the `disabled` attribute in HTML, or any element with a WAI-ARIA role which allows the `aria-disabled` attribute.  Authors *SHOULD NOT* use `aria-disabled="true"` on any element which also has a `disabled` attribute.  Authors *MUST NOT* use `aria-disabled="false"` on any element which also has a `disabled` attribute. |
| Any element with a `hidden` attribute | `aria-hidden="true"` | Authors *MAY* use the [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden) attribute on any HTML element that allows [global `aria-*` attributes](https://www.w3.org/TR/wai-aria-1.2/#global_states) to be specified, with the exception of focusable elements and the [`body`](#el-body) element.  It is generally *NOT RECOMMENDED* for authors to use `aria-hidden="true"` on any element which also has the `hidden` attribute specified. However, authors *MUST NOT* use `aria-hidden="true"` on any element which also has the `hidden` attribute specified in the `until-found` state.  Note  A focusable element is any element which can be focused by use of keyboard or pointer device. Focusable elements are not always elements which can be tabbed to via a keyboard. For instance, an element with `tabindex="-1"` is focusable but is not a tabbable element.  Note  Using `aria-hidden="true"` on an element that has the `hidden` attribute is at best an unnecessary redundancy. At worst its usage can prevent access to the content if the `hidden` attribute's default UA style of `display: none` has been purposeuflly overwritten by an author or user style sheet. Finally, if the `hidden` attribute has the value of `until-found`, the use of `aria-hidden=true` will prevent this content from being discoverable to users of assistive technology when it is found via a browser's in-page find feature and visually rendered to users. |
| Any element where the `placeholder` attribute is allowed | `aria-placeholder="..."` | Use the `placeholder` attribute on any element that is allowed the `placeholder` attribute in HTML.  Authors *MAY* use the [`aria-placeholder`](https://www.w3.org/TR/wai-aria-1.2/#aria-placeholder) attribute on any element that is allowed the `placeholder` attribute in HTML, or any element with a WAI-ARIA role which allows the `aria-placeholder` attribute.  Authors *MUST NOT* use the `aria-placeholder` attribute on any element which also has a `placeholder` attribute. |
| Any element where the `max` attribute is allowed: `meter` `max`, `progress` `max`, and `input` `max` | `aria-valuemax="..."` | Use the `max` attribute on any element that is allowed the `max` attribute in HTML.  Authors *MAY* use the [`aria-valuemax`](https://www.w3.org/TR/wai-aria-1.2/#aria-valuemax) attribute on any other element with a WAI-ARIA role which allows the `aria-valuemax` attribute.  Authors *SHOULD NOT* use `aria-valuemax` on any element which allows the `max` attribute. Use the `max` attribute instead.  Authors *MUST NOT* use `aria-valuemax` on any element which also has a `max` attribute. |
| Any element where the `min` attribute is allowed: `meter` `min` and `input` `min` | `aria-valuemin="..."` | Use the `min` attribute on any element that is allowed the `min` attribute in HTML.  Authors *MAY* use the [`aria-valuemin`](https://www.w3.org/TR/wai-aria-1.2/#aria-valuemax) attribute on any other element with a WAI-ARIA role which allows the `aria-valuemin` attribute.  Authors *SHOULD NOT* use `aria-valuemin` on any element which allows the `min` attribute. Use the `min` attribute instead.  Authors *MUST NOT* use `aria-valuemin` on any element which also has a `min` attribute. |
| Any element which allows the `readonly` attribute: `input` `readonly`, `textarea` `readonly` and [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) which allows `readonly` | `aria-readonly="true"` | Use the `readonly` attribute on any element that is allowed the `readonly` attribute in HTML.  Authors *MAY* use the [`aria-readonly`](https://www.w3.org/TR/wai-aria-1.2/#aria-readonly) attribute on any element with a WAI-ARIA role which allows the attribute.  Authors *SHOULD NOT* use the `aria-readonly="true"` on any element which also has a `readonly` attribute.  Authors *MUST NOT* use `aria-readonly="false"` on any element which also has a `readonly` attribute. |
| Element with `contenteditable``=true` or element without `contenteditable` attribute whose closest ancestor with a `contenteditable` attribute has `contenteditable="true"`.  Note  This is equivalent to the [`isContentEditable`](https://html.spec.whatwg.org/multipage/interaction.html#dom-iscontenteditable) IDL attribute. | `aria-readonly="false"` | Authors *MUST NOT* set `aria-readonly="true"` on an element that has `isContentEditable="true"`. |
| Any element where the `required` attribute is allowed: `input` `required`, `textarea` `required`, and `select` `required` | `aria-required="true"` | Use the `required` attribute on any element that is allowed the `required` attribute in HTML.  Authors *MAY* use the [`aria-required`](https://www.w3.org/TR/wai-aria-1.2/#aria-required) attribute on any element that is allowed the `required` attribute in HTML, or any element with a WAI-ARIA role which allows the `aria-required` attribute.  Authors *SHOULD NOT* use the `aria-required="true"` on any element which also has a `required` attribute.  Authors *MUST NOT* use `aria-required="false"` on any element which also has a `required` attribute. |
| Any element where the `colspan` attribute is allowed: `td` and `th` | `aria-colspan="..."` | Use the `colspan` attribute on any element that is allowed the `colspan` attribute in HTML.  Authors *SHOULD NOT* use the `aria-colspan` attribute on any element which also has a `colspan` attribute.  Authors *MUST NOT* use `aria-colspan` on any element which also has a `colspan` attribute, and the values of each attribute do not match. |
| Any element where the `rowspan` attribute is allowed: `td` and `th` | `aria-rowspan="..."` | Use the `rowspan` attribute on any element that is allowed the `rowspan` attribute in HTML.  Authors *SHOULD NOT* use the `aria-rowspan` attribute on any element which also has a `rowspan` attribute.  Authors *MUST NOT* use `aria-rowspan` on any element which also has a `rowspan` attribute, and the values of each attribute do not match. |

### 4.3 Requirements for deprecated ARIA role, state and property and attributes

The ARIA Specification's [Deprecated Requirements](https://www.w3.org/TR/wai-aria-1.2/#deprecated) section indicates that if an ARIA feature is marked as deprecated then authors are advised not to use said feature for new content.

The following roles and attributes are deprecated features of ARIA and DPub ARIA. Conformance checkers *MUST* warn authors about the deprecated status of these features. Whenever possible, authors are advised to use alternatives to deprecated features.

#### 4.3.1 Deprecated ARIA roles

- [`directory`](https://www.w3.org/TR/wai-aria-1.2/#directory)

Note

The `directory` role is marked for deprecation in [WAI-ARIA 1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2"). In reality, the `directory` role had no functional difference to an element with an implicit or explicit `list` role. Authors are advised to use one of HTML's native list elements, or an ARIA `list` instead.

#### 4.3.2 Deprecated DPub ARIA roles

- [`doc-biblioentry`](https://www.w3.org/TR/dpub-aria-1.1/#doc-biblioentry)
- [`doc-endnote`](https://www.w3.org/TR/dpub-aria-1.1/#doc-endnote)

Note

The `doc-biblioentry` and `doc-endnote` roles are marked for deprecation in [Digital Publishing WAI-ARIA Module 1.1](https://www.w3.org/TR/dpub-aria-1.1/), as they are not valid children for an element with an implicit or explicit role of `list`. Authors can use standard list and child `li` elements without the need for these roles.

#### 4.3.3 Deprecated ARIA attributes

- [`aria-dropeffect`](https://www.w3.org/TR/wai-aria-1.1/#aria-dropeffect)
- [`aria-grabbed`](https://www.w3.org/TR/wai-aria-1.1/#aria-grabbed)

Note

The `aria-dropeffect` and `aria-grabbed` attributes were deprecated in [WAI-ARIA 1.1](#bib-wai-aria-1.1 "Accessible Rich Internet Applications (WAI-ARIA) 1.1"). There is presently no feature in ARIA to replace their proposed functionality.

### 4.4 Case requirements for ARIA role, state and property attributes

Authors *SHOULD* use [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase) for all `role` token values
and any state or property attributes (`aria-*`) whose values are
[defined as tokens](https://www.w3.org/TR/wai-aria-1.2/#propcharacteristic_value).

Note

While modern browsers treat the `role` or `aria-*` attribute values as [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive), not all assistive technologies will correctly parse these values.

To reduce interoperability issues, authors are strongly encouraged to use [ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase) for `aria-*` and `role` attribute values. Further, authors are encouraged to rigorously test with different browser and assistive technology combinations to ensure that their content will be correctly exposed to their users.

[Example 16](#example-16)

**Correct (conforming) examples:**

```
<div role="main">...</div>

<a href="home/" aria-current="page">home</a>
```

**Incorrect (non-conforming) examples:**

```
<!-- DO NOT DO THE FOLLOWING -->
<div role="MAIN">...</div>

<div role="Main">...</div>

<a href="home/" aria-current="Page">home</a>
```

## 5. Allowed descendants of ARIA roles

*This section is non-normative.*

The following table maps (and extends) the [Kinds of content](https://html.spec.whatwg.org/multipage/dom.html#kinds-of-content) and allowed descendant
information (defined in the
[[HTML](#bib-html "HTML Standard")] specification) to elements that have an equivalent `role`.

Column 1 links to the normative [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/) definitions for each ARIA `role`.
Column 2 identifies the [Kinds of content](https://html.spec.whatwg.org/multipage/dom.html#kinds-of-content)
categories each `role` has when it is used on an HTML element.
Column 3 indicates what kinds of HTML elements can be descendants of
an element with an explicit `role` specified, often matching the HTML element with
the same [implicit](#implicit) role.

For example, a `button` element has an implicit `role=button`.
In HTML a `button` element allows [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) as descendants, and does not allow [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2)
or descendants with a `tabindex` attribute. Therefore, any elements specified with a `role=button` would follow
the same descendant restrictions, and not allow any interactive content descendants,
elements with a `tabindex` specified, or any elements with role values
that are in the interactive content category (identified in column 3).

**Examples of non-conforming descendants**

```
<!-- conformance checkers will report an error -->
<button>
  <div role="button">...</div>
</button>

<div role="button">
  <button>...</button>
</div>

<div role="link">
  <textarea>...</textarea>
</div>
```

Additionally, there are certain roles which [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/) has specified specific requirements for their allowed descendants. These have been identified in column 3 (Descendant allowances) by indicating to "Refer to the 'Required Owned Elements'" for those particular roles.

Allowed descendants of ARIA roles

| Role | Kind of content | Descendant allowances |
| --- | --- | --- |
| [`alert`](https://www.w3.org/TR/wai-aria-1.2/#alert) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`alertdialog`](https://www.w3.org/TR/wai-aria-1.2/#alertdialog) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`application`](https://www.w3.org/TR/wai-aria-1.2/#application) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`article`](https://www.w3.org/TR/wai-aria-1.2/#article) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`banner`](https://www.w3.org/TR/wai-aria-1.2/#banner) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element), [header](https://html.spec.whatwg.org/multipage/sections.html#the-header-element), or [footer](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element) element descendants. |
| [`blockquote`](https://www.w3.org/TR/wai-aria-1.2/#blockquote) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`button`](https://www.w3.org/TR/wai-aria-1.2/#button) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`caption`](https://www.w3.org/TR/wai-aria-1.2/#caption) | N/A | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) or [table](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) element descendants. |
| [`cell`](https://www.w3.org/TR/wai-aria-1.2/#cell) | N/A | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`checkbox`](https://www.w3.org/TR/wai-aria-1.2/#checkbox) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`code`](https://www.w3.org/TR/wai-aria-1.2/#code) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`columnheader`](https://www.w3.org/TR/wai-aria-1.2/#columnheader) | N/A | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element), [header](https://html.spec.whatwg.org/multipage/sections.html#the-header-element), or [footer](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element) element descendants. |
| [`combobox`](https://www.w3.org/TR/wai-aria-1.2/#combobox) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`complementary`](https://www.w3.org/TR/wai-aria-1.2/#complementary) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`contentinfo`](https://www.w3.org/TR/wai-aria-1.2/#contentinfo) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element), [header](https://html.spec.whatwg.org/multipage/sections.html#the-header-element), or [footer](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element) element descendants. |
| [`definition`](https://www.w3.org/TR/wai-aria-1.2/#definition) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`deletion`](https://www.w3.org/TR/wai-aria-1.2/#deletion) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`dialog`](https://www.w3.org/TR/wai-aria-1.2/#dialog) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`directory`](https://www.w3.org/TR/wai-aria-1.2/#directory) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`document`](https://www.w3.org/TR/wai-aria-1.2/#document) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`emphasis`](https://www.w3.org/TR/wai-aria-1.2/#emphasis) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`feed`](https://www.w3.org/TR/wai-aria-1.2/#feed) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`figure`](https://www.w3.org/TR/wai-aria-1.2/#figure) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`form`](https://www.w3.org/TR/wai-aria-1.2/#form) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no `form` element descendants. |
| [`generic`](https://www.w3.org/TR/wai-aria-1.2/#generic) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`grid`](https://www.w3.org/TR/wai-aria-1.2/#grid) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`grid`](https://www.w3.org/TR/wai-aria-1.2/#grid) role. |
| [`gridcell`](https://www.w3.org/TR/wai-aria-1.2/#gridcell) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`group`](https://www.w3.org/TR/wai-aria-1.2/#group) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`heading`](https://www.w3.org/TR/wai-aria-1.2/#heading) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Heading content](https://html.spec.whatwg.org/multipage/dom.html#heading-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`img` or `image`](https://www.w3.org/TR/wai-aria-1.2/#img) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants. |
| [`insertion`](https://www.w3.org/TR/wai-aria-1.2/#insertion) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`link`](https://www.w3.org/TR/wai-aria-1.2/#link) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`list`](https://www.w3.org/TR/wai-aria-1.2/#list) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`list`](https://www.w3.org/TR/wai-aria-1.2/#list) role. |
| [`listbox`](https://www.w3.org/TR/wai-aria-1.2/#listbox) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`listbox`](https://www.w3.org/TR/wai-aria-1.2/#listbox) role. |
| [`listitem`](https://www.w3.org/TR/wai-aria-1.2/#listitem) | N/A | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`log`](https://www.w3.org/TR/wai-aria-1.2/#log) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`main`](https://www.w3.org/TR/wai-aria-1.2/#main) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`marquee`](https://www.w3.org/TR/wai-aria-1.2/#marquee) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`math`](https://www.w3.org/TR/wai-aria-1.2/#math) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`menu`](https://www.w3.org/TR/wai-aria-1.2/#menu) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`menu`](https://www.w3.org/TR/wai-aria-1.2/#menu) role. |
| [`menubar`](https://www.w3.org/TR/wai-aria-1.2/#menubar) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`menubar`](https://www.w3.org/TR/wai-aria-1.2/#menubar) role. |
| [`menuitem`](https://www.w3.org/TR/wai-aria-1.2/#menuitem) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`menuitemcheckbox`](https://www.w3.org/TR/wai-aria-1.2/#menuitemcheckbox) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`menuitemradio`](https://www.w3.org/TR/wai-aria-1.2/#menuitemradio) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`meter`](https://www.w3.org/TR/wai-aria-1.2/#meter) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [meter](https://html.spec.whatwg.org/multipage/form-elements.html#the-meter-element) element descendants. |
| [`navigation`](https://www.w3.org/TR/wai-aria-1.2/#navigation) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`none`](https://www.w3.org/TR/wai-aria-1.2/#none) | N/A | [Transparent](https://html.spec.whatwg.org/multipage/dom.html#transparent-content-models) |
| [`note`](https://www.w3.org/TR/wai-aria-1.2/#note) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`option`](https://www.w3.org/TR/wai-aria-1.2/#option) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`paragraph`](https://www.w3.org/TR/wai-aria-1.2/#paragraph) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`presentation`](https://www.w3.org/TR/wai-aria-1.2/#presentation) | N/A | [Transparent](https://html.spec.whatwg.org/multipage/dom.html#transparent-content-models) |
| [`progressbar`](https://www.w3.org/TR/wai-aria-1.2/#progressbar) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [progress](https://html.spec.whatwg.org/multipage/form-elements.html#the-progress-element) element descendants. |
| [`radio`](https://www.w3.org/TR/wai-aria-1.2/#radio) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`radiogroup`](https://www.w3.org/TR/wai-aria-1.2/#radiogroup) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`region`](https://www.w3.org/TR/wai-aria-1.2/#region) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`row`](https://www.w3.org/TR/wai-aria-1.2/#row) | N/A | Refer to the "Required Owned Elements" as defined for the ARIA [`row`](https://www.w3.org/TR/wai-aria-1.2/#row) role. |
| [`rowgroup`](https://www.w3.org/TR/wai-aria-1.2/#rowgroup) | N/A | Refer to the "Required Owned Elements" as defined for the ARIA [`rowgroup`](https://www.w3.org/TR/wai-aria-1.2/#rowgroup) role. |
| [`rowheader`](https://www.w3.org/TR/wai-aria-1.2/#rowheader) | N/A | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`scrollbar`](https://www.w3.org/TR/wai-aria-1.2/#scrollbar) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`search`](https://www.w3.org/TR/wai-aria-1.2/#search) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`searchbox`](https://www.w3.org/TR/wai-aria-1.2/#searchbox) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`separator`](https://www.w3.org/TR/wai-aria-1.2/#separator) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) (if focusable) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`slider`](https://www.w3.org/TR/wai-aria-1.2/#slider) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`spinbutton`](https://www.w3.org/TR/wai-aria-1.2/#spinbutton) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`status`](https://www.w3.org/TR/wai-aria-1.2/#status) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`strong`](https://www.w3.org/TR/wai-aria-1.2/#strong) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`subscript`](https://www.w3.org/TR/wai-aria-1.2/#subscript) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`superscript`](https://www.w3.org/TR/wai-aria-1.2/#superscript) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`switch`](https://www.w3.org/TR/wai-aria-1.2/#switch) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`tab`](https://www.w3.org/TR/wai-aria-1.2/#tab) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, and no descendants with a `tabindex` attribute specified. |
| [`table`](https://www.w3.org/TR/wai-aria-1.2/#table) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`table`](https://www.w3.org/TR/wai-aria-1.2/#table) role. |
| [`tablist`](https://www.w3.org/TR/wai-aria-1.2/#tablist) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA [`tablist`](https://www.w3.org/TR/wai-aria-1.2/#tablist) role. |
| [`tabpanel`](https://www.w3.org/TR/wai-aria-1.2/#tabpanel) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) |
| [`term`](https://www.w3.org/TR/wai-aria-1.2/#term) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`textbox`](https://www.w3.org/TR/wai-aria-1.2/#textbox) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`time`](https://www.w3.org/TR/wai-aria-1.2/#time) | - [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) - [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) - [Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`timer`](https://www.w3.org/TR/wai-aria-1.2/#timer) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`toolbar`](https://www.w3.org/TR/wai-aria-1.2/#toolbar) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) but with no [main](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element descendants. |
| [`tooltip`](https://www.w3.org/TR/wai-aria-1.2/#tooltip) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |
| [`tree`](https://www.w3.org/TR/wai-aria-1.2/#tree) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA `tree` role. |
| [`treegrid`](https://www.w3.org/TR/wai-aria-1.2/#treegrid) | [Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) | Refer to the "Required Owned Elements" as defined for the ARIA `treegrid` role. |
| [`treeitem`](https://www.w3.org/TR/wai-aria-1.2/#treeitem) | [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) | [Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) |

## 6. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *NOT RECOMMENDED*, *SHOULD*, and *SHOULD NOT* in this document
are to be interpreted as described in
[BCP 14](https://www.rfc-editor.org/info/bcp14)
[[RFC2119](#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")] [[RFC8174](#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")]
when, and only when, they appear in all
capitals, as shown here.

### 6.1 Conformance checking requirements

Conformance checkers that claim support for checking ARIA in HTML documents
*MUST* implement checks for the conformance requirements for use of the ARIA `role`
and `aria-*` attributes on [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) as defined in this specification.

A conforming document *MUST NOT* contain any elements with author defined `role`
or `aria-*` attributes with values other than those which, per this specification,
authors *MAY* use on each [HTML element](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) in [4. 
Document conformance requirements for use of ARIA attributes in HTML](#docconformance).
Conformance checkers *SHOULD* flag instances where authors are explicitly providing
an element with a `role` which matches its
[implicit ARIA semantics](https://www.w3.org/TR/wai-aria-1.2/#implicit_semantics) as failures,
as it is *NOT RECOMMENDED* for authors to explicitly set these roles.

A conformance checker *MAY* define their own terminology, and level or levels of
severity, when surfacing document failures to conform to this specification.

## 7. Privacy and security considerations

*This section is non-normative.*

This specification does not define the features of [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")],
[[dpub-aria-1.0](#bib-dpub-aria-1.0 "Digital Publishing WAI-ARIA Module 1.0")] or [[HTML](#bib-html "HTML Standard")]. Rather it provides rules and guidance for conformance
checkers that claim support for checking ARIA in HTML, as well as providing guidance to authors.

Therefore, there are no known privacy or security impacts of this specification,
as it defines no new features to introduce potential concern.

## A. References

### A.1 Normative references

[accname-1.2]
:   [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/). Bryan Garaventa; Melanie Sumner. W3C. 17 June 2025. W3C Working Draft. URL: <https://www.w3.org/TR/accname-1.2/>

[dpub-aria-1.0]
:   [Digital Publishing WAI-ARIA Module 1.0](https://www.w3.org/TR/dpub-aria-1.0/). Matt Garrish; Tzviya Siegman; Markus Gylling; Shane McCarron. W3C. 14 December 2017. W3C Recommendation. URL: <https://www.w3.org/TR/dpub-aria-1.0/>

[dpub-aria-1.1]
:   [Digital Publishing WAI-ARIA Module 1.1](https://www.w3.org/TR/dpub-aria-1.1/). Matt Garrish; Tzviya Siegman. W3C. 12 June 2025. W3C Recommendation. URL: <https://www.w3.org/TR/dpub-aria-1.1/>

[html]
:   [HTML Standard](https://html.spec.whatwg.org/multipage/). Anne van Kesteren; Domenic Denicola; Dominic Farolino; Ian Hickson; Philip Jägenstedt; Simon Pieters. WHATWG. Living Standard. URL: <https://html.spec.whatwg.org/multipage/>

[html-aam-1.0]
:   [HTML Accessibility API Mappings 1.0](https://www.w3.org/TR/html-aam-1.0/). Scott O'Hara; Rahim Abdi. W3C. 30 July 2025. W3C Working Draft. URL: <https://www.w3.org/TR/html-aam-1.0/>

[infra]
:   [Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[RFC2119]
:   [Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]
:   [Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[svg-aam-1.0]
:   [SVG Accessibility API Mappings](https://www.w3.org/TR/svg-aam-1.0/). Amelia Bellamy-Royds; Ian Pouncey. W3C. 10 May 2018. W3C Working Draft. URL: <https://www.w3.org/TR/svg-aam-1.0/>

[wai-aria-1.1]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/). Joanmarie Diggs; Shane McCarron; Michael Cooper; Richard Schwerdtfeger; James Craig. W3C. 14 December 2017. W3C Recommendation. URL: <https://www.w3.org/TR/wai-aria-1.1/>

[wai-aria-1.2]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/). Joanmarie Diggs; James Nurthen; Michael Cooper; Carolyn MacLeod. W3C. 6 June 2023. W3C Recommendation. URL: <https://www.w3.org/TR/wai-aria-1.2/>

### A.2 Informative references

[using-aria]
:   [Using ARIA](https://www.w3.org/TR/using-aria/). Steve Faulkner; David MacDonald. W3C. 27 September 2018. W3C Working Draft. URL: <https://www.w3.org/TR/using-aria/>

[wai-aria-practices-1.2]
:   [WAI-ARIA Authoring Practices 1.2](https://www.w3.org/TR/wai-aria-practices-1.2/). Matthew King; JaEun Jemma Ku; James Nurthen; Zoë Bijl; Michael Cooper. W3C. 19 May 2022. W3C Working Group Note. URL: <https://www.w3.org/TR/wai-aria-practices-1.2/>

[↑](#title)

[Permalink](#dfn-any-role)

**Referenced in:**

- [§ 4. Document conformance requirements for use of ARIA attributes in HTML](#ref-for-dfn-any-role-1 "§ 4. Document conformance requirements for use of ARIA attributes in HTML") [(2)](#ref-for-dfn-any-role-2 "Reference 2") [(3)](#ref-for-dfn-any-role-3 "Reference 3") [(4)](#ref-for-dfn-any-role-4 "Reference 4") [(5)](#ref-for-dfn-any-role-5 "Reference 5") [(6)](#ref-for-dfn-any-role-6 "Reference 6") [(7)](#ref-for-dfn-any-role-7 "Reference 7") [(8)](#ref-for-dfn-any-role-8 "Reference 8") [(9)](#ref-for-dfn-any-role-9 "Reference 9") [(10)](#ref-for-dfn-any-role-10 "Reference 10") [(11)](#ref-for-dfn-any-role-11 "Reference 11") [(12)](#ref-for-dfn-any-role-12 "Reference 12") [(13)](#ref-for-dfn-any-role-13 "Reference 13") [(14)](#ref-for-dfn-any-role-14 "Reference 14") [(15)](#ref-for-dfn-any-role-15 "Reference 15") [(16)](#ref-for-dfn-any-role-16 "Reference 16") [(17)](#ref-for-dfn-any-role-17 "Reference 17") [(18)](#ref-for-dfn-any-role-18 "Reference 18") [(19)](#ref-for-dfn-any-role-19 "Reference 19") [(20)](#ref-for-dfn-any-role-20 "Reference 20") [(21)](#ref-for-dfn-any-role-21 "Reference 21") [(22)](#ref-for-dfn-any-role-22 "Reference 22") [(23)](#ref-for-dfn-any-role-23 "Reference 23") [(24)](#ref-for-dfn-any-role-24 "Reference 24") [(25)](#ref-for-dfn-any-role-25 "Reference 25") [(26)](#ref-for-dfn-any-role-26 "Reference 26") [(27)](#ref-for-dfn-any-role-27 "Reference 27") [(28)](#ref-for-dfn-any-role-28 "Reference 28") [(29)](#ref-for-dfn-any-role-29 "Reference 29") [(30)](#ref-for-dfn-any-role-30 "Reference 30") [(31)](#ref-for-dfn-any-role-31 "Reference 31") [(32)](#ref-for-dfn-any-role-32 "Reference 32") [(33)](#ref-for-dfn-any-role-33 "Reference 33") [(34)](#ref-for-dfn-any-role-34 "Reference 34") [(35)](#ref-for-dfn-any-role-35 "Reference 35") [(36)](#ref-for-dfn-any-role-36 "Reference 36") [(37)](#ref-for-dfn-any-role-37 "Reference 37") [(38)](#ref-for-dfn-any-role-38 "Reference 38") [(39)](#ref-for-dfn-any-role-39 "Reference 39") [(40)](#ref-for-dfn-any-role-40 "Reference 40") [(41)](#ref-for-dfn-any-role-41 "Reference 41") [(42)](#ref-for-dfn-any-role-42 "Reference 42") [(43)](#ref-for-dfn-any-role-43 "Reference 43") [(44)](#ref-for-dfn-any-role-44 "Reference 44") [(45)](#ref-for-dfn-any-role-45 "Reference 45") [(46)](#ref-for-dfn-any-role-46 "Reference 46") [(47)](#ref-for-dfn-any-role-47 "Reference 47") [(48)](#ref-for-dfn-any-role-48 "Reference 48") [(49)](#ref-for-dfn-any-role-49 "Reference 49") [(50)](#ref-for-dfn-any-role-50 "Reference 50") [(51)](#ref-for-dfn-any-role-51 "Reference 51")

[Permalink](#dfn-no-role)

**Referenced in:**

- [§ 4. Document conformance requirements for use of ARIA attributes in HTML](#ref-for-dfn-no-role-1 "§ 4. Document conformance requirements for use of ARIA attributes in HTML") [(2)](#ref-for-dfn-no-role-2 "Reference 2") [(3)](#ref-for-dfn-no-role-3 "Reference 3") [(4)](#ref-for-dfn-no-role-4 "Reference 4") [(5)](#ref-for-dfn-no-role-5 "Reference 5") [(6)](#ref-for-dfn-no-role-6 "Reference 6") [(7)](#ref-for-dfn-no-role-7 "Reference 7") [(8)](#ref-for-dfn-no-role-8 "Reference 8") [(9)](#ref-for-dfn-no-role-9 "Reference 9") [(10)](#ref-for-dfn-no-role-10 "Reference 10") [(11)](#ref-for-dfn-no-role-11 "Reference 11") [(12)](#ref-for-dfn-no-role-12 "Reference 12") [(13)](#ref-for-dfn-no-role-13 "Reference 13") [(14)](#ref-for-dfn-no-role-14 "Reference 14") [(15)](#ref-for-dfn-no-role-15 "Reference 15") [(16)](#ref-for-dfn-no-role-16 "Reference 16") [(17)](#ref-for-dfn-no-role-17 "Reference 17") [(18)](#ref-for-dfn-no-role-18 "Reference 18") [(19)](#ref-for-dfn-no-role-19 "Reference 19") [(20)](#ref-for-dfn-no-role-20 "Reference 20") [(21)](#ref-for-dfn-no-role-21 "Reference 21") [(22)](#ref-for-dfn-no-role-22 "Reference 22") [(23)](#ref-for-dfn-no-role-23 "Reference 23") [(24)](#ref-for-dfn-no-role-24 "Reference 24") [(25)](#ref-for-dfn-no-role-25 "Reference 25") [(26)](#ref-for-dfn-no-role-26 "Reference 26") [(27)](#ref-for-dfn-no-role-27 "Reference 27") [(28)](#ref-for-dfn-no-role-28 "Reference 28") [(29)](#ref-for-dfn-no-role-29 "Reference 29") [(30)](#ref-for-dfn-no-role-30 "Reference 30") [(31)](#ref-for-dfn-no-role-31 "Reference 31") [(32)](#ref-for-dfn-no-role-32 "Reference 32") [(33)](#ref-for-dfn-no-role-33 "Reference 33") [(34)](#ref-for-dfn-no-role-34 "Reference 34") [(35)](#ref-for-dfn-no-role-35 "Reference 35") [(36)](#ref-for-dfn-no-role-36 "Reference 36") [(37)](#ref-for-dfn-no-role-37 "Reference 37") [(38)](#ref-for-dfn-no-role-38 "Reference 38") [(39)](#ref-for-dfn-no-role-39 "Reference 39") [(40)](#ref-for-dfn-no-role-40 "Reference 40") [(41)](#ref-for-dfn-no-role-41 "Reference 41") [(42)](#ref-for-dfn-no-role-42 "Reference 42") [(43)](#ref-for-dfn-no-role-43 "Reference 43") [(44)](#ref-for-dfn-no-role-44 "Reference 44") [(45)](#ref-for-dfn-no-role-45 "Reference 45") [(46)](#ref-for-dfn-no-role-46 "Reference 46") [(47)](#ref-for-dfn-no-role-47 "Reference 47") [(48)](#ref-for-dfn-no-role-48 "Reference 48") [(49)](#ref-for-dfn-no-role-49 "Reference 49") [(50)](#ref-for-dfn-no-role-50 "Reference 50") [(51)](#ref-for-dfn-no-role-51 "Reference 51") [(52)](#ref-for-dfn-no-role-52 "Reference 52") [(53)](#ref-for-dfn-no-role-53 "Reference 53") [(54)](#ref-for-dfn-no-role-54 "Reference 54") [(55)](#ref-for-dfn-no-role-55 "Reference 55") [(56)](#ref-for-dfn-no-role-56 "Reference 56") [(57)](#ref-for-dfn-no-role-57 "Reference 57") [(58)](#ref-for-dfn-no-role-58 "Reference 58") [(59)](#ref-for-dfn-no-role-59 "Reference 59") [(60)](#ref-for-dfn-no-role-60 "Reference 60") [(61)](#ref-for-dfn-no-role-61 "Reference 61") [(62)](#ref-for-dfn-no-role-62 "Reference 62")

[Permalink](#dfn-naming-prohibited)

**Referenced in:**

- [§ Status of This Document](#ref-for-dfn-naming-prohibited-1 "§ Status of This Document")
- [§ 4. Document conformance requirements for use of ARIA attributes in HTML](#ref-for-dfn-naming-prohibited-2 "§ 4. Document conformance requirements for use of ARIA attributes in HTML") [(2)](#ref-for-dfn-naming-prohibited-3 "Reference 2") [(3)](#ref-for-dfn-naming-prohibited-4 "Reference 3") [(4)](#ref-for-dfn-naming-prohibited-5 "Reference 4") [(5)](#ref-for-dfn-naming-prohibited-6 "Reference 5") [(6)](#ref-for-dfn-naming-prohibited-7 "Reference 6") [(7)](#ref-for-dfn-naming-prohibited-8 "Reference 7") [(8)](#ref-for-dfn-naming-prohibited-9 "Reference 8") [(9)](#ref-for-dfn-naming-prohibited-10 "Reference 9") [(10)](#ref-for-dfn-naming-prohibited-11 "Reference 10") [(11)](#ref-for-dfn-naming-prohibited-12 "Reference 11") [(12)](#ref-for-dfn-naming-prohibited-13 "Reference 12") [(13)](#ref-for-dfn-naming-prohibited-14 "Reference 13") [(14)](#ref-for-dfn-naming-prohibited-15 "Reference 14") [(15)](#ref-for-dfn-naming-prohibited-16 "Reference 15") [(16)](#ref-for-dfn-naming-prohibited-17 "Reference 16") [(17)](#ref-for-dfn-naming-prohibited-18 "Reference 17") [(18)](#ref-for-dfn-naming-prohibited-19 "Reference 18") [(19)](#ref-for-dfn-naming-prohibited-20 "Reference 19") [(20)](#ref-for-dfn-naming-prohibited-21 "Reference 20") [(21)](#ref-for-dfn-naming-prohibited-22 "Reference 21") [(22)](#ref-for-dfn-naming-prohibited-23 "Reference 22") [(23)](#ref-for-dfn-naming-prohibited-24 "Reference 23") [(24)](#ref-for-dfn-naming-prohibited-25 "Reference 24") [(25)](#ref-for-dfn-naming-prohibited-26 "Reference 25") [(26)](#ref-for-dfn-naming-prohibited-27 "Reference 26") [(27)](#ref-for-dfn-naming-prohibited-28 "Reference 27") [(28)](#ref-for-dfn-naming-prohibited-29 "Reference 28") [(29)](#ref-for-dfn-naming-prohibited-30 "Reference 29") [(30)](#ref-for-dfn-naming-prohibited-31 "Reference 30") [(31)](#ref-for-dfn-naming-prohibited-32 "Reference 31") [(32)](#ref-for-dfn-naming-prohibited-33 "Reference 32") [(33)](#ref-for-dfn-naming-prohibited-34 "Reference 33") [(34)](#ref-for-dfn-naming-prohibited-35 "Reference 34") [(35)](#ref-for-dfn-naming-prohibited-36 "Reference 35") [(36)](#ref-for-dfn-naming-prohibited-37 "Reference 36") [(37)](#ref-for-dfn-naming-prohibited-38 "Reference 37") [(38)](#ref-for-dfn-naming-prohibited-39 "Reference 38") [(39)](#ref-for-dfn-naming-prohibited-40 "Reference 39") [(40)](#ref-for-dfn-naming-prohibited-41 "Reference 40") [(41)](#ref-for-dfn-naming-prohibited-42 "Reference 41")

[Permalink](#dfn-no-corresponding-role)

**Referenced in:**

- [§ 4. Document conformance requirements for use of ARIA attributes in HTML](#ref-for-dfn-no-corresponding-role-1 "§ 4. Document conformance requirements for use of ARIA attributes in HTML") [(2)](#ref-for-dfn-no-corresponding-role-2 "Reference 2") [(3)](#ref-for-dfn-no-corresponding-role-3 "Reference 3") [(4)](#ref-for-dfn-no-corresponding-role-4 "Reference 4") [(5)](#ref-for-dfn-no-corresponding-role-5 "Reference 5") [(6)](#ref-for-dfn-no-corresponding-role-6 "Reference 6") [(7)](#ref-for-dfn-no-corresponding-role-7 "Reference 7") [(8)](#ref-for-dfn-no-corresponding-role-8 "Reference 8") [(9)](#ref-for-dfn-no-corresponding-role-9 "Reference 9") [(10)](#ref-for-dfn-no-corresponding-role-10 "Reference 10") [(11)](#ref-for-dfn-no-corresponding-role-11 "Reference 11") [(12)](#ref-for-dfn-no-corresponding-role-12 "Reference 12") [(13)](#ref-for-dfn-no-corresponding-role-13 "Reference 13") [(14)](#ref-for-dfn-no-corresponding-role-14 "Reference 14") [(15)](#ref-for-dfn-no-corresponding-role-15 "Reference 15") [(16)](#ref-for-dfn-no-corresponding-role-16 "Reference 16") [(17)](#ref-for-dfn-no-corresponding-role-17 "Reference 17") [(18)](#ref-for-dfn-no-corresponding-role-18 "Reference 18") [(19)](#ref-for-dfn-no-corresponding-role-19 "Reference 19") [(20)](#ref-for-dfn-no-corresponding-role-20 "Reference 20") [(21)](#ref-for-dfn-no-corresponding-role-21 "Reference 21") [(22)](#ref-for-dfn-no-corresponding-role-22 "Reference 22") [(23)](#ref-for-dfn-no-corresponding-role-23 "Reference 23") [(24)](#ref-for-dfn-no-corresponding-role-24 "Reference 24") [(25)](#ref-for-dfn-no-corresponding-role-25 "Reference 25") [(26)](#ref-for-dfn-no-corresponding-role-26 "Reference 26") [(27)](#ref-for-dfn-no-corresponding-role-27 "Reference 27") [(28)](#ref-for-dfn-no-corresponding-role-28 "Reference 28") [(29)](#ref-for-dfn-no-corresponding-role-29 "Reference 29") [(30)](#ref-for-dfn-no-corresponding-role-30 "Reference 30") [(31)](#ref-for-dfn-no-corresponding-role-31 "Reference 31") [(32)](#ref-for-dfn-no-corresponding-role-32 "Reference 32") [(33)](#ref-for-dfn-no-corresponding-role-33 "Reference 33") [(34)](#ref-for-dfn-no-corresponding-role-34 "Reference 34") [(35)](#ref-for-dfn-no-corresponding-role-35 "Reference 35") [(36)](#ref-for-dfn-no-corresponding-role-36 "Reference 36") [(37)](#ref-for-dfn-no-corresponding-role-37 "Reference 37") [(38)](#ref-for-dfn-no-corresponding-role-38 "Reference 38") [(39)](#ref-for-dfn-no-corresponding-role-39 "Reference 39") [(40)](#ref-for-dfn-no-corresponding-role-40 "Reference 40") [(41)](#ref-for-dfn-no-corresponding-role-41 "Reference 41") [(42)](#ref-for-dfn-no-corresponding-role-42 "Reference 42") [(43)](#ref-for-dfn-no-corresponding-role-43 "Reference 43") [(44)](#ref-for-dfn-no-corresponding-role-44 "Reference 44") [(45)](#ref-for-dfn-no-corresponding-role-45 "Reference 45") [(46)](#ref-for-dfn-no-corresponding-role-46 "Reference 46") [(47)](#ref-for-dfn-no-corresponding-role-47 "Reference 47") [(48)](#ref-for-dfn-no-corresponding-role-48 "Reference 48") [(49)](#ref-for-dfn-no-corresponding-role-49 "Reference 49") [(50)](#ref-for-dfn-no-corresponding-role-50 "Reference 50") [(51)](#ref-for-dfn-no-corresponding-role-51 "Reference 51")

(() => {
// @ts-check
if (document.respec) {
document.respec.ready.then(setupVarHighlighter);
} else {
setupVarHighlighter();
}
function setupVarHighlighter() {
document
.querySelectorAll("var")
.forEach(varElem => varElem.addEventListener("click", highlightListener));
}
function highlightListener(ev) {
ev.stopPropagation();
const { target: varElem } = ev;
const hightligtedElems = highlightVars(varElem);
const resetListener = () => {
const hlColor = getHighlightColor(varElem);
hightligtedElems.forEach(el => removeHighlight(el, hlColor));
[...HL\_COLORS.keys()].forEach(key => HL\_COLORS.set(key, true));
};
if (hightligtedElems.length) {
document.body.addEventListener("click", resetListener, { once: true });
}
}
// availability of highlight colors. colors from var.css
const HL\_COLORS = new Map([
["respec-hl-c1", true],
["respec-hl-c2", true],
["respec-hl-c3", true],
["respec-hl-c4", true],
["respec-hl-c5", true],
["respec-hl-c6", true],
["respec-hl-c7", true],
]);
function getHighlightColor(target) {
// return current colors if applicable
const { value } = target.classList;
const re = /respec-hl-\w+/;
const activeClass = re.test(value) && value.match(re);
if (activeClass) return activeClass[0];
// first color preference
if (HL\_COLORS.get("respec-hl-c1") === true) return "respec-hl-c1";
// otherwise get some other available color
return [...HL\_COLORS.keys()].find(c => HL\_COLORS.get(c)) || "respec-hl-c1";
}
function highlightVars(varElem) {
const textContent = norm(varElem.textContent);
const parent = varElem.closest(".algorithm, section");
const highlightColor = getHighlightColor(varElem);
const varsToHighlight = [...parent.querySelectorAll("var")].filter(
el =>
norm(el.textContent) === textContent &&
el.closest(".algorithm, section") === parent
);
// update availability of highlight color
const colorStatus = varsToHighlight[0].classList.contains("respec-hl");
HL\_COLORS.set(highlightColor, colorStatus);
// highlight vars
if (colorStatus) {
varsToHighlight.forEach(el => removeHighlight(el, highlightColor));
return [];
} else {
varsToHighlight.forEach(el => addHighlight(el, highlightColor));
}
return varsToHighlight;
}
function removeHighlight(el, highlightColor) {
el.classList.remove("respec-hl", highlightColor);
// clean up empty class attributes so they don't come in export
if (!el.classList.length) el.removeAttribute("class");
}
function addHighlight(elem, highlightColor) {
elem.classList.add("respec-hl", highlightColor);
}
/\*\*
\* Same as `norm` from src/core/utils, but our build process doesn't allow
\* imports in runtime scripts, so duplicated here.
\* @param {string} str
\*/
function norm(str) {
return str.trim().replace(/\s+/g, " ");
}
})()(() => {
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