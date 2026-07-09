---
title: "Physical Unclonable Functions (PUFs)"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[security-by-design]]"]
---

## One-line Summary
Physical Unclonable Functions (PUFs) are hardware security primitives that exploit manufacturing variations to create unique, unclonable device identifiers — like a silicon fingerprint for every chip.

## Core Intuition
Even when two chips are manufactured identically, microscopic physical variations make each one unique. PUFs harness these variations to generate device-specific responses to challenges. You can't clone a PUF because you can't replicate the exact physical structure — even the manufacturer can't.

## Formal Definition / Statement
**Physical Unclonable Function (PUF):** A hardware security primitive that exploits manufacturing variations in integrated circuits to create unique device identifiers. Given a challenge (input), the PUF produces a unique response (output) determined by the physical properties of that specific chip. The mapping is:
- **Unique** — each chip produces different responses
- **Unclonable** — cannot be physically replicated
- **Reproducible** — the same chip produces the same response to the same challenge

## Key Properties / Complexity

### Properties
- **Inherent uniqueness** from manufacturing process variations
- **No secret storage** — the "key" is the physical structure itself
- **Tamper-evident** — physical attacks alter the PUF response
- **Lightweight** — suitable for resource-constrained IoT devices
- **No key provisioning** — identity emerges from physics, not programming

### Types of PUFs
- **SRAM PUFs** — exploit power-up state of SRAM cells
- **Ring Oscillator PUFs** — exploit frequency variations in ring oscillators
- **Arbiter PUFs** — exploit path delay differences
- **Coating PUFs** — exploit dielectric variations

### Use Cases in IoT
- Device authentication without stored keys
- Secure key generation (PUF + fuzzy extractor = cryptographic key)
- Supply chain integrity verification
- Anti-counterfeiting

## Worked Example
**PUF-based Device Authentication:**
1. During enrollment, challenge-response pairs (CRPs) are recorded for a device's PUF
2. CRPs are stored in a secure server
3. To authenticate, server sends a challenge
4. Device's PUF generates the response
5. Server verifies the response matches the enrolled CRP
6. An attacker cannot clone the device because they can't replicate the PUF's physical structure

## Common Pitfalls
- Assuming PUFs replace all cryptography — they provide device identity, not general-purpose encryption
- Not accounting for environmental variations (temperature, voltage) affecting PUF responses
- Storing too many CRPs creates a security risk (model-building attacks on arbiter PUFs)
- Ignoring that PUFs need fuzzy extraction/error correction for reliable operation

## Connections
- [[security-by-design]] — PUFs are a hardware security design choice
- [[trusted-platform-module]] — Alternative/complementary hardware security
- [[iot-security-hardware]] — Topic page covering PUFs, TPMs, security co-processors
- [[device-memory-attack-surface]] — PUFs eliminate stored key vulnerabilities
- [[physical-unclonable-functions]] → connects to [[iot-secure-design]] for practical deployment

- [[iot-lecture-1]] — IoT Security Landscape — course overview
- [[iot-lecture-5]] — IoT Security Hardware — PUFs, TPMs, secure boot
- [[iot-lecture-9]] — DRAM-PUF based IoT security protocol — concrete application of DRAM retention PUFs for device authentication

## Open Questions
- How do PUFs scale to billions of IoT devices?
- Can PUFs be made resilient to machine-learning-based modelling attacks?
- What's the standardisation status for PUF-based authentication?
