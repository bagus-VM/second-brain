---
title: "XML and Structured Text"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [ascii-unicode-character-encoding]
---

## One-line Summary
XML (Extensible Markup Language) is a platform-independent, **self-describing markup language for representing structured data**, defined as a subset of SGML that combines SGML's flexibility with HTML's wide acceptance.

## Core Intuition
Plain text (ASCII/Unicode) stores characters, but says nothing about *structure*. Markup text separates content from presentation by embedding structural tags. XML takes this further: it lets you define your own tags to describe *any* data structure (not just document formatting). This makes XML an "ideal medium" for exchanging documents and data between heterogeneous systems — a critical requirement for multimedia databases that must interoperate across platforms.

## Formal Definition / Statement
- **SGML** (Standard Generalized Markup Language): the parent standard for structured document markup.
- **HTML**: a specific SGML application for web documents — fixed tag set, presentation-oriented.
- **XML**: a subset of SGML designed for:
  1. **Flexibility and performance** of SGML
  2. **Wide acceptance** of HTML
- XML is defined by the W3C (since 1996). It is:
  - Platform-independent
  - Open standard (self-describing documents)
  - Extensible (users define their own tags and schema)

**Well-formedness rules:**
1. Exactly one root element
2. All elements form a single hierarchical tree under the root
3. No invalid characters (must conform to the encoding specified in the prolog)
4. All tags must be properly nested and closed

**Validation:**
- Well-formedness ≠ validity
- A document is *valid* if it conforms to a **DTD** (Document Type Definition) or **XML Schema**
- Only well-formed documents can be validated
- Without DTD/Schema, a document can only be checked for well-formedness

## Key Properties / Complexity
- **Self-describing**: tags describe the meaning of data, not just its presentation.
- **Hierarchical tree structure**: every element has exactly one parent (except root).
- **Separation of form and content**: unlike early HTML, XML cleanly separates structure from presentation.
- **Namespaces**: allow combining vocabularies from different XML applications without tag name conflicts.
- **Text operations on XML**: character/string operations, editing, formatting, pattern recognition, sorting, compression (e.g., Huffman coding), encryption (e.g., DES, public-key).

## Worked Example
A simple XML document describing a multimedia object:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<multimedia-object>
  <title>Lecture Recording</title>
  <media type="video">
    <format>MP4</format>
    <codec>H.264</codec>
    <duration unit="seconds">3600</duration>
  </media>
  <media type="audio">
    <format>AAC</format>
    <sampling-rate unit="Hz">44100</sampling-rate>
  </media>
</multimedia-object>
```

Well-formedness check:
- Single root: `<multimedia-object>` ✓
- Hierarchical tree: all elements nested under root ✓
- Valid UTF-8 encoding ✓
- All tags properly closed ✓

## Common Pitfalls
- Confusing well-formedness with validity: a document can be well-formed XML but invalid against its DTD/Schema.
- Thinking XML = HTML: HTML has fixed tags and is forgiving of errors; XML has user-defined tags and *must* be well-formed (parsers reject malformed documents).
- Ignoring the encoding declaration: the prolog `<?xml version="1.0" encoding="UTF-8"?>` is critical — without it, parsers may misinterpret character encoding.
- Overusing XML for data that would be better represented in JSON or binary formats — XML's verbosity adds overhead.

## Connections
- [[ascii-unicode-character-encoding]] — XML documents are encoded in Unicode (typically UTF-8); the prolog specifies the encoding
- [[multimedia-database-intro]] — XML is used for metadata representation and data exchange in multimedia systems
- [[video-formats-container-vs-codec]] — XML is used in MPEG-7 for video metadata descriptions
- [[multimedia-databases-lecture-03]] — SVG (covered in lecture 3) is an XML-based format for vector graphics
- [[multimedia-definition]] — structured text/XML is a discrete media type

## Open Questions
- How does XML Schema compare to DTD in terms of expressiveness and validation power?
- What role does XML play in modern multimedia metadata standards like MPEG-7?
- Is JSON replacing XML for data exchange in multimedia databases, or do they serve different niches?
