---
title: "Photolithography"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[doping]]", "[[ion-implantation]]"]
---
## One-line Summary
Photolithography is the pattern-transfer process in semiconductor fabrication that uses light to selectively expose a photosensitive resist through a mask, enabling selective doping, etching, or deposition on specific regions of the wafer.

## Core Intuition
Think of it as photographic printing on silicon. You coat the wafer with a light-sensitive chemical (photoresist), project a pattern through a mask using UV light, and develop the resist — the exposed (or unexposed, depending on resist type) areas wash away. The remaining resist pattern acts as a stencil: dopants can only reach the silicon where resist has been removed, or etchants only attack exposed areas. Multiple lithography steps build up the complete circuit layer by layer.

## Formal Definition / Statement
Photolithography is the process of transferring geometric patterns from a photomask to a light-sensitive photoresist on the wafer surface. It is the enabling technology for defining the physical features of integrated circuits.

**Process Steps:**
1. **Surface Preparation:** Clean wafer, dehydrate bake
2. **Photoresist Application (Spin Coating):** Spin wafer at 3000-6000 RPM to spread a thin, uniform resist layer (~1μm)
3. **Soft Bake:** Remove resist solvents, improve adhesion
4. **Alignment and Exposure:** Align mask to wafer features, expose to UV light through the mask
5. **Development:** Dissolve exposed (positive resist) or unexposed (negative resist) areas
6. **Hard Bake:** Strengthen resist for subsequent processing
7. **Etch or Implant:** Use resist pattern as mask for etching or ion implantation
8. **Resist Strip:** Remove remaining resist after processing

**Photoresist Types:**
- **Positive resist:** Exposed areas become soluble (developer removes them). Higher resolution.
- **Negative resist:** Unexposed areas become soluble. Better adhesion, lower resolution.

## Key Properties / Complexity
- **Resolution limit:** Minimum feature size ≈ λ / (2 × NA), where NA is the numerical aperture of the lens system
- **Deep UV (DUV):** 248nm (KrF) and 193nm (ArF) wavelengths for modern processes
- **Extreme UV (EUV):** 13.5nm wavelength for sub-7nm nodes
- **Contact printing:** Mask touches wafer (high resolution, mask damage)
- **Projection printing:** Mask imaged through optics (most common, no mask damage)
- **Stepper vs. Scanner:** Stepper exposes one die at a time; scanner scans across the die
- Critical dimension (CD): The smallest feature that can be reliably printed
- Overlay accuracy: How well successive mask layers align to each other
- Multiple patterning: Using multiple exposures to achieve features smaller than the wavelength limit

## Worked Example
Patterning a gate oxide mask for nMOS transistors:
1. Wafer coated with 1μm positive photoresist at 4000 RPM
2. Mask with gate pattern aligned to existing source/drain features
3. Exposed to 248nm UV light through the mask (dose: 30 mJ/cm²)
4. Developed: exposed resist dissolves, leaving resist window where gate will be defined
5. Ion implantation through the resist window defines the channel doping
6. After implant, resist is stripped with O₂ plasma ashing
7. Result: selective doping only where the gate window was opened

## Common Pitfalls
- Contamination (particles) at any step can ruin the pattern — cleanroom environment essential.
- Under-exposure or over-exposure changes the feature size (CD variation).
- Poor alignment between layers causes device failure (overlay errors).
- Resist thickness non-uniformity causes exposure dose variation across the wafer.
- Standing wave effects in the resist cause linewidth variation (anti-reflective coatings help).

## Connections
- Enables selective [[ion-implantation]] and [[thermal-diffusion]] by defining doped regions.
- Core [[doping]] pattern-definition technique.
- Used at every layer of IC fabrication: active area, gate, contacts, metal interconnects.
- Resolution limits drive the need for shorter wavelengths (DUV → EUV).
- Related to [[mask-alignment]] and [[etching]] processes.

## Open Questions
- What comes after EUV lithography as feature sizes shrink below 3nm?
- How do computational lithography techniques compensate for optical limitations?
- Can directed self-assembly (DSA) supplement or replace optical lithography?
