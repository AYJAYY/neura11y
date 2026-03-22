---
ai_context: Auto-fetched full Core-AAM 1.2 specification. Prefer split core-aam-1.2-*.md
  files for AI use.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/core-aam-1.2/
standard: Core Accessibility API Mappings 1.2
status: normative
tags:
- aria
- core-aam
- accessibility-api
- mappings
title: Core Accessibility API Mappings 1.2 (Full Fetched)
---

[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

# Core Accessibility API Mappings 1.2

[W3C Candidate Recommendation Draft](https://www.w3.org/standards/types#CRD) 11 March 2026

More details about this document

This version:
:   <https://www.w3.org/TR/2026/CRD-core-aam-1.2-20260311/>

Latest published version:
:   <https://www.w3.org/TR/core-aam-1.2/>

Latest editor's draft:
:   <https://w3c.github.io/core-aam/>

History:
:   <https://www.w3.org/standards/history/core-aam-1.2/>
:   [Commit history](https://github.com/w3c/core-aam/commits/)

Implementation report:
:   <https://w3c.github.io/test-results/core-aam-1.2/>

Latest Recommendation:
:   <https://www.w3.org/TR/core-aam-1.1/>

Editors:
:   Valerie Young ([Igalia, S.L.](https://www.igalia.com))
:   [Cynthia Shelly](mailto:buphie@gmail.com) (W3C Invited Expert)

Former editors:
:   Alexander Surkov ([Igalia, S.L.](https://www.igalia.com)) (Editor until August 2025)
:   Joanmarie Diggs ([Igalia, S.L.](https://www.igalia.com)) (Editor until October 2022)
:   Richard Schwerdtfeger ([Knowbility](https://www.knowbility.org/)) (Editor until October 2017)
:   Joseph Scheuhammer ([Inclusive Design Research Centre, OCAD University](http://idrc.ocad.ca)) (Editor until May 2017)
:   Andi Snow-Weaver ([IBM](http://www.ibm.com)) (Editor until December 2012)
:   Aaron Leventhal ([IBM](http://www.ibm.com)) (Editor until January 2009)
:   Michael Cooper ([W3C](https://www.w3.org)) (Editor until July 2023)

Platform Mapping Maintainers:
:   Benjamin Beaudry ([Microsoft Corp.](https://microsoft.com/)) (UIA)
:   James Craig ([Apple, Inc.](https://apple.com/accessibility)) (AX API)
:   Joanmarie Diggs ([Igalia, S.L.](https://www.igalia.com)) (ATK / AT-SPI)
:   Alexander Surkov ([Igalia, S.L.](https://www.igalia.com)) (MSAA, IAccessible2)
:   David Tseng (Google LLC) (Android Accessibility API)

Feedback:
:   [GitHub w3c/core-aam](https://github.com/w3c/core-aam/)
    ([pull requests](https://github.com/w3c/core-aam/pulls/),
    [new issue](https://github.com/w3c/core-aam/issues/new/choose),
    [open issues](https://github.com/w3c/core-aam/issues/))

[Copyright](https://www.w3.org/policies/#copyright)
©
2014-2026
[World Wide Web Consortium](https://www.w3.org/).
W3C®
[liability](https://www.w3.org/policies/#Legal_Disclaimer),
[trademark](https://www.w3.org/policies/#W3C_Trademarks) and
[permissive document license](https://www.w3.org/copyright/software-license-2023/ "W3C Software and Document Notice and License") rules apply.

---

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

### 3.1 General rules for exposing WAI-ARIA semantics

Where supported by the platform [Accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api), [user agents](https://infra.spec.whatwg.org/#user-agent) expose WAI-ARIA
[semantics](https://www.w3.org/TR/wai-aria/#dfn-semantics) through the standard mechanisms of the desktop accessibility API. For example, for
WAI-ARIA [widgets](https://www.w3.org/TR/wai-aria/#dfn-widget), compare how the widget is exposed in a similar desktop widget. In general most
WAI-ARIA widget capabilities are exposed through the [role](https://www.w3.org/TR/wai-aria/#dfn-role), value, Boolean [states](https://www.w3.org/TR/wai-aria/#dfn-state), and
relations of the accessibility API.

With respect to WAI-ARIA 1.0 and 1.1, accessibility APIs operate in one
direction only. User agents publish WAI-ARIA information (roles, states, and properties) via an accessibility
API, and an AT can acquire that information using the same
API. However, the other direction is not supported. WAI-ARIA 1.0 and 1.1 do
not define mechanisms for assistive technologies to directly modify WAI-ARIA information.

The terms "exposing", "mapping", and "including" refer to the creation of [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) [nodes](https://dom.spec.whatwg.org/#concept-node) within the
[accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), and populating these objects with [Accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) specific [states](https://www.w3.org/TR/wai-aria/#dfn-state) and [properties](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.").

### 3.2 Conflicts between native markup semantics and WAI-ARIA

WAI-ARIA roles, states, and properties are intended to add [semantic](https://www.w3.org/TR/wai-aria/#dfn-semantics) information when native host language
[elements](https://dom.spec.whatwg.org/#concept-element) with these semantics are not available, and are generally used on elements that have no native semantics of their own. They can also be used on elements that
have similar but not identical semantics to the intended object (for instance, a nested list could be used to represent a tree structure). This method can be part of a fallback strategy for
older browsers that have no WAI-ARIA implementation, or because native presentation of the repurposed element reduces the amount of
style and/or script needed. Except for the cases outlined below, [user agents](https://infra.spec.whatwg.org/#user-agent) *MUST* always use the WAI-ARIA semantics to define
how it exposes the element to [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api), rather than using the host language semantics.

Host languages can have features that have implicit WAI-ARIA semantics corresponding to [roles](https://www.w3.org/TR/wai-aria/#dfn-role). When a
WAI-ARIA role is provided that has a corresponding role in the accessibility
API, user agents *MUST* use the semantic of the WAI-ARIA role for processing,
not the native semantic, unless the role requires WAI-ARIA states and properties whose attributes are explicitly forbidden on the
native element by the host language. Values for roles do not conflict in the same way as values for states and properties, and because authors are expected to have a valid reason to provide
a WAI-ARIA role even on elements that would not normally be repurposed. For example, spin buttons are typically constructed from
text fields (`<input type="text">`) in order to get most of the default keyboard support. But, the native role, "text field", is not correct because it
does not properly communicate the additional features of a spin button. The author adds the WAI-ARIA role of
`spinbutton` (`<input type="text" role="spinbutton" ...>`) so that the control is properly mapped in the accessibility
API. When a WAI-ARIA role is provided that does not have a corresponding role
in the accessibility API, user agents *MAY* expose the native semantic in addition to the
WAI-ARIA role. If the host language element is overridden by a
WAI-ARIA role whose semantics or structure is not equivalent to the native host language semantics or to a subclass of those
semantics, then treat any child elements having roles specified as Allowed Accessibility Child Roles as having [presentation](#role-map-presentation) or
[none](#role-map-none).

Note

The above text differs slightly from the WAI-ARIA specification. The requirement for user agents to expose the
WAI-ARIA role instead of the native role was intended to only apply in cases where there is a direct mapping from the
WAI-ARIA role to a corresponding role in the accessibility API. The wording
of the requirement is not clear in the WAI-ARIA specification, however, and has been interpreted differently by implementers. The
requirement has been clarified here and an additional statement added to indicate that user agents may expose native semantics if there is not a direct mapping to a role in the accessibility
API. Because there are differing implementations, authors will be advised against adding such
WAI-ARIA roles to native elements that have their own semantics in the
WAI-ARIA Authoring Practices Guide.

When WAI-ARIA states and properties correspond to host language features that have the same implicit
WAI-ARIA semantic, it can be problematic if the values become out of sync. For example, the
HTML `checked` attribute and the `aria-checked` attribute could have conflicting values. Therefore to prevent providing
conflicting states and properties to assistive technologies, host languages will explicitly declare where the use of
WAI-ARIA attributes on a host language element conflict with native attributes for that element. When a host language declares a
WAI-ARIA [attribute](https://dom.spec.whatwg.org/#concept-attribute) to be in direct semantic conflict with a native attribute for a given element, user
agents *MUST* ignore the WAI-ARIA attribute and instead use the host language attribute with the same implicit semantic.

Host languages might also document features that cannot be overridden with WAI-ARIA (these are called "strong native
semantics"). These can be features that have implicit WAI-ARIA semantics as well as features where the processing would be
uncertain if the semantics were changed with WAI-ARIA. While conformance checkers might signal an error or warning when a
WAI-ARIA role is used on elements with strong native semantics, user agents *MUST* still use the value of the semantic of the
WAI-ARIA role when exposing the element to accessibility APIs.

### 3.3 Exposing attributes that do not directly map to accessibility API properties

Platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) might have features that are not in WAI-ARIA. Likewise,
WAI-ARIA exposes capabilities that are not supported by accessibility
APIs at the time of publication. There typically is not a one to one relationship between all
WAI-ARIA [attributes](https://dom.spec.whatwg.org/#concept-attribute) and platform accessibility APIs.
When WAI-ARIA [roles](https://www.w3.org/TR/wai-aria/#dfn-role), [states](https://www.w3.org/TR/wai-aria/#dfn-state) and [properties](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.") do not directly map to an
accessibility API, and there is a mechanism in the API to expose the
WAI-ARIA role, states, and properties and their values, [user agents](https://infra.spec.whatwg.org/#user-agent) *MUST* expose the
WAI-ARIA data using that mechanism as follows:

- In IAccessible2 and ATK/AT-SPI, use object attributes to expose
  [semantics](https://www.w3.org/TR/wai-aria/#dfn-semantics) that are not directly supported in the APIs. Object attributes are name-value pairs that are
  loosely specified, and very flexible for exposing things where there is no specific interface in an accessibility API. For example,
  at this time, the [`aria-live`](#aria-live "Broken local reference found in document.") attribute can be exposed via an object attribute because accessibility
  APIs have no such property available. Specific rules for exposing object attribute name-value pairs are described throughout this
  document, and rules for the general cases are in [State and Property Mapping](#mapping_state-property).
- In Microsoft UIA, use the `AriaRole` and `AriaProperties` properties to expose semantics that are not directly
  supported in the control type.

Note

MSAA does not provide a mechanism for exposing attributes that do not map directly to the API and among implementers, there is no
agreement on how to do it.

User agents *MUST* also expose the entire role string through this mechanism and *MAY* also expose WAI-ARIA attributes and values
through this mechanism even when there is a direct mapping to an accessibility API.

Browser implementers are advised to publicly document their API methods for exposing any relevant information, so that
[assistive technology](https://www.w3.org/TR/wai-aria/#assistive-technology) developers can use the API to support user features.

### 3.4 Role mapping

Platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) traditionally have had a finite set of predefined [roles](https://www.w3.org/TR/wai-aria/#dfn-role) that are expected by
[assistive technologies](https://www.w3.org/TR/wai-aria/#assistive-technology) on that platform and only one or two roles may be exposed. In contrast,
WAI-ARIA allows multiple roles to be specified as an ordered set of space-separated valid role tokens. The additional roles are
fallback roles similar to the concept of specifying multiple fonts in case the first choice font type is not supported.

#### 3.4.1 General rules

User agents *MUST* expose the WAI-ARIA role string if the API supports a
mechanism to do so. This allows assistive technologies to do their own additional processing of roles.

- MSAA:
  [not supported](https://msdn.microsoft.com/en-us/library/windows/desktop/dd373608(v=vs.85).aspx "Object Roles (Windows)"). User agents *SHOULD NOT* expose a custom role in
  MSAA's `accRole` property.
- IAccessible2: expose as an object attribute pair (`xml-roles:"string"`)
- UIA: expose as `AriaRole` property. The `AriaRole property` can also support secondary roles using a space as a
  separator.
- ATK/AT-SPI: expose as an object attribute pair
  (`xml-roles:"string"`)

#### 3.4.2 Computed Role

The `computedrole` of an element is a string that represents the role of the element as computed by the browser engine. The `computedrole` is used primarily for the purposes of developer
tools and specification conformance and interoperability testing.

Note

User agents provide this role string, for example, in developer tools, and in response to the WebDriver function
[`getComputedRole`](https://w3c.github.io/webdriver/#get-computed-role), which is used for
[interoperability testing of ARIA, HTML-AAM, and other specifications](https://github.com/w3c/aria/blob/main/documentation/tests.md).

[Example 1](#example-1)

```
<button> <!-- computedrole returns "button" -->

<a href="#" role="button"> <!-- computedrole returns "button" -->
```

Note

When an element has a role but is not contained in the required context (for example, an orphaned `listitem` without the required accessible parent of role `list`), this is an authoring
error, but the user agent behavior is not specified as a single rule. For most roles, user agents can either recover the error by ignoring the role, or respect the author's intended role
in scenarios deemed by the implementation to be harmless. Please note that this permissiveness in how engines treat author role errors might be overridden in a language-specific mapping
document such as [[HTML-AAM](#bib-html-aam "HTML Accessibility API Mappings 1.0")].

[Example 2](#example-2)

```
<div role="listitem"> <!-- Author error: orphaned listitem. computedrole is unspecified. -->

<div role="list"> <!-- computedrole returns "list" -->
  <div role="listitem"> <!-- computedrole returns "listitem" in the appropriate context. -->
```

When host language elements do not have an exact or equivalent mapping to a valid, non-abstract role, the related Accessibilty API Mapping extension specification *MAY* specify a unique
`computedrole` string as the return value for interoperability testing purposes, such as `<video> -> "html-video"` in [[HTML-AAM](#bib-html-aam "HTML Accessibility API Mappings 1.0")]. However, authors *MUST NOT* use any
host-language-prefixed `computedrole` string in the `role` attribute (such as `html-video`), unless the token also matches valid, defined role (such as `dpub-chapter`). User Agents *MUST*
ignore any abstract or invalid role token.

[Example 3](#example-3)

```
<video> <!-- computedrole returns "html-video" -->

<main role="html-video"> <!-- Author error. computedrole returns "main" -->
```

#### 3.4.3 Role Mapping Tables

##### 3.4.3.1 `alert`

|  |  |
| --- | --- |
| ARIA Specification | [`alert`](#alert) |
| Computed Role | `alert` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_ALERT`  Event: The user agent *SHOULD* fire `EVENT_SYSTEM_ALERT`. [[Note 2](#ftn.note2)] |
| UIA | Control Type: `Group`  Localized Control Type: `alert`  LiveSetting: `Assertive (2)`  Event: The user agent *SHOULD* fire a system alert [event](https://dom.spec.whatwg.org/#concept-event). [[Note 2](#ftn.note2)] |
| ATK/AT-SPI | Role: `ROLE_NOTIFICATION`  Event: The user agent *SHOULD* fire a system alert [event](https://dom.spec.whatwg.org/#concept-event). [[Note 2](#ftn.note2)] |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationAlert`  Event: The user agent *SHOULD* fire a system alert [event](https://dom.spec.whatwg.org/#concept-event). [[Note 2](#ftn.note2)] |
| Android | TBD |

##### 3.4.3.2 `alertdialog`

|  |  |
| --- | --- |
| ARIA Specification | [`alertdialog`](#alertdialog) |
| Computed Role | `alertdialog` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_DIALOG`  Event: The user agent *SHOULD* fire `EVENT_SYSTEM_ALERT`. [[Note 2](#ftn.note2)] |
| UIA | Control Type: `Pane`  Event: The user agent *SHOULD* fire a system alert [event](https://dom.spec.whatwg.org/#concept-event). [[Note 2](#ftn.note2)] |
| ATK/AT-SPI | Role: `ROLE_ALERT`  Interface: `Window`  Event: The user agent *SHOULD* fire a system alert [event](https://dom.spec.whatwg.org/#concept-event). [[Note 2](#ftn.note2)] |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationAlertDialog`  Event: The user agent *SHOULD* fire a system alert [event](https://dom.spec.whatwg.org/#concept-event). [[Note 2](#ftn.note2)] |
| Android | TBD |

##### 3.4.3.3 `application`

|  |  |
| --- | --- |
| ARIA Specification | [`application`](#application) |
| Computed Role | `application` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_APPLICATION` |
| UIA | Control Type: `Pane`  Localized Control Type: `application` |
| ATK/AT-SPI | Role: `ROLE_EMBEDDED` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXWebApplication` |
| Android | TBD |

##### 3.4.3.4 `article`

|  |  |
| --- | --- |
| ARIA Specification | [`article`](#article) |
| Computed Role | `article` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_DOCUMENT`  State: `STATE_SYSTEM_READONLY`  Object Attribute: `xml-roles:article` |
| UIA | Control Type: `Group`  Localized Control Type: `article` |
| ATK/AT-SPI | Role: `ROLE_ARTICLE`  Object Attribute: `xml-roles:article` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXDocumentArticle` |
| Android | TBD |

##### 3.4.3.5 `banner`

|  |  |
| --- | --- |
| ARIA Specification | [`banner`](#banner) |
| Computed Role | `banner` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:banner` |
| UIA | Control Type: `Group`  Localized Control Type: `banner`  Landmark Type: `Custom`  Localized Landmark Type: `banner` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:banner` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkBanner` |
| Android | TBD |

##### 3.4.3.6 `blockquote`

|  |  |
| --- | --- |
| ARIA Specification | [`blockquote`](#blockquote) |
| Computed Role | `blockquote` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_BLOCK_QUOTE` |
| UIA | Control Type: `Group`  Localized Control Type: `blockquote` |
| ATK/AT-SPI | Role: `ROLE_BLOCK_QUOTE` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.7 `button` with default values for `aria-pressed` and `aria-haspopup`

|  |  |
| --- | --- |
| ARIA Specification | [`button`](#button "Broken local reference found in document.") with default values for [`aria-pressed`](#aria-pressed "Broken local reference found in document.") and [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.") |
| Computed Role | `button` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_PUSHBUTTON` |
| UIA | Control Type: `Button` |
| ATK/AT-SPI | Role: `ROLE_PUSH_BUTTON` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXButton`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.8 `button` with non-`false` value for `aria-haspopup`

|  |  |
| --- | --- |
| ARIA Specification | [`button`](#button "Broken local reference found in document.") with non-`false` value for `aria-haspopup` |
| Computed Role | `button` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_BUTTONMENU` |
| UIA | Control Type: `Button` |
| ATK/AT-SPI | Role: `ROLE_PUSH_BUTTON` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXPopUpButton`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.9 `button` with defined value for `aria-pressed`

|  |  |
| --- | --- |
| ARIA Specification | [`button`](#button "Broken local reference found in document.") with defined value for [`aria-pressed`](#aria-pressed "Broken local reference found in document.") |
| Computed Role | `button` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_PUSHBUTTON`  Role: `IA2_ROLE_TOGGLE_BUTTON` |
| UIA | Control Type: `Button` |
| ATK/AT-SPI | Role: `ROLE_TOGGLE_BUTTON` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCheckBox`  AXSubrole: `AXToggle` |
| Android | TBD |

##### 3.4.3.10 `caption`

|  |  |
| --- | --- |
| ARIA Specification | [`caption`](#caption) |
| Computed Role | `caption` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_CAPTION` |
| UIA | Control Type: `Text` |
| ATK/AT-SPI | Role: `ROLE_CAPTION` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.11 `cell`

|  |  |
| --- | --- |
| ARIA Specification | [`cell`](#cell) |
| Computed Role | `cell` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_CELL`  Interface: `IAccessibleTableCell` |
| UIA | Control Type: `DataItem`  Localized Control Type: `item`  Control Pattern: `GridItem`  Control Pattern: `TableItem` |
| ATK/AT-SPI | Role: `ROLE_TABLE_CELL`  Interface: `TableCell` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCell`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.12 `checkbox`

|  |  |
| --- | --- |
| ARIA Specification | [`checkbox`](#checkbox) |
| Computed Role | `checkbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_CHECKBUTTON`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `Checkbox`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_CHECK_BOX`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCheckBox`  AXSubrole: `<nil>`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.13 `code`

|  |  |
| --- | --- |
| ARIA Specification | [`code`](#code) |
| Computed Role | `code` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_TEXT_FRAME`  Object Attribute: `xml-roles:code` |
| UIA | Control Type: `Text`  Localized Control Type: `code` |
| ATK/AT-SPI | Role: `ROLE_STATIC`  Object Attribute: `xml-roles:code` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXCodeStyleGroup` |
| Android | TBD |

##### 3.4.3.14 `columnheader`

|  |  |
| --- | --- |
| ARIA Specification | [`columnheader`](#columnheader) |
| Computed Role | `columnheader` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_COLUMNHEADER`  Interface: `IAccessibleTableCell` |
| UIA | Control Type: `DataItem`  Localized Control Type: `column header`  Control Pattern: `GridItem`  Control Pattern: `TableItem` |
| ATK/AT-SPI | Role: `ROLE_COLUMN_HEADER`  Interface: `TableCell` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCell`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.15 `combobox`

|  |  |
| --- | --- |
| ARIA Specification | [`combobox`](#combobox) |
| Computed Role | `combobox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_COMBOBOX`  State: `STATE_SYSTEM_HASPOPUP`  State: `STATE_SYSTEM_COLLAPSED` if [`aria-expanded`](#aria-expanded "Broken local reference found in document.") is not `"true"` |
| UIA | Control Type: `Combobox` |
| ATK/AT-SPI | Role: `ROLE_COMBO_BOX`  State: `STATE_EXPANDABLE`  State: `STATE_HAS_POPUP` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXComboBox`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.16 `comment`

|  |  |
| --- | --- |
| ARIA Specification | [`comment`](#comment) |
| Computed Role | `comment` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_COMMENT`  Object Attribute: `xml-roles:comment` |
| UIA | Control Type: `Group`  Localized Control Type: `comment` |
| ATK/AT-SPI | Role: `ROLE_COMMENT`  Object Attribute: `xml-roles:comment` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup` |
| Android | TBD |

##### 3.4.3.17 `complementary`

|  |  |
| --- | --- |
| ARIA Specification | [`complementary`](#complementary) |
| Computed Role | `complementary` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:complementary` |
| UIA | Control Type: `Group`  Localized Control Type: `complementary`  Landmark Type: `Custom`  Localized Landmark Type: `complementary` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:complementary` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkComplementary` |
| Android | TBD |

##### 3.4.3.18 `contentinfo`

|  |  |
| --- | --- |
| ARIA Specification | [`contentinfo`](#contentinfo) |
| Computed Role | `contentinfo` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:contentinfo` |
| UIA | Control Type: `Group`  Localized Control Type: `content information`  Landmark Type: `Custom`  Localized Landmark Type: `content information` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:contentinfo` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkContentInfo` |
| Android | TBD |

##### 3.4.3.19 `definition`

|  |  |
| --- | --- |
| ARIA Specification | [`definition`](#definition) |
| Computed Role | `definition` |
| MSAA + IAccessible2 | Object Attribute: `xml-roles:definition` |
| UIA | Control Type: `Group`  Localized Control Type: `definition` |
| ATK/AT-SPI | Role: `ROLE_DESCRIPTION_VALUE`  Object Attribute: `xml-roles:definition` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXDefinition` |
| Android | TBD |

##### 3.4.3.20 `deletion`

|  |  |
| --- | --- |
| ARIA Specification | [`deletion`](#deletion) |
| Computed Role | `deletion` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_CONTENT_DELETION` |
| UIA | Control Type: `Text`  Localized Control Type: `deletion` |
| ATK/AT-SPI | Role: `ROLE_CONTENT_DELETION`  Object Attribute: `xml-roles:deletion` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXDeleteStyleGroup`  AXAttributedStringForTextMarkerRange: contains `AXIsSuggestedDeletion = 1;` for all text contained in a `deletion` |
| Android | TBD |

##### 3.4.3.21 `dialog`

|  |  |
| --- | --- |
| ARIA Specification | [`dialog`](#dialog) |
| Computed Role | `dialog` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_DIALOG` |
| UIA | Control Type: `Pane` |
| ATK/AT-SPI | Role: `ROLE_DIALOG`  Interface: `Window` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationDialog` |
| Android | TBD |

##### 3.4.3.22 `directory` (deprecated)

|  |  |
| --- | --- |
| ARIA Specification | [`directory`](#directory "Broken local reference found in document.") |
| Computed Role | list |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LIST` |
| UIA | Control Type: `List` |
| ATK/AT-SPI | Role: `ROLE_LIST` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXList`  AXSubrole: `AXContentList` |
| Android | TBD |

##### 3.4.3.23 `document`

|  |  |
| --- | --- |
| ARIA Specification | [`document`](#document) |
| Computed Role | `document` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_DOCUMENT`  State: `STATE_SYSTEM_READONLY` |
| UIA | Control Type: `Document` |
| ATK/AT-SPI | Role: `ROLE_DOCUMENT_FRAME` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXDocument` |
| Android | TBD |

##### 3.4.3.24 `emphasis`

|  |  |
| --- | --- |
| ARIA Specification | [`emphasis`](#emphasis) |
| Computed Role | `emphasis` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_TEXT_FRAME`  Object Attribute: `xml-roles:emphasis` |
| UIA | Control Type: `Text`  Localized Control Type: `emphasis` |
| ATK/AT-SPI | Role: `ROLE_STATIC`  Object Attribute: `xml-roles:emphasis` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXEmphasisStyleGroup` |
| Android | TBD |

##### 3.4.3.25 `feed`

|  |  |
| --- | --- |
| ARIA Specification | [`feed`](#feed) |
| Computed Role | `feed` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Object Attribute: `xml-roles:feed` |
| UIA | Control Type: `Group`  Localized Control Type: `feed` |
| ATK/AT-SPI | Role: `ROLE_PANEL`  Object Attribute: `xml-roles:feed` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationGroup` |
| Android | TBD |

##### 3.4.3.26 `figure`

|  |  |
| --- | --- |
| ARIA Specification | [`figure`](#figure) |
| Computed Role | `figure` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Object Attribute: `xml-roles:figure` |
| UIA | Control Type: `Group`  Localized Control Type: `figure` |
| ATK/AT-SPI | Role: `ROLE_PANEL`  Object Attribute: `xml-roles:figure` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.27 `form` with an accessible name

|  |  |
| --- | --- |
| ARIA Specification | [`form`](#form "Broken local reference found in document.") with an accessible name |
| Computed Role | `form` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_FORM`  Object Attribute: `xml-roles:form` |
| UIA | Control Type: `Group`  Localized Control Type: `form`  Landmark Type: `Form` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:form` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkForm` |
| Android | TBD |

##### 3.4.3.28 `form` without an accessible name

|  |  |
| --- | --- |
| ARIA Specification | [`form`](#form "Broken local reference found in document.") without an accessible name |
| Computed Role | `form` |
| MSAA + IAccessible2 | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| UIA | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| ATK/AT-SPI | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| AX API[[Note 1](#ftn.note1)] | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| Android | TBD |

##### 3.4.3.29 `generic`

|  |  |
| --- | --- |
| ARIA Specification | [`generic`](#generic) |
| Computed Role | `generic` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_SECTION` |
| UIA | Control Type: `Group` |
| ATK/AT-SPI | Role: `ROLE_SECTION` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.30 `grid`

|  |  |
| --- | --- |
| ARIA Specification | [`grid`](#grid) |
| Computed Role | `grid` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TABLE`  Object Attribute: `xml-roles:grid`  Interface: `IAccessibleTable2`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `DataGrid`  Control Pattern: `Grid`  Control Pattern: `Table`  Control Pattern: `Selection` |
| ATK/AT-SPI | Role: `ROLE_TABLE`  Object Attribute: `xml-roles:grid`  Interface: `Table`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTable`  AXSubrole: `<nil>`  AXColumnHeaderUIElements: a list of pointers to the columnheader elements  AXHeader: a pointer to the row or group containing those columnheader elements  AXRowHeaderUIElements: a list of pointers to the rowheader elements |
| Android | TBD |

##### 3.4.3.31 `gridcell`

|  |  |
| --- | --- |
| ARIA Specification | [`gridcell`](#gridcell) |
| Computed Role | `gridcell` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_CELL`  Interface: `IAccessibleTableCell` |
| UIA | Control Type: `DataItem`  Localized Control Type: `item`  Control Pattern: `SelectionItem`  Control Pattern: `GridItem`  Control Pattern: `TableItem`  SelectionItem.SelectionContainer: the containing `grid` |
| ATK/AT-SPI | Role: `ROLE_TABLE_CELL`  Interface: `TableCell` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCell`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.32 `group`

|  |  |
| --- | --- |
| ARIA Specification | [`group`](#group) |
| Computed Role | `group` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING` |
| UIA | Control Type: `Group` |
| ATK/AT-SPI | Role: `ROLE_PANEL` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationGroup` |
| Android | TBD |

##### 3.4.3.33 `heading`

|  |  |
| --- | --- |
| ARIA Specification | [`heading`](#heading) |
| Computed Role | `heading` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_HEADING`  Object Attribute: `xml-roles:heading` |
| UIA | Control Type: `Text`  Localized Control Type: `heading` |
| ATK/AT-SPI | Role: `ROLE_HEADING` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXHeading`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.34 `image`

|  |  |
| --- | --- |
| ARIA Specification | [`image`](#image) |
| Computed Role | `image` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GRAPHIC`  Interface: `IAccessibleImage` |
| UIA | Control Type: `Image` |
| ATK/AT-SPI | Role: `ROLE_IMAGE`  Interface: `Image` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXImage`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.35 `img`

|  |  |
| --- | --- |
| ARIA Specification | [`img`](#img) |
| Computed Role | `image` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GRAPHIC`  Interface: `IAccessibleImage` |
| UIA | Control Type: `Image` |
| ATK/AT-SPI | Role: `ROLE_IMAGE`  Interface: `Image` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXImage`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.36 `insertion`

|  |  |
| --- | --- |
| ARIA Specification | [`insertion`](#insertion) |
| Computed Role | `insertion` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_CONTENT_INSERTION` |
| UIA | Control Type: `Text`  Localized Control Type: `insertion` |
| ATK/AT-SPI | Role: `ROLE_CONTENT_INSERTION`  Object Attribute: `xml-roles:insertion` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXInsertStyleGroup`  AXAttributedStringForTextMarkerRange: contains `AXIsSuggestedInsertion = 1;` for all text contained in a `insertion` |
| Android | TBD |

##### 3.4.3.37 `link`

|  |  |
| --- | --- |
| ARIA Specification | [`link`](#link) |
| Computed Role | `link` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LINK`  State: `STATE_SYSTEM_LINKED`  State: `STATE_SYSTEM_LINKED` on its descendants  Interface: `IAccessibleHypertext` |
| UIA | Control Type: `HyperLink`  Control Pattern: `Value` |
| ATK/AT-SPI | Role: `ROLE_LINK`  Interface: `HyperlinkImpl` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXLink`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.38 `list`

|  |  |
| --- | --- |
| ARIA Specification | [`list`](#list) |
| Computed Role | `list` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LIST`  State: `STATE_SYSTEM_READONLY` |
| UIA | Control Type: `List` |
| ATK/AT-SPI | Role: `ROLE_LIST` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXList`  AXSubrole: `AXContentList` |
| Android | TBD |

##### 3.4.3.39 `listbox` without an accessibility parent of `combobox`

|  |  |
| --- | --- |
| ARIA Specification | [`listbox`](#listbox "Broken local reference found in document.") |
| Computed Role | `listbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LIST`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `List`  Control Pattern: `Selection` |
| ATK/AT-SPI | Role: `ROLE_LIST_BOX`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXList`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.40 `listbox` with an accessibility parent of `combobox`

|  |  |
| --- | --- |
| ARIA Specification | [`listbox`](#listbox "Broken local reference found in document.") |
| Computed Role | `listbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LIST`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `List`  Control Pattern: `Selection` |
| ATK/AT-SPI | Role: `ROLE_MENU`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXList`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.41 `listitem`

|  |  |
| --- | --- |
| ARIA Specification | [`listitem`](#listitem) |
| Computed Role | `listitem` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LISTITEM`  State: `STATE_SYSTEM_READONLY` |
| UIA | Control Type: `ListItem`  Control Pattern: `SelectionItem`  SelectionItem.SelectionContainer: the containing `list` |
| ATK/AT-SPI | Role: `ROLE_LIST_ITEM` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.42 `log`

|  |  |
| --- | --- |
| ARIA Specification | [`log`](#log) |
| Computed Role | `log` |
| MSAA + IAccessible2 | Object Attribute: `xml-roles:log`  Object Attribute: `container-live:polite`  Object Attribute: `live:polite`  Object Attribute: `container-live-role:log` |
| UIA | Control Type: `Group`  Localized Control Type: `log`  LiveSetting: `Polite (1)` |
| ATK/AT-SPI | Role: `ROLE_LOG`  Object Attribute: `xml-roles:log`  Object Attribute: `container-live:polite`  Object Attribute: `live:polite`  Object Attribute: `container-live-role:log` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationLog` |
| Android | TBD |

##### 3.4.3.43 `main`

|  |  |
| --- | --- |
| ARIA Specification | [`main`](#main) |
| Computed Role | `main` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:main` |
| UIA | Control Type: `Group`  Localized Control Type: `main`  Landmark Type: `Main` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:main` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkMain` |
| Android | TBD |

##### 3.4.3.44 `mark`

|  |  |
| --- | --- |
| ARIA Specification | [`mark`](#mark) |
| Computed Role | `mark` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_MARK`  Object Attribute: `xml-roles:mark` |
| UIA | Control Type: `Group` |
| ATK/AT-SPI | Role: `ROLE_MARK`  Object Attribute: `xml-roles:mark` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXRoleDescription: `highlight`  AXAttributedStringForTextMarkerRange: contains `AXHighlight = 1;` for all text contained in a `mark` |
| Android | TBD |

##### 3.4.3.45 `marquee`

|  |  |
| --- | --- |
| ARIA Specification | [`marquee`](#marquee) |
| Computed Role | `marquee` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_ANIMATION`  Object Attribute: `xml-roles:marquee` |
| UIA | Control Type: `Group`  Localized Control Type: `marquee` |
| ATK/AT-SPI | Role: `ROLE_MARQUEE` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationMarquee` |
| Android | TBD |

##### 3.4.3.46 `math`

|  |  |
| --- | --- |
| ARIA Specification | [`math`](#math) |
| Computed Role | `math` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_EQUATION` |
| UIA | Control Type: `Group`  Localized Control Type: `math` |
| ATK/AT-SPI | Role: `ROLE_MATH` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXDocumentMath` |
| Android | TBD |

##### 3.4.3.47 `menu`

|  |  |
| --- | --- |
| ARIA Specification | [`menu`](#menu) |
| Computed Role | `menu` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_MENUPOPUP`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `Menu` |
| ATK/AT-SPI | Role: `ROLE_MENU`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXMenu`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.48 `menubar`

|  |  |
| --- | --- |
| ARIA Specification | [`menubar`](#menubar) |
| Computed Role | `menubar` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_MENUBAR`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `MenuBar` |
| ATK/AT-SPI | Role: `ROLE_MENU_BAR`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXMenuBar`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.49 `menuitem`

|  |  |
| --- | --- |
| ARIA Specification | [`menuitem`](#menuitem) |
| Computed Role | `menuitem` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_MENUITEM` |
| UIA | Control Type: `MenuItem` |
| ATK/AT-SPI | Role: `ROLE_MENU_ITEM` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXMenuItem`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.50 `menuitemcheckbox`

|  |  |
| --- | --- |
| ARIA Specification | [`menuitemcheckbox`](#menuitemcheckbox) |
| Computed Role | `menuitemcheckbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_CHECKBUTTON` or `ROLE_SYSTEM_MENUITEM`  Role: `IA2_ROLE_CHECK_MENU_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `MenuItem`  Control Pattern: `Toggle`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_CHECK_MENU_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXMenuItem`  AXSubrole: `<nil>`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.51 `menuitemradio`

|  |  |
| --- | --- |
| ARIA Specification | [`menuitemradio`](#menuitemradio) |
| Computed Role | `menuitemradio` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_RADIOBUTTON` or `ROLE_SYSTEM_MENUITEM`  Role: `IA2_ROLE_RADIO_MENU_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `MenuItem`  Control Pattern: `Toggle`  Control Pattern: `SelectionItem`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_RADIO_MENU_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXMenuItem`  AXSubrole: `<nil>`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.52 `meter`

|  |  |
| --- | --- |
| ARIA Specification | [`meter`](#meter) |
| Computed Role | `meter` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LEVEL_BAR`  Interface: `IAccessibleValue` |
| UIA | Control Type: `ProgressBar`  Localized Control Type: `meter`  Control Pattern: `RangeValue` |
| ATK/AT-SPI | Role: `ROLE_LEVEL_BAR`  Interface: `Value` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXLevelIndicator`  AXSubrole: `AXMeter` |
| Android | TBD |

##### 3.4.3.53 `navigation`

|  |  |
| --- | --- |
| ARIA Specification | [`navigation`](#navigation) |
| Computed Role | `navigation` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:navigation` |
| UIA | Control Type: `Group`  Localized Control Type: `navigation`  Landmark Type: `Navigation` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:navigation` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkNavigation` |
| Android | TBD |

##### 3.4.3.54 `none`

|  |  |
| --- | --- |
| ARIA Specification | [`none`](#none) |
| Computed Role | `none` |
| MSAA + IAccessible2 | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it as `IA2_ROLE_TEXT_FRAME`. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| UIA | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it using the `text` pattern. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| ATK/AT-SPI | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it as `ROLE_SECTION`. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| AX API[[Note 1](#ftn.note1)] | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it as `AXGroup`. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| Android | TBD |

##### 3.4.3.55 `note`

|  |  |
| --- | --- |
| ARIA Specification | [`note`](#note) |
| Computed Role | `note` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_NOTE` |
| UIA | Control Type: `Group`  Localized Control Type: `note` |
| ATK/AT-SPI | Role: `ROLE_COMMENT` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXDocumentNote` |
| Android | TBD |

##### 3.4.3.56 `option` not inside `combobox`

|  |  |
| --- | --- |
| ARIA Specification | [`option`](#option "Broken local reference found in document.") not inside `combobox` |
| Computed Role | `option` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LISTITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `ListItem`  Control Pattern: `Invoke`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_LIST_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXStaticText`  AXSubrole: `<nil>`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.57 `option` inside `combobox`

|  |  |
| --- | --- |
| ARIA Specification | [`option`](#option "Broken local reference found in document.") inside `combobox` |
| Computed Role | `option` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_LISTITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `ListItem`  Control Pattern: `Invoke`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_MENU_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXStaticText`  AXSubrole: `<nil>`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.58 `paragraph`

|  |  |
| --- | --- |
| ARIA Specification | [`paragraph`](#paragraph) |
| Computed Role | `paragraph` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_PARAGRAPH` |
| UIA | Control Type: `Text` |
| ATK/AT-SPI | Role: `ROLE_PARAGRAPH` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.59 `presentation`

|  |  |
| --- | --- |
| ARIA Specification | [`presentation`](#presentation) |
| Computed Role | `none` |
| MSAA + IAccessible2 | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it as `IA2_ROLE_TEXT_FRAME`. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| UIA | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it using the `text` pattern. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| ATK/AT-SPI | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it as `ROLE_SECTION`. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| AX API[[Note 1](#ftn.note1)] | For objects that have specified allowed accessibility children (e.g., a grid with gridcell children, a list with listitem children), and the descendant is in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), expose it as `AXGroup`. [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* prune empty descendants from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree). |
| Android | TBD |

##### 3.4.3.60 `progressbar`

|  |  |
| --- | --- |
| ARIA Specification | [`progressbar`](#progressbar) |
| Computed Role | `progressbar` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_PROGRESSBAR`  State: `STATE_SYSTEM_READONLY`  Interface: `IAccessibleValue` |
| UIA | Control Type: `ProgressBar`  Control Pattern: `RangeValue` if `aria-valuenow`, `aria-valuemax`, or `aria-valuemin` is present |
| ATK/AT-SPI | Role: `ROLE_PROGRESS_BAR`  Interface: `Value` Because WAI-ARIA does not support modifying the value via the accessibility API, user agents *MUST* return `false` for all `Value` methods that provide a means to modify the value. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXProgressIndicator`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.61 `radio`

|  |  |
| --- | --- |
| ARIA Specification | [`radio`](#radio) |
| Computed Role | `radio` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_RADIOBUTTON`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `RadioButton`  Control Pattern: `Toggle`  Control Pattern: `SelectionItem`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_RADIO_BUTTON`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXRadioButton`  AXSubrole: `<nil>`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.62 `radiogroup`

|  |  |
| --- | --- |
| ARIA Specification | [`radiogroup`](#radiogroup) |
| Computed Role | `radiogroup` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING` |
| UIA | Control Type: `List` |
| ATK/AT-SPI | Role: `ROLE_PANEL` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXRadioGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.63 `region` with an accessible name

|  |  |
| --- | --- |
| ARIA Specification | [`region`](#region "Broken local reference found in document.") with an accessible name |
| Computed Role | `region` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:region` |
| UIA | Control Type: `Group`  Localized Control Type: `region`  Landmark Type: `Custom`  Localized Landmark Type: `region` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:region` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkRegion` |
| Android | TBD |

##### 3.4.3.64 `region` without an accessible name

|  |  |
| --- | --- |
| ARIA Specification | [`region`](#region "Broken local reference found in document.") without an accessible name |
| Computed Role | Use native host language role. |
| MSAA + IAccessible2 | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| UIA | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| ATK/AT-SPI | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| AX API[[Note 1](#ftn.note1)] | Do not expose the [element](https://dom.spec.whatwg.org/#concept-element) as a landmark. Use the native host language role of the element instead. |
| Android | TBD |

##### 3.4.3.65 `row` not inside `treegrid`

|  |  |
| --- | --- |
| ARIA Specification | [`row`](#row "Broken local reference found in document.") not inside `treegrid` |
| Computed Role | `row` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_ROW` |
| UIA | Control Type: `DataItem`  Localized Control Type: `row`  Control Pattern: `SelectionItem` |
| ATK/AT-SPI | Role: `ROLE_TABLE_ROW` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXRow`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.66 `row` inside `treegrid`

|  |  |
| --- | --- |
| ARIA Specification | [`row`](#row "Broken local reference found in document.") inside `treegrid` |
| Computed Role | `row` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_OUTLINEITEM` |
| UIA | Control Type: `DataItem`  Localized Control Type: `row`  Control Pattern: `SelectionItem` |
| ATK/AT-SPI | Role: `ROLE_TABLE_ROW` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXRow`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.67 `rowgroup`

|  |  |
| --- | --- |
| ARIA Specification | [`rowgroup`](#rowgroup) |
| Computed Role | `rowgroup` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING` |
| UIA | Control Type: `Group` |
| ATK/AT-SPI | Role: `ROLE_PANEL` |
| AX API[[Note 1](#ftn.note1)] | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.4.3.68 `rowheader`

|  |  |
| --- | --- |
| ARIA Specification | [`rowheader`](#rowheader) |
| Computed Role | `rowheader` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_ROWHEADER`  Interface: `IAccessibleTableCell` |
| UIA | Control Type: `HeaderItem` |
| ATK/AT-SPI | Role: `ROLE_ROW_HEADER`  Interface: `TableCell` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCell`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.69 `scrollbar`

|  |  |
| --- | --- |
| ARIA Specification | [`scrollbar`](#scrollbar) |
| Computed Role | `scrollbar` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_SCROLLBAR`  Interface: `IAccessibleValue` |
| UIA | Control Type: `ScrollBar`  Control Pattern: `RangeValue` |
| ATK/AT-SPI | Role: `ROLE_SCROLL_BAR`  Interface: `Value` Because WAI-ARIA does not support modifying the value via the accessibility API, user agents *MUST* return `false` for all `Value` methods that provide a means to modify the value. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXScrollBar`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.70 `search`

|  |  |
| --- | --- |
| ARIA Specification | [`search`](#search) |
| Computed Role | `search` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_LANDMARK`  Object Attribute: `xml-roles:search` |
| UIA | Control Type: `Group`  Localized Control Type: `search`  Landmark Type: `Search` |
| ATK/AT-SPI | Role: `ROLE_LANDMARK`  Object Attribute: `xml-roles:search` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXLandmarkSearch` |
| Android | TBD |

##### 3.4.3.71 `searchbox`

|  |  |
| --- | --- |
| ARIA Specification | [`searchbox`](#searchbox) |
| Computed Role | `searchbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TEXT`  Object Attribute: `text-input-type:search` |
| UIA | Control Type: `Edit`  Localized Control Type: `search box` |
| ATK/AT-SPI | Role: `ROLE_ENTRY`  Object Attribute: `xml-roles:searchbox`  Object Attribute: `text-input-type:search`    Interface: `EditableText` if [`aria-readonly`](#aria-readonly) is not `"true"` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTextField`  AXSubrole: `AXSearchField` |
| Android | TBD |

##### 3.4.3.72 `sectionfooter`

|  |  |
| --- | --- |
| ARIA Specification | [`sectionfooter`](#sectionfooter) |
| Computed Role | `sectionfooter` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Object Attribute: `xml-roles:sectionfooter` |
| UIA | Control Type: `Group`  Localized Control Type: `section footer` |
| ATK/AT-SPI | Role: `ROLE_FOOTER` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXSectionFooter`  AXRoleDescription: `section footer` |
| Android | TBD |

##### 3.4.3.73 `sectionheader`

|  |  |
| --- | --- |
| ARIA Specification | [`sectionheader`](#sectionheader) |
| Computed Role | `sectionheader` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Object Attribute: `xml-roles:sectionheader` |
| UIA | Control Type: `Group`  Localized Control Type: `section header` |
| ATK/AT-SPI | Role: `ROLE_HEADER` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXSectionHeader`  AXRoleDescription: `section header` |
| Android | TBD |

##### 3.4.3.74 `separator` (non-focusable)

|  |  |
| --- | --- |
| ARIA Specification | [`separator`](#separator "Broken local reference found in document.") (non-focusable) |
| Computed Role | `seperator` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_SEPARATOR` |
| UIA | Control Type: `Separator` |
| ATK/AT-SPI | Role: `ROLE_SEPARATOR` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXSplitter`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.75 `separator` (focusable)

|  |  |
| --- | --- |
| ARIA Specification | [`separator`](#separator "Broken local reference found in document.") (focusable) |
| Computed Role | `seperator` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_SEPARATOR`  Interface: `IAccessibleValue` |
| UIA | Control Type: `Thumb`  Control Pattern: `RangeValue` |
| ATK/AT-SPI | Role: `ROLE_SEPARATOR`  Interface: `Value` Because WAI-ARIA does not support modifying the value via the accessibility API, user agents *MUST* return `false` for all `Value` methods that provide a means to modify the value. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXSplitter`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.76 `slider`

|  |  |
| --- | --- |
| ARIA Specification | [`slider`](#slider) |
| Computed Role | `slider` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_SLIDER`  Interface: `IAccessibleValue` |
| UIA | Control Type: `Slider`  Control Pattern: `RangeValue` |
| ATK/AT-SPI | Role: `ROLE_SLIDER`  Interface: `Value` Because WAI-ARIA does not support modifying the value via the accessibility API, user agents *MUST* return `false` for all `Value` methods that provide a means to modify the value. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXSlider`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.77 `spinbutton`

|  |  |
| --- | --- |
| ARIA Specification | [`spinbutton`](#spinbutton) |
| Computed Role | `spinbutton` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_SPINBUTTON`  Interface: `IAccessibleValue` |
| UIA | Control Type: `Spinner`  Control Pattern: `RangeValue` |
| ATK/AT-SPI | Role: `ROLE_SPIN_BUTTON`  Interface: `Value` Because WAI-ARIA does not support modifying the value via the accessibility API, user agents *MUST* return `false` for all `Value` methods that provide a means to modify the value. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXIncrementor`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.78 `status`

|  |  |
| --- | --- |
| ARIA Specification | [`status`](#status) |
| Computed Role | `status` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_STATUSBAR`  Object Attribute: `container-live:polite`  Object Attribute: `live:polite`  Object Attribute: `container-live-role:status` |
| UIA | Control Type: `Group`  Localized Control Type: `status`  LiveSetting: `Polite (1)` |
| ATK/AT-SPI | Role: `ROLE_STATUSBAR`  Object Attribute: `container-live:polite`  Object Attribute: `live:polite`  Object Attribute: `container-live-role:status` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationStatus` |
| Android | TBD |

##### 3.4.3.79 `strong`

|  |  |
| --- | --- |
| ARIA Specification | [`strong`](#strong) |
| Computed Role | `strong` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_TEXT_FRAME`  Object Attribute: `xml-roles:strong` |
| UIA | Control Type: `Text`  Localized Control Type: `strong` |
| ATK/AT-SPI | Role: `ROLE_STATIC`  Object Attribute: `xml-roles:strong` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXStrongStyleGroup` |
| Android | TBD |

##### 3.4.3.80 `subscript`

|  |  |
| --- | --- |
| ARIA Specification | [`subscript`](#subscript) |
| Computed Role | `subscript` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_TEXT_FRAME`  Text Attribute: `text-position:sub` |
| UIA | Control Type: `Text`  Styles used are exposed by `IsSubscript` attribute of the `TextRange` Control Pattern implemented on the accessible object. |
| ATK/AT-SPI | Role: `ROLE_SUBSCRIPT` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXSubscriptStyleGroup` |
| Android | TBD |

##### 3.4.3.81 `suggestion`

|  |  |
| --- | --- |
| ARIA Specification | [`suggestion`](#suggestion) |
| Computed Role | `suggestion` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_SUGGESTION`  Object Attribute: `xml-roles:suggestion` |
| UIA | Control Type: `Group`  Localized Control Type: `suggestion` |
| ATK/AT-SPI | Role: `ROLE_SUGGESTION`  Object Attribute: `xml-roles:suggestion` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXAttributedStringForTextMarkerRange: contains `AXIsSuggestion = 1;` for all text contained in a `suggestion` |
| Android | TBD |

##### 3.4.3.82 `superscript`

|  |  |
| --- | --- |
| ARIA Specification | [`superscript`](#superscript) |
| Computed Role | `superscript` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Role: `IA2_ROLE_TEXT_FRAME`  Text Attribute: `text-position:super` |
| UIA | Control Type: `Text`  Styles used are exposed by `IsSuperscript` attribute of the `TextRange` Control Pattern implemented on the accessible object. |
| ATK/AT-SPI | Role: `ROLE_SUPERSCRIPT` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXSuperscriptStyleGroup` |
| Android | TBD |

##### 3.4.3.83 `switch`

|  |  |
| --- | --- |
| ARIA Specification | [`switch`](#switch) |
| Computed Role | `switch` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_CHECKBUTTON`  Role: `IA2_ROLE_TOGGLE_BUTTON`  Object Attribute: `xml-roles:switch`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `Button`  Localized Control Type: `toggleswitch`  Control Pattern: `Toggle`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_TOGGLE_BUTTON`  Object Attribute: `xml-roles:switch`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXCheckBox`  AXSubrole: `AXSwitch`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

##### 3.4.3.84 `tab`

|  |  |
| --- | --- |
| ARIA Specification | [`tab`](#tab) |
| Computed Role | `tab` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_PAGETAB`  State: `STATE_SYSTEM_SELECTED` if focus is inside [`tabpanel`](#tabpanel) associated with [`aria-labelledby`](#aria-labelledby) |
| UIA | Control Type: `TabItem` |
| ATK/AT-SPI | Role: `ROLE_PAGE_TAB`  State: `STATE_SELECTED` if focus is inside [`tabpanel`](#tabpanel) associated with [`aria-labelledby`](#aria-labelledby) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXRadioButton`  AXSubrole: `AXTabButton` |
| Android | TBD |

##### 3.4.3.85 `table`

|  |  |
| --- | --- |
| ARIA Specification | [`table`](#table) |
| Computed Role | `table` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TABLE`  Object Attribute: `xml-roles:table`  Interface: `IAccessibleTable2` |
| UIA | Control Type: `Table`  Control Pattern: `Grid`  Control Pattern: `Table` |
| ATK/AT-SPI | Role: `ROLE_TABLE`  Object Attribute: `xml-roles:table`  Interface: `Table` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTable`  AXSubrole: `<nil>`  AXColumnHeaderUIElements: a list of pointers to the columnheader elements  AXHeader: a pointer to the row or group containing those columnheader elements  AXRowHeaderUIElements: a list of pointers to the rowheader elements |
| Android | TBD |

##### 3.4.3.86 `tablist`

|  |  |
| --- | --- |
| ARIA Specification | [`tablist`](#tablist) |
| Computed Role | `tablist` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_PAGETABLIST`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `Tab`  Control Pattern: `Selection` |
| ATK/AT-SPI | Role: `ROLE_PAGE_TAB_LIST`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTabGroup`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.87 `tabpanel`

|  |  |
| --- | --- |
| ARIA Specification | [`tabpanel`](#tabpanel) |
| Computed Role | `tabpanel` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_PANE` or `ROLE_SYSTEM_PROPERTYPAGE` |
| UIA | Control Type: `Pane` |
| ATK/AT-SPI | Role: `ROLE_SCROLL_PANE` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXTabPanel` |
| Android | TBD |

##### 3.4.3.88 `term`

|  |  |
| --- | --- |
| ARIA Specification | [`term`](#term) |
| Computed Role | `term` |
| MSAA + IAccessible2 | Role: `IA2_ROLE_TEXT_FRAME`  Object Attribute: `xml-roles:term` |
| UIA | Control Type: `Text`  Localized Control Type: `term` |
| ATK/AT-SPI | Role: `ROLE_DESCRIPTION_TERM` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXTerm` |
| Android | TBD |

##### 3.4.3.89 `textbox` when `aria-multiline` is `false`

|  |  |
| --- | --- |
| ARIA Specification | [`textbox`](#textbox "Broken local reference found in document.") when `aria-multiline` is `false` |
| Computed Role | `textbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TEXT`  State: `IA2_STATE_SINGLE_LINE` |
| UIA | Control Type: `Edit` |
| ATK/AT-SPI | Role: `ROLE_ENTRY`  State: `STATE_SINGLE_LINE`  Interface: `EditableText` if [`aria-readonly`](#aria-readonly) is not `"true"` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTextField`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.90 `textbox` when `aria-multiline` is `true`

|  |  |
| --- | --- |
| ARIA Specification | [`textbox`](#textbox "Broken local reference found in document.") when `aria-multiline` is `true` |
| Computed Role | `textbox` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TEXT`  State: `IA2_STATE_MULTI_LINE` |
| UIA | Control Type: `Edit` |
| ATK/AT-SPI | Role: `ROLE_ENTRY`  State: `STATE_MULTI_LINE`  Interface: `EditableText` if [`aria-readonly`](#aria-readonly) is not `"true"` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTextArea`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.91 `time`

|  |  |
| --- | --- |
| ARIA Specification | [`time`](#time) |
| Computed Role | `time` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_GROUPING`  Object Attribute: `xml-roles:time` |
| UIA | Control Type: `Text`  Localized Control Type: `time`  Note: create a separate UIA Control of type Text. This is different from most UIA text mappings, which only create ranges in the page text pattern. |
| ATK/AT-SPI | Role: `ROLE_STATIC`  Object Attribute: `xml-roles:time` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXTimeGroup` |
| Android | TBD |

##### 3.4.3.92 `timer`

|  |  |
| --- | --- |
| ARIA Specification | [`timer`](#timer) |
| Computed Role | `timer` |
| MSAA + IAccessible2 | Object Attribute: `xml-roles:timer` |
| UIA | Control Type: `Group`  Localized Control Type: `timer` |
| ATK/AT-SPI | Role: `ROLE_TIMER` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXApplicationTimer` |
| Android | TBD |

##### 3.4.3.93 `toolbar`

|  |  |
| --- | --- |
| ARIA Specification | [`toolbar`](#toolbar) |
| Computed Role | `toolbar` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TOOLBAR` |
| UIA | Control Type: `ToolBar` |
| ATK/AT-SPI | Role: `ROLE_TOOL_BAR` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXToolbar`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.94 `tooltip`

|  |  |
| --- | --- |
| ARIA Specification | [`tooltip`](#tooltip) |
| Computed Role | `tooltip` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_TOOLTIP` |
| UIA | Control Type: `ToolTip` |
| ATK/AT-SPI | Role: `ROLE_TOOL_TIP` |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXGroup`  AXSubrole: `AXUserInterfaceTooltip` |
| Android | TBD |

##### 3.4.3.95 `tree`

|  |  |
| --- | --- |
| ARIA Specification | [`tree`](#tree) |
| Computed Role | `tree` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_OUTLINE`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `Tree` |
| ATK/AT-SPI | Role: `ROLE_TREE`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXOutline`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.96 `treegrid`

|  |  |
| --- | --- |
| ARIA Specification | [`treegrid`](#treegrid) |
| Computed Role | `treegrid` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_OUTLINE`  Interface: `IAccessibleTable2`  Method: `IAccessible::accSelect()`  Method: `IAccessible::get_accSelection()` |
| UIA | Control Type: `DataGrid` |
| ATK/AT-SPI | Role: `ROLE_TREE_TABLE`  Interface: `Table`  Interface: `Selection` Because WAI-ARIA does not support modifying the selection via the accessibility API, user agents *MUST* return `false` for all `Selection` methods that provide a means to modify the selection. |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXTable`  AXSubrole: `<nil>` |
| Android | TBD |

##### 3.4.3.97 `treeitem`

|  |  |
| --- | --- |
| ARIA Specification | [`treeitem`](#treeitem) |
| Computed Role | `treeitem` |
| MSAA + IAccessible2 | Role: `ROLE_SYSTEM_OUTLINEITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| UIA | Control Type: `TreeItem`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| ATK/AT-SPI | Role: `ROLE_TREE_ITEM`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| AX API[[Note 1](#ftn.note1)] | AXRole: `AXRow`  AXSubrole: `AXOutlineRow`  See also: `aria-checked` in the [State and Property Mapping Tables](#mapping_state-property_table) |
| Android | TBD |

Note

[Note 1]
User agent should return a user-presentable, localized string value for the AXRoleDescription.

Note

[Note 2] This specification does not currently contain guidance for when user agents should fire system alert events. Some guidance may be added to the specification at a
later date but it will be a recommendation (*SHOULD*), not a requirement (*MUST*).

### 3.5 State and Property Mapping

This section describes how to expose WAI-ARIA [states](https://www.w3.org/TR/wai-aria/#dfn-state) and [properties](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.").

#### 3.5.1 General rules

1. [User agents](https://infra.spec.whatwg.org/#user-agent) *MUST* compute [managed states](https://www.w3.org/TR/wai-aria/#dfn-managed-state) `VISIBLE`/`INVISIBLE`, `SHOWING`/`OFFSCREEN`, etc. This typically is done
   in the same way as for ordinary [elements](https://dom.spec.whatwg.org/#concept-element) that do not have WAI-ARIA attributes present. The
   `FOCUSABLE`/`FOCUSED` states may be affected by [`aria-activedescendant`](#aria-activedescendant).
2. User agents *MUST* continue to expose native semantics in addition to WAI-ARIA state and property semantics except where an
   explicit WAI-ARIA override is allowed by the host language. For example, an HTML checkbox may have an
   [`aria-labelledby`](#aria-labelledby) attribute but the native HTML semantics must still
   be exposed.
3. User agents *MUST* expose additional states for certain [roles](https://www.w3.org/TR/wai-aria/#dfn-role) as defined in the [Role Mapping Tables](#mapping_role_table).
4. User agents *MUST* compute states for the relevant WAI-ARIA [attributes](https://dom.spec.whatwg.org/#concept-attribute) and map to the
   [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) as specified in the [State and Property Mapping Tables](#mapping_state-property_table). To determine the relevant
   WAI-ARIA attributes, refer to the
   [Definition of Roles](#role_definitions "Broken local reference found in document.") [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")]]. Where the author has not provided values for required attributes, user agents *SHOULD*
   process as if the default value was provided.
5. Some WAI-ARIA properties are not global, and are only supported on certain roles. If a non-global
   WAI-ARIA state or property is used where it is not supported, user agents *SHOULD NOT* map the given
   WAI-ARIA property to the platform accessibility API. For example, if
   `aria-checked="true"` is specified on `<div role="grid">`, it should not be exposed in
   MSAA implementations as `STATE_SYSTEM_CHECKED`.
6. When an explicit or inherited role of `none` or `presentation` is applied to an element, the user agent *MUST* implement the rules for the
   [`none`](#none) or the [`presentation`](#presentation) [role](https://www.w3.org/TR/wai-aria/#dfn-role) defined in
   Accessible Rich Internet Applications (WAI-ARIA) 1.2 [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")]].

#### 3.5.2 State and Property Mapping Tables

##### 3.5.2.1 Not Mapped

There are a number of occurrences in the table where a given state or property is declared "Not mapped". In some cases, this occurs for the default value of the state/property, and is
equivalent to its absence. User agents might find it quicker to map the value than check to see if it is the default. For computational efficiency, user agents *MAY* expose the state or
property value if doing so is equivalent to not mapping it. These cases are marked with an asterisk.

In other cases, it is mandatory that the state/property not be mapped, since exposing it implies a related affordance. An example is
[`aria-grabbed`](#aria-grabbed "Broken local reference found in document."). Its absence not only indicates that the accessible object is not grabbed, but further defines it as not grab-able. These cases are marked as "Not mapped" without an asterisk.

##### 3.5.2.2 `aria-activedescendant`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-activedescendant`](#aria-activedescendant) |
| MSAA + IAccessible2 | See [Focus Changes](#focus_state_event_table). |
| UIA | See [Focus Changes](#focus_state_event_table). |
| ATK/AT-SPI | See [Focus Changes](#focus_state_event_table). |
| AX API | See [Focus Changes](#focus_state_event_table).  Property: `AXSelectedRows`: pointer to active descendant node |
| Android | TBD |

##### 3.5.2.3 `aria-atomic`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-atomic`](#aria-atomic "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | Object Attribute: `atomic:true`  Object Attribute: `container-atomic:true`  Object Attribute: `container-atomic:true` on all descendants  Relation: `IA2_RELATION_MEMBER_OF` pointing to this element (the atomic root)  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| UIA | Property: `AriaProperties.atomic`: `true`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| ATK/AT-SPI | Object Attribute: `atomic:true`  Object Attribute: `container-atomic:true`  Object Attribute: `container-atomic:true` on all descendants  Relation: `RELATION_MEMBER_OF` pointing to this element (the atomic root)  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| AX API | Property: `AXARIAAtomic`: `YES`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| Android | TBD |

##### 3.5.2.4 `aria-atomic`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-atomic`](#aria-atomic "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | [Not mapped\*](#not_mapped), but if mapped:  Object Attribute: `atomic:false`  Object Attribute: `container-atomic:false`  Object Attribute: `container-atomic:false` on all descendants  Relation: `IA2_RELATION_MEMBER_OF` pointing to this element (the atomic root)  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| UIA | Property: `AriaProperties.atomic`: `false`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| ATK/AT-SPI | [Not mapped\*](#not_mapped), but if mapped:  Object Attribute: `atomic:false`  Object Attribute: `container-atomic:false`  Object Attribute: `container-atomic:false` on all descendants  Relation: `RELATION_MEMBER_OF` pointing to this element (the atomic root)  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| AX API | Property: `AXARIAAtomic`: `NO`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| Android | TBD |

##### 3.5.2.5 `aria-autocomplete`=`inline`, `list`, or `both`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-autocomplete`](#aria-autocomplete "Broken local reference found in document.")=`inline`, `list`, or `both` |
| MSAA + IAccessible2 | Object Attribute: `autocomplete:<value>`  State: `IA2_STATE_SUPPORTS_AUTOCOMPLETION` |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | Object Attribute: `autocomplete:<value>`  State: `STATE_SUPPORTS_AUTOCOMPLETION` |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.6 `aria-autocomplete`=`none`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-autocomplete`](#aria-autocomplete "Broken local reference found in document.")=`none` |
| MSAA + IAccessible2 | [Not mapped\*](#not_mapped) |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | [Not mapped\*](#not_mapped) |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.7 `aria-braillelabel`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-braillelabel`](#aria-braillelabel) |
| MSAA + IAccessible2 | Object Attribute: `braillelabel:<value>` |
| UIA | Property: `AriaProperties.braillelabel`: `<value>` |
| ATK/AT-SPI | Object Attribute: `braillelabel:<value>` |
| AX API | Property: AXBrailleLabel |
| Android | TBD |

##### 3.5.2.8 `aria-brailleroledescription`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-brailleroledescription`](#aria-brailleroledescription) |
| MSAA + IAccessible2 | Object Attribute: `brailleroledescription:<value>` |
| UIA | Property: `AriaProperties.brailleroledescription`: `<value>` |
| ATK/AT-SPI | Object Attribute: `brailleroledescription:<value>` |
| AX API | Property: AXBrailleRoleDescription |
| Android | TBD |

##### 3.5.2.9 `aria-brailleroledescription` is undefined or the empty string

|  |  |
| --- | --- |
| ARIA Specification | [`aria-brailleroledescription`](#aria-brailleroledescription) is undefined or the empty string |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.10 `aria-busy`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-busy`](#aria-busy "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_BUSY` |
| UIA | Property: `AriaProperties.busy`: `true` |
| ATK/AT-SPI | State: `STATE_BUSY` |
| AX API | Property: `AXElementBusy`: `YES` |
| Android | TBD |

##### 3.5.2.11 `aria-busy`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-busy`](#aria-busy "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_BUSY` not exposed |
| UIA | Property: `AriaProperties.busy`: `false` |
| ATK/AT-SPI | State: `STATE_BUSY` not exposed |
| AX API | Property: `AXElementBusy`: `NO` |
| Android | TBD |

##### 3.5.2.12 `aria-checked`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-checked`](#aria-checked "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_CHECKED`  Object Attribute: `checkable:true` |
| UIA | Property: `Toggle.ToggleState`: `On (1)`  Property: `SelectionItem.IsSelected`: `True` for `radio` and `menuitemradio` |
| ATK/AT-SPI | State: `STATE_CHECKABLE`  State: `STATE_CHECKED` |
| AX API | Property: `AXValue`: `1`  Property: `AXMenuItemMarkChar`: `✓` for `menuitemcheckbox` and `menuitemradio` |
| Android | TBD |

##### 3.5.2.13 `aria-checked`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-checked`](#aria-checked "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_CHECKED` not exposed  Object Attribute: `checkable:true` |
| UIA | Property: `Toggle.ToggleState`: `Off (0)`  Property: `SelectionItem.IsSelected`: `False` for `radio` and `menuitemradio` |
| ATK/AT-SPI | State: `STATE_CHECKABLE`  State: `STATE_CHECKED` not exposed |
| AX API | Property: `AXValue`: `0`  Property: `AXMenuItemMarkChar`: `<nil>` for `menuitemcheckbox` and `menuitemradio` |
| Android | TBD |

##### 3.5.2.14 `aria-checked`=`mixed`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-checked`](#aria-checked "Broken local reference found in document.")=`mixed` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_MIXED`  Object Attribute: `checkable:true` |
| UIA | Property: `Toggle.ToggleState`: `Indeterminate (2)` |
| ATK/AT-SPI | State: `STATE_INDETERMINATE`  State: `STATE_CHECKABLE`  State: `STATE_CHECKED` not exposed |
| AX API | Property: `AXValue`: `2`  Property: `AXMenuItemMarkChar`: `<nil>` for `menuitemcheckbox` and `menuitemradio` |
| Android | TBD |

##### 3.5.2.15 `aria-checked` is undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-checked`](#aria-checked "Broken local reference found in document.") is undefined |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.16 `aria-colcount`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-colcount`](#aria-colcount) |
| MSAA + IAccessible2 | Object Attribute: `colcount:<value>`  Method: `IAccessible2::groupPosition()`: `similarItemsInGroup=<value>` on cells and headers |
| UIA | Property: `Grid.ColumnCount`: `<value>` |
| ATK/AT-SPI | Object Attribute: `colcount` should contain the author-provided value.  Method: `atk_table_get_n_columns()` should return the actual number of columns. |
| AX API | Property: `AXARIAColumnCount`: `<value>` |
| Android | TBD |

##### 3.5.2.17 `aria-colindex`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-colindex`](#aria-colindex) |
| MSAA + IAccessible2 | Object Attribute: `colindex:<value>`  Method: `IAccessible2::groupPosition()`: `positionInGroup=<value>` on cells and headers |
| UIA | Property: `GridItem.Column`: `<value>` (zero-based) |
| ATK/AT-SPI | Object Attribute: `colindex` should contain the author-provided value.  Method: `atk_table_cell_get_position()` should return the actual (zero-based) column index. |
| AX API | Property: `AXARIAColumnIndex`: `<value>` |
| Android | TBD |

##### 3.5.2.18 `aria-colindextext`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-colindextext`](#aria-colindextext) |
| MSAA + IAccessible2 | Object Attribute: `colindextext:<value>` |
| UIA | Property: `AriaProperties.colindextext`: `<value>` |
| ATK/AT-SPI | Object Attribute: `colindextext:<value>` |
| AX API | Property: `AXColumnIndexDescription`: `<value>` |
| Android | TBD |

##### 3.5.2.19 `aria-colspan`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-colspan`](#aria-colspan) |
| MSAA + IAccessible2 | Object Attribute: `colspan:<value>`  Method: `IAccessibleTableCell::columnExtent()`: `<value>` |
| UIA | Property: `GridItem.ColumnSpan`: `<value>` |
| ATK/AT-SPI | Object Attribute: `colspan` should contain the author-provided value.  Method: `atk_table_cell_get_row_column_span()` should return the actual column span. |
| AX API | Property: `AXColumnIndexRange.length`: `<value>` |
| Android | TBD |

##### 3.5.2.20 `aria-controls`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-controls`](#aria-controls) |
| MSAA + IAccessible2 | Relation: `IA2_RELATION_CONTROLLER_FOR` points to accessible nodes matching IDREFs  Reverse Relation: `IA2_RELATION_CONTROLLED_BY` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Property: `ControllerFor`: pointers to accessible nodes matching IDREFs |
| ATK/AT-SPI | Relation: `RELATION_CONTROLLER_FOR` points to accessible nodes matching IDREFs  Reverse Relation: `RELATION_CONTROLLED_BY` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | Property: `AXLinkedUIElements`: pointers to accessible nodes matching IDREFs |
| Android | TBD |

##### 3.5.2.21 `aria-current` with non-`false` allowed value

|  |  |
| --- | --- |
| ARIA Specification | [`aria-current`](#aria-current "Broken local reference found in document.") with non-`false` allowed value |
| MSAA + IAccessible2 | Object Attribute: `current:<value>` |
| UIA | Property: `AriaProperties.current`: `<value>` |
| ATK/AT-SPI | Object Attribute: `current:<value>`  State: `STATE_ACTIVE` |
| AX API | Property: `AXARIACurrent`: `<value>` |
| Android | TBD |

##### 3.5.2.22 `aria-current` with unrecognized value

|  |  |
| --- | --- |
| ARIA Specification | [`aria-current`](#aria-current "Broken local reference found in document.") with unrecognized value |
| MSAA + IAccessible2 | Object Attribute: `current:true` |
| UIA | Property: `AriaProperties.current`: `true` |
| ATK/AT-SPI | Object Attribute: `current:true`  State: `STATE_ACTIVE` |
| AX API | Property: `AXARIACurrent`: `true` |
| Android | TBD |

##### 3.5.2.23 `aria-current` is `false` or undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-current`](#aria-current "Broken local reference found in document.") is `false` or undefined |
| MSAA + IAccessible2 | [Not mapped\*](#not_mapped) |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | [Not mapped\*](#not_mapped) |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.24 `aria-describedby`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-describedby`](#aria-describedby) |
| MSAA + IAccessible2 | Property: `accDescription`: `<value>`  Relation: `IA2_RELATION_DESCRIBED_BY` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `IA2_RELATION_DESCRIPTION_FOR` points to element  See also: [Name Computation](#mapping_additional_nd) and [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Property: `FullDescription`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| ATK/AT-SPI | Property: `Description`: `<value>`  Relation: `RELATION_DESCRIBED_BY` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `RELATION_DESCRIPTION_FOR` points to element  See also: [Name Computation](#mapping_additional_nd) and [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | In the accessibilityCustomContent API, expose as an `AXCustomContent` object with `{ label: "description" }` and ``value`` set to the description string.  - See also: [Name Computation](#mapping_additional_nd) |
| Android | TBD |

##### 3.5.2.25 `aria-description`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-description`](#aria-description) |
| MSAA + IAccessible2 | Property: `accDescription`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| UIA | Property: `FullDescription`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| ATK/AT-SPI | Property: `Description`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| AX API | In the accessibilityCustomContent API, expose as an `AXCustomContent` object with `{ label: "description" }` and ``value`` set to the description string.  See also: [Name Computation](#mapping_additional_nd) |
| Android | TBD |

##### 3.5.2.26 `aria-details`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-details`](#aria-details) |
| MSAA + IAccessible2 | Relation: `IA2_RELATION_DETAILS` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `IA2_RELATION_DETAILS_FOR` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Property: `DescribedBy`: points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree |
| ATK/AT-SPI | Relation: `RELATION_DETAILS` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `RELATION_DETAILS_FOR` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.27 `aria-disabled`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-disabled`](#aria-disabled "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_UNAVAILABLE`  State: `STATE_SYSTEM_UNAVAILABLE` on all descendants with `STATE_SYSTEM_FOCUSABLE` |
| UIA | Property: `IsEnabled`: `false` |
| ATK/AT-SPI | State: `STATE_ENABLED` not exposed |
| AX API | Property: `AXEnabled`: `NO` |
| Android | TBD |

##### 3.5.2.28 `aria-disabled`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-disabled`](#aria-disabled "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_UNAVAILABLE` not exposed |
| UIA | Property: `IsEnabled`: `true` |
| ATK/AT-SPI | State: `STATE_ENABLED` |
| AX API | Property: `AXEnabled`: `YES` |
| Android | TBD |

##### 3.5.2.29 `aria-dropeffect`=`copy`, `move`, `link`, `execute`, or `popup` (deprecated)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-dropeffect`](#aria-dropeffect "Broken local reference found in document.")=`copy`, `move`, `link`, `execute`, or `popup` |
| MSAA + IAccessible2 | Object Attribute: `dropeffect:<value>` |
| UIA | Property: `AriaProperties.dropeffect`: `<value>` |
| ATK/AT-SPI | Object Attribute: `dropeffect:<value>` |
| AX API | `array AXDropEffects` |
| Android | TBD |

##### 3.5.2.30 `aria-dropeffect`=`none` (deprecated)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-dropeffect`](#aria-dropeffect "Broken local reference found in document.")=`none` |
| MSAA + IAccessible2 | Object Attribute: `dropeffect:none` if there are no other valid tokens  [Not mapped\*](#not_mapped) if not specified by the author |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | Object Attribute: `dropeffect:none` if there are no other valid tokens  [Not mapped\*](#not_mapped) if not specified by the author |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.31 `aria-errormessage`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-errormessage`](#aria-errormessage) |
| MSAA + IAccessible2 | Relation: `IA2_RELATION_ERROR` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `IA2_RELATION_ERROR_FOR` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Property: `ControllerFor`: pointer to the target accessible object |
| ATK/AT-SPI | Relation: `RELATION_ERROR_MESSAGE` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `RELATION_ERROR_FOR` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | Property: `AXErrorMessageElements`: pointers to accessible nodes matching IDREFs |
| Android | TBD |

##### 3.5.2.32 `aria-expanded`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-expanded`](#aria-expanded "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_EXPANDED` |
| UIA | Property: `ExpandCollapse.ExpandCollapseState`: `Expanded` |
| ATK/AT-SPI | State: `STATE_EXPANDABLE`  State: `STATE_EXPANDED` |
| AX API | Property: `AXExpanded`: `YES` |
| Android | TBD |

##### 3.5.2.33 `aria-expanded`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-expanded`](#aria-expanded "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_COLLAPSED` |
| UIA | Property: `ExpandCollapse.ExpandCollapseState`: `Collapsed` |
| ATK/AT-SPI | State: `STATE_EXPANDABLE`  State: `STATE_EXPANDED` not exposed |
| AX API | Property: `AXExpanded`: `NO` |
| Android | TBD |

##### 3.5.2.34 `aria-expanded` is undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-expanded`](#aria-expanded "Broken local reference found in document.") is undefined |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.35 `aria-flowto`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-flowto`](#aria-flowto) |
| MSAA + IAccessible2 | Relation: `IA2_RELATION_FLOW_TO` points to accessible nodes matching IDREFs  Reverse Relation: `IA2_RELATION_FLOW_FROM` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Property: `FlowsTo`: pointers to accessible nodes matching IDREFs |
| ATK/AT-SPI | Relation: `RELATION_FLOWS_TO` points to accessible nodes matching IDREFs  Reverse Relation: `RELATION_FLOWS_FROM` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | Property: `AXLinkedUIElements`: pointers to accessible nodes matching IDREFs |
| Android | TBD |

##### 3.5.2.36 `aria-grabbed`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-grabbed`](#aria-grabbed "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | Object Attribute: `grabbed:true` |
| UIA | Property: `AriaProperties.grabbed`: `true` |
| ATK/AT-SPI | Object Attribute: `grabbed:true` |
| AX API | Property: `AXGrabbed`: `YES` |
| Android | TBD |

##### 3.5.2.37 `aria-grabbed`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-grabbed`](#aria-grabbed "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | Object Attribute: `grabbed:false` |
| UIA | Property: `AriaProperties.grabbed`: `false` |
| ATK/AT-SPI | Object Attribute: `grabbed:false` |
| AX API | Property: `AXGrabbed`: `NO` |
| Android | TBD |

##### 3.5.2.38 `aria-grabbed` is undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-grabbed`](#aria-grabbed "Broken local reference found in document.") is undefined |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.39 `aria-haspopup`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP`  Object Attribute: `haspopup:menu` |
| UIA | Control Pattern: `ExpandCollapse` See also: [`aria-expanded`](#aria-expanded "Broken local reference found in document.") |
| ATK/AT-SPI | State: `STATE_HAS_POPUP`  Object Attribute: `haspopup:menu` |
| AX API | Property: `AXPopupValue:menu`  Action: `AXShowMenu` |
| Android | TBD |

##### 3.5.2.40 `aria-haspopup`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP` not exposed  Object Attribute: `haspopup:false` |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | [Not mapped\*](#not_mapped) |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.41 `aria-haspopup`=`dialog`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`dialog` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP`  Object Attribute: `haspopup:dialog` |
| UIA | Control Pattern: `ExpandCollapse`  See also: [`aria-expanded`](#aria-expanded "Broken local reference found in document.") |
| ATK/AT-SPI | State: `STATE_HAS_POPUP`  Object Attribute: `haspopup:dialog` |
| AX API | Property: `AXPopupValue:dialog`  Action: `AXShowMenu` |
| Android | TBD |

##### 3.5.2.42 `aria-haspopup`=`grid`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`grid` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP`  Object Attribute: `haspopup:grid` |
| UIA | Control Pattern: `ExpandCollapse`  See also: [`aria-expanded`](#aria-expanded "Broken local reference found in document.") |
| ATK/AT-SPI | State: `STATE_HAS_POPUP`  Object Attribute: `haspopup:grid` |
| AX API | Property: `AXPopupValue:grid`  Action: `AXShowMenu` |
| Android | TBD |

##### 3.5.2.43 `aria-haspopup`=`listbox`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`listbox` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP`  Object Attribute: `haspopup:listbox` |
| UIA | Control Pattern: `ExpandCollapse`  See also: [`aria-expanded`](#aria-expanded "Broken local reference found in document.") |
| ATK/AT-SPI | State: `STATE_HAS_POPUP`  Object Attribute: `haspopup:listbox` |
| AX API | Property: `AXPopupValue:listbox`  Action: `AXShowMenu` |
| Android | TBD |

##### 3.5.2.44 `aria-haspopup`=`menu`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`menu` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP`  Object Attribute: `haspopup:menu` |
| UIA | Control Pattern: `ExpandCollapse`  See also: [`aria-expanded`](#aria-expanded "Broken local reference found in document.") |
| ATK/AT-SPI | State: `STATE_HAS_POPUP`  Object Attribute: `haspopup:menu` |
| AX API | Property: `AXPopupValue:menu`  Action: `AXShowMenu` |
| Android | TBD |

##### 3.5.2.45 `aria-haspopup`=`tree`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-haspopup`](#aria-haspopup "Broken local reference found in document.")=`tree` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_HASPOPUP`  Object Attribute: `haspopup:tree` |
| UIA | Control Pattern: `ExpandCollapse`  See also: [`aria-expanded`](#aria-expanded "Broken local reference found in document.") |
| ATK/AT-SPI | State: `STATE_HAS_POPUP`  Object Attribute: `haspopup:tree` |
| AX API | Property: `AXPopupValue:tree`  Action: `AXShowMenu` |
| Android | TBD |

##### 3.5.2.46 `aria-hidden`=`true` on unfocused element

|  |  |
| --- | --- |
| ARIA Specification | [`aria-hidden`](#aria-hidden "Broken local reference found in document.")=`true` on unfocused element |
| MSAA + IAccessible2 | Element *SHOULD NOT* be exposed  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| UIA | Element *SHOULD NOT* be exposed  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| ATK/AT-SPI | Element *SHOULD NOT* be exposed  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| AX API | Element *SHOULD NOT* be exposed  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| Android | TBD |

##### 3.5.2.47 `aria-hidden`=`true` when element is focused or fires an accessibility event

|  |  |
| --- | --- |
| ARIA Specification | [`aria-hidden`](#aria-hidden "Broken local reference found in document.")=`true` when element is focused or fires an accessibility event |
| MSAA + IAccessible2 | Object Attribute: `hidden:true`  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| UIA | Property: `AriaProperties.hidden`: `true`  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| ATK/AT-SPI | Object Attribute: `hidden:true`  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| AX API | [Not mapped](#not_mapped)  See also: [Including Elements in the Accessibility Tree in the WAI-ARIA specification](#tree_inclusion "Broken local reference found in document.") |
| Android | TBD |

##### 3.5.2.48 `aria-hidden`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-hidden`](#aria-hidden "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.49 `aria-invalid`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-invalid`](#aria-invalid "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `IA2_STATE_INVALID_ENTRY`  Text Attribute: `invalid:true` |
| UIA | Property: `IsDataValidForForm`: `false` |
| ATK/AT-SPI | State: `STATE_INVALID_ENTRY`  Text Attribute: `invalid:true` |
| AX API | Property: `AXInvalid`: `true` |
| Android | TBD |

##### 3.5.2.50 `aria-invalid`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-invalid`](#aria-invalid "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `IA2_STATE_INVALID_ENTRY` not exposed |
| UIA | Property: `IsDataValidForForm`: `true` |
| ATK/AT-SPI | State: `STATE_INVALID_ENTRY` not exposed |
| AX API | Property: `AXInvalid`: `false` |
| Android | TBD |

##### 3.5.2.51 `aria-invalid`=`spelling` or `grammar`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-invalid`](#aria-invalid "Broken local reference found in document.")=`spelling` or `grammar` |
| MSAA + IAccessible2 | State: `IA2_STATE_INVALID_ENTRY`  Text Attribute: `invalid:<value>` |
| UIA | Property: `IsDataValidForForm`: `<value>` |
| ATK/AT-SPI | State: `STATE_INVALID_ENTRY`  Text Attribute: `invalid:<value>` |
| AX API | Property: `AXInvalid`: `<value>` |
| Android | TBD |

##### 3.5.2.52 `aria-invalid` with unrecognized value

|  |  |
| --- | --- |
| ARIA Specification | [`aria-invalid`](#aria-invalid "Broken local reference found in document.") with unrecognized value |
| MSAA + IAccessible2 | State: `IA2_STATE_INVALID_ENTRY`  Text Attribute: `invalid:true` |
| UIA | Property: `IsDataValidForForm`: `false` |
| ATK/AT-SPI | State: `STATE_INVALID_ENTRY`  Text Attribute: `invalid:true` |
| AX API | Property: `AXInvalid`: `true` |
| Android | TBD |

##### 3.5.2.53 `aria-keyshortcuts`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-keyshortcuts`](#aria-keyshortcuts) |
| MSAA + IAccessible2 | Property: `accKeyboardShortcut`: `<value>` |
| UIA | Property: `AcceleratorKey`: `<value>` |
| ATK/AT-SPI | Object Attribute: `keyshortcuts:<value>` |
| AX API | Property: `AXKeyShortcutsValue`: `<value>` |
| Android | TBD |

##### 3.5.2.54 `aria-label`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-label`](#aria-label) |
| MSAA + IAccessible2 | Property: `accName`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| UIA | Property: `Name`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| ATK/AT-SPI | Property: `Name`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| AX API | Property: `AXTitle`: `<value>`  See also: [Name Computation](#mapping_additional_nd) |
| Android | TBD |

##### 3.5.2.55 `aria-labelledby`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-labelledby`](#aria-labelledby) |
| MSAA + IAccessible2 | Property: `accName`: `<value>`  Relation: `IA2_RELATION_LABELLED_BY` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `IA2_RELATION_LABEL_FOR` points to element  See also: [Name Computation](#mapping_additional_nd) and [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Property: `Name`: `<value>`  Property: `LabeledBy`: points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  See also: [Name Computation](#mapping_additional_nd) |
| ATK/AT-SPI | Property: `Name`: `<value>`  Relation: `RELATION_LABELLED_BY` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `RELATION_LABEL_FOR` points to element  See also: [Name Computation](#mapping_additional_nd) and [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | Property: `AXTitle`: `<value>`  Property: `AXTitleUIElement` points to accessible node matching IDREF, if there is a single referenced element that is in the accessibility tree  See also: [Name Computation](#mapping_additional_nd) |
| Android | TBD |

##### 3.5.2.56 `aria-level` on non-`heading`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-level`](#aria-level "Broken local reference found in document.") on non-`heading` |
| MSAA + IAccessible2 | Object Attribute: `level:<value>`  Method: `IAccessible2::groupPosition()`: `groupLevel=<value>` on roles that support `aria-posinset` and `aria-setsize`  See also: [`groupPosition()`](#mapping_group_position) |
| UIA | Property: `AriaProperties.level`: `<value>` |
| ATK/AT-SPI | Object Attribute: `level:<value>` |
| AX API | Property: `AXDisclosureLevel`: `<value>` (zero-based), when used on an outline row (like a [`treeitem`](#treeitem) or [`group`](#group)) |
| Android | TBD |

##### 3.5.2.57 `aria-level` on `heading`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-level`](#aria-level "Broken local reference found in document.") on `heading` |
| MSAA + IAccessible2 | Object Attribute: `level:<value>` |
| UIA | Property: `AriaProperties.level`: `<value>`  Property: `StyleId_Heading`: `<value>` |
| ATK/AT-SPI | Object Attribute: `level:<value>` |
| AX API | Property: `AXValue`: `<value>` |
| Android | TBD |

##### 3.5.2.58 `aria-live`=`assertive`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-live`](#aria-live "Broken local reference found in document.")=`assertive` |
| MSAA + IAccessible2 | Object Attribute: `live:assertive`  Object Attribute: `container-live:assertive`  Object Attribute: `container-live:assertive` on all descendants  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| UIA | Property: `LiveSetting`: `"assertive"`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| ATK/AT-SPI | Object Attribute: `live:assertive`  Object Attribute: `container-live:assertive`  Object Attribute: `container-live:assertive` on all descendants  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| AX API | Property: `AXARIALive`: `"assertive"`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| Android | TBD |

##### 3.5.2.59 `aria-live`=`polite`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-live`](#aria-live "Broken local reference found in document.")=`polite` |
| MSAA + IAccessible2 | Object Attribute: `live:polite`  Object Attribute: `container-live:polite`  Object Attribute: `container-live:polite` on all descendants  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| UIA | Property: `LiveSetting`: `"polite"`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| ATK/AT-SPI | Object Attribute: `live:polite`  Object Attribute: `container-live:polite`  Object Attribute: `container-live:polite` on all descendants  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| AX API | Property: `AXARIALive`: `"polite"`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| Android | TBD |

##### 3.5.2.60 `aria-live`=`off`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-live`](#aria-live "Broken local reference found in document.")=`off` |
| MSAA + IAccessible2 | Object Attribute: `live:off`  Object Attribute: `container-live:off`  Object Attribute: `container-live:off` on all descendants |
| UIA | Property: `LiveSetting`: `"off"` |
| ATK/AT-SPI | Object Attribute: `live:off`  Object Attribute: `container-live:off`  Object Attribute: `container-live:off` on all descendants |
| AX API | Property: `AXARIALive`: `"off"` |
| Android | TBD |

##### 3.5.2.61 `aria-modal`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-modal`](#aria-modal "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `IA2_STATE_MODAL` |
| UIA | Property: `Window.IsModal`: `true` |
| ATK/AT-SPI | State: `STATE_MODAL` |
| AX API | Prune the accessibility tree such that the background content is no longer exposed. No specific property is set on the [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) that corresponds to the [element](https://dom.spec.whatwg.org/#concept-element) with `aria-modal="true"`. Only the tree whose root is that modal accessible object is exposed. |
| Android | TBD |

##### 3.5.2.62 `aria-modal`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-modal`](#aria-modal "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `IA2_STATE_MODAL` not exposed |
| UIA | Property: `Window.IsModal`: `false` |
| ATK/AT-SPI | State: `STATE_MODAL` not exposed |
| AX API | Grow the accessibility tree such that the background content is exposed. No specific property is set on the [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) that corresponds to the [element](https://dom.spec.whatwg.org/#concept-element) with `aria-modal="false"`. |
| Android | TBD |

##### 3.5.2.63 `aria-multiline`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-multiline`](#aria-multiline "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `IA2_STATE_MULTI_LINE`  State: `IA2_STATE_SINGLE_LINE` not exposed |
| UIA | Property: `AriaProperties.multiline`: `true` |
| ATK/AT-SPI | State: `STATE_MULTI_LINE`  State: `STATE_SINGLE_LINE` not exposed |
| AX API | [Not mapped](#not_mapped)  See also: [`textbox`](#role-map-textbox) in the Role Mapping Tables |
| Android | TBD |

##### 3.5.2.64 `aria-multiline`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-multiline`](#aria-multiline "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `IA2_STATE_SINGLE_LINE`  State: `IA2_STATE_MULTI_LINE` not exposed |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | State: `STATE_SINGLE_LINE`  State: `STATE_MULTI_LINE` not exposed |
| AX API | [Not mapped](#not_mapped)  See also: [`textbox`](#role-map-textbox) in the Role Mapping Tables |
| Android | TBD |

##### 3.5.2.65 `aria-multiselectable`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-multiselectable`](#aria-multiselectable "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_MULTISELECTABLE`  State: `STATE_SYSTEM_EXTSELECTABLE`  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| UIA | Property: `Selection.CanSelectMultiple`: `true`  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| ATK/AT-SPI | State: `STATE_MULTISELECTABLE`  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| AX API | Property: `AXIsMultiSelectable`: `YES`  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| Android | TBD |

##### 3.5.2.66 `aria-multiselectable`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-multiselectable`](#aria-multiselectable "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_MULTISELECTABLE` not exposed  State: `STATE_SYSTEM_EXTSELECTABLE` not exposed  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | State: `STATE_MULTISELECTABLE` not exposed |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.67 `aria-orientation`=`horizontal`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-orientation`](#aria-orientation "Broken local reference found in document.")=`horizontal` |
| MSAA + IAccessible2 | State: `IA2_STATE_HORIZONTAL`  State: `IA2_STATE_VERTICAL` not exposed |
| UIA | Property: `Orientation`: `horizontal` |
| ATK/AT-SPI | State: `STATE_HORIZONTAL`  State: `STATE_VERTICAL` not exposed |
| AX API | Property: `AXOrientation`: `AXHorizontalOrientation` |
| Android | TBD |

##### 3.5.2.68 `aria-orientation`=`vertical`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-orientation`](#aria-orientation "Broken local reference found in document.")=`vertical` |
| MSAA + IAccessible2 | State: `IA2_STATE_VERTICAL`  State: `IA2_STATE_HORIZONTAL` not exposed |
| UIA | Property: `Orientation`: `vertical` |
| ATK/AT-SPI | State: `STATE_VERTICAL`  State: `STATE_HORIZONTAL` not exposed |
| AX API | Property: `AXOrientation`: `AXVerticalOrientation` |
| Android | TBD |

##### 3.5.2.69 `aria-orientation` is undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-orientation`](#aria-orientation "Broken local reference found in document.") is undefined |
| MSAA + IAccessible2 | [Not mapped\*](#not_mapped) |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | State: `STATE_VERTICAL` not exposed  State: `STATE_HORIZONTAL` not exposed |
| AX API | Property: `AXOrientation`: `AXUnknownOrientation` |
| Android | TBD |

##### 3.5.2.70 `aria-owns`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-owns`](#aria-owns) |
| MSAA + IAccessible2 | User agents *MAY* expose the elements that are referenced by this property as children of the current element. In which case, if multiple [`aria-owns`](#aria-owns) relationships are found, use only the first one. If the accessibility tree is not modified, expose as: Relation: `IA2_RELATION_NODE_PARENT_OF` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `IA2_RELATION_NODE_CHILD_OF` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| UIA | Expose the elements that are referenced by this property as children of the current element. If multiple [`aria-owns`](#aria-owns) relationships are found, use only the first one. |
| ATK/AT-SPI | User agents *MAY* expose the elements that are referenced by this property as children of the current element. In which case, if multiple [`aria-owns`](#aria-owns) relationships are found, use only the first one. If the accessibility tree is not modified, expose as: Relation: `RELATION_NODE_PARENT_OF` points to accessible nodes matching IDREFs, if the referenced objects are in the accessibility tree  Reverse Relation: `RELATION_NODE_CHILD_OF` points to element  See also: [Mapping Additional Relations](#mapping_additional_relations) |
| AX API | Property: `AXOwns`: pointers to accessible nodes matching IDREFs |
| Android | TBD |

##### 3.5.2.71 `aria-placeholder`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-placeholder`](#aria-placeholder) |
| MSAA + IAccessible2 | Object Attribute: `placeholder-text:<value>` |
| UIA | Property: `HelpText`: `<value>` |
| ATK/AT-SPI | Object Attribute: `placeholder-text:<value>` |
| AX API | Property: `AXPlaceholderValue`: `<value>` |
| Android | TBD |

##### 3.5.2.72 `aria-posinset`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-posinset`](#aria-posinset) |
| MSAA + IAccessible2 | Object Attribute: `posinset:<value>`  See also: [Group Position](#mapping_additional_position) |
| UIA | Property: `AriaProperties.posinset`: `<value>`  See also: [Group Position](#mapping_additional_position) |
| ATK/AT-SPI | Object Attribute: `posinset:<value>`  See also: [Group Position](#mapping_additional_position) |
| AX API | Property: `AXARIAPosInSet`: `<value>`  See also: [Group Position](#mapping_additional_position) |
| Android | TBD |

##### 3.5.2.73 `aria-pressed`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-pressed`](#aria-pressed "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_PRESSED`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| UIA | Property: `Toggle.ToggleState`: `On (1)` |
| ATK/AT-SPI | State: `STATE_PRESSED`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| AX API | Property: `AXValue`: `1`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| Android | TBD |

##### 3.5.2.74 `aria-pressed`=`mixed`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-pressed`](#aria-pressed "Broken local reference found in document.")=`mixed` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_MIXED`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| UIA | Property: `Toggle.ToggleState`: `Indeterminate (2)` |
| ATK/AT-SPI | State: `STATE_INDETERMINATE`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| AX API | Property: `AXValue`: `2`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| Android | TBD |

##### 3.5.2.75 `aria-pressed`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-pressed`](#aria-pressed "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_PRESSED` not exposed  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| UIA | Property: `Toggle.ToggleState`: `Off (3)` |
| ATK/AT-SPI | State: `STATE_PRESSED` not exposed  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| AX API | Property: `AXValue`: `0`  See also: [`button` with defined value for `aria-pressed`](#role-map-button-pressed) |
| Android | TBD |

##### 3.5.2.76 `aria-pressed` is undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-pressed`](#aria-pressed "Broken local reference found in document.") is undefined |
| MSAA + IAccessible2 | [Not mapped\*](#not_mapped) |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | [Not mapped\*](#not_mapped) |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.77 `aria-readonly`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-readonly`](#aria-readonly)=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_READONLY` |
| UIA | Property: `Value.IsReadOnly`: `true`, if the element implements [`IValueProvider`](https://learn.microsoft.com/en-us/dotnet/api/system.windows.automation.provider.ivalueprovider).  Property: `RangeValue.IsReadOnly`: `true`, if the element implements [`IRangeValueProvider`](https://learn.microsoft.com/en-us/dotnet/api/system.windows.automation.provider.irangevalueprovider).  Property: `AriaProperties.readonly`: `true` |
| ATK/AT-SPI | State: `STATE_READ_ONLY`  State: `STATE_EDITABLE` not exposed on text input roles  State: `STATE_CHECKABLE` not exposed on roles supporting [`aria-checked`](#aria-checked "Broken local reference found in document.")  State: `STATE_CHECKABLE` not exposed on [radio](#radio) descendants when used on a `radiogroup` |
| AX API | Method: `AXUIElementIsAttributeSettable(AXValue)`: `NO` |
| Android | TBD |

##### 3.5.2.78 `aria-readonly`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-readonly`](#aria-readonly)=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_READONLY` not exposed  State: `IA2_STATE_EDITABLE` |
| UIA | Property: `Value.IsReadOnly`: `false`, if the element implements [`IValueProvider`](https://learn.microsoft.com/en-us/dotnet/api/system.windows.automation.provider.ivalueprovider).  Property: `RangeValue.IsReadOnly`: `false`, if the element implements [`IRangeValueProvider`](https://learn.microsoft.com/en-us/dotnet/api/system.windows.automation.provider.irangevalueprovider).  Property: `AriaProperties.readonly`: `false` |
| ATK/AT-SPI | State: `STATE_READ_ONLY` not exposed |
| AX API | Method: `AXUIElementIsAttributeSettable(AXValue)`: `YES` |
| Android | TBD |

##### 3.5.2.79 `aria-readonly` is unspecified on `gridcell`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-readonly`](#aria-readonly) is unspecified on `gridcell` |
| MSAA + IAccessible2 | The `gridcell` *MUST* inherit any author-provided value for `aria-readonly` from the containing `grid` or `treegrid`. Expose the inherited value on the `gridcell` as described for [`aria-readonly="true"`](#ariaReadonlyTrue) and [`aria-readonly="false"`](#ariaReadonlyFalse). |
| UIA | The `gridcell` *MUST* inherit any author-provided value for `aria-readonly` from the containing `grid` or `treegrid`. Expose the inherited value on the `gridcell` as described for [`aria-readonly="true"`](#ariaReadonlyTrue) and [`aria-readonly="false"`](#ariaReadonlyFalse). |
| ATK/AT-SPI | The `gridcell` *MUST* inherit any author-provided value for `aria-readonly` from the containing `grid` or `treegrid`. Expose the inherited value on the `gridcell` as described for [`aria-readonly="true"`](#ariaReadonlyTrue) and [`aria-readonly="false"`](#ariaReadonlyFalse). |
| AX API | The `gridcell` *MUST* inherit any author-provided value for `aria-readonly` from the containing `grid` or `treegrid`. Expose the inherited value on the `gridcell` as described for [`aria-readonly="true"`](#ariaReadonlyTrue) and [`aria-readonly="false"`](#ariaReadonlyFalse). |
| Android | TBD |

##### 3.5.2.80 `aria-relevant`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-relevant`](#aria-relevant) |
| MSAA + IAccessible2 | Object Attribute: `relevant:<value>`  Object Attribute: `container-relevant:<value>`  Object Attribute: `container-relevant:<value>` on all descendants  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| UIA | Property: `AriaProperties.relevant`: `<value>`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| ATK/AT-SPI | Object Attribute: `relevant:<value>`  Object Attribute: `container-relevant:<value>`  Object Attribute: `container-relevant:<value>` on all descendants  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| AX API | Property: `AXARIARelevant`: `<value>`  See also: [Changes to document content or node visibility](#mapping_events_visibility) |
| Android | TBD |

##### 3.5.2.81 `aria-required`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-required`](#aria-required)=`true` |
| MSAA + IAccessible2 | State: `IA2_STATE_REQUIRED` |
| UIA | Property: `IsRequiredForForm`: `true` |
| ATK/AT-SPI | State: `STATE_REQUIRED` |
| AX API | Property: `AXRequired`: `YES` |
| Android | TBD |

##### 3.5.2.82 `aria-required`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-required`](#aria-required)=`false` |
| MSAA + IAccessible2 | [Not mapped\*](#not_mapped) |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | [Not mapped\*](#not_mapped) |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.83 `aria-roledescription`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-roledescription`](#aria-roledescription) |
| MSAA + IAccessible2 | Method: `localizedExtendedRole()`: `<value>` |
| UIA | Localized Control Type: `<value>` |
| ATK/AT-SPI | Object Attribute: `roledescription:<value>` |
| AX API | Property: `AXRoleDescription`: `<value>` |
| Android | TBD |

##### 3.5.2.84 `aria-roledescription` is undefined or the empty string

|  |  |
| --- | --- |
| ARIA Specification | [`aria-roledescription`](#aria-roledescription) is undefined or the empty string |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | Localized Control Type is defined as that specified for the role of the element: based on the explicit role if the role attribute is provided; otherwise, based on the implicit role for the host language. |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | AXRoleDescription is defined as that specified for the role of the element: based on the explicit role if the role attribute is provided; otherwise, based on the implicit role for the host language. |
| Android | TBD |

##### 3.5.2.85 `aria-rowcount`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-rowcount`](#aria-rowcount) |
| MSAA + IAccessible2 | Object Attribute: `rowcount:<value>`  Method: `IAccessible2::groupPosition()`: `similarItemsInGroup=<value>` on rows |
| UIA | Property: `Grid.RowCount`: `<value>` |
| ATK/AT-SPI | Object Attribute: `rowcount` should contain the author-provided value.  Method: `atk_table_get_n_rows()` should return the actual number of rows. |
| AX API | Property: `AXARIARowCount`: `<value>` |
| Android | TBD |

##### 3.5.2.86 `aria-rowindex`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-rowindex`](#aria-rowindex) |
| MSAA + IAccessible2 | Object Attribute: `rowindex:<value>`  Method: `IAccessible2::groupPosition()`: `positionInGroup=<value>` on rows |
| UIA | Property: `GridItem.Row`: `<value>` (zero-based) |
| ATK/AT-SPI | Object Attribute: `rowindex` should contain the author-provided value.  Method: `atk_table_cell_get_position()` should return the actual (zero-based) row index. |
| AX API | Property: `AXARIARowIndex`: `<value>` |
| Android | TBD |

##### 3.5.2.87 `aria-rowindextext`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-rowindextext`](#aria-rowindextext) |
| MSAA + IAccessible2 | Object Attribute: `rowindextext:<value>` |
| UIA | Property: `AriaProperties.rowindextext`: `<value>` |
| ATK/AT-SPI | Object Attribute: `rowindextext:<value>` |
| AX API | Property: `AXRowIndexDescription`: `<value>` |
| Android | TBD |

##### 3.5.2.88 `aria-rowspan`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-rowspan`](#aria-rowspan) |
| MSAA + IAccessible2 | Object Attribute: `rowspan:<value>`  Method: `IAccessibleTableCell::rowExtent()`: `column=<value>` |
| UIA | Property: `GridItem.RowSpan`: `<value>` |
| ATK/AT-SPI | Object Attribute: `rowspan` should contain the author-provided value.  Method: `atk_table_cell_get_row_column_span()` should return the actual row span. |
| AX API | Property: `AXRowIndexRange.length`: `<value>` |
| Android | TBD |

##### 3.5.2.89 `aria-selected`=`true`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-selected`](#aria-selected "Broken local reference found in document.")=`true` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_SELECTABLE`  State: `STATE_SYSTEM_SELECTED`  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| UIA | Property: `SelectionItem.IsSelected`: `true` |
| ATK/AT-SPI | State: `STATE_SELECTABLE`  State: `STATE_SELECTED`  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| AX API | Property: `AXSelected`: `YES` |
| Android | TBD |

##### 3.5.2.90 `aria-selected`=`false`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-selected`](#aria-selected "Broken local reference found in document.")=`false` |
| MSAA + IAccessible2 | State: `STATE_SYSTEM_SELECTABLE`  State: `STATE_SYSTEM_SELECTED` not exposed  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| UIA | Property: `SelectionItem.IsSelected`: `false` |
| ATK/AT-SPI | State: `STATE_SELECTABLE`  State: `STATE_SELECTED` not exposed  See also: [Selection](#mapping_events_selection) for details on accessibility events |
| AX API | Property: `AXSelected`: `NO` |
| Android | TBD |

##### 3.5.2.91 `aria-selected` is undefined

|  |  |
| --- | --- |
| ARIA Specification | [`aria-selected`](#aria-selected "Broken local reference found in document.") is undefined |
| MSAA + IAccessible2 | [Not mapped](#not_mapped) |
| UIA | [Not mapped](#not_mapped) |
| ATK/AT-SPI | [Not mapped](#not_mapped) |
| AX API | [Not mapped](#not_mapped) |
| Android | TBD |

##### 3.5.2.92 `aria-setsize`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-setsize`](#aria-setsize) |
| MSAA + IAccessible2 | Object Attribute: `setsize:<value>`  See also: [Group Position](#mapping_additional_position) |
| UIA | Property: `AriaProperties.setsize`: `<value>`  See also: [Group Position](#mapping_additional_position) |
| ATK/AT-SPI | If the author-provided value of `aria-setsize` is `-1`, the exposed value should be based on the number of objects in the DOM. Object Attribute: `setsize:<value>`  State: `STATE_INDETERMINATE` if the author-provided value is `-1`  See also: [Group Position](#mapping_additional_position) |
| AX API | Property: `AXARIASetSize`: `<value>`  See also: [Group Position](#mapping_additional_position) |
| Android | TBD |

##### 3.5.2.93 `aria-sort`=`ascending`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-sort`](#aria-sort "Broken local reference found in document.")=`ascending` |
| MSAA + IAccessible2 | Object Attribute: `sort:ascending` |
| UIA | Property: `AriaProperties.sort`: `ascending`  Property: `ItemStatus`: `ascending` if the element maps to [`HeaderItem`](https://msdn.microsoft.com/en-us/library/windows/apps/ee671630.aspx) Control Type |
| ATK/AT-SPI | Object Attribute: `sort:ascending` |
| AX API | Property: `AXSortDirection`: `AXAscendingSortDirection` |
| Android | TBD |

##### 3.5.2.94 `aria-sort`=`descending`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-sort`](#aria-sort "Broken local reference found in document.")=`descending` |
| MSAA + IAccessible2 | Object Attribute: `sort:descending` |
| UIA | Property: `AriaProperties.sort`: `descending`  Property: `ItemStatus`: `descending` if the element maps to [`HeaderItem`](https://msdn.microsoft.com/en-us/library/windows/apps/ee671630.aspx) Control Type |
| ATK/AT-SPI | Object Attribute: `sort:descending` |
| AX API | Property: `AXSortDirection`: `AXDescendingSortDirection` |
| Android | TBD |

##### 3.5.2.95 `aria-sort`=`other`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-sort`](#aria-sort "Broken local reference found in document.")=`other` |
| MSAA + IAccessible2 | Object Attribute: `sort:other` |
| UIA | Property: `AriaProperties.sort`: `other`  Property: `ItemStatus`: `other` if the element maps to [`HeaderItem`](https://msdn.microsoft.com/en-us/library/windows/apps/ee671630.aspx) Control Type |
| ATK/AT-SPI | Object Attribute: `sort:other` |
| AX API | Property: `AXSortDirection`: `AXUnknownSortDirection` |
| Android | TBD |

##### 3.5.2.96 `aria-sort`=`none`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-sort`](#aria-sort "Broken local reference found in document.")=`none` |
| MSAA + IAccessible2 | Object Attribute: `sort:none`, if the value is not unspecified |
| UIA | [Not mapped\*](#not_mapped) |
| ATK/AT-SPI | Object Attribute: `sort:none`, if the value is not unspecified |
| AX API | [Not mapped\*](#not_mapped) |
| Android | TBD |

##### 3.5.2.97 `aria-valuemax`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-valuemax`](#aria-valuemax) |
| MSAA + IAccessible2 | Method: `IAccessibleValue::maximumValue()`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| UIA | Property: `RangeValue.Maximum`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| ATK/AT-SPI | Method: `atk_value_get_maximum_value()`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| AX API | Property: `AXMaxValue`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| Android | TBD |

##### 3.5.2.98 `aria-valuemin`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-valuemin`](#aria-valuemin) |
| MSAA + IAccessible2 | Method: `IAccessibleValue::minimumValue()`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| UIA | Property: `RangeValue.Minimum`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| ATK/AT-SPI | Method: `atk_value_get_minimum_value()`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| AX API | Property: `AXMinValue`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| Android | TBD |

##### 3.5.2.99 `aria-valuenow`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-valuenow`](#aria-valuenow) |
| MSAA + IAccessible2 | Method: `IAccessibleValue::currentValue()`: `<value>`  Method: `IAccessible::get_accValue()`: `<value>` if `aria-valuetext` is not defined  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| UIA | Property: `RangeValue.Value`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| ATK/AT-SPI | Method: `atk_value_get_current_value()`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| AX API | Property: `AXValue`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| Android | TBD |

##### 3.5.2.100 `aria-valuetext`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-valuetext`](#aria-valuetext) |
| MSAA + IAccessible2 | Method: `IAccessible::get_accValue()`: `<value>`  Object Attribute: `valuetext:<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| UIA | Property: `Value.Value`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| ATK/AT-SPI | Object Attribute: `valuetext:<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| AX API | Property: `AXValueDescription`: `<value>`  See also: [Handling Author Errors for States and Properties](#document-handling_author-errors_states-properties "Broken local reference found in document.") |
| Android | TBD |

### 3.6 Special Processing Requiring Additional Computation

#### 3.6.1 Name and Description

For information on how to compute an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) or
[accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description), see the section titled
[Accessible Name and Description Computation](#mapping_additional_nd_te "Broken local reference found in document.") of the
Accessible Name and Description Computation specification.

#### 3.6.2 Relations

Often in a GUI, there are [relationships](https://www.w3.org/TR/wai-aria/#dfn-relationship) between the [widgets](https://www.w3.org/TR/wai-aria/#dfn-widget) that can be exposed programmatically
to [assistive technology](https://www.w3.org/TR/wai-aria/#assistive-technology). WAI-ARIA provides several relationship [properties](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.") which are globally
applicable to any [element](https://dom.spec.whatwg.org/#concept-element): [`aria-controls`](#aria-controls), [`aria-describedby`](#aria-describedby), [`aria-flowto`](#aria-flowto), [`aria-labelledby`](#aria-labelledby), [`aria-owns`](#aria-owns), [`aria-posinset`](#aria-posinset), and [`aria-setsize`](#aria-setsize). Therefore, it is not important to check the [role](https://www.w3.org/TR/wai-aria/#dfn-role) before computing them. [User agents](https://infra.spec.whatwg.org/#user-agent) can simply map these relations to
[accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) as defined in the section titled [State and Property Mapping](#mapping_state-property).

##### 3.6.2.1 Reverse Relations

A reverse relation exists when an element's ID is referenced by a [property](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.") in another [element](https://dom.spec.whatwg.org/#concept-element). For
APIs that support reverse relations, [user agents](https://infra.spec.whatwg.org/#user-agent) *MUST* use the mapping defined in the
[State and Property Mapping Tables](#mapping_state-property_table) when an element's ID is referenced by a relation property of another element and the referenced element is
in the accessibility tree. All WAI-ARIA references must point to an element that is exposed as an accessible object in the accessibility tree. When the referenced object is not exposed
in the accessibility tree (e.g. because it is [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden "Normative reference to non-normative term.")), the reference is null. `aria-labelledby` and `aria-describedby` have an additional feature, which
allows them to pull a flattened string from the referenced element to populate the name or description fields of the accessibility API. This feature is described in the
[Name and Description](#mapping_additional_nd) section.

Special case: If both [`aria-labelledby`](#aria-labelledby) and HTML
`<label for= … >` are used, the user agent *MUST* use the WAI-ARIA relation and *MUST* ignore the
HTML label relation.

Note that [`aria-describedby`](#aria-describedby) may reference structured or interactive information where users would want to be able
to navigate to different sections of content. User agents *MAY* provide a way for the user to navigate to structured information referenced by
[`aria-describedby`](#aria-describedby) and [assistive technology](https://www.w3.org/TR/wai-aria/#assistive-technology) *SHOULD* provide such a method.

##### 3.6.2.2 Implied reverse relations

In addition to the explicit relations defined by WAI-ARIA [properties](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term."), reverse relations are implied in two other
situations: [elements](https://dom.spec.whatwg.org/#concept-element) with `role="treeitem"` where the ancestor does not have an
[`aria-owns`](#aria-owns) property and descendants of elements with
[`aria-atomic`](#aria-atomic "Broken local reference found in document.") property.

In the case of `role="treeitem"`, when [`aria-owns`](#aria-owns) is
not used, [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* do the following where reverse relations are supported by the API:

- If the current [`treeitem`](#treeitem) uses [`aria-level`](#aria-level "Broken local reference found in document."), then walk backwards in the tree until a [`treeitem`](#treeitem) is found with a lower
  [`aria-level`](#aria-level "Broken local reference found in document."), then set `RELATION_NODE_CHILD_OF` to that element. If the top of the tree is reached, then set `RELATION_NODE_CHILD_OF` to the tree element itself.
- If the parent of the [`treeitem`](#treeitem) has a [role](https://www.w3.org/TR/wai-aria/#dfn-role) of
  [`group`](#group), then walk backwards from the [`group`](#group) until an element with a role of
  [`treeitem`](#treeitem) is found, then set `RELATION_NODE_CHILD_OF` to that element.

In the case of [`aria-atomic`](#aria-atomic "Broken local reference found in document."), where reverse relations are supported by the API:

- User agents *SHOULD* check the chain of ancestor elements for [`aria-atomic`](#aria-atomic "Broken local reference found in document.")`="true"`. If found, user agents *SHOULD* set the `RELATION_MEMBER_OF` relation to point to the ancestor that sets
  [`aria-atomic`](#aria-atomic "Broken local reference found in document.")`="true"`.

#### 3.6.3 Group Position

[`aria-level`](#aria-level "Broken local reference found in document."), [`aria-posinset`](#aria-posinset), and [`aria-setsize`](#aria-setsize) are all 1-based. When the [property](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.") is not present or is "0", it indicates the
property is not computed or not supported. If any of these properties are specified by the author as either "0" or a negative number, [user agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* use "1"
instead.

If [`aria-level`](#aria-level "Broken local reference found in document.") is not provided or inherited for an element of [role](https://www.w3.org/TR/wai-aria/#dfn-role)
[`treeitem`](#treeitem) or [`comment`](#comment), user agents implementing IAccessible2 or ATK/AT-SPI *MUST* compute it by
following the explicit or computed `RELATION_NODE_CHILD_OF` relations.

If [`aria-posinset`](#aria-posinset) and [`aria-setsize`](#aria-setsize) are not provided,
user agents *MUST* compute them as follows:

- for `role="treeitem"` and `role="comment"`, walk
  the tree backward and forward until the explicit or computed level becomes less than the current item's level. Count items only if they are at the same level as the current item.
- Otherwise, if the role supports [`aria-posinset`](#aria-posinset) and
  [`aria-setsize`](#aria-setsize), process the parent (DOM parent or parent defined by [`aria-owns`](#aria-owns)), counting items that have the same role.
- Because these value are 1-based, include the current item in the computation. For [`aria-posinset`](#aria-posinset), include the current item and other group items if they are before the current item in the DOM. For [`aria-setsize`](#aria-setsize), add to that the number of items in the same group after the current item in the DOM.

If the author provides one or more of `aria-setsize` and `aria-posinset`, it is the author's responsibility to supply them for all elements in the set. [User agent](https://infra.spec.whatwg.org/#user-agent)
correction of missing values in this case is not defined.

MSAA/IAccessible2 API mappings involve an additional function, `groupPosition()` [[IAccessible2](#bib-iaccessible2 "IAccessible2")], when
[`aria-level`](#aria-level "Broken local reference found in document."), [`aria-posinset`](#aria-posinset), and/or [`aria-setsize`](#aria-setsize) are present on an element, or are computed by the user agent. When this occurs:

- [`aria-level`](#aria-level "Broken local reference found in document.") is exposed in the `groupLevel` parameter of `groupPosition()`,
- [`aria-setsize`](#aria-setsize) is exposed in the `similarItemsInGroup` parameter, and
- [`aria-posinset`](#aria-posinset) is exposed in the `positionInGroup` parameter.

### 3.7 Actions

As part of mapping roles to accessible objects as defined in [Role Mapping](#mapping_role), users agents expose a default action on the object.

- MSAA: If an AT calls `DoDefaultAction` on an accessible object, the user agent *SHOULD* simulate a click on the
  DOM element which is mapped to that accessible object.
- IAccessible2: If an AT calls the `IAccessibleAction` on an accessible object, the user agent *SHOULD* simulate a click on the
  DOM element which is mapped to that accessible object.
- UIA Automation: If an AT calls any UIA pattern method on an accessible object, the user agent
  *SHOULD* simulate a click on the DOM element which is mapped to that accessible object.
- ATK/AT-SPI: If an AT calls an
  action on an accessible object, the user agent *SHOULD* simulate a click on the DOM element which is mapped to that accessible object.
- AX API: If an AT triggers an `AXPress` action on an accessible object, the user agent
  *SHOULD* simulate a click on the DOM element which is mapped to that accessible object.

Note

Authors will need to create handlers for those click events that update WAI-ARIA states and properties in the
DOM accordingly, so that those updated states can be populated by the user agent in the Accessibility
API.

### 3.8 Events

[User agents](https://infra.spec.whatwg.org/#user-agent) fire [events](https://dom.spec.whatwg.org/#concept-event) for user actions, WAI-ARIA [state](https://www.w3.org/TR/wai-aria/#dfn-state) changes, changes to
document content or node visibility, changes in selection and operation of menus as defined in the following sections.

#### 3.8.1 State and Property Change Events

[User agents](https://infra.spec.whatwg.org/#user-agent) *MUST* notify [assistive technology](https://www.w3.org/TR/wai-aria/#assistive-technology) of [state](https://www.w3.org/TR/wai-aria/#dfn-state) changes as defined in the table below, *SHOULD* notify assistive technology of
[property](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term.") changes if the [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) defines a change [event](https://dom.spec.whatwg.org/#concept-event) for the property, and *SHOULD NOT* notify assistive technology of
property changes if the accessibility API does not define a change event for the property. For example, IAccessible2 defines an event
to be used when [`aria-activedescendant`](#aria-activedescendant) changes.
WAI-ARIA properties that are expected to change include
[`aria-activedescendant`](#aria-activedescendant), [`aria-valuenow`](#aria-valuenow), and [`aria-valuetext`](#aria-valuetext).

Note

In some APIs, AT will only be notified of events to which it has subscribed.

For simplicity and performance the user agent *MAY* trim out change events for state or property changes that [assistive technologies](https://www.w3.org/TR/wai-aria/#assistive-technology) typically ignore, such as events
that are happening in a window that does not currently have focus.

Note

Translators: For label text associated with the following table and its toggle buttons, see the `mappingTableLabels` object in the `<head>` section of this
document.

##### 3.8.1.1 `aria-activedescendant`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-activedescendant`](#aria-activedescendant) |
| MSAA + IAccessible2 event | See [Focus Changes](#focus_state_event_table). In addition:  `IA2_EVENT_ACTIVE_DESCENDANT_CHANGED` |
| UIA event | See [Focus Changes](#focus_state_event_table). In addition:  `PropertyChangedEvent`  Property: `AriaProperties` |
| ATK/AT-SPI event | See [Focus Changes](#focus_state_event_table). |
| AX API Notification | See [Focus Changes](#focus_state_event_table). In addition: `AXSelectedChildrenChanged` |
| Android | TBD |

##### 3.8.1.2 `aria-busy` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-busy`](#aria-busy "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Property: `AriaProperties` |
| ATK/AT-SPI event | `object:state-changed:busy` |
| AX API Notification | `AXElementBusyChanged` |
| Android | TBD |

##### 3.8.1.3 `aria-checked` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-checked`](#aria-checked "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, `ToggleState` as part of `toggle` pattern |
| ATK/AT-SPI event | `object:state-changed:checked` |
| AX API Notification | `AXValueChanged` |
| Android | TBD |

##### 3.8.1.4 `aria-current` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-current`](#aria-current "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `IA2_EVENT_OBJECT_ATTRIBUTE_CHANGED` |
| UIA event | `PropertyChangedEvent` Property: `AriaProperties` |
| ATK/AT-SPI event | `object:state-changed:active` |
| AX API Notification | `AXCurrentStateChanged` |
| Android | TBD |

##### 3.8.1.5 `aria-disabled` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-disabled`](#aria-disabled "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, `IsEnabled` |
| ATK/AT-SPI event | `object:state-changed:enabled` and `object:state-changed:sensitive` |
| AX API Notification | `AXDisabledStateChanged` |
| Android | TBD |

##### 3.8.1.6 `aria-describedby`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-describedby`](#aria-describedby) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_DESCRIPTIONCHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `DescribedBy` |
| ATK/AT-SPI event | `object:property-change:accessible-description` |
| AX API Notification | `AXDescribedByChanged` |
| Android | TBD |

##### 3.8.1.7 `aria-dropeffect` (property, deprecated)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-dropeffect`](#aria-dropeffect "Broken local reference found in document.") (property, deprecated) |
| MSAA + IAccessible2 event | `IA2_EVENT_OBJECT_ATTRIBUTE_CHANGED` |
| UIA event | `PropertyChangedEvent` Property: `AriaProperties` |
| ATK/AT-SPI event | `object:property-change` |
| AX API Notification | `AXDropEffectChanged` |
| Android | TBD |

##### 3.8.1.8 `aria-expanded` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-expanded`](#aria-expanded "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, `ExpandCollapseState` as part of the `ExpandCollapse` pattern |
| ATK/AT-SPI event | `object:state-changed:expanded` |
| AX API Notification | `AXRowExpanded`,  `AXRowCollapsed`,  `AXRowCountChanged` |
| Android | TBD |

##### 3.8.1.9 `aria-grabbed` (state, deprecated)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-grabbed`](#aria-grabbed "Broken local reference found in document.") (state, deprecated) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_SELECTION`  `IA2_EVENT_OBJECT_ATTRIBUTE_CHANGED` |
| UIA event | `PropertyChangedEvent` Property: `AriaProperties` |
| ATK/AT-SPI event | `object:property-change` |
| AX API Notification | `AXGrabbedStateChanged` |
| Android | TBD |

##### 3.8.1.10 `aria-hidden` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-hidden`](#aria-hidden "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `IA2_EVENT_OBJECT_ATTRIBUTE_CHANGED` |
| UIA event | `StructureChangedEvent` `PropertyChangedEvent`  Property: `AriaProperties` |
| ATK/AT-SPI event | `object:property-change` |
| AX API Notification | `AXUIElementDestroyed`,  `AXUIElementCreated` |
| Android | TBD |

##### 3.8.1.11 `aria-invalid` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-invalid`](#aria-invalid "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, `IsDataValidForForm` |
| ATK/AT-SPI event | `object:state-changed:invalid_entry` |
| AX API Notification | `AXInvalidStatusChanged` |
| Android | TBD |

##### 3.8.1.12 `aria-label` and `aria-labelledby`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-label`](#aria-label) and [`aria-labelledby`](#aria-labelledby) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_NAMECHANGE` |
| UIA event | `PropertyChangedEvent` Property for `aria-label`: `AriaProperties`  Property for `aria-labelledby`: `LabeledBy` |
| ATK/AT-SPI event | `object:property-change:accessible-name` |
| AX API Notification | `AXLabelCreated` |
| Android | TBD |

##### 3.8.1.13 `aria-pressed` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-pressed`](#aria-pressed "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, `ToggleState` as part of `toggle` pattern |
| ATK/AT-SPI event | `object:state-changed:pressed` |
| AX API Notification | `AXPressedStateChanged` |
| Android | TBD |

##### 3.8.1.14 `aria-readonly`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-readonly`](#aria-readonly) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Property: `AriaProperties` |
| ATK/AT-SPI event | `object:state-changed:readonly` |
| AX API Notification | `AXReadOnlyStatusChanged` |
| Android | TBD |

##### 3.8.1.15 `aria-required`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-required`](#aria-required) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_STATECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, `IsRequiredForForm` |
| ATK/AT-SPI event | `object:state-changed:required` |
| AX API Notification | `AXRequiredStatusChanged` |
| Android | TBD |

##### 3.8.1.16 `aria-selected` (state)

|  |  |
| --- | --- |
| ARIA Specification | [`aria-selected`](#aria-selected "Broken local reference found in document.") (state) |
| MSAA + IAccessible2 event | See section [Selection](#mapping_events_selection) for details. |
| UIA event | See section [Selection](#mapping_events_selection) for details. |
| ATK/AT-SPI event | See section [Selection](#mapping_events_selection) for details. |
| AX API Notification | See section [Selection](#mapping_events_selection) for details. |
| Android | TBD |

##### 3.8.1.17 `aria-valuenow`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-valuenow`](#aria-valuenow) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_VALUECHANGE` |
| UIA event | `PropertyChangedEvent` Properties: `AriaProperties`, also `RangeValueValue` if element is mapped with `RangeValue` Control Pattern |
| ATK/AT-SPI event | `object:property-change:accessible-value` |
| AX API Notification | `AXValueChanged` |
| Android | TBD |

##### 3.8.1.18 `aria-valuetext`

|  |  |
| --- | --- |
| ARIA Specification | [`aria-valuetext`](#aria-valuetext) |
| MSAA + IAccessible2 event | `EVENT_OBJECT_VALUECHANGE` |
| UIA event | `PropertyChangedEvent` Property: `AriaProperties` |
| ATK/AT-SPI event | `object:property-change:accessible-value` |
| AX API Notification | `AXValueChanged` |
| Android | TBD |

#### 3.8.2 Changes to document content or node visibility

Processing document changes is important regardless of WAI-ARIA. The events described in the table below are used by user agents
to inform AT of changes to the DOM via the accessibility tree. For the purposes of conformance with
this standard, [user agents](https://infra.spec.whatwg.org/#user-agent) *MUST* implement the behavior described in this section whenever WAI-ARIA attributes are applied to
dynamic content on a Web page.

Table of document change scenarios and events to be fired in each
API

| Scenario | MSAA + IAccessible2 event | UIA event | ATK/AT-SPI event | AX API Notification |
| --- | --- | --- | --- | --- |
| When text is removed | `IA2_EVENT_TEXT_REMOVED` | `EVENT_OBJECT_LIVEREGIONCHANGED` | `text_changed::delete` | If in a [live region](https://www.w3.org/TR/wai-aria/#dfn-live-region), `AXLiveRegionChanged`. If in `aria-errormessage`, `AXValidationErrorChanged`. |
| When text is inserted | `IA2_EVENT_TEXT_INSERTED` | `EVENT_OBJECT_LIVEREGIONCHANGED` | `text_changed::insert` | If in a [live region](https://www.w3.org/TR/wai-aria/#dfn-live-region), `AXLiveRegionChanged`. If in `aria-errormessage`, `AXValidationErrorChanged`. |
| When text is changed | `IA2_EVENT_TEXT_REMOVE` and `IA2_EVENT_TEXT_INSERTED` | `EVENT_OBJECT_LIVEREGIONCHANGED` | `text_changed::delete` and `text_changed::insert` | If in a [live region](https://www.w3.org/TR/wai-aria/#dfn-live-region), `AXLiveRegionChanged`. If in `aria-errormessage`, `AXValidationErrorChanged`. |

Fire the following events for node changes where the node in question is an element and has an [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object). The
accessibility subtree of a node is its [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) and all of it's
[accessibility descendants](https://www.w3.org/TR/wai-aria/#dfn-accessibility-descendant). It does not include objects which have relationships other than parent-child in that tree. For example, it does not include objects linked via
[aria-flowto](#aria-flowto) unless those objects are also descendants in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree).

Table of document change scenarios and events to be fired in each
API

| Scenario | MSAA | Microsoft UIA event | ATK/AT-SPI event | AX API Notification |
| --- | --- | --- | --- | --- |
| When an [accessibility subtree](#dfn-accessibility-subtree) is [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden "Normative reference to non-normative term.") | `EVENT_OBJECT_HIDE`  The MSAA event called `EVENT_OBJECT_DESTROY` is not used because this has a history of stability issues and assistive technology avoids it. In any case, from the user's point of view, there is no difference between something that is hidden or destroyed. | `AutomationElement..::.StructureChangedEvent` | `children_changed::remove` | `AXUIElementDestroyed`  If in a live region, `AXLiveRegionChanged` |
| When an accessibility subtree is removed | `EVENT_OBJECT_REORDER`  The MSAA event called `EVENT_OBJECT_DESTROY` is not used because this has a history of stability issues and assistive technology avoids it. In any case, from the user's point of view, there is no difference between something that is hidden or destroyed. | `AutomationElement..::.StructureChangedEvent` | `children_changed::remove` | `AXUIElementDestroyed`  If in a live region, `AXLiveRegionChanged` |
| When an accessibility subtree is shown | `EVENT_OBJECT_SHOW` |  | `children_changed::add` | `AXUIElementCreated`  If in a live region, `AXLiveRegionChanged` |
| When an accessibility subtree is inserted | `EVENT_OBJECT_REORDER` |  | `children_changed::add` | `AXUIElementCreated`  If in a live region, `AXLiveRegionChanged` |
| When an accessibility subtree is moved | Treat it as a removal from one place and insertion in another | Treat it as a removal from one place and insertion in another | Treat it as a removal from one place and insertion in another | `AXUIElementDestroyed`/ `AXUIElementCreated`  If in a live region, `AXLiveRegionChanged` |
| When an accessibility subtree is changed (e.g. replaceNode) | Treat it as a removal and insertion | Treat it as a removal and insertion | Treat it as a removal and insertion | `AXUIElementDestroyed`/ `AXUIElementCreated`  If in a live region, `AXLiveRegionChanged` |

In some cases, node changes may occur where the node is not an element or has no accessible object. For example, a numbered list bullet ("12.") may have a node in the accessibility tree
but not in the DOM tree. For text within a paragraph marked in HTML as
`<strong>`, the `<strong>` element has a node in the DOM tree but may not have one in the accessibility tree.
The text itself will of course be in the accessibility tree along with the identification of the range of text that is formatted as strong. If any of the changes described in the table
above occur on such a node, user agents *SHOULD* compute and fire relevant text change events as described above.

User agents *SHOULD* ensure that an assistive technology, running in process can receive notification of a node being removed prior to removal. This allows an assistive technology, such as a
screen reader, to refer back to the corresponding DOM node being deleted. This is important for [live regions](https://www.w3.org/TR/wai-aria/#dfn-live-region) where
removals are important. For example, a screen reader would want to notify a user that another user has left a chat room. The event in
MSAA would be `EVENT_OBJECT_HIDE`. For ATK/AT-SPI
this would be `children_changed::remove`. And in macOS, the event is `AXLiveRegionChanged`. This also requires the user agent to provide a unique ID in the
[accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) notification identifying the unique node being removed.

When firing any of the above-mentioned change events, it is very useful to provide information about whether the change was caused by user input (as opposed to a timeout initiated from the
page load, etc.). This allows the assistive technology to have different rules for presenting changes from the real world as opposed to from user action. Mouse hovers are not considered
explicit user input because they can occur from accidental bumps of the mouse.

To expose whether a change occurred from user input:

- In ATK/AT-SPI this can be provided by appending the string
  ":system" to the event name when the user did not cause the change.
- In IAccessible2, which screen readers typically access in process on the same thread, the best practice is to expose the object attribute `event-from-user-input:true` on the
  accessible object for the event, if the user caused the change.

Exposing additional useful information about the context of the change:

- In ATK/AT-SPI and IAccessible2, the
  `RELATION_MEMBER_OF` relation on the accessible event's target accessible object *SHOULD* point to any ancestor with
  [`aria-atomic`](#aria-atomic "Broken local reference found in document.")`="true"` (if any).
- In ATK/AT-SPI and IAccessible2, the `container-live`,
  `container-relevant`, `container-busy`, `container-atomic` object attributes *SHOULD* be exposed on the accessible event object, providing the computed
  value for the related WAI-ARIA properties. The computed value is the value of the closest ancestor. It is recommended to not
  expose the object attribute if the default value is used.

Additional MSAA events may be necessary:

- If something changes in an ancestor with a mapped MSAA role of `ROLE_SYSTEM_ALERT`, then an
  `EVENT_SYSTEM_ALERT` event *SHOULD* be fired for the alert. The alert role has an implied value of "assertive" for the
  [`aria-live`](#aria-live "Broken local reference found in document.") property.
- Menu events may need to be fired. See [Special Events for Menus](#mapping_events_menus).

#### 3.8.3 Focus Changes

The following table defines the accessibility API keyboard focus states and events.

Table of
[accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api)
for focus states and
[events](https://dom.spec.whatwg.org/#concept-event)

|  | MSAA | Microsoft UIA | ATK/AT-SPI | AX API |
| --- | --- | --- | --- | --- |
| Focusable state | `STATE_SYSTEM_FOCUSABLE` | Current state reflected in `IUIAutomationElement::CurrentIsKeyboardFocusable`, can be retrieved with `IUIAutomationElement::GetCurrentPropertyValue` method using `UIA_IsKeyboardFocusablePropertyId` property identifier. | `STATE_FOCUSABLE` | `boolean AXFocused`: the `AXUIElementIsAttributeSettable` method returns `YES`. |
| Focused state | `STATE_SYSTEM_FOCUSED` | Current state reflected in `IUIAutomationElement::CurrentHasKeyboardFocus`, can be retrieved with `IUIAutomationElement::GetCurrentPropertyValue` method using `UIA_HasKeyboardFocusPropertyId` property identifier. | `STATE_FOCUSED` | `boolean AXFocused` |
| Focus event | `EVENT_OBJECT_FOCUS` | Clients can subscribe with `IUIAutomation::AddFocusChangedEventHandler` using callback interface is `IUIAutomationFocusChangedEventHandler` | `object:state-changed:focused` and:  - `detail1 = 1` for the [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) which just gained focus. - `detail1 = 0` for the [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) which just lost focus. | `AXFocusedUIElementChanged` |

#### 3.8.4 Selection

There are two cases for selection:

- Single selection
- Multiple selection

In the single selection case, selection follows focus (see the section "[Focus States and Events Table](#focus_state_event_table)" for information about focus events). User
agents *MUST* fire the following events when [`aria-selected`](#aria-selected "Broken local reference found in document.") changes:

Single selection events

| Scenario | MSAA | Microsoft UIA | ATK/AT-SPI | AX API |
| --- | --- | --- | --- | --- |
| Focus change | `EVENT_OBJECT_SELECTION` and `EVENT_OBJECT_STATECHANGE` on newly focused item. | `UIA_SelectionItem_ElementSelectedEventId` on the newly focused element. If on a `gridcell`, `row`, `option`, or `tab`, fire `UIA_SelectionItem_ElementSelectedEventId`. | - `object:selection-changed` on the current container, - `object:state-changed:selected` on the descendant [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) whose selection has changed:   - `detail1 = 1` for the descendant which just became selected.   - `detail1 = 0` for the descendant which just became unselected. | `AXSelectedChildrenChanged` |

The multiple selection case occurs when [`aria-multiselectable`](#aria-multiselectable "Broken local reference found in document.")`="true"` on an [element](https://dom.spec.whatwg.org/#concept-element) with a [role](https://www.w3.org/TR/wai-aria/#dfn-role) that supports that [property](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term."). User agents *MUST* fire the following events
when [`aria-selected`](#aria-selected "Broken local reference found in document.") changes on a descendant, as follows:

The multiple selection case occurs when [`aria-multiselectable`](#aria-multiselectable "Broken local reference found in document.")`="true"` on an [element](https://dom.spec.whatwg.org/#concept-element) with a [role](https://www.w3.org/TR/wai-aria/#dfn-role) that supports that [property](https://www.w3.org/TR/wai-aria/#dfn-property "Normative reference to non-normative term."). There are several important aspects:

1. In Microsoft UIA, the `Selection` and `SelectionItem` Control Patterns expose the selection availability, state, and
   methods.
2. User agents *MUST* fire the following events when [`aria-selected`](#aria-selected "Broken local reference found in document.") changes on a descendant, as follows:

Multiple selection events

| Scenario | MSAA | Microsoft UIA | ATK/AT-SPI | AX API |
| --- | --- | --- | --- | --- |
| Toggle [`aria-selected`](#aria-selected "Broken local reference found in document.") | `EVENT_OBJECT_SELECTIONADD`/`EVENT_OBJECT_SELECTIONREMOVE` on the item. | `SelectionItem Control Pattern`:`UIA_SelectionItem_ElementAddedToSelectionEventId` or `UIA_SelectionItem_ElementRemovedFromSelectionEventId` on the item. | - `object:selection-changed` on the current container, - `object:state-changed:selected` on any descendant [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) whose selection has changed:   - `detail1 = 1` for any descendant which just became selected.   - `detail1 = 0` for any descendant which just became unselected. | `AXSelectedChildrenChanged` |
| Selection follows focus | `EVENT_OBJECT_SELECTION` and `EVENT_OBJECT_STATECHANGE` on newly focused item. | `FocusChangedEvent` should be fired but individual selection event may not happen, to avoid redundancy. | - `object:selection-changed` on the current container, - `object:state-changed:selected` on any descendant [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) whose selection has changed:   - `detail1 = 1` for any [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) which just became selected.   - `detail1 = 0` for any [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) which just became unselected. | `AXSelectedChildrenChanged` |
| Select or deselect many items at once | User agent *MAY* fire an `EVENT_OBJECT_SELECTIONWITHIN`. If this event is fired the other events noted above *MAY* be trimmed out for performance. | For each element selected or deselected, fire `SelectionItem` Control Pattern: `UIA_SelectionItem_ElementAddedToSelectionEventId` or `UIA_SelectionItem_ElementRemovedFromSelectionEventId` on the current container. User agents *MAY* choose to fire the Selection Control Pattern Invalidated event, which indicates that the selection in a container has changed significantly and requires sending more addition and removal events than the `InvalidateLimit` constant permits. | - the user agent *MAY* fire a single `object:selection-changed` event on the container, vs. multiple events, for performance, - `object:state-changed:selected` on any descendant [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) whose selection has changed:   - `detail1 = 1` for any [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) which just became selected.   - `detail1 = 0` for any [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) which just became unselected. | `AXSelectedChildrenChanged` |

#### 3.8.5 Special Events for Menus

Some APIs, provide special [events](https://dom.spec.whatwg.org/#concept-event) whenever a menu is opened or closed. [User agents](https://infra.spec.whatwg.org/#user-agent) *SHOULD* provide the
events as described in the table below. If provided, because menus can be made visible or [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden "Normative reference to non-normative term.") using a variety of techniques, a [user agent](https://infra.spec.whatwg.org/#user-agent) *MUST* ensure that the events are
nested and symmetrical.

Frequently, a [`menubar`](#menubar) is used to organize a hierarchy of menus. In those cases, the menubar *MUST* be a
DOM parent of the associated [`menuitem`](#menuitem)s, or one defined by [`aria-owns`](#aria-owns). In other cases, no menubar is involved; for example, when the [`menu`](#menu) is associated with a toolbar button, or is a context menu.
Nonetheless the relevant menu events are provided as described in the following table.

Menu events

| Scenario | MSAA | Microsoft UIA | AX API |
| --- | --- | --- | --- |
| Menubar is currently not active, and user moves focus to the menubar from elsewhere thereby activating it. As a result, a menuitem in the menubar is focused. | Activate the menubar and fire `EVENT_SYSTEM_MENUSTART` on the accessible object for the menubar. | `MenuModeStartEvent` on the accessible object for the menu. | `AXMenuOpenedNotification` |
| Focus a menuitem while menubar is activated, or focus a menuitem in a menu. | `EVENT_OBJECT_FOCUS` | `AutomationFocusChangedEvent` | `AXMenuItemSelectedNotification` |
| Menu popup made visible (menu is opened).  Should only be fired once until the menu is closed and opened again. | `EVENT_SYSTEM_MENUPOPUPSTART` | `MenuOpenedEvent`, then a `focus` event on a menuitem. | `AXMenuOpenedNotification` |
| Menu popup hidden (menu is closed). | `EVENT_SYSTEM_MENUPOPUPEND` once only for accessible menu object and only if `EVENT_SYSTEM_MENUPOPUPSTART` was fired for it. | `MenuClosedEvent` | `AXMenuClosedNotification` |
| Any open menus are closed including sub-menus, and user moves focus away from the menubar; menubar is deactivated. | `EVENT_SYSTEM_MENUEND` on the menubar and deactivate the menubar. | `MenuClosedEvent`, then `MenuModeEndEvent` | `AXMenuClosedNotification` |

## 4. Algorithms

Some APIs provide methods which require specific algorithms to be followed. The following sections provide the algorithm mapping tables
for these methods.

### 4.1 ARIANotifyMixin Algorithm Mapping Tables

The `ARIANotifyMixin` provides a method for announcing content to assistive technologies. The following algorithm mappings specify how these announcements will be implemented across
different accessibility APIs to ensure consistent behavior for users of assistive technologies.

#### 4.1.1 ariaNotify

To `aria notify` given node, announcement, and priority:

|  |  |
| --- | --- |
| ARIA Specification | [`aria notify`](#arianotify) |
| Preconditions | If node is [excluded from the accessibility tree](#tree_exclusion "Broken local reference found in document."), then abort these steps. |
| Language | User agents and assistive technologies *MUST* determine the language of the announcement by taking the first valid BCP 47 language tag from the following sources:   1. The node's nearest ancestor element's `lang` attribute (including    node    itself). 2. The document element's `lang` attribute (including when called on the document). 3. A user agent or platform default.   Assistive technologies *MUST* present the announcement using that language (for example, voice, pronunciation rules, braille table). |
| MSAA + IAccessible2 | No implementation specified ([see fallback note](#arianotify-fallback-note)). |
| UIA | 1. Let mapped\_priority be `NotificationProcessing_ImportantAll` if priority is "high", otherwise `NotificationProcessing_All`. 2. Call `UiaRaiseNotificationEvent` with node, `NotificationKind_ActionCompleted`, mapped\_priority, announcement, and the empty    string.   Note  If the platform accessibility implementation determines that node is not represented in the UIA [Control view](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-treeoverview#control-view) or [Content view](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-treeoverview#content-view), user agents *SHOULD* instead raise the notification event on the nearest ancestor that is represented as a UIA Control. If no such ancestor exists, user agents *SHOULD* raise it on the document root (which is expected to be in one of these views) to ensure assistive technologies that ignore events on elements not in the Control or Content view receive the notification. |
| ATK | 1. Let mapped\_priority be `Atk.Live.ATK_LIVE_ASSERTIVE` if priority is "high", otherwise `Atk.Live.ATK_LIVE_POLITE`. 2. Call `g_signal_emit_by_name` with node, `"notification"`, announcement, and mapped\_priority.   On older Linux accessibility stacks prior to ATK 2.50.0, user agents *MAY* use the fallback; [see fallback note](#arianotify-fallback-note). |
| AT-SPI | 1. Let mapped\_priority be `ATSPI_LIVE_ASSERTIVE` if priority is "high", otherwise `ATSPI_LIVE_POLITE`. 2. Send a DBUS signal `ATSPI_DBUS_INTERFACE_EVENT_OBJECT` with node, `"announcement"`, announcement, and mapped\_priority. |
| AX API | 1. Let mapped\_priority be `NSAccessibilityPriorityHigh` if priority is "high", otherwise `NSAccessibilityPriorityMedium`. 2. Let userInfo be a `NSDictionary` with the following keys:     1. `NSAccessibilityAnnouncementKey` as announcement    2. `NSAccessibilityPriorityKey` as mapped\_priority 3. Call `NSAccessibilityPostNotificationWithUserInfo` with node, NSAccessibilityAnnouncementRequestedNotification, and userInfo. |

Note

When no suitable platform notification API is available (for example, older Linux accessibility stacks prior to ATK 2.50.0 that lack the newer notification signal, or on Windows when the user
agent is not able to use UIA), a user agent *MAY* synthesize a temporary, assistive-technology-only live region in its accessibility tree to convey an `aria notify` announcement. Such
fallback nodes are not exposed to or detectable by web content and this behavior is not required.

## 5. Privacy considerations

In accordance with [Web Platform Design Principles](https://w3ctag.github.io/design-principles/#do-not-expose-use-of-assistive-tech), this specification provides no programmatic
interface to determine if information is being used by Assistive Technologies. However, this specification does allow an author to present different information to users of Assistive
Technologies from the information available to users who do not use Assistive Technologies. This is possible using many features of the ARIA and CORE-AAM specifications, just as this is
possible using many other parts of the web technology stack. This content disparity could be abused to perform
[active fingerprinting](https://www.w3.org/TR/fingerprinting-guidance/#active-0) of users of Assistive Technologies.

## 6. Security considerations

This specification introduces no new security considerations.

## A. Change Log

### A.1 Substantive changes since the last [Candidate Recommendation Snapshot](https://www.w3.org/TR/2022/CR-core-aam-1.2-20221122/)

- 14-Nov-2022: add new AX API mappings for colindextext/rowindextext
- 4-Jan-2024: Fix: errant computed role for treegrid row
- 31-Oct-2023: Update UIA aria-readonly mappings
- 31-Oct-2023: Add aria-haspopup='grid' mappings
- 31-Oct-2023: Correct AXAPI notifications
- 26-Oct-2023: Remove UIA\_DescribedBy property from aria-describedby UIA mappings
- 12-Oct-2023: Make haspopup='true' mapping identical to haspopup='menu'
- 1-Sep-2023: Fix AX API aria-haspopup mappings
- 25-Aug-2023: Add map for `role=image` (synonym of `img`)
- 17-Aug-2023: add normative expectations and examples for computedrole
- 16-Aug-2023: Update mapping for aria-errormessage
- 15-May-2023: Add computed role section and mappings
- 8-May-2023: update UIA ins/del
- 13-Apr-2023: Add mapping for aria-braillelabel and aria-brailleroledescription
- 9-Apr-2023: Update annotation roles AXAPI mapping
- 6-Apr-2023: Update aria-describedby and aria-description AXAPI
- 6-Apr-2023: Update role='meter' subrole for AXAPI
- 1-Feb-2023: remove AXAPI-specific 'menuitem in group' guidance
- 1-Feb-2023: Update AXAPI mapping for aria-keyshortcuts
- 1-Feb-2023: Update IA2 role='blockquote' map
- 1-Feb-2023: Update MSAA mapping for paragraph and time and caption

### A.2 Substantive changes since the [Core Accessibility API Mappings 1.1 Recommendation](https://www.w3.org/TR/core-aam-1.1/)

- 1-Nov-2022: draft privacy and security
- 13-Oct-2022: fix: remove label and legend
- 12-Oct-2022: Remove mappings for `label` and `legend`.
- 05-Apr-2021: Update ATK mappings for `aria-colindex`, `aria-colspan`, `aria-colcount`, `aria-rowindex`, `aria-rowspan`, and
  `aria-rowcount`.
- 06-Apr-2020: Update ATK mappings for `alert` and `alertdialog`.
- 25-Feb-2020: Add mappings for `comment`, `mark`, and `suggestion` roles. Include `comment` in calculation for `aria-label` and group
  position.
- 25-Feb-2020: Add mappings for `aria-description`.
- 03-Nov-2019: Remove explicit AXRoleDescription values for AX API. User agents should follow the guidance described in the note.
- 22-Oct-2019: Add mappings for `strong` and `emphasis` roles for AX API.
- 22-Oct-2019: Add mappings for `code` role for AX API.
- 21-Oct-2019: Add mappings for `aria-colindextext` and `aria-rowindextext` roles for ATK, IA2, and UIA.
- 21-Oct-2019: Add mappings for `strong` and `emphasis` roles for ATK, IA2, and UIA.
- 21-Oct-2019: Add mappings for `code` role for ATK, IA2, and UIA.
- 18-Sep-2019: Update MSAA mappings for `subscript` and `superscript`
- 10-Sep-2019: Add mappings for `generic` role.
- 09-Jul-2019: Add mappings for `insertion` and `deletion` roles.
- 14-May-2019: Add mappings for `legend` role.
- 14-May-2019: Add mappings for `label` role.
- 14-May-2019: Add mappings for `time` role.
- 25-Apr-2019: Add mappings for `subscript` and `superscript` roles.
- 25-Feb-2019: Add mappings for `meter` role.
- 05-Feb-2019: Update UIA state and property change events.
- 06-Jun-2018: Update UIA mappings for `aria-placeholder`.
- 04-Jun-2018: Add mappings for `blockquote`, `caption`, and `paragraph` roles.
- 05-Mar-2018: Add mention of `AXTitle` for exposing rendered labels for AXAPI.
- 05-Mar-2018: Add events for `aria-label`, `aria-labelledby`, and `aria-describedby`.

## B. Acknowledgments

*This section is non-normative.*

The following people contributed to the development of this document.

- [Aaron Leventhal](https://github.com/aleventhal)
- [Benjamin Beaudry](https://github.com/benbeaudry)
- [Bogdan Brinza](https://github.com/boggydigital)
- [Carolyn MacLeod](https://github.com/carmacleod)
- [Daniel Montalvo](https://github.com/daniel-montalvo)
- [Denis Ah-Kang](https://github.com/deniak)
- [Dominique Hazael-Massieux](https://github.com/dontcallmedom)
- [James Craig](https://github.com/cookiecrook)
- [James Nurthen](https://github.com/jnurthen)
- [Jason Kiss](https://github.com/jasonkiss)
- [joanmarie](https://github.com/joanmarie)
- [Joseph Scheuhammer](https://github.com/klown)
- [Matt King](https://github.com/mcking65)
- [Melanie Richards](https://github.com/melanierichards)
- [Peter Krautzberger](https://github.com/pkra)
- [Philippe Le Hegaret](https://github.com/plehegar)
- [R Brown](https://github.com/ricksbrown)
- [Rahim Abdi](https://github.com/rahimabdi)
- [Richard Schwerdtfeger](https://github.com/richschwer)
- [Sarah Higley](https://github.com/smhigley)
- [Sayan Sivakumaran](https://github.com/sivakusayan)
- [Scott O'Hara](https://github.com/scottaohara)
- [Steve Faulkner](https://github.com/stevefaulkner)

### B.1 ARIA WG participants at the time of publication

### B.2 Enabling funders

This publication has been funded in part with U.S. Federal funds from the Department of Education, National Institute on Disability, Independent Living, and Rehabilitation Research (NIDILRR), initially under contract number ED-OSE-10-C-0067, then under contract number HHSP23301500054C, and now under HHS75P00120P00168. The content of this publication does not necessarily reflect the views or policies of the U.S. Department of Education, nor does mention of trade names, commercial products, or organizations imply endorsement by the U.S. Government.

## C. References

### C.1 Normative references

[HTML-AAM]
:   [HTML Accessibility API Mappings 1.0](https://www.w3.org/TR/html-aam-1.0/). Scott O'Hara; Rahim Abdi. W3C. 11 March 2026. W3C Working Draft. URL: <https://www.w3.org/TR/html-aam-1.0/>

[IAccessible2]
:   [IAccessible2](https://wiki.linuxfoundation.org/accessibility/iaccessible2/). Linux Foundation. URL: <https://wiki.linuxfoundation.org/accessibility/iaccessible2/>

[infra]
:   [Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[RFC2119]
:   [Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]
:   [Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[wai-aria]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.0](https://www.w3.org/TR/wai-aria/). James Craig; Michael Cooper et al. W3C. 20 March 2014. W3C Recommendation. URL: <https://www.w3.org/TR/wai-aria/>

[WAI-ARIA-1.2]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/). Joanmarie Diggs; James Nurthen; Michael Cooper; Carolyn MacLeod. W3C. 6 June 2023. W3C Recommendation. URL: <https://www.w3.org/TR/wai-aria-1.2/>

### C.2 Informative references

[accname-1.2]
:   [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/). Bryan Garaventa; Melanie Sumner. W3C. 11 March 2026. W3C Working Draft. URL: <https://www.w3.org/TR/accname-1.2/>

[Android-Accessibility-API]
:   [Android Accessibility API](https://developer.android.com/guide/topics/ui/accessibility). Google. URL: <https://developer.android.com/guide/topics/ui/accessibility>

[AT-SPI]
:   [Assistive Technology Service Provider Interface](https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/). The GNOME Project. URL: <https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/>

[ATK]
:   [ATK - Accessibility Toolkit](https://developer.gnome.org/atk/stable/). The GNOME Project. URL: <https://developer.gnome.org/atk/stable/>

[AXAPI]
:   [The NSAccessibility Protocol for macOS](https://developer.apple.com/documentation/appkit/nsaccessibility). Apple, Inc. URL: <https://developer.apple.com/documentation/appkit/nsaccessibility>

[CORE-AAM-1.1]
:   [Core Accessibility API Mappings 1.1](https://www.w3.org/TR/core-aam-1.1/). Joanmarie Diggs; Joseph Scheuhammer; Richard Schwerdtfeger; Michael Cooper; Andi Snow-Weaver; Aaron Leventhal. W3C. 14 December 2017. W3C Recommendation. URL: <https://www.w3.org/TR/core-aam-1.1/>

[dom]
:   [DOM Standard](https://dom.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: <https://dom.spec.whatwg.org/>

[UI-AUTOMATION]
:   [UI Automation](https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification). Microsoft Corporation. URL: <https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification>

[UIA-EXPRESS]
:   [The IAccessibleEx Interface](https://docs.microsoft.com/en-us/windows/win32/winauto/iaccessibleex). Microsoft Corporation. URL: <https://docs.microsoft.com/en-us/windows/win32/winauto/iaccessibleex>

[WAI-ARIA-ROADMAP]
:   [Roadmap for Accessible Rich Internet Applications (WAI-ARIA Roadmap)](https://www.w3.org/TR/wai-aria-roadmap/). Richard Schwerdtfeger. W3C. 4 February 2008. W3C Working Draft. URL: <https://www.w3.org/TR/wai-aria-roadmap/>

[↑](#title)

[Permalink](#dfn-accessibility-subtree)
exported

**Referenced in:**

- [§ 3.8.2 Changes to document content or node visibility](#ref-for-dfn-accessibility-subtree-1 "§ 3.8.2 Changes to document content or node visibility")

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