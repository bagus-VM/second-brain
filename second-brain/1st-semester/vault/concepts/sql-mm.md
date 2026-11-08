---
title: "SQL/MM (SQL Multimedia)"
tags: [concept, multimedia-databases, semester-1, sql-mm, content-based-retrieval, standard]
course: "Multimedia Databases"
source_count: 2
status: current
last_updated: 2026-06-25
prerequisites: ["[[object-relational-databases]]", "[[content-based-retrieval]]", "[[mpeg-7]]"]
---

## One-line Summary
ISO/IEC 13249 extension of SQL for multimedia applications, supporting content-based queries.

## Core Intuition
Standard SQL is great for querying structured data (tables of numbers and strings), but it has no built-in support for multimedia data types (images, video, audio) or content-based queries ("find images similar to this one").

**SQL/MM** (SQL Multimedia) is an ISO standard that extends SQL with:
- **Multimedia data types**: `STILL IMAGE`, `VIDEO`, `AUDIO` with their own attributes and methods
- **Content-based query predicates**: `SIMILAR TO`, `CONTAINS`, `EXTRACT FEATURE`
- **Query-by-Example (QbE)**: pass a sample image/audio, get similar items back
- **Integration with MPEG-7**: use MPEG-7 descriptors as the standard feature representation

This allows you to write queries like:
```sql
SELECT * FROM images
WHERE image_data SIMILAR TO :query_image
USING DESCRIPTOR dominant_color
WITHIN DISTANCE 0.3;
```

SQL/MM bridges the gap between traditional relational databases and multimedia retrieval systems, allowing you to store, manage, and query multimedia data using standard SQL.

## Formal Definition / Statement

**SQL/MM Parts**:
- **SQL/MM Part 1: Framework** — overall architecture, data type hierarchy
- **SQL/MM Part 2: Full-text** — full-text search (FT) predicates and functions
- **SQL/MM Part 3: Spatial** — spatial data types and functions (geometry, geography)
- **SQL/MM Part 5: Still Image** — still image data type and methods (SI). UDT `SI_StillImage` with `SI_content` (BLOB, includes header/colour tables), `SI_contentLength`, `SI_format` (8 chars), `SI_height`, `SI_width`. Feature subtypes: `SI_AverageColor`, `SI_ColorHistogram`, `SI_PositionalColor`, `SI_Texture`. Each has an `SI_Score` method that computes distance and returns a real value 0-1. CBR query example: `WHERE p1.photo1_color.SI_Score(p2.photo2) > 0.5`.
- **SQL/MM Part 2: Full Text** — UDT `FullText` with two search methods: `Contains` (boolean yes/no) and `Rank` (implementation-dependent real value). Supports contextual and conceptual search patterns.
- **SQL/MM Part 3: Spatial** — UDTs for 2D data: `ST_Point` (0-dim), `ST_Curve`/`ST_LineString`/`ST_CircularString` (1-dim), `ST_Surface`/`ST_Polygon` (2-dim), plus `ST_Multi*` collections. Each geometry has an SRID (spatial reference system identifier).
- **SQL/MM Part 6: Data Mining** — data mining functions (not yet finalized)
- **SQL/MM Part 7: History** — temporal data (not yet finalized)
- **SQL/MM Part 8: Sequences** — sequence data (not yet finalized)
- **SQL/MM Part 9: Management of External Data** — external data management

**Still Image Type (SQL/MM Part 4)**:
```sql
-- Data type
CREATE TYPE SI_StillImage AS (
    content BLOB,
    width INTEGER,
    height INTEGER,
    format VARCHAR(10),
    color_space VARCHAR(20)
);

-- Methods
CREATE METHOD get_content() RETURNS BLOB FOR SI_StillImage;
CREATE METHOD get_width() RETURNS INTEGER FOR SI_StillImage;
CREATE METHOD get_height() RETURNS INTEGER FOR SI_StillImage;
CREATE METHOD get_format() RETURNS VARCHAR FOR SI_StillImage;
```

**Content-Based Query Predicates**:
```sql
-- Similarity query
SELECT image_id, image_data
FROM images
WHERE image_data SIMILAR TO :query_image
USING DESCRIPTOR dominant_color
WITHIN DISTANCE 0.2;

-- Feature extraction
SELECT SI_extractFeature(image_data, 'dominant_color')
FROM images
WHERE image_id = 123;

-- Content-based join
SELECT i1.image_id, i2.image_id, 
       SI_similarity(i1.image_data, i2.image_data, 'color_histogram') AS sim
FROM images i1, images i2
WHERE i1.image_id < i2.image_id
  AND SI_similarity(i1.image_data, i2.image_data, 'color_histogram') < 0.3;
```

**Query-by-Example (QbE)**:
```sql
-- User provides a sample image, system finds similar images
PREPARE query_by_example AS
SELECT image_id, image_data,
       SI_similarity(image_data, ?, 'dominant_color') AS distance
FROM images
WHERE SI_similarity(image_data, ?, 'dominant_color') < 0.5
ORDER BY distance
LIMIT 10;

EXECUTE query_by_example USING :sample_image, :sample_image;
```

**Integration with MPEG-7**:
```sql
-- Store MPEG-7 descriptors
CREATE TYPE MPEG7_DominantColor AS (
    colors ColorType ARRAY[8],
    percentages FLOAT ARRAY[8],
    spatial_coherency FLOAT
);

CREATE TABLE image_descriptors (
    image_id INTEGER REFERENCES images(id),
    dominant_color MPEG7_DominantColor,
    color_layout ColorLayoutType,
    edge_histogram EdgeHistogramType
);

-- Query using MPEG-7 descriptors
SELECT i.image_id
FROM images i JOIN image_descriptors d ON i.id = d.image_id
WHERE SI_similarity(d.dominant_color, :query_descriptor, 'weighted_euclidean') < 0.3;
```

## Key Properties / Complexity

### Supported Multimedia Types
| Type | SQL/MM Part | Description | Example |
|------|-------------|-------------|---------|
| `SI_StillImage` | Part 4 | Still images (JPEG, PNG, TIFF) | Photos, scans, diagrams |
| `Video` | (proposed) | Video sequences (MP4, AVI) | Movies, clips, surveillance |
| `Audio` | (proposed) | Audio streams (MP3, WAV) | Music, speech, sound effects |
| `Full-text` | Part 2 | Text documents with full-text search | PDFs, Word docs, web pages |
| `Spatial` | Part 3 | Geometric and geographic data | Maps, GIS, CAD |

### Content-Based Query Operations
- **Similarity search**: find items similar to a query item
- **Feature extraction**: compute descriptors (colour histogram, texture, shape)
- **Distance computation**: compute distance between two feature vectors
- **Threshold query**: find items within a distance threshold
- **k-NN query**: find the k most similar items

### Distance Metrics in SQL/MM
SQL/MM supports multiple distance metrics for similarity computation:
- **L1 (Manhattan)**: `Σ|pᵢ - qᵢ|`
- **L2 (Euclidean)**: `√(Σ(pᵢ - qᵢ)²)`
- **L∞ (Chebyshev)**: `max|pᵢ - qᵢ|`
- **Weighted Euclidean**: `√(Σ wᵢ(pᵢ - qᵢ)²)` with per-dimension weights
- **Mahalanobis**: covariance-aware distance
- **Custom**: user-defined distance functions

### Advantages
- **Standardization**: ISO standard ensures portability across DBMS vendors
- **Integration**: multimedia queries use standard SQL syntax
- **Type safety**: multimedia data types are first-class citizens
- **Extensibility**: can define custom descriptors and distance functions
- **MPEG-7 integration**: standard descriptors ensure interoperability

### Disadvantages
- **Limited adoption**: few commercial DBMS fully implement SQL/MM
- **Performance**: content-based queries can be slow without specialized indexes
- **Complexity**: multimedia data types add complexity to the database schema
- **Vendor lock-in**: some vendors implement proprietary extensions beyond SQL/MM

## Worked Example

**Zoo Database with SQL/MM** (from Exercise 8):

```sql
-- Create image type with MPEG-7 descriptors
CREATE TYPE ZooImageType AS (
    image_data SI_StillImage,
    dominant_color MPEG7_DominantColor,
    color_layout ColorLayoutType
);

-- Table of animals with images
CREATE TABLE animals (
    animal_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    species VARCHAR(50),
    photo ZooImageType
);

-- Insert an animal with its image
INSERT INTO animals VALUES (
    1,
    'Simba',
    'Lion',
    ROW(
        SI_importFromURL('http://zoo.com/images/simba.jpg'),
        ROW(
            ARRAY[RGB(255,200,0), RGB(139,69,19), RGB(255,255,255)],
            ARRAY[0.6, 0.3, 0.1],
            0.85
        ),
        NULL
    )
);

-- Query-by-Example: find animals with similar photos
PREPARE find_similar_animals AS
SELECT a.animal_id, a.name, a.species,
       SI_similarity(a.photo.dominant_color, ?, 'weighted_euclidean') AS distance
FROM animals a
WHERE SI_similarity(a.photo.dominant_color, ?, 'weighted_euclidean') < 0.4
ORDER BY distance
LIMIT 5;

-- Execute with a query image
EXECUTE find_similar_animals USING :query_descriptor, :query_descriptor;

-- Content-based join: find pairs of similar animals
SELECT a1.name AS animal1, a2.name AS animal2,
       SI_similarity(a1.photo.dominant_color, a2.photo.dominant_color, 'weighted_euclidean') AS similarity
FROM animals a1, animals a2
WHERE a1.animal_id < a2.animal_id
  AND SI_similarity(a1.photo.dominant_color, a2.photo.dominant_color, 'weighted_euclidean') < 0.3
ORDER BY similarity;
```

## Common Pitfalls
- **Assuming SQL/MM is widely supported**: most commercial DBMS (Oracle, PostgreSQL, SQL Server) have partial or no SQL/MM support. Check vendor documentation.
- **Forgetting to extract features before querying**: SQL/MM queries require feature descriptors to be pre-computed and stored. You can't query raw pixel data directly.
- **Using the wrong distance metric**: different metrics capture different notions of similarity. Euclidean is good for colour histograms, but Mahalanobis is better when features are correlated.
- **Ignoring indexing**: content-based queries without indexes require full table scan. Use R-trees, VP-trees, or LSH for high-dimensional feature vectors.
- **Confusing SQL/MM with MPEG-7**: SQL/MM is a database standard, MPEG-7 is a multimedia content description standard. SQL/MM can use MPEG-7 descriptors, but they're separate things.

## Connections
- [[object-relational-databases]] — SQL/MM extends OR-DBMS with multimedia types
- [[content-based-retrieval]] — SQL/MM provides the query interface for CBIR
- [[mpeg-7]] — SQL/MM integrates with MPEG-7 descriptors
- [[mpeg-7-descriptors]] — specific descriptors (dominant colour, colour layout) used in SQL/MM queries
- [[feature-vector]] — SQL/MM queries operate on feature vectors
- [[structured-vs-unstructured-retrieval]] — SQL/MM bridges structured SQL and unstructured multimedia
- [[moql]] — another SQL/OQL extension approach for multimedia queries
- [[multimedia-query-languages]] — overview of MMQL history and categories

## Open Questions
- Will SQL/MM gain wider adoption, or will specialized multimedia databases (vector databases, document stores) replace it?
- How do you optimise SQL/MM queries for large-scale multimedia collections? Traditional B-trees don't work for high-dimensional feature vectors.
- Can SQL/MM handle deep learning embeddings (512-2048 dim vectors)? Or do we need a new standard for vector similarity search?
- How do you version multimedia data in SQL/MM? If an image is edited, does the descriptor change? How do you track the history?
- Can SQL/MM support real-time multimedia queries (e.g., video stream analysis)? Or is it limited to static content?
