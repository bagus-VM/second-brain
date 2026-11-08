---
title: "MOQL (Multimedia Object Query Language)"
tags: [concept, multimedia-databases, semester-1, query-languages, moql, oql-extension]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[oql]]", "[[multimedia-query-languages]]", "[[object-relational-databases]]"]
---

## One-line Summary
An extension of OQL that adds spatial relations, temporal interval logic, a contains predicate, and a presentation clause to the WHERE clause.

## Core Intuition
OQL already handles objects, identity, and path expressions. What it cannot express is multimedia specific structure: "is this lake inside this region," "does this clip come before that clip," or "show the result video in this window layout." MOQL bolts these onto OQL's WHERE clause rather than inventing a new query shape. The idea is that users already know OQL or SQL syntax, and object orientation is a good fit for modelling media objects, so extending the familiar language beats starting over.

The extensions target four gaps: where things are in space (spatial_expression), when things happen in time (temporal_expression), what an object contains (contains_predicate), and how results are shown (the present clause). VisualMOQL, part of the DISIMA project, implements the image portion. The language is a prototype, runs on ObjectStore, and notably has no audio support.

## Formal Definition / Statement

MOQL extends the WHERE clause of OQL queries with four constructs:
- **spatial_expression**: spatial relations between geometric objects
- **temporal_expression**: temporal relations between time intervals
- **contains_predicate**: a containment relation for media objects
- **present clause**: presentation functions for result layout

### Spatial predicates

Predicates are indexed by the geometry types of their two operands (Point, Line, Region):

| Return | Point | Line | Region (circle, rectangle) |
|--------|-------|------|----------------------------|
| Point | nearest, farthest | within, midpoint | centroid, inside |
| Line | cross | intersect | inside (contains), cross |
| Region | cover (coveredBy), topological_predicate, cross | cover, cross | directional_predicate |

Directions supported: left, right, above, below, front, back, north, south, west, east, northwest, and combinations with front/back (front_left, back_north, and so on).

### Spatial functions

| Return | Point | Line | Region | Value |
|--------|-------|------|--------|-------|
| Point | nearest, farthest | | region | |
| Line | intersect | intersect | region | length, slope |
| Region | | centroid | interior, exterior, mbr | area, perimeter |

Example query:
```
select lake, area(lake.region)
from   Lakes lake
where  lake.region coveredBy SachsenAnhalt
  and  area(lake.region) > 10
```

### Temporal relations

Defined over time intervals: equal, before, after, meet, metBy, overlap, overlappedBy, during, include, start, startedBy, finish, finishedBy.

- A time interval has a start and an end.
- A time point is a time interval for which start equals stop.
- Time constructs: year, month, day, hour, minute, second, ms.

### Temporal continuous media (video)

Functions operate on Frame, clip, and video:

| Return | Frame | clip | video |
|--------|-------|------|-------|
| Frame | prior, next | clip | |
| clip | firstFrame, lastFrame, nth | prior, next | video |
| video | | firstClip, lastClip, nth | |

Predicates for camera motions: zoomIn, zoomOut, panLeft, panRight, tiltUp, tiltDown, cut, fade, wipe, dissolve.

Example video query, "find the first film segment with person MrX from the video JamesB":
```
select firstClip(
  select c from JamesB.clips c
  where c contains MrX
  order by lowerBound(c.timestamp)
)
```

### Presentation functions

A new present clause:
```
select ... from ... where ...
present layout { and layout }
```
The layout is built from spatial and temporal entries, or from a user defined scenario. Entries and functions include atWindow, play, parStart, display.

### VisualMOQL and DISIMA
- VisualMOQL implements the image part of MOQL.
- It is part of the DISIMA project (Distributed Image Database Management System), supporting content based queries on salient objects and declarative queries.

## Key Properties / Complexity

### What MOQL adds over OQL
- Spatial reasoning over Point, Line, and Region geometries with both predicates (boolean) and functions (value returning).
- Temporal reasoning over intervals with the full Allen style relation set (before, meet, overlap, during, and the rest).
- Video specific frame and clip navigation plus camera motion predicates.
- A presentation clause that controls where and how results are displayed, something SQL has no concept of.

### Scope limits
- No audio support. The temporal machinery targets video; audio is not covered.
- Prototype only. Implemented on ObjectStore, not a production system.
- In theory it satisfies all requirements of a general MM query language. In practice, only the image part (VisualMOQL) was implemented.

### Query shape
- Spatial and temporal predicates compose with AND in the WHERE clause, so a query can ask for lakes inside a region with area above a threshold, or for clips that overlap a time window and contain a person.
- The present clause is separate from filtering, so layout does not interfere with selection logic.

## Worked Example

A combined spatial and attribute query: find lakes in Saxony Anhalt larger than 10 area units.
```
select lake, area(lake.region)
from   Lakes lake
where  lake.region coveredBy SachsenAnhalt
  and  area(lake.region) > 10
```
Step by step:
1. `Lakes lake` binds the identifier lake to each lake object.
2. `lake.region coveredBy SachsenAnhalt` applies the spatial predicate coveredBy between each lake's region and the region object SachsenAnhalt.
3. `area(lake.region) > 10` applies the spatial function area to each surviving lake's region and keeps only those above 10.
4. The projection returns the lake object and its computed area.

A temporal video query: find the first clip in JamesB that contains MrX.
```
select firstClip(
  select c from JamesB.clips c
  where c contains MrX
  order by lowerBound(c.timestamp)
)
```
1. The inner query selects clips c from JamesB.clips where the contains_predicate `c contains MrX` holds.
2. Results are ordered by the lower bound of each clip's timestamp.
3. firstClip returns the first element of that ordered set, giving the earliest segment containing MrX.

## Common Pitfalls
- **Confusing coveredBy and cover**: coveredBy and cover are inverse directional relations. Swapping them reverses which object must contain the other.
- **Treating a time point as distinct from an interval**: MOQL defines a time point as an interval where start equals stop. Code that assumes points and intervals are separate types will misapply the temporal predicates.
- **Expecting audio support**: MOQL has none. Queries about audio content cannot be expressed.
- **Assuming a production implementation**: MOQL was a prototype on ObjectStore via VisualMOQL for images. Do not assume a modern DBMS ships it.
- **Mixing presentation into the WHERE clause**: layout belongs in the present clause, separate from filtering. Putting display logic in the WHERE clause is a category error in MOQL.

## Connections
[[oql]]: MOQL extends OQL's WHERE clause and reuses its select from where shape.
[[multimedia-query-languages]]: MOQL is the representative extension of OQL in the first MMQL category.
[[sql-mm]]: the parallel extension of SQL with spatial and still image UDTs; SQL/MM Spatial covers similar geometry ground.
[[object-relational-databases]]: MOQL's object model assumes an OR style store with object identity and path expressions.
[[multimedia-query-predicates]]: the spatial, temporal, and contains predicates MOQL introduces.
[[mpqf]]: the from scratch alternative that also handles multimedia query conditions, compared against MOQL in the MMQL categories.

## Open Questions
- Could MOQL's temporal interval relations be reused for audio, given that audio segments are also intervals?
- How would MOQL's spatial predicate table extend to 3D regions for volumetric or point cloud data?
- Is there value in reviving MOQL's present clause idea for modern multimedia presentation, or do application layer frameworks make it redundant?
- How does the contains_predicate interact with object detection confidence? The prototype assumes crisp salient objects, but real detection is probabilistic.
