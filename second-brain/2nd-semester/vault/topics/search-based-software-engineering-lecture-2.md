---
title: "Search-Based Software Engineering — Lecture 2 Overview (Local Search Algorithms)"
tags: [topic, search-based-software-engineering, semester-2, local-search]
course: "Search-Based Software Engineering"
source_count: 3
status: current
last_updated: 2026-11-07
prerequisites: ["[[fitness-landscape]]"]
---

## One-line Summary

Three local-search algorithms on one template — hill climbing (always uphill), tabu search (always
best non-forbidden), simulated annealing (uphill with probability e^(−ΔE/T)) — followed by the half
of the lecture that matters most for the assignments: how to compare randomised algorithms
honestly.

## Core Map

```
Lecture 2 — Local Search (55 slides) + two Jupyter labs
│
├── The template (restated from lecture 1)
│   ├── search space S and objective f : S → R
│   ├── neighbourhood V(x), move operators Tᵢ
│   ├── exploration operator U
│   └── trajectory x₀ → x₁ → … until a stopping criterion
│
├── Hill climbing — U = best neighbour
│   ├── 8-queens, h = number of attacks; local optimum with fitness 1
│   ├── variants: first ascent · accept equal fitness · probabilistic
│   ├── restart when stuck
│   └── pros (cheap) / cons (cannot escape)          -> [[hill-climbing]]
│
├── Tabu search — best non-tabu neighbour, even if worse
│   ├── tabu list (circular buffer), tenure k, moves/attributes not solutions
│   ├── 20×20 grid instance: random walk vs tabu size 4 vs size 10
│   └── independent of the current solution's fitness  -> [[tabu-search]]
│
├── Simulated annealing — accept worse with p = min(1, e^(−ΔE/T))
│   ├── ΔE = E_new − E_current; T₀ from 100 probe moves and a chosen p₀
│   ├── equilibrium 12N accepted of 100N tried; T(k+1) = 0.9·T(k)
│   ├── stop after three stages without improvement
│   └── metallurgy: annealing vs quenching          -> [[simulated-annealing]]
│
└── Evaluating search algorithms
    ├── one run is not a result — distributions, not numbers
    ├── H₀ "no difference"; Type I / Type II; p-value; α = 0.05
    ├── two-tailed by default; parametric vs non-parametric (Mann-Whitney U)
    ├── n ≥ 30 rule of thumb; one-sample Wilcoxon against a deterministic baseline
    ├── effect size: d family · Vargha-Delaney Â12 · odds ratio ψ; bootstrap CIs
    └── lab: Holm correction, common seeds, 30 runs
            -> [[search-algorithm-evaluation]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[hill-climbing]] | Monotone improvement; the local optimum is indistinguishable from the global one |
| [[tabu-search]] | Best non-tabu neighbour plus a short-term memory of recent moves |
| [[simulated-annealing]] | Temperature-controlled acceptance, cooled on a schedule |
| [[search-algorithm-evaluation]] | Significance + effect size + correction, or the comparison is anecdote |
| [[fitness-landscape]] | The geometry that makes all three necessary |
| [[metaheuristics]] | The class properties (no guarantees, parameters, stopping condition) |

## Lecture Structure

1. **The local-search template** — repeated verbatim from lecture 1, so that the three algorithms
   can be read as three choices of U.
2. **Hill climbing** — five-step picture sequence, the Everest-in-fog aphorism, the 8-queens
   instance, the local-optimum board, restart, and the four variants of U; then the ascent-strategy
   discussion and the pros/cons slide.
3. **Tabu search** — Glover 1986, the selection rule, the tabu list as circular buffer, attributes
   versus solutions, banning time / tenure, and the 2-D grid instance with three trajectories.
4. **Simulated annealing** — the metallurgy, the algorithm, the acceptance probability, cooling
   schedules, the T₀ heuristic, the equilibrium rule, the termination rule.
5. **Evaluating search algorithms** — why (one run is not a result), measurements, the n = 10
   Android example, statistical difference and H₀, Type I/II errors, one- vs two-tailed,
   parametric vs non-parametric, n = 30, deterministic baselines, effect sizes (d, Â12, odds
   ratio), confidence intervals, and the Arcuri & Briand reading.
6. **The two Jupyter labs** — `2_LocalSearch_Jupyter_Part1` (landscape visualisation, n-queens
   slice, hill climbing, restarts, first vs steepest ascent) and `3_LocalSearch_Jupyter_Part2`
   (first ascent, the statistical comparison in code, Holm correction, parameter sensitivity).

## Exam-Relevant Points

1. **The three algorithms differ only in the acceptance rule and in what they remember** — that is
   the comparison table to be able to write: best neighbour / best non-tabu neighbour even if worse
   / random neighbour accepted with probability e^(−ΔE/T).
2. **Hill climbing is monotone, therefore it cannot escape a local optimum**; restart is the only
   remedy inside the algorithm, and it discards everything learned.
3. **Tabu selection is independent of f(xₙ)** — a subtle sentence that is easy to get wrong in an
   exam answer; the move is chosen by comparing neighbours, not by comparing to the current point.
4. **The annealing acceptance rule and its limits** — p = min(1, e^(−(ΔE/T))); ΔE < 0 always
   accepts; T → 0 reproduces hill climbing; T is computed from ⟨ΔE⟩ over 100 probe moves, not
   guessed.
5. **The schedule constants** — 12N accepted out of 100N tried defines equilibrium; T(k+1) = 0.9T(k);
   three stages without improvement terminates. These are the numbers the deck supplies.
6. **A p-value is the probability of a Type I error**, and the significance level is the largest
   p-value one accepts; α = 0.05 is conventional and "much debated".
7. **Two-tailed tests are the default in software engineering**, with the coin-carat example as the
   exception that shows when one-tailed is legitimate.
8. **The t-test's assumptions are not met** for these measures; the Mann-Whitney U / Wilcoxon
   rank-sum test is the non-parametric replacement.
9. **Significance ≠ importance**: with large n, trivial differences become significant, so an
   effect size (Â12, d, odds ratio) and a confidence interval are required.
10. **Â12 has a computable definition** — "the probability that running A yields higher M than
    running B", 0.5 for equivalence, computed from a rank sum as (R₁/m − (m+1)/2)/n.

## Connections

- [[search-based-software-engineering-lecture-1]] — the template and the landscape vocabulary this
  lecture reuses.
- [[search-based-software-engineering-lecture-3]] — the population-based successor, which inherits
  the whole evaluation apparatus.
- [[search-based-software-engineering-lecture-0]] — assignment A1 asks for exactly simulated
  annealing and an evolutionary algorithm, i.e. this lecture's third algorithm and the next
  lecture's.
- [[fitness-landscape]] — the n-queens slice picture is the lecture's own landscape exhibit.
- [[search-algorithm-evaluation]] — this lecture's second half, extracted.
- [[msr-statistical-methods]] — the semester's other statistics lecture; same tests, different
  subject matter.
- [[statistical-significance]], [[effect-sizes]], [[confidence-intervals]] — the Semester 1
  foundations reused here.

## Open Questions

- **`3_LocalSearch_Part2.pdf` is not new material**: its 19 pages are the statistics half of
  `2_LocalSearch.pdf` (slides 20 onward of the same deck) reproduced without the figures refined.
  It is ingested as part of this page rather than as a separate lecture.
- **The lab's schedule is not the slide's schedule.** The notebook chooses "all parameters in this
  chapter by guesswork" and defers to a later chapter on parameter tuning; the deck presents
  0.9 decay and 12N/100N as if they were the method.
- **The lecture gives no worked numerical example of a full annealing run** — only the acceptance
  formula and the calibration procedure; the lab runs a schedule but does not print a trace.
- **Holm correction is used in the lab and absent from the slides**, so "the course's method" for
  multiple comparisons is only in the notebook.
- **Whether the assignments expect these evaluation methods** (as opposed to just a working
  algorithm) is not stated in either the deck or the organisational slides.