---
title: "Search-Based Software Engineering — Lecture 3 Overview (Evolutionary Algorithms)"
tags: [topic, search-based-software-engineering, semester-2, evolutionary-computation]
course: "Search-Based Software Engineering"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[evolutionary-algorithm]]"]
---

## One-line Summary

The deck is a biology lecture — Lamarck, Darwin, Mendel, mutation, drift, memetics, and the
1975–1992 timeline of evolutionary computation — while the Jupyter lab is the actual course: the
(1+1) → (μ,λ) family of evolution strategies, a genetic algorithm with tournament selection, and a
measured comparison of all of them on One Max.

## Core Map

```
Lecture 3 — Evolutionary Algorithms (26 slides + 48-page lab)
│
├── Slides: what evolution is
│   ├── Lamarckism — heritability of acquired characteristics
│   ├── Darwinism — scarcity, variation, heritability, differential reproduction
│   │   └── evolutionary / selection pressure; peppered moth
│   ├── Mendelism — genes, alleles, chromosomes, genotype vs phenotype
│   │   ├── law of dominance · segregation · independent assortment
│   │   └── mutation (catastrophic / neutral / advantageous)
│   ├── genetic drift, fixation · Baldwin effect · memetics
│   └── history of evolutionary computation
│       1948 Turing · 1962 Bremermann · 1964 Rechenberg · 1965 Fogel et al.
│       1975 Holland · 1992 Koza
│
└── Lab: the algorithms on One Max (n = 100, budget 1000 evaluations)
    ├── general scheme — encoding, population, parent selection, recombination,
    │   mutation, survivor selection, termination
    ├── mutation of a bitstring: each bit flipped with probability 1/n
    ├── evolution strategies
    │   ├── (1+1)ES — parent vs mutant, accept if at least as good
    │   ├── (1+λ)ES · (1,λ)ES — plus vs comma survivor selection
    │   ├── (μ+λ)ES · (μ,λ)ES — truncation selection, comma preferred in practice
    │   └── (μ/2+λ)ES · (μ/2,λ)ES — plus recombination of two parents
    ├── genetic algorithm
    │   ├── generational, elitism 5 %, tournament selection k = 5,
    │   │   single-point crossover, P_xover = 0.7, population 20
    │   └── steady-state variant — replace the worst if offspring ≥ worst
    ├── One Max vs Leading Ones — neutrality, autocorrelation, expected wait
    └── comparison — 30 runs, common seeds, Mann-Whitney, Holm, Â12
            -> [[evolutionary-algorithm]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[evolutionary-algorithm]] | The scheme, the (μ/ρ ± λ) notation, mutation 1/n, the measured comparison |
| [[search-algorithm-evaluation]] | The statistics the lab uses to compare eight variants |
| [[fitness-landscape]] | Neutrality and autocorrelation — why Leading Ones is hard |
| [[metaheuristics]] | The class properties |
| [[sbse-paradigm]] | Where genetic improvement, neuroevolution and FunSearch sit |

## Lecture Structure

**Slides (26 pages, `4_EvolutionaryAlgorithms_Part1.pdf`):**

1. **What is evolution?** — Lamarck and Lamarckism; Darwin and the five facts plus three
   inferences of natural selection; the peppered moth; evolutionary pressure.
2. **Mendel and genetics** — heredity units; genes, alleles, chromosomes, genome, genotype,
   phenotype; the three laws (dominance, segregation, independent assortment); de Vries and
   mutation, with the three outcomes (catastrophic, neutral, advantageous); the Baldwin effect;
   Lyssenkoism; Sewall Wright and genetic drift; Dawkins and memetics.
3. **History** — the six dated contributions from Turing 1948 to Koza 1992.
4. The deck stops there; "Evolutionary Algorithms" is announced in its contents list but the
   algorithm slides are not in Part 1.

**Lab (`4_EvolutionaryAlgorithms_Jupyter_Part1`, 48 pages):**

1. The general scheme of an evolutionary algorithm, and the three design steps (representation,
   variation operators, selection operators).
2. Evolution strategies: mutation with p = 1/n per gene; (1+1)ES implemented and plotted; the
   μ/λ/ρ notation derived step by step through (1+λ), (1,λ), (μ+λ), (μ,λ), (μ/2+λ), (μ/2,λ).
3. Genetic algorithm: the difference from ES (genotype-level operation, fitness-based parent
   selection), tournament selection, elitism, single-point crossover, the parameter table.
4. Steady-state GA and its replacement rule.
5. Comparison across 30 runs with common seeds, significance tests and effect sizes.
6. One Max vs Leading Ones: neighbour counts, neutrality, autocorrelation, expected waiting time.

## Exam-Relevant Points

1. **The general scheme's seven decisions** are the examinable skeleton: encoding, population,
   parent selection, recombination, mutation, survivor selection, termination.
2. **The (μ/ρ ± λ) notation decodes in one sentence**: μ parents, ρ participants in recombination,
   λ offspring, `+` keeps parents eligible as survivors, `,` does not.
3. **Mutation rate for bitstrings is 1/n per gene**, "on average one element", with the stated
   trade-off between exploration (too small) and exploitation (too large).
4. **Evolution strategies vs genetic algorithms differ in where selective pressure is applied** —
   ES: random parents plus truncation survivor selection; GA: fitness-based probabilistic parent
   selection (tournament) plus elitism.
5. **Comma selection is preferred in practice**, "because it is better at leaving local optima as
   well as following moving optima" — and its price is that the current population can be worse
   than the best seen, so the reported result is the best evaluated candidate.
6. **Elitism, tournament selection and P_xover are parameters with the lab's values** (20, 5,
   0.7, elite 5 %), described as "common default values" without a source.
7. **Neutrality is not the same as unimodality**: Leading Ones has one local optimum and 89 of 100
   neighbours neutral at fitness 10, so its expected improvement wait is 100–270 evaluations where
   One Max offers 90 improving moves.
8. **The measured verdict on One Max**: (1+1)ES and (μ/2+μ)ES beat the GA (Â12 ≈ 0.95 and 0.85),
   and the two ES variants are indistinguishable — "no evidence of a difference" is not the same
   as "the same".

## Connections

- [[search-based-software-engineering-lecture-2]] — local search, and the evaluation procedure the
  lab reuses verbatim (`run_all`, common seeds, 30 runs).
- [[search-based-software-engineering-lecture-1]] — the representation/operators/fitness triad that
  the EA scheme formalises.
- [[evolutionary-algorithm]] — the concept page for this material.
- [[hill-climbing]] — (1+1)ES is a stochastic hill climber with equal-fitness acceptance.
- [[search-based-software-engineering-lecture-0]] — assignment A1 pairs simulated annealing with an
  evolutionary algorithm, and A2 uses NSGA-II (multi-objective, a later lecture).

## Open Questions

- **The slides never define an evolutionary algorithm.** Everything operational is in the notebook,
  so a student revising from slides alone has biology and a timeline. This is a real gap, not a
  summary shortcut.
- **Where Part 2 is**: the deck is named `Part1` and ends mid-topic (contents list "What is
  Evolution? / History / Evolutionary Algorithms"); no Part 2 file is in `raw/`.
- **Parameter provenance is missing** — population size 20, elite 5 %, P_xover 0.7 and tournament
  size 5 are "common default values", and the tuning chapter is future.
- **The "Neatest" name in assignment A3** ("Testing Games with Neatest") does not appear in this
  lecture's material, so the connection between the neuroevolution assignment and this deck is
  asserted only by the schedule.
- **Selection-pressure strength is not quantified** for tournament size 5 or for elitism at 5 %;
  the lab varies neither.
- **The comparison is one instance and one configuration**, which the lab states explicitly as a
  limitation rather than a result.