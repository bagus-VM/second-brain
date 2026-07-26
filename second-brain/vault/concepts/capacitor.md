---
title: "Capacitor"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[electricity]]"]
---
## One-line Summary
*A capacitor is a two-terminal component that stores energy in an electric field between two conductive plates separated by an insulator (dielectric), with capacitance proportional to plate area and inversely proportional to separation distance.*

## Core Intuition
A capacitor is like a tiny rechargeable battery that stores energy in an electric field rather than in chemicals. When you apply voltage, charge builds up on the plates — positive on one side, negative on the other — creating an electric field in the insulating gap. The bigger the plates and the thinner the gap, the more charge it can store for a given voltage. Capacitors block DC (once fully charged, no more current flows) but pass AC (because the charge/discharge cycle keeps current flowing).

## Formal Definition / Statement
**Capacitance (C):** The ratio of stored charge to applied voltage:
    C = Q / V  (in farads, F)

**Parallel-plate capacitor:**
    C = ε × A / d
where ε = ε₀ × εᵣ is the permittivity of the dielectric, A is plate area, and d is plate separation.

**Energy stored:**
    E = ½CV² = ½Q²/C = ½QV

**Current-voltage relationship:**
    I = C × dV/dt

This means current only flows when voltage is changing — capacitors block DC and pass AC.

**Impedance (AC):**
    Z_C = 1 / (jωC)
At high frequency (ω → ∞), Z_C → 0 (short circuit). At DC (ω = 0), Z_C → ∞ (open circuit).

## Key Properties / Complexity
- **Dielectric materials:** Air (εᵣ ≈ 1), paper (~2.5), ceramic (~20–10000), SiO₂ (~3.9), Ta₂O₅ (~25), HfO₂ (~25)
- **Capacitors in parallel:** C_total = C₁ + C₂ + ... (add like resistors in series)
- **Capacitors in series:** 1/C_total = 1/C₁ + 1/C₂ + ... (add like resistors in parallel)
- **Time constant:** τ = RC — time to charge to 63% of final voltage
- **Energy density:** E/V = ½εᵣε₀(V/d)² — higher field strength and higher εᵣ store more energy per volume
- **Leakage current:** Real capacitors slowly discharge through the dielectric — important for memory and sample-and-hold circuits
- **Temperature dependence:** Ceramic capacitors (especially X7R, Y5V) can lose 50–80% of nominal capacitance with applied DC bias or temperature change

## Worked Example
MOS capacitor (the core of a [[mosfet]]):
- Gate oxide: SiO₂ with εᵣ = 3.9, thickness t_ox = 5 nm
- C_ox = ε₀ × εᵣ / t_ox = (8.85 × 10⁻¹²)(3.9) / (5 × 10⁻⁹) = 6.9 × 10⁻³ F/m² = 6.9 fF/μm²
- For a gate area of 1 μm × 10 μm = 10 μm²: C_gate = 69 fF
- With V_gs = 1.2 V: Q = CV = 69 × 10⁻¹⁵ × 1.2 = 82.8 fC of charge on the gate

This gate capacitance determines switching speed (τ = C/I) and is why thinner oxides give faster transistors — but too thin causes quantum tunnelling leakage.

## Common Pitfalls
- Assuming capacitors store charge "on" the plates — they actually store energy in the electric field between the plates
- Forgetting that current through a capacitor is I = C(dV/dt), not I = V/R — there's no DC current through an ideal capacitor
- Ignoring dielectric breakdown — exceeding the breakdown voltage causes permanent damage (this is relevant to [[avalanche-breakdown]] in semiconductor junctions)
- Confusing capacitance (a fixed geometric/material property) with charge (which varies with voltage)
- Neglecting parasitic capacitance in high-frequency circuits — every wire has some capacitance to its neighbours

## Connections
- [[mos-capacitor]] — The MOS structure (metal-oxide-semiconductor) that forms the gate of a [[mosfet]]
- [[mosfet]] — Uses gate capacitance to control channel formation
- [[electricity]] — Capacitors are a fundamental circuit element alongside resistors
- [[diode]] — Junction capacitance (C_j) and diffusion capacitance (C_d) are parasitic effects in diodes
- [[half-wave-rectifier]] and [[full-wave-rectifier]] — Filter capacitors smooth rectified output
- [[clamper-circuit]] — Uses a capacitor to shift the DC level of a waveform
- [[semiconductor]] — Depletion region acts as a voltage-dependent capacitor (varactor)

## Open Questions
- What are the fundamental limits of energy density in dielectric capacitors?
- Can negative-capacitance ferroelectric gate stacks break the 60 mV/dec subthreshold swing limit?
- How does quantum capacitance in 2D materials (graphene) affect MOS device modelling?
