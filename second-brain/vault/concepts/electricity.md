---
title: "Electricity"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*Electricity is the flow of electric charge (carried by electrons or holes), governed by fundamental relationships between voltage (push), current (flow), and resistance (opposition).*

## Core Intuition
Think of a water system: voltage is the water pressure (how hard electrons are being pushed), current is the flow rate (how many electrons pass a point per second), and resistance is the pipe width (how hard it is for electrons to flow). Ohm's law (V = IR) ties them together — more pressure or less resistance means more flow. In semiconductors, we manipulate resistance through doping and transistor switching to control current flow precisely.

## Formal Definition / Statement
**Charge (Q):** Measured in coulombs (C). 1 electron carries −1.6 × 10⁻¹⁹ C.

**Current (I):** Rate of charge flow: I = dQ/dt. Measured in amperes (A). By convention, current flows from positive to negative (opposite to electron flow).

**Voltage (V):** Electric potential difference between two points. V = W/Q (energy per unit charge). Measured in volts (V).

**Resistance (R):** Opposition to current flow. R = ρL/A where ρ is resistivity, L is length, A is cross-sectional area. Measured in ohms (Ω).

**Ohm's Law:** V = IR (linear relationship valid for ohmic materials)

**Power:** P = VI = I²R = V²/R. Measured in watts (W).

**Kirchhoff's Laws:**
- KCL: Sum of currents entering a node = sum leaving (conservation of charge)
- KVL: Sum of voltages around any closed loop = 0 (conservation of energy)

## Key Properties / Complexity
- **Conventional current vs electron flow:** Conventional current (positive to negative) is the engineering convention; actual electron flow in metals is negative to positive. In semiconductors, both electrons (negative carriers) and holes (positive carriers) contribute to current
- **AC vs DC:** DC (direct current) flows in one direction constantly. AC (alternating current) oscillates sinusoidally — mains power is 50/60 Hz AC
- **Resistivity of materials:**
  - Conductors: ρ ~ 10⁻⁸ Ω·m (copper, aluminum)
  - Semiconductors: ρ ~ 10⁻⁶ to 10⁶ Ω·m (tunable with doping)
  - Insulators: ρ ~ 10¹⁰ to 10¹⁸ Ω·m (glass, rubber)
- **Capacitance:** C = Q/V. Stores energy in electric field between conductors. C = εA/d for parallel plate
- **Energy stored in capacitor:** E = ½CV²

## Worked Example
A silicon resistor with ρ = 10 Ω·m, length L = 1 mm, cross-section A = 1 μm²:
- R = ρL/A = (10)(10⁻³) / (10⁻¹²) = 10¹⁰ Ω = 10 GΩ
- With V = 5 V applied: I = V/R = 5 / 10¹⁰ = 0.5 nA (very small — intrinsic silicon is nearly insulating)
- After heavy n-type doping (ρ drops to 10⁻³ Ω·m): R = 10⁶ Ω = 1 MΩ → I = 5 μA (much more useful)

This demonstrates why [[doping]] is essential — intrinsic semiconductor is too resistive for practical circuits.

## Common Pitfalls
- Confusing current direction: conventional current (positive to negative) vs electron flow (negative to positive)
- Forgetting that V = IR is only valid for ohmic materials — diodes and transistors are non-ohmic
- Mixing up resistance (property of a component) with resistivity (property of a material)
- Assuming voltage "flows" — voltage is a potential difference, not a substance. Current flows

## Connections
- [[semiconductor]] — Materials whose resistivity is between conductors and insulators and can be tuned
- [[band-theory]] — Explains why some materials conduct and others don't based on energy band structure
- [[capacitor]] — Stores charge and energy in electric fields; fundamental to MOS devices
- [[diode]] — A non-ohmic device that violates the simple V = IR relationship
- [[mosfet]] — Voltage-controlled device that modulates resistance in a semiconductor channel
- [[doping]] — Controls semiconductor resistivity by adding charge carriers

## Open Questions
- What are the fundamental limits of resistivity in doped semiconductors at nanoscale dimensions?
- How does quantum tunneling affect classical Ohm's law in ultra-thin devices?
