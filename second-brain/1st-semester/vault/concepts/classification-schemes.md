---
title: "Classification Schemes"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Classification Schemes (CS) in MPEG-7 are standardized taxonomies that provide controlled vocabularies for consistent naming and categorization of multimedia metadata.

## Core Intuition
Without controlled vocabularies, different systems would use different terms for the same concept ("jpeg" vs "JPEG" vs "JFIF"). Classification Schemes solve this by defining a fixed set of terms with unique IDs, ensuring interoperability. They are essentially standardized dictionaries embedded in the MPEG-7 schema.

## Formal Definition / Statement
Classification Schemes are XML-based taxonomies integrated into MPEG-7 for:
- Consistent naming of persons, objects, file formats, genres, etc.
- Integration of taxonomies into MPEG-7 descriptions
- Controlled vocabularies for metadata fields

**Example: FileFormatCS**
```xml
<ClassificationScheme uri="urn:mpeg:mpeg7:cs:FileFormatCS:2001"
  domain="//MediaInformation/MediaProfile/MediaFormat/FileFormat">
  <Term termID="1">
    <Name xml:lang="en">jpeg</Name>
    <Name xml:lang="en">jpg</Name>
    <Name xml:lang="en">jfif</Name>
    <Definition xml:lang="en">JPEG file format</Definition>
  </Term>
  <Term termID="2">
    <Name xml:lang="en">JPEG 2000</Name>
    <Definition xml:lang="en">JPEG 2000 file format</Definition>
  </Term>
</ClassificationScheme>
```

CS exist for: parental rating, genre, quality, semantic relations, file format, and more.
New CS must be registered with the MPEG-7 organisation.

## Key Properties / Complexity
- Each term has a unique `termID` within its CS
- Terms can have multiple names (aliases) and definitions
- CS are referenced by URI (e.g., `urn:mpeg:mpeg7:cs:FileFormatCS:2001`)
- New CS require registration — ensures consistency across implementations
- CS are used in both structural and semantic descriptions

## Worked Example
The SemanticRelationCS defines relationships between semantic entities:
- `key` — "B is a key for accessing A"
- `keyFor` — inverse of key
- `annotates` — "A is an annotation of B"
- `agent` — "A performs the action"
- `accompanier` — "A accompanies B"

These are used in [[mpeg-7-semantic-description]] to link events, agents, and objects.

## Common Pitfalls
- Confusing CS with ontologies — CS are simpler flat/hierarchical taxonomies, not full ontological models
- Forgetting that CS are closed-world — terms not in the CS cannot be used
- Assuming CS are universal — different domains may need different CS

## Connections
- [[mpeg-7]] — CS are integral to the MPEG-7 standard
- [[mpeg-7-semantic-description]] — SemanticRelationCS enables structured semantic relations
- [[multimedia-metadata]] — CS provide controlled vocabularies for metadata fields
- [[mpeg-7-indexing-pyramid]] — CS are primarily used at higher (semantic) pyramid levels

## Open Questions
- How do MPEG-7 CS compare to modern ontology standards (OWL, SKOS)?
- Can CS be automatically extended using machine learning?
- Are CS still maintained and updated?
