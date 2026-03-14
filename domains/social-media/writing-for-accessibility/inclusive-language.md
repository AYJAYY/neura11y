---
title: "Inclusive Language for Social Media"
standard: ""
source_url: ""
domain: ["social-media"]
last_fetched: "2026-03-13"
status: "curated"
tags: ["inclusive-language", "writing", "social-media", "disability-language", "emoji", "plain-language"]
ai_context: "Inclusive language guidelines for social media content. Covers disability language, emoji accessibility, hashtags, and writing for diverse audiences."
---

# Inclusive Language for Social Media

---

## Disability Language

### Identity-First vs. Person-First Language

There is an ongoing debate within disability communities between two approaches:

**Person-first language:** "person with a disability," "person who is deaf"
- Emphasizes personhood before disability
- Historically advocated by some disability organizations and medical contexts
- Preferred by many people with intellectual disabilities and their advocates

**Identity-first language:** "disabled person," "Deaf person," "autistic person"
- Treats disability as part of identity, not something separate from the person
- Preferred by many in the Deaf, autistic, and blind communities
- Increasingly used in disability studies and advocacy

**The rule: follow the individual's preference.**
- When writing about a specific person: use their stated preference
- When writing generally: follow the predominant preference of the community being discussed
- Autistic community: strongly prefers identity-first ("autistic person," not "person with autism")
- Deaf community (capital D): identity-first ("Deaf person"); note capital D indicates cultural identity
- Blind community: split — "blind person" and "person who is blind" are both acceptable

### Terms to Avoid

| Outdated / Offensive | Preferred |
|---|---|
| Handicapped | Disabled |
| Suffers from [disability] | Has [disability] / lives with [disability] |
| Confined to a wheelchair | Uses a wheelchair / wheelchair user |
| Wheelchair-bound | Wheelchair user |
| The disabled | People with disabilities / disabled people |
| Special needs | Disability (be specific when possible) |
| Handicapable | Not used (patronizing) |
| Differently abled | Disabled (many disabled people find this evasive) |
| Mentally retarded | Intellectual disability |
| Crazy, insane, nuts (as negative) | Avoid using mental health terms as insults |
| Dumb, lame, blind (as generic negatives) | Choose words that don't equate disability with failure |

### Ableist Language to Avoid in General Writing

These terms use disability as a metaphor for failure or stupidity:
- "That's crazy" → "That's surprising" / "That's intense"
- "That's insane" → "That's unbelievable" / "That's a lot"
- "What a lame idea" → "That's a weak idea"
- "Blind to the truth" → "Ignoring the truth"
- "Tone-deaf" → "Out of touch" / "Disconnected"
- "Falling on deaf ears" → "Being ignored"
- "Dumb mistake" → "Careless mistake"
- "That's stupid" → Be specific about what is problematic

---

## Emoji Accessibility

### How Screen Readers Read Emoji

Screen readers read the Unicode description for each emoji. Users hear the full name.

| Emoji | What Screen Readers Announce |
|-------|------------------------------|
| 😊 | "smiling face with smiling eyes" |
| ❤️ | "red heart" |
| 🎉 | "party popper" |
| 🔥 | "fire" |
| 💪 | "flexed biceps" |
| ✅ | "check mark button" |
| 🌍 | "globe showing Europe-Africa" |

### Emoji Rules for Accessibility

**Rule 1: Put emoji at the end of sentences, not the beginning or middle**

Screen readers read in sequence. Emoji mid-sentence interrupt the text flow.

- **Inaccessible:** "🎉 We're excited to announce 🎉 our new product! 🚀"
- **Accessible:** "We're excited to announce our new product! 🎉🚀"

**Rule 2: Don't repeat emoji excessively**

Each instance is read separately, creating repetitive output.

- **Inaccessible:** "Best day ever!!!! ❤️❤️❤️❤️❤️❤️❤️❤️"
- **Accessible:** "Best day ever! ❤️"

**Rule 3: Don't use emoji as bullet points or list markers**

```
// Inaccessible:
🔴 Requirement one
🔴 Requirement two
🔴 Requirement three

// Better:
- Requirement one
- Requirement two
- Requirement three
```

**Rule 4: Don't substitute emoji for words**

- **Inaccessible:** "Join us 📅 March 15 at 🕙 10:00 AM 📍 San Francisco"
- **Accessible:** "Join us March 15 at 10:00 AM in San Francisco 📅"

**Rule 5: Be aware of platform-specific emoji rendering**

Emoji appearance varies by platform:
- The same emoji codepoint looks different on iOS vs. Android vs. Windows
- Some emoji have subtly different meanings across platforms
- Emoji added in recent Unicode versions may not render on older devices (shows as square)

**Rule 6: Skin tone modifiers**

Skin tone modifier emoji (e.g., 👋🏿) are read as "[emoji name]: dark skin tone" on most screen readers. This is appropriate representation.

---

## Writing for Cognitive Accessibility

### Plain Language Principles

**Use simple, common words:**
- "use" instead of "utilize"
- "start" instead of "commence"
- "show" instead of "demonstrate"
- "end" instead of "terminate"

**Write short sentences:**
- Target: 15–20 words per sentence
- Maximum: 25 words before splitting

**Use active voice:**
- Active: "We updated the policy"
- Passive: "The policy was updated" (by whom? when?)

**Target reading level:**
- General social media audiences: Grade 8-10
- Technical audiences: Grade 12-14
- Accessibility-specific content for practitioners: Grade 12-14

**Avoid jargon** unless you define it:
- First use: "Web Content Accessibility Guidelines (WCAG)"
- Subsequent uses: "WCAG"

### Post Structure for Readability

- **Lead with the key point** — The most important information first
- **Use line breaks** — Blank line between paragraphs, even on social media
- **One idea per paragraph** — Don't cram multiple points together
- **Use numbers for lists** — When sequence matters: "Step 1, Step 2, Step 3"
- **Keep it concise** — If it can be said in fewer words, use fewer words

---

## Thread Accessibility (Twitter/X, Mastodon)

When posting a thread:
- Number each post: "1/5", "2/5" etc.
- The thread should be readable as standalone posts when possible
- Each tweet should make sense without context from the previous tweet
- End threads with "End." or "/end" to signal completion to screen reader users navigating threads

---

## Inclusive Imagery Language

When describing images of people in alt text or captions:

### Race and Ethnicity

- Describe race/ethnicity when it is relevant to the content (e.g., diversity posts, specific cultural context)
- Use terms the pictured individual or community uses (e.g., Black, not African-American, if the person or community uses that term)
- When uncertain, you can describe visible characteristics without labeling identity

### Gender

- Use gender-neutral language by default unless gender is relevant: "a person," "someone," "they"
- If gender is clearly apparent and relevant, use appropriate terms
- For non-binary or gender-nonconforming people: use they/them unless stated otherwise
- Don't assume from appearance

### Disability

- Describe disability-related features in images when relevant (wheelchair, white cane, hearing aid)
- Describe these as facts, not defining characteristics
- "A person using a power wheelchair near a coffee shop entrance"

### Age

- Describe apparent age range when relevant: "an elderly woman," "a young child," "a middle-aged man"
- Be approximate; avoid specific age guessing

---

## Content Warnings

Some platforms (especially Mastodon) support content warnings. Use them for:
- Graphic images (violence, medical content)
- Flashing images or GIFs (seizure risk — note flash frequency if known)
- Sensitive topics (trauma, mental health crisis)
- Spoilers

Standard content warning format on Mastodon: add text in the CW/spoiler field before your main content.

On platforms without CW support, add warning text at the start of the post: "CN: [content description]" or "CW: [content description]"
