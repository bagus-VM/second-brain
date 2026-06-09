---
title: "MOS Transistors"
tags: [concept, microelectronics, physics, transistor, mosfet, semester-1]
course: "Introduction to Microelectronics"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites:
  - semiconductor-physics
  - doping-and-extrinsic-semiconductors
  - p-n-junction-overview
  - mos-capacitor
---

## One-line Summary
*A MOSFET is a transistor where a voltage on a gate electrode controls current flow between two terminals — it's the switch that makes all digital electronics possible.*

## Core Intuition
The MOSFET is the most important invention in the history of electronics. The idea is deceptively simple: put a metal gate electrode on top of a thin oxide layer sitting on a semiconductor. The gate voltage creates an electric field that either attracts or repels carriers at the semiconductor surface, forming or destroying a conducting channel between the source and drain. No gate current flows (the oxide is an insulator), so the control is purely electric field-based — this is why it's called a Field-Effect Transistor. A modern processor has billions of these, each switching in picoseconds.

## Formal Definition / Statement
A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a four-terminal device (gate, drain, source, body/bulk) that uses an electric field to control current flow through a channel formed at the semiconductor-oxide interface.

**MOS capacitor (the gate structure):**
The [[mos-capacitor]] is the heart of the MOSFET. Gate voltage across the oxide creates an electric field that modulates the semiconductor surface:
- Accumulation: majority carriers accumulate at surface (V_G < V_FB)
- Depletion: majority carriers are pushed away (V_FB < V_G < V_T)
- Inversion: minority carriers form a conducting channel (V_G > V_T)

**Threshold voltage (V_T):**
The [[threshold-voltage]] is the gate voltage at which strong inversion begins:
- V_T = V_FB + 2φ_F + √(2ε_s q N_A (2φ_F)) / C_ox
- φ_F = (kT/q) × ln(N_A/n_i) — Fermi potential
- V_FB = flat-band voltage (depends on gate material work function and oxide charges)
- For nMOS on p-substrate: V_T is positive (must apply positive gate voltage)
- For pMOS on n-substrate: V_T is negative (must apply negative gate voltage)

**nMOS transistor:**
- [[nmos-transistor]]: n⁺ source and drain in p-type substrate
- V_GS > V_T → electron inversion layer forms → channel connects S to D
- Current flows from drain to source (electrons)
- V_DS > 0: electrons drift from S to D

**pMOS transistor:**
- [[pmos-transistor]]: p⁺ source and drain in n-type substrate
- V_SG > |V_T| → hole inversion layer forms
- Current flows from source to drain (holes)
- V_SD > 0: holes drift from S to D

**Operating regions ([[mosfet-operating-regions]]):**
- Cutoff: V_GS < V_T → no channel → I_D = 0
- Triode (linear): V_GS > V_T and V_DS < V_DS(sat) → channel is uniform
  - I_D = μ_n C_ox (W/L) [(V_GS - V_T)V_DS - V_DS²/2]
- Saturation: V_GS > V_T and V_DS ≥ V_DS(sat) = V_GS - V_T → channel pinched off
  - I_D = (1/2) μ_n C_ox (W/L) (V_GS - V_T)² (1 + λV_DS)
  - Saturation is where the transistor acts as an amplifier (analog) or a closed switch (digital)

## Key Properties / Complexity
- Gate draws no DC current (insulating oxide) — extremely high input impedance (~10¹⁴ Ω)
- V_T is the most critical parameter: it determines switching speed, power, and noise immunity
- Channel length modulation (λ): in saturation, I_D increases slightly with V_DS (not truly constant)
- Subthreshold conduction: below V_T, there's still a small exponential current (important for low-power design)
- Body effect: V_T increases when source-body voltage V_SB > 0 (back-gate bias effect)
- Velocity saturation: at short channel lengths, carrier velocity saturates and I_D becomes linear in V_GS (not quadratic)
- Transconductance: g_m = ∂I_D/∂V_GS — measures how effectively gate controls current
- W/L ratio is the primary design knob: larger W → more current → faster switching (but more capacitance)

## Worked Example
**nMOS transistor in 180nm technology:**

Parameters: μ_n C_ox = 270 μA/V², V_T = 0.4V, W/L = 10, λ = 0.05 V⁻¹, V_DD = 1.8V

Step 1: Is it in saturation or triode?
  V_GS = 1.8V, V_DS = 1.8V, V_DS(sat) = V_GS - V_T = 1.4V
  Since V_DS = 1.8V > 1.4V → saturation region ✓

Step 2: Drain current in saturation
  I_D = (1/2) × 270×10⁻⁶ × 10 × (1.8 - 0.4)² × (1 + 0.05 × 1.8)
      = 135×10⁻⁶ × 10 × 1.96 × 1.09
      = 2.89 mA

Step 3: Transconductance
  g_m = √(2 × μ_n C_ox × W/L × I_D)
      = √(2 × 270×10⁻⁶ × 10 × 2.89×10⁻³)
      = √(15.6×10⁻⁶)
      = 3.95 mA/V

Step 4: What if V_GS drops to 0.3V?
  V_GS = 0.3V < V_T = 0.4V → cutoff → I_D ≈ 0 (transistor is OFF)
  This is the basis of digital logic: HIGH → ON, LOW → OFF

## Common Pitfalls
- **"nMOS passes a strong 1"**: Actually, nMOS passes a degraded HIGH (V_out = V_GS - V_T). This is why CMOS (with pMOS pull-up) is needed for rail-to-rail output.
- **Confusing V_DS(sat) with V_GS - V_T**: They're the same thing in the simplest model, but velocity saturation at short channels changes the picture.
- **Forgetting body effect**: When source is not tied to bulk (common in CMOS logic), V_T increases. This is frequently tested.
- **Saturation ≠ cutoff**: "Saturation" in MOSFETs means the channel is pinched off at the drain — NOT that current is zero. BJT saturation and MOSFET saturation mean completely different things.
- **Gate current is zero**: Ideal MOSFET draws no gate current. In practice, gate oxide leakage becomes significant below ~2nm oxide thickness (and is why high-k dielectrics replaced SiO₂).
- **V_T depends on process**: Threshold voltage varies with oxide thickness, doping, and temperature. Modern designs must account for V_T variation.

## Connections
- [[mosfet]] — The generic term; nMOS and pMOS are the two flavors
- [[mos-capacitor]] — The gate-oxide-semiconductor structure that forms the foundation of the MOSFET
- [[threshold-voltage]] — The critical gate voltage that turns the transistor on
- [[nmos-transistor]] — Electron-channel transistor used in pull-down networks
- [[pmos-transistor]] — Hole-channel transistor used in pull-up networks
- [[mosfet-operating-regions]] — Cutoff, triode, and saturation regions define transistor behavior
- [[cmos-inverter]] — Combines nMOS and pMOS for rail-to-rail digital switching
- [[common-source-amplifier]] — Basic analog amplifier using MOSFET in saturation
- [[electron-hole]] — Electrons carry current in nMOS, holes in pMOS
- [[doping-and-extrinsic-semiconductors]] — Source/drain doping, substrate doping, and V_T are all determined by doping profiles

## Open Questions
- How does FinFET (3D) structure improve short-channel control over planar MOSFET?
- What limits the subthreshold slope to 60 mV/decade at room temperature, and can it be broken?
- How does gate oxide reliability (time-dependent dielectric breakdown) set the ultimate scaling limit?
