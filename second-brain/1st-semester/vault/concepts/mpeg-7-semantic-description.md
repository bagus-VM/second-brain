---
title: "MPEG-7 Semantic Description"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
MPEG-7 semantic description tools enable the representation of meaning — events, agents, places, times, and their relationships — attached to multimedia content segments.

## Core Intuition
Structural description tells you "what is where" (segments, regions, time ranges). Semantic description tells you "what it means" — who is in the scene, what event is happening, where and when it takes place. This is the high-level end of the [[mpeg-7-indexing-pyramid]] (levels 5–10), where world knowledge meets multimedia data.

## Formal Definition / Statement
The SemanticType hierarchy includes:

- **SemanticBase** (abstract) — base type for all semantic elements
  - **ObjectType** — objects depicted in the content
    - **AgentObjectType** — person, group, or organisation
  - **EventType** — events/actions occurring in the content
  - **SemanticPlaceType** — location of events in the narrative world
  - **SemanticTimeType** — time frame of scenes (numerical or textual)
  - **SemanticStateType** — states of objects

**Semantic Relations** are defined via Classification Schemes (CS):
- `agent` — who performs an action
- `accompanier` — who accompanies
- `key` / `keyFor` — access relationships
- `annotates` — annotation relationships

**Integration with structure**: The `<Semantic>` or `<SemanticRef>` element can be embedded in any SegmentType, linking structural segments to their meaning.

## Key Properties / Complexity
- AgentObject describes persons with structured fields (GivenName, FamilyName)
- SemanticPlace uses Place/Region/PostalAddress structure
- SemanticTime uses SemanticTimeInterval with displacement and direction
- Events can reference multiple agents and objects via Relation elements
- Classification Schemes (CS) provide controlled vocabularies for semantic relations
- Semantic descriptions can be embedded directly or referenced via SemanticRef

## Worked Example
Describing a "handshake" event:
```xml
<SemanticBase xsi:type="EventType" id="EV1">
  <Label><Name>Shake hands</Name></Label>
  <Definition>
    <FreeTextAnnotation>Clasping of right hands by two people.</FreeTextAnnotation>
  </Definition>
  <Relation type="...SemanticRelationCS...agent" target="#AOa"/>
  <Relation type="...SemanticRelationCS...accompanier" target="#AOb"/>
</SemanticBase>
```
This links an event (handshake) to two agent objects (Person A and Person B) using semantic relations.

## Common Pitfalls
- Confusing semantic description with annotation — semantic description uses structured MPEG-7 types, annotation is free-form text
- Assuming semantic descriptions are automatic — they typically require manual or semi-automatic creation
- Forgetting that semantic elements can reference structural segments (bridging structure and meaning)
- Ignoring that Classification Schemes must be registered with the MPEG-7 organisation

## Connections
- [[mpeg-7-structural-description]] — semantic descriptions attach to structural segments
- [[mpeg-7-indexing-pyramid]] — covers pyramid levels 5–10 (semantic)
- [[classification-schemes]] — provide controlled vocabularies for semantic relations
- [[multimedia-annotation]] — semantic description is a formalized form of annotation
- [[semantic-gap]] — semantic description is MPEG-7's approach to bridging the gap

## Open Questions
- Can semantic descriptions be automatically extracted from video using modern AI?
- How do MPEG-7 semantic types compare to knowledge graph ontologies?
- Is the MPEG-7 semantic model expressive enough for complex narrative structures?
