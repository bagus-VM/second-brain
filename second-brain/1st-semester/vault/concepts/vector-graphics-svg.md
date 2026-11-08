---
title: "Vector Graphics and SVG"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [image-representation-bitmap]
---

## One-line Summary
Vector graphics are mathematically defined drawing instructions (curves, lines, shapes) in a coordinate system, as opposed to pixel arrays; SVG is the web standard XML format for 2D vector graphics.

## Core Intuition
**Instead of storing a colour for every pixel (millions of values), vector graphics store a small set of mathematical instructions: "draw a curve from A to B with control points C and D, in red, 2px thick."** The image is *computed* at display time (rendered). This means you can zoom infinitely without pixelation, because the math scales perfectly. It's like the difference between a recipe (vector) and a photograph of a meal (raster).

## Formal Definition / Statement
Vector graphics = programmatically defined drawing instructions within a coordinate system.
Geometric transformations (scale, rotate, translate) are exact and trivial — they just transform the control points. Individual elements (layers, groups, objects) can be separated and their attributes (colour, line thickness, fill) modified independently.

**SVG (Scalable Vector Graphics)**:
- W3C standard for 2D vector graphics in XML
- Three types of graphical objects: **Shapes** (paths of curves/lines), **Images** (embedded raster), **Text**
- Features: global transformations, clipping paths, alpha masks, filter effects, object templates
- Objects can be grouped, styled (CSS), transformed, combined
- SVGs can be interactive and dynamic
- Coordinate system: (0,0) at top-left, default units = screen pixels; header defines width/height/units
	- ![[Pasted image 20260609110111.png]]

**Vector graphics formats**: PostScript (.ps, .eps), PDF, WMF/EMF, Corel Draw (.cdr), SVG, VRML (3D)

## Key Properties / Complexity
- Resolution-independent: scales to any size without quality loss
- Small file size for simple images (stores math, not pixels)
- Requires **rendering** (interpretation/drawing) to become visible — a computational cost
- Not suitable for photographic content (too many "instructions" needed)
- Individual elements are editable: change colour of a shape without touching anything else
- SVG integrates with web standards (CSS, JavaScript, DOM)

## Worked Example
An SVG path for a leaf shape:
```xml
<path stroke="sienna" stroke-width="2" fill="none"
  d="M 80,180
     Q 50,120 80,60
     Q 90,40 80,20
     Q 100,20 120,20
     Q 110,40 120,60
     Q 150,120 120,180Z" />
```
This defines a closed shape using quadratic Bézier curves — only 12 coordinate values instead of thousands of pixels.

## Common Pitfalls
- Confusing vector with raster — vector stores *instructions*, raster stores *pixel values*
- Forgetting that vector graphics require rendering (not instant display like bitmaps)
- Assuming vector is always better — photographic images are fundamentally raster
- SVG coordinate system has (0,0) at **top-left**, not bottom-left (common confusion from math)

## Connections
- [[bezier-curves]] — SVG paths use Bézier curves as their primary drawing primitive
- [[image-representation-bitmap]] — the complementary representation (raster vs. vector)
- [[image-file-formats]] — SVG is a file format; PDF/PostScript are also vector-based
- [[jpeg-compression-pipeline]] — JPEG is for raster images; no equivalent "JPEG for vectors"

## Open Questions
- How do hybrid formats (PDF with embedded raster images) handle the vector/raster boundary?
- What are the performance tradeoffs of SVG rendering vs. pre-rendered raster at fixed resolution?
