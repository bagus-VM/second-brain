---
title: "Band Theory"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[electricity]]"]
---
## One-line Summary
*Band theory explains how electrons in solids occupy continuous ranges of allowed energies (bands) separated by forbidden gaps, which determines whether a material is a conductor, semiconductor, or insulator.*

## Core Intuition
In an isolated atom, electrons sit in discrete energy levels (like rungs on a ladder). When billions of atoms bond in a crystal, those levels spread out into continuous bands — like turning each rung into a broad platform. The gap between platforms (the "forbidden zone") determines everything about electrical behaviour: no gap means electrons flow freely (conductor), a small gap means thermal energy can kick electrons across (semiconductor), and a huge gap means almost nothing gets through (insulator).

## Formal Definition / Statement
In a periodic crystal potential, electrons obey the Bloch theorem and occupy energy bands described by the E(k) dispersion relation. Each band can hold 2N states (where N is the number of unit cells and the factor of 2 accounts for spin). Key bands:

- **Valence band:** Highest energy band that is fully occupied at 0 K
- **Conduction band:** Lowest energy band that is empty at 0 K
- **Bandgap (E_g):** Energy difference between the top of the valence band and the bottom of the conduction band — the "forbidden" energy range where no electron states exist

Classification:
- Conductor: Valence and conduction bands overlap (E_g = 0)
- Semiconductor: 0.1 eV < E_g < 4 eV
- Insulator: E_g > 4 eV

The density of states, Fermi-Dirac distribution, and band structure together determine carrier concentrations and electrical properties.

## Key Properties / Complexity
- **Direct vs indirect bandgap:** In a direct bandgap material (GaAs), the conduction band minimum and valence band maximum occur at the same crystal momentum k — efficient photon emission. In indirect bandgap (Si, Ge), they occur at different k — photon emission requires phonon assistance
- **Effective mass:** Electrons in a band behave as if they have a different mass: m* = ℏ² / (d²E/dk²). This determines mobility and response to fields
- **Fermi level (E_F):** The energy at which the probability of occupation is 1/2 at thermal equilibrium. Positioned differently for conductors, semiconductors, and insulators
- **Density of states:** g(E) describes how many electron states exist per unit energy — determines how many carriers are available at each energy
- **Temperature effects:** As T increases, the Fermi-Dirac distribution broadens, exciting more electrons across the bandgap in semiconductors

## Worked Example
Silicon at 300 K:
- E_g = 1.12 eV (indirect bandgap)
- Thermal energy kT ≈ 0.026 eV
- Ratio E_g / kT ≈ 43 → very few electrons thermally excited across the gap
- n_i = sqrt(N_c × N_v) × exp(−E_g / 2kT) ≈ 1.5 × 10¹⁰ cm⁻³
- N_c ≈ 2.8 × 10¹⁹ cm⁻³ → only about 1 in 10⁹ silicon atoms contributes a conduction electron at room temperature

This shows why silicon is useful: the bandgap is small enough to allow some controllable conduction, but large enough that intrinsic conduction is negligible compared to doped concentrations.

## Common Pitfalls
- Confusing "band" (continuous range of allowed energies) with "orbital" (discrete energy level in a single atom)
- Assuming the bandgap is the only thing that matters — effective mass, density of states, and direct/indirect nature all critically affect device behaviour
- Thinking all semiconductors behave similarly — GaAs, SiC, GaN, and Ge have very different band structures and therefore very different applications
- Forgetting that band theory is a quantum mechanical result — classical physics cannot explain why some materials conduct and others don't

## Connections
- [[semiconductor]] — Materials with moderate bandgaps whose conductivity is tunable
- [[silicon]] — The dominant semiconductor, indirect bandgap 1.12 eV
- [[germanium]] — Smaller bandgap semiconductor (0.66 eV), indirect
- [[bandgap]] — The key parameter of band structure that determines semiconductor behaviour
- [[valence-band]] — The highest fully-occupied band at 0 K
- [[conduction-band]] — The lowest empty band at 0 K where free electrons reside
- [[doping]] — Introduces energy levels within the bandgap to control carrier concentration
- [[electricity]] — Basic electrical concepts that band theory explains at the material level

## Open Questions
- How do quantum confinement effects (in nanowires, quantum dots) modify bulk band structure?
- Can topological insulators offer fundamentally new band structures for electronics?
- What are the limits of band theory for strongly correlated electron systems?
