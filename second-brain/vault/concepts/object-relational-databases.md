---
title: "Object-Relational Databases"
tags: [concept, multimedia-databases, semester-1, object-relational, udt, sql]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-19
prerequisites: ["[[structured-vs-unstructured-retrieval]]", "[[multimedia-database-intro]]", "[[feature-vector]]"]
---

## One-line Summary
Extension of relational databases supporting objects, inheritance, and user-defined types for complex multimedia data.

## Core Intuition
Relational databases are great for structured data (tables of numbers and strings), but multimedia data is complex: an image isn't just a BLOB, it has structure (colour histogram, texture descriptors, spatial layout), behaviour (methods to extract features), and relationships (an image belongs to a collection, has annotations, links to related images).

**Object-relational databases** extend the relational model with object-oriented concepts:
- **User-defined types (UDTs)**: define complex types like `Image`, `Video`, `AudioClip` with their own attributes and methods
- **Inheritance**: a `VideoClip` type can inherit from a `MediaObject` base type
- **Polymorphism**: the same query can work on different types (e.g., `extract_features()` works on images, videos, and audio)
- **Object identifiers (OIDs)**: each object has a unique, system-generated identifier (like a primary key, but immutable and system-managed)

This allows you to store multimedia objects with their full structure and behaviour, not just as opaque BLOBs.

## Formal Definition / Statement

**User-Defined Type (UDT)**:
```sql
CREATE TYPE ImageType AS (
    width INTEGER,
    height INTEGER,
    format VARCHAR(10),
    color_histogram INTEGER ARRAY[256],
    texture_features FLOAT ARRAY[64]
);

CREATE METHOD extract_features() RETURNS FeatureVectorType
    FOR ImageType;
```

**Inheritance**:
```sql
CREATE TYPE VideoType UNDER MediaObjectType AS (
    duration FLOAT,
    frame_rate INTEGER,
    key_frames ImageType ARRAY[]
);
```

**Table of Objects**:
```sql
CREATE TABLE images OF ImageType (
    oid REF(ImageType) SYSTEM GENERATED,
    PRIMARY KEY (oid)
);
```

**Object Reference (REF)**:
```sql
CREATE TYPE AnnotationType AS (
    text VARCHAR(500),
    annotated_image REF(ImageType)
);
```

**DEREF**:
```sql
SELECT DEREF(annotated_image) FROM annotations WHERE text LIKE '%sunset%';
```

**Collections**:
- **Nested tables**: a table stored as a column value
- **Varrays**: variable-size arrays (bounded)

```sql
CREATE TYPE GalleryType AS (
    name VARCHAR(100),
    images ImageType ARRAY[1000]  -- varray
);

CREATE TABLE galleries OF GalleryType
    NESTED TABLE images STORE AS images_tab;
```

**Dot Operator** (accessing attributes/methods):
```sql
SELECT i.width, i.extract_features()
FROM images i
WHERE i.format = 'JPEG';
```

## Key Properties / Complexity

### UDTs vs Relational Types
| Aspect        | Relational                     | Object-Relational                       |
| ------------- | ------------------------------ | --------------------------------------- |
| Data types    | Primitive (INT, VARCHAR, DATE) | Primitive + User-defined (Image, Video) |
| Structure     | Flat tables                    | Nested, hierarchical                    |
| Behaviour      | None (data only)               | Methods attached to types               |
| Identity      | Primary key (user-defined)     | OID (system-generated)                  |
| Relationships | Foreign keys                   | REF (typed object references)           |

### Advantages
- **Complex data modelling**: can represent multimedia objects with their full structure
- **Encapsulation**: data + methods together (e.g., `image.extract_features()`)
- **Reusability**: inheritance allows type hierarchies (MediaObject → Image → SatelliteImage)
- **Polymorphism**: queries work across type hierarchies
- **Type safety**: the database enforces type constraints

### Disadvantages
- **Complexity**: harder to design, query, and optimise
- **Performance**: object navigation (following REFs) can be slower than joins
- **Tool support**: fewer OR-DBMS tools compared to pure RDBMS
- **Standardization**: SQL/MM is still evolving, vendor implementations vary

### OID vs Primary Key
- **OID**: system-generated, immutable, unique across the database, invisible to the user (unless explicitly exposed)
- **Primary key**: user-defined, can change, unique within a table, visible and meaningful

### REF vs Foreign Key
- **REF**: typed pointer to a specific object (like a C++ pointer), follows the object even if its primary key changes
- **Foreign key**: value-based reference to a primary key, breaks if the primary key changes

### Polymorphism in Queries
```sql
-- Works for any MediaObjectType subtype
SELECT m.extract_features()
FROM media m
WHERE m.format = 'JPEG';  -- applies to Image, Video keyframes, etc.
```

## Worked Example

**Zoo Database** (from Exercise 8):

```sql
-- Base type
CREATE TYPE AnimalType AS (
    name VARCHAR(50),
    species VARCHAR(50),
    birth_date DATE
);

CREATE METHOD get_age() RETURNS INTEGER
    FOR AnimalType;

-- Inheritance
CREATE TYPE BirdType UNDER AnimalType AS (
    wingspan FLOAT,
    can_fly BOOLEAN
);

-- Table of objects
CREATE TABLE animals OF AnimalType (
    oid REF(AnimalType) SYSTEM GENERATED,
    PRIMARY KEY (oid)
);

-- 1:n relationship (one keeper, many animals)
CREATE TYPE KeeperType AS (
    name VARCHAR(50),
    animals REF(AnimalType) ARRAY[]
);

CREATE TABLE keepers OF KeeperType;

-- Query using REF and DEREF
SELECT k.name, DEREF(a).name AS animal_name
FROM keepers k, UNNEST(k.animals) a
WHERE k.name = 'John';

-- Polymorphic query
SELECT a.name, a.get_age()
FROM animals a
WHERE a.get_age() > 5;  -- works for AnimalType and all subtypes
```

## Common Pitfalls
- **Confusing REF with foreign key**: REF is a pointer to an object instance, not a value-based reference. If the object is deleted, the REF becomes dangling.
- **Overusing inheritance**: deep type hierarchies are hard to query and maintain. Prefer composition over inheritance for multimedia types.
- **Ignoring OID overhead**: system-generated OIDs add storage and indexing overhead. For simple applications, a primary key may suffice.
- **Forgetting to dereference**: `SELECT annotated_image FROM annotations` returns a REF (pointer), not the actual image. Use `DEREF(annotated_image)` to get the object.
- **Nested table performance**: nested tables can be slow for large collections. Consider normalising into separate tables with foreign keys for better query performance.

## Connections
- [[structured-vs-unstructured-retrieval]] — OR-DBMS bridges the gap between structured metadata and unstructured media
- [[multimedia-database-intro]] — OR-DBMS is one approach to multimedia storage
- [[feature-vector]] — UDTs can encapsulate feature vectors and extraction methods
- [[sql-mm]] — the SQL/MM standard extends SQL for multimedia
- [[content-based-retrieval]] — OR-DBMS can store and query feature vectors for CBIR
- [[mpeg-7-descriptors]] — MPEG-7 descriptors can be modeled as UDTs
- [[nested-tables-vs-varrays]] — Oracle's two collection types for storing sets inside a column (exam hint)

## Open Questions
- Are object-relational databases the right abstraction for multimedia, or should we use specialized multimedia databases (e.g., vector databases for embeddings)?
- How do you index object references efficiently? B-trees work for scalar values, but REFs are pointers — do you need a separate index structure?
- Can OR-DBMS handle the scale of modern multimedia collections (billions of images, petabytes of video)? Or do we need distributed systems?
- How do you version multimedia objects? If an image is edited, does the OID change? How do you track the history?
