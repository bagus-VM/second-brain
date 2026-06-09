---
title: "Etching in Semiconductor Fabrication"
tags: [concept, microelectronics, fabrication, semester-1]
course: "Microelectronics"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*The process of selectively removing material from a wafer surface using chemical or physical methods to create circuit patterns.*

## Core Intuition
After photolithography defines where the pattern should be, etching actually removes the material. Think of it like sculpting: lithography draws the outline on the stone, and etching chisels away everything outside the outline. The challenge is etching precisely — removing only the intended material, at the intended depth, with vertical sidewalls and no undercutting.

## Formal Definition / Statement
Etching removes unprotected material from a wafer surface during IC fabrication.

**Types:**

1. **Wet etching** (chemical):
   - Immersion in liquid chemical etchant
   - Isotropic: etches equally in all directions (undercuts the mask)
   - Selective: different etchants for different materials
   - Examples: HF for SiO₂, H₃PO₄ for Si₃N₄, KOH for Si
   - Simple, cheap, but poor dimensional control

2. **Dry etching** (physical/chemical):
   - **Plasma etching**: Reactive ion species in a plasma
   - **RIE (Reactive Ion Etching)**: combines chemical reaction with physical ion bombardment
   - **DRIE (Deep RIE)**: Bosch process for deep silicon etching
   - Anisotropic: preferentially etches vertically (vertical sidewalls)
   - Better dimensional control than wet etching

3. **Ion milling** (purely physical):
   - Energetic ions physically sputter material
   - Very anisotropic but low selectivity

**Key parameters:**
- Etch rate: nm/min (determines throughput)
- Selectivity: ratio of etch rates for target vs mask vs underlying layer
- Anisotropy: ratio of vertical to lateral etch rate
- Uniformity: variation across the wafer
- Profile: sidewall angle (vertical = ideal)

## Key Properties / Complexity
- Wet etch is isotropic (undercuts mask by the etch depth)
- RIE is anisotropic (vertical sidewalls, minimal undercut)
- Selectivity: RIE can achieve >10:1 selectivity between materials
- Etch rate: wet etch ~100nm–1μm/min, RIE ~10–500nm/min
- The Bosch process alternates etching and passivation for deep trenches
- Endpoint detection: optical or mass spectrometry signals indicate when to stop etching

## Worked Example
Etching a gate oxide window:
1. Wafer: Si with 500nm SiO₂ layer
2. Photoresist pattern defines window where oxide should be removed
3. Wet etch option: dip in buffered HF (BOE)
   - Etch rate: ~100nm/min
   - Time: 5 minutes for 500nm
   - Result: isotropic undercut ~500nm on each side
4. RIE option: CHF₃/Ar plasma
   - Etch rate: ~200nm/min
   - Time: 2.5 minutes
   - Result: vertical sidewalls, minimal undercut (<50nm)
5. RIE is preferred for sub-micron features; wet etch is fine for large features

## Common Pitfalls
- **Undercut**: Wet etching removes material under the mask, widening the feature
- **Loading effect**: Dense patterns etch slower than isolated patterns (reactant depletion)
- **Microloading**: Small features etch differently than large features in the same area
- **Etch stop**: Incomplete etching leaves residual material
- **Damage**: Ion bombardment in RIE can damage the underlying layer
- **Selectivity limits**: No etchant is perfectly selective; some mask or substrate material is always removed

## Connections
- [[mask-alignment]] — Etching follows lithography; mask alignment determines pattern placement
- [[ion-implantation]] — Ion implantation may use etched features as masks
- [[thermal-diffusion]] — Diffusion uses oxide masks created by etching
- [[silicon]] — Silicon is the primary material being etched
- [[doping]] — Etched patterns define doped regions
- [[mosfet]] — Gate, source, and drain regions are defined by etching

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
