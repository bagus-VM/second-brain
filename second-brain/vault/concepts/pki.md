---
title: "Public Key Infrastructure (PKI)"
tags:
  - concept
  - iot-security
  - semester-1
  - cryptography
  - identity
course: IoT Security
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary
PKI is a framework for managing digital certificates and public-key encryption — enabling device authentication, secure communication, and firmware signing at scale.

## Core Intuition
How do you verify that a device is who it claims to be? How do you encrypt data so only the intended recipient can read it? Public Key Infrastructure provides the plumbing: a trusted authority (Certificate Authority) issues digital certificates that bind public keys to identities. For IoT, PKI solves three critical problems: (1) authenticating devices, (2) securing communication channels, and (3) verifying firmware updates. The challenge is managing certificates for billions of constrained devices.

## Formal Definition / Statement
PKI is a set of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption.

**Core components:**
- **Certificate Authority (CA)** — trusted entity that issues and signs certificates
- **Registration Authority (RA)** — verifies identity before CA issues certificate
- **Certificate Revocation List (CRL)** — list of revoked certificates
- **Online Certificate Status Protocol (OCSP)** — real-time certificate revocation checking
- **Digital certificates** — X.509 standard binding public key to identity

**Certificate structure (X.509):**
```
Certificate:
  Version: v3
  Serial Number: unique identifier
  Signature Algorithm: RSA-SHA256
  Issuer: CN=Root CA
  Validity:
    Not Before: 2026-01-01
    Not After: 2027-01-01
  Subject: CN=device-001, O=Manufacturer
  Subject Public Key: RSA 2048-bit
  Extensions:
    Key Usage: digitalSignature, keyEncipherment
```

## Key Properties
| Property | Detail |
|----------|--------|
| Trust hierarchy | Root CA → Intermediate CA → Device certificates |
| Asymmetric crypto | Public key encrypts, private key decrypts (or vice versa for signing) |
| Certificate lifecycle | Issuance → Usage → Renewal → Revocation |
| Scalability challenge | Billions of IoT devices × certificate management |
| Chain of trust | Verify certificate by checking signatures up to root CA |
| Revocation | CRL (periodic) or OCSP (real-time) to invalidate compromised certs |

## Worked Example
**Scenario:** A smart lock needs secure communication with the cloud backend.

**Certificate provisioning (factory):**
1. Manufacturer generates key pair on device (private key never leaves secure element)
2. Device sends public key + device ID to RA
3. RA verifies device identity (serial number, manufacturing record)
4. CA issues X.509 certificate signed with CA's private key
5. Certificate stored on device's secure element

**Mutual TLS handshake:**
1. Device connects to cloud server
2. Server presents its certificate → device verifies against trusted CA
3. Server requests device certificate → device presents it
4. Server verifies device certificate against trusted CA
5. Both derive session key from the handshake → encrypted communication established

**Firmware update verification:**
1. Manufacturer signs firmware binary with signing key
2. Device receives update, verifies signature using manufacturer's public certificate
3. If signature valid → install; if invalid → reject and alert

**Revocation scenario:** Device compromised → CA adds certificate serial to CRL → cloud server checks CRL during handshake → refuses connection.

## Common Pitfalls
- **Ignoring certificate lifecycle**: Certificates expire — automated renewal is essential for IoT at scale
- **Hardcoding root CA**: If root CA is compromised, all devices need updating — use intermediate CAs
- **CRL/OCSP availability**: If revocation checking fails, should devices fail-open (insecure) or fail-closed (denial of service)?
- **Private key protection**: If private key is extracted from device, identity is compromised — use hardware secure elements
- **Bootstrapping problem**: How to provision the first certificate on a factory-new device with no existing identity
- **Clock dependency**: Certificate validity depends on accurate time — IoT devices often lack reliable clocks

## Connections
- [[iot-identity-lifecycle]] — PKI manages device identity throughout its lifecycle
- [[key-management-lifecycle]] — certificate lifecycle is a subset of key management
- [[device-provisioning]] — initial certificate deployment during manufacturing
- [[secure-boot-chain]] — secure boot uses certificates to verify firmware
- [[iot-lecture-7]], [[iot-lecture-8]] — source lectures

## Open Questions
- How do resource-constrained devices handle certificate verification (RSA-2048 is computationally expensive)?
- What alternatives to traditional PKI exist for IoT (e.g., identity-based encryption, blockchain-based identity)?
- How do you handle CA compromise at scale (billions of devices)?
- Is certificate-based authentication practical for devices with <1KB RAM?
