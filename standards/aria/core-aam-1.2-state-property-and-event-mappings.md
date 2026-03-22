---
ai_context: Core-AAM mappings for ARIA states, properties, special processing, actions,
  events, and notify algorithms.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/core-aam-1.2/
standard: Core Accessibility API Mappings 1.2
status: normative
tags:
- aria
- core-aam
- states
- properties
- events
- accessibility-api
title: Core Accessibility API Mappings 1.2 State, Property, and Event Mappings
---

# Core Accessibility API Mappings 1.2 State, Property, and Event Mappings

## State, Property, Action, and Event Mappings

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

## ARIANotifyMixin Algorithm Mapping Tables

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