---
title: "Depletion Region"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[p-n-junction]]", "[[n-type-semiconductor]]", "[[p-type-semiconductor]]"]
---

## One-line Summary
The depletion region is the charge-carrier-free zone at a p-n junction where electrons and holes have recombined, leaving behind fixed ions that create a built-in electric field.

## Core Intuition
When p-type and n-type materials meet, electrons from the n-side rush to fill holes on the p-side. But once they fill those holes, they leave behind fixed positive ions (on the n-side) and fixed negative ions (on the p-side). This creates a region with no free carriers — just a built-in electric field that opposes further carrier movement.

## Formal Definition / Statement
The depletion region (also called the space-charge region) is the region at a [[p-n-junction]] where mobile charge carriers have been swept away, leaving only fixed ionized dopant atoms. The electric field across this region creates the built-in potential.

- **Width:** W = √(2εs(Vbi + VR)(1/NA + 1/ND)/q)
- **Built-in field:** E = -dV/dx across the depletion region
- **Charge neutrality:** total negative charge on p-side = total positive charge on n-side
- Narrows under forward bias, widens under reverse bias

## Key Properties / Complexity
- Contains no free charge carriers (depleted)
- Fixed positive ions on n-side, fixed negative ions on p-side
- Creates built-in electric field (from n-side to p-side)
- Built-in potential: Vbi ≈ 0.6–0.9 V for silicon
- Width depends on doping: lower doping → wider depletion region
- Acts as a capacitor (junction capacitance: Cj = εA/W)

## Worked Example
Si p-n junction with NA = ND = 10¹⁶ cm⁻³, at VR = 0V:
- Vbi ≈ 0.697 V
- W ≈ √(2 × 11.7 × 8.85×10⁻¹⁴ × 0.697 × 2/(10¹⁶ × 1.6×10⁻¹⁹))
- W ≈ 0.43 μm

At reverse bias VR = 5V: W increases to ≈ √(5.697/0.697) × 0.43 ≈ 1.23 μm

## Common Pitfalls
- Confusing depletion region with insulator — it's created by ionized dopants, not by material properties
- Forgetting that depletion width changes with applied voltage

## Connections
- [[p-n-junction]] — the depletion region forms at the junction
- [[diode]] — device behavior depends on depletion region width
- [[zener-breakdown]] — occurs when electric field in depletion region is very high
- [[avalanche-breakdown]] — carrier multiplication in depletion region
- [[mosfet]] — depletion region forms under the gate in some operating modes

## Open Questions
- How does depletion region width affect junction capacitance in high-frequency circuits?
