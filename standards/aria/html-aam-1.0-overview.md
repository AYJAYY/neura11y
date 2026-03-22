---
ai_context: Overview of HTML-AAM 1.0 scope, conformance, and general HTML-to-accessibility
  API rules.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/html-aam-1.0/
standard: HTML Accessibility API Mappings 1.0
status: normative
tags:
- aria
- html-aam
- overview
- html
- accessibility-api
title: HTML Accessibility API Mappings 1.0 Overview
---

# HTML Accessibility API Mappings 1.0 Overview

## Abstract

HTML Accessibility API Mappings (HTML-AAM) defines how [user agents](https://infra.spec.whatwg.org/#user-agent) map HTML [[HTML](#bib-html "HTML Standard")] elements and attributes to platform
[accessibility application programming interfaces (APIs)](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). It leverages and extends the
[Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/) and the [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) for use with the HTML host language. Documenting these mappings promotes interoperable exposure of roles, states, properties, and events
implemented by accessibility APIs and helps to ensure that this information appears in a manner consistent with author intent.

The HTML-AAM is part of the WAI-ARIA suite described in the
[WAI-ARIA Overview](https://www.w3.org/WAI/intro/aria.php).

## Status of This Document

*This section describes the status of this
document at the time of its publication. A list of current W3C
publications and the latest revision of this technical report can be found
in the
[W3C standards and drafts index](https://www.w3.org/TR/).*

Note

**This document is subject to change without notice.**

This document was initially developed by and with the approval of the [HTML Accessibility Taskforce](https://www.w3.org/WAI/PF/html-accessibility-tf.html), a joint task force of the
[Protocols and Formats Working Group](https://www.w3.org/WAI/PF/) and the [HTML Working Group](https://www.w3.org/html/wg/). Work continued with the successor groups
[Accessible Rich Internet Applications Working Group](https://www.w3.org/WAI/ARIA/) and the [Web Applications Working Group](https://www.w3.org/2019/webapps/). This
document is now maintained solely by the [Accessible Rich Internet Applications Working Group](https://www.w3.org/WAI/ARIA/).

This document was published by the [Accessible Rich Internet Applications Working Group](https://www.w3.org/groups/wg/aria) as
a Working Draft using the
[Recommendation track](https://www.w3.org/policies/process/20250818/#recs-and-notes).

Publication as a Working Draft does not
imply endorsement by W3C and its Members.

This is a draft document and may be updated, replaced, or obsoleted by other
documents at any time. It is inappropriate to cite this document as other
than a work in progress.

This document was produced by a group
operating under the
[W3C Patent
Policy](https://www.w3.org/policies/patent-policy/).
W3C maintains a
[public list of any patent disclosures](https://www.w3.org/groups/wg/aria/ipr)
made in connection with the deliverables of
the group; that page also includes
instructions for disclosing a patent. An individual who has actual
knowledge of a patent that the individual believes contains
[Essential Claim(s)](https://www.w3.org/policies/patent-policy/#def-essential)
must disclose the information in accordance with
[section 6 of the W3C Patent Policy](https://www.w3.org/policies/patent-policy/#sec-Disclosure).

This document is governed by the
[18 August 2025 W3C Process Document](https://www.w3.org/policies/process/20250818/).

## 1. Introduction

*This section is non-normative.*

This specification defines how HTML user agents respond to and expose [role](https://www.w3.org/TR/wai-aria/#dfn-role), [state](https://www.w3.org/TR/wai-aria/#dfn-state) and [property](https://www.w3.org/TR/wai-aria/#dfn-property) information provided for Web content. Unless indicated otherwise, an HTML
element or attribute with default [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/) semantics must be exposed to the platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) according to the relevant WAI-ARIA mappings defined in
the [Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/) specification.

In some cases, often due to features of the HTML host language or the accessibility API in question, an element or attribute's mapping differs from the corresponding ARIA mappings specified in
the [[core-aam-1.2](#bib-core-aam-1.2 "Core Accessibility API Mappings 1.2")]. Where an HTML element or attribute does not have any default WAI-ARIA semantics, the applicable mapping for each platform [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) is
defined by this specification.

This document also adapts the [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) specification for deriving the [accessible names](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) and
[accessible descriptions](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) of [[HTML](#bib-html "HTML Standard")] elements, and provides accessible implementation examples for specific HTML elements and
features.

Users often access HTML content using assistive technologies that rely on platform [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) to obtain and
interact with information from the page. This document is part of the following suite of accessibility API mapping specifications for content rendered by user agents:

- [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/)
- [Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/)
- HTML Accessibility API Mappings 1.0 (this specification)
- [MathML Accessibility API Mappings 1.0](https://w3c.github.io/mathml-aam/)
- [SVG Accessibility API Mappings](https://www.w3.org/TR/svg-aam-1.0/)

### 1.1 Accessibility APIs

[Accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) covered by this document are:

- MSAA with IAccessible2 1.3 [[IAccessible2](#bib-iaccessible2 "IAccessible2")]
- User Interface Automation [[UI-AUTOMATION](#bib-ui-automation "UI Automation")]
- ATK - Accessibility Toolkit [[ATK](#bib-atk "ATK - Accessibility Toolkit")] and Assistive Technology Service Provider Interface [[AT-SPI](#bib-at-spi "Assistive Technology Service Provider Interface")], referred to hereafter as "ATK/AT-SPI"
- macOS Accessibility Protocol [[AXAPI](#bib-axapi "The NSAccessibility Protocol for macOS")]

If user agent developers need to expose information using other [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api), it is recommended that they work closely with the developer of the platform where
the API runs, and assistive technology developers on that platform.

For more information regarding [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api), refer to [section 1.1 Accessibility APIs](https://www.w3.org/TR/core-aam-1.2/#intro_aapi) of the [Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/).

## 2. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, and *SHOULD* in this document
are to be interpreted as described in
[BCP 14](https://www.rfc-editor.org/info/bcp14)
[[RFC2119](#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")] [[RFC8174](#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")]
when, and only when, they appear in all
capitals, as shown here.

Normative sections provide requirements that user agents and assistive technologies *MUST* follow for an implementation to conform to this specification.

Non-normative (informative) sections provide information useful to understanding the specification. Such sections may contain examples of recommended practice, but it is not required to follow
such recommendations in order to conform to this specification.

### 2.1 Deprecated

There are currently no deprecated requirements.

## 3. Mapping HTML to Accessibility APIs

### 3.1 General Rules for Exposing WAI-ARIA Semantics

Note

WAI-ARIA support was first introduced to HTML in [[HTML5](#bib-html5 "HTML5")].

[User Agents](https://infra.spec.whatwg.org/#user-agent) *MUST* expose HTML elements or attributes with default WAI-ARIA semantics to the platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) in a way that conforms to
[General rules for exposing WAI-ARIA semantics](https://www.w3.org/TR/core-aam-1.2/#mapping_general) in the [Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/).

### 3.2 Conflicts Between Native Markup Semantics and WAI-ARIA

Where the host language is [[HTML](#bib-html "HTML Standard")], user agents *MUST* conform to
[Conflicts between native markup semantics and WAI-ARIA](https://www.w3.org/TR/core-aam-1.2/#mapping_conflicts) in the [Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/).

### 3.3 Exposing HTML Features That Do Not Directly Map to Accessibility APIs

HTML can include features that are not supported by [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) at the time of publication. There is not a one to one relationship between all features and
platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). When HTML roles, states and properties do not directly map to an [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api), and there is a method in the
API to expose a text string, user agents *MUST* expose the undefined role, states and properties via that method.

For HTML elements or attributes with default WAI-ARIA semantics, user agents *MUST* conform to
[Exposing attributes that do not directly map to accessibility API properties](https://www.w3.org/TR/core-aam-1.2/#mapping_nodirect) in
the [[core-aam-1.2](#bib-core-aam-1.2 "Core Accessibility API Mappings 1.2")].

### 3.4 Exposing HTML Features That Require a Minimum Role

A minimum role is the equivalent WAI-ARIA role an element will map to if the element does not have a more specific implicit role or platform role mappings, e.g., a non-generic
role. This can help ensure that users of assistive technologies get the best possible experience for commonly-used and valid HTML markup where otherwise a role would not be exposed.

A minimum role is provided when all of the following conditions are true:

- the author has **not** specified a valid explicit WAI-ARIA role to the element, **or** the specified role is either `none`, `presentation`, or `generic`;
- the element either has no implicit WAI-ARIA role or platform role mappings, or it has an implicit `generic` or `none` computed role;
- and the author has specified attributes which require a minimum role mapping for the element.

The [HTML Attribute State and Property Mappings](#html-attribute-state-and-property-mappings) section identifies the specific global attributes which would require an element map
to a minimum role.

When these conditions are met, user agents *MUST* expose an object using the mappings defined in CORE-AAM for the specified minimum role. If the element has multiple attributes specified which
require a minimum role be returned as the computed role for the element, prioritize the more specific role in the ARIA taxonomy.

## 5. Privacy considerations

In accordance with [Web Platform Design Principles](https://w3ctag.github.io/design-principles/#do-not-expose-use-of-assistive-tech), this specification provides no programmatic
interface to determine if information is being used by Assistive Technologies. However, this specification does allow an author to present different information to users of Assistive
Technologies from the information available to users who do not use Assistive Technologies. This is possible using many features of the ARIA and CORE-AAM specifications, just as this is
possible using many other parts of the web technology stack. This content disparity could be abused to perform
[active fingerprinting](https://www.w3.org/TR/fingerprinting-guidance/#active-0) of users of Assistive Technologies.

## 6. Security considerations

This specification introduces no new security considerations.