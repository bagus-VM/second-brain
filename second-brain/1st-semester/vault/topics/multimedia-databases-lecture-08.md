---
title: "Multimedia Databases - Lecture 08: Query Languages"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[sql-mm]]", "[[mpqf]]", "[[object-relational-databases]]"]
---

## One-line Summary
Lecture 08 covers multimedia query languages (MMQL): the history, categories, two representative approaches (MOQL extending OQL, SQL/MM extending SQL), the MPEG Query Format (MPQF) built from scratch, result presentation, and query processing with similarity-based algebra.

## Core Intuition
Standard SQL and OQL were designed for structured data. Multimedia queries need similarity search, spatial and temporal relations, fuzzy matching, and result presentation. Two strategies emerged: extend an existing language (SQL/MM extends SQL, MOQL extends OQL) or build from scratch (MPQF, VideoSQL). The lecture walks through both, then covers how results are presented and how queries are optimized.

## Key Topics

### 1. [[multimedia-query-languages]] Overview
- History 1980-2000: focus on image data (medical), spatial and similarity queries, SQL/OQL extensions
- History 2001-2011: multimodal, temporal queries, relevance feedback, SQL/MM and MPQF standards, fuzzy logic
- Two categories:
  1. Extensions of SQL/OQL: [[sql-mm]], [[moql]]
  2. From scratch: VideoSQL, [[mpqf]]
- Query types: exact (non-MM attributes), semantic (object/person occurrence), syntactic (resolution/framerate), similarity (low-level features), correlation (spatial/temporal)
- Requirements: universality, content-based, spatial, temporal, similarity, fuzzy, presentation

### 2. [[oql]] (Object Query Language)
- Based on ODMG object model
- Similar to SQL-92 with OO extensions: complex objects, object identity, path expressions, polymorphisms, function calls, late binding
- Basic construct: `select [distinct] projection_attributes from query [as identifier] where query`

### 3. [[moql]] (Multimedia Object Query Language)
- Extends OQL's WHERE clause with:
  - Spatial relations: point/line/region predicates (nearest, within, cross, coveredBy, directional: left/right/above/below/north/south...)
  - Temporal relations: Allen's 13 interval relations (equal, before, after, meet, overlap, during, starts, finishes...)
  - Contains relation
  - Presentation functions: `present` clause with layout (atWindow, play, parStart, display)
- VisualMOQL: implements the image part, part of DISIMA project
- Limitations: no audio support, prototype only on ObjectStore

### 4. [[sql-mm]] Details
- ISO/IEC 13249, self-contained part of SQL standard
- Part 1: Framework
- Part 2: Full Text. UDT `FullText` with `Contains` (boolean) and `Rank` (real value) methods. Contextual and conceptual search patterns.
- Part 3: Spatial. `ST_Geometry` hierarchy: ST_Point (0-dim), ST_Curve/ST_LineString/ST_CircularString (1-dim), ST_Surface/ST_Polygon (2-dim), ST_Multi* collections. SRID for spatial reference.
- Part 5: Still Image. UDT `SI_StillImage` with SI_content (BLOB), SI_format, SI_height, SI_width. Feature subtypes: SI_AverageColor, SI_ColorHistogram, SI_PositionalColor, SI_Texture. Each has SI_Score method (returns 0-1).
- Oracle and IBM DB2 base on SQL/MM concepts but use different syntax, no polymorphic ScoreFunction

### 5. [[mpqf]] (MPEG Query Format)
- International standard since 2008, Part 12 of MPEG-7
- XML-based, decoupled from specific metadata standard
- Three categories: Management (find the right MMRS), Input Query Format, Output Query Format
- Query structure: QFDeclaration (declare resources), OutputDescription (XPath-based result selection, grouping, sorting, paging), QueryCondition (modular filter, TargetMediaType, join)
- Scoring: preferenceValue, thresholdValue, scoringFunction for fuzzy boolean operators (AND/OR/XOR with t-norm/t-conorm)
- Sync/async mode, timeout functionality

### 6. Result Presentation
- More complex than traditional DB: spatial and temporal information needed
- SQL+D: multimedia and presentation extension for object-relational SQL
  - `DISPLAY panel main WITH a AS audio, v AS video ON main.Center(Overlay)`
  - Query interpreter separates DB content from display control

### 7. Query Processing and Optimization
- Requirements: data model for MM files, multimedia operations (similarity-based selection and join), formal algebra, optimization strategies
- Image data modeling: OR model M(id, O, F, A, P) linking image to features and semantic data
- Salient object support: S(ids, Fs, As) managing objects within images
- Similarity-based algebra enables query optimization for multi-criteria queries combining relational and similarity operations

## Worked Example: MOQL Video Query
Find the first film segment with person MrX from the video JamesB:
```sql
select firstClip(
  select c from JamesB.clips c
  where c contains MrX
  order by lowerBound(c.timestamp)
)
```
The temporal function `firstClip` wraps a subquery that filters clips by content (`contains MrX`) and orders by timestamp. This combines relational selection with temporal and content-based predicates in one expression.

## Connections
- [[oql]] → [[moql]] (MOQL extends OQL's WHERE clause)
- [[sql-mm]] → [[mpqf]] (two categories of MMQL: extension vs from-scratch)
- [[object-relational-databases]] (both SQL/MM and MOQL build on OR data models)
- [[nested-tables-vs-varrays]] — Oracle collection types used inside OR columns to hold feature vectors, key frames, etc.
- [[content-based-retrieval]] (query languages are the interface to CBR)
- [[multimedia-databases-lecture-06]] (modeling layer from L06 feeds into query languages)
- [[multimedia-databases-lecture-07]] (CBIR concepts from L07 are what these languages query)

## Exam-Relevant Key Points
- Two categories of MMQL and their representatives
- Five query types (exact, semantic, syntactic, similarity, correlation)
- Seven requirements for a MMQL
- MOQL's four extensions to OQL (spatial, temporal, contains, presentation)
- SQL/MM part structure and key UDTs (SI_StillImage, FullText, ST_Geometry)
- MPQF three categories and query structure (QFDeclaration, OutputDescription, QueryCondition)
- MPQF scoringFunction with t-norm/t-conorm
- Why similarity-based join is needed (Query 2 example: relational selection + similarity join)

## Open Questions
- Will SQL/MM gain wider adoption, or will vector databases replace it for similarity search?
- Can MPQF handle deep learning embeddings, or is it locked to MPEG-7 descriptors?
- How do you optimize multi-criteria queries that mix relational and similarity predicates?
