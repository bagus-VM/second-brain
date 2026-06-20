---
title: "MMDB Exercise 8 — Querying Multimedia Data"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-19
---

## Overview

Exercise 8 covers the transition from relational to object-relational databases for multimedia data, and introduces standardized query formats (SQL/MM, MPQF) for content-based retrieval.

## Task 1: Relational vs Object-Relational DB Differences

### Question
Compare relational and object-relational databases across the following dimensions:
1. Data structure complexity
2. Indexing strategies
3. Query predicates
4. Pros and cons of each approach

### Solution

| Dimension | Relational DB | Object-Relational DB |
|-----------|--------------|---------------------|
| **Data structure complexity** | Flat tables with primitive types (INT, VARCHAR, DATE). Complex data must be decomposed into multiple tables with foreign keys. | Supports nested structures, arrays, user-defined types (UDTs). Complex data (images, video) stored as structured objects. |
| **Indexing** | B-trees, hash indexes on scalar values. Well-understood, highly optimized. | B-trees on scalar attributes + specialized indexes for complex types (R-trees for spatial, VP-trees for feature vectors). More complex to manage. |
| **Query predicates** | Exact match (=), range (<, >, BETWEEN), pattern (LIKE). All operate on scalar values. | Scalar predicates + similarity predicates (SIMILAR TO, WITHIN DISTANCE), content-based predicates (CONTAINS FEATURE), object navigation (DEREF). |
| **Pros** | Simple, well-understood, fast for structured queries, mature tooling, ACID compliance. | Can model complex multimedia data natively, encapsulation (data + methods), inheritance, polymorphism. |
| **Cons** | Cannot represent complex multimedia data natively. Must store as BLOBs (opaque) or decompose into many tables (impedance mismatch). | More complex to design and query. Performance overhead for object navigation. Fewer tools, less mature ecosystem. |

### Key Insight
The fundamental difference is that relational DBs treat multimedia data as **opaque BLOBs** (the DB doesn't understand the content), while object-relational DBs treat multimedia data as **structured objects** with extractable features and queryable properties.

### When to Use Which
- **Relational**: when you only need metadata queries ("find all images uploaded by user X after date Y")
- **Object-Relational**: when you need content-based queries ("find images similar to this one")

---

## Task 2: DB Definitions

### 2.1 User-Defined Data Types (UDTs)

**Definition**: A user-defined type is a complex data type that encapsulates attributes (data) and methods (behavior) into a single unit.

```sql
CREATE TYPE ImageType AS (
    width INTEGER,
    height INTEGER,
    format VARCHAR(10),
    color_histogram INTEGER ARRAY[256]
);

CREATE METHOD extract_dominant_color() RETURNS ColorType
    FOR ImageType;
```

**Key properties**:
- Encapsulates data + behavior (like a class in OOP)
- Can be used as column types in tables
- Methods can be invoked with the dot operator: `image.extract_dominant_color()`

### 2.2 Inheritance

**Definition**: A type can inherit attributes and methods from a parent type, forming a type hierarchy.

```sql
CREATE TYPE MediaObjectType AS (
    id INTEGER,
    title VARCHAR(200),
    creation_date DATE
);

CREATE METHOD get_metadata() RETURNS MetadataType
    FOR MediaObjectType;

-- ImageType inherits from MediaObjectType
CREATE TYPE ImageType UNDER MediaObjectType AS (
    width INTEGER,
    height INTEGER,
    color_histogram INTEGER ARRAY[256]
);

-- VideoType inherits from MediaObjectType
CREATE TYPE VideoType UNDER MediaObjectType AS (
    duration FLOAT,
    frame_rate INTEGER
);
```

**Key properties**:
- Subtypes inherit all attributes and methods from the parent
- Subtypes can add new attributes and methods
- Subtypes can override parent methods (polymorphism)

### 2.3 Table of Objects

**Definition**: A table whose rows are instances of a UDT. Each row is an object with a system-generated OID.

```sql
CREATE TABLE images OF ImageType (
    oid REF(ImageType) SYSTEM GENERATED,
    PRIMARY KEY (oid)
);
```

**Key properties**:
- Each row is an object of the specified type
- System generates a unique OID for each object
- Can be referenced by other objects using REF

### 2.4 Polymorphism

**Definition**: The ability to invoke the same method on objects of different types, with the appropriate implementation being selected at runtime.

```sql
-- get_metadata() is defined for MediaObjectType and overridden in subtypes
SELECT m.get_metadata()
FROM media m;  -- works for ImageType, VideoType, AudioType, etc.
```

**Key properties**:
- Same method name, different implementations per type
- Enables generic queries across type hierarchies
- Reduces code duplication

### 2.5 Object Identifier (OID)

**Definition**: A system-generated, immutable, unique identifier for each object in a table of objects.

**Properties**:
- **System-generated**: the DBMS creates it automatically
- **Immutable**: never changes during the object's lifetime
- **Unique**: no two objects in the database share the same OID
- **Surrogate**: has no semantic meaning (unlike a primary key)

**vs Primary Key**:
| Property | OID | Primary Key |
|----------|-----|-------------|
| Generated by | System | User |
| Can change? | No | Yes |
| Semantic meaning | None | Meaningful to the application |
| Scope | Database-wide | Table-wide |

### 2.6 Relations Between UDTs

**1:1 Relationship** (using REF):
```sql
CREATE TYPE PassportType AS (
    number VARCHAR(20),
    owner REF(PersonType)
);
```

**1:n Relationship** (using collections):
```sql
CREATE TYPE DepartmentType AS (
    name VARCHAR(100),
    employees REF(EmployeeType) ARRAY[]
);
```

**n:m Relationship** (using a link table):
```sql
CREATE TABLE student_courses (
    student REF(StudentType),
    course REF(CourseType),
    grade CHAR(1)
);
```

### 2.7 REF and DEREF

**REF**: A typed pointer to an object. Stored as a column value, it references another object by its OID.

```sql
CREATE TYPE AnnotationType AS (
    text VARCHAR(500),
    annotated_image REF(ImageType)  -- pointer to an image
);
```

**DEREF**: Dereferences a REF to get the actual object.

```sql
-- Without DEREF: returns the REF (pointer)
SELECT annotated_image FROM annotations;
-- Result: REF(ImageType) = System.OID.12345

-- With DEREF: returns the actual object
SELECT DEREF(annotated_image) FROM annotations;
-- Result: ImageType(width=1920, height=1080, ...)
```

### 2.8 Collections

**Nested Tables**: A table stored as a column value.

```sql
CREATE TYPE GalleryType AS (
    name VARCHAR(100),
    images ImageType ARRAY[]  -- unbounded array (nested table)
);

CREATE TABLE galleries OF GalleryType
    NESTED TABLE images STORE AS gallery_images_tab;

-- Query nested table
SELECT g.name, i.width
FROM galleries g, TABLE(g.images) i
WHERE i.format = 'JPEG';
```

**Varrays**: Variable-size arrays with a maximum bound.

```sql
CREATE TYPE PlaylistType AS (
    name VARCHAR(100),
    tracks AudioType ARRAY[100]  -- max 100 tracks
);
```

### 2.9 Dot Operator

**Definition**: Accesses attributes and methods of an object.

```sql
-- Access attribute
SELECT i.width, i.height FROM images i;

-- Invoke method
SELECT i.extract_dominant_color() FROM images i;

-- Navigate REF
SELECT DEREF(a.annotated_image).width FROM annotations a;
```

---

## Task 3: Content-Based Image Search Using SQL/MM

### 3.1 Zoo Database — ER Model

**Entities**:
- **Animal**: animal_id, name, species, photo (image)
- **Keeper**: keeper_id, name, assigned_animals
- **Cage**: cage_id, location, capacity, occupants

**Relationships**:
- Keeper 1:n Animal (one keeper cares for many animals)
- Cage 1:n Animal (one cage houses many animals)
- Animal n:1 Keeper (each animal has one keeper)
- Animal n:1 Cage (each animal is in one cage)

### 3.2 Object-Relational SQL Creation

```sql
-- UDT for image with MPEG-7 descriptors
CREATE TYPE ZooImageType AS (
    image_data BLOB,
    width INTEGER,
    height INTEGER,
    dominant_color DominantColorType,
    color_layout ColorLayoutType,
    edge_histogram EdgeHistogramType
);

-- UDT for dominant color (MPEG-7)
CREATE TYPE DominantColorType AS (
    colors ColorValue ARRAY[8],
    percentages FLOAT ARRAY[8],
    spatial_coherency FLOAT
);

-- Animal type with photo
CREATE TYPE AnimalType AS (
    animal_id INTEGER,
    name VARCHAR(50),
    species VARCHAR(50),
    birth_date DATE,
    photo ZooImageType
);

-- Keeper type with references to animals
CREATE TYPE KeeperType AS (
    keeper_id INTEGER,
    name VARCHAR(50),
    assigned_animals REF(AnimalType) ARRAY[]
);

-- Cage type
CREATE TYPE CageType AS (
    cage_id INTEGER,
    location VARCHAR(100),
    capacity INTEGER,
    occupants REF(AnimalType) ARRAY[]
);

-- Create tables
CREATE TABLE animals OF AnimalType (
    oid REF(AnimalType) SYSTEM GENERATED,
    PRIMARY KEY (animal_id)
);

CREATE TABLE keepers OF KeeperType (
    PRIMARY KEY (keeper_id)
);

CREATE TABLE cages OF CageType (
    PRIMARY KEY (cage_id)
);
```

### 3.3 SQL/MM Queries for Query-by-Example

**Q1: Find animals with photos similar to a query image (using dominant color)**

```sql
SELECT a.animal_id, a.name, a.species,
       SI_similarity(a.photo.dominant_color, :query_descriptor, 'euclidean') AS distance
FROM animals a
WHERE SI_similarity(a.photo.dominant_color, :query_descriptor, 'euclidean') < 0.3
ORDER BY distance
LIMIT 10;
```

**Q2: Find animals with similar color AND texture**

```sql
SELECT a.animal_id, a.name,
       0.7 * SI_similarity(a.photo.dominant_color, :query_color, 'euclidean') +
       0.3 * SI_similarity(a.photo.edge_histogram, :query_texture, 'euclidean') AS combined_distance
FROM animals a
WHERE 0.7 * SI_similarity(a.photo.dominant_color, :query_color, 'euclidean') +
      0.3 * SI_similarity(a.photo.edge_histogram, :query_texture, 'euclidean') < 0.4
ORDER BY combined_distance
LIMIT 10;
```

**Q3: Find the keeper whose animals are most similar to a query image**

```sql
SELECT k.name,
       AVG(SI_similarity(DEREF(animal_ref).photo.dominant_color, :query_descriptor, 'euclidean')) AS avg_distance
FROM keepers k, UNNEST(k.assigned_animals) AS animal_ref
GROUP BY k.keeper_id, k.name
ORDER BY avg_distance
LIMIT 1;
```

---

## Task 4: MPEG Query Format (MPQF) — Natural Language to MPQF Translation

### Example 1: "Find images with a blue sky and green grass"

**Analysis**:
- Query type: Query-by-Feature (specifying features, not providing an example)
- Descriptors: DominantColor (blue, green), ColorLayout (spatial arrangement: blue on top, green on bottom)
- Distance metric: Euclidean
- Weights: Color = 0.6, Layout = 0.4

**MPQF**:
```xml
<Mpeg7Query>
    <QueryDescriptor>
        <QueryType>QueryByFeature</QueryType>
        
        <DescriptorUsage>
            <DescriptorName>DominantColor</DescriptorName>
            <Weight>0.6</Weight>
            <FeatureValues>
                <DominantColor>
                    <Color>RGB(0, 100, 255)</Color>  <!-- blue sky -->
                    <Percentage>0.5</Percentage>
                    <Color>RGB(0, 180, 0)</Color>  <!-- green grass -->
                    <Percentage>0.4</Percentage>
                </DominantColor>
            </FeatureValues>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>ColorLayout</DescriptorName>
            <Weight>0.4</Weight>
            <FeatureValues>
                <ColorLayout>
                    <TopRegion>blue-dominant</TopRegion>
                    <BottomRegion>green-dominant</BottomRegion>
                </ColorLayout>
            </FeatureValues>
        </DescriptorUsage>
        
        <SimilarityCriteria>
            <DistanceMetric>Euclidean</DistanceMetric>
            <Threshold>0.4</Threshold>
        </SimilarityCriteria>
        
        <ResultSpecification>
            <MaxResults>20</MaxResults>
            <OrderBy>Similarity</OrderBy>
        </ResultSpecification>
    </QueryDescriptor>
</Mpeg7Query>
```

### Example 2: "Find videos similar to this action sequence"

**Analysis**:
- Query type: Query-by-Example (providing a sample video)
- Descriptors: MotionTrajectory, DominantColor, EdgeHistogram
- Distance metric: Weighted Euclidean

**MPQF**:
```xml
<Mpeg7Query>
    <QueryDescriptor>
        <QueryType>QueryByExample</QueryType>
        
        <MediaLocator>
            <MediaUri>action-sequence.mp4</MediaUri>
        </MediaLocator>
        
        <DescriptorUsage>
            <DescriptorName>MotionTrajectory</DescriptorName>
            <Weight>0.5</Weight>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>DominantColor</DescriptorName>
            <Weight>0.3</Weight>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>EdgeHistogram</DescriptorName>
            <Weight>0.2</Weight>
        </DescriptorUsage>
        
        <SimilarityCriteria>
            <DistanceMetric>WeightedEuclidean</DistanceMetric>
            <Threshold>0.5</Threshold>
        </SimilarityCriteria>
        
        <ResultSpecification>
            <MaxResults>5</MaxResults>
            <OrderBy>Similarity</OrderBy>
        </ResultSpecification>
    </QueryDescriptor>
</Mpeg7Query>
```

---

## Common Pitfalls

- **Confusing REF with foreign key**: REF is a typed pointer (like a C++ reference), not a value-based link. If the referenced object is deleted, the REF becomes dangling.
- **Forgetting DEREF**: `SELECT annotated_image FROM annotations` returns a REF (pointer), not the actual object. Use `DEREF()` to navigate to the object.
- **Overlooking polymorphism**: if a method is defined on a parent type, it works for all subtypes. Don't write separate queries for each subtype.
- **Ignoring the semantic gap in SQL/MM**: SQL/MM can express similarity queries, but it can't bridge the semantic gap alone. You still need good feature extractors and appropriate distance metrics.
- **MPQF verbosity**: MPQF is XML-based and verbose. In practice, queries are generated by applications, not written by hand.
- **Choosing wrong distance metric in SQL/MM**: Euclidean is not always best. For color histograms, chi-squared or Earth Mover's Distance may be more perceptually meaningful.

## Related Lectures

- [[multimedia-databases-lecture-06]]
- [[content-based-retrieval]]
- [[object-relational-databases]]
- [[sql-mm]]
- [[mpqf]]
- [[mpeg-7-descriptors]]
- [[feature-vector]]
- [[structured-vs-unstructured-retrieval]]
