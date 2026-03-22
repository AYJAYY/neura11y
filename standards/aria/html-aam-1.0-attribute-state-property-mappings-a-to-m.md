---
ai_context: HTML-AAM attribute mappings for HTML attributes from abbr through muted.
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
- attributes
- states
- properties
title: HTML Accessibility API Mappings 1.0 Attribute State and Property Mappings A-M
---

# HTML Accessibility API Mappings 1.0 Attribute State and Property Mappings A-M

## HTML Attribute State and Property Mappings A-M

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