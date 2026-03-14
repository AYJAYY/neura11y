---
ai_context: Matterhorn Protocol 1.1 from the PDF Association. Defines 136 failure
  conditions for PDF/UA (ISO 14289-1) conformance. Each failure condition maps to
  a PDF/UA clause and is categorised as machine-checkable or requiring human inspection.
  Use when advising on PDF accessibility audit procedures.
domain:
- documents
last_fetched: '2026-03-13'
source_url: https://pdfa.org/resource/the-matterhorn-protocol/
standard: Matterhorn Protocol 1.1
status: normative
tags:
- matterhorn
- pdf-ua
- pdf
- conformance
- documents
title: Matterhorn Protocol 1.1 — PDF/UA Conformance Checking
---

Matterhorn Protocol 1.1
PDF/UA Conformance Testing Model
Copyright © 2021 PDF Association
This work is licensed under the Creative Commons Attribution 4.0
International License.
To view a copy of this license, visit
https://creativecommons.org/licenses/by/4.0/
or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.
PDF Association
Friedenstr. 2A · 16321 Bernau bei Berlin · Germany
E-mail: copyright@pdfa.org
Web: www.pdfa.org
Published in Germany and the United States of America
PDF Association
Introduction
Templates and document production processes can automate many aspects of accessibility,
but the range of necessary checkpoints is extensive and human judgment is required in many
areas.
Organizations committed to providing accessible electronic documents require a cost-
effective means of ensuring their document’s accessibility features are adequate.
Intended for software developers and document testers, the Matterhorn Protocol is designed
to foster PDF/UA adoption by specifying a common set of tests to facilitate the exchange of
detailed information on PDF/UA conformance.
NOTE: The concepts of “partial conformance” and “severity of non-conformance” are
intentionally not addressed in this document.
© 2021 PDF Association 1
PDF Association
Table of Contents
Introduction 1
Document History 4
Background 4
About PDF/UA 4
Matterhorn Protocol Checkpoints 5
Key to the Headers in the Failure Conditions Tables 5
Additional Reading 5
Other reading (superseded documents) 5
PDF/UA-1 Failure Conditions 6
Checkpoint 01: Real content tagged 6
Checkpoint 02: Role Mapping 7
Checkpoint 03: Flickering 7
Checkpoint 04: Color and Contrast 7
Checkpoint 05: Sound 8
Checkpoint 06: Metadata 8
Checkpoint 07: Dictionary 8
Checkpoint 08: OCR Validation 8
Checkpoint 09: Appropriate Tags 9
Checkpoint 10: Character Mappings 9
Checkpoint 11: Declared Natural Language 10
Checkpoint 12: Stretchable Characters 10
Checkpoint 13: Graphics 10
Checkpoint 14: Headings 11
Checkpoint 15: Tables 12
Checkpoint 16: Lists 12
Checkpoint 17: Mathematical Expressions 12
Checkpoint 18: Page Headers and Footers 13
Checkpoint 19: Notes and References 13
Checkpoint 20: Optional Content 13
© 2021 PDF Association 2
PDF Association
Checkpoint 21: Embedded Files 13
Checkpoint 22: Article Threads 13
Checkpoint 23: Digital Signatures 14
Checkpoint 24: Non-Interactive Forms 14
Checkpoint 25: XFA 14
Checkpoint 26: Security 14
Checkpoint 27: Navigation 14
Checkpoint 28: Annotations 15
Checkpoint 29: Actions 16
Checkpoint 30: XObjects 16
Checkpoint 31: Fonts 16
© 2021 PDF Association 3
PDF Association
Document History
Version Date Change
1.0 2013-08-07 Initial release
1.0 2013-10-10 Editorial and typographical corrections.
1.01 2014-02-11 Changed two “Machine” checks to “Human”, updated the description on page 2,
formatting changes to improve maintenance, added headings and a Table of
Contents to improve navigability.
1.02 2014-04-30 Minor editorial and formatting corrections, moved 08-003 to 01-007.
1.1 2020-11-10 ■ Failure condition 13-008 added
■ Clarification note added to failure condition 14-004
■ Clarification note added to checkpoint 28
■ Failure conditions 28-002, 28-004, 28-005 specified more precisely
■ Clarification note added to failure condition 31-010
■ Other minor changes include notes for clarity, minor editorial corrections and
PDF tagging using current best-practice.
Background
PDF is the electronic document format found worldwide in every corner of almost every organization
that uses computers. The value of PDF may be stated in terms of the capacity to deliver a stable and
trustworthy representation of a document.
Accordingly, PDF implementers have a special responsibility to ensure reliability and consistency by
following clear, specific and detailed industry and normative standards in the development of PDF
creation, modification and viewing software.
About PDF/UA
Ensuring content is accessible to users with disabilities presents broad and complex challenges in any
technology. ISO 14289-1 (PDF/UA-1) specifies technical requirements for PDF files to ensure a high-
quality and consistent reading experience when used by a variety of PDF/UA-conforming processors.
© 2021 PDF Association 4
PDF Association
Matterhorn Protocol Checkpoints
The Matterhorn Protocol is a set of 31 checkpoints comprised of 136 failure conditions encompassing file
format requirements specified in PDF/UA-1. 87 failure conditions can be determined by software alone,
47 failure conditions usually require human judgment. 2 failure conditions have no specific tests (23-001
and 27-001). Some failure conditions pertain to the document, some to the page and most to individual
objects such as tags, tables or annotations.
Key to the Headers in the Failure Conditions Tables
Index A numerical identifier for individual failure conditions within a given Checkpoint.
Failure Non-conforming condition present in the PDF file.
Condition
NOTE: Pathological software behavior (such as “flickering” by using a script to cause animation
effects via a series of actions) is not addressed.
Section A reference to the relevant section in PDF/UA on a paragraph level. “UA1” refers to the
PDF/UA-1 standard. The point-separated numbers after the colon refer to a clause in PDF/UA-1.
The digits following the hyphen identify a specific paragraph within the clause.
Type The nature of the tested item. Possible values are Doc for aspects of the document as a whole,
Page for pages inside the document, Object for individual data objects, JS for JavaScript
embedded in the document and All where all aspects of the document are affected.
How While not determinative the value of “How” generally indicates the realistic best-practice
approach at the present time. Some checkpoints may always be decided by M (Machine), some
usually or probably require H (Human) interaction.
See Certain failure conditions are covered in full by other failure conditions. Such cases are
indicated by an index reference in this column.
Additional Reading
Tagged PDF Best Practice Guide: Syntax,
■
https://www.pdfa.org/resource/tagged-pdf-best-practice-guide-syntax/
PDF/UA Reference Suite, https://www.pdfa.org/resource/pdfua-reference-suite/
■
PDF/UA in a Nutshell, https://www.pdfa.org/resource/pdfua-in-a-nutshell/
■
Other reading (superseded documents)
PDF/UA-1 Technical Implementation Guide: Understanding ISO 14289-1 (PDF/UA-1), https://www.
■
aiim.org/Global/AIIM_Widgets/Community_Widgets/Technical-Implementation-Guide-32000-1
Achieving WCAG 2.0 with PDF/UA, https://www.aiim.org/Global/AIIM_Widgets/Community_
■
Widgets/Achieving_WCAG
© 2021 PDF Association 5
PDF Association
PDF/UA-1 Failure Conditions
Checkpoint 01: Real content tagged
Index Failure Condition Section Type How See
01-001 Artifact is tagged as real content. UA1:7.1-1 Object H –
01-002 Real content is marked as artifact. UA1:7.1-1 Object H –
01-003 Content marked as Artifact is present inside tagged content. UA1:7.1-1 Object M –
01-004 Tagged content is present inside content marked as Artifact. UA1:7.1-1 Object M –
01-005 Content is neither marked as Artifact nor tagged as real content. UA1:7.1-2 Object M –
01-006 The structure type and attributes of a structure element are not UA1:7.1-2 Object H –
semantically appropriate for the structure element. All of the
following structure types must be taken into account:
<Document>, <Part>, <Art>, <Sect>, <Div>, <BlockQuote>,
<Caption>, <TOC>, <TOCI>, <Index>, <NonStruct>, <Private>,
<P>, <H>, <H1>, <H2>, <H3>, <H4>, <H5>, <H6>, <L>, <LI>, <Lbl>,
<LBody>, <Table>, <TR>, <TH>, <TD>, <THead>, <TBody, <TFoot,
<Span>, <Quote>, <Note>, <Reference>, <BibEntry>, <Code>,
<Link>, <Annot>, <Ruby>, <Warichu>, <RB>, <RT>, <RP>, <WT>,
<WP>, <Figure>, <Formula>, <Form>.
NOTE 1: Structure type is not semantically appropriate if the
nature of the content inside the structure element does not
match the structure type of the structure element.
NOTE 2: For any non-standard structure types, the standard
structure type to which the type is role-mapped shall be used for
validation.
NOTE 3: Tables are regular when the number of logical cells is
equal in each row after accounting for RowSpan and ColSpan
attributes.
While PDF/UA-1 does not prohibit irregular tables, irregular tables
are almost always a strong indicator of improper table structure.
It may be a good idea to raise a warning when such tables are
encountered, but it is not required by the Matterhorn Protocol.
NOTE 4: The value of table cell attributes is a function of the cell’s
semantic role in the table’s structure. Therefore, a <TH> cell may
not include a Scope attribute with an inappropriate value.
01-007 Suspects entry has a value of true. UA1:7.1-11 Doc M –
© 2021 PDF Association 6
PDF Association
Checkpoint 02: Role Mapping
Index Failure Condition Section Type How See
02-001 One or more non-standard tag’s mapping does not UA1:7.1-3 Doc M –
terminate with a standard type.
NOTE: Although PDF/UA defines the nomenclature
for heading levels above <H6> (<Hn>), these are not
standard structure types (as defined in ISO 32000-1) and
therefore <Hn> tags must (PDF/UA-1 7.1, paragraph 1) be
role-mapped to a standard structure type. According to
PDF/UA-1, PDF/UA-conforming processors are expected
to ignore such mappings and respect the heading level.
02-002 The mapping of one or more non-standard types is UA1:7.1-3 Doc H –
semantically inappropriate.
02-003 A circular mapping exists UA1:7.1-3 Doc M –
02-004 One or more standard types are remapped. UA1:7.1-4 Doc M –
NOTE: All Failure Conditions in Checkpoint 02 apply to entries in the role map dictionary regardless of
whether a given tag is used in the structure tree or not.
Checkpoint 03: Flickering
Index Failure Condition Section Type How See
03-001 One or more Actions lead to flickering. UA1:7.1-5 Page H –
03-002 One or more multimedia objects contain flickering content. UA1:7.1-5 Object H –
03-003 One or more JavaScript actions lead to flickering. UA1:7.1-5 JS H –
Checkpoint 04: Color and Contrast
Index Failure Condition Section Type How See
04-001 Information is conveyed by contrast, color, format or UA1:7.1-6 Object H –
layout, or some combination thereof but the content is
not tagged to reflect all meaning conveyed by the use of
contrast, color, format or layout, or some combination
thereof.
© 2021 PDF Association 7
PDF Association
Checkpoint 05: Sound
Index Failure Condition Section Type How See
05-001 Media annotation present, but audio content not UA1:7.1-7 Object H –
available in another form.
NOTE 1: An example of another form is a transcript.
05-002 Audio annotation present, but content not UA1:7.1-7 Object H –
available in another form.
NOTE 2: An example of another form is a transcript.
05-003 JavaScript uses beep function but does not UA1:7.1-7 JS H –
provide another means of notification.
Checkpoint 06: Metadata
Index Failure Condition Section Type How See
06-001 Document does not contain an XMP metadata UA1:7.1-8 Doc M –
stream
06-002 The XMP metadata stream in the Catalog UA1:5 Doc M –
dictionary does not include the PDF/UA identifier.
06-003 XMP metadata stream does not contain dc:title UA1:7.1-8 Doc M –
06-004 dc:title does not clearly identify the document UA1:7.1-8 Doc H –
Checkpoint 07: Dictionary
Index Failure Condition Section Type How See
07-001 ViewerPreferences dictionary of the Catalog UA1:7.1-9 Doc M –
dictionary does not contain a DisplayDocTitle
entry.
07-002 ViewerPreferences dictionary of the Catalog UA1:7.1-9 Doc M –
dictionary contains a DisplayDocTitle entry with a
value of false.
Checkpoint 08: OCR Validation
Index Failure Condition Section Type How See
08-001 OCR-generated text contains significant errors. UA1:7.1-10 Page H –
08-002 OCR-generated text is not tagged UA1:7.1-10 Page H 01-006
© 2021 PDF Association 8
PDF Association
Checkpoint 09: Appropriate Tags
Index Failure Condition Section Type How See
09-001 Tags are not in logical reading order. UA1:7.2-1 Doc H –
09-002 Structure elements are nested in a semantically UA1:7.2-1 Object H –
inappropriate manner. (e.g., a table inside a
heading).
09-003 The structure type (after applying any role- UA1:7.2-1 Object H 01-006
mapping as necessary) of a structure element is not
semantically appropriate.
09-004 A table-related structure element is used in a way UA1:7.2-1 Object M –
that does not conform to the syntax defined in ISO
32000-1, Table 337.
09-005 A list-related structure element is used in a way UA1:7.2-1 Object M –
that does not conform to Table 336 in ISO 32000-1.
09-006 A TOC-related structure element is used in a way UA1:7.2-1 Object M –
that does not conform to Table 333 in ISO 32000-1.
09-007 A Ruby-related structure element is used in a way UA1:7.2-1 Object M –
that does not conform to Table 338 in ISO 32000-1.
09-008 A Warichu-related structure element is used in UA1:7.2-1 Object M –
a way that does not conform to Table 338 in ISO
32000-1.
Checkpoint 10: Character Mappings
Index Failure Condition Section Type How See
10-001 Character code cannot be mapped to Unicode. UA1:7.2-2 Object M –
NOTE: Unicode mapping requirements are specified in ISO 32000-1:2008, 14.8.2.4 “Extraction of
character properties”.
© 2021 PDF Association 9
PDF Association
Checkpoint 11: Declared Natural Language
Index Failure Condition Section Type How See
11-001 Natural language for text in page content cannot be UA1:7.2-3 Object M –
determined.
11-002 Natural language for text in Alt, ActualText and UA1:7.2-3 Object M –
E attributes cannot be determined.
11-003 Natural language in the Outline entries cannot be UA1:7.2-3 Object M –
determined.
11-004 Natural language in the Contents entry for annotations UA1:7.2-3 Object M –
cannot be determined.
11-005 Natural language in the TU entry for form fields cannot UA1:7.2-3 Object M –
be determined.
11-006 Natural language for document metadata cannot be UA1:7.2-3 Doc M –
determined.
11-007 Natural language is not appropriate. UA1:7.2-3 All H –
Checkpoint 12: Stretchable Characters
Index Failure Condition Section Type How See
12-001 Stretched characters are not represented appropriately. UA1:7.2-4 Object H –
Checkpoint 13: Graphics
Index Failure Condition Section Type How See
13-001 Graphics objects other than text objects and artifacts UA1:7.3-1 Object H –
are not tagged with a <Figure> tag.
13-002 A link with a meaningful background does not include UA1:7.3-1 Object H –
alternative text describing both the link and the
graphic’s purpose.
13-003 A caption is not tagged with a <Caption> tag. UA1:7.3-2 Object H –
13-004 <Figure> tag alternative or replacement text missing. UA1:7.3-3 Object M –
13-005 ActualText used for a <Figure> for which alternative UA1:7.3-4 Object H –
text is more appropriate.
13-006 Graphics objects that possess semantic value only UA1:7.3-5 Object H –
within a group of graphics objects is tagged on its own.
13-007 A more accessible representation is not used. UA1:7.3-6 Object H –
13-008 ActualText not present when a <Figure> is intended to UA1:7.3-4 Object H –
be consumed primarily as text.
© 2021 PDF Association 10
PDF Association
Checkpoint 14: Headings
Index Failure Condition Section Type How See
14-001 Headings are not tagged. UA1:7.4-1 Doc H 01-006
14-002 Does use numbered headings, but the first UA1:7.4.2-1 Doc M –
heading tag is not <H1>.
14-003 Numbered heading levels in descending UA1:7.4-1 Doc M –
sequence are skipped (Example: <H3> follows
directly after <H1>).
14-004 Numbered heading tags do not use Arabic UA1:7.4.3-1 Object H 01-006
numerals and are not role mapped to heading
types that do use Arabic numerals.
NOTE 1: A human is required to validate that the
custom structure element is intended to be a
heading element.
Note 2: The rule requiring Arabic numerals for
headings applies to the heading subtype for
the structure element or, if role mapped, to its
eventual heading target.
14-005 Content representing a 7th level (or higher) UA1:7.4.3-1 Object H 01-006
heading does not use an <H7> (or higher) tag.
14-006 A node contains more than one <H> tag. UA1:7.4.4-1 Object M –
14-007 Document uses both <H> and <H#> tags. UA1:7.4.4-3 Doc M –
NOTE 3: In weakly-structured documents,
headings always take the form <Hn> (e.g., <H1>,
<H2>, <Hn>) without intervening whitespace or
numerical separators.
© 2021 PDF Association 11
PDF Association
Checkpoint 15: Tables
Index Failure Condition Section Type How See
15-001 A row has a header cell, but that header cell is not UA1:7.5-1 Object H –
tagged as a header.
15-002 A column has a header cell, but that header cell is UA1:7.5-1 Object H –
not tagged as a header.
15-003 In a table not organized with Headers attributes UA1:7.5-2 Object M –
and IDs, a <TH> cell does not contain a Scope
attribute.
15-004 Content is tagged as a table for information that is UA1:7.5-3 Object H –
not organized in rows and columns.
15-005 A given cell’s header cannot be unambiguously UA1:7.5-2 Object H 01-006
determined.
Checkpoint 16: Lists
Index Failure Condition Section Type How See
16-001 List is an ordered list, but no value for the UA1:7.6-1 Object H –
ListNumbering attribute is present.
16-002 List is an ordered list, but the ListNumbering UA1:7.6-1 Object H –
value is not one of the following: Decimal,
UpperRoman, LowerRoman, UpperAlpha,
LowerAlpha.
16-003 Content is a list but is not tagged as a list. UA1:7.6-2 Object H 01-006
Checkpoint 17: Mathematical Expressions
Index Failure Condition Section Type How See
17-001 Content is a mathematical expression but is not UA1:7.7-1 Object H 01-006
tagged with a <Formula> tag.
17-002 <Formula> tag is missing an Alt attribute. UA1:7.7-1 Object M –
17-003 Unicode mapping requirements are not met. UA1:7.7-2 Object M 10-001
© 2021 PDF Association 12
PDF Association
Checkpoint 18: Page Headers and Footers
Index Failure Condition Section Type How See
18-001 Headers and footers are not marked as pagination UA1:7.8-1 Object H –
artifacts.
18-002 Header or footer artifacts are not classified as UA1:7.8-1 Object H –
Header or Footer subtypes.
Checkpoint 19: Notes and References
Index Failure Condition Section Type How See
19-001 Footnotes or endnotes are not tagged as <Note>. UA1:7.9-1 Object H –
19-002 References are not tagged as <Reference>. UA1:7.9-1 Object H –
19-003 ID entry of the <Note> tag is not present. UA1:7.9-2 Object M –
19-004 ID entry of the <Note> tag is non-unique. UA1:7.9-2 Object M –
Checkpoint 20: Optional Content
Index Failure Condition Section Type How See
20-001 Name entry is missing or has an empty string as UA1:7.10-1 Object M –
its value in an Optional Content Configuration
Dictionary in the Configs entry in the
OCProperties entry in the Catalog dictionary.
20-002 Name entry is missing or has an empty string as UA1:7.10-1 Object M –
its value in an Optional Content Configuration
Dictionary that is the value of the D entry in the
OCProperties entry in the Catalog dictionary.
20-003 An AS entry appears in an Optional Content UA1:7.10-2 Object M –
Configuration Dictionary.
Checkpoint 21: Embedded Files
Index Failure Condition Section Type How See
21-001 The file specification dictionary for an embedded UA1:7.11-1 Object M –
file does not contain F and UF entries.
Checkpoint 22: Article Threads
Index Failure Condition Section Type How See
22-001 Article threads do not reflect logical reading order. UA1:7.12-1 Object H –
© 2021 PDF Association 13
PDF Association
Checkpoint 23: Digital Signatures
Index Failure Condition Section Type How See
23-001 No test specific to digital signatures is required, UA1:7.13-1 -- -- 01-006
however other provisions apply (form fields).
Checkpoint 24: Non-Interactive Forms
Index Failure Condition Section Type How See
24-001 Non-interactive forms are not tagged with the UA1:7.14-1 Object H –
PrintFields attribute.
Checkpoint 25: XFA
Index Failure Condition Section Type How See
25-001 File contains the dynamicRender element with UA1:7.15-1 Object M –
value “required”.
Checkpoint 26: Security
Index Failure Condition Section Type How See
26-001 The file is encrypted but does not contain a P UA1:7.16-1 Object M –
entry in its encryption dictionary.
26-002 The file is encrypted and does contain a P entry UA1:7.16-1 Object M –
but the 10th bit position of the P entry is false.
Checkpoint 27: Navigation
Index Failure Condition Section Type How See
27-001 No tests specific to navigation are required; use UA1:7.17-1 -- -- 01-006
appropriate semantics.
© 2021 PDF Association 14
PDF Association
Checkpoint 28: Annotations
Clause 7.18 in PDF/UA-1 (14289-1) is not applicable to annotations whose hidden flag is set or whose
rectangle is outside the CropBox or whose Subtype is Popup. In all these cases, the rules of checkpoint
28 do not apply.
Index Failure Condition Section Type How See
28-001 An annotation is not in correct reading order. UA1:7.18.1-2 Object H –
28-002 An annotation, other than of subtype Widget, Link UA1:7.18.1-2 Object M 28-010,
and PrinterMark, is not a direct child of an <Annot> 28-011,
structure element. 28-017,
28-018
28-003 An annotation is used for visual formatting but is UA1:7.18.1-3 Object H –
not tagged according to its semantic function.
28-004 An annotation, other than of subtype Widget, does UA1:7.18.1-4 Object M –
not have a Contents entry and does not have an
alternative description (in the form of an Alt entry
in the enclosing structure element).
28-005 A form field does not have a TU entry and does not UA1:7.18.1-4 Object M –
have an alternative description (in the form of an
Alt entry in the enclosing structure element).
28-006 An annotation with subtype undefined in ISO 32000 UA1:7.18.2-1 Object M 28-001,
does not meet 7.18.1. 28-002,
28-003,
28-004
28-007 An annotation of subtype TrapNet exists. UA1:7.18.2-2 Object M –
28-008 A page containing an annotation does not contain a UA1:7.18.3-1 Object M –
Tabs entry.
28-009 A page containing an annotation has a Tabs entry UA1:7.18.3-1 Object M –
with a value other than S.
28-010 A widget annotation is not nested within a <Form> tag. UA1:7.18.4-1 Object M –
28-011 A link annotation is not nested within a <Link> tag. UA1:7.18.5-1 Object M –
28-012 A link annotation does not include an alternate UA1:7.18.5-2 Object M –
description in its Contents entry.
28-013 An IsMap entry is present with a value of true but UA1:7.18.5-3 Object H –
the functionality is not provided in some other way.
© 2021 PDF Association 15
PDF Association
Index Failure Condition Section Type How See
28-014 CT entry is missing from the media clip data UA1:7.18.6.2-1 Object M –
dictionary.
28-015 Alt entry is missing from the media clip data UA1:7.18.6.2-1 Object M –
dictionary.
28-016 File attachment annotations do not conform UA1:7.18.7-1 Object M 20-001
to 7.11.
28-017 A PrinterMark annotation is included in the logical UA1:7.18.8-1 Object M –
structure.
28-018 The appearance stream of a PrinterMark UA1:7.18.8-2 Object M 01-002,
annotation is not marked as Artifact. 01-005
Checkpoint 29: Actions
Index Failure Condition Section Type How See
29-001 A script requires specific timing for individual UA1:7.19-1 Object H –
keystrokes.
Checkpoint 30: XObjects
Index Failure Condition Section Type How See
30-001 A reference XObject is present. UA1:7.20-1 Object M –
30-002 Form XObject contains MCIDs and is referenced UA1:7.20-2 Object M –
more than once.
Checkpoint 31: Fonts
Index Failure Condition Section Type How See
31-001 A Type 0 font dictionary with encoding other than UA1:7.21.3-1 Object M –
Identity-H and Identity-V has values for Registry
in both CIDSystemInfo dictionaries that are not
identical.
31-002 A Type 0 font dictionary with encoding other than UA1:7.21.3.1-1 Object M –
Identity-H and Identity-V has values for Ordering
in both CIDSystemInfo dictionaries that are not
identical.
© 2021 PDF Association 16
PDF Association
Index Failure Condition Section Type How See
31-003 A Type 0 font dictionary with encoding other UA1:7.21.3.1-1 Object M –
than Identity-H and Identity-V has a value for
Supplement in the CIDSystemInfo dictionary
of the CID font that is less than the value for
Supplement in the CIDSystemInfo dictionary of
the CMap.
31-004 A Type 2 CID font contains neither a stream nor the UA1:7.21.3.2-1 Object M –
name Identity as the value of the CIDToGIDMap
entry.
31-005 A Type 2 CID font does not contain a CIDToGIDMap UA1:7.21.3.2-1 Object M –
entry.
31-006 A CMap is neither listed as described in ISO 32000- UA1:7.21.3.3-1 Object M –
1:2008, 9.7.5.2, Table 118 nor is it embedded.
31-007 The WMode entry in a CMap dictionary is not UA1:7.21.3.3-1 Object M –
identical to the WMode value in the CMap stream.
31-008 A CMap references another CMap which is not UA1:7.21.3.3-2 Object M –
listed in ISO 32000-1:2008, 9.7.5.2, Table 118.
NOTE 1: For more information see ISO 32000-1
9.7.5.3, UseCMap entry.
31-009 For a font used by text intended to be rendered the UA1:7.21.4.1-1 Object M –
font program is not embedded.
NOTE 2: A glyph is used for rendering if the text
render mode is not 3 (text render mode 3 is used
for invisible text).
31-010 A font program is embedded that is not legally UA1:7.21.4.1-2 Object H –
embeddable for unlimited, universal rendering.
NOTE 3: Although machines may detect relevant
flags, this may not correspond to actual legal
circumstances.
31-011 For a font used by text the font program is UA1:7.21.4.1-3 Object M –
embedded but it does not contain glyphs for
all of the glyphs referenced by the text used for
rendering.
NOTE 4: A glyph is used for rendering if the text
render mode is not 3 (text render mode 3 is used
for invisible text).
© 2021 PDF Association 17
PDF Association
Index Failure Condition Section Type How See
31-012 The FontDescriptor dictionary of an embedded UA1:7.21.4.2-1 Object M –
Type 1 font contains a CharSet string, but at least
one of the glyphs present in the font program is not
listed in the CharSet string.
31-013 The FontDescriptor dictionary of an embedded UA1:7.21.4.2-2 Object M –
Type 1 font contains a CharSet string, but at least
one of the glyphs listed in the CharSet string is not
present in the font program.
31-014 The FontDescriptor dictionary of an embedded UA1:7.21.4.2-3 Object M –
CID font contains a CIDSet string, but at least one
of the glyphs present in the font program is not
listed in the CIDSet string.
31-015 The FontDescriptor dictionary of an embedded UA1:7.21.4.2-4 Object M –
CID font contains a CIDSet string, but at least
one of the glyphs listed in the CIDSet string is not
present in the font program.
31-016 For one or more glyphs, the glyph width UA1:7.21.5-1 Object M –
information in the font dictionary and in the
embedded font program differ by more than
1/1000 unit.
31-017 A non-symbolic TrueType font is used for UA1:7.21.6-1 Object M –
rendering, but none of the cmap entries in the
embedded font program is a non-symbolic cmap.
31-018 A non-symbolic TrueType font is used for rendering, but UA1:7.21.6-2 Object M –
for at least one glyph to be rendered the glyph cannot be
looked up by any of the non-symbolic cmap entries in
the embedded font program.
31-019 The font dictionary for a non-symbolic TrueType UA1:7.21.6-3 Object M –
font does not contain an Encoding entry.
31-020 The font dictionary for a non-symbolic TrueType UA1:7.21.6-4 Object M –
font contains an Encoding dictionary which does
not contain a BaseEncoding entry.
31-021 The value for either the Encoding entry or the UA1:7.21.6-5 Object M –
BaseEncoding entry in the Encoding dictionary in
a non-symbolic TrueType font dictionary is neither
MacRomanEncoding nor WinAnsiEncoding.
© 2021 PDF Association 18
PDF Association
Index Failure Condition Section Type How See
31-022 The Differences array in the Encoding entry in a UA1:7.21.6-6 Object M –
non-symbolic TrueType font dictionary contains
one or more glyph names which are not listed in
the Adobe Glyph List.
31-023 The Differences array is present in the Encoding UA1:7.21.6-7 Object M –
entry in a non-symbolic TrueType font dictionary
but the embedded font program does not contain a
(3,1) Microsoft Unicode cmap.
31-024 The Encoding entry is present in the font UA1:7.21.6-8 Object M –
dictionary for a symbolic TrueType font.
31-025 The embedded font program for a symbolic UA1:7.21.6-9 Object M –
TrueType font contains no cmap.
31-026 The embedded font program for a symbolic UA1:7.21.6-10 Object M –
TrueType font contains more than one cmap,
but none of the cmap entries is a (3,0) Microsoft
Symbol cmap.
31-027 A font dictionary does not contain the ToUnicode UA1:7.21.7-1 Object M –
entry and none of the following is true:
■ the font uses MacRomanEncoding,
MacExpertEncoding or WinAnsiEncoding
■ the font is a Type 1 or Type 3 font and the
glyph names of the glyphs referenced are all
contained in the Adobe Glyph List or the set
of named characters in the Symbol font, as
defined in ISO 32000-1:2008, Annex D
■ the font is a Type 0 font, and its descendant
CIDFont uses Adobe-GB1, Adobe-CNS1,
Adobe-Japan1 or Adobe-Korea1 character
collections
■ the font is a non-symbolic TrueType font
31-028 One or more Unicode values specified in the UA1:7.21.7-2 Object M –
ToUnicode CMap are zero (0).
31-029 One or more Unicode values specified in the UA1:7.21.7-3 Object M –
ToUnicode CMap are equal to either U+FEFF or
U+FFFE.
31-030 One or more characters used in text showing UA1:7.21.8-1 Object M –
operators reference the .notdef glyph.
© 2021 PDF Association 19