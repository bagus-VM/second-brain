---
title: "Non-repudiation"
tags: [concept, iot-security, semester-1, iot-security]
course: "IoT Security"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[digital-signatures]]", "[[cia-triad]]"]
---

## One-line Summary
Non-repudiation ensures that a party cannot deny having performed an action — providing cryptographic proof that a specific entity sent a specific message or performed a specific operation.

## Core Intuition
Imagine an industrial IoT system where a valve was opened, causing a chemical spill. The operator says "I never sent that command." Without non-repudiation, there's no way to prove who sent it. With non-repudiation, every command is digitally signed, and the signature mathematically proves who sent it — the signer cannot later deny it. This is different from authentication (which verifies identity *at the time of action*) — non-repudiation provides proof *after the fact*, usable in audits and legal proceedings.

## Formal Definition / Statement

### Definition
Non-repudiation is the property that prevents an entity from successfully denying having:
- **Sent a message** (non-repudiation of origin)
- **Received a message** (non-repudiation of delivery)
- **Performed an action** (non-repudiation of action)

### Mechanism
Non-repudiation is achieved through **digital signatures**:
1. Entity signs a message/command with their **private key**
2. Anyone can verify the signature using the entity's **public key**
3. Only the private key holder could have produced the signature
4. Therefore, the entity cannot deny having signed

### Key Requirement
Non-repudiation requires **asymmetric cryptography**. Symmetric MACs (Message Authentication Codes) do NOT provide non-repudiation because both parties share the secret key — either party could have created the MAC.

| Property | Digital Signature | MAC |
|----------|-------------------|-----|
| Key type | Asymmetric (private/public) | Symmetric (shared secret) |
| Non-repudiation | ✓ Yes | ✗ No |
| Authentication | ✓ Yes | ✓ Yes |
| Integrity | ✓ Yes | ✓ Yes |

## Key Properties / Complexity

### Non-repudiation in IoT
- **Audit trails:** Every actuator command, sensor reading, and configuration change must be signed and logged
- **Industrial accountability:** In industrial IoT, knowing exactly who did what is critical for safety investigations and regulatory compliance
- **Legal evidence:** Signed logs can be used as evidence in legal proceedings

### Challenges
- **Key management:** Non-repudiation requires a PKI (Public Key Infrastructure) with certificate authorities
- **Time synchronisation:** Logs must have trusted timestamps — a signed command without a reliable timestamp can be replayed
- **Resource constraints:** Digital signatures are computationally expensive (~1000x slower than symmetric operations)
- **Long-term validity:** Signatures must remain verifiable for years, even as cryptographic standards change (algorithm agility)
- **Device compromise:** If a device's private key is extracted, the attacker can produce valid signatures that the device cannot repudiate

### Non-repudiation vs. Authentication
| Aspect | Authentication | Non-repudiation |
|--------|---------------|-----------------|
| When | At the time of action | After the fact |
| Purpose | Verify identity for access | Provide proof for accountability |
| Audience | The system being accessed | Third parties (auditors, courts) |
| Mechanism | Passwords, certificates, biometrics | Digital signatures on logged actions |

## Worked Example
**Industrial IoT Command Audit:**

1. **Normal operation:** Operator sends "Open valve V-101" command
   - Command is signed with operator's private key: σ = Sign(sk_operator, "open V-101, timestamp=2026-06-09T14:30:00Z")
   - Command is logged: (command, σ, timestamp, device_id)

2. **Incident:** Chemical spill occurs at 14:32

3. **Investigation:** Auditor examines logs
   - Finds signed command "Open valve V-101" from operator's key
   - Verifies signature: Verify(pk_operator, "open V-101...", σ) = true
   - Operator cannot deny having sent the command — the signature proves it

4. **If operator claims compromise:** The investigation shifts to whether the private key was stolen, but the signature itself is irrefutable proof that *someone with that key* sent the command

## Common Pitfalls
- Confusing authentication with non-repudiation — authentication verifies who you are right now; non-repudiation proves who you were later
- Using symmetric MACs for non-repudiation — both parties share the key, so either could have created the MAC
- Not timestamping signed messages — without trusted timestamps, old signatures can be replayed
- Ignoring key compromise — if the private key is stolen, the real owner's signatures become indistinguishable from the attacker's
- Not implementing certificate revocation — compromised keys must be revoked to limit non-repudiation damage
- Treating non-repudiation as purely technical — it also requires organisational processes (key custody, access logs)

## Connections
- [[digital-signatures]] — The cryptographic mechanism that provides non-repudiation
- [[authentication]] — Authentication verifies identity; non-repudiation prevents denial
- [[information-assurance]] — Non-repudiation is one of the seven IA properties (extending CIA)
- [[cia-triad]] — Non-repudiation is beyond CIA — it's about accountability, not secrecy/integrity/availability
- [[firmware-security]] — Signed firmware provides non-repudiation for firmware origin
- [[trusted-platform-module]] — TPMs store signing keys and perform signing operations
- [[iot-attack-taxonomy]] — Spoofing attacks violate non-repudiation
- [[digital-signatures]] — Digital signatures are the primary mechanism for achieving non-repudiation

## Open Questions
- How do we maintain non-repudiation when cryptographic algorithms become obsolete (post-quantum)?
- Should non-repudiation be mandatory for all IoT commands, or only safety-critical ones?
- How do we handle non-repudiation for autonomous IoT systems that act without human commands?
