---
ai_context: Auto-fetched full HTML-AAM 1.0 specification. Prefer split html-aam-1.0-*.md
  files for AI use.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/html-aam-1.0/
standard: HTML Accessibility API Mappings 1.0
status: normative
tags:
- aria
- html-aam
- html
- accessibility-api
- mappings
title: HTML Accessibility API Mappings 1.0 (Full Fetched)
---

[![W3C](https://www.w3.org/StyleSheets/TR/2021/logos/W3C)](https://www.w3.org/)

# HTML Accessibility API Mappings 1.0

[W3C Working Draft](https://www.w3.org/standards/types#WD) 11 March 2026

More details about this document

This version:
:   <https://www.w3.org/TR/2026/WD-html-aam-1.0-20260311/>

Latest published version:
:   <https://www.w3.org/TR/html-aam-1.0/>

Latest editor's draft:
:   <https://w3c.github.io/html-aam/>

History:
:   <https://www.w3.org/standards/history/html-aam-1.0/>
:   [Commit history](https://github.com/w3c/html-aam/commits/)

Editors:
:   Scott O'Hara ([Microsoft](https://www.microsoft.com/))
:   Rahim Abdi ([Apple](https://www.apple.com/))

Former editors:
:   Steve Faulkner ([TPGi](https://www.tpgi.com/)) (until May 2023)
:   Alexander Surkov ([Mozilla Foundation](https://www.mozilla.org/)) (until August 2018)
:   Bogdan Brinza ([Microsoft](https://www.microsoft.com/)) (until July 2018)
:   Jason Kiss (Invited Expert) (until June 2018)
:   Cynthia Shelly ([Microsoft](https://www.microsoft.com/)) (until September 2013)

Feedback:
:   [GitHub w3c/html-aam](https://github.com/w3c/html-aam/)
    ([pull requests](https://github.com/w3c/html-aam/pulls/),
    [new issue](https://github.com/w3c/html-aam/issues/new/choose),
    [open issues](https://github.com/w3c/html-aam/issues/))

[Copyright](https://www.w3.org/policies/#copyright)
©
2015-2026
[World Wide Web Consortium](https://www.w3.org/).
W3C®
[liability](https://www.w3.org/policies/#Legal_Disclaimer),
[trademark](https://www.w3.org/policies/#W3C_Trademarks) and
[permissive document license](https://www.w3.org/copyright/software-license-2023/ "W3C Software and Document Notice and License") rules apply.

---

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

### 3.5 HTML Element Role Mappings

- User agents *MUST* map HTML elements with implicit WAI-ARIA role semantics to platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) according to the identified WAI-ARIA role mapping as defined
  in the [[core-aam-1.2](#bib-core-aam-1.2 "Core Accessibility API Mappings 1.2")] specification.
- "Not mapped" means the element does not need to be exposed via an [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). This is usually because the element is not displayed as part of the user
  interface. However, authors can force some of these elements to be rendered. For instance, by overriding user agent styles to render elements that would have been otherwise set to
  `display: none`. In these cases, the user agent *SHOULD* map such elements to the role of [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic), unless other HTML features have been
  specified which would require a more specific [minimum role](#dfn-minimum-role) to be exposed.
- Where an element is indicated as having "No corresponding (WAI-ARIA) role", or is mapped to the [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role, user agents
  *MUST NOT* expose the [`aria-roledescription`](https://www.w3.org/TR/core-aam-1.2/#ariaRoleDescription) property value in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) unless the element has an
  explicit, conforming `role` attribute value which [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] does not prohibit the use of `aria-roledescription`.
- Some HTML elements expose implicit WAI-ARIA roles depending on whether they have been provided an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name). How an element
  participates in the computation of its own or another element's [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) and/or
  [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) is described in the
  [Accessible Name and Description Computation](#accessible-name-and-description-computation) section of this document.

#### 3.5.1 Platform API mapping requirements

- When HTML elements do not have an exact or equivalent mapping to a valid, non-abstract WAI-ARIA role, a unique `computedrole`
  string has been specified to serve as the return value for interoperability testing purposes. For instance, user agents *MAY* expose the `video` element with a `computedrole` of
  "`html-video`". Authors *MUST NOT* use any `html-`prefixed computed role string in the role attribute (such as `html-video`). User Agents *MUST* ignore any abstract or invalid role token.

  `<video> <!-- computedrole returns 'html-video' --> <main role="html-video"> <!-- Author error. computed role returns 'main' -->`
- **IAccessible2:**
  - All elements with accessible objects *SHOULD* implement the IAccessible, IAccessible2 and IAccessible2\_2 interfaces.
- **UIA:**
  - When a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) is referenced by a `label` element's `for` attribute, or a descendant of a `label` element, the labelable
    element's UIA `LabeledBy` property points to the UIA element for the `label` element.
  - Elements mapped to the `Text` Control Type are not generally represented as [accessible objects](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) in the
    [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), but are just part of the `Text` Control Pattern implemented for the whole HTML document. However, if they have any `aria-` attributes or an
    explicit `tabindex` specified, elements mapped to the `Text` Control Type will be represented as [accessible objects](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) in the
    [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree).
- **AXAPI:**
  - User agents *SHOULD* return a user-presentable, localized string value for the Mac Accessibility AXRoleDescription.

#### 3.5.2 `a` (represents a hyperlink)

|  |  |
| --- | --- |
| HTML Specification | [`a`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element) (represents a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`link`](https://www.w3.org/TR/core-aam-1.2/#role-map-link) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.3 `a` (no `href` attribute)

|  |  |
| --- | --- |
| HTML Specification | [`a`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element) (no [`href`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-href) attribute) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.4 `abbr`

|  |  |
| --- | --- |
| HTML Specification | [`abbr`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-abbr-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-abbr` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Roles: `ROLE_SYSTEM_TEXT`; `IA2_ROLE_TEXT_FRAME`  Object attributes: "abbr" attribute on the containing [`td`](#el-td) if a single child, text content used as a value |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Text` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_STATIC`  Object attributes: "abbr" attribute on the containing [`td`](#el-td) if a single child, text content used as a value |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.5 `address`

|  |  |
| --- | --- |
| HTML Specification | [`address`](https://html.spec.whatwg.org/multipage/sections.html#the-address-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.6 `area` (represents a hyperlink)

|  |  |
| --- | --- |
| HTML Specification | [`area`](https://html.spec.whatwg.org/multipage/image-maps.html#the-area-element) (represents a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`link`](https://www.w3.org/TR/core-aam-1.2/#role-map-link) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.7 `area` (no `href` attribute)

|  |  |
| --- | --- |
| HTML Specification | [`area`](https://html.spec.whatwg.org/multipage/image-maps.html#the-area-element) (no [`href`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-href) attribute) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User agents *MAY* still expose an `a` element lacking the `href` attribute with a `link` role in the event an author specifies interactive behavior for the element. For example, if using an [event handler attribute](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes). |

#### 3.5.8 `article`

|  |  |
| --- | --- |
| HTML Specification | [`article`](https://html.spec.whatwg.org/multipage/sections.html#the-article-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`article`](https://www.w3.org/TR/core-aam-1.2/#role-map-article) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.9 `aside` (scoped to the `body` or `main` element)

|  |  |
| --- | --- |
| HTML Specification | [`aside`](https://html.spec.whatwg.org/multipage/sections.html#the-aside-element) (scoped to the `body` or `main` element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`complementary`](https://www.w3.org/TR/core-aam-1.2/#role-map-complementary) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.10 `aside` (scoped to a sectioning content element)

|  |  |
| --- | --- |
| HTML Specification | [`aside`](https://html.spec.whatwg.org/multipage/sections.html#the-aside-element) (scoped to a [sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content) element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`complementary`](https://www.w3.org/TR/core-aam-1.2/#role-map-complementary) role if the [`aside`](https://html.spec.whatwg.org/multipage/sections.html#the-aside-element) element has an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name). Otherwise, [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.11 `audio`

|  |  |
| --- | --- |
| HTML Specification | [`audio`](https://html.spec.whatwg.org/multipage/media.html#audio) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-audio` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_GROUPING` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Group`  Localized Control Type: `"audio"`  **Note:** If the [`controls`](https://html.spec.whatwg.org/multipage/media.html#attr-media-controls) attribute is present, UI controls (e.g., play, volume) are exposed as children of the [`audio`](https://html.spec.whatwg.org/multipage/media.html#audio) element in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), and mapped as appropriate for the type of control (e.g., [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) or [`slider`](https://www.w3.org/TR/core-aam-1.2/#role-map-slider)).  User agents *MAY* include the following in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) and mark them as hidden or off-screen:  - Loading messages or error messages - UI controls that are not currently displayed |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role:  `ATK_ROLE_AUDIO` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `AXAudio`  AXRoleDescription: `"audio playback"`  **Note:** If the [`controls`](https://html.spec.whatwg.org/multipage/media.html#attr-media-controls) attribute is present, UI controls (e.g., play, volume) are exposed as descendants of an [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) with a role of [`toolbar`](https://www.w3.org/TR/core-aam-1.2/#role-map-toolbar), and mapped as appropriate for the type of control (e.g., [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) or [`slider`](https://www.w3.org/TR/core-aam-1.2/#role-map-slider)). |
| Comments |  |

#### 3.5.12 autonomous custom element

|  |  |
| --- | --- |
| HTML Specification | [autonomous custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#autonomous-custom-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If the author assigned a conforming ARIA role using the `role` attribute, map to that role. Otherwise, the [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.13 `b`

|  |  |
| --- | --- |
| HTML Specification | [`b`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-b-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Exposed by platform specific bold font weight text styles. |

#### 3.5.14 `base`

|  |  |
| --- | --- |
| HTML Specification | [`base`](https://html.spec.whatwg.org/multipage/semantics.html#the-base-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.15 `bdi`

|  |  |
| --- | --- |
| HTML Specification | [`bdi`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdi-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | IA2/ATK: May affect on "writing-mode" text attribute on its text container. |

#### 3.5.16 `bdo`

|  |  |
| --- | --- |
| HTML Specification | [`bdo`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | IA2/ATK: Exposed as "writing-mode" text attribute on its text container. |

#### 3.5.17 `blockquote`

|  |  |
| --- | --- |
| HTML Specification | [`blockquote`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-blockquote-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`blockquote`](https://www.w3.org/TR/core-aam-1.2/#role-map-blockquote) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.18 `body`

|  |  |
| --- | --- |
| HTML Specification | [`body`](https://html.spec.whatwg.org/multipage/sections.html#the-body-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User agents *MUST* ignore the `aria-hidden` attribute if specified on the `body` element. |

#### 3.5.19 `br`

|  |  |
| --- | --- |
| HTML Specification | [`br`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-br-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | May be exposed as '\n' character by the platform interface. |

#### 3.5.20 `button`

|  |  |
| --- | --- |
| HTML Specification | [`button`](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | A `button`'s mapping will change if the [`aria-pressed`](https://www.w3.org/TR/core-aam-1.2/#role-map-button-pressed) or [`aria-haspopup`](https://www.w3.org/TR/core-aam-1.2/#role-map-button-haspopup) attributes are specified. |

#### 3.5.21 `canvas`

|  |  |
| --- | --- |
| HTML Specification | [`canvas`](https://html.spec.whatwg.org/multipage/canvas.html#canvas) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-canvas` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Roles: `ROLE_SYSTEM_GRAPHIC`; `IA2_ROLE_CANVAS` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Image`  Descendants of the `canvas` element are mapped separately. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_CANVAS` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `""` |
| Comments |  |

#### 3.5.22 `caption`

|  |  |
| --- | --- |
| HTML Specification | [`caption`](https://html.spec.whatwg.org/multipage/tables.html#the-caption-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`caption`](https://www.w3.org/TR/core-aam-1.2/#role-map-caption) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Relations: `IA2_RELATION_LABEL_FOR` with parent [`table`](#el-table) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping  Other properties: The `LabeledBy` property for the parent [`table`](#el-table) element points to the UIA element for the `caption` element. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping  Relations: `ATK_RELATION_LABEL_FOR` with parent [`table`](#el-table) |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping  Relations: `ATK_RELATION_LABEL_FOR` with parent [`table`](#el-table) |
| Comments | Note  If a `caption` element is [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden) from the accessibility tree, then it will not provide an accessible name to its parent `table` element. |

#### 3.5.23 `cite`

|  |  |
| --- | --- |
| HTML Specification | [`cite`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-cite-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-cite` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | No accessible object. Styles used are mapped into text attributes on its text container. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | No accessible object. Styles used are exposed by UIA text attributes of the `TextRange` Control Pattern implemented on a parent accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | No accessible object. Styles used are mapped into text attributes on its text container. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.24 `code`

|  |  |
| --- | --- |
| HTML Specification | [`code`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-code-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`code`](https://www.w3.org/TR/core-aam-1.2/#role-map-code) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.25 `col`

|  |  |
| --- | --- |
| HTML Specification | [`col`](https://html.spec.whatwg.org/multipage/tables.html#the-col-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.26 `colgroup`

|  |  |
| --- | --- |
| HTML Specification | [`colgroup`](https://html.spec.whatwg.org/multipage/tables.html#the-colgroup-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_GROUPING` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Group`  Localized Control Type: `"colgroup"` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.27 `data`

|  |  |
| --- | --- |
| HTML Specification | [`data`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-data-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.28 `datalist` (represents pre-defined options for `input` element)

|  |  |
| --- | --- |
| HTML Specification | [`datalist`](https://html.spec.whatwg.org/multipage/form-elements.html#the-datalist-element) (represents pre-defined options for `input` element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`listbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-listbox) role, with the [`aria-multiselectable`](https://www.w3.org/TR/core-aam-1.2/#ariaMultiselectableFalse) property set to "true" if the `datalist`'s selection model allows multiple `option` elements to be selected at a time, and "false" otherwise |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If `datalist` is not linked to a proper `input` element, then `datalist` element is not mapped to accessibility APIs. |

#### 3.5.29 `dd`

|  |  |
| --- | --- |
| HTML Specification | [`dd`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dd-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`definition`](https://www.w3.org/TR/core-aam-1.2/#role-map-definition) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping  Note  Editorial Note: This value may change upon resolution of [ARIA #1662](https://github.com/w3c/aria/issues/1662). |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.30 `del`

|  |  |
| --- | --- |
| HTML Specification | [`del`](https://html.spec.whatwg.org/multipage/edits.html#the-del-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`deletion`](https://www.w3.org/TR/core-aam-1.2/#role-map-deletion) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.31 `details`

|  |  |
| --- | --- |
| HTML Specification | [`details`](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping  Localized Control Type: `"details"` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping  Relations: `"ATK_RELATION_DETAILS_FOR"` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.32 `dfn`

|  |  |
| --- | --- |
| HTML Specification | [`dfn`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-dfn-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`term`](https://www.w3.org/TR/core-aam-1.2/#role-map-term) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.33 `dialog`

|  |  |
| --- | --- |
| HTML Specification | [`dialog`](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`dialog`](https://www.w3.org/TR/core-aam-1.2/#role-map-dialog) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | See also the `dialog` element's [`open`](#att-open-dialog) attribute. |

#### 3.5.34 `dir` (obsolete)

|  |  |
| --- | --- |
| HTML Specification | [`dir`](https://html.spec.whatwg.org/multipage/obsolete.html#dir) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`list`](https://www.w3.org/TR/core-aam-1.2/#role-map-list) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | The `dir` element is marked as obsolete in HTML, and is not to be used by authors. |

#### 3.5.35 `div`

|  |  |
| --- | --- |
| HTML Specification | [`div`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-div-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.36 `dl`

|  |  |
| --- | --- |
| HTML Specification | [`dl`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dl-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`list`](https://www.w3.org/TR/core-aam-1.2/#role-map-list) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | list  Note  Editorial Note: This value may change upon resolution of [ARIA #1662](https://github.com/w3c/aria/issues/1662). |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_LIST`  States: `STATE_SYSTEM_READONLY` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `List` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_DESCRIPTION_LIST` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXList`  AXSubrole: `AXDefinitionList`  AXRoleDescription: `"definition list"` |
| Comments |  |

#### 3.5.37 `dt`

|  |  |
| --- | --- |
| HTML Specification | [`dt`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dt-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`term`](https://www.w3.org/TR/core-aam-1.2/#role-map-term) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping  Note  Editorial Note: This value may change upon resolution of [ARIA #1662](https://github.com/w3c/aria/issues/1662). |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.38 `em`

|  |  |
| --- | --- |
| HTML Specification | [`em`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-em-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`emphasis`](https://www.w3.org/TR/core-aam-1.2/#role-map-emphasis) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.39 `embed`

|  |  |
| --- | --- |
| HTML Specification | [`embed`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-embed` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Roles: `ROLE_SYSTEM_CLIENT`; `IA2_ROLE_EMBEDDED_OBJECT`  States: `STATE_SYSTEM_UNAVAILABLE` for windowless plugin |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Pane` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_EMBEDDED` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Depends on format of data file |
| Comments |  |

#### 3.5.40 `fieldset`

|  |  |
| --- | --- |
| HTML Specification | [`fieldset`](https://html.spec.whatwg.org/multipage/form-elements.html#the-fieldset-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: Use WAI-ARIA mapping  Relations: `IA2_RELATION_LABELLED_BY` with the first instance of a rendered child [`legend`](#el-legend) element |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Role: Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: Use WAI-ARIA mapping  Relations: `ATK_RELATION_LABELLED_BY` with first instance of a rendered child [`legend`](#el-legend) element |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Role: Use WAI-ARIA mapping  AXSubrole: `AXFieldset`  **AXDescription:** value from the first instance of a rendered child [`legend`](#el-legend) element |
| Comments | Note  If a `legend` element is [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden) from the accessibility tree, then it will not provide an accessible name to its parent `fieldset` element. |

#### 3.5.41 `figcaption`

|  |  |
| --- | --- |
| HTML Specification | [`figcaption`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figcaption-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`caption`](https://www.w3.org/TR/core-aam-1.2/#role-map-caption) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Role: Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Role: Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.42 `figure`

|  |  |
| --- | --- |
| HTML Specification | [`figure`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figure-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`figure`](https://www.w3.org/TR/core-aam-1.2/#role-map-figure) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Role: Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.43 `footer` (scoped to the `body` element)

|  |  |
| --- | --- |
| HTML Specification | [`footer`](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element) (scoped to the [`body`](https://html.spec.whatwg.org/multipage/sections.html#the-body-element) element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`contentinfo`](https://www.w3.org/TR/core-aam-1.2/#role-map-contentinfo) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.44 `footer` (scoped to the `main` element, or a sectioning content element)

|  |  |
| --- | --- |
| HTML Specification | [`footer`](https://html.spec.whatwg.org/multipage/sections.html#the-footer-element) (scoped to the [`main`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element, or a [sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content) element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`sectionfooter`](https://www.w3.org/TR/core-aam-1.2/#role-map-sectionfooter) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Group`  Localized Control Type: `"footer"` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_FOOTER` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User agents and assistive technology *MAY* not expose the `sectionfooter` role if the element:  - has no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) - is not keyboard focusable - has no other global ARIA attributes or HTML attributes that expose information to user agent's [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) |

#### 3.5.45 `form`

|  |  |
| --- | --- |
| HTML Specification | [`form`](https://html.spec.whatwg.org/multipage/forms.html#the-form-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`form`](https://www.w3.org/TR/core-aam-1.2/#role-map-form) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping  If a `form` has no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name):  Role: `ATK_ROLE_FORM` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If a [`form` has no accessible name](https://www.w3.org/TR/core-aam-1.2/#role-map-form-nameless), do not expose the element as a landmark. |

#### 3.5.46 form-associated custom element

|  |  |
| --- | --- |
| HTML Specification | [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-face-example) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If the author assigned a conforming ARIA role using the `role` attribute, map to that role. Otherwise, the [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.47 `h1`, `h2`, `h3`, `h4`, `h5`, and `h6`

|  |  |
| --- | --- |
| HTML Specification | [`h1`, `h2`, `h3`, `h4`, `h5`, and `h6`](https://html.spec.whatwg.org/multipage/sections.html#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`heading`](https://www.w3.org/TR/core-aam-1.2/#role-map-heading) role, with the [`aria-level`](https://www.w3.org/TR/core-aam-1.2/#ariaLevel) property set to the number in the element's tag name. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.48 `head`

|  |  |
| --- | --- |
| HTML Specification | [`head`](https://html.spec.whatwg.org/multipage/semantics.html#the-head-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not Mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.49 `header` (scoped to the `body` element)

|  |  |
| --- | --- |
| HTML Specification | [`header`](https://html.spec.whatwg.org/multipage/sections.html#the-header-element) (scoped to the [`body`](https://html.spec.whatwg.org/multipage/sections.html#the-body-element) element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`banner`](https://www.w3.org/TR/core-aam-1.2/#role-map-banner) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.50 `header` (scoped to the `main` element, or a sectioning content element)

|  |  |
| --- | --- |
| HTML Specification | [`header`](https://html.spec.whatwg.org/multipage/sections.html#the-header-element) (scoped to the [`main`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) element, or a [sectioning content](https://html.spec.whatwg.org/multipage/dom.html#sectioning-content) element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`sectionheader`](https://www.w3.org/TR/core-aam-1.2/#role-map-sectionheader) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Group`  Localized Control Type: `"header"` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_HEADER` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User agents and assistive technology *MAY* not expose the `sectionheader` role if the element:  - has no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) - is not keyboard focusable - has no other global ARIA attributes or HTML attributes that expose information to user agent's [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) |

#### 3.5.51 `hgroup`

|  |  |
| --- | --- |
| HTML Specification | [`hgroup`](https://html.spec.whatwg.org/multipage/sections.html#the-hgroup-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If an `hgroup` contains multiple heading elements, then the user agent *MAY* treat the heading element with the highest priority level as the sole heading of the `hgroup`. The user agent *MAY* expose all other heading elements as if they were [`p`](#el-p) elements. See [`paragraph` role on Core AAM](https://www.w3.org/TR/core-aam-1.2/#role-map-paragraph). |

#### 3.5.52 `hr`

|  |  |
| --- | --- |
| HTML Specification | [`hr`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-hr-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`separator`](https://www.w3.org/TR/core-aam-1.2/#role-map-separator) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If an `hr` element is a descendant of a `select` element, user agents *MAY* expose the element with a role of `none`. |

#### 3.5.53 `html`

|  |  |
| --- | --- |
| HTML Specification | [`html`](https://html.spec.whatwg.org/multipage/semantics.html#the-html-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User agents *MUST* ignore the `aria-hidden` attribute if specified on the `html` element.  Note  The `document` role of a web page is not exposed by the `html` element, but rather from a parent `document node` created by the user agent. |

#### 3.5.54 `i`

|  |  |
| --- | --- |
| HTML Specification | [`i`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-i-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Exposed by platform specific italic text styles. |

#### 3.5.55 `iframe`

|  |  |
| --- | --- |
| HTML Specification | [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-iframe-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-iframe` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `IA2_ROLE_INTERNAL_FRAME` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Pane` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_INTERNAL_FRAME` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.56 `img`

|  |  |
| --- | --- |
| HTML Specification | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`image`](https://www.w3.org/TR/core-aam-1.2/#role-map-image) or [`img`](https://www.w3.org/TR/core-aam-1.2/#role-map-img) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Note  ARIA 1.3 adds the `image` role as the preferred synonym to the ARIA 1.0 `img` role. The expected computed role for named `img` elements is now "image". |

#### 3.5.57 `img` (`alt` attribute value, when trimmed of [whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), is the empty string, i.e., `alt=""`, `alt=" "`, or `alt` with no value in the markup)

|  |  |
| --- | --- |
| HTML Specification | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element) ([`alt`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-alt) attribute value, when trimmed of [whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), is the empty string, i.e., `alt=""`, `alt=" "`, or `alt` with no value in the markup) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`none`](https://www.w3.org/TR/core-aam-1.2/#role-map-none) or [`presentation`](https://www.w3.org/TR/core-aam-1.2/#role-map-presentation) |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Note  If an `img` has an empty `alt`, but has been provided an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) via another valid naming mechanism per the [naming steps of this specification](#el-img-name), user agents will expose the element with its implicit `image` role. |

#### 3.5.58 `input` (`type` attribute in the Button state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Button](https://html.spec.whatwg.org/multipage/input.html#button-state-(type=button)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.59 `input` (`type` attribute in the Checkbox state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Checkbox](https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`checkbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-checkbox) role, with the [`aria-checked`](https://www.w3.org/TR/core-aam-1.2/#ariaCheckedMixed) state set to "mixed" if the element's [`indeterminate` IDL attribute](https://html.spec.whatwg.org/multipage/input.html#dom-input-indeterminate) is true, or "true" if the element's [checkedness](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-checked) is true, or "false" otherwise |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.60 `input` (`type` attribute in the Color state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Color](https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-color` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | If implemented as a textbox:  Roles: `ROLE_SYSTEM_TEXT`  If implemented as a color picker:  Roles: `IA2_ROLE_COLOR_CHOOSER` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | If implemented as a textbox:  Control Type: `Edit`  Localized Control Type:  "edit"  If implemented as a color picker:  Control Type: `button`  Localized Control Type:  "color picker" |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | If implemented as a button, use WAI-ARIA mapping for [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button).  If implemented as a textbox, use WAI-ARIA mapping for [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox). |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | If implemented as a textbox:  AXRole: `AXTextField`  AXSubrole: `(nil)`  AXRoleDescription: `"text field"`  If implemented as a color picker:  AXRole: `AXColorWell`  AXSubrole: `(nil)`  AXRoleDescription: `"color well"` |
| Comments | If implemented as a color picker, any UI controls presented for selecting a color are exposed in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), associated with the `input` element, and mapped as appropriate for the type of control (e.g., button or slider). |

#### 3.5.61 `input` (`type` attribute in the Date state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Date](https://html.spec.whatwg.org/multipage/input.html#date-state-(type=date)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-date` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | If implemented as a textbox:  Role: `ROLE_SYSTEM_TEXT`  Object attributes: `text-input-type:date`  If implemented as a date picker:  Role: `IA2_ROLE_DATE_EDITOR` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Depends on UI design of implementation. The UI in Windows 10 Edge, for example, is a composite of multiple spinners. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role:  `ATK_ROLE_CALENDAR` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXDateField`  AXSubrole: `(nil)`  AXRoleDescription: `"date field"` |
| Comments |  |

#### 3.5.62 `input` (`type` attribute in the Local Date and Time state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Local Date and Time](https://html.spec.whatwg.org/multipage/input.html#local-date-and-time-state-(type=datetime-local)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-datetime-local` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `IA2_ROLE_DATE_EDITOR` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Depends on UI design of implementation. The UI in Windows 10 Edge, for Example, is a composite of multiple spinners. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_CALENDAR` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXTextField`  AXSubrole: `(nil)`  AXRoleDescription: `"text field"` |
| Comments |  |

#### 3.5.63 `input` (`type` attribute in the E-mail state with no suggestions source element)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [E-mail](https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)) state with no [suggestions source element](https://html.spec.whatwg.org/multipage/input.html#concept-input-list)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Object attributes:  `text-input-type:email` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.64 `input` (`type` attribute in the File Upload state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [File Upload](https://html.spec.whatwg.org/multipage/input.html#file-upload-state-(type=file)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-file` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Implementation dependent. If represented by a container with a button a text label inside then:  Roles: `IA2_ROLE_TEXT_FRAME`  Children: `ROLE_SYSTEM_PUSHBUTTON` and `IA2_ROLE_LABEL` for a button and a text label elements. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Can be rendered as a single button control, or as a button control with a text input field.  Button control:  Control Type: `Button`  Text input field:  Control Type: `Edit`  Localized Control Type: `"file"` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_STATIC`  Children: `ATK_ROLE_PUSH_BUTTON` when pressed `ATK_ROLE_FILE_CHOOSER` dialog shown |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXButton`  AXSubrole: `AXFileUploadButton`  AXRoleDescription: `file upload button` |
| Comments |  |

#### 3.5.65 `input` (`type` attribute in the Hidden state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Hidden](https://html.spec.whatwg.org/multipage/input.html#hidden-state-(type=hidden)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.66 `input` (`type` attribute in the Image Button state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.67 `input` (`type` attribute in the Month state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Month](https://html.spec.whatwg.org/multipage/input.html#month-state-(type=month)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-month` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `IA2_ROLE_DATE_EDITOR` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Depends on UI design of implementation. The UI in Windows 10 Edge, for Example, is a composite of multiple spinners. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_DATE_EDITOR` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXTextField`  AXSubrole: `(nil)`  AXRoleDescription: `"text field"` |
| Comments |  |

#### 3.5.68 `input` (`type` attribute in the Number state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Number](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`spinbutton`](https://www.w3.org/TR/core-aam-1.2/#role-map-spinbutton) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | If implemented as a spin button, use WAI-ARIA mapping for [`spinbutton`](https://www.w3.org/TR/core-aam-1.2/#role-map-spinbutton).  If implemented as a text input, use WAI-ARIA mapping for [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox).  Object attributes: `text-input-type:number` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | If implemented as a spin button, use WAI-ARIA mapping for [`spinbutton`](https://www.w3.org/TR/core-aam-1.2/#role-map-spinbutton).  If implemented as a text input, use WAI-ARIA mapping for [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox).  Object attributes: `text-input-type:number` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.69 `input` (`type` attribute in the Password state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Password](https://html.spec.whatwg.org/multipage/input.html#password-state-(type=password)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-password` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_TEXT`  States: `STATE_SYSTEM_PROTECTED`; `IA2_STATE_SINGLE_LINE`; `STATE_SYSTEM_READONLY` if readonly, otherwise `IA2_STATE_EDITABLE` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Edit`  Other properties: `isPassword=true` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_PASSWORD_TEXT`  States: `ATK_STATE_SINGLE_LINE`; `ATK_STATE_READ_ONLY` if readonly, otherwise `ATK_STATE_EDITABLE` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXTextField`  AXSubrole: `AXSecureTextField`  AXRoleDescription: `"secure text field"` |
| Comments |  |

#### 3.5.70 `input` (`type` attribute in the Radio Button state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Radio Button](https://html.spec.whatwg.org/multipage/input.html#radio-button-state-(type=radio)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`radio`](https://www.w3.org/TR/core-aam-1.2/#role-map-radio) role, with the [`aria-checked`](https://www.w3.org/TR/core-aam-1.2/#ariaCheckedTrue) state set to "true" if the element's [checkedness](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-checked) is true, or "false" otherwise. With [`aria-setsize`](https://www.w3.org/TR/core-aam-1.1/#ariaSetsize) value reflecting number of `type=radio input` elements within the [radio button group](https://html.spec.whatwg.org/multipage/input.html#radio-button-group) and [`aria-posinset`](https://www.w3.org/TR/core-aam-1.1/#ariaPosinset) value reflecting the elements position within the [radio button group](https://html.spec.whatwg.org/multipage/input.html#radio-button-group). |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.71 `input` (`type` attribute in the Range state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Range](https://html.spec.whatwg.org/multipage/input.html#range-state-(type=range)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`slider`](https://www.w3.org/TR/core-aam-1.2/#role-map-slider) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.72 `input` (`type` attribute in the Reset Button state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Reset Button](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.73 `input` (`type` attribute in the Search state with no suggestions source element)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Search](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)) state with no [suggestions source element](https://html.spec.whatwg.org/multipage/input.html#concept-input-list)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`searchbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-searchbox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.74 `input` (`type` attribute in the Submit Button state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element)  ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Submit Button](https://html.spec.whatwg.org/multipage/input.html#submit-button-state-(type=submit)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.75 `input` (`type` attribute in the Telephone state with no suggestions source element)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element)  ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Telephone](https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)) state with no [suggestions source element](https://html.spec.whatwg.org/multipage/input.html#concept-input-list)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Object attributes:  `text-input-type:telephone` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.76 `input` (`type` attribute in the Text state with no suggestions source element)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element)  ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Text](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)) state with no [suggestions source element](https://html.spec.whatwg.org/multipage/input.html#concept-input-list)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.77 `input` (`type` attribute in the Text, Search, Telephone, URL, or E-mail states with a suggestions source element)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element)  ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Text](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), [Search](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)), [Telephone](https://html.spec.whatwg.org/multipage/input.html#telephone-state-(type=tel)), [URL](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)), or [E-mail](https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)) states with a [suggestions source element](https://html.spec.whatwg.org/multipage/input.html#concept-input-list)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`combobox`](https://www.w3.org/TR/core-aam-1.2/#role-map-combobox) role, with the [`aria-controls`](https://www.w3.org/TR/core-aam-1.2/#ariaControls) property set to the same value as the [`list`](https://html.spec.whatwg.org/multipage/input.html#attr-input-list) attribute |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Object attributes: `text-input-type:`*`as per input type`* |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping  Other properties: `ControllerFor` points to the suggestions source element |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.78 `input` (`type` attribute in the Time state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Time](https://html.spec.whatwg.org/multipage/input.html#time-state-(type=time)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-time` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_SPINBUTTON` if implemented as a simple [widget](https://www.w3.org/TR/wai-aria/#dfn-widget); `ROLE_SYSTEM_GROUPING` with child controls mapped as appropriate if implemented as a complex [widget](https://www.w3.org/TR/wai-aria/#dfn-widget)  Object attributes: `text-input-type:time` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Depends on UI design of implementation. The UI in Windows 10 Edge, for Example, is a composite of multiple spinners. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_SPINBUTTON` if implemented as a simple [widget](https://www.w3.org/TR/wai-aria/#dfn-widget).  If implemented as a complex [widget](https://www.w3.org/TR/wai-aria/#dfn-widget) use:  Role: `ROLE_PANEL` and map child controls as appropriate. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXTimeField`  AXSubrole: `(nil)`  AXRoleDescription: `"time field"` |
| Comments |  |

#### 3.5.79 `input` (`type` attribute in the URL state with no suggestions source element)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element) ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [URL](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)) state with no [suggestions source element](https://html.spec.whatwg.org/multipage/input.html#concept-input-list)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Object attributes: `text-input-type:url` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.80 `input` (`type` attribute in the Week state)

|  |  |
| --- | --- |
| HTML Specification | [`input`](https://html.spec.whatwg.org/multipage/input.html#the-input-element)  ([`type`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) attribute in the [Week](https://html.spec.whatwg.org/multipage/input.html#week-state-(type=week)) state) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-input-week` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `IA2_ROLE_DATE_EDITOR`  Object attributes: `text-input-type:week` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Depends on UI design of implementation. The UI in Windows 10 Edge, for Example, is a composite of multiple spinners. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_CALENDAR` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXTextField`  AXSubrole: `(nil)`  AXRoleDescription: `"text field"` |
| Comments |  |

#### 3.5.81 `ins`

|  |  |
| --- | --- |
| HTML Specification | [`ins`](https://html.spec.whatwg.org/multipage/edits.html#the-ins-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`insertion`](https://www.w3.org/TR/core-aam-1.2/#role-map-insertion) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.82 `kbd`

|  |  |
| --- | --- |
| HTML Specification | [`kbd`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-kbd-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-kbd` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | No accessible object.  Text attributes: `font-family:monospace` on the text container |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | No accessible object. Styles used are exposed by UIA text attribute identifiers of the `TextRange` Control Pattern implemented on a parent accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | No accessible object. Mapped into "font-family:monospace" text attribute on its text container. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.83 `label`

|  |  |
| --- | --- |
| HTML Specification | [`label`](https://html.spec.whatwg.org/multipage/forms.html#the-label-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-label` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Roles: `ROLE_SYSTEM_STATICTEXT`; `IA2_ROLE_LABEL`  Relations: `IA2_RELATION_LABEL_FOR` with a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) that is child to the `label` or referred to by the `label` element's [`for`](#att-for-label) attribute. The associated labelable element has `IA2_RELATION_LABELLED_BY` pointing to the `label`. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Group`  Relations: When the `label` element contains a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label), the `LabeledBy` property for the element points to the UIA element for the `label` element.  When the `label` element has a [`for`](#att-for-label) attribute referencing a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label), the `LabeledBy` property for the referenced element points to the UIA element for the `label` element. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_LABEL`  Relations: `ATK_RELATION_LABEL_FOR` for a child [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) or labelable element referred by [`for`](#att-for-label) attribute. Note, related labelable element provides `ATK_RELATION_LABELLED_BY` pointing to the `label`. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments | Note  If a `label` element is [hidden](https://www.w3.org/TR/wai-aria/#dfn-hidden) from the accessibility tree, then it will not provide an accessible name to the [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) it is associated with. |

#### 3.5.84 `legend`

|  |  |
| --- | --- |
| HTML Specification | [`legend`](https://html.spec.whatwg.org/multipage/form-elements.html#the-legend-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-legend` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Roles: `ROLE_SYSTEM_STATICTEXT`; `IA2_ROLE_LABEL`  Relations: `IA2_RELATION_LABEL_FOR` with the parent [`fieldset`](#el-fieldset) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Text`  Other properties: The `LabeledBy` property for the parent [`fieldset`](#el-fieldset) points to the UIA element for the `legend` element. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_LABEL`  Relations: `ATK_RELATION_LABEL_FOR` with parent [`fieldset`](#el-fieldset) element |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.85 `li`

|  |  |
| --- | --- |
| HTML Specification | [`li`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-li-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`listitem`](https://www.w3.org/TR/core-aam-1.2/#role-map-listitem) role with [`aria-setsize`](https://www.w3.org/TR/core-aam-1.1/#ariaSetsize) value reflecting number of `li` elements within the parent `ol`, `menu` or `ul` and [`aria-posinset`](https://www.w3.org/TR/core-aam-1.1/#ariaPosinset) value reflecting the `li` elements position within the set. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If `li` element is not a child of [`ol`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ol-element) , [`menu`](https://html.spec.whatwg.org/multipage/grouping-content.html#menus) or [`ul`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element), or if the containing list element is no longer exposed with a `list` role, then expose the `li` element with a `generic` role. |

#### 3.5.86 `link`

|  |  |
| --- | --- |
| HTML Specification | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#the-link-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.87 `main`

|  |  |
| --- | --- |
| HTML Specification | [`main`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-main-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`main`](https://www.w3.org/TR/core-aam-1.2/#role-map-main) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.88 `map`

|  |  |
| --- | --- |
| HTML Specification | [`map`](https://html.spec.whatwg.org/multipage/image-maps.html#the-map-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-map` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped if used as an image map. Otherwise,  Role: `IA2_ROLE_TEXT_FRAME` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped if used as an image map, otherwise:  Role: `ATK_ROLE_STATIC` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Role: `AXImageMap` if used as an image map. Otherwise,  Role: `AXGroup` if associated with an `img` with no `alt`. Otherwise,  not mapped if not associated with an `img`. |
| Comments |  |

#### 3.5.89 `mark`

|  |  |
| --- | --- |
| HTML Specification | [`mark`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-mark-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`mark`](https://www.w3.org/TR/core-aam-1.2/#role-map-mark) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.90 `math`

|  |  |
| --- | --- |
| HTML Specification | [`math`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#mathml) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | See comments |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | See comments |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | See comments |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | See comments |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | See comments |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | See comments |
| Comments | Mapping for `math` is defined by [MathML AAM 1.0](https://w3c.github.io/mathml-aam/). |

#### 3.5.91 `menu`

|  |  |
| --- | --- |
| HTML Specification | [`menu`](https://html.spec.whatwg.org/multipage/grouping-content.html#menus) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`list`](https://www.w3.org/TR/core-aam-1.2/#role-map-list) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | The [`menu`](https://html.spec.whatwg.org/multipage/grouping-content.html#menus) element is a semantic alternative to the [`ul`](#el-ul) element. It has no implemented mappings or behavior that reflect the semantics of the ARIA [`menu`](https://www.w3.org/TR/core-aam-1.2/#role-map-menu) role.  Note obsolete [`menuitem` element](https://html.spec.whatwg.org/multipage/obsolete.html#menuitem) and [`menu` with `type` attribute](https://html.spec.whatwg.org/multipage/obsolete.html#attr-menu-type). |

#### 3.5.92 `meta`

|  |  |
| --- | --- |
| HTML Specification | [`meta`](https://html.spec.whatwg.org/multipage/semantics.html#meta) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.93 `meter`

|  |  |
| --- | --- |
| HTML Specification | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#the-meter-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`meter`](https://www.w3.org/TR/core-aam-1.2/#role-map-meter) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.94 `nav`

|  |  |
| --- | --- |
| HTML Specification | [`nav`](https://html.spec.whatwg.org/multipage/sections.html#the-nav-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`navigation`](https://www.w3.org/TR/core-aam-1.2/#role-map-navigation) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.95 `noscript`

|  |  |
| --- | --- |
| HTML Specification | [`noscript`](https://html.spec.whatwg.org/multipage/scripting.html#the-noscript-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.96 `object`

|  |  |
| --- | --- |
| HTML Specification | [`object`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-object-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-object` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Depends on format of data file. If it contains a plugin then,  Role: `IA2_ROLE_EMBEDDED_OBJECT`  States: `STATE_SYSTEM_UNAVAILABLE` for windowless plugin |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Depends on format of data file. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Depends on format of data file. If contains a plugin then  Role: `ATK_ROLE_EMBEDDED` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Depends on format of data file. |
| Comments |  |

#### 3.5.97 `ol`

|  |  |
| --- | --- |
| HTML Specification | [`ol`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ol-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`list`](https://www.w3.org/TR/core-aam-1.2/#role-map-list) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.98 `optgroup`

|  |  |
| --- | --- |
| HTML Specification | [`optgroup`](https://html.spec.whatwg.org/multipage/form-elements.html#the-optgroup-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.99 `option` (in a list of options or represents a suggestion in a `datalist`)

|  |  |
| --- | --- |
| HTML Specification | [`option`](https://html.spec.whatwg.org/multipage/form-elements.html#the-option-element) (in a [list of options](https://html.spec.whatwg.org/multipage/form-elements.html#concept-select-option-list) or represents a suggestion in a [`datalist`](https://html.spec.whatwg.org/multipage/form-elements.html#the-datalist-element)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`option`](https://www.w3.org/TR/core-aam-1.2/#role-map-option) role, with the [`aria-selected`](https://www.w3.org/TR/core-aam-1.2/#ariaSelectedTrue) state set to "true" if the element's [selectedness](https://html.spec.whatwg.org/multipage/form-elements.html#concept-option-selectedness) is true, or "false" otherwise. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.100 `output`

|  |  |
| --- | --- |
| HTML Specification | [`output`](https://html.spec.whatwg.org/multipage/form-elements.html#the-output-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`status`](https://www.w3.org/TR/core-aam-1.2/#role-map-status) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Relations: `IA2_RELATION_LABELLED_BY` with associated `label` element |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping  Relations: `ATK_RELATION_LABELLED_BY` with associated `label` element |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | `AXDescription`: value from associated `label` element subtree. |
| undefined |  |

#### 3.5.101 `p`

|  |  |
| --- | --- |
| HTML Specification | [`p`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-p-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`paragraph`](https://www.w3.org/TR/core-aam-1.2/#role-map-paragraph) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.102 `param`

|  |  |
| --- | --- |
| HTML Specification | [`param`](https://html.spec.whatwg.org/multipage/obsolete.html#param) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | `param` is obsolete in HTML |

#### 3.5.103 `picture`

|  |  |
| --- | --- |
| HTML Specification | [`picture`](https://html.spec.whatwg.org/multipage/embedded-content.html#the-picture-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.104 `pre`

|  |  |
| --- | --- |
| HTML Specification | [`pre`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-pre-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.105 `progress`

|  |  |
| --- | --- |
| HTML Specification | [`progress`](https://html.spec.whatwg.org/multipage/form-elements.html#the-progress-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`progressbar`](https://www.w3.org/TR/core-aam-1.2/#role-map-progressbar) role, with, if the progress bar is determinate, the [`aria-valuemax`](https://www.w3.org/TR/core-aam-1.2/#ariaValueMax) property set to the maximum value of the progress bar, the [`aria-valuemin`](https://www.w3.org/TR/core-aam-1.2/#ariaValueMin) property set to zero, and the [`aria-valuenow`](https://www.w3.org/TR/core-aam-1.2/#ariaValueNow) property set to the current value of the progress bar |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.106 `q`

|  |  |
| --- | --- |
| HTML Specification | [`q`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-q-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | `::before` and `::after` CSS pseudo content is used by platforms to render the element's quotation marks. |

#### 3.5.107 `rp`

|  |  |
| --- | --- |
| HTML Specification | [`rp`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-rp-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | html-rp |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | No accessible object. No child elements are exposed if [`ruby`](#el-ruby) is supported by the browser. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | No accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | No accessible object. No child elements are exposed if [`ruby`](#el-ruby) is supported by the browser. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.108 `rt`

|  |  |
| --- | --- |
| HTML Specification | [`rt`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-rt-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | html-rt |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | No accessible object. No child elements are exposed if [`ruby`](#el-ruby) is supported by the browser. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | No accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | No accessible object. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `AXRubyText`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.109 `ruby`

|  |  |
| --- | --- |
| HTML Specification | [`ruby`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-ruby-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | html-ruby |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_TEXT`; `IA2_ROLE_TEXT_FRAME` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Text`  Localized Control Type: `"ruby"` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_STATIC` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `AXRubyInline`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.110 `s`

|  |  |
| --- | --- |
| HTML Specification | [`s`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-s-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`deletion`](https://www.w3.org/TR/core-aam-1.2/#role-map-deletion) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.111 `samp`

|  |  |
| --- | --- |
| HTML Specification | [`samp`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-samp-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.112 `script`

|  |  |
| --- | --- |
| HTML Specification | [`script`](https://html.spec.whatwg.org/multipage/scripting.html#the-script-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.113 `search`

|  |  |
| --- | --- |
| HTML Specification | [`search`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-search-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`search`](https://www.w3.org/TR/core-aam-1.2/#role-map-search) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.114 `section`

|  |  |
| --- | --- |
| HTML Specification | [`section`](https://html.spec.whatwg.org/multipage/sections.html#the-section-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`region`](https://www.w3.org/TR/core-aam-1.2/#role-map-region) role if the [`section`](https://html.spec.whatwg.org/multipage/sections.html#the-section-element) element has an [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name). Otherwise, the [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role. |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.115 `select` (with a `multiple` attribute or `size` attribute having value greater than `1`)

|  |  |
| --- | --- |
| HTML Specification | [`select`](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element)  (with a [`multiple`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-multiple) attribute or [`size`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-size) attribute having value greater than `1`) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`listbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-listbox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.116 `select` (with NO `multiple` attribute and NO `size` attribute having value greater than `1`)

|  |  |
| --- | --- |
| HTML Specification | [`select`](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element)  (with NO [`multiple`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-multiple) attribute and NO [`size`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-size) attribute having value greater than `1`) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`combobox`](https://www.w3.org/TR/core-aam-1.2/#role-map-combobox) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.117 `slot`

|  |  |
| --- | --- |
| HTML Specification | [`slot`](https://html.spec.whatwg.org/multipage/scripting.html#the-slot-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.118 `small`

|  |  |
| --- | --- |
| HTML Specification | [`small`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-small-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Exposed by platform specific font size styles. |

#### 3.5.119 `source`

|  |  |
| --- | --- |
| HTML Specification | [`source`](https://html.spec.whatwg.org/multipage/embedded-content.html#the-source-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.120 `span`

|  |  |
| --- | --- |
| HTML Specification | [`span`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-span-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.121 `strong`

|  |  |
| --- | --- |
| HTML Specification | [`strong`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-strong-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`strong`](https://www.w3.org/TR/core-aam-1.2/#role-map-strong) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.122 `style`

|  |  |
| --- | --- |
| HTML Specification | [`style`](https://html.spec.whatwg.org/multipage/semantics.html#the-style-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | **Note:** There are instances where CSS properties can affect what is exposed by accessibility APIs. For instance, `display: none` or `visibility: hidden` will remove an element from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) and hide its presence from assistive technologies. |

#### 3.5.123 `sub`

|  |  |
| --- | --- |
| HTML Specification | [`sub`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-sub-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`subscript`](https://www.w3.org/TR/core-aam-1.2/#role-map-subscript) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.124 `summary`

|  |  |
| --- | --- |
| HTML Specification | [`summary`](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-summary-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | If the element is the first child of its type within a parent `details` element: `html-summary`  Otherwise, if it is not the first child of its type of a parent `details` element, or it is not a child of a `details` element: [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_PUSHBUTTON`  States: `STATE_SYSTEM_EXPANDED` / `STATE_SYSTEM_COLLAPSED`  Actions: `expand` / `collapse` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Button`  Control Pattern: `ExpandCollapse` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ROLE_TOGGLE_BUTTON`  Relations: `ATK_RELATION_DETAILS` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXDisclosureTriangle`  AXSubrole: `(nil)`  AXRoleDescription: `"disclosure triangle"` |
| Comments | If a `summary` element is not a child of a `details` element, or it is not the first `summary` element of a parent `details`, then user agents *MUST* expose the `summary` element with a `generic` role. |

#### 3.5.125 `sup`

|  |  |
| --- | --- |
| HTML Specification | [`sup`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-sup-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`superscript`](https://www.w3.org/TR/core-aam-1.2/#role-map-superscript) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.126 `svg`

|  |  |
| --- | --- |
| HTML Specification | [`svg`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#svg-0) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | See comments |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | See comments |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | See comments |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | See comments |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | See comments |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | See comments |
| Comments | Mapping for `svg` is defined by [SVG Accessibility API Mappings](https://www.w3.org/TR/svg-aam-1.0/). See also [Graphics Accessibility API Role Mappings](https://w3c.github.io/graphics-aam/#mapping_role_table) |

#### 3.5.127 `table`

|  |  |
| --- | --- |
| HTML Specification | [`table`](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`table`](https://www.w3.org/TR/core-aam-1.2/#role-map-table) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Relations: `IA2_RELATION_LABELLED_BY` with first instance of a rendered child [`caption`](#el-caption) element |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping  Relations: `ATK_RELATION_LABELLED_BY` with first instance of a rendered child [`caption`](#el-caption) element |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping  **AXDescription:** value from the first instance of a rendered child [`caption`](#el-caption) element |
| Comments |  |

#### 3.5.128 `tbody`

|  |  |
| --- | --- |
| HTML Specification | [`tbody`](https://html.spec.whatwg.org/multipage/tables.html#the-tbody-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`rowgroup`](https://www.w3.org/TR/core-aam-1.2/#role-map-rowgroup) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.129 `td` (ancestor `table` element has `table` role)

|  |  |
| --- | --- |
| HTML Specification | [`td`](https://html.spec.whatwg.org/multipage/tables.html#the-td-element) (ancestor [`table`](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) element has [`table`](https://www.w3.org/TR/core-aam-1.2/#role-map-table) role) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`cell`](https://www.w3.org/TR/core-aam-1.2/#role-map-cell) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.130 `td` (ancestor `table` element has `grid` or `treegrid` role)

|  |  |
| --- | --- |
| HTML Specification | [`td`](https://html.spec.whatwg.org/multipage/tables.html#the-td-element) (ancestor [`table`](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) element has [`grid`](https://www.w3.org/TR/core-aam-1.2/#role-map-grid) or [`treegrid`](https://www.w3.org/TR/core-aam-1.2/#role-map-treegrid) role) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`gridcell`](https://www.w3.org/TR/core-aam-1.2/#role-map-gridcell) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.131 `template`

|  |  |
| --- | --- |
| HTML Specification | [`template`](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.132 `textarea`

|  |  |
| --- | --- |
| HTML Specification | [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#the-textarea-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`textbox`](https://www.w3.org/TR/core-aam-1.2/#role-map-textbox) role, with the [`aria-multiline`](https://www.w3.org/TR/core-aam-1.2/#ariaMultilineTrue) property set to "true" |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.133 `tfoot`

|  |  |
| --- | --- |
| HTML Specification | [`tfoot`](https://html.spec.whatwg.org/multipage/tables.html#the-tfoot-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`rowgroup`](https://www.w3.org/TR/core-aam-1.2/#role-map-rowgroup) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.134 `th` (is not a column header, row header, column group header or row group header, and ancestor `table` element has `table` role)

|  |  |
| --- | --- |
| HTML Specification | [`th`](https://html.spec.whatwg.org/multipage/tables.html#the-th-element) (is not a [column header](https://html.spec.whatwg.org/multipage/tables.html#column-header), [row header](https://html.spec.whatwg.org/multipage/tables.html#row-header), [column group header](https://html.spec.whatwg.org/multipage/tables.html#column-group-header) or [row group header](https://html.spec.whatwg.org/multipage/tables.html#row-group-header), and ancestor [`table`](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) element has [`table`](https://www.w3.org/TR/core-aam-1.2/#role-map-table) role) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`cell`](https://www.w3.org/TR/core-aam-1.2/#role-map-cell) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.135 `th` (is not a column header, row header, column group header or row group header, and ancestor `table` element has `grid` or `treegrid` role)

|  |  |
| --- | --- |
| HTML Specification | [`th`](https://html.spec.whatwg.org/multipage/tables.html#the-th-element) (is not a [column header](https://html.spec.whatwg.org/multipage/tables.html#column-header), [row header](https://html.spec.whatwg.org/multipage/tables.html#row-header), [column group header](https://html.spec.whatwg.org/multipage/tables.html#column-group-header) or [row group header](https://html.spec.whatwg.org/multipage/tables.html#row-group-header), and ancestor [`table`](https://html.spec.whatwg.org/multipage/tables.html#the-table-element) element has [`grid`](https://www.w3.org/TR/core-aam-1.2/#role-map-grid) or [`treegrid`](https://www.w3.org/TR/core-aam-1.2/#role-map-treegrid) role) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`gridcell`](https://www.w3.org/TR/core-aam-1.2/#role-map-gridcell) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.136 `th` (is a column header or column group header)

|  |  |
| --- | --- |
| HTML Specification | [`th`](https://html.spec.whatwg.org/multipage/tables.html#the-th-element) (is a [column header](https://html.spec.whatwg.org/multipage/tables.html#column-header) or [column group header](https://html.spec.whatwg.org/multipage/tables.html#column-group-header)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`columnheader`](https://www.w3.org/TR/core-aam-1.2/#role-map-columnheader) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.137 `th` (is a row header or row group header)

|  |  |
| --- | --- |
| HTML Specification | [`th`](https://html.spec.whatwg.org/multipage/tables.html#the-th-element) (is a [row header](https://html.spec.whatwg.org/multipage/tables.html#row-header) or [row group header](https://html.spec.whatwg.org/multipage/tables.html#row-group-header)) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`rowheader`](https://www.w3.org/TR/core-aam-1.2/#role-map-rowheader) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.138 `thead`

|  |  |
| --- | --- |
| HTML Specification | [`thead`](https://html.spec.whatwg.org/multipage/tables.html#the-thead-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`rowgroup`](https://www.w3.org/TR/core-aam-1.2/#role-map-rowgroup) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.139 `time`

|  |  |
| --- | --- |
| HTML Specification | [`time`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`time`](https://www.w3.org/TR/core-aam-1.2/#role-map-time) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.140 `title`

|  |  |
| --- | --- |
| HTML Specification | [`title`](https://html.spec.whatwg.org/multipage/semantics.html#the-title-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | A `title` element provides the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) for its document. |

#### 3.5.141 `tr`

|  |  |
| --- | --- |
| HTML Specification | [`tr`](https://html.spec.whatwg.org/multipage/tables.html#the-tr-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`row`](https://www.w3.org/TR/core-aam-1.2/#role-map-row) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.142 `track`

|  |  |
| --- | --- |
| HTML Specification | [`track`](https://html.spec.whatwg.org/multipage/media.html#the-track-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.5.143 `u`

|  |  |
| --- | --- |
| HTML Specification | [`u`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-u-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`generic`](https://www.w3.org/TR/core-aam-1.2/#role-map-generic) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Exposed by platform specific underline text styles. |

#### 3.5.144 `ul`

|  |  |
| --- | --- |
| HTML Specification | [`ul`](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`list`](https://www.w3.org/TR/core-aam-1.2/#role-map-list) role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Use WAI-ARIA mapping |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.5.145 `var`

|  |  |
| --- | --- |
| HTML Specification | [`var`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-var-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-var` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | No accessible object. Styles used are mapped to text attributes on its text container. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | No accessible object. Styles used are exposed by UIA text attribute identifiers of the `TextRange` Control Pattern implemented on a parent accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | No accessible object. Styles used are mapped to text attributes on its text container. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments |  |

#### 3.5.146 `video`

|  |  |
| --- | --- |
| HTML Specification | [`video`](https://html.spec.whatwg.org/multipage/media.html#video) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | `html-video` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Role: `ROLE_SYSTEM_GROUPING` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Control Type: `Group`  Localized Control Type: `"group"`  **Note:** If the [`controls`](https://html.spec.whatwg.org/multipage/media.html#attr-media-controls) attribute is present, UI controls (e.g., play, volume) are exposed as children of the [`video`](https://html.spec.whatwg.org/multipage/media.html#video) element in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), and mapped as appropriate for the type of control (e.g., [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) or [`slider`](https://www.w3.org/TR/core-aam-1.2/#role-map-slider)).  User agents *MAY* include the following in the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree) and mark them as hidden or off-screen:  - Loading messages or error messages - UI controls that are not currently displayed |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Role: `ATK_ROLE_VIDEO` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `AXVideo`  AXRoleDescription: `"video playback"`  **Note:** If the [`controls`](https://html.spec.whatwg.org/multipage/media.html#attr-media-controls) attribute is present, UI controls (e.g., play, volume) are exposed as descendants of an [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) with a role of [`toolbar`](https://www.w3.org/TR/core-aam-1.2/#role-map-toolbar), and mapped as appropriate for the type of control (e.g., [`button`](https://www.w3.org/TR/core-aam-1.2/#role-map-button) or [`slider`](https://www.w3.org/TR/core-aam-1.2/#role-map-slider)). |
| Comments |  |

#### 3.5.147 `wbr`

|  |  |
| --- | --- |
| HTML Specification | [`wbr`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-wbr-element) |
| [[wai-aria-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | No corresponding role |
| [Computed Role](https://www.w3.org/TR/core-aam-1.2/#roleMappingComputedRole) | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | If a line break is added, expose it with `IAccessibleText` on the text container |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | A line break if added is exposed via Text interface on its text container |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | AXRole: `AXGroup`  AXSubrole: `(nil)`  AXRoleDescription: `"group"` |
| Comments |  |

### 3.6 HTML Attribute State and Property Mappings

- User agents *MUST* map HTML attributes with default WAI-ARIA state and property semantics to platform [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api) according to the identified WAI-ARIA state and
  property mapping as defined in the [[core-aam-1.2](#bib-core-aam-1.2 "Core Accessibility API Mappings 1.2")] specification.
- A '?' in a cell indicates the data has yet to be provided.
- "Not mapped" (Not Applicable) means the attribute does not need to be exposed via an [accessibility API](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). This is usually because the attribute is not displayed as
  part of the user interface.

  Note

  In some cases, while not directly exposed to accessibility APIs, an attribute can still impact the accessibility of an element. e.g., [`autoplay`](#att-autoplay) will
  automatically start playing [`video`](#el-video) or [`audio`](#el-audio) elements.
- All elements having an accessible object in IAccessible2 mapping are supposed to implement IAccessible, IAccessible2 and IAccessible2\_2 interfaces.
- User interaction with certain HTML elements will set an element's [dirty value flag](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-fe-dirty). These elements, as identified
  in [HTML], could have attributes that represent the default value or state of the element. When the dirty flag is set, that default value or state does not necessarily determine the value
  or state of the element or corresponding accessible node.

#### 3.6.1 `abbr`

|  |  |
| --- | --- |
| HTML Specification | `abbr` |
| Element(s) | [`th`](https://html.spec.whatwg.org/multipage/tables.html#attr-th-abbr) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: "abbr" until child [`abbr`](#el-abbr) element is provided |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: "abbr" until child [`abbr`](#el-abbr) element is provided |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXDescription: <value>` |
| Comments |  |

#### 3.6.2 `accept`

|  |  |
| --- | --- |
| HTML Specification | `accept` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-accept) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.3 `accept-charset`

|  |  |
| --- | --- |
| HTML Specification | `accept-charset` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/forms.html#attr-form-accept-charset) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.4 `accesskey`

|  |  |
| --- | --- |
| HTML Specification | `accesskey` |
| Element(s) | [`HTML elements`](https://html.spec.whatwg.org/multipage/interaction.html#the-accesskey-attribute) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | A key binding accessible by [`accKeyboardShortcut`](https://msdn.microsoft.com/en-us/library/accessibility.iaccessible.acckeyboardshortcut.aspx) and `IAccessibleAction::keyBinding` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Properties: `AccessKey: <value>` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | `atk_action_get_keybinding` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXAccessKey: <value>` |
| Comments |  |

#### 3.6.5 `action`

|  |  |
| --- | --- |
| HTML Specification | `action` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-action) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.6 `allow`

|  |  |
| --- | --- |
| HTML Specification | `allow` |
| Element(s) | [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-allow) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.7 `allowfullscreen`

|  |  |
| --- | --- |
| HTML Specification | `allowfullscreen` |
| Element(s) | [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-allowfullscreen) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.8 `alt`

|  |  |
| --- | --- |
| HTML Specification | `alt` |
| Element(s) | [`area`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-alt); [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-alt); [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-alt) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Used for [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name), exposed via [`accName`](https://msdn.microsoft.com/en-us/library/system.windows.automation.automationelement.automationelementinformation.name.aspx) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Properties: [`Name`](https://msdn.microsoft.com/en-us/library/system.windows.automation.automationelement.automationelementinformation.name.aspx) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Used for [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name), exposed via `atk_object_get_name` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXDescription: <value>` |
| Comments |  |

#### 3.6.9 `as`

|  |  |
| --- | --- |
| HTML Specification | `as` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-as) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.10 `async`

|  |  |
| --- | --- |
| HTML Specification | `async` |
| Element(s) | [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-async) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.11 `autocapitalize`

|  |  |
| --- | --- |
| HTML Specification | `autocapitalize` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocapitalize) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.12 `autocomplete`

|  |  |
| --- | --- |
| HTML Specification | `autocomplete` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/forms.html#attr-form-autocomplete) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Note  **Note:** the `aria-autocomplete` attribute and the HTML `autocomplete` attribute have disparate features. The `aria-autocomplete` attribute is not supported on the HTML `form` element or elements with an explicit ARIA `form` role.  Note  When used on a `form` element, the `autocomplete` attribute identifies whether form controls owned by the form will have their [autofill field name](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill-field-name) set to "`on`" or "`off`" by default. See [`autocomplete` for `input`, `select`, `textarea`](#att-autocomplete) for control mappings. |

#### 3.6.13 `autocomplete`

|  |  |
| --- | --- |
| HTML Specification | `autocomplete` |
| Element(s) | [`input`, `select` and `textarea`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-autocomplete) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If specified `autocomplete=off` or the control is owned by a `form` with `autocomplete=off` - [`aria-autocomplete=none`](https://www.w3.org/TR/core-aam-1.2/#ariaAutocompleteNone)  Otherwise, [`aria-autocomplete`](https://www.w3.org/TR/core-aam-1.2/#ariaAutocompleteInlineListBoth)  Note  **Note:** the `aria-autocomplete` attribute and the HTML `autocomplete` attribute have disparate features, but they overlap as mechanisms for user agents to expose the control's support for autocompletion. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If the form control has been specified as both `autocomplete=off` (whether due to explicit use of the attribute, or from inheriting the `off` state from a parent `form` element with `autocomplete=off`) and with an `aria-autocomplete` attribute with a valid value, user agents *MUST* expose only the `aria-autocomplete` attribute value.  Otherwise, if the form control has an `autocomplete` attribute specified with a valid token value, and an `aria-autocomplete` attribute, then user agents *MUST* expose only the `autocomplete` attribute value. |

#### 3.6.14 `autofocus`

|  |  |
| --- | --- |
| HTML Specification | `autofocus` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#attr-fe-autofocus) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Provides a [minimum role](termref) of [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group). |

#### 3.6.15 `autoplay`

|  |  |
| --- | --- |
| HTML Specification | `autoplay` |
| Element(s) | [`audio` and `video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-autoplay) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.16 `blocking`

|  |  |
| --- | --- |
| HTML Specification | `blocking` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-blocking); [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-defer); [`style`](https://html.spec.whatwg.org/multipage/semantics.html#attr-style-media) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.17 `charset`

|  |  |
| --- | --- |
| HTML Specification | `charset` |
| Element(s) | [`meta`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-charset) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.18 `checked` (if present)

|  |  |
| --- | --- |
| HTML Specification | `checked` (if present) |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-checked) `type=checkbox` or `type=radio` |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-checked`](https://www.w3.org/TR/core-aam-1.2/#ariaCheckedTrue)="true" |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Property: `Toggle.ToggleState: On (1)` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXValue: 1` |
| Comments | If an `input` element in the `checkbox` or `radio` state includes both the `checked` attribute and the `aria-checked` attribute with a valid value, User Agents *MUST* expose only the `checked` attribute value. |

#### 3.6.19 `checked` (if absent)

|  |  |
| --- | --- |
| HTML Specification | `checked` (if absent) |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-checked) `type=checkbox` or `type=radio` |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-checked`](https://www.w3.org/TR/core-aam-1.2/#ariaCheckedFalse)="false" |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Property: `Toggle.ToggleState: Off (0)` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXValue: 0` |
| Comments | An `input` element in the `checkbox` or `radio` state without a `checked` attribute has an implicit "false" state. User Agents *MUST* ignore an `aria-checked` attribute which conflicts with the native element's implicit checked state. |

#### 3.6.20 `cite`

|  |  |
| --- | --- |
| HTML Specification | `cite` |
| Element(s) | [`blockquote`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-blockquote-cite); [`del` and `ins`](https://html.spec.whatwg.org/multipage/edits.html#attr-mod-cite); [`q`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-q-cite) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXURL: <value>` |
| Comments |  |

#### 3.6.21 `class`

|  |  |
| --- | --- |
| HTML Specification | `class` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#classes) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: `class: <value>` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Property: `UIA_ClassNamePropertyId` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: `class: <value>` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Property: `AXDOMClassList` |
| Comments |  |

#### 3.6.22 `color`

|  |  |
| --- | --- |
| HTML Specification | `color` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-color) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.23 `cols`

|  |  |
| --- | --- |
| HTML Specification | `cols` |
| Element(s) | [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-cols) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXRangeForLine: <value>` |
| Comments | Not mapped |

#### 3.6.24 `colspan`

|  |  |
| --- | --- |
| HTML Specification | `colspan` |
| Element(s) | [`td` and `th`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-colspan) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-colspan`](https://www.w3.org/TR/core-aam-1.2/#ariaColSpan) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.25 `command` (in the Toggle, Show, and Hide popover states)

|  |  |
| --- | --- |
| HTML Specification | `command` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/button.html#attr-input-command) (`command` in the [Toggle popover state](https://html.spec.whatwg.org/multipage/input.html#attr-button-command-toggle-popover-state) [Show popover state](https://html.spec.whatwg.org/multipage/input.html#attr-button-command-show-popover-state) and [Hide popover state](https://html.spec.whatwg.org/multipage/input.html#attr-button-command-hide-popover-state)) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If the associated element is displayed as a popover: [`aria-expanded=true`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedTrue)  If the associated element is hidden: [`aria-expanded=false`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedFalse)  If the associated element is an accessibility ancestor of the element with the `command` attribute or is not present in the DOM: [`aria-expanded=undefined`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedUndefined)  If the associated element is not a valid `popover` element: no `aria-expanded` mapping. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Object attributes: `details-roles:popover` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | Use WAI-ARIA mapping  Object attributes: `details-roles:popover` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User Agents *MUST* expose an [`aria-details`](https://www.w3.org/TR/core-aam-1.2/#ariaDetails) relationship with the associated element (identified via the specified `commandfor` attribute) **except** under the following conditions:   - The associated popover element is the next immediate accessibility sibling to the invoking element, - The element is a descendant of the `popover` it is associated with.   Note  A button that represents a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button) or is in the [reset state](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)) with a [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) cannot invoke a command. |

#### 3.6.26 `command` (in the Close and Show Modal states)

|  |  |
| --- | --- |
| HTML Specification | `command` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/button.html#attr-input-command) (`command` in the [Close state](https://html.spec.whatwg.org/multipage/input.html#attr-button-command-close-state)) and [Show Modal state](https://html.spec.whatwg.org/multipage/input.html#attr-button-command-show-modal-state)) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | A `command` attribute in the `close` and `show-modal` states provide no additional accessibility mappings to the `button` element. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Note  A button that represents a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button) or is in the [reset state](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)) with a [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) cannot invoke a command. |

#### 3.6.27 `commandfor`

|  |  |
| --- | --- |
| HTML Specification | `commandfor` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/button.html#attr-input-commandfor) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | See comments |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | See comments |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | See comments |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | See comments |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | See comments |
| Comments | The `commandfor` attribute identifies the associated element for the `button` element.  The specified `command` state will determine if a relationship mapping needs to be exposed between the `button` and its programmatically associated element. |

#### 3.6.28 `content`

|  |  |
| --- | --- |
| HTML Specification | `content` |
| Element(s) | [`meta`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-content) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.29 `contenteditable`

|  |  |
| --- | --- |
| HTML Specification | `contenteditable` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#attr-contenteditable) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | If the element is in the editable state, the following mappings apply to the element and every nested accessible object with the exception of those which have been specified in the `false` state.  States: `IA2_STATE_EDITABLE` and `IA2_STATE_MULTI_LINE`  Interfaces: `IAccessibleEditableText`  If the element is in the `false` state: not mapped.  If the element is in the `inherit` state: match the editable state of its parent element. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | If the element is in the editable state, the following mappings apply to the element and every nested accessible object with the exception of those which have been specified in the `false` state.  Control Pattern: `TextEdit`  Property: `AriaProperties.multiline:true`  If the element is in the `false` state: not mapped.  If the element is in the `inherit` state: match the editable state of its parent element. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | If the element is in the editable state, the following mappings apply to the element and every nested accessible object with the exception of those which have been specified in the `false` state.  States: `ATK_STATE_EDITABLE` and `ATK_STATE_MULTI_LINE`  Interfaces: `AtkEditableText`  If the element is in the `false` state: not mapped.  If the element is in the `inherit` state: match the editable state of its parent element. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Role: [AXTextArea](#el-textarea) Use WAI-ARIA mapping |
| Comments | If the element is set to `contenteditable` and `aria-readonly="true"`, User Agents *MUST* expose only the `contenteditable` state. |

#### 3.6.30 `controls`

|  |  |
| --- | --- |
| HTML Specification | `controls` |
| Element(s) | [`audio` and `video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-controls) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Controls exposed as `AXToolbar` |
| Comments |  |

#### 3.6.31 `coords`

|  |  |
| --- | --- |
| HTML Specification | `coords` |
| Element(s) | [`area`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-coords) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Defines an accessible object's dimensions (`IAccessible::accLocation`) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Defines an accessible object's dimensions (`BoundingRectangle`) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Defines an accessible object's dimensions, exposed via `atk_component_get_position` and `atk_component_get_size` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Defines an accessible object's dimensions, exposed via `Frame` property |
| Comments |  |

#### 3.6.32 `crossorigin`

|  |  |
| --- | --- |
| HTML Specification | `crossorigin` |
| Element(s) | [`audio`](https://html.spec.whatwg.org/multipage/media.html#attr-media-crossorigin); [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-crossorigin); [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-crossorigin); [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-crossorigin); [`video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-crossorigin) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.33 `data`

|  |  |
| --- | --- |
| HTML Specification | `data` |
| Element(s) | [`object`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-object-data) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.34 `datetime`

|  |  |
| --- | --- |
| HTML Specification | `datetime` |
| Element(s) | [`del` and `ins`](https://html.spec.whatwg.org/multipage/edits.html#attr-mod-datetime) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: `datetime: <value>` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: `datetime: <value>` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXDateTimeValue: <value>` |
| Comments |  |

#### 3.6.35 `datetime`

|  |  |
| --- | --- |
| HTML Specification | `datetime` |
| Element(s) | [`time`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-time-datetime) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: `datetime: <value>` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Properties: `FullDescription: <value>` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: `datetime: <value>` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXDateTimeValue: <value>` |
| Comments |  |

#### 3.6.36 `decoding`

|  |  |
| --- | --- |
| HTML Specification | `decoding` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-decoding) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.37 `default`

|  |  |
| --- | --- |
| HTML Specification | `default` |
| Element(s) | [`track`](https://html.spec.whatwg.org/multipage/media.html#attr-track-default) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.38 `defer`

|  |  |
| --- | --- |
| HTML Specification | `defer` |
| Element(s) | [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-defer) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.39 `dir`

|  |  |
| --- | --- |
| HTML Specification | `dir` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as "writing-mode" text attribute on the text container. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Exposed by `TextFlowDirections` attribute of the `TextRange` Control Pattern implemented on a parent accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as "writing-mode" text attribute on the text container. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.40 `dir`

|  |  |
| --- | --- |
| HTML Specification | `dir` |
| Element(s) | [`bdo`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as "writing-mode" text attribute on the text container. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Exposed by `TextFlowDirections` attribute of the `TextRange` Control Pattern implemented on a parent accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as "writing-mode" text attribute on the text container. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.41 `dirname`

|  |  |
| --- | --- |
| HTML Specification | `dirname` |
| Element(s) | [`input` and `textarea`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-dirname) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.42 `disabled`

|  |  |
| --- | --- |
| HTML Specification | `disabled` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-disabled); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-disabled); [`optgroup`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-optgroup-disabled); [`option`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-disabled); [`select`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-disabled); [`textarea`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-disabled); [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-disabled="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaDisabledTrue) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If the element has both the `disabled` attribute and the `aria-disabled` attribute with a valid value, User Agents *MUST* expose only the `disabled` attribute value. |

#### 3.6.43 `disabled`

|  |  |
| --- | --- |
| HTML Specification | `disabled` |
| Element(s) | [`fieldset`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-fieldset-disabled) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-disabled="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaDisabledTrue) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | Form controls within a valid `legend` child element of a `fieldset` with a `disabled` attribute do not become disabled.  If the element has both the `disabled` attribute and the `aria-disabled` attribute with a valid value, User Agents *MUST* expose only the `disabled` attribute value. |

#### 3.6.44 `disabled`

|  |  |
| --- | --- |
| HTML Specification | `disabled` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#the-link-element) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.45 `download`

|  |  |
| --- | --- |
| HTML Specification | `download` |
| Element(s) | [`a` and `area`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-download) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.46 `draggable`

|  |  |
| --- | --- |
| HTML Specification | `draggable` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dnd.html#the-draggable-attribute) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: draggable:true |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: draggable:true |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Provides a [minimum role](termref) of [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group). |

#### 3.6.47 `enctype`

|  |  |
| --- | --- |
| HTML Specification | `enctype` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-enctype) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.48 `enterkeyhint`

|  |  |
| --- | --- |
| HTML Specification | `enterkeyhint` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#attr-enterkeyhint) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Modifies the action label (or icon) to present for the `enter` key on virtual keyboards. |

#### 3.6.49 `fetchpriority`

|  |  |
| --- | --- |
| HTML Specification | `fetchpriority` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-fetchpriority); [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-fetchpriority); [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-fetchpriority) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.50 `for`

|  |  |
| --- | --- |
| HTML Specification | `for` |
| Element(s) | [`label`](https://html.spec.whatwg.org/multipage/forms.html#attr-label-for) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Used for [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name)  Relations:  `IA2_RELATION_LABEL_FOR` and `IA2_RELATION_LABEL_BY` relations between [`label`](#el-label) and referred [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Used for [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name)  When the `label` element has a `for` attribute referencing another [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label), the `LabeledBy` property for the referenced element points to the UIA element for the `label` element. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Used for [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name)  Relations:  `ATK_RELATION_LABEL_FOR` and `ATK_RELATION_LABEL_BY` relations between [`label`](#el-label) and referred [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Used for [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) |
| Comments |  |

#### 3.6.51 `for`

|  |  |
| --- | --- |
| HTML Specification | `for` |
| Element(s) | [`output`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-output-for) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Relations:  `IA2_RELATION_CONTROLLED_BY` with an element pointed by the attribute. Paired element exposes `IA2_RELATION_CONTROLLER_FOR` relation. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Relations:  `ATK_RELATION_CONTROLLED_BY` with an element pointed by the attribute. Paired element exposes `ATK_RELATION_CONTROLLER_FOR` relation. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.52 `form`

|  |  |
| --- | --- |
| HTML Specification | `form` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`fieldset`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`label`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`object`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`output`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`select`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [`textarea`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fae-form); [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.53 `formaction`

|  |  |
| --- | --- |
| HTML Specification | `formaction` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formaction); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formaction) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.54 `formenctype`

|  |  |
| --- | --- |
| HTML Specification | `formenctype` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formenctype); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formenctype) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.55 `formmethod`

|  |  |
| --- | --- |
| HTML Specification | `formmethod` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formmethod); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formmethod) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.56 `formnovalidate`

|  |  |
| --- | --- |
| HTML Specification | `formnovalidate` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formnovalidate); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formnovalidate) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.57 `formtarget`

|  |  |
| --- | --- |
| HTML Specification | `formtarget` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formtarget); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-formtarget) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.58 `headers`

|  |  |
| --- | --- |
| HTML Specification | `headers` |
| Element(s) | [`td`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-headers); [`th`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-headers) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Links the cell to its header cells. Exposed via `IAccessibleTableCell::rowHeaderCells` and `IAccessibleTableCell::columnHeaderCells`. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Links the cell to its header cells. Exposed via `Table.ItemColumnHeaderItems` and `Table.ItemRowHeaderItems`. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Links the cell to its row and [column header](https://html.spec.whatwg.org/multipage/tables.html#column-header) cells (note, only one row and one column header cells can be exposed because of API restrictions). See `atk_table_get_row_header` and `atk_table_get_column_header`. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Expose via `AXColumnHeaderUIElements` and `AXRowHeaderUIElements` |
| Comments |  |

#### 3.6.59 `height`

|  |  |
| --- | --- |
| HTML Specification | `height` |
| Element(s) | [`canvas`](https://html.spec.whatwg.org/multipage/canvas.html#attr-canvas-height); [`embed`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height); [`iframe`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height); [`img`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height); [`input`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height); [`object`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height); [`source` (in `picture`)](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height); [`video`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-height) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Defines an accessible object's height (`IAccessible::accLocation`) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Defines an accessible object's height (`BoundingRectangle`) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Defines an accessible object's height (`atk_component_get_size`) |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Defines an accessible object's height (`AXSize` property) |
| Comments |  |

#### 3.6.60 `hidden`

|  |  |
| --- | --- |
| HTML Specification | [`hidden`](https://html.spec.whatwg.org/multipage/interaction.html#the-hidden-attribute) |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-hidden="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaHiddenTrue) if the element retains its user agent default styling of `display: none`. Otherwise, if no other method for hiding the content is used (e.g., `visibility: hidden`) then it is not mapped. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.61 `high`

|  |  |
| --- | --- |
| HTML Specification | `high` |
| Element(s) | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-high) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `RangeValue.Maximum` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.62 `href`

|  |  |
| --- | --- |
| HTML Specification | [`href`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-href) |
| Element(s) | `a`; `area` |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Creates a link accessible object. For details, refer to [`a`](#el-a) and [`area`](#el-area) element mappings. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Creates a link accessible object. For details, refer to [`a`](#el-a) and [`area`](#el-area) element mappings. The value of the `href` attribute is stored in the `Value.Value` UIA property. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Creates a link accessible object. For details, refer to [`a`](#el-a) and [`area`](#el-area) element mappings. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXURL: <value>` |
| Comments |  |

#### 3.6.63 `href`

|  |  |
| --- | --- |
| HTML Specification | `href` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-href) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.64 `hreflang`

|  |  |
| --- | --- |
| HTML Specification | `hreflang` |
| Element(s) | [`a`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-hreflang); [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-hreflang) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.65 `http-equiv`

|  |  |
| --- | --- |
| HTML Specification | `http-equiv` |
| Element(s) | [`meta`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-http-equiv) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.66 `id`

|  |  |
| --- | --- |
| HTML Specification | `id` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: `id: <value>` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Property: `UIA_AutomationIdPropertyId` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: `id: <value>` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Property: `AXDOMIdentifier` |
| Comments |  |

#### 3.6.67 `inert`

|  |  |
| --- | --- |
| HTML Specification | `inert` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not Mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | See comments |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | See comments |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | See comments |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | See comments |
| Comments | Nodes that are [inert](https://html.spec.whatwg.org/multipage/interaction.html#inert) are not exposed to an accessibility API.  Note  Note: an inert node can have descendants that are not inert. For example, a [modal dialog](https://html.spec.whatwg.org/multipage/interaction.html#modal-dialogs-and-inert-subtrees) can escape an inert subtree. |

#### 3.6.68 `indeterminate [IDL]`

|  |  |
| --- | --- |
| HTML Specification | `indeterminate [IDL]` |
| Element(s) | HTML elements; [`input`](https://html.spec.whatwg.org/multipage/input.html#dom-input-indeterminate) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-checked`](https://www.w3.org/TR/core-aam-1.2/#ariaCheckedTrue) (state)="mixed" |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If the element has the `indeterminate [IDL]` set and the `aria-checked` attribute set, User Agents *MUST* expose only the `indeterminate [IDL]` state. |

#### 3.6.69 `ismap`

|  |  |
| --- | --- |
| HTML Specification | `ismap` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-ismap) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.70 `itemid`

|  |  |
| --- | --- |
| HTML Specification | `itemid` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemid) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.71 `itemprop`

|  |  |
| --- | --- |
| HTML Specification | `itemprop` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemprop) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.72 `itemref`

|  |  |
| --- | --- |
| HTML Specification | `itemref` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemref) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.73 `itemscope`

|  |  |
| --- | --- |
| HTML Specification | `itemscope` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemscope) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.74 `itemtype`

|  |  |
| --- | --- |
| HTML Specification | `itemtype` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/microdata.html#attr-itemtype) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.75 `kind`

|  |  |
| --- | --- |
| HTML Specification | `kind` |
| Element(s) | [`track`](https://html.spec.whatwg.org/multipage/media.html#attr-track-kind) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.76 `label`

|  |  |
| --- | --- |
| HTML Specification | `label` |
| Element(s) | [`optgroup`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-optgroup-label); [`option`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-label); [`track`](https://html.spec.whatwg.org/multipage/media.html#attr-track-label) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Associates the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | The target element of the `label` attribute has a `LabeledBy` property pointing to the element with the `label` attribute. Participates in [name computation.](#accname-computation) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Associates the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXTitle`: `<value>` |
| Comments | See Also: [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/) |

#### 3.6.77 `lang`

|  |  |
| --- | --- |
| HTML Specification | `lang` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#attr-lang) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as "language" text attribute on the text container |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | The value of the `lang` attribute is exposed as a locale identifier by `Culture` property of the UIA element representing the HTML element, and by `Culture` attribute of the `TextRange` Control Pattern implemented on a parent accessible object. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as "language" text attribute on the text container |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXLanguage: <value>` |
| Comments |  |

#### 3.6.78 `list`

|  |  |
| --- | --- |
| HTML Specification | `list` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-list) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-controls`](https://www.w3.org/TR/core-aam-1.2/#ariaControls) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | `IA2_RELATION_CONTROLLER_FOR` point to the `datalist` element referred to by the IDREF value of the `list` attribute. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `ControllerFor` point to the `datalist` element referred to by the IDREF value of the `list` attribute. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | `ATK_RELATION_CONTROLLER_FOR` point to the `datalist` element referred to by the IDREF value of the `list` attribute. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Property: `AXLinkedUIElements`: point to the `datalist` element referred to by the IDREF value of the `list` attribute. |
| Comments | Refer to [`datalist`](#el-datalist) and [`input`](#el-input-textetc-autocomplete) element mappings. |

#### 3.6.79 `loop`

|  |  |
| --- | --- |
| HTML Specification | `loop` |
| Element(s) | [`audio`](https://html.spec.whatwg.org/multipage/media.html#attr-media-loop); [`video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-loop) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.80 `low`

|  |  |
| --- | --- |
| HTML Specification | `low` |
| Element(s) | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-low) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `RangeValue.Minimum` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.81 `max`

|  |  |
| --- | --- |
| HTML Specification | `max` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-max) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuemax`](https://www.w3.org/TR/core-aam-1.2/#ariaValueMax) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as `IAccessibleValue::maximumValue` if the element implements the interface |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `RangeValue.Maximum` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as `atk_value_get_maximum_value` if the element implements the `AtkValue` interface |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXMaxValue: <value>` |
| Comments |  |

#### 3.6.82 `max`

|  |  |
| --- | --- |
| HTML Specification | `max` |
| Element(s) | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-max); [`progress`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-progress-max) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuemax`](https://www.w3.org/TR/core-aam-1.2/#ariaValueMax) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as `IAccessibleValue::maximumValue` if the element implements the interface |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `RangeValue.Maximum` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as `atk_value_get_maximum_value` if the element implements the `AtkValue` interface |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXMaxValue: <value>` |
| Comments |  |

#### 3.6.83 `maxlength`

|  |  |
| --- | --- |
| HTML Specification | `maxlength` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-maxlength); [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-maxlength) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.84 `media`

|  |  |
| --- | --- |
| HTML Specification | `media` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-media); [`meta`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-media); [`source` (in `picture`)](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-source-media); [`style`](https://html.spec.whatwg.org/multipage/semantics.html#attr-style-media) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.85 `method`

|  |  |
| --- | --- |
| HTML Specification | `method` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-method) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.86 `min`

|  |  |
| --- | --- |
| HTML Specification | `min` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-min) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuemin`](https://www.w3.org/TR/core-aam-1.2/#ariaValueMin) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as `IAccessibleValue::minimumValue` if the element implements the interface |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `RangeValue.Minimum` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as `atk_value_get_minimum_value` if the element implements the `AtkValue` interface |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXMinValue: <value>` |
| Comments |  |

#### 3.6.87 `min`

|  |  |
| --- | --- |
| HTML Specification | `min` |
| Element(s) | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-min) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuemin`](https://www.w3.org/TR/core-aam-1.2/#ariaValueMin) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as `IAccessibleValue::minimumValue` if the element implements the interface |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | `RangeValue.Minimum` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as `atk_value_get_minimum_value` if the element implements the `AtkValue` interface |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXMinValue: <value>` |
| Comments |  |

#### 3.6.88 `minlength`

|  |  |
| --- | --- |
| HTML Specification | `minlength` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-minlength); [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-minlength) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | States: `IA2_STATE_INVALID_ENTRY` if value doesn't meet the designated minimum length value. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | States: `IsDataValidForForm` if value doesn't meet the designated minimum length value. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | States: `ATK_STATE_INVALID_ENTRY` if value doesn't meet the designated minimum length value. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Property: `AXInvalid`: `true` if value doesn't meet the designated minimum length value. |
| Comments |  |

#### 3.6.89 `multiple`

|  |  |
| --- | --- |
| HTML Specification | `multiple` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-multiple) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.90 `multiple`

|  |  |
| --- | --- |
| HTML Specification | `multiple` |
| Element(s) | [`select`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-multiple) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-multiselectable="true"`](https://www.w3.org/TR/wai-aria-1.2/#aria-multiselectable) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.91 `muted`

|  |  |
| --- | --- |
| HTML Specification | `muted` |
| Element(s) | [`audio`](https://html.spec.whatwg.org/multipage/media.html#attr-media-muted); [`video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-muted) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.92 `name`

|  |  |
| --- | --- |
| HTML Specification | `name` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name); [`fieldset`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name); [`input`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name); [`output`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name); [`select`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name); [`textarea`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name); [form-associated custom element](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.93 `name`

|  |  |
| --- | --- |
| HTML Specification | `name` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/forms.html#attr-form-name) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.94 `name`

|  |  |
| --- | --- |
| HTML Specification | `name` |
| Element(s) | [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-name); [`object`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-object-name) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.95 `name`

|  |  |
| --- | --- |
| HTML Specification | `name` |
| Element(s) | [`map`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-map-name) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.96 `name`

|  |  |
| --- | --- |
| HTML Specification | `name` |
| Element(s) | [`meta`](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-name) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.97 `name`

|  |  |
| --- | --- |
| HTML Specification | `name` |
| Element(s) | [`slot`](https://html.spec.whatwg.org/multipage/scripting.html#attr-slot-name) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.98 `nomodule`

|  |  |
| --- | --- |
| HTML Specification | `nomodule` |
| Element(s) | [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-nomodule) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.99 `nonce`

|  |  |
| --- | --- |
| HTML Specification | `nonce` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-nonce) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.100 `novalidate`

|  |  |
| --- | --- |
| HTML Specification | `novalidate` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-novalidate) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.101 `open`

|  |  |
| --- | --- |
| HTML Specification | `open` |
| Element(s) | [`details`](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-details-open) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-expanded`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedTrue)="true | false" |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | `STATE_SYSTEM_EXPANDED` `STATE_SYSTEM_COLLAPSED` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | [`ExpandCollapsePattern`](https://msdn.microsoft.com/en-us/library/system.windows.automation.expandcollapsepattern.aspx) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | States:  `ATK_STATE_COLLAPSED` or `ATK_STATE_EXPANDED` depending on the attribute value |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXExpanded: YES|NO` |
| Comments | Set properties on the [`summary`](#el-summary) element. |

#### 3.6.102 `open`

|  |  |
| --- | --- |
| HTML Specification | `open` |
| Element(s) | [`dialog`](https://html.spec.whatwg.org/multipage/interactive-elements.html#attr-dialog-open) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If the `open` attribute is set via the `showModal()` method then [`aria-modal="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaModalTrue) and [`aria-hidden="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaHiddenFalse).  Otherwise, if the `open` attribute is set via the `show()` method, or explicitly specified by an author, then [`aria-modal="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaModalFalse) and [`aria-hidden="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaHiddenFalse). |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | The `open` attribute's value is irrelevant. When the `open` attribute is not specified the default user agent styling for a `dialog` is `display: none`.  Authors can reveal a `dialog` through the style layer by modifying its `display` property. If revealed this way then the `dialog` is [`aria-modal="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaModalFalse) and [`aria-hidden="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaHiddenFalse). |

#### 3.6.103 `optimum`

|  |  |
| --- | --- |
| HTML Specification | `optimum` |
| Element(s) | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-optimum) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.104 `pattern`

|  |  |
| --- | --- |
| HTML Specification | `pattern` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-pattern) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If the value doesn't match the pattern: [`aria-invalid="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaInvalidTrue); Otherwise, [`aria-invalid="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaInvalidFalse) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.105 `ping`

|  |  |
| --- | --- |
| HTML Specification | `ping` |
| Element(s) | [`a` and `area`](https://html.spec.whatwg.org/multipage/links.html#ping) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.106 `placeholder`

|  |  |
| --- | --- |
| HTML Specification | `placeholder` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-placeholder); [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-placeholder) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-placeholder`](https://www.w3.org/TR/core-aam-1.2/#ariaPlaceholder) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | When the `placeholder` and `aria-placeholder` attributes are both present, and the `placeholder` attribute's value is non-empty, user agents *MUST* expose the value of the `placeholder` attribute, and ignore `aria-placeholder`. If the `placeholder` attribute's value is empty, then user agents *MUST* expose the value of the `aria-placeholder` attribute. |

#### 3.6.107 `playsinline`

|  |  |
| --- | --- |
| HTML Specification | `playsinline` |
| Element(s) | [`video`](https://html.spec.whatwg.org/multipage/media.html#attr-video-playsinline) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.108 `popover`

|  |  |
| --- | --- |
| HTML Specification | `popover` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/popover.html#attr-popover) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Relations: `IA2_RELATION_DETAILS_FOR` points to invoking element. [See Comments](#att-popover-comments). Object attributes: `ispopup: <value>` where `<value>` reflects the [popover](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute) type. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | A details relation is made with the invoking element, if an invoking element exists which meets the conditions for necessitating a details relationship. [See Comments](#att-popover-comments). |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Relations: `RELATION_DETAILS_FOR` points to invoking element. [See Comments](#att-popover-comments).  Object attributes: `ispopup: <value>` where `<value>` reflects the [popover](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute) type. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | TBD |
| Comments | User agents *MUST NOT* expose a details relation between a `popover` and its invoking element under the following conditions:   - when the `popover` is the next immediate accessibility sibling to the invoking element, - when the element has a `popovertargetaction=hide` attribute value, - or when the element is a descendant of the `popover` and its `popovertarget` is the "`auto`" state.   If specified on an element with an implicit role of `generic`, then the element's role instead maps to [`group`](https://www.w3.org/TR/core-aam-1.2/#role-map-group) for all [`popover` states](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute).  Note  There are no unique mappings for the different `popover` states. Any accessibility mapping changes for the popover element would be the responsibility of the author. e.g., using different base HTML elements, attributes, or ARIA attributes to make such changes. |

#### 3.6.109 `popovertarget`

|  |  |
| --- | --- |
| HTML Specification | `popovertarget` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertarget); [`input type=button, image, reset, submit`](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertarget) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If the associated element is displayed as a popover: [`aria-expanded=true`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedTrue)  If the associated element is hidden: [`aria-expanded=false`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedFalse)  If the associated element is an accessibility ancestor of the element with the `command` attribute or is not present in the DOM: [`aria-expanded=undefined`](https://www.w3.org/TR/core-aam-1.2/#ariaExpandedUndefined)  If the associated element is not a valid `popover` element: no `aria-expanded` mapping. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping  Object attributes: `details-roles:popover` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping  Object attributes: `details-roles:popover` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User Agents *MUST* expose an [`aria-details`](https://www.w3.org/TR/core-aam-1.2/#ariaDetails) relation with the associated popover element **except** under the following conditions:   - The element's `popovertargetaction` attribute value is "`hide`" - The associated popover element is the next immediate accessibility sibling to the invoking element, - The element's implicit or explicit `popovertargetaction` is the "`auto`" state and the element is a descendant of the `popover` it is associated with.   Note  A button that represents a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button) with a [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) cannot invoke a popover. |

#### 3.6.110 `popovertargetaction`

|  |  |
| --- | --- |
| HTML Specification | `popovertargetaction` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction); [`input type=button, image, reset, submit`](https://html.spec.whatwg.org/multipage/popover.html#attr-popovertargetaction) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | The value of this attribute can impact the mappings of its related [`popovertarget`](#att-popovertarget) attribute. |

#### 3.6.111 `poster`

|  |  |
| --- | --- |
| HTML Specification | `poster` |
| Element(s) | [`video`](https://html.spec.whatwg.org/multipage/media.html#attr-video-poster) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.112 `preload`

|  |  |
| --- | --- |
| HTML Specification | `preload` |
| Element(s) | [`audio` and `video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-preload) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.113 `readonly`

|  |  |
| --- | --- |
| HTML Specification | `readonly` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-readonly); [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-readonly); [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#attr-face-readonly) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-readonly="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaReadonlyTrue) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If the element includes both the `readonly` attribute and the `aria-readonly` attribute with a valid value, User Agents *MUST* expose only the `readonly` attribute value. |

#### 3.6.114 `referrerpolicy`

|  |  |
| --- | --- |
| HTML Specification | `referrerpolicy` |
| Element(s) | [`a`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-referrerpolicy); [`area`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-referrerpolicy); [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-referrerpolicy); [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-referrerpolicy); [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-referrerpolicy); [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-referrerpolicy) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.115 `rel`

|  |  |
| --- | --- |
| HTML Specification | `rel` |
| Element(s) | [`a`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-rel); [`area`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-rel); [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-rel) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.116 `required`

|  |  |
| --- | --- |
| HTML Specification | `required` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-required); [`select`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-required); [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-required) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-required`](https://www.w3.org/TR/core-aam-1.2/#ariaRequiredTrue) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If the element includes both the `required` attribute and the `aria-required` attribute with a valid value, User Agents *MUST* expose only the `required` attribute value.  If an element is [required](https://html.spec.whatwg.org/multipage/input.html#concept-input-required), user agents *MUST NOT* expose the element with an intitial invalid state ([`aria-invalid="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaInvalidTrue)). The user agent *SHOULD* expose the invalid state only after **1)** a user has purposefully interacted with a required element, or attempted to submit a form and **2)** the element, or elements, do not meet [constraint validation](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#constraint-validation).  Until these conditions are met, user agents *MUST* expose the elements as ([`aria-invalid="false"`](https://www.w3.org/TR/core-aam-1.2/#ariaInvalidFalse)). |

#### 3.6.117 `reversed`

|  |  |
| --- | --- |
| HTML Specification | `reversed` |
| Element(s) | [`ol`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-ol-reversed) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Reverses the numerical or alphabetical order of the child list item markers. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Reverses the numerical or alphabetical order of the child list item markers. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Reverses the numerical or alphabetical order of the child list item markers. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Reverses the numerical or alphabetical order of the child list item markers. |
| Comments |  |

#### 3.6.118 `rows`

|  |  |
| --- | --- |
| HTML Specification | `rows` |
| Element(s) | [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-rows) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.119 `rowspan`

|  |  |
| --- | --- |
| HTML Specification | `rowspan` |
| Element(s) | [`td`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-rowspan); [`th`](https://html.spec.whatwg.org/multipage/tables.html#attr-tdth-rowspan) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-rowspan`](https://www.w3.org/TR/core-aam-1.2/#ariaRowSpan) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.120 `sandbox`

|  |  |
| --- | --- |
| HTML Specification | `sandbox` |
| Element(s) | [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.121 `scope`

|  |  |
| --- | --- |
| HTML Specification | `scope` |
| Element(s) | [`th`](https://html.spec.whatwg.org/multipage/tables.html#attr-th-scope) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | If `scope="row"` then map `th` to [`rowheader`](https://www.w3.org/TR/core-aam-1.2/#role-map-columnheader)  If `scope="col"` then map `th` to [`columnheader`](https://www.w3.org/TR/core-aam-1.2/#role-map-columnheader) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.122 `selected`

|  |  |
| --- | --- |
| HTML Specification | `selected` |
| Element(s) | [`option`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-selected) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-selected="true"`](https://www.w3.org/TR/core-aam-1.2/#ariaSelectedTrue) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | If the element includes both the `selected` attribute and the `aria-selected` attribute with a valid value, User Agents *MUST* expose only the `selected` attribute value. |

#### 3.6.123 `shape`

|  |  |
| --- | --- |
| HTML Specification | `shape` |
| Element(s) | [`area`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.124 `size`

|  |  |
| --- | --- |
| HTML Specification | `size` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-size); [`select`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-select-size) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped for `input` elements.  If greater than 1, then creates a listbox accessible object. Refer to [`select`](#el-select-listbox) element for details. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped for `input` elements.  For `select` element use WAI-ARIA mapping. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped for `input` elements.  For `select` element use WAI-ARIA mapping. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped for `input` elements.  For `select` element use WAI-ARIA mapping. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped for `input` elements.  For `select` element use WAI-ARIA mapping. |
| Comments | For `input` elements that allow the `size` attribute, the attribute will modify their default width. A width provided by CSS will negate the effects of the `size` attribute on these `input` elements. |

#### 3.6.125 `sizes`

|  |  |
| --- | --- |
| HTML Specification | `sizes` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-sizes) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.126 `sizes`

|  |  |
| --- | --- |
| HTML Specification | `sizes` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-sizes); [`source`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-source-sizes) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.127 `slot`

|  |  |
| --- | --- |
| HTML Specification | `slot` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#attr-slot) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.128 `span`

|  |  |
| --- | --- |
| HTML Specification | `span` |
| Element(s) | [`col`](https://html.spec.whatwg.org/multipage/tables.html#attr-col-span); [`colgroup`](https://html.spec.whatwg.org/multipage/tables.html#attr-colgroup-span) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as `IAccessibleTableCell::columnExtent` on all cells at the column |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Exposed as `GridItem.ColumnSpan` on all cells at the column |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed via `atk_table_get_column_extent_at` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXColumnIndexRange.length: <value>` |
| Comments |  |

#### 3.6.129 `spellcheck`

|  |  |
| --- | --- |
| HTML Specification | `spellcheck` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#attr-spellcheck) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-invalid="spelling"` or `grammar`](https://www.w3.org/TR/core-aam-1.2/#ariaInvalidSpellingGrammar) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.130 `src`

|  |  |
| --- | --- |
| HTML Specification | `src` |
| Element(s) | [`audio`](https://html.spec.whatwg.org/multipage/media.html#attr-media-src); [`embed`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-embed-src); [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-src); [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-src); [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-src); [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-src); [`source` (in `audio` or `video`)](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-source-src); [`track`](https://html.spec.whatwg.org/multipage/media.html#attr-track-src); [`video`](https://html.spec.whatwg.org/multipage/media.html#attr-media-src) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Object attributes: `src` on [`img`](#el-img) only |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Object attributes: `src` on [`img`](#el-img) only |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXURL: <value>` on [`img`](#el-img) and [`input type="image"`](#el-input-image) |
| Comments |  |

#### 3.6.131 `srcdoc`

|  |  |
| --- | --- |
| HTML Specification | `srcdoc` |
| Element(s) | [`iframe`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-srcdoc) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.132 `srclang`

|  |  |
| --- | --- |
| HTML Specification | `srclang` |
| Element(s) | [`track`](https://html.spec.whatwg.org/multipage/media.html#attr-track-srclang) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.133 `srcset`

|  |  |
| --- | --- |
| HTML Specification | `srcset` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-srcset); [`source`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-source-srcset) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not Mapped |
| Comments |  |

#### 3.6.134 `start`

|  |  |
| --- | --- |
| HTML Specification | `start` |
| Element(s) | [`ol`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-ol-start) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Changes the first number of the child list item accessible objects to match the `start` attribute's value. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Changes the first number of the child list item accessible objects to match the `start` attribute's value. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Changes the first number of the child list item accessible objects to match the `start` attribute's value. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Changes the first number of the child list item accessible objects to match the `start` attribute's value. |
| Comments |  |

#### 3.6.135 `step`

|  |  |
| --- | --- |
| HTML Specification | `step` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-step) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | If the `input` is in the [`Range`](#el-input-range) state, set both `RangeValue.SmallChange` and `RangeValue.LargeChange` to the value of `step`. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as `atk_value_get_minimum_increment` if the element implements the `AtkValue` interface. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.136 `style`

|  |  |
| --- | --- |
| HTML Specification | `style` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#the-style-attribute) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.137 `tabindex`

|  |  |
| --- | --- |
| HTML Specification | `tabindex` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/interaction.html#attr-tabindex) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [See Focus States and Events Table](https://www.w3.org/TR/core-aam-1.2/#focus_state_event_table) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.138 `target`

|  |  |
| --- | --- |
| HTML Specification | `target` |
| Element(s) | [`a`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-target); [`area`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-target) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.139 `target`

|  |  |
| --- | --- |
| HTML Specification | `target` |
| Element(s) | [`base`](https://html.spec.whatwg.org/multipage/semantics.html#attr-base-target) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.140 `target`

|  |  |
| --- | --- |
| HTML Specification | `target` |
| Element(s) | [`form`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fs-target) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.141 `title`

|  |  |
| --- | --- |
| HTML Specification | `title` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#attr-title) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Either the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name), or the [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description), or Not mapped (see Comments). |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | The [Accessible Name and Description Computation](#accessible-name-and-description-computation) section specifies if the `title` attribute will be mapped and, if so, through what [[WAI-ARIA](#bib-wai-aria "Accessible Rich Internet Applications (WAI-ARIA) 1.0")] property. |

#### 3.6.142 `title`

|  |  |
| --- | --- |
| HTML Specification | `title` |
| Element(s) | [`abbr`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-abbr-title); [`dfn`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-dfn-title) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Associates the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Associates the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Associates the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXExpandedTextValue: <value>` |
| Comments |  |

#### 3.6.143 `title`

|  |  |
| --- | --- |
| HTML Specification | `title` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-title) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.144 `title`

|  |  |
| --- | --- |
| HTML Specification | `title` |
| Element(s) | [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-title); [`style`](https://html.spec.whatwg.org/multipage/semantics.html#attr-style-title) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Provides the name for the CSS style sheet. |

#### 3.6.145 `translate`

|  |  |
| --- | --- |
| HTML Specification | `translate` |
| Element(s) | [HTML elements](https://html.spec.whatwg.org/multipage/dom.html#attr-translate) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.146 `type`

|  |  |
| --- | --- |
| HTML Specification | `type` |
| Element(s) | [`a`](https://html.spec.whatwg.org/multipage/links.html#attr-hyperlink-type); [`link`](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-type) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.147 `type`

|  |  |
| --- | --- |
| HTML Specification | `type` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-type) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | [`submit`](#el-input-submit) type may be a default button in the form. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | [`submit`](#el-input-submit) type may be a default button in the form. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | [`submit`](#el-input-submit) type may be a default button in the form. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | [`submit`](#el-input-submit) type may be a default button in the form. |
| Comments |  |

#### 3.6.148 `type`

|  |  |
| --- | --- |
| HTML Specification | `type` |
| Element(s) | [`embed`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-embed-type); [`object`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-object-type); [`script`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type); [`source`](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-source-type) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.149 `type`

|  |  |
| --- | --- |
| HTML Specification | `type` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-type) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Refer to WAI-ARIA mappings for input types with defined ARIA roles. |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Defines the accessible role, states and other properties, refer to `type="text"`, `type="password"`, `type="button"`, etc. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Defines the accessible role, states and other properties, refer to `type="text"`, `type="password"`, `type="button"`, etc. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Defines the accessible role, states and other properties, refer to `type="text"`, `type="password"`, `type="button"`, etc. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Defines the accessible role, states and other properties, refer to `type="text"`, `type="password"`, `type="button"`, etc. |
| Comments |  |

#### 3.6.150 `type`

|  |  |
| --- | --- |
| HTML Specification | `type` |
| Element(s) | [`ol`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-ol-type) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Defines the list item marker, which has no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object), but is exposed as content in the accessible text of the associated list item.  Interfaces: `IAccessibleText2` |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Defines the list item marker, which has no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object), but is exposed as content in the accessible text of the associated list item.  Control Pattern: `Text` |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Defines the list item marker, which has no [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object), but is exposed as content in the accessible text of the associated list item.  Interfaces: `ATKText` |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Defines the list item marker, which is exposed as content in `AXValue`, and rendered as an [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object):  AXRole: `AXListMarker`  AXSubrole: `(nil)`  AXRoleDescription: `"list marker"` |
| Comments | Some platforms (IAccessible2, ATK, UIA) do not expose an [accessible object](https://www.w3.org/TR/wai-aria/#dfn-accessible-object) for the list item marker, whether it was created and then pruned from the [accessibility tree](https://www.w3.org/TR/wai-aria/#dfn-accessibility-tree), or never created in the first place. Instead, they expose the list item marker as part of the associated list item's accessible text. In these cases, implementors need to consider such things as adjusting the offsets (e.g., for caret-moved events, text-selection events, etc.) for the updated list item text that now also contains the list item marker as content, rather than just taking the offsets unmodified from the list item renderer. |

#### 3.6.151 `usemap`

|  |  |
| --- | --- |
| HTML Specification | `usemap` |
| Element(s) | [`img`](https://html.spec.whatwg.org/multipage/image-maps.html#attr-hyperlink-usemap) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Responsible for image map creation. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Responsible for image map creation. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Responsible for image map creation. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Responsible for image map creation. |
| Comments | Refer to [`img`](#el-img) element. |

#### 3.6.152 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`button`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-button-value); [`option`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-option-value) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.153 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`data`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#attr-data-value) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

#### 3.6.154 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`input`](https://html.spec.whatwg.org/multipage/input.html#attr-input-value); [`input type=date`](https://html.spec.whatwg.org/multipage/input.html#date-state-(type=date)); [`input type=datetime-local`](https://html.spec.whatwg.org/multipage/input.html#datetime-local-state-(type=datetime-local)); [`input type=email`](https://html.spec.whatwg.org/multipage/input.html#email-state-(type=email)); [`input type=month`](https://html.spec.whatwg.org/multipage/input.html#month-state-(type=month)); [`input type=number`](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)); [`input type=password`](https://html.spec.whatwg.org/multipage/input.html#password-state-(type=password)); [`input type=range`](https://html.spec.whatwg.org/multipage/input.html#range-state-(type=range)) [`input type=search`](https://html.spec.whatwg.org/multipage/input.html#search-state-(type=search)); [`input type=tel`](https://html.spec.whatwg.org/multipage/input.html#tel-state-(type=tel)); [`input type=text`](https://html.spec.whatwg.org/multipage/input.html#text-state-(type=text)); [`input type=url`](https://html.spec.whatwg.org/multipage/input.html#url-state-(type=url)); [`input type=week`](https://html.spec.whatwg.org/multipage/input.html#week-state-(type=week)); |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuenow`](https://www.w3.org/TR/core-aam-1.2/#ariaValueNow) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.155 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`input type=button`](https://html.spec.whatwg.org/multipage/input.html#button-state-(type=button)); [`input type=reset`](https://html.spec.whatwg.org/multipage/input.html#reset-button-state-(type=reset)); [`input type=submit`](https://html.spec.whatwg.org/multipage/input.html#submit-button-state-(type=submit)) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Contributes to the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) of the `input` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | See comments |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | See comments |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | See comments |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | See comments |
| Comments | If specified, the value of the attribute will be the [host language label](https://www.w3.org/TR/accname-1.2/#comp_host_language_label) used in the [accessible name computation](#input-type-button-input-type-submit-and-input-type-reset-elements-accessible-name-computation) for `input` elements in the `button`, `reset` and `submit` states. |

#### 3.6.156 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`input type=checkbox`](https://html.spec.whatwg.org/multipage/input.html#checkbox-state-(type=checkbox)); [`input type=hidden`](https://html.spec.whatwg.org/multipage/input.html#hidden-state-(type=hidden)); [`input type=radio`](https://html.spec.whatwg.org/multipage/input.html#radio-state-(type=radio)) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments | Note  The `value` attribute of these `input` states is not directly communicated to users. |

#### 3.6.157 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`input type=color`](https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color)) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuenow`](https://www.w3.org/TR/core-aam-1.2/#ariaValueNow) & [`aria-valuetext`](https://www.w3.org/TR/core-aam-1.2/#ariaValueText) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments | User agents *MAY* use the exact text value of the `value` attribute, or a localized variation of the specified text to present a human friendly representation of the color value. |

#### 3.6.158 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`input type=image`](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Contributes to the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) of the `input` |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | See comments |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | See comments |
| [ATK](https://gnome.pages.gitlab.gnome.org/atk/) | See comments |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | See comments |
| Comments | If specified, and the `input` in the `image` state has no `alt` attribute specified, then the value of the attribute will be the [host language label](https://www.w3.org/TR/accname-1.2/#comp_host_language_label) used in the [accessible name computation](#input-type-button-input-type-submit-and-input-type-reset-elements-accessible-name-computation), and will render as text if the image source is broken. Otherwise, the attribute is ignored. |

#### 3.6.159 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`li`](https://html.spec.whatwg.org/multipage/grouping-content.html#attr-li-value) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Exposed as first text node of `li`'s accessible object. |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Expose the value of the `value` attribute as the first text node in the list item. If the value of the `value` attribute is an integer, set the UIA `PositionInSet` property to the integer value. |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Exposed as first text node of `li`'s accessible object. |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Exposed as `AXValue: <value>` with accessible object:  AXRole: `AXListMarker`  AXSubrole: `(nil)`  AXRoleDescription: `list marker` |
| Comments |  |

#### 3.6.160 `value`

|  |  |
| --- | --- |
| HTML Specification | `value` |
| Element(s) | [`meter`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-value); [`progress`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-progress-value) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | [`aria-valuenow`](https://www.w3.org/TR/core-aam-1.2/#ariaValueNow) |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Use WAI-ARIA mapping |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Use WAI-ARIA mapping |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Use WAI-ARIA mapping |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Use WAI-ARIA mapping |
| Comments |  |

#### 3.6.161 `width`

|  |  |
| --- | --- |
| HTML Specification | `width` |
| Element(s) | [`canvas`](https://html.spec.whatwg.org/multipage/canvas.html#attr-canvas-width); [`embed`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width); [`iframe`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width); [`img`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width); [`input`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width); [`object`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width); [`source` (in `picture`)](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width); [`video`](https://html.spec.whatwg.org/multipage/embedded-content-other.html#attr-dim-width) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Defines an accessible object's width (`IAccessible::accLocation`) |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Defines an accessible object's width (`BoundingRectangle`) |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Defines an accessible object's width (`atk_component_get_size`) |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | `AXSize: w=n` |
| Comments |  |

#### 3.6.162 `wrap`

|  |  |
| --- | --- |
| HTML Specification | `wrap` |
| Element(s) | [`textarea`](https://html.spec.whatwg.org/multipage/form-elements.html#attr-textarea-wrap) |
| [[WAI-ARIA-1.2](#bib-wai-aria-1.2 "Accessible Rich Internet Applications (WAI-ARIA) 1.2")] | Not mapped |
| [MSAA](https://msdn.microsoft.com/en-us/library/dd373608%28v=VS.85%29.aspx) + [IAccessible2](http://accessibility.linuxfoundation.org/a11yspecs/ia2/docs/html/) | Not mapped |
| [UIA](https://msdn.microsoft.com/en-us/library/ms726297%28v=VS.85%29.aspx) | Not mapped |
| [[ATK](#bib-atk "ATK - Accessibility Toolkit")] | Not mapped |
| [AX](https://developer.apple.com/reference/appkit/nsaccessibility) | Not mapped |
| Comments |  |

## 4. Accessible Name and Description Computation

The terms [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) and [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) are properties provided in
all [accessibility APIs](https://www.w3.org/TR/wai-aria/#dfn-accessibility-api). The name of the properties may differ across APIs but they serve the same function: as a container for a short (name) or longer (description)
string of text.

The [text alternative computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) is used to generate both the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) and
[accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description). There are different rules provided for several different types of
[elements](https://dom.spec.whatwg.org/#concept-element), [nodes](https://dom.spec.whatwg.org/#concept-node), and combinations of markup.

Note

User Agents notify assistive technology when relevant accessibility information changes, sometimes by destroying and recreating the accessibility object, or sometimes by notifying of changes
to the object per the specified
[name change event mappings](https://www.w3.org/TR/core-aam-1.2/#event-aria-label) and [description change event mappings](https://www.w3.org/TR/core-aam-1.2/#event-aria-describedby).

### 4.1 Accessible Name Computations By HTML Element

#### 4.1.1 `input type="text"`, `input type="password"`, `input type="number"`, `input type="search"`, `input type="tel"`, `input type="email"`, `input type="url"` and `textarea` Elements Accessible Name Computation

1. If the control has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of
   the associated `label` element's subtree - if more than one `label` is associated; concatenate their subtrees by DOM order, delimited by spaces.

   If the control is encapsulated by its `label` element, exclude the control's author specified or user-entered value from its computed
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the value of the control's `title` attribute.
4. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the value of the control's [placeholder](#att-placeholder) attribute.
5. Otherwise, use the value of the element's [`aria-placeholder`](https://www.w3.org/TR/wai-aria-1.2/#aria-placeholder) attribute.
6. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.2 `input type="button"`, `input type="submit"` and `input type="reset"` Elements Accessible Name Computation

1. If the control has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of
   the associated `label` element's subtree - if more than one `label` is associated; concatenate their subtrees by DOM order, delimited by spaces.

   If the control is encapsulated by its `label` element, and the control has an author specified `value` or the lack of a `value` has produced an
   [implementation defined](https://infra.spec.whatwg.org/#implementation-defined) string to render, then exclude either from the control's computed
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the value of the control's `value` attribute.
4. For `input type=submit` and `type=reset`: if the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty, and the `value` attribute is unspecified, use the
   [implementation defined](https://infra.spec.whatwg.org/#implementation-defined) string respective to the input type. For instance, a localized string of the word "submit" or
   "reset" respective to the type of `input`.
5. Otherwise: use the value of the control's `title` attribute.
6. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.3 `input type="image"` Element Accessible Name Computation

1. If the control has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of
   the associated `label` element's subtree - if more than one `label` is associated; concatenate their subtrees by DOM order, delimited by spaces.

   If the control is encapsulated by its `label` element, and the control has an `alt` attribute, then exclude the attribute's value from the control's computed
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the value of the control's `alt` attribute if present and its value, when trimmed of
   [whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), is not the empty string.
4. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the value of the control's `title` attribute if present and its value is not the empty
   string.
5. Otherwise, if the previous steps do not yield a usable text string: use the [implementation defined](https://infra.spec.whatwg.org/#implementation-defined) string respective
   to the input type (an `input` in the `image` state represents a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button)). For instance, a localized string of the word
   "submit" or the words "Submit Query".
6. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.4 `button` Element Accessible Name Computation

1. If the `button` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of
   the associated `label` element's subtree - if more than one `label` is associated; concatenate their subtrees by DOM order, delimited by spaces.

   If the `button` element is encapsulated by its `label` element, ignore the `button` element's subtree from its computed
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of
   the element's subtree.
4. Otherwise: use the value of the element's `title` attribute.
5. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.5 `fieldset` Element Accessible Name Computation

1. If the `fieldset` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty, then: if the `fieldset` element has a
   [child](https://dom.spec.whatwg.org/#concept-tree-child) that is a `legend` element, then use the subtree of the first such element.
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty, then:, if the `fieldset` element has a `title` attribute, then use that attribute.
4. Otherwise, there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.6 `output` Element Accessible Name Computation

1. If the `output` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use the associated `label` element or elements [accessible name(s)](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) - if more than one `label` is associated; concatenate by
   DOM order, delimited by spaces.
3. Otherwise use `title` attribute.
4. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.7 Other Form Elements Accessible Name Computation

1. If the control has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use `label` element.
3. Otherwise use `title` attribute.
4. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.8 `summary` Element Accessible Name Computation

1. If the first `summary` element, which is a direct child of the `details` element, has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an
   [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the
   algorithm defined in [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use `summary` element subtree.
3. Otherwise use `title` attribute.
4. If there is no `summary` element as a direct child of the `details` element, the user agent *SHOULD* provide one with a subtree containing a localized string of the word "details".
5. If there is a `summary` element as a direct child of the `details` element, but none of the above yield a usable text string, there is no
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.9 `figure` Element Accessible Name Computation

A [`figcaption`](#el-figcaption) provides additional information related to its parent [`figure`](#el-figure) element. A `figcaption` does not take part in the
[accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) or [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description)
computation, unless explicitly referenced by an author.

1. If the `figure` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise, use the `title` attribute.
3. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.10 `img` Element Accessible Name Computation

1. If the `img` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty: use `alt` attribute, even if its value, when trimmed of [whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), is the
   empty string.

   Note

   An `img` with an `alt` attribute whose value, when trimmed of [whitespace](https://infra.spec.whatwg.org/#ascii-whitespace), is the empty string is mapped to the
   [`presentation`](https://www.w3.org/TR/core-aam-1.2/#role-map-presentation) role. It has no accessible name.
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty and there is no `alt` attribute, use the `title` attribute.
4. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty and there are no `alt` or `title` attributes, and the `img` is a descendant of a `figure`
   element with a child `figcaption` but no other non-[whitespace](https://html.spec.whatwg.org/multipage/dom.html#inter-element-whitespace)
   [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) descendants, then use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of the
   `figcaption` element's subtree.
5. Otherwise there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.11 `table` Element Accessible Name Computation

1. If the `table` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty, then: if the `table` element has a
   [child](https://dom.spec.whatwg.org/#concept-tree-child) that is a `caption` element, then use the subtree of the first such element.
3. If the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is still empty, then: if the `table` element has a `title` attribute, then use that attribute.
4. Otherwise, there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.12 `tr`, `td`, `th` Elements Accessible Name Computation

1. If the element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use the `title` attribute.
3. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.13 `a` Element Accessible Name Computation

1. If the `a` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use `a` element subtree.
3. Otherwise use the `title` attribute.
4. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.14 `area` Element Accessible Name Computation

1. If the `area` element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use `area` element's `alt` attribute.
3. Otherwise use the `title` attribute.
4. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.15 `iframe` Element Accessible Name Computation

1. If the element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use the `title` attribute.
3. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

Note

The document referenced by the `src` of the `iframe` element gets its name from that document's `title` element, like any other document. If there is no `title` provided, there is no
accessible name.

#### 4.1.16 Section and Grouping Element Accessible Name Computation

1. If the element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use the `title` attribute.
3. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

#### 4.1.17 Text-level Element Accessible Name Computation

[`abbr`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-abbr-element), [`b`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-b-element), [`bdi`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdi-element), [`bdo`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element), [`br`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-br-element), [`cite`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-cite-element), [`code`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-code-element), [`dfn`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-dfn-element), [`em`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-em-element), [`i`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-i-element), [`kbd`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-kbd-element), [`mark`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-mark-element), [`q`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-q-element),
[`rp`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-rp-element), [`rt`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-rt-element), [`ruby`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-ruby-element), [`s`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-s-element), [`samp`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-samp-element), [`small`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-small-element), [`strong`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-strong-element),
[`sub` and `sup`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-sub-and-sup-elements), [`time`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element), [`u`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-u-element), [`var`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-var-element), [`wbr`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-wbr-element)

1. If the element has an [`aria-label`](https://www.w3.org/TR/wai-aria-1.2/#aria-label) or an [`aria-labelledby`](https://www.w3.org/TR/wai-aria-1.2/#aria-labelledby) attribute the
   [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) is to be calculated using the algorithm defined in
   [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/).
2. Otherwise use the `title` attribute.
3. If none of the above yield a usable text string there is no [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).

### 4.2 Accessible Description Computation

Authors *MAY* provide an [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) for any HTML element that is a valid child of the `body` element. The following list
represents the order of precedence for [user agents](https://infra.spec.whatwg.org/#user-agent) to compute the [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) of an element. As
defined by [Accessible Name and Description Computation: Description Computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_description) , [user agents](https://infra.spec.whatwg.org/#user-agent) *MUST*
use the first applicable description source, even if its use results in an empty description.

1. If the element has an [`aria-describedby`](https://www.w3.org/TR/wai-aria-1.2/#aria-describedby) or [`aria-description`](https://w3c.github.io/aria/#aria-description) attribute refer
   to the computation conditions defined in [Accessible Name and Description: Computation and API Mappings](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_description).
2. Otherwise, if the [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description) is still empty, and the element is:
   - a `table` element which has a [child](https://dom.spec.whatwg.org/#concept-tree-child) `caption` element, use the
     [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of the subtree of the first `caption` element if it was not used as the
     [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
   - a `summary` element, use the [text equivalent computation](https://www.w3.org/TR/accname-1.2/#mapping_additional_nd_te) of its subtree if it was not used as the
     [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
   - an `input` element whose `type` attribute is the `button`, `submit` or `reset` state, and it has a `value` attribute, then use the flat string of the attribute if it was not used as
     the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name).
3. Otherwise, use the flat string of the `title` attribute if it was not used as the [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name) for the element.
4. If none of the above are applicable, there is no [accessible description](https://www.w3.org/TR/accname-1.2/#dfn-accessible-description).

## 5. Privacy considerations

In accordance with [Web Platform Design Principles](https://w3ctag.github.io/design-principles/#do-not-expose-use-of-assistive-tech), this specification provides no programmatic
interface to determine if information is being used by Assistive Technologies. However, this specification does allow an author to present different information to users of Assistive
Technologies from the information available to users who do not use Assistive Technologies. This is possible using many features of the ARIA and CORE-AAM specifications, just as this is
possible using many other parts of the web technology stack. This content disparity could be abused to perform
[active fingerprinting](https://www.w3.org/TR/fingerprinting-guidance/#active-0) of users of Assistive Technologies.

## 6. Security considerations

This specification introduces no new security considerations.

## A. Appendices

### A.1 Change Log

Review the [commit history](https://github.com/w3c/html-aam/commits/gh-pages) of this document on GitHub.

#### A.1.1 Substantive changes since moving to the [Accessible Rich Internet Applications Working Group](https://www.w3.org/WAI/ARIA/) (03-Nov-2019)

- 2-April-2025: Add `command` and `commandfor` attribute mappings. See [GitHub ARIA PR 2354](https://github.com/w3c/aria/pull/2354/).
- 11-July-2024: User Agents ignore `aria-hidden=true` on `body` and `html` elements. See [GitHub PR 516](https://github.com/w3c/html-aam/pull/516).
- 06-June-2024: Add concept of Minimum Role. See [GitHub PR 454](https://github.com/w3c/html-aam/pull/454).
- 06-June-2024: Add `popover`, `popovertarget` and `popovertargetaction` mappings. See [GitHub PR 481](https://github.com/w3c/html-aam/pull/481).
- 09-Oct-2023: Acknowledge use of `hr` element within `select` element. See [GitHub PR 504](https://github.com/w3c/html-aam/pull/504).
- 03-Oct-2023: Update image mappings to reference the primary synonym roles (`image` and `none`). See [GitHub PR 498](https://github.com/w3c/html-aam/pull/498).
- 03-Oct-2023: Clarify when to expose required field as invalid. See [GitHub PR 429](https://github.com/w3c/html-aam/pull/429).
- 06-Jun-2023: Add computed roles for all HTML elements. See [GitHub PR 465](https://github.com/w3c/html-aam/pull/465).
- 28-Mar-2023: Add `inert` attribute mapping. See [GitHub PR 410](https://github.com/w3c/html-aam/pull/410).
- 24-Mar-2023: Add `search` element and its mappings. See [GitHub PR 355](https://github.com/w3c/html-aam/pull/355/).
- 08-Mar-2023: Update `hgroup` element to be mapped to `role=group`. See [GitHub PR 398](https://github.com/w3c/html-aam/pull/398).
- 08-Mar-2023: Clarify naming algorithm for `output` element. See [GitHub PR 402](https://github.com/w3c/html-aam/pull/402).
- 12-Dec-2022: Revise mapping for `s` element to be `role=deletion`. See [GitHub PR 442](https://github.com/w3c/html-aam/pull/442).
- 28-Nov-2022: Simplify accessible description computation section. See [GitHub PR 444](https://github.com/w3c/html-aam/pull/444).
- 19-Jul-2022: Update `address` element to be mapped to `role=group`. See [GitHub PR 420](https://github.com/w3c/html-aam/pull/420).
- 03-Apr-2022: Update `aside` mappings based on its nesting context. See [GitHub PR 350](https://github.com/w3c/html-aam/pull/350).
- 06-Mar-2022: Update the following elements to map to the `generic` role: `a no href`, `footer` not scoped to `body`, `header` not scoped to `body`, `samp`, `span`. See
  [GitHub PR 364](https://github.com/w3c/html-aam/pull/364).
- 06-Feb-2022: Update `mark` to point to Core AAM mapping for the role. See [GitHub Issue 316](https://github.com/w3c/html-aam/issues/316).
- 02-Nov-2021: Updating `blockquote`, `caption`, `code`, `del`, `em`, `ins`, `meter`, `paragraph`, `strong`, `sub`, `sup` and `time` to ARIA 1.2 mappings in Core AAM. Fix `body` mapping to
  `generic`, and `html` mapping to `document`. Fix `hgroup` mapping to `generic`. Update `details` to map to `group` with additional information specific to ATK, UIA. See
  [GitHub issue #348](https://github.com/w3c/html-aam/pull/348)
- 12-May-2021: Add FACES references to attributes table - `readonly`, `name`, `form`, `disabled`. See [Issue 257](https://github.com/w3c/html-aam/issues/257).
- 12-Dec-2019: Adds `hgroup`, `slot`, autonomous custom element and form associated custom element. See [GitHub issue #189](https://github.com/w3c/html-aam/issues/189).
- 26-Nov-2019: Updates mappings for `disabled`, `scope`, `spellcheck`, `tabindex` to point to WAI-ARIA. Adds AX `pattern`, `reversed`, `rows`, `size`, `span`, `src`, `start`, `step`,
  `type` attribute mappings. Adds `min-length`, `ping`, `playsinline`, `referrerpolicy`, `sizes`, `srcset`, `data[value]` attribute mappings. See
  [GitHub pull request #245](https://github.com/w3c/html-aam/pull/245).

##### Substantive changes since moving to the Web Application Working Group (formerly Web Platform WG) (01-Oct-2016)

- 30-Sept-2019: Remove mappings for `rb` and `rtc` elements as they are marked as obsolete in HTML. See [GitHub issue #115](https://github.com/w3c/html-aam/issues/115) and
  [pull request #253](https://github.com/w3c/html-aam/pull/253).
- 23-Sept-2019: Update attribute mappings for `high`, `low`, `max`, `min`, and `meter` and `progress`'s `value` attribute. See
  [GitHub pull request #244](https://github.com/w3c/html-aam/pull/244).
- 18-Sept-2019: Update `mark` element's UIA `LocalizedControlType` and AX `AXRoleDescription`. See [GitHub issue #236](https://github.com/w3c/html-aam/issues/236).
- 18-Sept-2019: Update ATK mappings for `summary` and `details` elements. See [GitHub issue #142](https://github.com/w3c/html-aam/issues/142) and
  [GitHub issue #147](https://github.com/w3c/html-aam/issues/147).
- 18-Sept-2019: Update MSAA mappings for `sub` and `sup`. See [GitHub pull request #252](https://github.com/w3c/html-aam/pull/252).
- 11-Sept-2019: Update mapping for `menu` to match HTML Living Standard. Remove element and attribute mappings that are not applicable to `menu` and `menuitem`. Update mapping of `menu`
  to `role="list"`. See [GitHub issue #188](https://github.com/w3c/html-aam/issues/188).
- 10-July-2019: Further updated mappings for `ins` and `del` elements. See [GitHub pull request #219](https://github.com/w3c/html-aam/pull/219).
- 13-June-2019: Update mappings for `ins` and `del` elements. See [GitHub issue #141](https://github.com/w3c/html-aam/issues/141).
- 10-June-2019: Update ATK mappings for `header` and `footer` when not scoped to the `body`. See [GitHub issue #129](https://github.com/w3c/html-aam/issues/129).
- 21-May-2019: Update AXAPI mappings for `map` element. Add accessible name and description computation for `area`. See
  [GitHub issue #176](https://github.com/w3c/html-aam/issues/176).
- 11-Apr-2019: Update UIA mappings for `sub` and `sup` elements. See [Pull request #177](https://github.com/w3c/html-aam/pull/177).
- 20-Mar-2019: Updated IA2 mappings for `sup` and `sub` elements. See [GitHub issue #174](https://github.com/w3c/html-aam/issues/174).
- 26-Feb-2019: Updated mappings for the `address` element. See [GitHub issue #170](https://github.com/w3c/html-aam/issues/170).
- 19-Feb-2019: Added `placeholder` attribute to accessible name computation for various `input` elements. See [GitHub issue #167](https://github.com/w3c/html-aam/issues/167).
- 07-Feb-2018: Added entries for the `rb` and `rtc` elements, and updated AXAPI mappings for the `rb`, `rt` and `ruby` elements. See
  [GitHub issue #115](https://github.com/w3c/html-aam/issues/115).
- 07-Feb-2018: Updated mappings for the `svg` element. See [GitHub issue #43](https://github.com/w3c/html-aam/issues/43).
- 07-Feb-2018: Updated AXAPI mappings for the `del` and `ins` elements, and the `datetime` attribute.
- 07-Feb-2018: Aligned mappings with CORE-AAM as appropriate for `header` and `footer` when scoped to `body`, `aside`, and `output`. See
  [GitHub issue #119](https://github.com/w3c/html-aam/issues/119).
- 07-Feb-2018: Updated ATK and AX mappings for the `multiple` attribute on `input` element. See [GitHub issue #96](https://github.com/w3c/html-aam/issues/96).
- 07-Feb-2018: Updated ATK mappings for the `sub` and `sup` elements. See [GitHub issue #121](https://github.com/w3c/html-aam/issues/121).
- 07-Feb-2018: Updated mappings for the `body` element. See [GitHub issue #117](https://github.com/w3c/html-aam/issues/117).
- 01-Feb-2018: Updated IA2 mapping for the `meter` element. See [GitHub issue #2](https://github.com/w3c/html-aam/issues/2).
- 29-Jan-2018: Updated heading mapping to reflect implementations. See [GitHub issue #116](https://github.com/w3c/html-aam/issues/116).
- 23-Jan-2018: Added note regarding effect of some CSS properties. See [GitHub issue #234](https://github.com/w3c/html-aam/issues/24).
- 23-Jan-2018: Updated mappings for the `address` element. See [GitHub issue #33](https://github.com/w3c/html-aam/issues/33).
- 23-Jan-2018: Updated mappings for the `dt` element. See [GitHub issue #78](https://github.com/w3c/html-aam/issues/78).
- 23-Jan-2018: Updated AXAPI mappings for the `mark` element.
- 08-Jan-2018: Updated mappings for the `input` element with the `type` attribute in the Color state. See [GitHub issue #48](https://github.com/w3c/html-aam/issues/48).
- 06-Jan-2018: Updated IA2 mappings for the `pre`, `q`, and `ruby` elements, and the `multiple` attribute for the `input` element. See
  [GitHub issue #94](https://github.com/w3c/html-aam/issues/94).
- 18-Dec-2017: Rewrote first paragraph in Introduction to better reflect the relationship between the HTML-AAM and CORE-AAM specifications. See
  [GitHub issue #66](https://github.com/w3c/html-aam/issues/66).
- 18-Dec-2017: Updated `readonly` attribute to use `aria-readonly="true"` WAI-ARIA mappings. See [GitHub issue #93](https://github.com/w3c/html-aam/issues/93).
- 08-Dec-2017: Changed AXAPI mapping for the `canvas` element from `AXImage` to `AXGroup`.
- 01-Dec-2017: Updated mappings for the `dfn` element. See [GitHub issue #6](https://github.com/w3c/html-aam/issues/6).
- 30-Nov-2017: Updated mappings for the `meter` element. See [GitHub issue #2](https://github.com/w3c/html-aam/issues/2).
- 24-Nov-2017: Updated mappings for the `audio` and `video` elements. See [GitHub issue #80](https://github.com/w3c/html-aam/issues/80).
- 23-Nov-2017: Updated `figure` element mappings to reflect the [WAI-ARIA `figure` role mappings](https://w3c.github.io/core-aam/#role-map-figure).
- 23-Nov-2017: Updated mappings for the `form` element based on presence of [accessible name](https://www.w3.org/TR/accname-1.2/#dfn-accessible-name). See
  [GitHub issue #106](https://github.com/w3c/html-aam/issues/106).
- 23-Nov-2017: Removed the accessible name computation requirement to ignore an `img` element's `title` attribute when the element's `alt` attribute is empty. See
  [GitHub issue #99](https://github.com/w3c/html-aam/issues/99).
- 23-Nov-2017: Added note to not expose `aria-roledescription` unless element also a conforming `role` attribute value. See
  [GitHub issue #98](https://github.com/w3c/html-aam/issues/98).
- 09-Aug-2017: Updated mappings for the `type` attribute on the `ol` element. See [GitHub issue #91](https://github.com/w3c/html-aam/issues/91).
- 25-July-2017: Updated UIA mappings for multiple elements and attributes. See [GitHub issue #95](https://github.com/w3c/html-aam/issues/95) and
  [GitHub pull request #101](https://github.com/w3c/html-aam/pull/101).
- 02-June-2017: Updated AXAPI mappings for `title` attribute on `abbr` element, and `abbr` attribute on `th` element. See
  [GitHub issue #16](https://github.com/w3c/html-aam/issues/16).
- 31-May-2017: Updated mappings for `hidden` attribute. See [GitHub issue #38](https://github.com/w3c/html-aam/issues/38).
- 24-May-2017: Updated mappings for `selected` attribute. See [GitHub issue #92](https://github.com/w3c/html-aam/issues/92).
- 01-May-2017: Updated AXAPI mapping for `time` element. See [GitHub issue #88](https://github.com/w3c/html-aam/issues/88).
- 27-Apr-2017: Updated UIA mappings for `lang` and `dir` attributes. See [GitHub issue #19](https://github.com/w3c/html-aam/issues/19).
- 19-Apr-2017: Updated mapping for `colspan` and `rowspan` attributes. See GitHub [issue #56](https://github.com/w3c/html-aam/issues/56) and
  [issue #57](https://github.com/w3c/html-aam/issues/57).
- 03-Apr-2017: Updated mapping for `section` element. See [GitHub issue #79](https://github.com/w3c/html-aam/issues/79).
- 23-Dec-2016: No mapping for `datalist` element if not linked with `input` element. See [GitHub issue #26](https://github.com/w3c/html-aam/issues/26).
- 23-Dec-2016: Updated IA2 mapping for `list` attribute. See [GitHub issue #21](https://github.com/w3c/html-aam/issues/21).
- 22-Dec-2016: Sync mappings for `footer` and `header` elements. See [GitHub issue #59](https://github.com/w3c/html-aam/issues/59).
- 22-Dec-2016: Updated IA2 mapping for `input@type='date'` attribute. See [GitHub issue #61](https://github.com/w3c/html-aam/issues/61).
- 22-Dec-2016: Updated IA2 mapping for `input@type='file'` element. See [GitHub issue #62](https://github.com/w3c/html-aam/issues/62).
- 22-Dec-2016: Updated IA2 mapping for `summary` element. See [GitHub issue #64](https://github.com/w3c/html-aam/issues/64).
- 14-Dec-2016: Updated wording distinguishing when `header` and `footer` elements are or are not ARIA landmarks. See
  [GitHub issue #65](https://github.com/w3c/html-aam/issues/65).
- 07-Dec-2016: Modified `aria-multiselectable` mapping for `datalist` to reflect listbox selection model. See [GitHub issue #71](https://github.com/w3c/html-aam/issues/71).
- 07-Dec-2016: Mappings for the `multiple` attribute on `input` and `select` elements. See [GitHub issue #72](https://github.com/w3c/html-aam/issues/72).
- 27-Nov-2016: Added implementation rules for the `checked`, `contenteditable`, `disabled`, and `indeterminate` attributes.
- 21-Nov-2016: Removed `placeholder` attribute from accessible description computation for various `input` elements.

### A.2 Acknowledgments

*This section is non-normative.*

The following people contributed to the development of this document.

- [Adam Page](https://github.com/adampage)
- [Alex Lloyd](https://github.com/AlexLloyd0)
- [Alexander Surkov](https://github.com/asurkov)
- [Bogdan Brinza](https://github.com/boggydigital)
- [Carolyn MacLeod](https://github.com/carmacleod)
- [Dan Clark](https://github.com/dandclark)
- [Denis Ah-Kang](https://github.com/deniak)
- [Dominique Hazael-Massieux](https://github.com/dontcallmedom)
- [einSelbst](https://github.com/einSelbst)
- [James Craig](https://github.com/cookiecrook)
- [James Nurthen](https://github.com/jnurthen)
- [Jason Kiss](https://github.com/jasonkiss)
- [joanmarie](https://github.com/joanmarie)
- [Johanna](https://github.com/Johanna-hub)
- [Jon Gunderson](https://github.com/jongund)
- [Léonie Watson](https://github.com/LJWatson)
- [Marcos Cáceres](https://github.com/marcoscaceres)
- [Melanie Richards](https://github.com/melanierichards)
- [Nick Schonning](https://github.com/nschonni)
- [Peter Krautzberger](https://github.com/pkra)
- [Philippe Le Hegaret](https://github.com/plehegar)
- [Sid Vishnoi](https://github.com/sidvishnoi)
- [Simon Pieters](https://github.com/zcorpan)
- [Steve Faulkner](https://github.com/stevefaulkner)
- [Valerie Young](https://github.com/spectranaut)
- [Vikas Parashar](https://github.com/vikas-parashar)
- [Xiaoqian Wu](https://github.com/siusin)
- [Yummy\_Bacon5](https://github.com/YummyBacon5)
- [Yves Lafon](https://github.com/ylafon)

#### A.2.1 ARIA WG participants at the time of publication

#### A.2.2 Enabling funders

This publication has been funded in part with U.S. Federal funds from the Department of Education, National Institute on Disability, Independent Living, and Rehabilitation Research (NIDILRR), initially under contract number ED-OSE-10-C-0067, then under contract number HHSP23301500054C, and now under HHS75P00120P00168. The content of this publication does not necessarily reflect the views or policies of the U.S. Department of Education, nor does mention of trade names, commercial products, or organizations imply endorsement by the U.S. Government.

## B. References

### B.1 Normative references

[accname-1.2]
:   [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/). Bryan Garaventa; Melanie Sumner. W3C. 11 March 2026. W3C Working Draft. URL: <https://www.w3.org/TR/accname-1.2/>

[core-aam-1.2]
:   [Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/). Valerie Young; Cynthia Shelly. W3C. 11 March 2026. CRD. URL: <https://www.w3.org/TR/core-aam-1.2/>

[HTML]
:   [HTML Standard](https://html.spec.whatwg.org/multipage/). Anne van Kesteren; Domenic Denicola; Dominic Farolino; Ian Hickson; Philip Jägenstedt; Simon Pieters. WHATWG. Living Standard. URL: <https://html.spec.whatwg.org/multipage/>

[infra]
:   [Infra Standard](https://infra.spec.whatwg.org/). Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: <https://infra.spec.whatwg.org/>

[RFC2119]
:   [Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119). S. Bradner. IETF. March 1997. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc2119>

[RFC8174]
:   [Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words](https://www.rfc-editor.org/rfc/rfc8174). B. Leiba. IETF. May 2017. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc8174>

[svg-aam-1.0]
:   [SVG Accessibility API Mappings](https://www.w3.org/TR/svg-aam-1.0/). Cynthia Shelly; Mark Rogers. W3C. 11 March 2026. W3C Working Draft. URL: <https://www.w3.org/TR/svg-aam-1.0/>

[WAI-ARIA]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.0](https://www.w3.org/TR/wai-aria/). James Craig; Michael Cooper et al. W3C. 20 March 2014. W3C Recommendation. URL: <https://www.w3.org/TR/wai-aria/>

[WAI-ARIA-1.2]
:   [Accessible Rich Internet Applications (WAI-ARIA) 1.2](https://www.w3.org/TR/wai-aria-1.2/). Joanmarie Diggs; James Nurthen; Michael Cooper; Carolyn MacLeod. W3C. 6 June 2023. W3C Recommendation. URL: <https://www.w3.org/TR/wai-aria-1.2/>

### B.2 Informative references

[AT-SPI]
:   [Assistive Technology Service Provider Interface](https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/). The GNOME Project. URL: <https://gnome.pages.gitlab.gnome.org/at-spi2-core/libatspi/>

[ATK]
:   [ATK - Accessibility Toolkit](https://developer.gnome.org/atk/stable/). The GNOME Project. URL: <https://developer.gnome.org/atk/stable/>

[AXAPI]
:   [The NSAccessibility Protocol for macOS](https://developer.apple.com/documentation/appkit/nsaccessibility). Apple, Inc. URL: <https://developer.apple.com/documentation/appkit/nsaccessibility>

[dom]
:   [DOM Standard](https://dom.spec.whatwg.org/). Anne van Kesteren. WHATWG. Living Standard. URL: <https://dom.spec.whatwg.org/>

[HTML5]
:   [HTML5](https://www.w3.org/TR/html5/). Ian Hickson; Robin Berjon; Steve Faulkner; Travis Leithead; Erika Doyle Navara; Theresa O'Connor; Silvia Pfeiffer. W3C. 27 March 2018. W3C Recommendation. URL: <https://www.w3.org/TR/html5/>

[IAccessible2]
:   [IAccessible2](https://wiki.linuxfoundation.org/accessibility/iaccessible2/). Linux Foundation. URL: <https://wiki.linuxfoundation.org/accessibility/iaccessible2/>

[UI-AUTOMATION]
:   [UI Automation](https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification). Microsoft Corporation. URL: <https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification>

[↑](#title)

[Permalink](#dfn-minimum-role)

**Referenced in:**

- [§ 3.5 HTML Element Role Mappings](#ref-for-dfn-minimum-role-1 "§ 3.5 HTML Element Role Mappings")

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