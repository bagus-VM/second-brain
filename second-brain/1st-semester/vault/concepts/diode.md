---
title: "Diode"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[p-n-junction]]", "[[depletion-region]]"]
---

## One-line Summary
A diode is a two-terminal semiconductor device based on a p-n junction that allows current to flow primarily in one direction (from anode to cathode).

## Core Intuition
A diode is an electrical "check valve" — it lets current flow easily in one direction (forward bias) but blocks it in the other (reverse bias). This one-way behaviour comes from the [[depletion-region]] at the [[p-n-junction]].

## Formal Definition / Statement
A diode is a two-terminal electronic component formed by a [[p-n-junction]]. The p-type side is the **anode** and the n-type side is the **cathode**.

**I-V characteristic:**
$$I = I_s \left(e^{V/nV_T} - 1\right)$$

where:
- Is = reverse saturation current (~10⁻¹² to 10⁻¹⁵ A)
- n = ideality factor (1–2)
- VT = kT/q ≈ 26 mV at 300K (thermal voltage)

**Operating regions:**
- **Forward bias (V > 0):** Current flows exponentially once V exceeds built-in potential (~0.6–0.7 V for Si)
- **Reverse bias (V < 0):** Only leakage current (≈ -Is) flows
- **Breakdown:** At excessive reverse voltage, current suddenly increases

## Key Properties / Complexity
- Unidirectional current flow
- Forward voltage drop: ~0.6–0.7 V for silicon
- Reverse breakdown voltage: depends on doping and structure
- Used in [[rectifier]], [[clamper-circuit]], [[limiter-circuit]] circuits
- Special types: [[zener-diode]] (voltage regulation)

## Worked Example
Silicon diode with Is = 10⁻¹² A, n = 1, at 300K:
- At V = 0.5V: I = 10⁻¹² × (e^(0.5/0.026) - 1) ≈ 2.2 mA
- At V = 0.7V: I = 10⁻¹² × (e^(0.7/0.026) - 1) ≈ 4.9 A (practically limited by resistance)
- At V = -5V: I ≈ -Is = -10⁻¹² A (negligible)

## Common Pitfalls
- Confusing anode (p-type) and cathode (n-type) — current flows from anode to cathode
- Assuming diodes have zero forward voltage — always ~0.6–0.7V for Si
- Forgetting that breakdown is reversible in diodes (unlike dielectric breakdown)

## Connections
- [[p-n-junction]] — the physical structure of a diode
- [[depletion-region]] — controls diode behaviour
- [[zener-diode]] — special diode for voltage regulation
- [[rectifier]] — converts AC to DC using diodes
- [[clamper-circuit]] — shifts DC level using diodes
- [[limiter-circuit]] — clips voltage using diodes
- [[transistor]] — next level of complexity (three terminals)

## Open Questions
- How does temperature affect diode I-V characteristics?
- What are the practical limits of diode switching speed?
