---
title: "Threshold Voltage"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[mos-capacitor]]"]
---
## One-line Summary
The threshold voltage (VTH) is the minimum gate-to-source voltage required to create a conducting inversion channel in a MOSFET, marking the transition from OFF to ON state.

## Core Intuition
As you increase VGS on a MOSFET, the gate oxide capacitor accumulates charge and the depletion region widens. At VGS = VTH, enough minority carriers are attracted to the surface to form a conducting channel. Below VTH, the transistor is effectively an open switch. Above VTH, current can flow. VTH is the single most important parameter defining when a MOSFET switches.

## Formal Definition / Statement
For an nMOS transistor with P-type substrate:

VTH = VTH0 + γ(√(|2φF + VSB|) - √(|2φF|))

Where:
- VTH0 = threshold voltage with VSB = 0 (zero body bias)
- γ = body effect coefficient = √(2qεsNA) / Cox
- φF = (kT/q)ln(NA/ni) ≈ 0.35V for typical silicon
- VSB = source-to-body voltage
- NA = substrate doping concentration
- Cox = εox/tox (oxide capacitance per unit area)

VTH0 depends on:
- Gate material work function
- Oxide thickness (tox)
- Substrate doping (NA)
- Oxide fixed charges (Qox)
- Fermi potential (φF)

## Key Properties / Complexity
- Typically 0.3V to 1.0V for modern processes (decreasing with technology scaling)
- Body effect: VTH increases with VSB (reverse body bias makes it harder to invert)
- VTH can be adjusted by ion implantation (channel doping)
- Lower VTH = faster switching but higher leakage current
- pMOS threshold is negative: |VGS| > |VTH| to turn on

## Worked Example
nMOS with VTH0 = 0.5V, γ = 0.4 V^(1/2), φF = 0.35V, VSB = 1V:
- VTH = 0.5 + 0.4(√(0.7 + 1) - √(0.7))
- VTH = 0.5 + 0.4(√1.7 - √0.7)
- VTH = 0.5 + 0.4(1.304 - 0.837)
- VTH = 0.5 + 0.4(0.467)
- VTH = 0.5 + 0.187 = 0.687V

The body effect increased VTH from 0.5V to 0.687V due to 1V source-body bias.

## Common Pitfalls
- Forgetting the body effect — VTH is not constant; it depends on VSB.
- Confusing nMOS and pMOS threshold polarity (nMOS VTH > 0, pMOS VTH < 0).
- Assuming VTH is a sharp cutoff — subthreshold conduction exists below VTH.
- Ignoring process variation — VTH varies across a wafer and between chips.

## Connections
- Derived from [[mos-capacitor]] physics (depletion → inversion transition).
- Critical for [[nmos-transistor]] and [[pmtransistor]] operation.
- Used in [[mosfet-operating-regions]] to define cutoff condition.
- Modified by [[ion-implantation]] during fabrication.
- [[thermal-diffusion]] historically used for channel doping.

## Open Questions
- How does random dopant fluctuation affect VTH in nanoscale transistors?
- What is the minimum achievable VTH before leakage becomes unmanageable?
