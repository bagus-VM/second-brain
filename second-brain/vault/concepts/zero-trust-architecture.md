---
title: "Zero Trust Architecture"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[network-security-fundamentals]]", "[[device-provisioning]]"]
---
## One-line Summary
Zero Trust Architecture — "never trust, always verify" — replaces perimeter-based security with identity-centric, microsegmented access control that treats every device and user as potentially compromised.

## Core Intuition
Traditional network security assumes "inside the firewall = trusted." Zero Trust rejects this assumption. In an IoT context, this means a compromised smart bulb should not be able to access a medical device, even if they're on the same network. Every device must prove its identity, every connection must be authenticated and authorized, and access must be limited to the minimum necessary. The perimeter is dead; identity is the new perimeter.

## Formal Definition / Statement
Zero Trust Architecture (ZTA) is a security framework based on the principle that no user, device, or network segment should be inherently trusted. Key tenets (NIST SP 800-207):

**Core Principles:**
1. **All resources are accessed securely regardless of network location**: No distinction between "inside" and "outside" the network
2. **Access is granted on a per-session basis**: No persistent trust; every request evaluated independently
3. **Access is determined by dynamic policy**: Based on device health, user identity, behaviour patterns, and context
4. **Enterprise monitors and measures integrity and security posture of all assets**: Continuous verification
5. **Authentication and authorization are dynamic and strictly enforced before access is allowed**: No implicit trust

**Zero Trust for IoT:**
- **Device identity**: Every IoT device has a unique, verifiable cryptographic identity (certificate, TPM attestation)
- **Microsegmentation**: Each device or device group is isolated; communication requires explicit policy
- **Least privilege**: Devices can only access the specific resources they need (e.g., sensor can publish to its own topic only)
- **Continuous verification**: Device health checked continuously (firmware attestation, behaviour monitoring)
- **Encryption everywhere**: All communication encrypted, even within the "internal" network

**Implementation Approaches:**
- **Software-Defined Perimeter (SDP)**: Devices must authenticate before even seeing network resources
- **Identity-Aware Proxy**: All traffic routed through a proxy that enforces identity-based access
- **Microsegmentation platforms**: NSX, Illumio, Akamai Guardicore for per-workload segmentation
- **Device attestation**: TPM-based or PUF-based continuous device health verification

## Key Properties / Complexity

- **Identity is foundational**: Zero Trust requires strong device identity — provisioning is a prerequisite
- **Continuous verification is expensive**: Attesting every device continuously requires infrastructure and bandwidth
- **Constrained devices challenge ZTA**: Class 0-1 devices cannot run mTLS, certificate validation, or attestation protocols
- **Latency concerns**: Every connection requiring authentication and authorization adds latency — problematic for real-time industrial IoT
- **Policy management at scale**: Millions of IoT devices require automated policy generation and enforcement
- **Legacy device problem**: Devices that cannot support modern authentication cannot participate in ZTA
- **Operational complexity**: ZTA requires robust identity management, policy engines, and monitoring infrastructure

## Worked Example

**Zero Trust IoT network for a hospital:**
1. Every medical device provisioned with X.509 certificate during manufacturing
2. Devices authenticate to identity-aware gateway using mTLS before accessing any network resource
3. Policy engine evaluates: device identity + device health (firmware attestation) + user context + time of day
4. Infusion pump allowed to communicate with: pharmacy server (drug library updates), nurse station (alarm forwarding), monitoring system (vitals reporting)
5. Same pump denied communication with: billing system, guest Wi-Fi, internet (except update server)
6. Continuous monitoring: anomalous traffic patterns trigger automatic quarantine
7. If firmware attestation fails (tampered firmware), device automatically isolated

## Common Pitfalls

- Applying ZTA principles only to users, not devices
- Not having strong device identity as a foundation (ZTA without identity is theater)
- Over-segmenting to the point where legitimate communication breaks
- Not accounting for constrained devices that cannot participate in ZTA protocols
- Treating ZTA as a product rather than an architecture (no single vendor solution)
- Ignoring operational overhead — ZTA requires continuous management and policy updates

## Connections

- [[device-provisioning]] — Device identity is the foundation of Zero Trust
- [[network-security-fundamentals]] — Traditional network security that ZTA evolves beyond
- [[security-principles]] — Least privilege as a core ZTA principle
- [[principle-of-least-privilege]] — Deep dive into minimal access rights
- [[iot-network-architecture]] — Network architecture implications of ZTA
- [[iot-firewalling]] — Microsegmentation implementation
- [[iot-lecture-4]] — Zero Trust as a design principle for IoT

## Open Questions
- Can Zero Trust be meaningfully applied to Class 0-1 constrained IoT devices?
- How does Zero Trust interact with mesh networking protocols where devices route traffic for others?
- What is the right granularity for microsegmentation in an IoT network with 10,000 devices?
