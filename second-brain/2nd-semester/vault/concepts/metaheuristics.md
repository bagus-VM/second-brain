---
title: "Metaheuristics"
tags: [concept, search-based-software-engineering, semester-2, optimisation]
course: "Search-Based Software Engineering"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["basic complexity theory (P, NP, NP-hard)", "the idea of an objective function and a feasible set"]
---

## One-line Summary

A metaheuristic is an approximation algorithm that gives a good answer in acceptable time
without any guarantee of optimality: it makes no assumption about the objective function beyond
"f(x) can be computed", and it works by smart trial and error.

## Core Intuition

The course opens by asking what engineering disciplines actually do to improve quality, and
answers with three things: theory, simulation, optimisation. A steel beam can be analysed
(stress, tensile strength), a structure can be simulated, and once a simulation exists,
optimisation follows "naturally. It is, simply, trial and error, which is only possible because we
have the simulation environment."

Software engineering is the third column that is missing those instruments. The slide's grid puts
theory, simulation and optimisation against product for bridges, and against software it can only
write "?" in the simulation and optimisation cells. Metaheuristics are the course's answer to
filling the optimisation cell: you cannot solve the program analytically, but you can *evaluate*
a candidate program, and evaluation is all a metaheuristic needs.

The second intuition is the Super Mario comparison, which is the cleanest statement of what
metaheuristic search is. Player A plays properly: read the manual, study the map, plan every
button press, then execute the plan. Player B grabs the controller, plays, dies, repeats until
the level is cleared — and "intelligence lies in how differently you die next time." Player B is
a metaheuristic. The three ingredients of that intelligence are the ones the course then names:
what you try this time (representation), how it differs from what you tried before (operators),
and how well it went (fitness).

## Formal Definition / Statement

The slide's definition, in its own words: metaheuristics are "approximation algorithms that
provide good or acceptable solutions within an acceptable computing time", with "no formal
guarantees about the quality of solutions or global optimality", "usually non-deterministic",
"not problem specific", and "smart trial and error".

The vocabulary the definition needs first:

- **Decision problem** — a problem that requires a yes/no answer. For P, the instances can be
  partitioned into positive and negative sets, and an algorithm solves P if it answers correctly
  for all of them. For NP, a "yes" answer can be *checked* in polynomial time.
- **Optimisation problem** — "finding a solution that maximises (or minimises) a given criterion
  called objective function"; a solution "may be required to obey certain constraints to be
  feasible (admissible)". Formally, let S be a finite set of feasible solutions and f a cost
  function f : S → R; an instance asks for x ∈ S such that f(x) ≥ f(s) for all s ∈ S.
- The lecture's two examples make the gap concrete: connectivity is solvable in O(|V| + |E|) by
  breadth-first search, while the Hamiltonian-cycle decision problem has no known polynomial
  algorithm although a proposed path is easy to check. The Travelling Salesman Problem is the
  optimisation version and is "at least as hard".

**The properties the slide attributes to metaheuristics**, which double as the exam list:

1. No hypothesis on the mathematical properties of the objective function — "The only
   requirement is that f(x) can be computed for all x ∈ S" (no continuity, no differentiability).
2. They have few parameters that influence solution quality and convergence speed, "but the
   optimal values of the parameters are generally unknown".
3. A starting point must be specified, "usually the initial solution is chosen randomly".
4. A stopping condition must be built in, "usually based on CPU time or number of evaluations".
5. They are "generally easy to implement and can usually be parallelised efficiently".
6. They balance **exploitation** — "explores the neighbourhood of an already promising solution" —
   against **exploration** — "tries to visit regions of the search space not already seen".

## Key Properties

**Why not just solve the problem?** The lecture lists the escape routes and closes them: special
cases help only sometimes ("worst case scenario doesn't always appear in practice"; 2-SAT is
solvable; the simplex algorithm is exponential in theory "but usually is quick"); brute force
depends on "increase in computer power may allow enumerating all admissible solutions"; parallel
computing is limited because "not all algorithms are easily parallelisable".

**Random search is the baseline every method must beat.** Its definition is minimal: "Next point
in the search is chosen uniformly at random in the whole search space S; solution having the best
fitness is kept." Its failure probability is stated just as plainly — "probability of finding
global optimum is small, if S is large (1/|S|)" — and so is its role: "Random search should
always be the default sanity check against your own search methodology: if it does not do better
than random search, you are doing something wrong." It is also the right method when the problem
gives no guidance at all, e.g. "search for the input to program A that will result in a program
crash", because "given an arbitrary program, you cannot measure the distance between the current
program state and a crash".

**NP-hardness of the target domain is itself a research topic.** The lecture uses Aloupis,
Demaine, Guo and Viglietta, "Classic Nintendo Games are (Computationally) Hard" (2015) to show
that even Super Mario is NP-hard — i.e. the games that motivate neuroevolution and game testing
are not tractable either.

## Worked Example

**Max One**, the smallest illustration of a search problem: maximise f(x₁, …, xₙ) = Σ xᵢ, so the
obvious solution is x = (1, 1, …, 1). The lecture uses it as the first coding example and returns
it in the evolutionary-algorithms lab, where the search space is the n-bit string and the fitness
is simply the number of ones.

**Super Mario as a representation choice.** The same game, two representations, two different
searches over the same problem:

| | Search over inputs | Search over a neural network |
|---|---|---|
| Representation | a list of (button, start_time, end_time) tuples | a neural network |
| Operators | change the button type in one tuple; increase or decrease start_time / end_time | change the weights; change the network structure |
| Fitness | the distance travelled without dying | the distance travelled without dying |

The fitness function is identical; only the representation and the operators differ. That is the
point of the example — a metaheuristic is defined by those three ingredients, not by the problem.

## Common Pitfalls

- **Expecting a guarantee.** By definition there is none; the value of a technique is empirical,
  which is why the course spends a whole lecture on how to evaluate one.
- **Skipping random search.** Without the baseline you cannot claim your search method works.
- **Reporting a single run.** Randomised algorithms "usually produce different results" on the
  same instance; one run is an anecdote.
- **Tuning parameters by intuition and presenting it as result.** The lecture's own lab says of
  its parameters (tabu list size, cooling schedule, restarts, neighbourhood): "We chose all
  parameters in this chapter by guesswork; choosing them systematically is the topic of the
  chapter on parameter tuning and control."
- **Confusing the optimisation target with the data.** In machine-learning applications "x is
  (typically) the weights w! NOT the input data x" — the search runs over parameters, not over
  examples.
- **Assuming a hard problem needs a metaheuristic.** Check for the special case first; a
  polynomial algorithm beats a heuristic whenever one exists.

## Connections

- [[sbse-paradigm]] — the application of these techniques to software-engineering problems.
- [[fitness-landscape]] — the geometry a metaheuristic walks on, and why it decides difficulty.
- [[hill-climbing]], [[tabu-search]], [[simulated-annealing]], [[evolutionary-algorithm]] — the
  four algorithms the course builds.
- [[search-algorithm-evaluation]] — how to tell whether one metaheuristic beats another.
- [[gradient-descent-step-mechanics]] — the deterministic, differentiable cousin: same
  "step against the gradient" idea, but it requires a gradient.
- [[msr-statistical-methods]] — the same significance machinery reached from the repository-mining
  side of the semester.

## Open Questions

- **No bound on how bad a metaheuristic answer can be** is given anywhere in the slide set; the
  approximation ratio is not discussed at all, so "good or acceptable" stays undefined.
- **"Acceptable computing time" is not quantified** — the course never states a budget policy,
  only that a stopping condition must exist.
- **Whether parallelisation is actually exploited** by the algorithms presented is claimed as a
  property but never shown.
- **The lecture asserts software engineering lacks a simulation column** without discussing the
  counter-examples it later relies on (test execution, program analysis, profiling).