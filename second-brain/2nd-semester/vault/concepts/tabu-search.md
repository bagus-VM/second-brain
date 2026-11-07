---
title: "Tabu Search"
tags: [concept, search-based-software-engineering, semester-2, local-search]
course: "Search-Based Software Engineering"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[hill-climbing]]"]
---

## One-line Summary

Tabu search always moves to the best non-forbidden neighbour — even if it is worse than the
current solution — and keeps a short-term memory of recent moves so the search cannot immediately
undo itself.

## Core Intuition

Hill climbing's weakness is that it refuses to lose ground. Tabu search fixes that with two
changes, and only two: it accepts a worse neighbour when that neighbour is the best available, and
it forbids the moves it just made. The first change lets the search walk out of a local optimum
(downhill); the second stops it from walking straight back in (oscillation).

The memory is deliberately short-lived. "Tabu attribute is not permanent (usually a certain number
of iterations)" — so a region is excluded for a while and then becomes available again, which is
what lets the search commit to a direction instead of circling.

## Formal Definition / Statement

The slide's specification, verbatim in substance:

- "Proposed 1986 by F. Glover."
- "Starting from arbitrary solution."
- "Search operator selects xₙ₊₁ in V(xₙ) as the non-tabu xₙ₊₁ that locally optimises fitness."
- "Choice is independent of the fitness of the current solution f(xₙ). (If there is more than one
  candidate, one is chosen randomly.)"
- "Tabu prevents re-exploration of already visited parts of search space."
- "Tabu implemented as a list to enumerate forbidden points and movements. Tabu list is
  continuously updated."

That third bullet is the whole difference from hill climbing: "locally optimises fitness" is
computed over the neighbouring set, not relative to the current point, so a move is taken even
when every neighbour is worse than where you stand.

**Implementation choices the slide names:**

- "Obvious implementation of tabu list: circular buffer."
- "Often it is more convenient to store items that are related to the visited solutions, rather
  than the solutions themselves, e.g. attributes belonging to the visited solutions such as
  fitness values; moves that have been used to explore the search space."
- **Banning time / tabu tenure:** "if a move m has been used in iteration t, or the attribute h
  characterises the current solution at time step t, then the inverse move of m, or the attribute
  h, will be forbidden until iteration t + k, where k is the banning time"; and "k is often chosen
  randomly in each iteration according to a specific probability distribution."

## Key Properties

**Memory is over moves or attributes, not over solutions.** This is the practical point of the
circular-buffer remark: storing full solutions is expensive, and the thing you actually want to
prevent is the *inverse move*.

**The tabu list size is a real parameter with a measured effect.** The lecture runs the same
50-step search on the same objective function with tabu size 4 and tabu size 10 and shows the
trajectories side by side; the lab's own conclusion is that the parameter was chosen "by
guesswork". The course treats parameter tuning as a separate later chapter.

**Tabu search is a strong baseline in the lab's comparison.** Holm-corrected Mann-Whitney over 30
runs: "Random Search vs Tabu Search p = 5e-08", "Hill Climbing vs Tabu Search p = 4.9e-08", and
"Tabu Search vs Simulated Annealing p = 0.5" — i.e. tabu search and simulated annealing are not
distinguishable on that instance, while both beat random search and hill climbing clearly.

**Aspiration is implied, not stated.** Because the rule is "the non-tabu xₙ₊₁ that locally
optimises fitness", a tabu move that would reach the best solution seen so far is still excluded
by the slides' formulation. The classic aspiration criterion (override the tabu status when the
move beats the best known solution) does not appear in this material.

## Worked Example

**The lecture's 2-D grid instance.** Objective function f(x, y) over "S = {0, 1, …, 19} ×
{0, 1, …, 19}", with a global optimum at P₁ = (10, 10), a local maximum at P₂ = (6, 6), and the
4-neighbourhood V(x, y) = {(x−1, y), (x+1, y), (x, y−1), (x, y+1)}. Three 50-step trajectories are
shown from the same start (7, 8):

1. **Random walk, 50 iterations** — the scatter baseline.
2. **Tabu search, 50 steps, tabu size 4.**
3. **Tabu search, 50 steps, tabu size 10.**

The comparison the slides intend is visible in the picture rather than stated as a number: the
random walk diffuses; tabu search with a small list can loop back around the same basin; with a
longer list it is pushed further across the grid. This is the same instance the course uses to
argue that list size is not a cosmetic parameter.

**In the lab, on n-queens**, tabu search is one of the four algorithms compared under a shared
evaluation cap with a tabu list size of 50 and a restart when "every neighbour is tabu" — the
implementation detail the slides leave out: a tabu search can reach a state where *all* neighbours
are forbidden, and something must happen then.

## Common Pitfalls

- **Treating the tabu list as a visited-set.** It bans recent moves or attributes for a bounded
  tenure; it does not prevent revisiting a solution by another route, and after k iterations it
  forgets.
- **Confusing tabu list size with memory length in evaluations.** The tenure is in iterations,
  which is not the same as fitness evaluations, so budgets across algorithms are not comparable
  without care.
- **Never unblocking.** If every neighbour is tabu, the plain algorithm has no legal move; the
  lab's restart is one answer, and the slides do not discuss the case at all.
- **Reading "independent of the fitness of the current solution" as "ignores fitness".** It
  ignores the *current* value as a threshold; it still maximises over the neighbourhood.
- **Assuming it always improves.** The trajectory can spend many iterations worse than its best
  seen value; only the best-seen value is the result.
- **Picking the tenure by intuition** — the course's own lab flags exactly this and defers to the
  tuning chapter.

## Connections

- [[hill-climbing]] — the algorithm tabu search repairs: same neighbourhood, different acceptance
  rule, plus memory.
- [[simulated-annealing]] — the alternative repair: stochastic acceptance instead of memory. The
  lab finds them statistically indistinguishable on n-queens.
- [[fitness-landscape]] — why accepting a worse move is necessary at all.
- [[search-algorithm-evaluation]] — the p-values and effect sizes quoted above come from that
  procedure.
- [[metaheuristics]] — the general properties.
- [[search-based-software-engineering-lecture-2]] — the lecture that presents it.

## Open Questions

- **No aspiration criterion is given**, so the slides' tabu search can be blocked from the best
  solution it has already found — a standard omission with a standard fix that the material
  never mentions.
- **How to choose the tenure k** is stated as "often chosen randomly … according to a specific
  probability distribution", but the distribution is not given.
- **The dead-end case (all neighbours tabu)** is unaddressed in the slides.
- **Memory cost is not discussed**: the circular buffer is named, but no bound on the list length
  in terms of problem size is given.