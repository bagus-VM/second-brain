---
title: "Semiconductor Physics"
tags: [topic, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[electricity]]", "[[band-theory]]"]
---

## One-line Summary
Semiconductors are materials whose electrical conductivity lies between conductors and insulators, defined by their [[bandgap]] structure, and [[silicon]] dominates due to its ideal gap, oxide quality, and abundance.

## Core Intuition
Think of energy levels in an atom spreading into bands when billions of atoms bond in a crystal. The [[valence-band]] holds electrons locked in bonds. The [[conduction-band]] holds electrons free to move. The gap between them determines everything: a tiny or zero gap means conductor (copper), a huge gap means insulator (glass), and a moderate gap (1–3 eV) means [[semiconductor]]. At room temperature, thermal energy (~0.026 eV) excites some electrons across the gap, creating a predictable, tunable number of charge carriers.

## Formal Definition / Statement
A [[semiconductor]] is a crystalline or amorphous solid whose [[valence-band]] is completely filled and [[conduction-band]] is completely filled at 0 K, separated by a [[bandgap]] E_g typically in the range 0.1–4 eV. At finite temperature T, the intrinsic carrier concentration follows:

    n_i = sqrt(N_c * N_v) * exp(-E_g / 2kT)

where N_c and N_v are the effective densities of states in the conduction and valence bands, k is Boltzmann's constant, and T is absolute temperature. For [[silicon]] at 300 K: n_i ≈ 1.5 × 10^10 cm^-3.

## Key Properties / Complexity

**Band Structure Classification:**
- **Conductor:** Overlapping bands, no gap — electrons move freely (Cu, Al).
- **Insulator:** E_g > 4 eV — almost no thermal carriers (SiO_2, diamond).
- **Semiconductor:** 0.1 eV < E_g < 4 eV — controllable carrier density.

**Direct vs Indirect Bandgap:**
- Direct bandgap (GaAs, InP): electron transitions conserve momentum — efficient light emission (LEDs, lasers).
- Indirect bandgap (Si, Ge): photon emission requires phonon assistance — poor light emitters but excellent electronic material.

**Why [[silicon]] Dominates:**
1. E_g = 1.12 eV — ideal for room-temperature operation.
2. SiO_2 is a superb native oxide — enables MOS devices.
3. Second most abundant element on Earth — cheap, scalable.
4. Decades of manufacturing infrastructure (CMOS fabs).

**Temperature Dependence:**
- As T increases, n_i increases exponentially.
- At very high T, intrinsic carriers overwhelm any doping — device failure.
- At very low T, freeze-out occurs — carriers recombine.

**Mobility:**
- Electron mobility in Si: ~1350 cm^2/V·s
- Hole mobility in Si: ~480 cm^2/V·s
- Conductivity: σ = q(nμ_n + pμ_p)

## Connections

- [[silicon]] — The dominant semiconductor material, indirect bandgap 1.12 eV.
- [[bandgap]] — Energy difference between conduction and valence band edges; determines intrinsic carrier concentration.
- [[valence-band]] — Highest energy band fully occupied at 0 K; holes reside here.
- [[conduction-band]] — Lowest energy band empty at 0 K; electrons reside here when excited.
- [[semiconductor]] — The class of materials with moderate bandgaps enabling controllable conductivity.
- [[intrinsic-semiconductor]] — A pure, undoped semiconductor where n = p = n_i.
- [[doping]] — Adding impurities to control carrier type and concentration.
- [[germanium]] — First semiconductor used historically (E_g = 0.66 eV), higher leakage than Si.

## Open Questions
- Can wide-bandgap semiconductors (SiC, GaN, 3.3–3.4 eV) fully replace Si in power electronics?
- How does quantum confinement in nanoscale devices alter the bulk band structure?
- What are the fundamental limits of scaling for Si-based transistors?
