---
title: "Conductor"
tags: [concept, microelectronics, physics, semester-1]
course: "Microelectronics"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*A material with high electrical conductivity due to free charge carriers (typically electrons) that can move easily through the lattice.*

## Core Intuition
Conductors are the highways of electrical circuits — charge flows through them with minimal resistance. Metals are the most common conductors because their atoms share a 'sea' of free electrons. Understanding conductors is fundamental to understanding how circuits work: they connect components, deliver power, and carry signals.

## Formal Definition / Statement
A conductor is a material that allows the flow of electric charge (current) with low resistance.

**Physics of conduction:**
- Metals: outer (valence) electrons are delocalized, forming an 'electron gas'
- Conductivity: σ = n × q × μ (carrier density × charge × mobility)
- For copper: n ≈ 8.5 × 10²⁸ /m³, μ ≈ 0.0032 m²/Vs, σ ≈ 5.96 × 10⁷ S/m

**Key properties:**
- Resistivity (ρ = 1/σ): copper = 1.68 × 10⁻⁸ Ωm
- Temperature coefficient: resistance increases with temperature (α ≈ 0.004/°C for copper)
- Skin effect: at high frequencies, current flows only on the conductor surface
- Electromigration: high current density can physically move atoms, causing failure

**Common conductor materials:**
- Copper (Cu): best balance of conductivity, cost, and manufacturability
- Aluminum (Al): lighter, cheaper, used in IC interconnects and power lines
- Gold (Au): corrosion-resistant, used for contact plating
- Silver (Ag): highest conductivity, expensive

**In ICs:**
- Aluminum interconnects (traditional)
- Copper damascene process (modern, lower resistance)
- Tungsten for vias
- Polysilicon for gate electrodes (not a good conductor but useful for MOS structure)

## Key Properties / Complexity
- Conductivity spans ~25 orders of magnitude from best conductors to best insulators
- Superconductors have zero resistance below a critical temperature
- Resistance: R = ρL/A (resistivity × length / cross-sectional area)
- Power dissipation: P = I²R = V²/R
- Current density: J = I/A (limited by electromigration in ICs)

## Worked Example
Choosing conductor material for an IC interconnect:
- Requirement: carry 1mA through a 1μm × 0.5μm wire, 100μm long
- Aluminum: R = ρL/A = 2.65×10⁻⁸ × 100×10⁻⁶ / (1×10⁻⁶ × 0.5×10⁻⁶) = 5.3Ω
- Copper: R = 1.68×10⁻⁸ × 100×10⁻⁶ / (0.5×10⁻¹²) = 3.36Ω
- Power: P_Al = (1mA)² × 5.3Ω = 5.3μW, P_Cu = 3.36μW
- Copper saves 37% power — why modern ICs use copper interconnects
- Electromigration limit: J_max ≈ 10⁶ A/cm² for copper → max current = 0.5A through this wire (1mA is safe)

## Common Pitfalls
- **Temperature dependence**: Resistance increases with temperature — important for power electronics
- **Skin depth**: At GHz frequencies, current only flows in the outer ~1μm of copper
- **Electromigration**: High current density in IC interconnects causes physical degradation over time
- **Contact resistance**: Conductor-to-conductor interfaces add resistance (oxide, contamination)
- **Via resistance**: Vertical connections (vias) between IC metal layers add significant resistance

## Connections
- [[silicon]] — Silicon is a semiconductor, not a conductor (doped to vary conductivity)
- [[electricity]] — Conductors enable current flow (Ohm's law: V = IR)
- [[capacitor]] — Capacitor plates are conductors
- [[doping]] — Doping silicon makes it more conductor-like
- [[band-theory]] — Conductors have overlapping valence and conduction bands
- [[insulator]] — Opposite of conductor — materials that resist current flow

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
