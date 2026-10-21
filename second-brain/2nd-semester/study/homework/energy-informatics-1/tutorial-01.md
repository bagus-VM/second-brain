---
title: "Tutorial 1 — Solutions (discussion 20/22 Oct 2026)"
tags: [homework, energy-informatics, semester-2]
course: "Energy Informatics I"
source_count: 2
status: current
last_updated: 2026-10-19
---

# Energy Informatics I — Tutorial 1 solutions

Source: `Tutorial_1.pdf` (Bettermann/Gagin), lecture `EnInf_I_0.Motivation.pdf`.
Discussed 20 October and 22 October 2026.

---

## Task 1 — Alternating current

### One-line answers

- **a)** AC is a sinusoid: `u(t) = Û · sin(ωt + φ)`, with `ω = 2πf`.
- **b)** Amplitude = the peak value Û. Period T = time for one full cycle. Frequency f = 1/T, measured in Hz.
- **c)** A sine wave with Û marked on the vertical axis and T on the horizontal axis.
- **d)** `U_rms = Û/√2 ≈ 0.7071 · Û` for a sinusoid.
- **e)** German outlets: **230 V RMS**, so peak = 230 · √2 = **≈ 325.3 V** (peak-to-peak ≈ 650.5 V), at 50 Hz (T = 20 ms).

### a) Modelling AC as a function of time

Voltage and current are both sinusoids of the same frequency (for a linear load):

```
u(t) = Û · sin(ωt + φ_u)
i(t) = Î  · sin(ωt + φ_i)
```

where Û/Î are the peak values, ω = 2πf is the angular frequency, and φ is the phase. The grid is a three-phase system: three such sinusoids offset by 120° (2π/3).

### b) The three terms

| Term | Meaning | Relation |
|------|---------|----------|
| Amplitude value Û | maximum absolute value the signal reaches | — |
| Period T | duration of one complete cycle | T = 1/f |
| Frequency f | cycles per second | f = 1/T [Hz] |

Angular frequency ω = 2πf [rad/s] is the parameter that actually appears in the sine.

### c) Graph

```
 u
 Û|      ....              ....
  |    .      .          .      .
  |   .        .        .        .
 0|--+---------+-------+----------+-----> t
  |  .          .     .            .
-Û| .            .....              .
  |<--- T --->|
  |<--- T --->|
```

### d) RMS voltage — derivation

RMS ("root mean square") is the DC voltage that would deliver the same average power into a resistor. For a periodic signal:

```
U_rms = sqrt( (1/T) · ∫₀ᵀ u²(t) dt )
```

Step by step for `u(t) = Û sin(ωt)` over one period:

1. **Square it:** `u²(t) = Û² sin²(ωt)`.
2. **Linearise:** `sin²(ωt) = (1 − cos(2ωt)) / 2`, so `u²(t) = (Û²/2)(1 − cos(2ωt))`.
3. **Integrate:** the cosine term completes two full cycles over T, so its integral is zero:
   `∫₀ᵀ u² dt = (Û²/2) · T`.
4. **Mean, then root:** `U_rms = sqrt( (Û²/2 · T)/T ) = Û/√2 ≈ 0.7071 · Û`.

The √2 is not a magic constant: it is exactly what the vanishing `cos(2ωt)` term leaves behind.

### e) German residential outlets

Germany uses **230 V** — that number is already the RMS value, not the peak:

```
Û = U_rms · √2 = 230 V · 1.41421 = 325.27 V
U_peak-to-peak = 2 · 325.27 V ≈ 650.5 V
T = 1/f = 1/50 Hz = 20 ms
```

**Exam trap:** equipment insulation is rated against the *peak*, not the RMS value. 230 V is the figure on the label; 325 V is the figure the capacitor sees.

---

## Task 2 — Sector coupling

### One-line answers

- **a)** Sector coupling links electricity, heat, gas, and transport so energy can be converted and shifted between them under one integrated management.
- **b)** It adds flexibility and storage, absorbs renewable surpluses, and decarbonises heat and transport.
- **c)** It costs conversion losses, capital, complexity, and creates a hard dependency on ICT.
- **d)** *Real* conversion physically changes energy form (power-to-gas via electrolysis); *virtual* conversion changes the operating point of an existing plant (shifting the electricity/heat ratio of a CHP).

### a) The concept

> Interoperability between the energy systems (electricity, gas, thermal), with integrated energy management in distributed systems, to increase efficiency, flexibility, and stability of the combined sectors.

Energy conversion between sectors (real and virtual) and additional storage capacity (real and virtual) are what make the coupling useful. The lecture's diagram shows the electricity network, gas network, district heating/cooling networks, and the transport network connected through electrolysers, heat pumps, CHPs, batteries, and hydrogen storage.

### b) Advantages

- **Extra flexibility**: loads and generators from other sectors can be shifted to balance the electricity grid.
- **Storage without new electricity storage**: gas and heat networks already store energy; power-to-gas and heat storage extend that capacity to electricity.
- **Absorbing renewable surplus**: otherwise-curtailed wind/solar becomes hydrogen, heat, or synthetic fuel.
- **Efficiency**: waste heat from generation or from computing (e.g. the RENergetic project feeding supercomputer waste heat into district heating) is reused rather than dumped.
- **Decarbonising heat and transport**, which cannot be electrified directly everywhere.
- **New business models**: smart meter operators, charging-point operators, energy communities.

### c) Disadvantages

- **Conversion losses**: every conversion (electricity → hydrogen → electricity) loses energy. Round trips are poor, so sector coupling trades quantity for flexibility.
- **Capital cost and complexity**: electrolysers, heat pumps, and coupling infrastructure are expensive; the control problem grows with the number of coupled sectors.
- **ICT dependency — the lecture's own warning.** In the future smart grid, many participants connect through ICT, so an ICT failure becomes a grid failure. ICT-based control must be fail-safe. The reverse also holds: power-quality events (overvoltage) can damage ICT infrastructure, so ICT needs its own protection.
- **Regulatory and market barriers**: electricity, gas, and heat are regulated separately; cross-sector tariffs and ownership rules are unresolved.
- **Lock-in risk**: coupling couples failures too.

### d) Real vs virtual conversion

| | Real conversion | Virtual conversion |
|---|---|---|
| Mechanism | energy physically changes form | the operating point of an existing multi-output plant changes |
| Example | power-to-gas: electrolysis turns electricity into hydrogen | changing the conversion rate between electricity and heat in a Combined Heat and Power plant |
| Storage analogue | battery, pumped hydro | demand shifting |
| Cost | new hardware | control and market design |

**The distinction in one sentence:** real conversion adds a device; virtual conversion changes how an existing device is run.

---

## Task 3 — Assumptions and implications of the power grid

### One-line answers

- **a)** Yes. Nominal frequency is 50 Hz in Europe; load > generation lowers it, load < generation raises it.
- **b)** Demand is uncontrollable, electricity cannot be stored in the grid, supply is centralised at high voltage, demand sits in the low-voltage grid — so "supply follows demand".
- **c)** Renewables make supply partially unpredictable and decentralised, and can reverse power flow — so demand must become controllable too.

### a) Frequency as a balance indicator

The whole synchronous European grid runs at 50 Hz (60 Hz in the US). Because the grid is coupled, the frequency is the same everywhere, which is exactly what makes it usable as a control signal:

| Condition | Frequency | Interpretation |
|-----------|-----------|----------------|
| Load > generation | drops below 50 Hz | too little generation, or too much load |
| Load < generation | rises above 50 Hz | surplus generation |
| Load = generation | 50 Hz | balanced |

Control happens through spinning reserve and balancing power (primary, secondary, minute, hour), triggered by frequency deviation. Frequency is not just an indicator — it is the physical consequence of kinetic energy being drained from or fed into rotating generators.

### b) Traditional assumptions

1. **Demand cannot be controlled.** Load is whatever consumers happen to do.
2. **Electricity cannot be stored (in the grid).** Production and consumption must match instantaneously — there is no buffer between them.
3. **Mainly centralised supply** at the high-voltage transmission grid.
4. **Demand is located in the low-voltage distribution grid.**
5. **Control** happens via spinning reserve and balancing power, triggered by frequency deviations.

Together these yield the major principle: **supply follows demand**. Every generator is dispatched to chase a load nobody controls.

### c) What renewables break

Renewable generation violates the assumptions in three ways:

1. **Supply becomes partially uncontrollable and unpredictable.** Wind and sun are weather, not dispatch.
2. **Supply becomes decentralised** and moves towards the edge, into the low-voltage distribution grid — where the load is, not where the control is.
3. **Power flow can reverse.** Distribution feeders were designed for one direction; with rooftop PV, power flows outward, which the protection and voltage control of the legacy grid were not built for.

The consequence: since supply can no longer follow demand, **demand must be able to follow supply** — demand-side integration, load shifting, and storage. That is exactly the gap the lecture's ICT use cases fill: metering and data collection, forecasting (with real-time data, where latency, completeness, and correctness matter), and the control layer that turns flexible loads into an asset.

---

## Source notes

- Definitions, numbers (50 Hz, three-phase, the traditional assumptions, sector-coupling examples) come from `EnInf_I_0.Motivation.pdf`.
- Task list and phrasing come from `Tutorial_1.pdf`.
- The RMS derivation, the 230 V → 325.3 V arithmetic, and the advantages/disadvantages tables are worked out here; the slides state the concepts but do not print a pros/cons list.
