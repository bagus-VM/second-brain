---
title: "Device Provisioning"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-device-fundamentals]]", "[[key-management-lifecycle]]"]
---
## One-line Summary
Device provisioning is the process of giving each IoT device its unique identity, credentials, and initial configuration — the moment where security is established (or fails) for the device's entire lifetime.

## Core Intuition
Provisioning is the "birth certificate" of an IoT device. Done right, each device gets a unique cryptographic identity, the correct certificates, and the right permissions. Done wrong, you get the Mirai botnet: millions of devices with identical default credentials. The challenge is doing this at scale — provisioning a million devices in a factory while maintaining security and keeping costs low.

## Formal Definition / Statement
Device provisioning is the process of establishing a device's identity, credentials, and configuration before or during its first deployment. It encompasses:

**Identity Establishment:**
- **Unique device identity**: Each device needs a unique, verifiable identity (X.509 certificate, device attestation key, PUF-derived identity)
- **Device attestation**: Proving the device is genuine (not counterfeit) and running authorized firmware
- **Identity binding**: Associating the device identity with a cloud account, user, or organizational unit

**Credential Injection:**
- **Certificate provisioning**: Generating or injecting X.509 certificates for TLS client authentication
- **Key injection**: Loading symmetric keys (for Zigbee, LoRaWAN) or asymmetric key pairs into secure storage
- **Root of trust**: Provisioning root CA certificates for certificate chain validation

**Initial Configuration:**
- **Network configuration**: SSID, network keys, gateway addresses
- **Cloud endpoint**: MQTT broker address, API endpoints, telemetry configuration
- **Security policy**: Update schedule, communication allowed list, logging level

**Provisioning Methods:**
1. **Factory provisioning**: Keys/certificates injected during manufacturing. Most secure but requires manufacturing line integration.
2. **Zero-touch provisioning (ZTP)**: Device self-provisions on first boot by connecting to a provisioning service. Requires initial bootstrap credential.
3. **Just-in-time provisioning**: Device registers with cloud service upon first connection, receives credentials dynamically.
4. **Manual provisioning**: Technician configures each device individually. Does not scale.
5. **Commissioning**: Protocol-specific joining process (Zigbee commissioning, BLE pairing, Thread joining).

## Key Properties / Complexity

- **Scale**: Factory provisioning must handle 10,000-1,000,000 devices per day
- **Uniqueness**: Every device must have unique credentials — shared credentials enable mass compromise
- **Secure key injection**: Keys must be generated in a Hardware Security Module (HSM) and injected over a secure channel
- **Bootstrap problem**: The device needs credentials to securely communicate, but needs to communicate to get credentials
- **Supply chain trust**: Provisioning must happen in a trusted manufacturing environment to prevent key leakage
- **Certificate lifecycle**: Provisioned certificates expire and need renewal — plan for this from day one
- **Zero-touch vs. security**: ZTP is convenient but requires a bootstrap credential that itself must be protected

## Worked Example

**Factory provisioning flow:**
1. Device PCB arrives at manufacturing line with MCU and secure element (e.g., ATECC608B)
2. Manufacturing station connects to factory HSM over secure channel
3. HSM generates unique key pair for device
4. HSM creates Certificate Signing Request (CSR) with device's public key
5. Factory CA (also in HSM) signs the CSR, producing device certificate
6. Certificate and private key injected into device's secure element via I2C/SPI
7. Device unique ID (serial number, MAC) bound to certificate in cloud device registry
8. Device undergoes functional test, then ships to customer
9. On first boot: device connects to Wi-Fi, presents certificate to cloud, cloud validates and activates

**Zero-touch provisioning flow:**
1. Device ships with bootstrap credential (pre-shared key or initial certificate)
2. Customer connects device to network
3. Device connects to provisioning service using bootstrap credential
4. Provisioning service validates device identity (checks serial number against order database)
5. Service generates device-specific certificate, sends to device over secure channel
6. Device stores certificate in secure element, discards bootstrap credential
7. Device registers with production cloud service using new certificate

## Common Pitfalls

- Sharing credentials across all devices in a product line (one key compromise = all devices compromised)
- Storing private keys in plaintext flash instead of secure hardware
- Not validating device identity during provisioning (allowing rogue devices to join)
- Using weak bootstrap credentials that can be brute-forced
- Not planning for certificate renewal at provisioning time
- Provisioning in untrusted manufacturing environments where keys can be copied
- Not having a mechanism to revoke and re-provision compromised devices

## Connections

- [[key-management-lifecycle]] — Provisioning is the first phase of key lifecycle
- [[secure-boot-chain]] — Provisioning establishes the root of trust for secure boot
- [[device-memory-attack-surface]] — Where credentials are stored after provisioning
- [[trusted-platform-module]] — TPM as provisioning target for keys
- [[physical-unclonable-functions]] — PUF as device identity foundation
- [[zero-trust-architecture]] — Device identity as the foundation of zero-trust
- [[iot-lecture-4]] — Secure integration points requiring device identity
- [[mqtt-security]] — Certificate provisioning for MQTT client authentication

## Open Questions
- Can decentralized identity (DID) replace centralized device registries for IoT provisioning?
- How do we handle provisioning for devices that will be deployed for 20+ years?
- What happens to provisioned credentials when a device is decommissioned and recycled?
