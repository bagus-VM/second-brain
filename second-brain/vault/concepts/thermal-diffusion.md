---
title: "Thermal Diffusion"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[doping]]", "[[silicon]]"]
---
## One-line Summary
Thermal diffusion is a doping method where silicon wafers are heated in the presence of dopant vapor or solid sources, allowing dopant atoms to diffuse into the crystal — the primary doping method until the 1960s when ion implantation took over.

## Core Intuition
At high temperatures (800-1200°C), silicon atoms vibrate vigorously, creating vacancies and allowing dopant atoms from the surface to slowly migrate (diffuse) deeper into the crystal. The depth of diffusion depends on temperature and time. Higher temperature = faster diffusion. Longer time = deeper diffusion. It's essentially the same physics as dye spreading in water, but in a solid crystal lattice.

## Formal Definition / Statement
Thermal diffusion introduces dopant atoms into silicon by exposing heated wafers to a dopant-containing gas or solid source. The dopant atoms enter the surface and diffuse inward following Fick's laws of diffusion.

**Fick's First Law:** J = -D × (dN/dx)
- J = diffusion flux (atoms/cm²·s)
- D = diffusion coefficient (cm²/s)
- dN/dx = concentration gradient

**Fick's Second Law:** ∂N/∂t = D × (∂²N/∂x²)

**Diffusion Coefficient:** D = D₀ × exp(-EA/kT)
- D₀ = pre-exponential factor (material constant)
- EA = activation energy for diffusion
- k = Boltzmann constant
- T = absolute temperature

The diffusion coefficient increases exponentially with temperature, which is why high temperatures are essential.

Two common diffusion profiles:
- **Constant surface concentration (predeposition):** N(x,t) = Ns × erfc(x / (2√(Dt)))
- **Constant total dose (drive-in):** N(x,t) = (Q / √(πDt)) × exp(-x²/(4Dt))

## Key Properties / Complexity
- **Advantages:**
  - Simple equipment (furnace tube with gas supply)
  - Good uniformity across large wafer batches
  - Lower crystal damage than ion implantation
  - Can create deep junctions efficiently
- **Disadvantages:**
  - Poor dose control compared to ion implantation
  - Requires high temperatures (can affect previously processed layers)
  - Lateral diffusion occurs under mask edges (spreading)
  - Limited to dopant species that have suitable vapor sources
  - Slow process for shallow junctions
- Dopant sources: B₂H₆ (boron), PH₃ (phosphine), AsH₃ (arsine) as gases; BN, P₂O₅ as solids
- Boron diffuses slower than phosphorus in silicon

## Worked Example
Phosphorus diffusion into silicon at 1100°C for 1 hour:
- D at 1100°C ≈ 10⁻¹³ cm²/s (typical for phosphorus)
- Diffusion depth: x ≈ 2√(Dt) = 2√(10⁻¹³ × 3600) = 2√(3.6×10⁻¹⁰) ≈ 0.38 μm
- If surface concentration Ns = 10²⁰ cm⁻³, then at x = 0.38μm: N ≈ Ns × erfc(1) ≈ 0.157 × 10²⁰ = 1.57×10¹⁹ cm⁻³

## Common Pitfalls
- Assuming diffusion depth scales linearly with time — it scales with √t, so doubling time only increases depth by ~41%.
- Ignoring lateral diffusion — dopants diffuse in all directions, not just vertically.
- Forgetting that D depends exponentially on temperature — small temperature changes cause large depth changes.
- Not accounting for solid solubility limits — there's a maximum dopant concentration achievable at each temperature.

## Connections
- Alternative to [[ion-implantation]] for introducing dopants into [[silicon]].
- Both are forms of [[doping]] used in semiconductor fabrication.
- Used before [[photolithography]] patterned specific regions.
- Drive-in diffusion often follows a predeposition step.

## Open Questions
- How do diffusion profiles change with non-uniform initial conditions?
- What role does oxidation-enhanced diffusion play in modern processing?
