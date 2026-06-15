---
title: "HMAC (Hash-based Message Authentication Code)"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[hashing]]", "[[message-authentication-code]]", "[[symmetric-encryption]]"]
---

## One-line Summary
HMAC (Hash-based MAC, RFC 2104) is the standard construction for a [[message-authentication-code]] using a cryptographic hash function — HMAC-SHA256 is the most widely deployed variant, with HMAC-SHA1 and HMAC-SHA384/512 as the other versions; the construction H(k⊕opad ‖ H(k⊕ipad ‖ m)) is provably secure as a PRF and avoids the length-extension vulnerability of naive H(secret ‖ message).

## Core Intuition
HMAC is the *one MAC construction to rule them all*. It takes a cryptographic hash (SHA-256, SHA-1, SHA-512) and a key k, and produces a fixed-size tag that proves the message came from a holder of k and was not modified.

The construction looks weird on first glance:

```
HMAC(k, m) = H((k ⊕ opad) ‖ H((k ⊕ ipad) ‖ m))
```

where ipad = 0x36 repeated and opad = 0x5c repeated, each the size of the hash's internal block.

Why two hashes with two pads? **To defeat the length-extension attack on naive H(secret ‖ message)**. If the hash is built from a Merkle-Damgård construction (SHA-1, SHA-2), then given H(secret ‖ m), an attacker can compute H(secret ‖ m ‖ x) for any x *without knowing the secret*. This is because the hash's internal state after processing secret ‖ m is exposed in the digest, and the attacker can resume from that state. HMAC defeats this by hashing the key twice with different pads, so the attacker never sees the internal state at a useful point.

The proof (Bellare, Canetti, Krawczyk 1996) shows HMAC is a secure PRF as long as the underlying hash has certain weak properties — no need to assume collision resistance. This is why HMAC has held up even after MD5 and SHA-1 were broken for collision resistance.

For the Mexis et al. paper, HMAC-SHA-256 is the authentication primitive over time messages. The same construction is used in TLS, IPsec, JSON Web Tokens, AWS SigV4, and a hundred other places.

## Formal Definition / Statement

**HMAC (RFC 2104):**

Inputs:
- k: key (any length up to block_size bytes; keys longer than block_size are pre-hashed)
- m: message (any length)
- H: cryptographic hash with block_size and output_size (e.g., SHA-256: block=64 bytes, output=32 bytes)
- ipad = byte 0x36 repeated block_size times
- opad = byte 0x5c repeated block_size times

```
k' = k if |k| == block_size, else H(k) padded with zeros to block_size
inner  = H((k' ⊕ ipad) ‖ m)         # first hash, ipad-mixed key
outer  = H((k' ⊕ opad) ‖ inner)      # second hash, opad-mixed key
return outer
```

**HMAC-SHA256 (the default):**
- Hash: SHA-256
- Block size: 64 bytes
- Output size: 32 bytes
- Key size: any (typically 32 bytes, same as the output)

**HMAC-SHA384 / HMAC-SHA512 (higher security):**
- Hash: SHA-384 or SHA-512
- Block size: 128 bytes
- Output size: 48 or 64 bytes

**HMAC-SHA1 (legacy):**
- Hash: SHA-1
- Block size: 64 bytes
- Output size: 20 bytes
- Status: deprecated in modern protocols (TLS 1.3 removes HMAC-MD5 and reduces HMAC-SHA1 use)

**Security property (RFC 2104, Bellare et al. 1996):**
HMAC is a secure PRF (pseudorandom function) if the compression function of H is a secure PRF. This is a weaker assumption than collision resistance on H, which is why HMAC-HMAC-SHA1 remains secure in some contexts even after SHA-1 collisions were found.

## Key Properties / Complexity
- **Provable security**: as secure as a PRF built from the compression function of the hash
- **Length-extension safe**: defeats the attack on naive H(secret ‖ message)
- **Fast**: ~1-2 GB/s software on modern CPU; slower on small MCUs but still practical
- **No nonce required**: unlike AES-GCM, HMAC is stateless and does not need a nonce
- **Key size**: any, but typically matches the output size (32 bytes for HMAC-SHA256)
- **Output size**: equals the hash output (32 bytes for HMAC-SHA256)
- **Replay protection**: must be added separately (sequence number, timestamp, nonce in the authenticated data)

## Worked Example

**Mexis et al. demonstrator — authenticated time sync:**
```
1. Master → Slave: TimeRequest
2. Master → Slave: TimeResponse + nonce + timestamp
3. Slave authenticates: ok = HMAC-SHA256(K, "TimeResponse"||nonce||timestamp) == tag?
4. If ok, slave has a trusted time value to use for subsequent data messages
```

An attacker can see the time (no confidentiality), but cannot forge a different time (would invalidate the tag), and cannot replay the same time later (the nonce ensures freshness).

**TLS 1.2 record authentication (HMAC-SHA256):**
```
mac_key = derived from handshake
seq_num = 64-bit sequence number
plaintext = record payload
mac = HMAC-SHA256(mac_key, seq_num || type || version || length || plaintext)
```

This is the "MAC-then-encrypt" pattern that TLS 1.2 used (and that TLS 1.3 replaced with AEAD). HMAC authenticates the record; encryption is separate (AES-CBC, AES-GCM, ChaCha20).

**Hot-patch for length-extension vulnerability:**
```
insecure:  tag = SHA-256(secret || message)
secure:    tag = HMAC-SHA-256(secret, message)
```

The two give the same output for *valid* messages, but only HMAC-SHA-256 prevents the attacker from computing the tag for `message || attacker_chosen_extension` without knowing the secret.

## Common Pitfalls
- **Using H(secret ‖ message) instead of HMAC**: vulnerable to length-extension for Merkle-Damgård hashes (SHA-1, SHA-2). Use HMAC.
- **HMAC-SHA1 in new designs**: deprecated. Use HMAC-SHA256 minimum.
- **Reusing the same key for HMAC and as the key in another construction**: bad practice. Use separate keys for separate purposes (e.g., a key derivation function to derive subkeys).
- **Short HMAC keys**: < 128-bit effective security is brute-forceable. Use a full 256-bit key for HMAC-SHA256.
- **Missing replay protection**: HMAC authenticates a message but does not prevent replay. Always bind a nonce, sequence number, or timestamp to the authenticated data.
- **Confusing HMAC with HKDF**: HMAC is a MAC. HKDF (HMAC-based Key Derivation Function) uses HMAC *internally* but its purpose is key derivation, not authentication. Don't use HKDF as a MAC.
- **Truncating the HMAC tag**: if you only need 128 bits, you can use the first 128 bits of HMAC-SHA256, but use the full 256 bits when you can.

## Connections
- [[hashing]] — HMAC is built on top of a hash
- [[message-authentication-code]] — HMAC is the standard hash-based MAC
- [[symmetric-encryption]] — HMAC is the symmetric authentication primitive
- [[digital-signatures]] — asymmetric equivalent
- [[ascon]] — ASCON provides integrated AEAD (no need for separate MAC)
- [[lightweight-cryptography]] — HMAC-SHA256 is too heavy for the smallest devices; lightweight MACs (Chaskey, SipHash) exist
- [[mqtt-security]] — TLS uses HMAC-SHA256 in older cipher suites
- [[ota-updates]] — firmware integrity verification with HMAC
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. use HMAC-SHA-256 for time authentication
- [[paper-iot-mexis-2021-poster]] — same
- [[iot-lecture-6]] — source lecture, lists HMAC-SHA1, HMAC-SHA256, CMAC, GMAC as MAC examples

## Open Questions
- For the smallest IoT devices, is HMAC-SHA256/64 (truncated to 64 bits) acceptable, or should a true lightweight MAC (Chaskey) be used?
- Does the exam want the full HMAC construction (H(k⊕opad ‖ H(k⊕ipad ‖ m))), or just the name and purpose?
