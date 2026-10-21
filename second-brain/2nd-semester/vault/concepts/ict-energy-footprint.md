---
title: "ICT Energy Footprint"
tags: [concept, energy-informatics, sustainability, semester-2]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
Computing consumes a measurable share of global energy, and the fastest-growing parts — cloud, AI, blockchain — are exactly the parts that were supposed to be "virtual" and therefore free.

## Core Intuition
Every byte moved and every FLOP executed is paid for in watts. The interesting part is not the total (a few percent of global demand) but the *shape* of the growth: efficiency per operation keeps improving while total consumption keeps rising, because new applications eat the savings. This is Jevons' paradox wearing a data-centre badge. Energy informatics exists partly because of this: computing is now a large enough load that it has to be managed like one.

## Formal Definition / Statement

**ICT share of demand:** information and communication technology accounted for **up to 3% of global energy demand in 2015** (Gupta 2022).

**Data-centre energy drivers** (Masanet 2022, relative change 2010→2018): workloads and compute instances grew ~6.5× and ~11×, while installed servers grew only ~1.3× and average server energy intensity fell to ~0.24 of the 2010 value. Storage energy per terabyte fell to ~0.11. Total data-centre energy rose far less than traffic — efficiency worked, but did not zero out growth.

**PUE (Power Usage Effectiveness):**

```
PUE = Total Energy / IT Equipment Energy
```

PUE = 1.0 is a perfect data centre (all power reaches IT equipment); real values are above 1 because of cooling and losses. PUE is a ratio, not a total — a low PUE on a huge facility can still be a large absolute load.

**Programming-language energy** (Pereira 2021, normalised to C = 1.00): Python 75.88× energy and 71.90× time; Java 6.01× memory but modest time; Rust energy ≈ 1.03× C but 1.54× memory. There is **no single best language** across energy, time, and memory simultaneously — the choice is a trade-off, not an optimisation.

**Machine-learning development phases** (Wu 2022, Meta): *experimentation* (exploration of models/algorithms/training methods), *training* (evaluation on larger datasets), *inference* (best model deployed). Experimentation and inference dominate in practice, not just training. Training one large model can emit as much carbon as **~400,000 km driven by an average passenger car**. Meta's recommendation model sizes grew **20×** from 2019 to 2021. Optimising algorithms, software, hardware, and infrastructure together can cut operational carbon by up to **810×**.

**Blockchain consensus** (Platt 2021, De Vries 2018): proof-of-work is energy-hungry by design — **10^18 hash calculations per transaction** in March 2018. Proof-of-stake replaces hashing with validator voting and reduces consumption by **at least three orders of magnitude**. Ethereum's Merge on **15.09.2022** cut its energy use by **99.95%**.

## Key Properties

- **ICT's share of global energy demand was up to 3% in 2015** — a floor, not a ceiling, and a moving target as workloads change.
- **Efficiency and consumption move independently.** Data-centre workloads grew ~11x from 2010 to 2018 while total energy grew far less; the gap is efficiency, not restraint.
- **PUE ≥ 1 by construction.** It is a ratio of total to IT energy, so it measures overhead, not usefulness. A facility can be efficient and wasteful at the same time.
- **The ML cost profile is dominated by experimentation and inference**, not only training — the part that is easiest to overlook because it is spread across many small runs.
- **Consensus mechanism is a design choice with an energy consequence of orders of magnitude**, not a percentage point.
- **Language choice trades three quantities against each other** (energy, time, memory). Optimising one reliably costs another.

## Worked Example — why "just make it efficient" is not enough

Take a data centre with PUE 1.3 and IT load of 1 MW. Total draw = 1.3 MW; 0.3 MW is overhead. Halve the IT load through better software and total draw is 0.65 MW — a real 50% saving. Now double the workload at the same efficiency and you are back at 1.3 MW with twice the useful output. Efficiency gains buy headroom; they do not cap demand. That is why the lecture pairs efficiency with *demand-side* measures ([[demand-side-integration]]) rather than treating efficiency as a solution.

## Common Pitfalls

- **Confusing PUE with efficiency of computation.** PUE says nothing about whether the FLOPs were useful.
- **Quoting a single number as "the" ICT footprint.** Estimates vary by boundary: data centres only, or including networks and end-user devices.
- **Assuming training dominates ML energy.** The lecture's data puts experimentation and inference on the same chart for a reason.
- **Assuming PoS is "free".** It is orders of magnitude cheaper, not zero.
- **Reading language benchmarks as universal.** Pereira's numbers are task-dependent; Python being 75× C on one benchmark does not generalise to every workload.

## Connections

- [[power-grid-fundamentals]] — the load ICT puts on the grid is the reason energy informatics studies the grid at all.
- [[demand-side-integration]] — efficiency alone does not balance supply and demand; shifting load does.
- [[sector-coupling]] — data-centre waste heat is a sector-coupling opportunity (the RENergetic project).
- [[paris-agreement-climate-goals]] — the policy frame that makes any of these numbers matter.

## Open Questions

- The 3% figure is from 2015. What is the current estimate, and how much of the growth since then is AI training specifically? The slides cite 2022 sources but not a current total.
- How should PUE be interpreted for colocated HPC in wind parks (the ESN4NW project), where the "data centre" is not a building?
