---
title: "Power Grid Fundamentals"
tags: [concept, energy-informatics, semester-2, power-grid]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
The grid is a two-level hierarchy — transmission above, distribution below — held together by one shared frequency that reports the demand/supply mismatch, and run on the principle that supply follows demand.

## Core Intuition
A grid is a live balance, not a tank: generation must equal load at every instant, and the leftover mismatch appears as a frequency deviation, identical everywhere in the synchronous area. The hierarchy follows distance and voltage — bulk power travels far at high voltage, then is stepped down near the customer. Every "smart" mechanism is a control loop around this balance, and every assumption it rests on is what renewables break.

## Formal Definition / Statement

**Transmission grid.** Long-distance transport at high voltage levels; connects big power stations and industry.

**Distribution grid.** Medium to short distances at stepped-down voltage levels; small loads plus Distributed Energy Resources (DER) and emerging loads — wind and solar plants, Combined Heat and Power (CHP) plants, electric vehicles (EV), heat pumps. Voltage bands follow IEC 60038; the lecture figure labels the levels but quotes no kV values.

**DC vs AC.** Direct current is a unidirectional flow of charge, typically at constant voltage. Alternating current periodically changes the direction of current flow, is typically a sine wave, and is operated as a three-phase system.

**Frequency as balance indicator.** Europe runs at 50 Hz, the US at 60 Hz. Load > generation lowers the frequency; load < generation raises it. The same frequency holds everywhere in the grid, which is what makes it the indicator for control. Correction uses spinning reserve and balancing power, graded primary, secondary, minute, hour; the time constants belong to the Energy Economics chapter.

**Traditional assumptions of energy management and control:** demand cannot be controlled; electricity cannot be stored (in the grid); supply is mainly centralised at the high voltage grid; demand is located in the low voltage grid.

**Major principle: supply follows demand.** Control is triggered by deviations of frequency, not by a schedule of consumer wishes.

## Key Properties
- Balance is instantaneous — "steady balance between demand and supply" is the operating condition, not a daily average.
- Frequency carries two things: the sign of the deviation gives the direction of the imbalance, the magnitude its size.
- The control chain is graded: fast and small reserves first, slower and larger products afterwards.

## Worked Example
At 50 Hz one cycle lasts T = 1/50 s = 20 ms, so the operator compares a measured frequency against a 20 ms reference waveform, not against a daily energy total. A reading of 49.98 Hz gives Δf = −0.02 Hz: negative, so load exceeds generation, so upward balancing power is called; 50.02 Hz means the opposite, and the magnitude sizes the response. (The 0.02 Hz is arithmetic illustration of how the indicator is read; the lecture states the direction rule, not a threshold.)

The voltage chain runs transmission → stepped-down distribution → customer, ending at 230 V. That figure is an RMS value, not a peak — see [[alternating-current-basics]] for why the peak is roughly 325 V.

## Common Pitfalls
- **Reading frequency as a load meter.** It measures imbalance, not demand; a 50.00 Hz grid can carry any total load.
- **Taking "electricity cannot be stored" literally.** The slide says *in the grid*: batteries and pumped storage exist, but the grid itself has no buffer.
- **Treating the distribution grid as "small loads".** Wind, solar, CHP, EV and heat pumps are listed there — the low-voltage level is where the new dynamics live.
- **Assuming 50 Hz is universal.** The US runs 60 Hz, so period-based reasoning has to be re-derived.

## Connections
- [[alternating-current-basics]] — the waveform behind the 50 Hz and 230 V numbers used here.
- [[demand-side-integration]] — what happens to these assumptions once supply is volatile and decentralised.
- [[sector-coupling]] — coupling the grid to gas and heat changes what "the grid" is balancing.

## Open Questions
- Which of the four assumptions fails *first* as renewable share rises — uncontrollable demand, or one-way power flow in the distribution grid? The lecture presents them as a set, without an ordering.
- Balancing power is graded primary/secondary/minute/hour, but no response times are given. How much of the stability budget is spent before minute reserve engages?
