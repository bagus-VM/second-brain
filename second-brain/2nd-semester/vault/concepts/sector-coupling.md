---
title: "Sector Coupling"
tags: [concept, energy-informatics, semester-2, sector-coupling]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[demand-side-integration]]"]
---

## One-line Summary
Sector coupling is the interoperability of the electricity, gas and thermal systems under one integrated energy management, so that flexibility in one carrier can serve as conversion or storage for another — with ICT as both the enabler and the single point of failure.

## Core Intuition
Each sector alone has a hard limit: electricity has no buffer, heat is local, gas is storable. Coupled, the limits stop coinciding — a wind surplus becomes hydrogen instead of curtailment, and a CHP plant decides whether the same fuel becomes more electricity or more heat. Some coupling is *real*, where energy physically changes carrier; some is *virtual*, where only the split between carriers moves. Both need measurement and control across sectors — ICT.

## Formal Definition / Statement

**Definition (lecture).** Sector coupling is interoperability between energy systems — electricity, gas, thermal — with integrated energy management in distributed systems, to increase efficiency, flexibility and stability of the combined sectors.

**Energy conversion between sectors:**
- *Real* — e.g. power-to-gas: electricity is electrolysed into hydrogen and synthetic fuels, so the energy leaves the electrical carrier.
- *Virtual* — e.g. changing the conversion rate of electricity and heat in a CHP plant: the same fuel input is re-split between electrical and thermal output, with no new carrier created.

**Additional storage capacity:**
- *Real* — battery, pumped storage: a device holds the energy.
- *Virtual* — demand shifting: nothing is stored, consumption moves in time.

**Advantages and disadvantages.** The lecture states the aims and the ICT dependency separately; the pros/cons split is my structuring.

| Advantages | Disadvantages |
|---|---|
| One carrier absorbs another's volatility (wind → hydrogen, heat) | Real conversion loses energy at every hop |
| Virtual options add flexibility with no new hardware | Coupling propagates disturbances between carriers |
| Additional storage, real and virtual, without new grid capacity | Control becomes safety-critical and must be fail safe |

## Key Properties
- Coupling adds options, not capacity: one asset serves two sectors, raising utilisation.
- Real coupling crosses an efficiency barrier; virtual coupling builds nothing.
- Every coupling point is a control point, hence an ICT dependency.
- ICT is also part of recovery: it can help restore operation after a brownout or blackout.

## Worked Example
Tutorial Task 2d asks for exactly this, and the lecture supplies the pair.

*Real conversion.* Wind output exceeds load. Instead of curtailing, electrolysis turns the electricity into hydrogen, stored or fed into the gas network as synthetic fuel. The energy has changed carrier, so getting electricity back means converting again, and each hop loses energy.

*Virtual conversion.* The same surplus is absorbed by a CHP plant running heat-led. Raising its electrical output and lowering its heat output shifts the electricity/heat ratio with no new carrier. No electrolyser, no hydrogen — just a different operating point on an existing machine.

The storage pair behaves identically: a battery (real) versus moving a load to a later hour (virtual). "Real vs virtual" turns on whether energy moves between carriers or devices, or only where it is used.

## Common Pitfalls
- **Calling demand shifting "storage".** It is virtual storage: nothing is charged, the timing changes.
- **Assuming virtual conversion is lossless.** It skips a conversion step; it does not escape the plant's own efficiency limits.
- **Forgetting the dependency runs both ways.** A grid failure takes ICT down — servers and routers need power, and overvoltage can damage hardware — so battery and overvoltage protection are required.
- **Assuming the legacy grid is equally exposed.** It depends weakly on ICT; the exposure arrives with the smart grid, where many participants connect.

## Connections
- [[demand-side-integration]] — virtual storage is demand shifting, so coupling inherits the demand-side problem.
- [[power-grid-fundamentals]] — coupling changes what the 50 Hz balance is actually balancing.
- [[ict-energy-footprint]] — the other direction of the relationship: coupling is one way computing pays the grid back.

## Open Questions
- The lecture requires ICT-based control to be *fail safe* but never says what that means for a multi-carrier system: does a CHP plant fall back to heat-led operation, and who decides?
- Real coupling pays a conversion loss at every hop, and the "Efficiency of energy sectors" slide (Tom Brown et al.) carries no numbers — at what round-trip efficiency does power-to-gas stop being worth it?
