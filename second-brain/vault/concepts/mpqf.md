---
title: "MPEG Query Format (MPQF)"
tags: [concept, multimedia-databases, semester-1, mpqf, mpeg-7, query-format]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-19
prerequisites: ["[[mpeg-7]]", "[[mpeg-7-descriptors]]", "[[content-based-retrieval]]"]
---

## One-line Summary
Standardized format for expressing multimedia queries using MPEG-7 descriptors.

## Core Intuition
Content-based multimedia retrieval needs a way to express queries like "find images similar to this one" or "find videos with similar color distribution." But how do you represent these queries in a standardized, interoperable way?

**MPEG Query Format (MPQF)** is an ISO standard (part of MPEG-7) that provides a structured way to express multimedia queries using MPEG-7 descriptors. It allows you to specify:
- **Query type**: query-by-example, query-by-feature, query-by-sket
- **Descriptors**: which MPEG-7 descriptors to use (dominant color, texture, shape)
- **Similarity criteria**: distance metric, threshold, weights
- **Query items**: the actual query data (sample image, feature values)

MPQF is to multimedia queries what SQL is to relational queries — a standardized language that different systems can understand and execute.

## Formal Definition / Statement

**MPQF Structure** (XML-based):
```xml
<Mpeg7Query xmlns="urn:mpeg:mpeg7:schema:2001">
    <QueryDescriptor>
        <QueryType>QueryByExample</QueryType>
        
        <MediaLocator>
            <MediaUri>http://example.com/query-image.jpg</MediaUri>
        </MediaLocator>
        
        <DescriptorUsage>
            <DescriptorName>DominantColor</DescriptorName>
            <Weight>1.0</Weight>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>ColorLayout</DescriptorName>
            <Weight>0.5</Weight>
        </DescriptorUsage>
        
        <SimilarityCriteria>
            <DistanceMetric>Euclidean</DistanceMetric>
            <Threshold>0.3</Threshold>
        </SimilarityCriteria>
        
        <ResultSpecification>
            <MaxResults>10</MaxResults>
            <OrderBy>Similarity</OrderBy>
        </ResultSpecification>
    </QueryDescriptor>
</Mpeg7Query>
```

**Query Types**:
1. **Query-by-Example (QbE)**: user provides a sample media item
   ```xml
   <QueryType>QueryByExample</QueryType>
   <MediaLocator>
       <MediaUri>query-image.jpg</MediaUri>
   </MediaLocator>
   ```

2. **Query-by-Feature**: user specifies feature values directly
   ```xml
   <QueryType>QueryByFeature</QueryType>
   <FeatureValues>
       <DominantColor>
           <Color>RGB(255,200,0)</Color>
           <Percentage>0.6</Percentage>
       </DominantColor>
   </FeatureValues>
   ```

3. **Query-by-Sketch**: user provides a sketch (drawing)
   ```xml
   <QueryType>QueryBySketch</QueryType>
   <SketchData>
       <Shape>circle</Shape>
       <Position>(100, 100)</Position>
       <Size>50</Size>
   </SketchData>
   ```

**Descriptor Usage**:
```xml
<DescriptorUsage>
    <DescriptorName>DominantColor</DescriptorName>
    <Weight>1.0</Weight>
    <Region>
        <SpatialRegion>
            <TopLeft>(0, 0)</TopLeft>
            <BottomRight>(100, 100)</BottomRight>
        </SpatialRegion>
    </Region>
</DescriptorUsage>
```

**Similarity Criteria**:
```xml
<SimilarityCriteria>
    <DistanceMetric>Euclidean</DistanceMetric>
    <!-- or: Manhattan, Chebyshev, Mahalanobis, WeightedEuclidean -->
    
    <Threshold>0.3</Threshold>
    <!-- Maximum distance for a result to be included -->
    
    <Normalization>
        <Method>MinMax</Method>
        <!-- or: ZScore, None -->
    </Normalization>
</SimilarityCriteria>
```

**Result Specification**:
```xml
<ResultSpecification>
    <MaxResults>10</MaxResults>
    <OrderBy>Similarity</OrderBy>
    <!-- or: Distance, Relevance, Custom -->
    
    <ReturnFields>
        <Field>MediaLocator</Field>
        <Field>SimilarityScore</Field>
        <Field>DescriptorValues</Field>
    </ReturnFields>
</ResultSpecification>
```

## Key Properties

### Query Types
| Type | Input | Use Case | Example |
|------|-------|----------|---------|
| Query-by-Example | Sample media item | Find similar items | "Find images like this sunset photo" |
| Query-by-Feature | Feature values | Find items matching specific features | "Find images with 60% red, 30% orange" |
| Query-by-Sketch | Sketch/drawing | Find items matching a rough shape | "Find images with a circle in the center" |
| Query-by-Concept | Semantic concept | Find items matching a concept | "Find images of beaches" (requires semantic mapping) |

### Descriptor Usage
MPQF allows you to specify which MPEG-7 descriptors to use in the query:
- **Visual descriptors**: DominantColor, ColorLayout, EdgeHistogram, Texture, Shape
- **Audio descriptors**: AudioSpectrum, MFCC, AudioHarmonicity
- **Multimedia descriptors**: MotionTrajectory, FaceRecognition

You can combine multiple descriptors with weights:
```xml
<DescriptorUsage>
    <DescriptorName>DominantColor</DescriptorName>
    <Weight>0.7</Weight>
</DescriptorUsage>
<DescriptorUsage>
    <DescriptorName>Texture</DescriptorName>
    <Weight>0.3</Weight>
</DescriptorUsage>
```

### Distance Metrics
MPQF supports multiple distance metrics:
- **Euclidean (L2)**: `√(Σ(pᵢ - qᵢ)²)` — most common, good for color histograms
- **Manhattan (L1)**: `Σ|pᵢ - qᵢ|` — robust to outliers
- **Chebyshev (L∞)**: `max|pᵢ - qᵢ|` — focuses on the largest difference
- **Mahalanobis**: covariance-aware, good when features are correlated
- **Weighted Euclidean**: `√(Σ wᵢ(pᵢ - qᵢ)²)` — per-dimension weights
- **Custom**: user-defined distance functions

### Advantages
- **Standardization**: ISO standard ensures interoperability across systems
- **Flexibility**: supports multiple query types, descriptors, and distance metrics
- **Extensibility**: can define custom descriptors and distance functions
- **MPEG-7 integration**: uses MPEG-7 descriptors, ensuring compatibility
- **XML-based**: human-readable, easy to parse and generate

### Disadvantages
- **Complexity**: XML-based format is verbose and hard to write by hand
- **Limited adoption**: few systems fully implement MPQF
- **Performance**: parsing XML queries adds overhead
- **Learning curve**: requires understanding of MPEG-7 descriptors and distance metrics

## Worked Example

**Natural Language to MPQF Translation** (from Exercise 8):

**Query**: *"Find images that are mostly red and have a smooth texture."*

**Step 1: Identify query type**
- This is a **Query-by-Feature** (user specifies feature values, not a sample image)

**Step 2: Identify descriptors**
- "mostly red" → **DominantColor** descriptor
- "smooth texture" → **Texture** descriptor (e.g., Gabor filters, LBP)

**Step 3: Specify feature values**
- DominantColor: red (RGB 255,0,0) with high percentage (e.g., 0.7)
- Texture: low frequency, high smoothness (specific values depend on the texture descriptor)

**Step 4: Choose distance metric and threshold**
- Distance metric: **Weighted Euclidean** (to combine color and texture)
- Threshold: **0.4** (allow some variation)

**Step 5: Specify result requirements**
- Max results: **20**
- Order by: **Similarity**

**MPQF**:
```xml
<Mpeg7Query xmlns="urn:mpeg:mpeg7:schema:2001">
    <QueryDescriptor>
        <QueryType>QueryByFeature</QueryType>
        
        <DescriptorUsage>
            <DescriptorName>DominantColor</DescriptorName>
            <Weight>0.6</Weight>
            <FeatureValues>
                <DominantColor>
                    <Color>RGB(255, 0, 0)</Color>
                    <Percentage>0.7</Percentage>
                </DominantColor>
            </FeatureValues>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>Texture</DescriptorName>
            <Weight>0.4</Weight>
            <FeatureValues>
                <Texture>
                    <Smoothness>high</Smoothness>
                    <Frequency>low</Frequency>
                </Texture>
            </FeatureValues>
        </DescriptorUsage>
        
        <SimilarityCriteria>
            <DistanceMetric>WeightedEuclidean</DistanceMetric>
            <Threshold>0.4</Threshold>
        </SimilarityCriteria>
        
        <ResultSpecification>
            <MaxResults>20</MaxResults>
            <OrderBy>Similarity</OrderBy>
        </ResultSpecification>
    </QueryDescriptor>
</Mpeg7Query>
```

**Another Example**: *"Find images similar to this sunset photo, focusing on color."*

**MPQF**:
```xml
<Mpeg7Query xmlns="urn:mpeg:mpeg7:schema:2001">
    <QueryDescriptor>
        <QueryType>QueryByExample</QueryType>
        
        <MediaLocator>
            <MediaUri>sunset.jpg</MediaUri>
        </MediaLocator>
        
        <DescriptorUsage>
            <DescriptorName>DominantColor</DescriptorName>
            <Weight>1.0</Weight>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>ColorLayout</DescriptorName>
            <Weight>0.5</Weight>
        </DescriptorUsage>
        
        <DescriptorUsage>
            <DescriptorName>Texture</DescriptorName>
            <Weight>0.2</Weight>
        </DescriptorUsage>
        
        <SimilarityCriteria>
            <DistanceMetric>Euclidean</DistanceMetric>
            <Threshold>0.5</Threshold>
        </SimilarityCriteria>
        
        <ResultSpecification>
            <MaxResults>10</MaxResults>
            <OrderBy>Similarity</OrderBy>
        </ResultSpecification>
    </QueryDescriptor>
</Mpeg7Query>
```

## Common Pitfalls
- **Confusing MPQF with SQL/MM**: MPQF is a query format (XML), SQL/MM is a database query language (SQL). MPQF can be translated to SQL/MM for execution.
- **Over-specifying descriptors**: using too many descriptors with equal weights can dilute the query. Focus on the most relevant descriptors for the task.
- **Choosing the wrong distance metric**: Euclidean is not always the best. For color histograms, chi-squared or Earth Mover's Distance may be more appropriate.
- **Ignoring normalization**: features with different scales (e.g., color percentages 0-1, texture values 0-1000) need normalization before distance computation.
- **Forgetting to specify weights**: when combining multiple descriptors, weights determine their relative importance. Default weights (all 1.0) may not be appropriate.

## Connections
- [[mpeg-7]] — MPQF is part of the MPEG-7 standard
- [[mpeg-7-descriptors]] — MPQF uses MPEG-7 descriptors (DominantColor, Texture, etc.)
- [[content-based-retrieval]] — MPQF is the query interface for CBIR systems
- [[feature-vector]] — MPQF queries operate on feature vectors (MPEG-7 descriptors)
- [[sql-mm]] — MPQF queries can be translated to SQL/MM for database execution
- [[structured-vs-unstructured-retrieval]] — MPQF bridges natural language queries and structured multimedia data

## Open Questions
- Will MPQF gain wider adoption, or will proprietary query formats dominate?
- How do you translate natural language queries ("find beautiful sunsets") to MPQF? This requires NLP and semantic mapping.
- Can MPQF handle deep learning embeddings? MPEG-7 descriptors are hand-crafted; modern systems use CNN embeddings.
- How do you optimize MPQF query execution? Parsing XML and computing distances for millions of items is slow.
- Can MPQF support interactive queries (relevance feedback)? The user marks results as relevant/irrelevant, and the system refines the query.
