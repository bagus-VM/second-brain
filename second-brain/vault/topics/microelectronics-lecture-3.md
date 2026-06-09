---
title: "P-N Junction Overview"
tags: [topic, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[microelectronics-lecture-2]]", "[[microelectronics-lecture-1]]"]
---

## One-line Summary
A [[p-n-junction]] forms when p-type and n-type semiconductor regions meet, creating a built-in electric field in the [[depletion-region]] that enables current to flow in one direction — the fundamental mechanism behind every [[diode]] and transistor.

## Core Intuition
When you press p-type and n-type silicon together, holes from the p-side and electrons from the n-side rush toward the junction and recombine, leaving behind fixed ionized dopant atoms (positive on n-side, negative on p-side). This exposed charge creates an electric field — the built-in potential V_bi — that opposes further diffusion. Equilibrium is reached when diffusion current equals drift current. Applying forward bias (positive to p, negative to n) lowers this barrier and allows current. Reverse bias widens the barrier and blocks current. This asymmetry is the basis of all semiconductor devices.

## Formal Definition / Statement
The built-in potential of a [[p-n-junction]] is:

    V_bi = (kT/q) × ln(N_A × N_D / n_i^2)

The [[depletion-region]] width under zero bias:

    W = sqrt(2ε_s(V_bi) × (1/N_A + 1/N_D) / q)

where ε_s is the semiconductor permittivity. The depletion width extends more into the lightly-doped side.

**Diode equation (ideal):**

    I = I_s × [exp(qV / nkT) - 1]

where I_s is the reverse saturation current, n is the ideality factor (1–2), V is the applied voltage.

## Key Properties / Complexity

**Junction Formation and Equilibrium:**
1. Electrons diffuse from n→p, holes diffuse from p→n.
2. Recombination near junction exposes fixed donor (+) and acceptor (−) ions.
3. Electric field E builds up opposing further diffusion.
4. Equilibrium: J_diffusion + J_drift = 0.

**Biasing Conditions:**

| Condition | Barrier | Current | Depletion Width |
|-----------|---------|---------|-----------------|
| Zero bias | V_bi | Zero (net) | W_0 |
| Forward bias (V > 0) | V_bi − V | Exponential increase | Narrows |
| Reverse bias (V < 0) | V_bi + |V| | ≈ −I_s (tiny) | Widens |

**Breakdown Mechanisms:**

1. **[[avalanche-breakdown]]:**
   - Occurs in lightly-doped (wide depletion region) junctions.
   - Reverse bias accelerates carriers to high kinetic energy.
   - Impact ionization: a fast carrier knocks out electron-hole pairs.
   - Chain reaction → exponential current increase.
   - Typically at V_BR > 6 V for Si.
   - Positive temperature coefficient (V_BR increases with T).

2. **[[zener-breakdown]]:**
   - Occurs in heavily-doped (narrow depletion region) junctions.
   - Strong electric field (~10^6 V/cm) directly breaks covalent bonds.
   - Quantum mechanical tunneling of electrons across the narrow barrier.
   - Typically at V_BR < 5 V for Si.
   - Negative temperature coefficient (V_BR decreases with T).

**Practical Diode Effects:**
- **Forward voltage drop:** ~0.7 V (Si), ~0.3 V (Ge), ~1.5 V (GaAs).
- **Reverse leakage current:** due to minority carriers and generation in depletion region.
- **Junction capacitance:** C_j = ε_s × A / W — varies with bias (varactor effect).
- **Diffusion capacitance:** C_d — due to minority carrier storage in forward bias.

## Connections

- [[p-n-junction]] — The boundary between p-type and n-type regions; the fundamental diode structure.
- [[depletion-region]] — The charge-free zone at the junction where the built-in electric field exists.
- [[diode]] — A two-terminal device based on the p-n junction that conducts current in one direction.
- [[avalanche-breakdown]] — High-voltage breakdown from impact ionization in lightly-doped junctions.
- [[zener-breakdown]] — Low-voltage breakdown from quantum tunneling in heavily-doped junctions.
- [[microelectronics-lecture-2]] — How the p and n regions are created.
- [[zener-diode]] — A diode specifically designed to operate safely in breakdown for voltage regulation.
- [[transistor]] — Built from two p-n junctions (BJT) or uses junction fields (MOSFET).

## Open Questions
- How does trap-assisted tunneling affect leakage in ultra-thin junctions?
- What determines the boundary between Zener and avalanche mechanisms?
- How do heterojunctions (e.g., GaAs/AlGaAs) modify the junction physics?
