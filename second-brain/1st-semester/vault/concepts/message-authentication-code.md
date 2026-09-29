---
title: "Message Authentication Code (MAC)"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[hashing]]", "[[symmetric-encryption]]", "[[information-assurance]]"]
---

## One-line Summary
A Message Authentication Code (MAC) is a symmetric-key tag that proves a message came from a holder of the shared secret and was not modified — HMAC-SHA256 is the most common, with CMAC (block-cipher based) and GMAC (GCM's authentication component) as the other standard variants; MACs provide integrity and data-origin authentication but **not** non-repudiation.

## Core Intuition
A MAC is the symmetric equivalent of a digital signature, but with a critical limitation: both the sender and the receiver share the same key k, so the receiver could have produced the same MAC themselves. This means the sender can later deny having sent the message ("anyone with k could have produced that tag"). For non-repudiation, you need an asymmetric signature.

But for *integrity* and *data-origin authentication* — meaning "this message came from someone who knows k and has not been modified" — a MAC is exactly what you want. And it's *much* faster than a signature (hash-based HMAC is ~1000× faster than ECDSA).

In IoT, MACs are everywhere:
- **TLS record authentication**: HMAC-SHA256 (TLS 1.2) or AES-GCM (TLS 1.3, which is technically an AEAD, not a standalone MAC)
- **Firmware integrity**: HMAC-SHA256 of the firmware image, signed by the manufacturer
- **Sensor data authentication**: HMAC over each sensor reading, so the receiver knows it wasn't tampered with
- **API request signing**: AWS SigV4, OAuth JWT signatures (HMAC-based)
- **Authenticated boot**: each boot stage verifies the next with a MAC

The lecture highlights three flavours of MAC:

1. **HMAC (Hash-based MAC)**: HMAC-SHA1, HMAC-SHA256, HMAC-SHA512. The most widely used. The construction (H(k ⊕ opad ‖ H(k ⊕ ipad ‖ m))) is provably secure if the underlying hash is a PRF.
2. **CMAC (Cipher-based MAC)**: CMAC-AES, CMAC-3DES. Uses a block cipher in CBC-like mode, outputs a tag the size of the block (128 bits for AES).
3. **GMAC (Galois MAC)**: the authentication component of GCM mode of AES. Specialised for high-speed authenticated encryption.

## Formal Definition / Statement

A MAC is a pair of algorithms:
- **Tag**(k, m) → t  (also written MAC(k, m))
- **Verify**(k, m, t) → {accept, reject}

with correctness: Verify(k, m, Tag(k, m)) = accept.

**Security**: EUF-CMA (existential unforgeability under chosen-message attack). The adversary can request tags for any messages of their choice, and wins if they produce a valid tag for any *new* message. A secure MAC has success probability ≤ 2^(-n) + q/2^n where n is the tag length and q is the number of queries.

**HMAC construction (RFC 2104):**
```
k' = k if |k| = block_size, else k' = H(k) padded to block_size
ipad = 0x36 repeated block_size/8 times
opad = 0x5c repeated block_size/8 times
HMAC(k, m) = H((k' ⊕ opad) ‖ H((k' ⊕ ipad) ‖ m))
```

For HMAC-SHA256: block_size = 512 bits, output = 256 bits.
For HMAC-SHA1: block_size = 512 bits, output = 160 bits (legacy, deprecated).

**CMAC construction (NIST SP 800-38B):**
- Uses a block cipher (AES or 3DES) in CBC mode
- Generates two subkeys K1, K2 from the encryption of zero
- For message m split into blocks m_1, ..., m_n:
  - c_0 = 0
  - c_i = E_K(m_i ⊕ c_{i-1})
  - if m_n complete: t = E_K(m_n ⊕ c_{n-1} ⊕ K1)
  - if m_n partial: t = E_K((m_n ‖ 10...0) ⊕ c_{n-1} ⊕ K2)
- Output tag length = block size (128 bits for AES-CMAC)

**GMAC (NIST SP 800-38D):**
- Special case of GCM mode where there is no plaintext to encrypt
- Uses GHASH (a universal hash over GF(2^128)) with a secret key H = E_K(0^128)
- Tag is computed over (AD, ciphertext) using GHASH
- The H in GHASH must be kept secret — this is why reusing a key/nonce in GCM leaks the auth key

## Key Properties / Complexity

| Property | HMAC-SHA256 | CMAC-AES | GMAC |
|---|---|---|---|
| Primitive | Hash (SHA-256) | Block cipher (AES) | Block cipher (AES) + GHASH |
| Tag length | 256 bits | 128 bits | 128 bits |
| Speed (software, modern CPU) | ~1-2 GB/s | ~1 GB/s | ~5 GB/s |
| Output expansion | 32 bytes | 16 bytes | 16 bytes |
| Nonce requirement | None | None | Unique per key |
| Key size | any | 128/192/256 bits | 128/192/256 bits |

- **Provides**: integrity, data-origin authentication
- **Does NOT provide**: non-repudiation (both parties share k), confidentiality (the message is sent in clear unless encrypted separately)
- **Replay protection**: MACs do not prevent replay attacks by themselves. Add a nonce, sequence number, or timestamp to the authenticated data.
- **Length extension attack**: HMAC is *not* vulnerable (that's the design's whole point — to fix the vulnerability in H(secret ‖ message)). Naive MACs like H(secret ‖ message) are vulnerable.

## Worked Example

**HMAC-SHA256 used for IoT sensor authentication (Mexis et al. demonstrator):**
```
master device sends: TimeRequest
slave device returns: timeResponse, timestamp, HMAC(K, "timeResponse"||timestamp)

attacker can:
  - see the timestamp (no confidentiality)
  - replay the exact message (no replay protection — needs nonce or sequence)
  - not modify the message (would invalidate HMAC)
  - not forge a new message (would need K)
```

This is the authentication part of the Mexis et al. architecture. The encryption is separate (AES-128-CBC over the data payload).

**AES-GCM providing both encryption and authentication (an AEAD):**
```
key = 128-bit symmetric key
nonce = 96-bit unique value
plaintext = data to encrypt
associated_data = header to authenticate but not encrypt
→ (ciphertext, tag) = AES-GCM(key, nonce, plaintext, associated_data)
→ ciphertext length = plaintext length
→ tag = 128 bits
```

GCM is the dominant authenticated encryption mode in TLS 1.3, modern IoT protocols, and disk encryption. It is an *AEAD* (authenticated encryption with associated data), combining confidentiality and authentication in one primitive.

## Common Pitfalls

- **MACs are not signatures**: cannot prove authorship to a third party. Use digital signatures for that.
- **Reusing a nonce in GMAC/GCM**: catastrophic. Leaks the authentication key H, allowing arbitrary forgery. The number-one crypto deployment bug.
- **Naive MAC = H(secret ‖ message)**: vulnerable to length extension attacks. Use HMAC.
- **MAC without replay protection**: a captured (message, tag) pair can be re-sent. Add a nonce, sequence number, or timestamp.
- **MAC with weak key**: short keys (e.g., 64-bit HMAC) can be brute-forced. Use the full hash output size.
- **Tag comparison timing attack**: comparing tags byte-by-byte leaks matching prefix. Use a constant-time compare.
- **Encrypting with one algorithm and MACing with another without a proven composition**: use encrypt-then-MAC, or better, use an AEAD mode like GCM that does both right.

## Connections
- [[information-assurance]] — integrity, authentication (not non-repudiation)
- [[digital-signatures]] — asymmetric equivalent; provides non-repudiation
- [[hashing]] — the underlying primitive for HMAC
- [[symmetric-encryption]] — the underlying primitive for CMAC/GMAC
- [[key-management-lifecycle]] — shared key distribution is the operational challenge
- [[physical-unclonable-functions]] — can generate the shared key without storing it
- [[ota-updates]] — firmware integrity verification
- [[mqtt-security]] — TLS uses HMAC-SHA256 in older suites, AES-GCM (an AEAD using GMAC) in TLS 1.3
- [[zigbee-security-model]] — AES-CCM* uses AES-CMAC for authentication
- [[iot-lecture-6]] — source lecture
- [[iot-lecture-3]] — authentication attacks (L3) and the cryptographic defences (L6)

## Open Questions
- For constrained devices, is HMAC-SHA256/64 (truncated to 64 bits) acceptable for some use cases? (Yes, in some protocols like TLS 1.3, with a clear security argument.)
- When should one use a standalone MAC vs. an AEAD? (AEAD is preferred — you don't have to worry about composition. Use HMAC only when AEAD is not available, e.g., when you only need authentication and have no encryption.)
