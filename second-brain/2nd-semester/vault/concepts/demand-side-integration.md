---
title: "Demand-Side Integration"
tags: [concept, energy-informatics, semester-2, demand-side]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[power-grid-fundamentals]]"]
---

## One-line Summary
Once supply becomes volatile and moves into the low-voltage grid, the controllable side of the balance has to become demand — which turns load flexibility, storage and forecasting into an ICT problem.

## Core Intuition
The traditional grid balanced by dispatching large plants to follow a forecastable load. Renewables invert that: cheap energy now arrives when the weather says so, from thousands of small units at the bottom of the voltage hierarchy. Supply has become the unpredictable part, so the remaining lever is *when* consumption happens. Demand-side integration exploits that lever, and it only works if the grid can see, predict and address individual loads.

## Formal Definition / Statement

**Why renewables force it — three implications stated in the lecture:**
1. Supply is only partially controllable or predictable.
2. Supply becomes decentralised and moves towards the edge, into the low-voltage distribution grid.
3. Potential reversal of power flow — power can travel from the distribution level upward.

The lecture names the result directly: **"New Challenge: Demand Side Integration!"**

**Consequences, and the ICT need they create:** discover and exploit degrees of freedom for decentralised "demand (and supply) management", i.e. load shifting; and develop new storage technologies.

**New business actors and business cases** (roles paraphrased):

| Actor | Role created by the shift |
|---|---|
| Smart Meter Operator | Metering plus data communication and storage |
| E-Mobility Service Provider | Mobility as an electricity service |
| Charging Point Operator | Operates the physical charging infrastructure |
| Smart City | Municipal load and service coordination |
| Renewable Energy Communities | Collective local generation |

**Forecasting.** Fluctuation in demand and renewable supply limits predictability. ICT records and stores data about generation and loads, and AI methods forecast from energy data such as generation profiles. Data may be collected in real time, so **latency** matters, and **completeness and correctness** are vital. The lecture illustrates the forecasting object with German renewable generation and load in October 2024 (smard.de).

## Key Properties
- Degrees of freedom are the resource: not how much load exists, but how much can move and by how much.
- Shifting preserves daily energy demand while changing its shape within the day; storage holds the energy instead.
- Decentralisation moves the control problem to the edge, where the grid is least instrumented.
- Forecast quality is bounded by data quality, not model quality.

## Worked Example
A low-voltage feeder built for the traditional assumption carries load downward: transformer → households. Add rooftop PV and the same feeder exports at midday. The mechanism is the lecture's third implication; the magnitudes below are a constructed illustration, not slide figures.

Suppose the households draw 100 kW at noon while rooftop systems on the same feeder produce 150 kW. It now pushes 50 kW *up* into the distribution grid — the reverse of its design direction. Three levers exist, all demand-side or ICT levers: shift the 100 kW toward midday (virtual storage), add local storage (real storage), or curtail. Choosing requires knowing in near real time what each household draws — the smart-meter and forecasting stack the lecture lists. Latency decides whether the answer arrives while the surplus exists; incompleteness decides whether 100 kW is a measurement or a guess.

## Common Pitfalls
- **Confusing it with energy efficiency.** Efficiency reduces the total; integration moves the timing.
- **Assuming the distribution grid stays passive.** Reversal of power flow is a first-class implication, not an edge case.
- **Treating forecasting as a pure ML problem.** The stated constraints are latency, completeness and correctness — data properties.
- **Assuming smart meters are billing devices.** The listed operator role includes data communication and storage.

## Connections
- [[power-grid-fundamentals]] — the assumptions broken here are stated there.
- [[sector-coupling]] — where shifted load goes when it leaves the electrical carrier.
- [[ict-energy-footprint]] — ICT is the enabler here and a load on the same grid it manages.

## Open Questions
- Degrees of freedom are the resource, but the lecture never quantifies how much residential load is shiftable without violating comfort. Is household flexibility large enough to matter at grid scale, or only at the margin?
- Reversal of power flow is stated as a grid consequence; the lecture does not say how the smart meter operator's data model represents an export, or who may act on it.
