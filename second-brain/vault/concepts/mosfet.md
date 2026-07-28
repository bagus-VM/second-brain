---
title: "MOSFET"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[transistor]]", "[[semiconductor]]"]
---
## One-line Summary
A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a voltage-controlled transistor where an electric field through a gate oxide controls current flow in a semiconductor channel.

## Core Intuition
The MOSFET operates by applying a voltage to the gate terminal, which creates an electric field through a thin insulating oxide layer. This field attracts or repels charge carriers in the semiconductor beneath, either creating or depleting a conducting channel between source and drain. No DC current flows into the gate — it's purely field-effect operation.

## Formal Definition / Statement
A MOSFET is a four-terminal device (Gate, Drain, Source, Body) consisting of a metal (or polysilicon) gate electrode separated from the semiconductor substrate by a thin silicon dioxide (SiO₂) insulating layer. The gate voltage modulates the conductivity of a channel between source and drain.

Structure (top to bottom): Metal gate → Oxide (SiO₂) → Semiconductor (Si substrate)

Two types:
- **nMOS:** N-type source/drain in P-type substrate. Electrons are the channel carriers. VGS > VTH turns it ON.
- **pMOS:** P-type source/drain in N-type substrate. Holes are the channel carriers. |VGS| > |VTH| turns it ON.

## Key Properties / Complexity
- Extremely high input impedance (gate draws essentially zero DC current)
- Voltage-controlled device (gate voltage controls drain current)
- Four terminals: Gate (G), Drain (D), Source (S), Body (B)
- Oxide thickness (tox) is critical — thinner oxide = stronger field effect = lower VTH
- No gate current means very low static power dissipation (ideal)
- Foundation of CMOS technology (complementary nMOS + pMOS)

## Worked Example
nMOS transistor with VTH = 0.7V, k = 0.5 mA/V²:
- VGS = 0V: OFF (cutoff), ID = 0
- VGS = 2V, VDS = 0.5V (linear region): ID = k[(VGS-VTH)VDS - VDS²/2] = 0.5[(1.3)(0.5) - 0.125] = 0.263 mA
- VGS = 2V, VDS = 3V (saturation): ID = k(VGS-VTH)²/2 = 0.5(1.3)²/2 = 0.423 mA

## Common Pitfalls
- Confusing the MOSFET's field-effect operation with BJT's current-controlled operation.
- Forgetting the body terminal — it affects VTH through the body effect.
- Assuming infinite gate impedance — at high frequencies, gate capacitance matters.
- Mixing up nMOS and pMOS carrier types and bias conditions.

## Connections
- Extends the concept of [[transistor]] to voltage-controlled, field-effect operation.
- The [[mos-capacitor]] is the fundamental physical structure underlying MOSFET operation.
- Specific implementations: [[nmos-transistor]] and [[pmtransistor]].
- Operating behaviour described by [[mosfet-operating-regions]].
- [[threshold-voltage]] is the key parameter determining ON/OFF switching.

## Open Questions
- How does gate oxide scaling affect reliability (tunnelling, breakdown)?
- What replaces MOSFETs when we hit physical scaling limits?
