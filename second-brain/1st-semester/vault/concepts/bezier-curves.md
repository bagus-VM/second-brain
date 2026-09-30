---
title: "Bézier Curves"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [vector-graphics-svg]
---

## One-line Summary
Bézier curves are parametric curves defined by a set of control points, using Bernstein polynomials as basis functions; the curve is a weighted blend of control point positions as parameter t goes from 0 to 1.

## Core Intuition
Imagine pulling a string between two endpoints while "magnets" (control points) tug the string toward them. The curve bows toward the control points but doesn't necessarily pass through them (except the first and last). Moving a control point smoothly deforms the entire curve — this is why they're so useful for design: intuitive, smooth, and mathematically well-behaved.

## Formal Definition / Statement
Given d+1 control points p₀, p₁, ..., p_d, the Bézier curve of degree d is:

```
x(t) = Σᵢ₌₀ᵈ pᵢ · Bᵢᵈ(t)
```

where the **Bernstein basis polynomials** are:

```
Bᵢᵈ(t) = C(d,i) · tⁱ · (1-t)^(d-i)
```

and C(d,i) = d! / (i! · (d-i)!) is the binomial coefficient.

**Derivation from Hermite splines**: A Hermite cubic spline x = at³ + bt² + ct + d is determined by 4 constraints (pass through endpoints at t=0,1 and match given derivatives). Solving gives the coefficients. Bézier curves reparameterize this: instead of derivative values, control points *geometrically* determine the tangent directions.

**Key**: the first and last control points are *interpolated* (the curve passes through them); intermediate control points only *influence* the curve's shape.

## Key Properties / Complexity
- **Endpoint interpolation**: curve passes through p₀ and p_d
- **Tangent property**: tangent at p₀ points toward p₁; tangent at p_d points toward p_{d-1}
- **Convex hull**: the curve lies entirely within the convex hull of its control points
- **Affine invariance**: transforming all control points = transforming the curve
- **Variation diminishing**: the curve doesn't oscillate more than its control polygon
- **Degree = number of segments minus 1**: cubic Bézier (degree 3) uses 4 control points, most common in practice
- **Bézier vs. Hermite**: Hermite specifies endpoints + derivatives; Bézier specifies endpoints + geometric control points — more intuitive for designers

**Bernstein polynomials** for cubic (d=3):
- B₀³(t) = (1-t)³
- B₁³(t) = 3t(1-t)²
- B₂³(t) = 3t²(1-t)
- B₃³(t) = t³

These always sum to 1 (partition of unity), ensuring the curve is a convex combination of control points.

## Worked Example
Cubic Bézier with 4 control points p₀=(0,0), p₁=(1,2), p₂=(3,2), p₃=(4,0):

At t=0: curve is at p₀ = (0,0)
At t=0.5: x = 0·(0.125) + 1·(0.375) + 3·(0.375) + 4·(0.125) = 0 + 0.375 + 1.125 + 0.5 = 2.0
           y = 0·(0.125) + 2·(0.375) + 2·(0.375) + 0·(0.125) = 0 + 0.75 + 0.75 + 0 = 1.5
At t=1: curve is at p₃ = (4,0)

The curve starts at origin, bows upward toward the control points, and returns to the x-axis.

## Common Pitfalls
- Confusing control points with interpolation points — only first and last are on the curve
- Thinking Bézier curves can represent circles/exact conics — they can only approximate (use rational Béziers/NURBS for exact conics)
- Forgetting the convex hull property — useful for fast bounding-box tests in rendering
- Piecewise cubic Béziers (joined end-to-end) are used in practice; a single high-degree Bézier is numerically unstable

## Connections
- [[vector-graphics-svg]] — SVG `<path>` uses cubic and quadratic Bézier commands (C, Q)
- [[linear-convolution-filters]] — rendering Bézier curves to raster involves sampling/rasterization
- [[image-file-formats]] — PostScript/PDF use Bézier curves for font outlines and vector paths

## Open Questions
- How do NURBS (Non-Uniform Rational B-Splines) extend Bézier curves for CAD applications?
- What is de Casteljau's algorithm and why is it numerically more stable than direct polynomial evaluation?
