---
title: "Multimedia Query Languages (MMQL)"
tags: [concept, multimedia-databases, semester-1, query-languages, mmql]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[object-relational-databases]]", "[[query-by-example-and-feature]]"]
---

## One-line Summary
A family of query languages built to express multimedia searches, from exact attribute filters to spatial, temporal, and similarity conditions that plain SQL cannot state.

## Core Intuition
Plain SQL asks exact questions about structured rows: give me employees hired after 2020. Multimedia data demands more. A user wants images similar to a sample, video segments where a person appears, or frames where a red ball sits next to a yellow one. None of these fit a simple equality predicate. They need similarity comparisons, spatial relations, temporal interval logic, and fuzzy thresholds.

A multimedia query language (MMQL) extends or replaces SQL to express these. The field spent two decades arguing about how: bolt multimedia types onto SQL and OQL, or design a language from scratch. Both paths produced standards and prototypes, and the requirements a good MMQL must meet settled into a shared list that every candidate language is measured against.

## Formal Definition / Statement

**Query types in multimedia systems**:
- **Exact queries**: target non multimedia attributes (standard SQL style filtering).
- **Semantic queries**: determine the result from descriptions of the semantic content, such as the occurrence of specific objects or persons.
- **Syntactic queries**: target basic media characteristics such as resolution or framerate.
- **Similarity queries (content based)**: operate on low level features (colour distributions, texture) and return media with similar features.
- **Correlation queries**: identify spatial and temporal correlations in media, such as "all images in which a red ball is next to a yellow one."

**Requirements for a MMQL**:
- Universality (also support querying classical database attributes)
- Content based (semantic) queries
- Spatial queries
- Temporal queries
- Content based similarity queries
- Fuzzy queries
- Presentation

**History, 1980 to 2000**:
- Focus on image data, especially medical images
- Mainly spatial and similarity based queries
- Mainly extensions of existing languages (SQL, OQL)

**History, 2001 to 2011**:
- Multimedia in general, including multimodal data
- Temporal queries and relevance feedback
- New standards: SQL/MM and MPQF
- Fuzzy logic, user preferences, thresholds

**Categories of MMQL**:
1. **Extensions of SQL and OQL**: SQL/MM (extends SQL 99, standardized by ISO/IEC JTC 1/SC 32) and MOQL (extends OQL). Vendor specific de facto standards also exist, such as Oracle MultiMedia.
2. **From scratch**: VideoSQL and the MPEG Query Format (MPQF).

## Key Properties / Complexity

### Why two categories coexist
- Extension approaches reuse a familiar syntax. Adoption is easier because SQL and OQL are already well known, and object orientation is desirable for modelling complex media. The cost is that the base language was never designed for similarity or spatial logic, so the extensions can feel bolted on.
- From scratch approaches design around multimedia from the start. MPQF, for example, is XML based and decoupled from any specific metadata standard, so it can target any XML described metadata, not only MPEG 7. The cost is a new syntax users must learn.

### The five query types form a ladder
- Exact and syntactic queries are cheap and precise. They filter on metadata that is either present or not.
- Semantic queries need object or person recognition, which depends on annotation or detection quality.
- Similarity queries need feature vectors and distance functions, returning ranked rather than binary results.
- Correlation queries combine spatial or temporal reasoning with the above, making them the most expensive to process.

### Requirements as an evaluation checklist
- A language missing spatial or temporal support cannot handle video or geographic image data.
- A language missing fuzzy queries cannot express "much more important than" or threshold weighted preferences, which real users state constantly.
- A language missing presentation support leaves the result display to the application, which is fine for text but inadequate for synchronized multimedia output.

### Processing and optimization implications
- Similarity queries break the usual "push selections down" heuristic. A similarity based selection can be more expensive than a join, so the optimizer cannot assume cheap predicates.
- A formal similarity algebra (similarity based selection and join, the Mine operator) is needed to optimise these queries the way relational algebra optimizes SQL.

## Worked Example

A natural language query from the lecture:

> Give me all images and their titles which are similar to my example image and were taken in Berlin, where the similarity to the example image is much more important than its association to Berlin. In addition, the data size of the selected images should not exceed 2048 KB.

Mapping this to the query types and requirements:
- "similar to my example image" = similarity query (content based), a QBE.
- "taken in Berlin" = exact query on a non multimedia attribute.
- "much more important than" = fuzzy query with weighted preferences and thresholds.
- "data size should not exceed 2048 KB" = syntactic query on a media characteristic.
- Result must include images and titles with a presentation that reflects the weighted ranking.

No single classical SQL statement expresses this. A MMQL must combine an exact filter, a similarity comparison, a fuzzy preference, a syntactic constraint, and a presentation directive in one query. This is exactly why the requirements list exists: a language that handles only some of these leaves the rest to hand written application code.

## Common Pitfalls
- **Assuming SQL plus a BLOB column is enough**: storing images in a table does not make SQL a multimedia query language. Without similarity, spatial, and temporal predicates, the language cannot express the core multimedia query types.
- **Confusing SQL/MM with MPQF**: SQL/MM extends SQL with multimedia UDTs inside a database. MPQF is an XML query format, part 12 of MPEG 7, decoupled from any specific metadata standard. They solve related but distinct problems and can be used together.
- **Treating all five query types as equivalent in cost**: exact and syntactic filters are cheap. Similarity and correlation queries dominate execution time and drive optimization decisions.
- **Forgetting presentation**: multimedia results need spatial and temporal layout, media composition, and synchronized playout. Dropping the presentation requirement pushes complex orchestration into the client.
- **Expecting fuzzy support from extension languages**: not every SQL or OQL extension implements fuzzy boolean operators. MPQF adds scoringFunction with AND, OR, XOR for this reason.

## Connections
[[sql-mm]]: the extension of SQL 99 with multimedia UDTs for full text, spatial, and still image data.
[[mpqf]]: the from scratch XML query format, part 12 of MPEG 7, with management, input, and output categories.
[[moql]]: the extension of OQL with spatial, temporal, and presentation clauses.
[[oql]]: the object query language that MOQL extends.
[[content-based-retrieval]]: similarity queries are the MMQL expression of CBR.
[[multimedia-query-predicates]]: the spatial, temporal, and similarity predicates a MMQL must provide.
[[query-by-example-and-feature]]: QBE and QBF are the similarity query modes a MMQL exposes.
[[object-relational-databases]]: the data model that extension style MMQLs build on.

## Open Questions
- Will extension languages (SQL/MM, MOQL) keep up with deep learning embeddings, or will from scratch formats like MPQF adapt faster because they are metadata agnostic?
- How should a MMQL optimizer rank a similarity join against a relational selection when predicate costs are data dependent?
- Can one language satisfy all seven requirements without becoming too complex for practical query writing?
- Is there a modern successor to MPQF for vector similarity search, or do vector databases sidestep the query language question entirely?
