---
title: "Relevance Feedback"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Relevance feedback is an iterative retrieval technique where the user marks results as relevant/irrelevant, and the system adjusts its search accordingly to bridge the [[semantic-gap]].

## Core Intuition
Content-based retrieval using fixed features often returns semantically irrelevant results because low-level features don't capture meaning. Relevance feedback closes this loop: the user says "this result is good, that one is bad," and the system learns what the user actually means. Over multiple iterations, the system's notion of similarity converges toward the user's semantic intent — effectively learning a user-specific mapping from features to meaning.

## Formal Definition / Statement
Relevance feedback is an interactive retrieval process:
1. User submits a query (e.g., example image)
2. System retrieves initial results using [[content-based-retrieval]]
3. User marks results as relevant (+) or irrelevant (-)
4. System adjusts feature weights, query point, or similarity function
5. System re-retrieves and presents updated results
6. Repeat until user is satisfied

**Common approaches:**
- **Query point movement**: shift the query toward relevant results, away from irrelevant (Rocchio algorithm)
- **Feature weight adjustment**: increase weights of features that discriminate relevant from irrelevant
- **Metric learning**: learn a new [[similarity-measures|distance function]] from feedback

## Key Properties
- Iterative — improves with each feedback round
- User-specific — different users get different results for the same query
- Addresses the [[semantic-gap]] by incorporating human judgment
- Typically requires only a few iterations (3–5) for significant improvement
- Can be implemented by modifying the query, the similarity function, or both

## Worked Example
Query: "find images of beaches"
1. Initial retrieval returns: sunset (✓), ocean waves (✓), desert (✗), red car (✗)
2. User marks: sunset and ocean as relevant, desert and car as irrelevant
3. System learns: increase weight on blue color, sandy texture; decrease weight on red/orange, solid surfaces
4. Re-retrieval: beach scene (✓), coral reef (✓), mountain lake (✗)
5. User marks: beach and coral as relevant, lake as irrelevant
6. System further refines — converging on "beach" semantics

## Common Pitfalls
- Assuming feedback is always reliable — users may make inconsistent judgments
- Ignoring that feedback is session-specific — doesn't transfer across queries
- Forgetting computational cost — re-computing rankings after each round
- Overfitting to a small number of feedback examples

## Connections
- [[content-based-retrieval]] — relevance feedback is an extension of CBR
- [[semantic-gap]] — the primary problem relevance feedback addresses
- [[feature-extraction]] — feedback adjusts how features are weighted
- [[similarity-measures]] — feedback can modify the similarity function
- [[multimedia-annotation]] — feedback implicitly annotates results

## Open Questions
- Can active learning reduce the number of feedback iterations needed?
- How does relevance feedback compare to zero-shot retrieval with modern embeddings?
- Can feedback from one session be generalized across users?
