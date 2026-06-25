---
title: "MPEG-7 Structural Description"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
MPEG-7 structural description tools enable spatial, temporal, spatio-temporal, and media-type based segmentation of multimedia content using the SegmentType hierarchy.

## Core Intuition
Multimedia content has structure: an image has regions, a video has shots, a scene has moving objects. MPEG-7's structural description tools let you decompose complex multimedia content into meaningful segments and describe the relationships between them. This is the "skeleton" onto which semantic descriptions are attached.

## Formal Definition / Statement
The structural description uses the **SegmentType** (Segment DS) as its root element. The Segment DS hierarchy includes:

- **StillRegionDS** — spatial segments of still images
  - StillRegionSpatialDecomposition
  - SpatialMask datatype
  - ImageTextDS
- **VideoSegmentDS** — temporal segments of video
  - VideoSegmentTemporalDecomposition
  - VideoSegmentSpatialDecomposition
  - VideoSegmentSpatioTemporalDecomposition
  - VideoSegmentMediaSourceDecomposition
  - VideoTextDS
- **MovingRegionDS** — spatio-temporal segments (moving objects)
  - MovingRegionSpatialDecomposition
  - MovingRegionTemporalDecomposition
  - MovingRegionSpatioTemporalDecomposition
  - MosaicDS

**Segment types correspond to decomposition dimensions:**
- Spatial: decompose a still image into regions (StillRegion)
- Temporal: decompose video/audio into time segments (VideoSegment, AudioSegment)
- Spatio-temporal: decompose into moving regions (MovingRegion)
- Media-type: decompose mixed content into media components

**Segment composition** allows:
- Connected segments (single region/object)
- Non-connected segments (multiple regions treated as one entity)

## Key Properties
- Spatial segments use SpatialMask with polygon coordinates
- Temporal segments use MediaTimePoint and MediaDuration
- Spatio-temporal segments track objects across frames
- Segments can overlap or have gaps (controlled by `gap` and `overlap` attributes)
- Each segment can carry its own descriptors (visual, audio) and semantic annotations

## Worked Example
Image with spatial decomposition:
```xml
<MultimediaContent xsi:type="ImageType">
  <Image>
    <SpatialDecomposition gap="true" overlap="false">
      <StillRegion id="AlexSR">
        <VisualDescriptor xsi:type="ScalableColorType" numOfCoeff="16"
          numOfBitplanesDiscarded="0">
          <Coeff>1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6</Coeff>
        </VisualDescriptor>
      </StillRegion>
      <StillRegion id="AnaSR">
        <VisualDescriptor xsi:type="ScalableColorType" numOfCoeff="16"
          numOfBitplanesDiscarded="0">
          <Coeff>1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6</Coeff>
        </VisualDescriptor>
      </StillRegion>
    </SpatialDecomposition>
  </Image>
</MultimediaContent>
```
This describes an image decomposed into two still regions (AlexSR and AnaSR), each with its own color descriptor.

## Common Pitfalls
- Confusing structural description with semantic description — structure is about "where/when", semantics is about "what it means"
- Forgetting that segments can be non-connected (e.g., a person's face and hands as one segment)
- Assuming decomposition is always hierarchical — it can be flat or nested

## Connections
- [[mpeg-7]] — structural description is one of the three pillars of MPEG-7
- [[mpeg-7-semantic-description]] — semantic annotations can be attached to structural segments
- [[mpeg-7-descriptors]] — descriptors are attached to segments
- [[mpeg-7-indexing-pyramid]] — structural description covers pyramid levels 1–4

## Open Questions
- How do modern video segmentation algorithms map to MPEG-7's segment hierarchy?
- Is the segment-based approach still viable with today's dense prediction models?
