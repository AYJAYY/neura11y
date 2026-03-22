---
ai_context: HTML-AAM element role mappings for native HTML elements and states.
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
- roles
- element-mappings
title: HTML Accessibility API Mappings 1.0 Element Role Mappings
---

# HTML Accessibility API Mappings 1.0 Element Role Mappings

## HTML Element Role Mappings

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