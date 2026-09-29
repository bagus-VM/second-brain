---
title: "Multimedia Databases - Lecture 06: Modeling"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---
 
## One-line Summary
Lecture 06 covers multimedia data modeling — how to annotate, describe, and structure multimedia content using metadata standards, with MPEG-7 as the comprehensive framework spanning from low-level features to high-level semantics.

## Core Intuition
Raw multimedia data (pixels, audio samples) is meaningless without structured description. This lecture addresses the fundamental question: "How do we represent multimedia content in a database so it can be searched, compared, and managed?" The answer involves three pillars: annotation (labeling content), metadata (structured descriptions), and MPEG-7 (the standardized framework that unifies everything).

## Key Topics

### 1. [[multimedia-annotation]]
- Associating textual labels/tags to multimedia objects
- Manual, automatic, or semi-automatic
- Two fundamental challenges:
  - [[sensory-gap]]: gap between real-world objects and recordings
  - [[semantic-gap]]: gap between extractable features and human interpretation

### 2. [[multimedia-metadata]]
- "Data about data" — structured information describing multimedia resources
- Categories: content description, administrative, structural, legal, technical, low-level features
- Storage: extrinsic (independent database) vs. intrinsic (embedded, e.g., EXIF)
- Issues: interoperability, digital preservation, transmission, relevance

### 3. [[mpeg-7]] (ISO/IEC 15938)
- International standard for multimedia metadata (since 2001, v2 in 2006)
- 12 parts covering: Systems, DDL, Visual, Audio, MDS, Reference Software, etc.
- Three pillars:
  - [[mpeg-7-ddl]] — Description Definition Language (XML-Schema based)
  - [[mpeg-7-structural-description]] — spatial/temporal/spatio-temporal segmentation
  - [[mpeg-7-semantic-description]] — events, agents, places, times

### 4. [[mpeg-7-indexing-pyramid]]
- 10-level framework from syntactic to semantic
- Syntactic levels (1–4): Type/Technique, Global Distribution, Local Structure, Global Composition
- Semantic levels (5–10): Generic/Specific Objects/Scenes, Abstract Objects/Scenes

### 5. [[mpeg-7-descriptors]]
- 20 visual descriptor types: Color (7), Texture (3), Shape (3), Motion (4), Localization (2), Face (1)
- Standardized numerical representations of visual properties
- Examples: ScalableColor, DominantColor, EdgeHistogram, MotionActivity

### 6. [[classification-schemes]]
- Standardized taxonomies for controlled vocabularies
- Used for consistent naming across MPEG-7 descriptions
- Examples: FileFormatCS, SemanticRelationCS, GenreCS

### 7. Related Concepts (from other lectures, cross-linked)
- [[feature-extraction]] — computing low-level features from raw data
- [[content-based-retrieval]] — searching by content features, not just text
- [[similarity-measures]] — quantifying how "close" two multimedia objects are
- [[relevance-feedback]] — iterative user-guided refinement of retrieval

## Worked Example: Complete MPEG-7 Workflow
1. **Annotate**: User describes a video as "Worldcup Soccer"
2. **Extract features**: Compute color histograms, motion activity per segment
3. **Structure**: Decompose video into temporal segments (shots)
4. **Describe semantically**: Tag segments with events ("goal", "celebration"), agents ("player X"), places ("stadium")
5. **Store**: Save MPEG-7 descriptions alongside the video
6. **Retrieve**: User queries "find goals" → system matches semantic tags + visual features
7. **Refine**: [[relevance-feedback]] adjusts results based on user's relevance judgments

## Connections
- [[multimedia-annotation]] → [[semantic-gap]] → [[mpeg-7-indexing-pyramid]] (the pyramid models the gap)
- [[multimedia-metadata]] → [[mpeg-7]] (MPEG-7 is the standard metadata format)
- [[feature-extraction]] → [[mpeg-7-descriptors]] (features become descriptors)
- [[content-based-retrieval]] → [[similarity-measures]] → [[relevance-feedback]] (retrieval pipeline)
- [[classification-schemes]] → [[mpeg-7-semantic-description]] (controlled vocabularies for semantics)

## Common Pitfalls
- Confusing MPEG-7 with video compression (MPEG-1/2/4) — MPEG-7 describes, not encodes
- Assuming the semantic gap can be fully bridged — it's a fundamental challenge
- Ignoring that feature extraction is NOT standardized by MPEG-7 (only the output format is)
- Thinking metadata is always reliable or complete

## Exam-Relevant Key Points
- Definition and differences: [[sensory-gap]] vs. [[semantic-gap]]
- MPEG-7 structure: 12 parts, DDL, Descriptors, Description Schemes
- [[mpeg-7-indexing-pyramid]]: know all 10 levels and syntactic vs. semantic division
- [[mpeg-7-descriptors]]: Color (7), Texture (3), Shape (3), Motion (4), Localization (2), Face (1)
- Metadata categories: content, administrative, structural, legal, technical, low-level features
- Extrinsic vs. intrinsic metadata storage
- The role of [[classification-schemes]] in MPEG-7

## Open Questions
- Why has MPEG-7 adoption been limited despite its comprehensiveness?
- How do modern deep learning approaches (embeddings, CLIP) relate to MPEG-7?
- Can the [[semantic-gap]] ever be fully closed?
