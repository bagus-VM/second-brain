---
title: "Content-Based Retrieval"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Content-based retrieval (CBR) searches multimedia databases by comparing the actual content of objects (color, texture, shape, motion) rather than relying solely on textual annotations.

## Core Intuition
Traditional database queries use exact text matches ("find all JPEG files"). Content-based retrieval asks: "find images that look like this one." Instead of matching keywords, it matches the actual visual/audio properties of the content. This requires [[feature-extraction]] to convert content into comparable numerical representations, and [[similarity-measures]] to determine how "close" two items are.

## Formal Definition / Statement
Content-based retrieval is the process of searching multimedia databases using features derived from the content itself (not metadata alone). The typical CBR pipeline:

1. **Feature Extraction** — compute descriptors from raw content (color, texture, shape, motion)
2. **Indexing** — organize features for efficient search (e.g., index structures)
3. **Query Formulation** — user provides a query (example image, sketch, text)
4. **Similarity Computation** — compare query features against database features
5. **Ranking** — return results ordered by similarity
6. **[[relevance-feedback]]** — user refines results iteratively

In the [[mpeg-7]] context, the pull model: Multimedia Resource → Feature Extraction → MPEG-7 Descriptions → Storage → Search/Query/Browse → User.

## Key Properties
- Enables search without textual annotations (addresses the annotation bottleneck)
- Relies on [[feature-extraction]] and [[similarity-measures]]
- Subject to the [[semantic-gap]] — content-based similarity ≠ semantic similarity
- Supports query-by-example, query-by-sketch, query-by-text
- [[relevance-feedback]] can significantly improve results

## Worked Example
A user uploads a photo of a sunset and asks "find similar images":
1. System extracts color histogram, texture, and edge features from the query
2. Compares against stored features in the database using L2 distance
3. Returns top-k images ranked by similarity
4. User marks some results as relevant/irrelevant (relevance feedback)
5. System adjusts feature weights and re-ranks

## Common Pitfalls
- Confusing content-based with text-based retrieval — CBR uses actual content features
- Assuming CBR solves the semantic gap — it operates at the feature level, not the meaning level
- Ignoring that CBR requires efficient indexing for large databases
- Forgetting that the quality of results depends heavily on feature choice and similarity measure

## Connections
- [[feature-extraction]] — provides the content representations used in CBR
- [[similarity-measures]] — determine how content is compared
- [[mpeg-7]] — provides standardized descriptors for CBR
- [[semantic-gap]] — the fundamental limitation of CBR
- [[relevance-feedback]] — iterative refinement technique for CBR
- [[multimedia-metadata]] — can complement CBR with text-based search
- [[mpeg-7-indexing-pyramid]] — different pyramid levels support different CBR granularities

## Open Questions
- How has deep learning changed content-based retrieval (e.g., learned embeddings)?
- Can CBR and text-based retrieval be effectively combined (multi-modal retrieval)?
- What are the scalability limits of CBR for billion-scale databases?
