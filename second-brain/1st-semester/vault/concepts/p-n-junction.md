---
title: "P-N Junction"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[n-type-semiconductor]]", "[[p-type-semiconductor]]", "[[depletion-region]]"]
---

## One-line Summary
A p-n junction is the boundary formed when p-type and n-type semiconductors meet, creating a depletion region that allows current to flow in one direction but not the other — the fundamental diode.

## Core Intuition
When p-type and n-type materials meet, electrons from the n-side rush to fill holes on the p-side, creating a "no man's land" (depletion region) with no free carriers. This creates a built-in voltage barrier. Forward bias pushes carriers through the barrier; reverse bias widens it and blocks current.

Water analogy: The p-n junction is a canal with a dam of rocks (depletion region). The dam allows some leakage (leakage current). Forward bias = removing rocks (depletion region shrinks, current flows). Reverse bias = adding rocks (depletion region grows, blocks current).

## Formal Definition / Statement
A p-n junction is formed when a [[p-type-semiconductor]] (anode) and [[n-type-semiconductor]] (cathode) are brought into contact. At equilibrium:

- **Depletion region** forms at the interface — electrons from n-side fill holes on p-side
- **Built-in potential:** Vbi ≈ 0.6–0.9 V for silicon
- **Forward bias** (V > 0): provides force for majority carriers toward junction → current flows, depletion region narrows
- **Reverse bias** (V < 0): pulls majority carriers away from junction → depletion region grows, blocks current
- **Leakage current:** small current under reverse bias due to minority carriers
- **Breakdown:** at excessive reverse voltage, depletion region collapses → sudden current increase

## Key Properties / Complexity
- Built-in potential: Vbi = (kT/q) × ln(Na×Nd/nᵢ²) ≈ 0.6–0.9 V for Si
- Depletion width: W = √(2ε(Vbi - V)(1/Na + 1/Nd)/q)
- Forward current: I = Is(exp(V/nVT) - 1), where VT = kT/q ≈ 26 mV at 300K
- Reverse saturation current: Is ≈ 10⁻¹² to 10⁻¹⁵ A
- Breakdown voltage depends on doping concentration

## Worked Example
Silicon p-n junction with Na = Nd = 10¹⁶ cm⁻³:
- Vbi = 0.026 × ln(10¹⁶ × 10¹⁶ / (1.5×10¹⁰)²) ≈ 0.026 × ln(4.4×10¹¹) ≈ 0.697 V
- At forward bias V = 0.7V: I ≈ Is × exp(0.7/0.026) — exponential current increase

## Common Pitfalls
- Confusing forward bias with reverse bias polarity for p-n junctions
- Assuming the depletion region is doped — it's depleted of free carriers
- Forgetting that breakdown is reversible (unlike dielectric breakdown)

## Connections
- [[n-type-semiconductor]] — n-side of junction
- [[p-type-semiconductor]] — p-side of junction
- [[depletion-region]] — the carrier-free zone at the junction
- [[diode]] — the two-terminal device based on p-n junction
- [[zener-diode]] — operates in breakdown region
- [[mosfet]] — contains p-n junctions (source/drain to body)

## Open Questions
- How does junction capacitance affect high-frequency operation?
- What happens at the atomic scale during junction formation?
