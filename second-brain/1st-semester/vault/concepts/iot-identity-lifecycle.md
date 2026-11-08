---
title: "IoT Identity Lifecycle"
tags: [concept, iot-security, semester-1, identity-management]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-19
prerequisites: ["[[iot-lecture-6]]", "[[secure-boot-chain]]", "[[authentication]]"]
---

## One-line Summary
The cradle-to-grave management of device identities from bootstrapping through deactivation.

## Core Intuition

Every IoT device needs a verifiable identity — not just a MAC address or IP address (which are network-layer concepts), but a cryptographic identity that proves "I am the device I claim to be." This identity must be created securely (bootstrapping), maintained throughout the device's operational life (credential rotation, monitoring), and destroyed completely when the device is decommissioned (deactivation).

Think of it as a passport system for devices: issued by a trusted authority, carried by the device, verified at every checkpoint, and revoked when the device is compromised or retired.

## Formal Definition / Statement

### Device Naming Attributes

A device identity consists of a set of attributes:

| Attribute | Description | Mutability |
|---|---|---|
| **Manufacturer** | Entity that produced the device | Immutable |
| **Device type** | Model, capabilities, firmware class | Immutable |
| **Serial number** | Unique instance identifier | Immutable |
| **Deployment date** | When the device entered service | Set once |
| **Location** | Physical deployment location | May change |
| **Owner/operator** | Entity responsible for the device | May change |

These attributes are bound to cryptographic credentials (certificates, keys) during provisioning.

### Credential Provisioning

**Bootstrapping**: the one-time process of establishing a device's initial identity and credentials.

Methods:
1. **Factory provisioning**: credentials injected during manufacturing (most secure)
2. **Pre-shared key (PSK) bootstrap**: device ships with a symmetric key; uses it to obtain long-term credentials
3. **Certificate-based bootstrap**: device ships with a manufacturer certificate; uses it to obtain operational credentials
4. **Out-of-band transfer**: QR code, NFC, or physical interface transfers initial credentials

**Credential types:**
- Symmetric keys (for MAC-based authentication)
- X.509 certificates (for PKI-based authentication)
- Implicit certificates (IEEE 1609.2, for vehicular networks)

### Account Lifecycle States

```
[Provisioned] → [Active] → [Monitored] → [Updated] → [Suspended] → [Deactivated/Deleted]
```

- **Provisioned**: identity created, credentials issued, but not yet deployed
- **Active**: device is operational and communicating
- **Monitored**: device behaviour is being assessed for anomalies
- **Updated**: credentials rotated, firmware updated, policies changed
- **Suspended**: temporary revocation of access (anomalous behaviour detected)
- **Deactivated/Deleted**: permanent removal of identity and credentials

### Connection to PKI and Certificate Management

The identity lifecycle is implemented through a Public Key Infrastructure (PKI):

1. **Root CA**: offline, air-gapped, signs intermediate CA certificates
2. **Intermediate CA(s)**: operational CAs that issue device certificates
3. **Registration Authority (RA)**: validates device identity before certificate issuance
4. **Device certificate**: binds device identity attributes to a public key
5. **Certificate revocation**: CRLs, OCSP, or short-lived certificates

**Automated enrollment protocols:**
- **EST (Enrollment over Secure Transport, RFC 7030)**: HTTPS-based certificate enrollment
- **CMP (Certificate Management Protocol, RFC 4210)**: full lifecycle management

**Scalability challenge**: billions of IoT devices need certificates. Manual enrollment is impossible; automation is essential.

## Key Properties / Complexity

### Identity vs. Anonymity

- **Strong identity** (unique certificate per device): enables authentication, accountability, audit trails — but creates privacy risk (device can be tracked)
- **Weak identity** (shared credentials, pseudonyms): better privacy, but harder to detect compromised devices and enforce policies

The engineering challenge is finding the right balance for each use case.

### Credential Rotation

Credentials must be rotated periodically to limit the window of exposure if a credential is compromised:

- **Symmetric keys**: re-keying protocols (e.g., TLS re-handshake)
- **Certificates**: renewal before expiration; short-lived certificates (hours/days) avoid revocation entirely
- **Challenge**: how does a constrained device with no UI know when to rotate? (Automated protocols, server-initiated rotation)

### Revocation at Scale

- **CRLs (Certificate Revocation Lists)**: periodic list of revoked certificates. Bandwidth-heavy at scale (millions of devices).
- **OCSP (Online Certificate Status Protocol)**: real-time query per certificate. Privacy concern: OCSP server learns who is connecting to whom.
- **OCSP stapling**: server queries OCSP on behalf of client, staples response to TLS handshake.
- **Short-lived certificates**: certificates valid for hours/days; no revocation needed (just don't renew).

### Decommissioning

When a device is retired, sold, or destroyed:
1. Revoke the device's certificate (add to CRL or OCSP responder)
2. Delete the device identity from the management system
3. If the device is reused, wipe all credentials (secure erase, cryptographic erasure)
4. Audit trail: record the decommissioning event

**Cryptographic erasure**: delete the encryption key that protects stored credentials; the data becomes unrecoverable.

## Worked Example

### Smart Thermostat Identity Lifecycle

**1. Factory provisioning:**
- Manufacturer generates unique key pair for each thermostat
- Device certificate issued: `CN=Thermostat-T200, OU=BuildingAutomation, O=AcmeSensors, serialNumber=SN-00A4F2B7`
- Certificate signed by manufacturer's intermediate CA
- Certificate and private key stored in device's secure element

**2. Deployment:**
- Installer mounts thermostat; device connects to building network
- Device presents certificate to network access control (802.1X)
- RADIUS server validates certificate chain: device cert → intermediate CA → root CA
- Device granted network access; assigned IP address

**3. Operational phase:**
- Device communicates with building management system using mutual TLS (mTLS)
- Device certificate renewed annually (automated via EST protocol)
- Device behaviour monitored: normal temperature adjustments vs. anomalous commands
- If anomaly detected (e.g., device sending data to external IP), certificate suspended

**4. Update:**
- Firmware update signed by manufacturer; device verifies signature before installing
- New firmware may include updated root CA certificates

**5. Decommissioning:**
- Building manager marks device as retired in management system
- Certificate revoked (added to CRL)
- Device identity deleted from management database
- If device is reused, secure element wiped (cryptographic erasure)

## Common Pitfalls

- **Hardcoded credentials**: shipping devices with default passwords or shared certificates
- **No revocation mechanism**: if a device is compromised, there's no way to revoke its credentials
- **Manual enrollment**: impossible at scale; automation (EST, CMP) is essential
- **Ignoring decommissioning**: retired devices left in the system with valid credentials
- **Over-privileged identities**: device certificate grants access to all systems, not just the ones it needs
- **No credential rotation**: credentials never change; compromise is permanent
- **Storing keys in software**: vulnerable to extraction via firmware dump or side-channel attack
- **Shared credentials across device models**: one compromise breaks all devices of that model

## Connections

- [[iot-lecture-7]] — the full lecture topic; identity lifecycle is one half
- [[secure-boot-chain]] — bootstrapping relies on a chain of trust from hardware to identity
- [[authentication]] — the security service that identity management enables
- [[key-management-lifecycle]] — credential provisioning and rotation
- [[iot-compliance-frameworks]] — regulatory requirements for identity management
- [[iot-secure-design]] — identity as a secure design goal
- [[nist-iot-cybersecurity]] — NIST framework includes device identity and authentication
- [[iot-data-lifecycle]] — identity is managed throughout the data lifecycle
- [[asymmetric-encryption]] — certificates are built on asymmetric cryptography
- [[trusted-platform-module]] — hardware that stores device credentials securely

## Open Questions

- Will decentralized identity (DID, blockchain) replace PKI for IoT, or will they coexist?
- How should identity work for devices that change ownership (resale, rental)?
- Is short-lived certificate rotation practical for battery-powered devices with limited compute?
- Can identity be portable across platforms (a device works with multiple cloud providers)?
- How do you authenticate a device that has no user interface and no network connectivity during provisioning?
