---
title: "Semiconductor Physics"
tags: [concept, microelectronics, physics, semiconductor, semester-1]
course: "Introduction to Microelectronics"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites:
  - band-theory
  - valence-band
  - conduction-band
---

## One-line Summary
*Semiconductors are materials whose electrical conductivity falls between conductors and insulators, and can be precisely controlled — which is why every chip in the world is made from silicon.*

## Core Intuition
Why silicon? Not because it's the best conductor or the cheapest material, but because its bandgap (1.12 eV) is the sweet spot: large enough that thermal noise at room temperature doesn't flood the material with carriers, yet small enough that modest doping or applied voltage can switch conductivity by orders of magnitude. This controllability is what makes transistors possible. Understanding semiconductor physics means understanding why carriers exist, how many there are, and what controls their behaviour.

## Formal Definition / Statement
A semiconductor is a crystalline material whose electronic band structure features a valence band separated from a conduction band by a bandgap E_g that is neither zero (metal) nor very large (insulator). For silicon at 300K:

- **Bandgap:** E_g = 1.12 eV (indirect bandgap)
- **Intrinsic carrier concentration:** n_i = 1.5 × 10¹⁰ cm⁻³
- **Crystal structure:** Diamond cubic, each Si atom covalently bonded to 4 neighbours

**Carrier concentration in intrinsic semiconductors:**
- n_i² = N_c × N_v × exp(-E_g / kT)
- N_c = effective density of states in conduction band (2.8 × 10¹⁹ cm⁻³ for Si)
- N_v = effective density of states in valence band (1.04 × 10¹⁹ cm⁻³ for Si)
- At thermal equilibrium: n × p = n_i² (mass action law)

**Why silicon dominates:**
- Abundant (sand = SiO₂), well-understood processing
- Native oxide (SiO₂) is an excellent insulator — critical for MOS devices
- Bandgap allows operation from -55°C to +125°C without excessive leakage
- Decades of manufacturing infrastructure (>$1 trillion invested globally)

## Key Properties / Complexity
- Bandgap determines intrinsic carrier concentration: larger E_g → fewer carriers → lower leakage but harder to switch
- At 0K, a pure semiconductor is a perfect insulator (all electrons in valence band)
- Every 10°C increase roughly doubles n_i — temperature sensitivity is a major design concern
- Silicon's indirect bandgap means it's poor for light emission (why LEDs use GaAs, not Si)
- Germanium (E_g = 0.66 eV): too leaky at room temperature for modern digital circuits
- GaAs (E_g = 1.42 eV, direct): better for RF/optoelectronics but expensive and no native oxide
- Carrier mobility: electrons move faster than holes in Si (μ_e ≈ 1350, μ_h ≈ 480 cm²/Vs)

## Worked Example
**Calculate n_i for silicon at 300K:**

Given: N_c = 2.8 × 10¹⁹ cm⁻³, N_v = 1.04 × 10¹⁹ cm⁻³, E_g = 1.12 eV, kT = 0.0259 eV

n_i² = N_c × N_v × exp(-E_g / kT)
     = 2.8×10¹⁹ × 1.04×10¹⁹ × exp(-1.12 / 0.0259)
     = 2.91×10³⁸ × exp(-43.24)
     = 2.91×10³⁸ × 7.35×10⁻¹⁹
     = 2.14 × 10²⁰ cm⁻⁶

n_i = √(2.14 × 10²⁰) ≈ 1.46 × 10¹⁰ cm⁻³ ≈ 1.5 × 10¹⁰ cm⁻³ ✓

This means in pure silicon at room temperature, only about 1 in 10¹² atoms contribute a free carrier — which is why doping is necessary to make practical devices.

**What happens at 400K?**
- kT = 0.0345 eV
- n_i² = 2.91×10³⁸ × exp(-32.46) ≈ 2.67 × 10²⁴
- n_i ≈ 5.2 × 10¹² cm⁻³ — a ~350× increase from just 100°C rise

## Common Pitfalls
- **Confusing intrinsic with undoped**: Intrinsic means perfectly pure (n = p = n_i). Real "undoped" silicon still has trace impurities.
- **Assuming n_i is constant**: It changes dramatically with temperature — this is why high-temperature electronics are hard.
- **Bandgap ≠ activation energy**: E_g is the energy gap between band edges; the activation energy for carrier generation is E_g/2 (each photon/phonon creates an electron AND a hole).
- **Silicon is not the only semiconductor**: GaAs, GaN, SiC, Ge are all semiconductors with different properties suited to different applications.
- **Mobility vs conductivity**: High mobility doesn't mean high conductivity — you also need high carrier concentration. Doping increases concentration but decreases mobility (ionized impurity scattering).

## Connections
- [[bandgap]] — The fundamental parameter that makes silicon a semiconductor rather than a conductor or insulator
- [[valence-band]] — Where bound electrons and holes reside
- [[conduction-band]] — Where free electrons carry current
- [[intrinsic-semiconductor]] — The pure, undoped material with n = p = n_i
- [[electron-hole]] — The two carrier types that enable current flow in semiconductors
- [[silicon]] — The dominant semiconductor material; its properties drive all downstream design choices
- [[doping]] — The deliberate introduction of impurities to control carrier concentration
- [[conductor]] — Metals have overlapping bands (E_g = 0); semiconductors have a finite gap
- [[insulator]] — Large bandgap materials (>4 eV); semiconductors are in between

## Open Questions
- How does the density of states function shape the carrier concentration vs. temperature curve?
- Why does silicon's indirect bandgap matter for recombination lifetime?
- How do quantum confinement effects change band structure in modern nanoscale transistors?
