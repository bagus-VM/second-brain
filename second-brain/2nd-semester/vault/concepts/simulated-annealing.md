---
title: "Simulated Annealing"
tags: [concept, search-based-software-engineering, semester-2, local-search]
course: "Search-Based Software Engineering"
source_count: 3
status: current
last_updated: 2026-11-07
prerequisites: ["[[hill-climbing]]", "the exponential function and logarithms"]
---

## One-line Summary

Simulated annealing accepts worsening moves with probability p = min(1, e^(−ΔE/T)) and lowers T
over time, so the search roams early and behaves like hill climbing late — the physical analogy is
cooling metal into a low-energy crystal.

## Core Intuition

The metallurgy is not decoration; it explains the schedule. "In heated metal atoms undergo
disordered movements of large amplitude. Cooling the metal down progressively reduces movement and
stabilises atoms around fixed positions in a regular crystal structure with minimal energy." Heat
= freedom to move anywhere; slow cooling = the system finds a low-energy arrangement on the way
down. The contrast case is given too: "Quenching, rapidly cooling down metal … causes metal to be
more fragile, but also harder and more resistant to wear and vibration" — cool too fast and you
freeze the structure wherever it happened to be.

So the algorithm is hill climbing with a temperature-controlled willingness to go downhill, and
the temperature is what buys escape from local optima. There is no memory and no population: the
whole mechanism is the acceptance probability.

## Formal Definition / Statement

From the slide, in order:

- "Algorithm searches for the minimum of a given objective function, called energy E."
- "Initialised with arbitrary admissible solution" and an "initial temperature".
- "Elementary transformations: algorithm does not test all neighbours, but selects a random move
  among the allowed ones."
- "If the move leads to a lower energy value, then the new configuration is accepted and becomes
  the current solution."
- "Even moves that lead to an increase of the energy can be accepted with positive probability."
- "The probability of accepting solutions that worsen the fitness are computed from the energy
  variation ΔE before and after the given move: ΔE = E_new − E_current."

**Acceptance rule.** "The probability p of accepting the new configuration is defined by the
exponential p = min(1, e^(−(ΔE/T)))." Three consequences worth reading off it directly: ΔE < 0
always accepts (the min clamps to 1); ΔE > 0 accepts with probability e^(−ΔE/T); a larger T makes
worse moves more likely, a smaller T makes them rarer, and as T → 0 the rule converges to hill
climbing.

**Cooling schedule.** "The temperature is progressively decreased during the search. Temperature
schedule / cooling schedule. Often preferred to lower the temperature in stages: first constant
temperature for a while, until the search reaches a stationary value of the energy that fluctuates
around a given average value that doesn't change any more; at this point the temperature is
decreased to allow the system to achieve convergence to a lower energy state; finally, after
several stages in which the temperature has been decreased, there are no possible fitness
improvements; a state is reached that is to be considered the final one, and the algorithm stops."

**Initial temperature heuristic.** "Perform 100 elementary transformations randomly starting from
the initial configuration; compute ⟨ΔE⟩, i.e., the average of the energy variations observed in
these 100 moves; choose an initial acceptance probability p₀ for worsening moves according to the
assumed quality of the initial solution. Typically, p₀ = 0.5 if the quality is assumed to be
average, and p₀ = 0.2 if it is assumed to be good. After that, T₀ can be computed such that
exp(−(⟨ΔE⟩/T)) = p₀, which means that the temperature is high enough to allow the system to
traverse energy barriers of size ⟨ΔE⟩ with probability p₀."

Inverting that equation gives T₀ = −⟨ΔE⟩ / ln p₀, which is the form to memorise for a calculation:
p₀ = 0.5 → T₀ = 1.4427·⟨ΔE⟩; p₀ = 0.2 → T₀ = 0.6213·⟨ΔE⟩ (computed, not copied).

**Equilibrium and decay.** "Equilibrium state is reached if 12N elementary transformations have
been accepted over a total quantity of 100N tried moves. (N is the number of degrees of freedom of
the problem, i.e., the number of variables that define the solution.)" The schedule then "goes to
another temperature stage by decreasing T according to a geometric law: T(k+1) = 0.9·T(k), where k
= is the stage number."

**Termination.** "If during the last three successive temperature stages the energy E didn't
improve then the process is halted."

## Key Properties

**Every parameter of the schedule is a number you can compute from the other numbers.** ⟨ΔE⟩ from
100 probe moves → T₀ from the chosen p₀ → the 12N/100N equilibrium rule decides when to drop T →
0.9 geometric decay decides by how much → three stages without improvement decides when to stop.
This is the most completely specified algorithm in the lecture; hill climbing and tabu search are
left much looser.

**The neighbourhood is sampled, not enumerated.** "The algorithm does not test all neighbours, but
selects a random move among the allowed ones." That is one fitness evaluation per iteration
instead of |V(x)|, and it is why simulated annealing scales to large neighbourhoods where
steepest-ascent hill climbing does not.

**Hot is not free.** The lab measures it: on the 12-queens problem a deliberately hotter schedule
"is significantly worse: our schedule ends higher in four out of five pairings of runs
(A12 = 0.80)". The notebook's explanation is the landscape argument — "The slice has only 900
solutions, so wandering around at a high temperature soon covers most of it. The 12-queens
problem has 1212, almost 9 × 10¹², solutions, and wandering through these is not much better than
a random walk." And the honest caveat: "A slice shows us what a parameter does, but not which
value is best for the real problem."

**On n-queens it is statistically indistinguishable from tabu search.** Holm-corrected
Mann-Whitney over 30 runs: "Tabu Search vs Simulated Annealing p = 0.5", with the A12 bootstrap
interval for that pair including 0.5 — "the data are compatible with either algorithm being
somewhat ahead."

## Worked Example

**The acceptance rule, evaluated by hand.** Suppose ⟨ΔE⟩ = 1 after the 100 probe moves and the
initial solution is assumed average, so p₀ = 0.5. Then T₀ = −1/ln(0.5) = 1.4427. At that
temperature:

| Move | ΔE | e^(−ΔE/T₀) | Accepted? |
|---|---|---|---|
| improves | −0.5 | e^(+0.347) = 1.41 → clamped to 1 | always |
| average worsening | +1.0 | e^(−0.693) = 0.500 | 50 % of the time |
| large worsening | +3.0 | e^(−2.079) = 0.125 | 12.5 % of the time |

After the first cooling step (T = 0.9·T₀ = 1.2984) the +1.0 move is accepted with
e^(−0.770) = 0.463, and after ten steps (T = 0.9¹⁰·T₀ = 0.5024) with e^(−1.990) = 0.137. That is
the whole "annealing" behaviour in one table: the same worsening move becomes progressively less
likely, and at T → 0 it becomes impossible.

**The lab's own annealing run** uses a different, hand-chosen schedule and reports its outcome in
the same Holm-corrected table as the other three algorithms, where it beats random search and hill
climbing (p = 1.5e-12 and 4.3e-09) and ties tabu search (p = 0.5).

## Common Pitfalls

- **Sign confusion.** ΔE = E_new − E_current, so an *improvement* is negative and always accepted;
  T appears in the denominator, so a large T means "accept almost anything".
- **Cooling from a temperature that was never calibrated.** Skipping the 100-probe estimate means
  p₀ is unknown and the schedule's early behaviour is arbitrary.
- **Cooling too fast (quenching).** The metallurgy analogy is the warning: you freeze wherever you
  are.
- **Cooling too slowly or too hot.** The measured 12-queens result shows a hotter schedule losing
  significantly; the cost is search time spent diffusing.
- **Treating "12N accepted out of 100N tried" as a per-iteration check.** It is an equilibrium
  criterion for a temperature stage, and N is the number of variables, not the number of
  neighbours.
- **Assuming it beats tabu search.** In this course's own experiment it does not.
- **Forgetting that acceptance is probabilistic** — a single run is not reproducible, which is
  precisely why the same lecture ends with statistical evaluation.

## Connections

- [[hill-climbing]] — the T → 0 limit; the monotone special case.
- [[tabu-search]] — memory instead of temperature; the lab cannot separate them on n-queens.
- [[fitness-landscape]] — energy barriers are what the temperature is calibrated against.
- [[search-algorithm-evaluation]] — the machinery behind the p-values and A12 figures quoted here.
- [[metaheuristics]] — the general properties; this is the most parameterised member.
- [[search-based-software-engineering-lecture-2]] — the lecture that presents it.

## Open Questions

- **The 12N/100N equilibrium rule's constant is asserted without derivation**; the slide gives no
  source for 12 and 100.
- **0.9 geometric decay likewise has no justification** in the material, and no guidance on
  adapting it per problem.
- **"The last three successive temperature stages" is a heuristic, not a proof of convergence**,
  and the slide presents it without qualification.
- **Whether the ⟨ΔE⟩ estimate should come from the initial solution only** is implied but not
  stated; a bad initial solution would bias the temperature.
- **The lab's schedule differs from the slide's recipe**, and the material does not reconcile the
  two, so "the course's own parameters" is ambiguous.