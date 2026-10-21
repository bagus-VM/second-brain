---
title: "Energy Informatics I — Lecture 0 Overview (Motivation and Basics)"
tags: [topic, energy-informatics, semester-2, motivation]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
Lecture 0 sets up the whole course: computing is a large and growing energy load, the electrical grid
is a real-time balancing act with hard physical rules, and renewables break those rules — which is
precisely where ICT becomes necessary.

## Core Map

```
Energy Informatics I — Motivation and Basics
│
├── Impact of ICT on energy systems          -> [[ict-energy-footprint]]
│   ├── data centres, PUE, language energy
│   ├── ML development phases (experiment/train/infer)
│   └── blockchain consensus (PoW vs PoS)
│
├── Energy System Basics
│   ├── climate policy frame                 -> [[paris-agreement-climate-goals]]
│   ├── transmission vs distribution grid    -> [[power-grid-fundamentals]]
│   ├── AC vs DC, three-phase, 50 Hz         -> [[alternating-current-basics]]
│   └── demand/supply matching via frequency -> [[power-grid-fundamentals]]
│
└── Use cases for ICT in energy systems
    ├── renewables break "supply follows demand" -> [[demand-side-integration]]
    ├── sector coupling (electricity/gas/heat)   -> [[sector-coupling]]
    └── new business actors (metering, charging, communities)
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[ict-energy-footprint]] | ICT was up to 3% of global energy demand in 2015; data centres, AI, and blockchain drive growth; PUE and language choice quantify part of it |
| [[paris-agreement-climate-goals]] | 2 °C / 1.5 °C targets, why they were chosen (tipping points), and how the EU 20-20-20 package actually landed |
| [[power-grid-fundamentals]] | Transmission vs distribution, DER, AC/DC, and 50 Hz frequency as the demand/supply indicator; "supply follows demand" |
| [[alternating-current-basics]] | AC as a sinusoid, amplitude/period/frequency, the RMS derivation, 230 V vs 325 V |
| [[sector-coupling]] | Electricity/gas/heat as one system; real vs virtual conversion and storage; the ICT dependency in both directions |
| [[demand-side-integration]] | Renewables make supply uncontrollable and decentralised, so demand must become flexible: load shifting, storage, forecasting, new actors |

## Lecture Structure

0. **Impact of ICT on energy systems** — global share, data-centre energy drivers, PUE, programming-language
   energy, ML phases and carbon, PoW vs PoS, finished research projects (SoftAWERE, DeepMind cooling,
   RENergetic, ESN4NW).
0. **Energy system basics** — Paris goals and tipping points, EU 2020 targets and results, efficiency of
   energy sectors, grid structure, AC vs DC, frequency and balancing power, the traditional assumptions.
0. **Use cases for ICT** — implications of renewables, demand-side integration, sector coupling
   (three slides deep), new business actors, forecasting with AI (latency, completeness, correctness).
0. **Outline of the course** — the 0–4 roadmap that leads to SGAM, communication standards, AMI, EV
   charging, substation automation, smart converters.

## Exam-Relevant Points

1. **Frequency as a control signal**: load > generation → frequency falls; load < generation → rises;
   50 Hz everywhere is what makes it usable. Know the reserve types (primary, secondary, minute, hour).
2. **The traditional assumptions** and exactly how renewables violate each one. This is a classic
   "state and explain" question.
3. **PUE = total energy / IT equipment energy.** Be able to say what it does *not* measure.
4. **Sector coupling, real vs virtual conversion** — with an example each (power-to-gas vs changing a
   CHP's electricity/heat ratio).
5. **RMS vs peak**: 230 V is RMS, ≈325 V is peak. Derive the √2 rather than quoting it.
6. **The ICT dependency argument**: a future smart grid depends on ICT, so ICT failures become grid
   failures, and power-quality events damage ICT. Fail-safe control is required.

## Connections

- [[energy-informatics-1]] — course page, exam dates (17.02.2027, 24.03.2027), tutorial schedule.
- Homework: `study/homework/energy-informatics-1/tutorial-01.md` — Tutorial 1 (AC, sector coupling,
  grid assumptions) works entirely from this lecture.
- [[ict-energy-footprint]] is the one page here that leaves the grid behind: it is about computing as
  a load, not about the grid itself.

## Open Questions

- The lecture gives the 2020 EU climate targets and their results, but not the current 2030/2050
  framework — presumably for a later lecture.
- "Flexibility" (syllabus 1.2) is named but never defined in this lecture.
- SGAM (syllabus topic 2) is announced with no content yet.
