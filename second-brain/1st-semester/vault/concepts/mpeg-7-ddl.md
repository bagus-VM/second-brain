---
title: "MPEG-7 Description Definition Language"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The Description Definition Language (DDL) is the XML-Schema-based language that specifies the syntax of all MPEG-7 description tools, with MPEG-7-specific extensions for multimedia data types.

## Core Intuition
MPEG-7 needs a formal language to define what valid descriptions look like — what elements exist, what attributes they have, what values are allowed. The DDL is that language. It's essentially an XML Schema with multimedia-specific extensions (arrays, matrices, temporal types) that serve as the "grammar" for all MPEG-7 descriptions.

## Formal Definition / Statement
DDL (ISO/IEC 15938-2) specifies the syntax of MPEG-7 description tools. Its elements:

**Standard XML-Schema constructs:**
- Declaration of namespaces, elements, attributes, and types
- Structural properties: order and number of child elements
- Default, max/min values for attributes

**MPEG-7 specific extensions:**
- Array and matrix data types
- Temporal data types (e.g., `timePoint`)

The DDL defines:
- **Description Tools**: Descriptors (single piece of metadata syntax & semantics) and Description Schemes (structures combining multiple descriptors)
- **Root Element**: `<Mpeg7>` — topmost element containing either a `DescriptionUnit` (partial) or `Description` (complete)

## Key Properties / Complexity
- Based on W3C XML Schema with custom extensions
- Enables validation of MPEG-7 documents
- Supports extensibility through XML-Schema extension mechanisms
- Defines the type hierarchy (CompleteDescription → ContentDescription/ContentManagement/ContentAbstraction)

## Worked Example
The MPEG-7 root element definition:
```xml
<element name="Mpeg7">
  <complexType>
    <complexContent>
      <extension base="mpeg7:Mpeg7Type">
        <choice>
          <element name="DescriptionUnit" type="mpeg7:Mpeg7BaseType"/>
          <element name="Description" type="mpeg7:CompleteDescriptionType"
            minOccurs="1" maxOccurs="unbounded"/>
        </choice>
      </extension>
    </complexContent>
  </complexType>
</element>
```
Every valid MPEG-7 document must start with `<Mpeg7>` and contain either a DescriptionUnit or one or more Descriptions.

## Common Pitfalls
- Confusing DDL with the descriptions themselves — DDL is the schema, not the data
- Assuming DDL is purely standard XML Schema — it has MPEG-7-specific extensions
- Forgetting that DDL enables both validation and extensibility

## Connections
- [[mpeg-7]] — DDL is Part 2 of the MPEG-7 standard
- [[mpeg-7-structural-description]] — DDL defines the SegmentType hierarchy
- [[mpeg-7-semantic-description]] — DDL defines the SemanticType hierarchy
- [[mpeg-7-descriptors]] — DDL defines descriptor data types
- [[classification-schemes]] — DDL defines how CS are structured

## Open Questions
- Would JSON Schema or other modern schema languages be more practical today?
- How does the DDL handle versioning and backward compatibility?
