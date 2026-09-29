---
title: "Nested Tables vs VARRAYs"
tags: [concept, multimedia-databases, semester-1, oracle, ordbms, collection-types, exam-hint]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[object-relational-databases]]", "[[sql-mm]]"]
---

## One-line Summary
Oracle offers two collection types for storing sets of values inside a column: VARRAYs (bounded, ordered, index-accessed) and nested tables (unbounded, queryable, set-operable). The choice depends on whether you know the max size upfront, whether order matters, and whether you need to run SQL against the collection.

## Core Intuition
When you model multimedia data in an object-relational database, you often need to store collections inside a row. An image has a list of feature vectors. A video has a list of key frames. A gallery has a list of images. Oracle gives you two ways to do this, and the professor wants you to know which one fits which situation.

The distinction comes down to three questions:
1. Do you know the maximum number of elements in advance?
2. Does the order of elements matter?
3. Do you need to query the collection's contents with SQL?

VARRAYs win when the answer to 1 and 2 is yes and 3 is no. Nested tables win when you need flexibility on size, SQL access to elements, or set operations.

## Formal Definition / Statement

### VARRAY (Variable-Size Array)
```sql
CREATE TYPE ColorPalette AS VARRAY(8) OF VARCHAR(20);

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    palette ColorPalette
);
```
- Bounded: you declare a maximum size at type creation. `VARRAY(8)` means at most 8 elements.
- Ordered: element position is preserved. `palette(1)` is always the first colour.
- Index-accessed: access elements by position `palette(i)`.
- Stored inline (for small sizes) or as a LOB (for larger declared sizes). No separate storage table.

### Nested Table
```sql
CREATE TYPE FeatureItem AS OBJECT (
    feature_name VARCHAR(30),
    value FLOAT
);

CREATE TYPE FeatureList AS TABLE OF FeatureItem;

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    features FeatureList
) NESTED TABLE features STORE AS features_tab;
```
- Unbounded: no maximum size declared at type creation. Grows dynamically.
- Unordered: no positional semantics. You should not rely on element order.
- SQL-queryable: use the `TABLE()` operator to treat the collection as a table and run SQL against it.
- Stored in a separate storage table (`features_tab`). The parent row holds a pointer to this storage table.

## Key Properties / Complexity

### Comparison table
| Property | VARRAY | Nested Table |
|----------|--------|--------------|
| Max size | Declared at type creation | Unbounded |
| Order | Preserved | Not preserved |
| Access | By index: `coll(i)` | By SQL query via `TABLE()` |
| Storage | Inline or LOB in parent row | Separate storage table |
| DML on elements | Replace entire collection | Insert/update/delete individual elements |
| SQL queries on contents | Not directly (must unnest in PL/SQL) | Yes, via `TABLE()` operator |
| Set operations | No | Yes (SET, MULTISET UNION, INTERSECT) |
| Join with other tables | No (not directly) | Yes |
| Use when | Bounded, ordered, small, no SQL needed | Unbounded, need SQL, need joins |

### When to use VARRAY
- You know the maximum size at design time (e.g., MPEG-7 dominant colour has at most 8 colours)
- Order is meaningful (e.g., key frames in video sequence, colour palette entries ranked by dominance)
- The collection is small and accessed as a whole (read all, write all)
- You do not need to query individual elements with SQL
- You want inline storage for fewer I/O operations on small data

### When to use nested table
- The collection size is unbounded or varies a lot (e.g., number of annotations per image)
- You need to query the collection's contents with SQL (`SELECT ... FROM TABLE(features) WHERE feature_name = 'color'`)
- You need to join the collection with other tables
- You need set operations (UNION, INTERSECT, MULTISET)
- You need to insert, update, or delete individual elements without rewriting the whole collection
- The collection is large (separate storage avoids bloating the parent row)

## Worked Example

Scenario: modelling an image database with MPEG-7 descriptors.

**VARRAY for dominant colours** (at most 8, order matters by dominance):
```sql
CREATE TYPE DominantColor AS OBJECT (
    color_value VARCHAR(20),
    percentage  FLOAT,
    variance    FLOAT
);

CREATE TYPE DominantColorList AS VARRAY(8) OF DominantColor;

CREATE TABLE images (
    id          INTEGER PRIMARY KEY,
    file_name   VARCHAR(200),
    dominant_colors DominantColorList
);
```
Why VARRAY: MPEG-7 DCD has at most N dominant colours. The order reflects dominance ranking. You always read the whole palette at once. No need to SQL-query individual colours.

**Nested table for annotations** (unbounded, need SQL, need joins):
```sql
CREATE TYPE Annotation AS OBJECT (
    text       VARCHAR(500),
    author     VARCHAR(100),
    timestamp  DATE
);

CREATE TYPE AnnotationList AS TABLE OF Annotation;

CREATE TABLE images (
    id          INTEGER PRIMARY KEY,
    file_name   VARCHAR(200),
    annotations AnnotationList
) NESTED TABLE annotations STORE AS annotations_tab;
```
Why nested table: an image can have zero or thousands of annotations. You need to query "find all images annotated by user X" which means joining the annotation collection. You need to add or remove individual annotations without rewriting the whole list.

Querying the nested table:
```sql
SELECT i.file_name, a.text
FROM images i, TABLE(i.annotations) a
WHERE a.author = 'professor';
```

## Common Pitfalls
- **Using VARRAY when you need SQL access**: VARRAYs cannot be queried with `TABLE()` directly in standard SQL. If you later need to filter or join on collection elements, you are stuck. Choose nested table if there is any chance you will need SQL access.
- **Using nested table when the collection is tiny and fixed-size**: the separate storage table adds I/O overhead. For a fixed 8-element colour palette, VARRAY inline storage is faster.
- **Forgetting the STORE AS clause**: nested table columns require `NESTED TABLE ... STORE AS <storage_tab>`. Without it, Oracle rejects the DDL.
- **Assuming nested table order is stable**: nested tables are unordered. If you insert elements and then read them back, the order is not guaranteed. If order matters, use VARRAY or add a sequence column.
- **Confusing VARRAY bound with actual size**: `VARRAY(100)` declares a maximum of 100. You can store 0 to 100 elements. The bound is a ceiling, not a fixed length.
- **VARRAY size limit is 1 at the type level but storage strategy changes**: in Oracle, VARRAYs stored inline when small (typically <= 4000 bytes) and automatically stored as LOBs when larger. This is transparent but affects performance.

## Connections
[[object-relational-databases]] — VARRAYs and nested tables are Oracle's two collection types for ORDBMS columns.
[[sql-mm]] — SQL/MM Part 5 Still Image uses UDTs whose feature lists could be modeled as either collection type.
[[multimedia-query-languages]] — whether a collection is queryable (nested table) affects what query expressions are possible.
[[dominant-color]] — MPEG-7 DCD's bounded colour list is a textbook VARRAY use case.
[[mpqf]] — MPQF query conditions may need to join on feature values, favoring nested tables' SQL-queryable property
- [[multimedia-databases-lecture-08]] — Source lecture: Query Languages (MMQL, SQL/MM, MPQF, OR extensions; this is the implementation detail)

## Open Questions
- Does Oracle's SQL/MM implementation (Oracle Multimedia) use VARRAYs or nested tables internally for SI_FeatureList? The standard defines the type but not the storage.
- For very large feature collections (e.g., SIFT keypoints: thousands per image), is nested table even performant enough, or should features go in a separate table with a foreign key instead?
- How does this decision interact with indexing? Can you build a B-tree or bitmap index on a nested table column but not on a VARRAY element?
