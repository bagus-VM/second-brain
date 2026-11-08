---
title: "Search-Based Software Engineering — Lecture 1 Overview (Introduction, Search Spaces and Fitness Landscapes)"
tags: [topic, search-based-software-engineering, semester-2, foundations]
course: "Search-Based Software Engineering"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: []
---

## One-line Summary

The first content lecture builds the whole frame: optimisation problems and why they are hard,
metaheuristics as smart trial and error, SBSE as metaheuristics aimed at software-engineering
problems, and search spaces and fitness landscapes as the geometry that decides how hard the
search will be.

## Core Map

```
Lecture 1 — Introduction (88 slides)
│
├── Motivating frame — what engineering disciplines do
│   ├── Theory (stress, tensile strength) · Simulation · Optimisation
│   ├── Software engineering's grid has "?" in the simulation/optimisation cells
│   └── "It is, simply, trial and error" — possible once simulation exists
│
├── Solving optimisation problems
│   ├── Decision problems — P, NP, NP-complete, NP-hard
│   │   ├── Connectivity — O(|V|+|E|) by BFS
│   │   └── Hamiltonian cycle — no polynomial algorithm known, easy to check
│   ├── Optimisation problem — feasible set S, f : S → R, x* maximising f
│   │   └── TSP — "at least as hard" as the Hamiltonian decision problem
│   ├── Escape routes and why they fail
│   │   ├── special cases (2-SAT, simplex in practice)
│   │   ├── brute force (hardware growth)
│   │   └── parallelism (not all algorithms parallelise)
│   └── Metaheuristics — "smart trial and error"
│       ├── no assumptions on f, few parameters, random start, stopping condition
│       ├── exploitation vs exploration
│       ├── random search — the mandatory sanity check (1/|S|)
│       └── Super Mario: Player A plans, Player B dies intelligently
│               -> [[metaheuristics]]
│
├── Search-Based Software Engineering
│   ├── "apply optimisation techniques to SE problems (NOT search engines or code search)"
│   ├── origin: Miller & Spooner 1976, floating-point test data by numerical maximisation
│   ├── domains: structural testing, SBST (Daimler parking), requirements (next release),
│   │   project planning, design/refactoring (clustering), genetic improvement,
│   │   code transplantation, FunSearch, AlphaEvolve
│   └── key ingredients: representation · operators · fitness · constraints
│           -> [[sbse-paradigm]]
│
├── Course organisation
│   ├── tentative schedule (13.10 → 02.02), slides + Jupyter notebooks
│   ├── four assignments, Java, individual work
│   └── registration 12.10.2026 – 03.11.2026, first exercise 20.10.
│
└── Search spaces and fitness landscapes
    ├── search space S, |S|, degrees of freedom, continuous vs combinatorial
    ├── neighbourhood V(x) and move operators Tᵢ
    ├── landscape: S + fitness + neighbourhood
    ├── shapes: single-peak · local optimum · rugged · plateau · needle
    ├── needle repair: predicate → distance (f₁ vs f₂)
    └── artificial example: x + y = 10, f = |10 − (x+y)|
            -> [[fitness-landscape]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[metaheuristics]] | Approximation without guarantees; the six properties; random search as baseline |
| [[sbse-paradigm]] | Optimisation applied to SE problems, and the domains it covers |
| [[fitness-landscape]] | Search space + fitness + neighbourhood; shape predicts difficulty |
| [[hill-climbing]] | Introduced here as the local-search template, developed in lecture 2 |
| [[search-algorithm-evaluation]] | Signposted by the "1/|S|" probability argument; delivered in lecture 2 |

## Lecture Structure

1. **The engineering frame** — Dijkstra's "The Humble Programmer" (1972) epigraph; the 1968 NATO
   conference's conclusion that software engineering should adopt established engineering
   philosophies; theory / simulation / optimisation illustrated with a steel beam, a truss
   simulation, and Smith, Hodgins, Oppenheim & Witkin's optimisation of truss structures (2002).
2. **Software "Engineering"** — the grid with "?" cells, and the unresolved question mark over the
   whole paradigm.
3. **Complexity theory** — decision problems, P, NP, the connectivity example, the Hamiltonian
   cycle example, then the formal optimisation-problem statement and TSP.
4. **How to solve optimisation problems** — special cases, brute force, parallelism, and then
   metaheuristics as the fourth option.
5. **Super Mario** — Aloupis et al., "Classic Nintendo Games are (Computationally) Hard" (2015);
   Player A vs Player B; the three key ingredients; two representations of the same game.
6. **What SBSE is** — the definition, the SEBASE repository, Miller & Spooner 1976, then the domain
   tour: structural testing, Daimler's parking system, next release problem, project planning,
   design/refactoring, genetic improvement, code transplantation, FunSearch, AlphaEvolve.
7. **Course organisation** — the tentative week-by-week schedule, slides and Jupyter notebooks,
   grading, assignment releases, registration window, and the three recommended books.
8. **Search spaces and fitness landscapes** — definitions, the artificial x + y = 10 example, the
   five landscape shapes, the needle-in-a-haystack repair, the metaheuristic property list, random
   search, Max One as the coding example, and the local-search template.

## Exam-Relevant Points

1. **The distinction decision problem vs optimisation problem is stated precisely** and is the
   course's opening formalism: a decision problem asks yes/no, an optimisation problem asks for
   x ∈ S maximising f, subject to feasibility.
2. **The four failed escape routes** (special cases, brute force, parallelism, and "just be smart")
   are the argument for metaheuristics — and the exam-relevant phrasing is "no formal guarantees
   about the quality of solutions or global optimality".
3. **The six properties of metaheuristics** are a list to reproduce: no hypothesis on f, unknown
   optimal parameters, random start, stopping condition, easy to implement and parallelisable,
   exploitation vs exploration.
4. **Random search is the baseline, with a reason**: probability 1/|S| of hitting the optimum, and
   "if it does not do better than random search, you are doing something wrong".
5. **SBSE's definition carries its own negation** ("NOT search engines or code search") and its
   founding citation (Miller & Spooner, TSE 1976).
6. **The three key ingredients plus constraints** — representation, operators, fitness, constraints
   — are the answer template for every later domain example.
7. **Landscape shapes and their consequences** are a table to reproduce: single-peak (easy), local
   optimum (stops early), rugged (hard), plateau (no guidance), needle (worst).
8. **The needle repair is the pedagogically important one**: a predicate fitness gives no gradient,
   a distance does (f₁ = (x==15 && y==15) ? 0 : 10 versus f₂ = |x−15| + |y−15|).
9. **The local-search template's four steps** (search space and objective, neighbourhood, operator
   U, trajectory until a stopping criterion) are the definition every later algorithm instantiates.

## Connections

- [[search-based-software-engineering-lecture-0]] — the logistics this lecture summarises again
  (with a different assignment-3 date).
- [[search-based-software-engineering-lecture-2]] — local search in full: hill climbing, tabu,
  annealing, evaluation.
- [[search-based-software-engineering-lecture-3]] — evolutionary algorithms.
- [[metaheuristics]], [[fitness-landscape]], [[sbse-paradigm]] — the three pages this lecture
  creates.
- [[hill-climbing]] — the Daimler example is fitness-guided search over a physical parameter space,
  the same idea as gradient-free hill climbing.
- [[mining-software-repositories]] — the other course in the semester that treats software
  artifacts as data; MSR measures, SBSE optimises.
- Genetic improvement has no page of its own — it appears only as a domain on this lecture's slide;
  see [[sbse-paradigm]].

## Open Questions

- **The recommended literature is listed but never cited in the text**: Chopard & Tomassini,
  *An Introduction to Metaheuristics for Optimization*; Eiben & Smith, *Introduction to
  Evolutionary Computing*; Poli, Langdon & McPhee, *A Field Guide to Genetic Programming* (free
  online). Whether any of them is examinable is not stated.
- **The course's own "tentative schedule" and the assignment dates in the organisational deck
  disagree for assignment 3** (15.12 vs 22.12), and the lecture repeats both.
- **"AlphaEvolve" appears on a slide with no citation, date or description**, unlike FunSearch.
- **The claim that software engineering lacks a simulation column** is left as a rhetorical
  contrast; test execution and program analysis — the things SBSE actually uses — are not
  acknowledged as simulation.
- **No worked example of a full SBSE problem** (representation → operators → fitness → result) is
  given in this lecture; the domains are each one slide.
- **The slide's "1/|S|" for random search assumes a uniform draw over the whole space with
  replacement**, which is not stated.