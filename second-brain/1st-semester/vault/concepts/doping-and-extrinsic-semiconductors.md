---
title: "Doping and Extrinsic Semiconductors"
tags: [concept, microelectronics, physics, semiconductor, doping, semester-1]
course: "Introduction to Microelectronics"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites:
  - semiconductor-physics
  - electron-hole
  - bandgap
---

## One-line Summary
*Doping means adding tiny amounts of specific impurity atoms to silicon to create an excess of either electrons or holes — turning an insulator-like material into a controllable conductor.*

## Core Intuition
Pure silicon at room temperature has so few carriers (1 in 10¹² atoms) that it's practically useless for electronics. Doping is the answer: replace one silicon atom in a million with a phosphorus atom (which has 5 valence electrons instead of 4), and you get a free electron. Do the same with boron (3 valence electrons), and you get a free hole. This is not adding material — it's substituting individual atoms in the crystal lattice. The result is extrinsic semiconductors with carrier concentrations that can be tuned over many orders of magnitude, which is the foundation of every transistor ever built.

## Formal Definition / Statement
Doping is the intentional introduction of impurity atoms into a semiconductor crystal to control its electrical properties.

**n-type doping (donors):**
- Group V elements: P, As, Sb (5 valence electrons)
- 4 electrons bond with Si neighbours, 5th electron is loosely bound
- Donor ionisation energy: E_D ≈ 0.045 eV for P in Si (easily ionized at room temp)
- Result: n ≈ N_D (donor concentration), p = n_i²/N_D (minority holes)
- Fermi level shifts up toward conduction band

**p-type doping (acceptors):**
- Group III elements: B, Al, Ga (3 valence electrons)
- Accepts an electron from the valence band → creates a hole
- Acceptor ionisation energy: E_A ≈ 0.045 eV for B in Si
- Result: p ≈ N_A (acceptor concentration), n = n_i²/N_A (minority electrons)
- Fermi level shifts down toward valence band

**Fermi level position:**
- Intrinsic: E_F = E_i ≈ E_g/2 (midgap)
- n-type: E_F = E_i + kT × ln(N_D/n_i) (shifts up)
- p-type: E_F = E_i - kT × ln(N_A/n_i) (shifts down)
- Heavily doped (>10¹⁹ cm⁻³): E_F enters the band (degenerate semiconductor)

**Doping methods:**
- [[thermal-diffusion]]: high temperature (~1000°C) drives impurity atoms into the wafer
- [[ion-implantation]]: accelerated ions are shot into the surface (more precise, room temp)

## Key Properties / Complexity
- Typical doping range: 10¹⁴ to 10²⁰ atoms/cm³ (vs. ~5×10²² Si atoms/cm³)
- At room temperature, all donors/acceptors are ionized (thermal energy >> 0.045 eV)
- Mass action law still holds: n × p = n_i² regardless of doping
- Compensated doping: if both donors and acceptors are present, net effect is |N_D - N_A|
- Heavy doping effects: bandgap narrowing, increased recombination, Fermi level enters band
- Doping affects mobility: more dopants → more ionized impurity scattering → lower mobility
- Typical fabrication precision: ±1% of target doping concentration

## Worked Example
**Phosphorus doping of silicon, N_D = 10¹⁶ cm⁻³:**

Step 1: Majority carrier concentration (electrons)
  n ≈ N_D = 10¹⁶ cm⁻³

Step 2: Minority carrier concentration (holes) via mass action law
  p = n_i²/n = (1.5 × 10¹⁰)² / 10¹⁶ = 2.25 × 10²⁰ / 10¹⁶ = 2.25 × 10⁴ cm⁻³

Step 3: Fermi level shift
  E_F - E_i = kT × ln(N_D/n_i) = 0.0259 × ln(10¹⁶/1.5×10¹⁰)
            = 0.0259 × ln(6.67×10⁵)
            = 0.0259 × 13.41
            = 0.347 eV

  So E_F is 0.347 eV above midgap, closer to the conduction band — confirming n-type behaviour.

Step 4: Check if fully ionized
  Donor ionisation energy E_D = 0.045 eV >> kT = 0.0259 eV? Not quite, but at room temp the fraction ionized is still ~97% because the density of states in the conduction band is much larger than N_D.

**What if we add boron, N_A = 5×10¹⁵ cm⁻³?**
  Net donor effect: N_D - N_A = 10¹⁶ - 5×10¹⁵ = 5×10¹⁵ cm⁻³
  n ≈ 5×10¹⁵ cm⁻³, p = n_i²/n ≈ 4.5×10⁴ cm⁻³
  Still n-type, but less heavily doped — this is compensated semiconductor.

## Common Pitfalls
- **"n-type means negative charge"**: No — n-type means excess electrons (negative carriers), but the material is electrically neutral overall (donor ions are fixed positive charges in the lattice).
- **Adding dopants increases conductivity forever**: Past ~10²⁰ cm⁻³, solubility limits kick in and dopants form clusters instead of activating. Mobility also drops significantly.
- **Confusing concentration with density**: N_D is in atoms/cm³ (a concentration), not atoms/cm² (areal density). Ion implantation doses are in atoms/cm².
- **Room temperature always means full ionisation**: True for Si with shallow dopants (0.045 eV), but not for wide-bandgap semiconductors like SiC where dopant activation energy can be >0.1 eV.
- **Forgetting minority carriers**: In n-type, holes are rare (2.25×10⁴ cm⁻³) but they're critical for p-n junction physics and BJT operation.

## Connections
- [[semiconductor-physics]] — Doping is how we make semiconductors practical; it controls the carrier concentration
- [[n-type-semiconductor]] — Material with excess electrons from donor atoms
- [[p-type-semiconductor]] — Material with excess holes from acceptor atoms
- [[ion-implantation]] — Modern doping method: high-energy ion beams for precise, room-temperature doping
- [[thermal-diffusion]] — Classical doping method: high-temperature diffusion from gas or solid sources
- [[electron-hole]] — Doping breaks the intrinsic n=p balance, creating one dominant carrier type
- [[p-n-junction]] — The boundary between n-type and p-type material — the fundamental diode
- [[mosfet]] — Source and drain regions are doped regions in the substrate

## Open Questions
- How does retrograde doping (profile that increases with depth) affect transistor performance?
- What happens to carrier concentration when doping approaches the Mott transition?
- How do quantum confinement effects interact with dopant placement at nanometer scales?
