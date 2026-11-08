---
title: "Search Spaces and Fitness Landscapes"
tags: [concept, search-based-software-engineering, semester-2, optimisation]
course: "Search-Based Software Engineering"
source_count: 3
status: current
last_updated: 2026-11-07
prerequisites: ["[[metaheuristics]]"]
---

## One-line Summary

A fitness landscape is the search space with a fitness value attached to every solution and a
neighbourhood relation between solutions — and its shape (single-peaked, rugged, plateau, needle)
predicts whether a search will work, not the problem's difficulty class.

## Core Intuition

The search space is what you are allowed to pick from; the fitness landscape is what you see
while picking. Two things must be fixed before either exists: the representation (which points
count as solutions) and the neighbourhood (which points count as one step apart). Change the
neighbourhood and you have changed the landscape — the same fitness function can be smooth under
one move set and a minefield under another.

The course's own working definition, from the lab notebook: "A fitness landscape consists of
three things" — the solutions, their fitness, and the neighbourhood. And its most useful
clarification: "A landscape is not a property of the problem alone: it also depends on the
neighbourhood. With a different `get_neighbours`, the same solutions and fitness function form a
different landscape, possibly with fewer local optima or none at all. Choosing the neighbourhood
is a design decision, and often matters more than the choice of algorithm."

The second intuition is what the algorithm can and cannot see: "A local search walks around this
landscape, but it can only see the height of its current solution and its immediate neighbours.
It cannot tell a local optimum from a global one."

## Formal Definition / Statement

**Search space.** From the lecture, with the worked constraint example "find point in the
x = (x₁, x₂) plane that minimises f(x) = x₁² + x₂², subject to the constraint x₁ + x₂ = 3":

- "Search space S: all x ∈ S are admissible solutions (i.e. satisfy constraints)"
- "Optimal solutions: f(x) ≤ f(y), ∀y ∈ S"
- "Size of optimisation problem: degrees of freedom"
- "Search space size |S|: number of solutions in S"
- "If |S| is infinite or uncountable, we have a continuous optimisation problem"
- "Combinatorial optimisation problem has a discrete, countable search space"

**Fitness landscape.** "Fitness landscape is a representation of f that preserves the
neighbourhood topology" — "search space with a fitness value for each configuration and a
neighbourhood relationship". Given a solution space S and a fitness function F, "a fitness
landscape is a hyper dimensional surface that represents F: S → R". The optimum is defined
analytically: "points at which all first-order partial derivatives vanish (∇F = 0)". And the
practical caveat: "Usually impossible to visualise."

**Neighbourhood and move operators** (stated in the local-search lecture and needed here):
"Neighbourhood V(x) for x ∈ S: set of solutions y that one can reach from x in one step", usually
defined implicitly by transformations Tᵢ, "if y in V(x) then there is an i for which y = Tᵢ(x)"
— the transformations are the "moves".

## Key Properties

The lecture's taxonomy of landscape shapes, and the consequence of each:

| Shape | What it looks like | Consequence for search |
|---|---|---|
| Single-peak / few peaks | one smooth hill | "easy" |
| Local optimum | a peak that is not the highest | search stops early, believing it is done |
| Rugged | many peaks and valleys | "very rugged landscapes are difficult" |
| Plateau | "large flat region that does not exhibit any gradients" | "there is no guidance; hard to escape" |
| Needle in the haystack | one point of good fitness, everything else equal | "worst landscape to search" |

**Ruggedness is a trade, not a defect.** The slide contrasts "easy to get stuck in one of many
local optima" against "smooth descent" — a smooth landscape gives guidance but traps a greedy
climber, a rugged one gives many escape routes but no direction.

**The needle can sometimes be removed by re-designing the fitness function.** The slide's own
repair: for the target (x, y) = (15, 15), the naive f₁(x, y) = (x == 15 && y == 15) ? 0 : 10 is a
needle; f₂(x, y) = |x − 15| + |y − 15| is the same problem with a gradient. "Can be avoided by
transforming the problem and/or designing better fitness functions."

**On the artificial example** (0 ≤ x ≤ 10, 0 ≤ y ≤ 10, find (x, y) such that x + y = 10) the
fitness is "how far are we from solving the problem": if the current sum is s, then
f(x, y) = |10 − (x + y)|, and search minimises it until it reaches 0. This is the canonical move
from a *predicate* ("solved / not solved") to a *distance* — the same move the needle repair
makes, and the same move that makes test-data generation searchable at all.

## Worked Example

**The n-queens slice, from the lab notebook (a 2-D projection of a 30-queen landscape).** The
notebook fixes every queen but the first two and varies those two over a 30 × 30 grid, so a
900-cell picture of the landscape exists:

- The dark bands "running across the picture are the rows in which one of our two movable queens
  collides with a queen we left fixed. A whole line of the plot drops in fitness at once,
  regardless of what the other queen is doing. The fainter diagonal structure comes from the
  diagonal attacks. This is the constraint structure of the problem, made visible."
- Between the bands the surface is bumpy: "There is no single smooth hill leading to the best
  cell; instead there are a great many small peaks, and the brightest cell is only slightly
  brighter than a good number of its rivals."
- Measured: a single hill climber visits "4 of 900" cells and reaches fitness 409 against a slice
  best of 410; with random restarts, "243 of 900" cells are visited and the best is found. "The
  hillclimber walks a short way uphill and then stops on a peak that is not the best one in the
  picture – as it does from most starting cells."
- Conclusion drawn by the notebook itself: "Local optima and global optima look exactly the same
  to an algorithm that can only see its immediate neighbours."

**The One Max vs Leading Ones contrast** (evolutionary-algorithms lab) shows the same idea
without pictures. Both have exactly one local optimum under single-bit flips, so both are
"unimodal" — and yet they behave completely differently. At fitness 10 on n = 100:

| Landscape | improving | neutral | worsening |
|---|---|---|---|
| One Max | 90 | 0 | 10 |
| Leading Ones | 1 | 89 | 10 |

Measured over random walks: "One Max: median neutral fraction 0.000, median autocorrelation
0.980" against "Leading Ones: median neutral fraction 0.980, median autocorrelation 0.971". The
notebook's verdict: "Unimodality guarantees an improving neighbour exists, but says little about
how easy it is to find."

## Common Pitfalls

- **Treating the landscape as a property of the problem.** It is a property of problem *plus*
  representation *plus* neighbourhood.
- **Equating unimodal with easy.** Leading Ones is unimodal and still hard: one improving move
  against 89 neutral ones.
- **Reading a picture of a slice as the real landscape.** The notebook is explicit: "A slice
  shows us what a parameter does, but not which value is best for the real problem" — the 900-cell
  slice versus the 12-queens space of "almost 9 × 10¹²" solutions.
- **Forgetting that plateaus need equal-fitness moves to be traversable.** Hill climbing "gets
  stuck on plateaux unless we also admit solutions with equal fitness".
- **Designing a needle and then blaming the algorithm.** A predicate-style fitness (0 for solved,
  constant otherwise) destroys all guidance; the repair is a distance.
- **Trying to visualise.** Beyond two parameters (three with fitness) it is "usually impossible";
  aggregate statistics (neutral fraction, autocorrelation, ECDF) replace the picture.

## Connections

- [[metaheuristics]] — the class of algorithms that walk these landscapes.
- [[hill-climbing]] — the purest walker: it sees only the immediate neighbourhood, so every
  property listed here is a statement about its failure modes.
- [[tabu-search]], [[simulated-annealing]] — the two repairs for local optima and plateaus.
- [[evolutionary-algorithm]] — a population-based walk, where neutrality and autocorrelation
  become measured quantities.
- [[search-algorithm-evaluation]] — how to compare two search configurations that produce
  different distributions of outcomes.

## Open Questions

- **The lecture gives no way to compute ruggedness or neutrality for a real software-engineering
  problem**; the lab measures them only on bit strings.
- **The claim that neighbourhood choice "often matters more than the choice of algorithm"** is
  asserted from experience; no experiment in the material compares the two factors.
- **No guidance on how to transform a predicate fitness into a distance automatically** — every
  example is hand-designed.
- **The optimum condition ∇F = 0** applies to continuous landscapes only, but the slide presents
  it alongside combinatorial examples without separating the cases.