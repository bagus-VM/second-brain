---
title: "Hill Climbing"
tags: [concept, search-based-software-engineering, semester-2, local-search]
course: "Search-Based Software Engineering"
source_count: 3
status: current
last_updated: 2026-11-07
prerequisites: ["[[fitness-landscape]]"]
---

## One-line Summary

Hill climbing picks the best neighbour and moves there, repeating until no neighbour is better —
cheap, monotone, and therefore certain to stop at whatever local optimum it happens to walk into.

## Core Intuition

"Like climbing Everest in thick fog with amnesia." You can measure the slope under your feet and
nothing else; you always step uphill; you stop when every direction is downhill — which on Everest
is usually a false summit, and you will never know, because a false summit and the real one feel
identical.

The algorithm has no memory and no willingness to lose ground. That is exactly why it is fast
(few fitness evaluations, no bookkeeping) and exactly why it is fragile: monotone improvement
cannot cross a valley, and a flat region provides no direction at all.

## Formal Definition / Statement

The local-search template all three algorithms in this lecture share (the slide states it once,
before hill climbing):

1. "For a given problem we define a search space S and an objective function f: S → R".
2. "Neighbourhood V(x) for x ∈ S: set of solutions y that one can reach from x in one step",
   usually defined implicitly by transformations Tᵢ — "if y in V(x) then there is an i for which
   y = Tᵢ(x)". The transformations are the "moves".
3. "Exploration operator U: applied on a current solution x₀ generates the next point to explore
   in the search trajectory", making use of the fitness values in the neighbourhood.
4. "Exploration process x₀ → x₁ ∈ V(x) → x₂ ∈ V(x₁) → … continues until a stopping criterion is
   met."

"The result is either the last xₙ in the trajectory, or the xᵢ found along the trajectory that
produces the best fitness value." Which of the two is reported is a design decision, and the
lecture does not settle it.

**Hill climbing** = this template with U = "choose best neighbour". The five steps, from the
slide: select a random value; explore the neighbourhood; choose a better neighbour; repeat until
the optimum is found.

**Variants of U** listed by the slide:

- "Choose first neighbour with better fitness" (first ascent, instead of steepest ascent).
- "Randomised iterative improvements: worsening moves accepted with certain probability."
- "Probabilistic hill climber: next search point x′ in V(x) is selected with probability p(x′)
  that is proportional to the fitness f(x′)" — for a maximisation problem with positive f,
  p(x′) = f(x′) / Σ_{y ∈ V(x)} f(y).

## Key Properties

**Monotonicity is the defining property, and it cuts both ways.** "Regardless of strategy, hill
climbing monotonically climbs, until it reaches local/global optimum; it never goes down."

**Pros, as the slide lists them:** "cheap (fewer fitness evaluations compared to global search
algorithms), easy to implement, repeated applications can give insights into the landscape,
suitable for solutions that need to be built through small incremental changes."

**Cons, same slide:** "more likely to get stuck in local optima, unable to escape local optima."

**Plateaus need a special case.** "Gets stuck on plateaux unless we also admit solutions with
equal fitness." The lab's measurements make the cost concrete: on Leading Ones at fitness 10 of
n = 100, 89 of 100 single-bit neighbours are neutral, and hill climbing's steepest-ascent variant
therefore spends "n evaluations per completed neighbourhood scan" to find the single improving
move — "evaluating all the other neighbours does not produce a better improvement."

**Restart is the standard repair, and it is a real trade.** "If search gets stuck: Random
Restart." The lab quantifies what restarting buys and costs: a single climb visits 4 of 900 cells
in its slice and lands on a peak that is not the best; with restarts, 243 of 900 cells are
visited and the slice best is found. "But it also discards everything it has learned every time it
restarts: a restart is exactly as likely to land in a hopeless region as a promising one, and a
climb that was heading somewhere good gets no more attention than one that was not."

**Steepest ascent vs first ascent is an evaluation-budget choice.** "The version we considered is
called steepest ascent hillclimbing, because it will always explore all neighbours, and then pick
the best one. An alternative approach is first ascent, which will pick the first neighbour that
has a better fitness value. We scan the neighbours in random order; with a fixed order, first
ascent would always try to move the first queen before any other." And: "Both must stop at the
same evaluation cap, including initialization. This makes different amounts of search work visible
on the horizontal axis."

## Worked Example

**The 8-queens problem**, the lecture's first worked instance: place 8 queens on an 8 × 8 board so
that they cannot check each other, with the heuristic h = "number of attacks" to minimise. The
slide's local-optimum illustration is a concrete board with fitness 1 and the diagnosis: "check
col. 4 and 7, white diagonal — and every change will create a worse state." The search is stuck
at one attack, and a restart is the only way out (the slide's next step is literally "Local
search → Restart").

**The lab version, measured.** On the n-queens slice the hill climber's trace ends: "Best fitness
visited: 409 (best in this slice: 410); distinct cells visited: 4 of 900", and "the hillclimber
walks a short way uphill and then stops on a peak that is not the best one in the picture – as it
does from most starting cells, according to the count above. All of its neighbours are worse, so
by its own rule it has finished – and it has no way even to tell that it is standing on a minor
peak rather than on the best solution available." With random restarts the same code reports
"Best fitness visited: 410 (best in this slice: 410); distinct cells visited: 243 of 900."

**Against random search, hill climbing wins decisively in the lab's comparison of randomised
algorithms** — the notebook's Holm-corrected table reports "Random Search vs Hill Climbing"
at p = 6e-12 over 30 runs per algorithm. That table is the reason the course insists on random
search as the baseline rather than on intuition.

## Common Pitfalls

- **Reporting the last point instead of the best point** (or vice versa) without saying which —
  the template allows both, and they differ once the trajectory descends, which is exactly what
  the variants do.
- **Assuming "the optimum is found" in the loop condition is a check.** Nothing is checked; the
  loop ends when no neighbour improves, which is locally optimal and nothing more.
- **Forgetting equal-fitness moves on a plateau** — without them the search halts on flat ground
  that is not a peak at all.
- **Comparing budgets dishonestly.** First ascent and steepest ascent spend different numbers of
  objective calls per move; the lab caps evaluations to keep the comparison fair.
- **Unbounded restarts.** Restarting helps coverage but throws away all progress; without a
  stopping condition (evaluation cap or time) the process has no defined end.
- **Reading a restarted run's scatter as a single descent.** The lab notes the trail "has become a
  scatter of short, disconnected climbs".

## Connections

- [[fitness-landscape]] — the geometry hill climbing is blind to.
- [[tabu-search]] — accepts worsening moves and remembers where it has been: the direct repair.
- [[simulated-annealing]] — accepts worsening moves with a controlled probability instead of
  remembering.
- [[evolutionary-algorithm]] — replaces one trajectory with a population, so several basins are
  explored in parallel.
- [[search-algorithm-evaluation]] — hill climbing is the standard baseline a new technique is
  tested against, after random search.
- [[metaheuristics]] — the general properties it inherits (no guarantees, parameters, stopping
  condition).

## Open Questions

- **Which point to return** (last vs best along the trajectory) is never resolved by the slides,
  although it changes reported results.
- **No restart policy is given** — how many restarts, when to stop, and whether to keep the best
  across restarts are all left to the implementer. The lab uses an evaluation cap.
- **The probabilistic variant's normalisation assumes positive fitness** and the slide says so
  without saying what to do when f can be negative.
- **"Repeated applications can give insights into the landscape"** is asserted; the material never
  says which statistics to collect from those repetitions.