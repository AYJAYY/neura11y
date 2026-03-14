---
ai_context: W3C alt text decision tree for determining the correct alt text approach.
domain:
- web
- documents
- social-media
last_fetched: '2026-03-13'
source_url: https://www.w3.org/WAI/tutorials/images/decision-tree/
standard: WCAG 2.2
status: prescriptive
tags:
- alt-text
- images
- decision-tree
title: Alt Text Decision Tree (Fetched)
---

This decision tree describes how to use the `alt` attribute of the `<img>` element in various situations. For some types of images, there are alternative approaches, such as using CSS background images for decorative images or web fonts instead of images of text.

- **Does the image contain text?**
  - **Yes:**
    - **… and the text is also present as *real* text nearby.**
      *Use an empty `alt` attribute. See [Decorative Images](/WAI/tutorials/images/decorative/).*
    - **… and the text is only shown for visual effects.**
      *Use an empty `alt` attribute. See [Decorative Images](/WAI/tutorials/images/decorative/).*
    - **… and the text has a specific function, for example is an icon.**
      *Use the `alt` attribute to communicate the function of the image. See [Functional Images](/WAI/tutorials/images/functional/).*
    - **… and the text in the image is not present otherwise.** *Use the `alt` attribute to include the text of the image. See [Images of Text](/WAI/tutorials/images/textual/#styled-text-decorative-effect).*
  - **No:**
    - Continue.
- **Is the image used in a link or a button, and would it be hard or impossible to understand what the link or the button does, if the image wasn’t there?**
  - **Yes:**
    - *Use the `alt` attribute to communicate the destination of the link or action taken. See [Functional Images](/WAI/tutorials/images/functional/).*
  - **No:**
    - Continue.
- **Does the image contribute meaning to the current page or context?**
  - **Yes:**
    - **… and it’s a simple graphic or photograph.**
      *Use a brief description of the image in a way that conveys that meaning in the `alt` attribute. See [Informative Images](/WAI/tutorials/images/informative/).*
    - **… and it’s a graph or complex piece of information.**
      *Include the information contained in the image elsewhere on the page. See [Complex Images](/WAI/tutorials/images/complex/).*
    - **… and it shows content that is redundant to *real* text nearby.**
      *Use an empty `alt` attribute. See (redundant) [Functional Images](/WAI/tutorials/images/functional/#logo-image-within-link-text).*
  - **No:**
    - Continue.
- **Is the image purely decorative or not intended for users?**
  - **Yes:**
    - *Use an empty `alt` attribute. See [Decorative Images](/WAI/tutorials/images/decorative/).*
  - **No:**
    - Continue.
- **Is the image’s use not listed above or it’s unclear what `alt` text to provide?**
  - This decision tree **does not** cover all cases. For detailed information on the provision of text alternatives refer to the [Images Tutorial](/WAI/tutorials/images/).

Please share your ideas, suggestions, or comments via e-mail to the publicly-archived list [wai@w3.org](mailto:wai@w3.org?body=%5Binclude%20a%20relevant%20email%20Subject%5D%0A%0A%5Bput%20comment%20here...%5D%0A%0AI%20give%20permission%20to%20share%20this%20to%20a%20publicly-archived%20e-mail%20list.) or via GitHub.

[E-mail](mailto:wai@w3.org?body=%5Binclude%20a%20relevant%20email%20Subject%5D%0A%0A%5Bput%20comment%20here...%5D%0A%0AI%20give%20permission%20to%20share%20this%20to%20a%20publicly-archived%20e-mail%20list.)[Fork & Edit on GitHub](
https://github.com/w3c/wai-website/edit/main/pages/design-develop/tutorials/images/decision-tree.md
)[New GitHub Issue](https://github.com/w3c/wai-website/issues/new?template=content-issue.yml&wai-resource-id=wai-tutorials&wai-url=https://www.w3.org/WAI/tutorials/images/decision-tree/)

 [Back to Top](#top)