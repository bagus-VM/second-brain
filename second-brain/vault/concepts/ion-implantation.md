---
title: "Ion Implantation"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[doping]]", "[[silicon]]"]
---
## One-line Summary
Ion implantation is a doping technique that uses an electron gun to accelerate dopant ions to high energy and shoot them into the silicon wafer, offering precise control of dose and depth but causing crystal damage that requires annealing.

## Core Intuition
Instead of relying on heat to diffuse dopants into silicon (as in thermal diffusion), ion implantation physically hurls dopant atoms into the crystal at high velocity. The kinetic energy determines how deep the ions penetrate, and the beam current × time determines how many ions are implanted (dose). This gives much finer control but knocks silicon atoms out of their crystal lattice in the process.

## Formal Definition / Statement
Ion implantation is a process in which ionized dopant atoms are accelerated through an electric field (typically 5-500 keV) and directed at a silicon wafer surface. The ions embed themselves in the crystal at a controlled depth.

Key process parameters:
- **Dose (Φ):** Number of ions per unit area (ions/cm²). Controls the dopant concentration.
- **Energy (E):** Kinetic energy of ions in keV. Controls the implantation depth (projected range Rp).
- **Projected Range (Rp):** Average depth ions penetrate. Increases with energy, depends on ion mass and target material.
- **Straggle (ΔRp):** Statistical spread of ion depths around Rp (standard deviation of the distribution).

The implanted ion profile is approximately Gaussian:
n(x) = (Φ / (ΔRp × √(2π))) × exp(-(x - Rp)² / (2ΔRp²))

## Key Properties / Complexity
- **Advantages over thermal diffusion:**
  - Precise dose control (measured by beam current × time)
  - Precise depth control (set by accelerating voltage)
  - Can implant through thin layers (oxide, photoresist masks)
  - Works at room temperature (no high-temp processing needed)
  - Can implant any element, not just common dopants
- **Disadvantages:**
  - Causes crystal lattice damage (displaced silicon atoms)
  - Requires annealing (800-1000°C) to repair lattice and activate dopants
  - Channeling: ions can travel deep along crystal axes if wafer is aligned
  - Equipment is expensive and complex
- Masks: Photoresist or oxide layers can block implantation in selected areas
- Amorphization: Heavy implants can make the surface layer amorphous (non-crystalline)

## Worked Example
Boron implant into silicon:
- Energy: 100 keV → Rp ≈ 0.3 μm, ΔRp ≈ 0.07 μm
- Dose: 10¹⁵ ions/cm²
- Peak concentration at x = Rp: n(Rp) = 10¹⁵ / (0.07×10⁻⁴ × √(2π)) ≈ 5.7 × 10¹⁹ cm⁻³
- After annealing: dopants activated, lattice repaired, resulting in a P-type doped region

## Common Pitfalls
- Forgetting annealing — implanted ions are not electrically active until the lattice is repaired.
- Ignoring channeling — tilting the wafer (7° typical) prevents ions from channeling deep along crystal planes.
- Confusing dose (total ions/cm²) with concentration (ions/cm³) — they're related by the distribution profile.
- Not accounting for mask penetration — ions may pass through thin mask edges (straggle).

## Connections
- Alternative to [[thermal-diffusion]] for introducing dopants into [[silicon]].
- Used to set [[threshold-voltage]] by implanting the channel region.
- Part of the [[photolithography]] process flow (implant through patterned masks).
- Fundamental [[doping]] technique in modern IC fabrication.

## Open Questions
- How does multi-energy implantation create complex doping profiles?
- What are the limits of ion implantation for ultra-shallow junctions?
