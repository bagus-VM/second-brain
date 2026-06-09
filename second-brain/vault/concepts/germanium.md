---
title: "Germanium"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: draft
last_updated: 2026-06-04
prerequisites: ["[[semiconductor]]", "[[silicon]]"]
---

## One-line Summary
*Germanium was the first semiconductor used in transistors but was largely replaced by silicon due to its higher leakage current and lack of a stable native oxide.*

## Core Intuition
Germanium (Ge) was the material that started the semiconductor revolution — the first transistor (1947, Bell Labs) was made from Ge. It has a smaller bandgap (0.66 eV vs silicon's 1.12 eV), which means it conducts more easily but also leaks more at room temperature. Its oxide (GeO₂) is water-soluble and unstable, so it couldn't support the MOS technology that made silicon dominant. Today germanium is making a comeback in high-speed transistors (strained SiGe channels) and photodetectors (for infrared light).

## Formal Definition / Statement
Germanium (Ge) is a group-IV element with electron configuration [Ar] 3d¹⁰ 4s² 4p². Like silicon, it crystallizes in the diamond cubic lattice with 4 valence electrons forming covalent bonds. Key parameters:

- Bandgap: E_g = 0.66 eV at 300 K (vs 1.12 eV for Si)
- Intrinsic carrier concentration: n_i ≈ 2.4 × 10¹³ cm⁻³ at 300 K (much higher than Si's 1.5 × 10¹⁰)
- Electron mobility: ~3900 cm²/V·s (higher than Si's ~1350)
- Hole mobility: ~1900 cm²/V·s (higher than Si's ~480)
- Crystal structure: Diamond cubic, lattice constant 5.658 Å

## Key Properties / Complexity
- **Smaller bandgap (0.66 eV):** More intrinsic carriers at room temperature → higher leakage current in devices
- **Higher carrier mobility:** Both electrons and holes move faster in Ge than in Si — attractive for high-speed applications
- **Poor native oxide:** GeO₂ is water-soluble and thermally unstable — cannot form a reliable gate insulator for MOS devices
- **Historical significance:** First transistor material (Bardeen, Brattain, Shockley, 1947–48)
- **Modern revival:** Used in SiGe heterojunction bipolar transistors (HBTs) for RF, strained-channel MOSFETs, and photodetectors for telecom wavelengths (1.3–1.55 μm)
- **Doping:** Same dopants as silicon — Group V (P, As, Sb) for n-type, Group III (B, Al, Ga) for p-type

## Worked Example
Comparing intrinsic carrier concentration at 300 K:
- Germanium: n_i = sqrt(N_c × N_v) × exp(−E_g / 2kT) ≈ 2.4 × 10¹³ cm⁻³
- Silicon: n_i ≈ 1.5 × 10¹⁰ cm⁻³

This ~1600× difference means a germanium diode at room temperature already has significant conduction, while a silicon diode is essentially off. This is why silicon replaced germanium — it has much better on/off contrast for digital switching.

## Common Pitfalls
- Assuming germanium is "obsolete" — it's critical in modern SiGe heterojunction devices
- Forgetting that the smaller bandgap means much higher leakage — germanium devices get "leaky" at elevated temperatures
- Confusing GeO₂ (unstable, water-soluble) with SiO₂ (extremely stable, glass) — this single difference shaped the entire semiconductor industry

## Connections
- [[silicon]] — The semiconductor that replaced germanium for most applications
- [[semiconductor]] — Germanium is a textbook semiconductor with moderate bandgap
- [[band-theory]] — Germanium's bandgap (0.66 eV) and indirect band structure explain its properties
- [[doping]] — Germanium is doped with the same Group III/V elements as silicon
- [[diode]] — Early germanium diodes had lower forward voltage (~0.3 V) but higher leakage
- [[p-n-junction]] — The physics of germanium junctions is identical to silicon, just with different parameters

## Open Questions
- Can germanium's native oxide problem be solved with high-κ dielectrics to enable Ge MOSFETs?
- Will Ge or GeSn alloys replace silicon for channel materials below 3 nm nodes?
- How does germanium's higher mobility compare to III-V compounds (InGaAs) for future logic?
