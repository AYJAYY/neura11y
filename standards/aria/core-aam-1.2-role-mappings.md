---
ai_context: Core-AAM role exposure rules and role mapping tables for WAI-ARIA semantics.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/core-aam-1.2/
standard: Core Accessibility API Mappings 1.2
status: normative
tags:
- aria
- core-aam
- roles
- role-mappings
- accessibility-api
title: Core Accessibility API Mappings 1.2 Role Mappings
---

# Core Accessibility API Mappings 1.2 Role Mappings

## General Rules and Role Mappings

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