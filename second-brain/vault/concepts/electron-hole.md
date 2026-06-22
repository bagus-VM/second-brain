---
title: "Electron Hole"
tags: [concept, microelectronics, physics, semiconductor, semester-1]
course: "Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites:
  - band-theory
  - valence-band
  - conduction-band
---
## One-line Summary
*A hole is the absence of an electron in the valence band that behaves like a positively charged particle with positive effective mass.*

## Core Intuition
When an electron is kicked out of the valence band into the conduction band, it leaves behind an empty state — a hole. Instead of tracking every remaining electron in a nearly-full band (an impossible many-body problem), we track the one missing electron as if it were a real particle. The hole has positive charge (+e), positive effective mass, and responds to electric fields in the opposite direction of electrons. This is not a metaphor — in the valence band, a hole genuinely behaves as a mobile carrier. It is the key to understanding why semiconductors conduct current through two carrier types, not just one.

## Formal Definition / Statement
An electron hole is a quasiparticle representing the absence of an electron in an otherwise filled valence band. It is characterized by:

- **Charge:** +e (positive elementary charge)
- **Effective mass:** m*_h (positive, typically heavier than electron effective mass in silicon: m*_h ≈ 0.56 m₀ vs m*_e ≈ 0.26 m₀ for conductivity)
- **Location:** Valence band
- **Generation:** When thermal energy or photon absorption promotes an electron from valence to conduction band (electron-hole pair generation)
- **Recombination:** When a conduction-band electron falls back into the hole, annihilating both carriers

The hole concept is valid because the valence band is nearly full. An empty state in a nearly-full band can be mathematically described as a positively charged particle with positive effective mass. The effective mass of the hole is determined by the curvature of the valence band at the top:

    m*_h = ℏ² / (d²E/dk²) at k = 0 (top of valence band)

Since the valence band curves downward, d²E/dk² is negative, and the hole mass (defined with opposite sign convention) is positive.

**Hole current:** In an electric field E, holes drift in the direction of the field (opposite to electron drift), contributing a current density:

    J_h = e · p · μ_h · E

where p = hole concentration, μ_h = hole mobility.

## Key Properties / Complexity
- Hole charge: +e (same magnitude as electron, opposite sign)
- Hole effective mass: larger than electron effective mass in most semiconductors → holes move slower
- Hole mobility (μ_h) is lower than electron mobility (μ_e) in silicon: ~480 vs ~1350 cm²/Vs
- Holes exist in the valence band; electrons exist in the conduction band
- Thermal generation creates electron-hole pairs (EHPs) — always generated and annihilated in pairs
- In intrinsic silicon: n = p = n_i ≈ 1.5 × 10¹⁰ cm⁻³ at 300K
- In extrinsic semiconductors: doping breaks the n = p symmetry
  - n-type: n >> p (electrons dominate)
  - p-type: p >> n (holes dominate)

## Worked Example
Silicon at 300K, intrinsic carrier concentration n_i = 1.5 × 10¹⁰ cm⁻³:

**Intrinsic silicon:**
- Electron concentration: n = n_i = 1.5 × 10¹⁰ cm⁻³
- Hole concentration: p = n_i = 1.5 × 10¹⁰ cm⁻³
- Mass action law: n · p = n_i² = 2.25 × 10²⁰ cm⁻⁶
- Both carriers contribute equally to current

**After doping with phosphorus (n-type, N_D = 10¹⁶ cm⁻³):**
- Electrons: n ≈ N_D = 10¹⁶ cm⁻³ (from donors)
- Holes: p = n_i² / n = (2.25 × 10²⁰) / (10¹⁶) = 2.25 × 10⁴ cm⁻³
- Ratio: n/p ≈ 4.4 × 10¹¹ — electrons overwhelmingly dominate
- Hole current is negligible, but holes still exist and are critical for device physics (e.g., minority carrier injection in BJTs)

## Common Pitfalls
- **Holes are not positrons**: They are quasiparticles in a crystal, not antiparticles. They arise from the band structure of a periodic lattice.
- **Holes are not protons**: Despite having +e charge, holes are not protons. They are missing electrons in a specific band.
- **"Holes move" is shorthand**: What actually moves is the rearrangement of many-electron wavefunctions in the valence band. The net effect is equivalent to a +e particle moving.
- **Hole mass ≠ electron mass**: The effective mass depends on band curvature. Holes are typically heavier than electrons in silicon, which is why μ_h < μ_e.
- **np = n_i² always holds** in thermal equilibrium regardless of doping — this is the mass action law and is a frequent exam target.
- **Don't confuse hole concentration with acceptor concentration**: In p-type material, p ≈ N_A only when N_A >> n_i. At high temperatures, intrinsic generation can dominate.

## Connections
- [[valence-band]] — Holes exist at the top of the valence band; band curvature determines hole effective mass
- [[conduction-band]] — Electron-hole pair generation promotes an electron from valence to conduction band
- [[band-theory]] — The quasiparticle concept of holes is a direct consequence of band structure in periodic potentials
- [[bandgap]] — Bandgap energy determines intrinsic carrier concentration and thus equilibrium hole density
- [[intrinsic-semiconductor]] — In intrinsic material, n = p = n_i; holes and electrons are perfectly balanced
- [[doping]] — Doping breaks the electron-hole balance; acceptors create p-type material dominated by holes
- [[mosfet]] — Hole current in p-channel MOSFETs; hole inversion layer formation
- [[mosfet-operating-regions]] — Inversion requires minority carrier (hole) accumulation at the surface in n-substrate

## Open Questions
- How does hole velocity saturation differ from electron velocity saturation at high fields?
- What is the role of heavy holes vs light holes (split valence bands) in realistic semiconductor modeling?
- How does the hole concept extend to direct vs indirect bandgap semiconductors?
