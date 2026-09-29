---
title: "Multimedia Query Predicates"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [multimedia-database-intro, structured-vs-unstructured-retrieval]
---

## One-line Summary
Multimedia queries use four types of predicates — attribute (metadata values), structure (temporal/spatial relations), spatial (layout properties like contains, adjoins), and semantic (content meaning via extracted features) — to express conditions across both structured and unstructured multimedia data.

## Core Intuition
A traditional SQL query only has attribute predicates: `WHERE price > 100`. But for multimedia, you need to ask questions like "find videos where a ball enters a goal followed by crowd cheering for 30 seconds" — that involves *time* (temporal structure), *space* (spatial layout), and *meaning* (semantic content). The multimedia query predicate taxonomy formalizes these different dimensions of querying, and a [[multimedia-database-intro|MMDBMS]] must support all four types.

## Formal Definition / Statement
Four predicate types for multimedia queries:

**1. Attribute predicates:**
- Concern attributes with precise values (like traditional DB attributes)
- Examples: "date of an image", "name of a show"
- Deterministic matching, handled by standard SQL

**2. Structure predicates:**
- Temporal predicates for time synchronization information
- Apply to continuous media (audio, video)
- Express temporal relations between media components
- Example: "Find all objects in which a jingle runs for the duration of an image"

**3. Spatial predicates:**
- Specify spatial layout properties of multimedia objects
- Operators: contains, is contained in, cuts, adjoins
- Example: "Find all images where a car is parked next to a tree"
- Can be combined with temporal predicates
- Example: "Find video segments where a ball is seen within a goal-box followed by crowd cheering lasting more than 30s"
- Can reference whole objects or subcomponents (requires complex object data model)

**4. Semantic predicates:**
- Target the semantic content of the data
- Represented by features extracted and stored per multimedia object
- Support uncertainty, proximity, and significance
- Example: "Find all videos in which two brothers shake hands"

## Key Properties / Complexity
- **Attribute predicates** are the easiest — standard DBMS handles them.
- **Structure predicates** require temporal reasoning (Allen's interval relations, etc.).
- **Spatial predicates** require spatial indexing and geometric reasoning.
- **Semantic predicates** are the hardest — they require feature extraction, possibly ML-based, and inherently involve uncertainty.
- **Combinability**: All four types can (and should) be combined in a single query.
- **Granularity**: Predicates can reference whole objects or subcomponents, if the data model supports complex objects.

## Worked Example
**Query: "Find all video segments from after 2023 where a goalkeeper catches a ball inside the penalty area, followed by crowd celebration lasting more than 10 seconds."**

| Predicate Type | Condition |
|---|---|
| Attribute | `date > 2023-01-01` |
| Semantic | "goalkeeper catches ball" (feature extraction + matching) |
| Spatial | "inside the penalty area" (spatial containment) |
| Structure (temporal) | "followed by crowd celebration" (temporal ordering) |
| Structure (temporal) | "lasting more than 10 seconds" (duration constraint) |

This single query exercises all four predicate types simultaneously.

## Common Pitfalls
- Treating semantic predicates as deterministic. Unlike attribute predicates, semantic matching involves uncertainty — "similar to" is a spectrum, not a binary.
- Confusing structure predicates with spatial predicates. Structure predicates are about *temporal* relations; spatial predicates are about *layout/position*.
- Forgetting that subcomponent predicates require a complex object data model. Simple flat schemas can't express "the ball *within* the goal-box *within* the video."
- Assuming users write these predicates directly. In practice, a GUI translates user interactions (clicking on a region, selecting a sample image) into formal predicates.

## Connections
- [[multimedia-database-intro]] — MMDBMS must support all predicate types
- [[structured-vs-unstructured-retrieval]] — attribute predicates = structured; semantic predicates = unstructured
- [[media-types-discrete-continuous]] — structure predicates specifically target continuous media
- [[multimedia-definition]] — spatial/temporal predicates relate to presentation dimensions

## Open Questions
- How are semantic predicates implemented in practice — traditional feature extraction (SIFT, colour histograms) vs deep learning embeddings?
- What query optimization strategies work when combining deterministic (attribute) and probabilistic (semantic) predicates?
- How does MPEG-7's description scheme relate to these predicate types?
