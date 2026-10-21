---
title: "Paris Agreement and EU 2020 Climate Goals"
tags: [concept, energy-informatics, semester-2, climate-policy]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
The 2015 Paris Agreement sets a "well below 2 °C, pursue 1.5 °C" target to avoid irreversible tipping points; the EU's 20/20/20 package tests whether such a target can be met.

## Core Intuition
A temperature target is not a physical constant but a risk threshold: some elements of the Earth system flip irreversibly past a certain warming, and 2 °C and 1.5 °C were chosen to stay on the safe side of as many flips as possible. That turns an abstract climate number into a design constraint — the grid must decarbonise on a schedule. The EU 2020 package is the empirical check on whether a 20% target structure delivered.

## Formal Definition / Statement

**Paris Agreement (2015).** Hold the global average temperature increase well below 2 °C above pre-industrial levels, and pursue efforts to limit it to 1.5 °C. The targets were chosen to avoid potentially irreversible tipping points in the Earth's systems (Schellnhuber 2016).

**Tipping elements, split by whether the target can still save them** (Schellnhuber 2016, as presented):

| Avoidable | Probably not avoidable |
|---|---|
| Amazon rainforest, boreal forest | West Antarctic Ice Sheet |
| Thermohaline circulation (warms Europe) | Greenland, alpine glaciers |
| Sahel | Arctic summer sea ice |
| El Niño–Southern Oscillation | Coral reefs |
| East Antarctic ice sheet, permafrost, Arctic winter sea ice | |

The left column is what the target buys; the right is what it is already too late for.

**EU 2020 climate & energy package** — three targets: a 20% cut in greenhouse gas emissions from 1990 levels; 20% of EU energy from renewables; a 20% improvement in energy efficiency.

**Reported outcome** (European Commission / EEA):

| Target | Goal | Outcome |
|---|---|---|
| Greenhouse gases vs 1990 | −20% | −31%, but only 21 member states reached their national target |
| Renewables share | 20% | 21.3% |
| Energy consumption reduction | 20% | 25%, distorted by COVID-19 lockdowns |

The lecture also shows scenarios for the probability of meeting climate goals, keyed to INDC (Intended Nationally Determined Contributions) and IPCC AR5 (2014).

## Key Properties
- Targets are risk statements, not predictions: "well below 2 °C" is a boundary, 1.5 °C an aspiration inside it.
- Irreversibility is what makes the threshold binding; a reversible effect would need no hard target.
- Three parallel 20% goals mean progress can be uneven while the headline still looks met.
- Headline achievement and member-state compliance are different measurements, and here they disagree.

## Worked Example
Check the scorecard. The GHG goal was a 20% cut from 1990; the reported cut is 31% — 11 points beyond target, or 31/20 = 1.55× the required reduction. Renewables reached 21.3% against 20% (1.065×), met by 1.3 points. Energy consumption fell 25% against a 20% goal (1.25×), with lockdowns doing much of the work.

Read it structurally. Only 21 member states hit their *national* targets even though the EU-wide GHG number overshot by more than half again: the aggregate was carried by a subset. A system-level metric can be satisfied while the distribution of effort is not — the same failure mode as an average grid frequency hiding local congestion.

## Common Pitfalls
- **Reading "well below 2 °C" as "2 °C".** The agreement has two tiers; the 1.5 °C effort is in the text.
- **Assuming the tipping lists are symmetric.** The lecture separates avoidable from probably-not-avoidable; West Antarctic ice and coral reefs are in the second column.
- **Treating 31% > 20% as full compliance.** The national shortfall is reported alongside.
- **Quoting the 25% efficiency result without the COVID caveat.** Lockdowns heavily influenced the data.

## Connections
- [[ict-energy-footprint]] — ICT's up-to-3% of global demand (2015) is the load this frame must absorb.
- [[power-grid-fundamentals]] — decarbonisation forces the generation mix, and with it the grid assumptions.
- [[demand-side-integration]] — the operational answer to the volatile mix built to meet these targets.

## Open Questions
- The lecture reports the 2020 outcome but not the mechanism: was the 31% driven by renewables deployment, coal-to-gas switching, deindustrialisation, or the lockdown effect?
- If 21 states met national targets while the aggregate overshot by 55%, should the next architecture be set per state, or is only the aggregate physically meaningful?
