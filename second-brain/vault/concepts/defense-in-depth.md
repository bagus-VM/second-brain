---
title: "Defence in Depth"
tags:
  - concept
  - iot-security
  - semester-1
  - security
course: IoT Security
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary
Defence-in-depth layers multiple defensive mechanisms so that if one layer fails, others remain — forcing attackers to breach all layers to succeed.

## Core Intuition
No single defense is sufficient. An attacker with enough time and resources can bypass any individual security measure. Defence-in-depth assumes breach will happen and designs for resilience: if the perimeter is breached, there are more walls inside. For IoT, this means securing the physical device, the firmware, the network, the application, the cloud backend, the data itself, and the operational processes around it. Governmental-level attackers (vast resources, time, effort) make this strategy mandatory, not optional.

## Formal Definition / Statement
Defence-in-depth is a security architecture principle where multiple independent layers of controls are deployed so that the failure of any single control does not compromise the system. Formally, if each layer $L_i$ has a breach probability $p_i$, the probability of an attacker breaching all $n$ layers is:

$$P_{breach} = \prod_{i=1}^{n} p_i$$

This assumes layers are independent — in practice, correlated failures reduce effectiveness.

## Key Properties
| Property | Detail |
|----------|--------|
| Layered defense | Multiple independent security mechanisms |
| Assumes breach | Designs for resilience, not prevention alone |
| Independence | Layers should not share common failure modes |
| Depth | More layers = exponentially harder to breach (if independent) |
| Complexity | More layers = more operational overhead |
| Cost | Each layer adds cost to implementation and maintenance |

The 7 layers for IoT:
1. **Physical security** — tamper resistance, secure enclosures
2. **Device security** — secure boot, firmware signing, trusted execution
3. **Network security** — encryption, segmentation, firewalls
4. **Application security** — input validation, secure coding practices
5. **Cloud security** — access control, monitoring, API security
6. **Data security** — encryption at rest and in transit
7. **Operational security** — patching, monitoring, incident response

## Worked Example
Consider a smart home thermostat with defence-in-depth:

**Layer 1 — Physical:** Tamper-evident enclosure; if opened, keys are wiped
**Layer 2 — Device:** Secure boot verifies firmware signature before execution
**Layer 3 — Network:** TLS 1.3 for all communication; device on isolated VLAN
**Layer 4 — Application:** Input validation on temperature setpoints; rate limiting on API calls
**Layer 5 — Cloud:** OAuth2 tokens with short expiry; role-based access control
**Layer 6 — Data:** User preferences encrypted at rest (AES-256); PII anonymized in logs
**Layer 7 — Operational:** Automatic security updates; anomaly detection alerts on unusual traffic patterns

**Attack scenario:** Attacker compromises the Wi-Fi network (breaches Layer 3). Without defence-in-depth, they'd have full access. With it: TLS encryption prevents reading traffic (Layer 3 still partially effective), application input validation blocks injection (Layer 4), cloud tokens are expired or scoped (Layer 5), stored data is encrypted (Layer 6), and anomaly detection triggers an alert (Layer 7).

## Common Pitfalls
- **Assuming layers are independent**: If all layers use the same underlying library, a single vulnerability can breach multiple layers
- **Adding layers for quantity**: A poorly implemented layer gives false confidence — better to have fewer strong layers
- **Ignoring operational security**: The best technical controls fail without monitoring and incident response
- **Over-engineering for simple devices**: A temperature sensor doesn't need all 7 layers at enterprise grade — risk-proportionate defense
- **Confusing depth with perimeter**: Defence-in-depth is not just "more firewalls" — it includes internal controls

## Connections
- [[zero-trust-architecture]] — related concept: no single trust domain, verify at every layer
- [[security-by-design]] — defence-in-depth should be designed in from the start
- [[secure-boot-chain]] — Layer 2 (device security) relies on secure boot
- [[network-security-fundamentals]] — Layer 3 (network security) implementation
- [[privacy-by-design]] — data security (Layer 6) aligns with privacy principles
- [[iot-lecture-8]] — source lecture

## Open Questions
- How do resource-constrained IoT devices implement all 7 layers without excessive cost or power consumption?
- What is the minimum viable defence-in-depth for a simple sensor vs. a critical infrastructure device?
- How do you measure the independence of layers in practice?
- When does adding more layers provide diminishing returns?
