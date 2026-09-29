---
title: "MOS Capacitor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[mosfet]]", "[[semiconductor]]"]
---
## One-line Summary
The MOS capacitor is the fundamental structure beneath the MOSFET gate — a metal-oxide-semiconductor stack where an applied electric field controls the concentration of charge carriers in the semiconductor.

## Core Intuition
When you apply a voltage across the gate and substrate, the electric field penetrates the oxide and reaches the semiconductor surface. Depending on the voltage polarity and magnitude, the surface can accumulate majority carriers, deplete them, or invert to form minority-carrier channels. This is the physical mechanism that makes MOSFETs work.

## Formal Definition / Statement
A MOS capacitor consists of a metal (or polysilicon) gate electrode, a thin insulating oxide layer (SiO₂), and a doped semiconductor substrate. The applied gate voltage VG creates an electric field that modifies the charge distribution at the semiconductor surface.

Three operating regimes for a P-type substrate:
1. **Accumulation (VG < 0):** Negative gate voltage attracts holes to the surface. Majority carrier concentration increases at the oxide-semiconductor interface.
2. **Depletion (0 < VG < VTH):** Positive gate voltage repels holes, creating a depletion region of uncovered negative acceptor ions near the surface.
3. **Inversion (VG ≥ VTH):** Strong positive gate voltage attracts minority carriers (electrons) to the surface, forming an inversion layer — a thin conducting N-type channel at the surface of the P-type substrate.

## Key Properties / Complexity
- Gate oxide capacitance per unit area: Cox = εox / tox
- Depletion region width increases with gate voltage until inversion
- Inversion layer charge is proportional to (VGS - VTH)
- The transition from depletion to inversion defines the threshold voltage VTH
- At high frequencies, the inversion layer cannot respond fast enough (only depletion + oxide capacitance seen)
- At low frequencies, the full capacitance (oxide + inversion) is measured

## Worked Example
MOS capacitor with P-type substrate (NA = 10¹⁶ cm⁻³), tox = 10nm, SiO₂:
- Cox = εox/tox = (3.9 × 8.85×10⁻¹⁴) / (10×10⁻⁷) = 3.45×10⁻⁷ F/cm²
- Built-in potential φF = (kT/q)ln(NA/ni) = 0.026 × ln(10¹⁶/1.5×10¹⁰) ≈ 0.349V
- Maximum depletion width: Wmax = √(4εsφF/qNA) ≈ 0.3μm
- Threshold voltage depends on oxide thickness, doping, and flat-band voltage

## Common Pitfalls
- Confusing accumulation and inversion — accumulation has MORE majority carriers; inversion has minority carriers dominating the surface.
- Forgetting that VTH depends on substrate doping (body effect).
- Assuming the inversion charge responds instantly — it has finite generation/recombination time.
- Ignoring oxide fixed charges and interface traps that shift the flat-band voltage.

## Connections
- Foundation of [[mosfet]] operation — the gate-channel structure IS a MOS capacitor.
- Directly leads to [[threshold-voltage]] definition (voltage at which inversion begins).
- Related to [[semiconductor]] physics and carrier concentration.
- Flat-band voltage and work function differences are key parameters.

## Open Questions
- How does quantum confinement in ultra-thin oxide layers affect capacitance?
- What is the role of high-k dielectrics in modern MOS capacitors?
