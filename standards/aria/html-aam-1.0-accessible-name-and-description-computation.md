---
ai_context: HTML-AAM accessible name and accessible description computation rules
  for HTML elements.
domain:
- web
last_fetched: '2026-03-21'
source_url: https://www.w3.org/TR/html-aam-1.0/
standard: HTML Accessibility API Mappings 1.0
status: normative
tags:
- aria
- html-aam
- accessible-name
- accessible-description
- html
title: HTML Accessibility API Mappings 1.0 Accessible Name and Description Computation
---

# HTML Accessibility API Mappings 1.0 Accessible Name and Description Computation

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