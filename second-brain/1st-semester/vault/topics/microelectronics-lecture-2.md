---
title: "Doping and Extrinsic Semiconductors"
tags: [topic, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[microelectronics-lecture-1]]", "[[intrinsic-semiconductor]]"]
---

## One-line Summary
[[doping]] is the deliberate introduction of impurity atoms into a [[semiconductor]] crystal to control its electrical conductivity, creating [[n-type-semiconductor]] or [[p-type-semiconductor]] materials with vastly more carriers than the intrinsic material.

## Core Intuition
An [[intrinsic-semiconductor]] has very few carriers at room temperature — too few for practical devices. Doping solves this by replacing a tiny fraction of host atoms with atoms that have one more or one fewer valence electron. A Group V atom (P, As, Sb) in silicon donates an extra electron → [[n-type-semiconductor]]. A Group III atom (B, Al, Ga) creates a missing electron (hole) → [[p-type-semiconductor]]. The crystal stays electrically neutral, but the carrier concentration jumps by orders of magnitude, making the material useful for building transistors and diodes.

## Formal Definition / Statement
In a doped [[semiconductor]], the carrier concentrations satisfy the mass-action law:

    n × p = n_i^2

For an [[n-type-semiconductor]] with donor concentration N_D >> n_i:

    n ≈ N_D,   p = n_i^2 / N_D

For a [[p-type-semiconductor]] with acceptor concentration N_A >> n_i:

    p ≈ N_A,   n = n_i^2 / N_A

When both donors and acceptors are present (compensation):

    n - p = N_D - N_A,   n × p = n_i^2

Donor ionization energy (Si:P): E_d ≈ E_c - 0.045 eV (shallow donor).
Acceptor ionization energy (Si:B): E_a ≈ E_v + 0.045 eV (shallow acceptor).

## Key Properties / Complexity

**Types of Dopants in Silicon:**
| Dopant | Type | Group | Role |
|--------|------|-------|------|
| Phosphorus (P) | n-type | V | Donates electron |
| Arsenic (As) | n-type | V | Donates electron |
| Antimony (Sb) | n-type | V | Donates electron |
| Boron (B) | p-type | III | Accepts electron (creates hole) |
| Aluminum (Al) | p-type | III | Accepts electron |
| Gallium (Ga) | p-type | III | Accepts electron |

**Doping Concentration Ranges:**
- Light doping: 10^14 – 10^16 cm^-3 (used in substrate, channel regions)
- Moderate doping: 10^16 – 10^18 cm^-3 (used in wells, drift regions)
- Heavy doping (n+ or p+): 10^18 – 10^21 cm^-3 (used in source/drain, contacts)

**Fabrication Methods:**

1. **[[thermal-diffusion]]:** Wafer heated to 900–1200°C in presence of dopant gas (PH_3, BCl_3). Dopants diffuse into crystal. Gaussian or complementary error function profile. Used for deep, uniform doping. Older technique, less precise.

2. **[[ion-implantation]]:** Dopant ions accelerated to keV–MeV energies and shot into wafer. Precise dose control (ions/cm^2), can use [[photolithography]] to mask regions. Creates lattice damage requiring annealing. Gaussian distribution centered at projected range R_p. Modern standard.

3. **In-situ doping:** Dopants added during epitaxial growth. Very uniform, low defect density.

**Effect on Fermi Level:**
- More n-type doping → E_F moves closer to E_c.
- More p-type doping → E_F moves closer to E_v.
- At extreme doping (>10^19), the semiconductor becomes degenerate (metallic).

## Connections

- [[n-type-semiconductor]] — Material with electron majority carriers from donor atoms.
- [[p-type-semiconductor]] — Material with hole majority carriers from acceptor atoms.
- [[doping]] — The process of adding impurity atoms to control conductivity.
- [[ion-implantation]] — Modern doping technique using accelerated ions.
- [[thermal-diffusion]] — Older doping technique using high-temperature diffusion.
- [[photolithography]] — Patterning technique that defines where doping occurs.
- [[intrinsic-semiconductor]] — The pure, undoped starting material.
- [[microelectronics-lecture-1]] — Foundation of band structure and carrier statistics.
- [[p-n-junction]] — Formed when n-type and p-type regions meet.

## Open Questions
- How does random dopant fluctuation (RDF) affect nanoscale transistor variability?
- What are the limits of ultra-high doping before crystal integrity is lost?
- Can 2D materials be doped as reliably as silicon?
