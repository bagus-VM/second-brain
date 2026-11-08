---
title: "Key Management Lifecycle"
tags: [concept, iot-security, cryptography, management, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*The complete lifecycle of cryptographic keys from generation through distribution, storage, use, rotation, and destruction.*

## Core Intuition
Cryptography is only as good as your key management. You can use AES-256, but if your keys are stored in plaintext flash, hardcoded in firmware, or never rotated, the encryption is theater. For IoT, key management is especially challenging because devices may be physically accessible, have limited secure storage, and need to operate for years without human intervention. The key management lifecycle ensures keys are properly handled at every stage.

## Formal Definition / Statement
The key management lifecycle encompasses all phases of a cryptographic key's existence:

1. **Generation**
   - Keys must be generated using approved random number generators (TRNG, CSPRNG)
   - Generation can occur at manufacturing (pre-provisioned), at first boot, or on-demand
   - Entropy sources: hardware TRNG, environmental noise, PUFs

2. **Distribution/Provisioning**
   - Secure delivery of keys to devices
   - Methods: pre-provisioned in factory, key agreement protocols (ECDH), certificate-based (PKI)
   - Zero-touch provisioning for large-scale deployments

3. **Storage**
   - Keys must be protected at rest
   - Options: hardware secure element (SE), TPM, TrustZone, encrypted flash
   - Never store keys in plaintext firmware or source code

4. **Use**
   - Keys should be used only for their designated purpose (signing vs encryption vs authentication)
   - Usage limits: key derivation functions, per-session keys
   - Isolation: different keys for different services/tenants

5. **Rotation**
   - Periodic replacement of keys to limit exposure from compromise
   - Automated rotation via protocols (e.g., TLS session keys, MQTT key rotation)
   - Zero-downtime rotation: new key deployed before old key retired

6. **Revocation/Destruction**
   - Immediate invalidation when compromise is suspected
   - Certificate Revocation Lists (CRLs), OCSP for PKI-based systems
   - Secure erasure: cryptographic erasure, physical destruction of key material

## Key Properties / Complexity
- NIST SP 800-57 provides the authoritative key management guidelines
- Key sizes: RSA-2048 minimum (RSA-3072 recommended), ECDSA-P256, AES-128/256
- Hardware security modules (HSMs) provide the strongest key protection
- IoT devices often use pre-shared keys (PSK) for simplicity, but PKI is more scalable
- Key rotation frequency depends on threat model: daily for high-security, yearly for low-risk
- Asymmetric keys for authentication/key exchange, symmetric keys for bulk encryption

## Worked Example
An IoT fleet of 10,000 sensors manages keys:
1. **Manufacturing**: Each sensor gets a unique device certificate signed by the manufacturer's CA. Private key generated on-chip, never leaves the secure element.
2. **Provisioning**: During first boot, the sensor connects to the provisioning server, presents its device certificate, and receives operational keys for MQTT and OTA.
3. **Operation**: MQTT uses TLS with the device certificate for mutual authentication. Session keys are derived per-connection via TLS handshake.
4. **Rotation**: Every 90 days, the provisioning server pushes new operational keys via the secure channel. Device certificate rotates annually.
5. **Compromise response**: If sensor #4721 is detected behaving anomalously, its certificate is revoked via CRL. The device is quarantined and re-provisioned.
6. **Decommissioning**: When a sensor is retired, cryptographic erasure destroys all key material. The device certificate is revoked.

## Common Pitfalls
- **Hardcoded keys**: The #1 IoT key management failure. Keys embedded in firmware are extractable.
- **Shared keys**: Using the same key across all devices means one compromised device compromises all.
- **No rotation**: Keys that never rotate accumulate exposure risk over the device's lifetime.
- **Clock dependency**: Certificate validation and CRL checking require accurate time. IoT devices often lack RTC and struggle with time synchronization.
- **Scale challenges**: Managing keys for millions of devices requires robust PKI infrastructure.
- **Entropy starvation**: Microcontrollers may have poor entropy sources, leading to weak key generation.

## Connections
- [[tcg-specifications]] — TPM and DICE provide hardware-backed key storage and generation
- [[fips-140-2]] — FIPS validates the cryptographic implementations used for key management
- [[device-provisioning]] — Key provisioning is a core component of device onboarding
- [[secure-boot-chain]] — Signing keys are the most critical keys in the lifecycle
- [[iot-communication-protocols]] — TLS/DTLS in MQTT, CoAP depend on proper key management
- [[privacy-by-design]] — Proper key management enables data confidentiality and minimization

## Open Questions
- How does this standard/framework apply to resource-constrained IoT devices with limited processing power?
- What are the practical tradeoffs between compliance and actual security improvement?
