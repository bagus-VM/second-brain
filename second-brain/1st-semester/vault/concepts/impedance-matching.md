---
title: "Impedance Matching"
tags: [concept, microelectronics, semester-1, introduction-to-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-20
prerequisites: [voltage-follower]
---

## One-line Summary
*Impedance matching means designing circuits so that a source can deliver maximum power to a load, or so that stages don't load each other down.*

## Core Intuition
Imagine a fire hose connected to a garden hose fitting. The pressure (voltage) is there, but almost no water (current) flows — the impedances are mismatched. Impedance matching is about making the "pipe sizes" compatible.

In electronics, every signal source has an output impedance (how much it "pushes back" against current flow) and every load has an input impedance (how much it "resists" current flow). If these are poorly matched, you lose signal — either through voltage division (load too low) or power reflection (in RF systems).

The voltage follower (unity-gain buffer) is the simplest impedance matcher: it has near-infinite input impedance (draws no current from the source) and near-zero output impedance (can drive heavy loads).

## Formal Definition / Statement
For a source with output impedance Zs driving a load with input impedance Zl:

**Voltage transfer:** V_load = V_source × Zl/(Zs + Zl)

- To maximise **voltage transfer:** Zl >> Zs (high-impedance load)
- To maximise **power transfer:** Zl = Zs* (complex conjugate match — used in RF)
- To minimise **signal reflection** (transmission lines): Zl = Z0 (characteristic impedance match)

The **maximum power transfer theorem** states that power delivered to the load is maximised when Zl = Zs*, but at that point, efficiency is only 50% (half the power is dissipated in the source).

## Key Properties / Complexity
- **Voltage vs power matching:** Voltage matching (Zl >> Zs) is preferred in most analogue circuits; power matching (Zl = Zs*) is preferred in RF
- **Buffer role:** A voltage follower achieves voltage matching by transforming impedance: high Zin, low Zout
- **Cascade problem:** Without buffering, connecting amplifier stages in series causes each stage to load the previous one, reducing overall gain
- **Frequency dependence:** Impedance is complex (real + imaginary), so matching depends on frequency. A circuit matched at DC may be mismatched at high frequencies
- **Transmission line matching:** When wire length > λ/10 (where λ is signal wavelength), reflections become significant and characteristic impedance matching is required

## Worked Example
**Source with Zs = 10kΩ, load with Zl = 1kΩ:**

Without buffer: V_load = V_source × 1k/(10k + 1k) = 0.091 × V_source — 91% signal loss!

Insert a voltage follower between source and load:
- Follower draws negligible current from source (Zin ≈ 10^12 Ω for CMOS)
- Follower drives load with Zout ≈ 100 Ω
- V_load = V_source × 1k/(100 + 1k) ≈ 0.91 × V_source — only 9% loss

The buffer didn't amplify anything (gain = 1), but it preserved the signal by isolating source from load impedance.

## Common Pitfalls
- **Confusing voltage matching with power matching:** In most analogue circuits, you want voltage matching (Zl >> Zs). Only in RF do you typically want power matching (Zl = Zs*). At the power match, efficiency is only 50%!
- **Ignoring frequency effects:** A source impedance that's purely resistive at DC may become reactive (capacitive or inductive) at higher frequencies, requiring different matching strategies
- **Forgetting that the follower itself has limits:** The voltage follower can't drive arbitrarily low impedances — it has a maximum output current. If Zl is too low, the output clips or distorts
- **Matching at the wrong point:** In a multi-stage amplifier, you must consider the impedance at each interface, not just the source-to-load

## Connections
- [[voltage-follower]] — the canonical impedance-matching circuit (unity-gain buffer)
- [[opamp-basics]] — op-amp's high input impedance and low output impedance make it ideal for impedance matching
- [[negative-feedback]] — negative feedback reduces output impedance by factor (1 + Aβ)
- [[common-source-amplifier]] — CS amplifier has high output impedance; cascode or follower needed for matching

## Open Questions
- How does impedance matching change when the source or load is reactive (capacitive/inductive)?
- What is the trade-off between noise figure matching and power matching in low-noise amplifier design?
