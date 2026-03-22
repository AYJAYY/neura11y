---
ai_context: Overview of Core-AAM 1.2 scope, conformance, accessibility API model,
  and algorithm context.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/core-aam-1.2/
standard: Core Accessibility API Mappings 1.2
status: normative
tags:
- aria
- core-aam
- overview
- accessibility-api
- mappings
title: Core Accessibility API Mappings 1.2 Overview
---

# Core Accessibility API Mappings 1.2 Overview

## Abstract

This document describes how [user agents](https://infra.spec.whatwg.org/#user-agent) should expose semantics of web content languages to [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). This helps users with disabilities to obtain and interact with information using [assistive technologies](https://www.w3.org/TR/wai-aria/#assistive-technology). Documenting these mappings promotes interoperable exposure of
roles, states, properties, and events implemented by accessibility APIs and helps to ensure that this information appears in a manner consistent with author intent.

This Core Accessibility API Mappings specification defines support that applies across multiple content technologies, including general keyboard navigation support and mapping of
general-purpose [roles](https://www.w3.org/TR/wai-aria/#dfn-role), states, and properties provided in Web content via
[WAI-ARIA](https://www.w3.org/TR/wai-aria-1.2/)
[[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")]. Other Accessibility API Mappings specifications depend on and extend this Core specification for specific technologies, including native technology features and WAI-ARIA
extensions. This document updates and will eventually supersede the guidance in the [Core Accessibility API Mappings 1.1](https://www.w3.org/TR/core-aam-1.1/) [[CORE-AAM-1.1](#bib-core-aam-1.1 "Core Accessibility API Mappings 1.1")] W3C
Recommendation. It is part of the WAI-ARIA suite described in the
[WAI-ARIA Overview](https://www.w3.org/WAI/intro/aria.php).

## Status of This Document

*This section describes the status of this
document at the time of its publication. A list of current W3C
publications and the latest revision of this technical report can be found
in the
[W3C standards and drafts index](https://www.w3.org/TR/).*

The Accessible Rich Internet Applications Working Group seeks feedback on any aspect of the specification. When submitting feedback, please consider issues in the context of the companion
documents. To comment, [file an issue in the W3C core-aam GitHub repository](https://github.com/w3c/core-aam/issues/new). If this is
not feasible, send email to [public-aria@w3.org](mailto:public-aria@w3.org?subject=Comment%20on%20Core-AAM%201.2) ([comment archive](http://lists.w3.org/Archives/Public/public-aria/)). In-progress updates to the document may be viewed in the [publicly visible editors' draft](http://w3c.github.io/core-aam/).

**Living specification** — This document is maintained as a living specification. For the latest normative version, visit
[Core Accessibility API Mappings](https://www.w3.org/TR/core-aam-1.2/).

This document was published by the [Accessible Rich Internet Applications Working Group](https://www.w3.org/groups/wg/aria) as
a Candidate Recommendation Draft using the
[Recommendation track](https://www.w3.org/policies/process/20250818/#recs-and-notes).

Publication as a Candidate Recommendation does not
imply endorsement by W3C and its Members. A Candidate Recommendation Draft integrates
changes from the previous Candidate Recommendation that the Working Group
intends to include in a subsequent Candidate Recommendation Snapshot.

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

The Core Accessibility API Mappings specifies how WAI-ARIA [roles](https://www.w3.org/TR/wai-aria/#dfn-role), [states](https://www.w3.org/TR/wai-aria/#dfn-state), and
[properties](https://www.w3.org/TR/wai-aria/#dfn-property) are expected to be exposed by user agents via platform accessibility APIs. It is part of a set of resources that
define and support the WAI-ARIA specification which includes the following documents:

- Accessible Rich Internet Applications (WAI-ARIA) 1.2 [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")], a W3C recommendation,
  defines the WAI-ARIA standard.
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/), describes how web content developers can develop accessible rich internet applications using WAI-ARIA. It provides detailed
  advice and examples directed primarily to web application developers, yet also useful to user agent and developers of assistive technologies.
- [Roadmap for Accessible Rich Internet Applications (WAI-ARIA Roadmap)](https://www.w3.org/TR/wai-aria-roadmap/)
  [[WAI-ARIA-ROADMAP](#bib-wai-aria-roadmap "Roadmap for Accessible Rich Internet Applications (WAI-ARIA Roadmap)")], defines the path to make rich web content accessible, including steps already taken, remaining future steps, and a time line.

For an introduction to WAI-ARIA, see the
[WAI-ARIA Overview](https://www.w3.org/WAI/intro/aria.php).

### 1.1 Accessibility APIs

[Accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) make it possible to communicate accessibility information about user interfaces to assistive
technologies. This information includes:

1. Descriptive properties (role, name, value, position, etc.)
2. Transient states (pressed, focused, etc.)
3. Events (text changed, button was clicked, checkbox was toggled)
4. Actions the user might take (click, check/toggle, drag, etc.)
5. Relationships (parent/child, description/described object, previous object/next object, etc.)
6. Textual content

Accessibility APIs covered by this specification are:

- MSAA with IAccessible2 1.3 [[IAccessible2](#bib-iaccessible2 "IAccessible2")]
- User Interface Automation [[UI-AUTOMATION](#bib-ui-automation "UI Automation")]
- ATK - Accessibility Toolkit [[ATK](#bib-atk "ATK - Accessibility Toolkit")] and Assistive Technology Service Provider Interface [[AT-SPI](#bib-at-spi "Assistive Technology Service Provider Interface")], referred to hereafter as "ATK/AT-SPI"
- macOS Accessibility Protocol [[AXAPI](#bib-axapi "The NSAccessibility Protocol for macOS")]
- [Android](https://developer.android.com/reference/android/view/accessibility/package-summary) [[Android-Accessibility-API](#bib-android-accessibility-api "Android Accessibility API")]

The [WAI-ARIA 1.0 User Agent Implementation Guide](https://www.w3.org/TR/wai-aria-implementation/) included mappings for [[UIA-EXPRESS](#bib-uia-express "The IAccessibleEx Interface")], also known as IAccessibleEx,
which was implemented in Microsoft Internet Explorer 8.0 - 11. New implementations are strongly encouraged to use [UI Automation](https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification) instead.

If user agent developers need to expose information using other accessibility APIs, it is recommended that they work closely with the
developer of the platform where the API runs, and assistive technology developers on that platform.

### 1.2 Comparing Accessibility APIs

For various technological and historical reasons, accessibility APIs do not all work in the same way. In many cases, there is no simple one-to-one relationship between how each of them names
or exposes roles, states, and properties to assistive technologies. The following subsections describe a few of the distinguishing characteristics of some of the APIs.

#### 1.2.1 ATK/AT-SPI

MSAA, IAccessible2, UIA, and AX API each define an API that is shared by both the software application exposing information about its content and interactive components, and the assistive
technology consuming that information. Conversely, Linux/GNOME separates that shared interface into its two aspects, each represented by a different accessibility API: ATK or AT-SPI.

ATK defines an interface that is implemented by software in order to expose accessibility information, whereas AT-SPI is a desktop service that gathers accessibility information from
active applications and relays it to other interested applications, usually assistive technologies.

For example, the GNOME GUI toolkit [GTK], implements the relevant aspects of ATK for each widget (menu, combobox, checkbox, etc.) in order that GTK widgets expose accessibility information
about themselves. AT-SPI then acquires the information from applications built with GTK and makes it available to interested parties.

ATK is most relevant to implementors, whereas AT-SPI is relevant to consumers. In the context of mapping WAI-ARIA roles, states and properties, user agents are implementors and use ATK.
Assistive Technologies are consumers, and use AT-SPI.

#### 1.2.2 UIA (UI Automation)

UI Automation expresses every element of the application user interface as an automation element. Automation elements form the nodes of the application accessibility tree, that can be
queried, traversed and interacted with by automation clients.

There are several concepts central to UI Automation:

- Automation element - controls and some application content are presented as automation elements.
- Element properties - Automation elements have several common properties describing native framework element characteristics in an agnostic way that all automation clients can understand.
  There are several ways to access element property values, described below.
- Control Patterns - Some common interactivity in different frameworks is expressed as control patterns in UIA, allowing different automation clients to interact with controls using common
  programmatic interfaces.
- Events - Similar to other accessibility APIs, automation elements support various events that allow automation providers to notify clients on important state changes.

All automation elements inherit from the `IUIAutomationElement` interface and all properties that are not specific to a particular control pattern can be queried through that
interface. There are several ways to access UI Automation element properties:

- Direct property accessors to the current values - `Current{PropertyName}`, e.g. `IUIAutomationElement::CurrentName` for the `Name` property
- Cached property accessors - `Cached{PropertyName}`, e.g. `IUIAutomationElement::CachedName` for the `Name` property. Using cached values is preferred
  when providers and clients are used in remote environments.
- `GetCurrentPropertyValue` and passing the UIA Property ID enumeration value corresponding to that property to get the current value, e.g.
  `IUIAutomationElement::GetCurrentPropertyValue(UIA_NamePropertyId)` for the `Name` property.
- `GetCachedPropertyValue` and passing the UIA Property ID enumeration value corresponding to that property to get the cached value, e.g.
  `IUIAutomationElement::GetCachedPropertyValue(UIA_NamePropertyId)` for the `Name` property.

Properties for specific UIA control patterns are queried the same way using relevant control pattern interfaces. Taking Toggle Pattern as an example, to query the ToggleState property
clients can use IUIAutomationTogglePattern::CurrentToggleState or IUIAutomationTogglePattern::GetCurrentPropertyValue(UIA\_ToggleToggleStatePropertyId) to get the current value.

The property mappings in this specification provide the `{PropertyName}` and do not specify all specific ways to access the property value. Automation clients can access current
or cached values using conventions described above, depending on specific needs and coding style conventions.

#### 1.2.3 Android Accessibility API

Android accessibility services and applications both express user interface elements as a tree of `AccessibilityNodeInfo` objects. Accessibility services receive events,
traverse the `AccessibilityNodeInfo` tree, retrieve properties, and perform actions on a node. Conversely, Android applications build the `AccessibilityNodeInfo` tree
indirectly by constructing views or composables, or directly via an `AccessibilityNodeProvider`. They then subsequently fire events, and handle actions.

For WAI-ARIA implementers, of particular interest is the mapping into properties, actions, and events on `AccessibilityNodeInfo` and `AccessibilityEvent`.

#### 1.2.4 Accessible Names and Descriptions

Each platform accessibility API includes a way to assign and retrieve [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) and
[accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) properties for each [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) created in the
[accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). How these properties are implemented and what they are called vary depending on the API.

For instance, in MSAA, all [accessible objects](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) support the `accName` property, which stores the object's
[accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name). Where the object also supports having an
[accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description), MSAA stores this property in the object's `accDescription` property.

Software using ATK can read and write to an object's `accessible-name` and `accessible-description` properties. In turn, AT-SPI can query the values of those
properties through its `atspi_accessible_get_name` and `atspi_accessible_get_description` functions.

Automation elements in the UIA accessibility tree have a `Name` property. Where the object also supports having an
[accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description), UIA stores this property in the object's `FullDescription` property.

An object's [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description), where provided by
[`aria-description`](#aria-description) or [`aria-describedby`](#aria-describedby), should be exposed in the `accessibilityCustomContent` API. Otherwise, it should be exposed as `AXHelp`.

In Android, accessible names map to a number of properties defined on `AccessibilityNodeInfo` such as content description, supplemental description, and text.

For more detail, see the Accessible Name and Description Computation specification.

## 2. Conformance

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words *MAY*, *MUST*, *MUST NOT*, *SHOULD*, and *SHOULD NOT* in this document
are to be interpreted as described in
[BCP 14](https://www.rfc-editor.org/info/bcp14)
[[RFC2119](#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")] [[RFC8174](#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")]
when, and only when, they appear in all
capitals, as shown here.

Normative sections provide requirements that user agents and assistive technologies *MUST* follow for an implementation to conform to this specification.

Non-normative (informative) sections provide information useful to understanding the specification. Such sections may contain examples of recommended practice, but it is not required to follow
such recommendations in order to conform to this specification.

### 2.1 Features Deprecated in WAI-ARIA

The WAI-ARIA specification [lists some features as deprecated](#deprecated "Broken local reference found in document."). Although this means authors are encouraged not to use such features, it is expected
that the features could still be used in legacy content. Therefore, it is important that user agents continue to map these features to accessibility APIs, and doing so is part of conformance
to this specification. When future versions of the WAI-ARIA specification change such features from deprecated to removed, they will be removed from the mappings as well and user agents will
no longer be asked to continue support for those features.

## 3. Mapping WAI-ARIA to Accessibility APIs

## 5. Privacy considerations

In accordance with [Web Platform Design Principles](https://w3ctag.github.io/design-principles/#do-not-expose-use-of-assistive-tech), this specification provides no programmatic
interface to determine if information is being used by Assistive Technologies. However, this specification does allow an author to present different information to users of Assistive
Technologies from the information available to users who do not use Assistive Technologies. This is possible using many features of the ARIA and CORE-AAM specifications, just as this is
possible using many other parts of the web technology stack. This content disparity could be abused to perform
[active fingerprinting](https://www.w3.org/TR/fingerprinting-guidance/#active-0) of users of Assistive Technologies.

## 6. Security considerations

This specification introduces no new security considerations.