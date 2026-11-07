---
title: "Advanced IT Security — Lecture 2: Cryptography Continued (Checksums, the Birthday Bound, MD5/SHA History, MACs, Encryption)"
tags: [topic, advanced-it-security, semester-2, lecture, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-07
prerequisites: ["[[advanced-it-security-lecture-1]]"]
---

## One-line Summary
The continuation of the same cryptography deck (slides 18–55): what a checksum is and is not, the
birthday bound and brute-force complexity, how hash functions are built and how MD4/MD5/SHA-1 were
broken, what that breaks in practice (certificates), how to build a MAC correctly, and — in the last
four slides — the first statement of symmetric encryption and cryptanalysis.

## Core Map

```
Advanced IT Security — Lecture 2, "Introduction to Cryptography" continued (35 pages, 20261105_1_Symmetric.pdf)
│
├── Checksums (18–20)
│   ├── hash value = message digest = checksum
│   ├── CRC is NOT a cryptographic hash — designed for transmission errors
│   └── use cases: integrity/signatures (OWHF) · file identification · passwords ·
│       key derivation · MACs · pseudorandom generation (CRHF)
│
├── Attack cost (21–22)
│   ├── pre-image / 2nd pre-image: O(2ⁿ)
│   ├── collision: O(2^(0.5n)) — the birthday paradox
│   └── 1 Gops/s × 100 ops × 1000 units: 2⁶⁴ ≈ 50 h · 2⁸⁰ ≈ 380 y · 2¹²⁸ ≈ 10¹⁷ y
│           -> [[birthday-bound]]
│
├── Construction (23–25, 46)
│   ├── compression function f on fixed-size blocks, hᵢ = f(xᵢ‖hᵢ₋₁), padding
│   ├── docs: "no good theory for general design (so far)"
│   ├── 50+ broken schemes; MD4/MD5 broken; SHA-*; RIPEMD-160; SHA-3 (Keccak)
│   └── SHA-512 round functions Ch, Maj, Σ, σ
│           -> [[merkle-damgard-construction]]
│
├── History and impact (29–33)
│   ├── 1990–2005 timeline: MD4 → Dobbertin → Wang et al. → SHA-1 attacks
│   ├── MD5: pseudo-collision → compression-function collision →
│   │   identical-prefix (128 bytes) → chosen-prefix (716 bytes) → 2^123.4 preimage
│   └── what it buys an attacker: 2 colliding executables · postscript ·
│       RSA keys/X.509 certs · arbitrary files for 100 K$ · rogue CA cert
│
├── MD5 / SHA-1 / SHA-512 (47–51)
│   └── parameters and the round function's mixture of rotations, XOR, AND, +
│
├── MACs (41–45)
│   ├── hash has no key → integrity values must be protected
│   ├── secret prefix / suffix / envelope, and their analyses
│   └── HMAC(x) = h(k⊕o_pad ‖ h(k⊕i_pad ‖ x)) — RFC 2104
│           -> [[hmac]]
│
└── Encryption and cryptanalysis (52–55)
    ├── e_K(x), d_K(x), x = d_K(e_K(x)); one shared secret key
    ├── domains of trust at both ends, area of attack in the middle
    ├── cryptanalysis = plaintext from ciphertext without the key
    └── assume the algorithm is known; obscurity is the wrong bet
            -> [[symmetric-encryption]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[birthday-bound]] | Collisions cost 2^(n/2), pre-images 2ⁿ — half the bits is the real security level |
| [[merkle-damgard-construction]] | Iterate a fixed-size compression function over padded blocks; no design theory |
| [[hmac]] *(Semester 1, IoT Security)* | Keyed hash as h(k⊕o_pad ‖ h(k⊕i_pad ‖ x)), because naive key concatenation fails — the fuller treatment, since this deck gives only the formula and the citations |
| [[symmetric-encryption]] *(Semester 1, IoT Security)* | One shared key, two domains of trust, and the attacker knows the algorithm — AES and lightweight ciphers are on that page; this deck stops at the model |
| [[cryptographic-hash-functions]] | Properties from lecture 1 that this deck starts from (slide 18 recaps them) |
| [[mdc-vs-mac]] | The unkeyed/keyed split the MAC half of this deck builds on |

## Lecture Structure

| Slide | Content |
|-------|---------|
| 18 | Recapitulation: the OWHF and CRHF property lists |
| 19 | Checksums: the third name for a digest, and why CRC is not one |
| 20 | Use cases of cryptographic hashes, annotated by which property they need |
| 21 | The birthday paradox, in urn form |
| 22 | Complexity of brute-force attacks, with the 10¹⁴ ops/s illustration |
| 23 | Construction: compression function, padding, iteration |
| 24 | A typical hash architecture (message → compression → hash value) |
| 25 | Constructions in use: 50+ broken schemes, MD4/MD5, SHA-*, RIPEMD-160, SHA-3 |
| 26–28 | Performance, and "hash functions – real life…" pointers (image slides) |
| 29 | History of hash functions, 1990–2005, in eleven dated lines |
| 30 | History of MD5, and its four escalating attacks |
| 31 | Impact of collisions: what an attacker can actually build |
| 32 | The rogue CA certificate: two challenges, 200 PS3s, ≈ $20 000 of EC2 |
| 33–40 | Image slides (the certificates and the attack) — no extractable text |
| 41 | MACs: hashes have no key, so integrity values must be protected |
| 42 | The three simple constructions and the security-analysis citation |
| 43 | RFC 2104 (link only) |
| 44 | The HMAC construction |
| 45 | Image slide |
| 46 | Internals: compression function, iteration, rotations/XOR/AND/+, no design theory |
| 47 | MD5: 1991, 2004 collisions, 2008 practical certificate collision |
| 48 | SHA-1: NSA design, 1993/1995, 160-bit, 2005 flaws, SHA-2 as 256/512 extensions |
| 49–51 | SHA-512 overview and round function (Ch, Maj, Σ, σ) |
| 52 | Encryption: confidentiality, e_K(x), d_K(x) |
| 53 | Symmetric key encryption picture |
| 54 | The symmetric system diagram: domains of trust, area of attack, key generation |
| 55 | Cryptanalysis and the case against security by obscurity |

## Exam-Relevant Points

1. **CRC ≠ cryptographic hash.** The single sentence worth memorising: "a cyclic redundancy check
   (CRC) is not a cryptographic hash function: CRCs are designed for detecting transmission errors."
2. **The complexity table** — pre-image and second pre-image O(2ⁿ), collision O(2^(0.5n)) — plus the
   three time estimates at 10¹⁴ ops/s (50 hours, 380 years, 10¹⁷ years).
3. **The construction is three lines**: compression function on fixed-size blocks, padding of the last
   block, hᵢ = f(xᵢ ‖ hᵢ₋₁) from a fixed h₀, digest = hₘ.
4. **"No good theory for general design"** is the deck's own admission and a fair exam answer about why
   hash designs are argued by cryptanalysis.
5. **The MD5 escalation ladder** is the most concrete case study in the course: pseudo-collision (1993)
   → compression-function collision (1996) → identical-prefix (2004) → chosen-prefix (2006) →
   certificate collision (2008) → theoretical pre-image 2^123.4 (2009).
6. **What a collision buys** is a list to reproduce: two colliding executables, two postscript
   documents, two colliding RSA public keys (hence X.509 certificates), two arbitrary colliding files
   for 100 K$, and a rogue CA certificate (1–2 days on 200 PS3s, ≈ $20 000 on EC2).
7. **The three naive MAC constructions and their names** — secret prefix h(k‖m), secret suffix h(m‖k),
   secret envelope h(k₁‖m‖k₂) — and the HMAC formula with the two padding fields.
8. **Why encryption alone is not enough** is set up here and cashed in by exercise 2: confidentiality is
   one service, the diagram's "area of attack" still carries deletion and insertion.
9. **Cryptanalysis's stance**: assume the attacker knows the algorithm; security depends on the key.
   The mattress/safe analogy is the answer to "isn't publishing the algorithm dangerous?".

## Connections

- [[advanced-it-security-lecture-1]] — the deck this continues (slides 1–16: definitions, paradigms,
  services, hash properties). Slide 18 here recaps its last three slides verbatim.
- [[advanced-it-security-exercise-2]] — the sheet examined on 05.11.2026, the same day this deck was
  published; its question 2(d) is the 32-bit instance of the birthday bound.
- [[birthday-bound]], [[merkle-damgard-construction]] — the two pages this deck produced.
- [[hmac]] and [[symmetric-encryption]] — **existing Semester 1 pages** (IoT Security), deliberately not
duplicated here: they carry the construction analysis and the cipher landscape, while this deck supplies
only the formula, the three naive MAC constructions and the trust-domain model. The one thing the
Semester 1 page does not have is slide 55's stance, quoted above: "always assume attackers know the
algorithms used … security should depend on secrecy of the key, not the algorithm".
- [[cryptographic-hash-functions]], [[mdc-vs-mac]] — lecture 1's pages, extended here.
- [[unconditional-vs-conditional-security]] — every cost estimate on slides 21–22 is a conditional
  claim.
- [[advanced-it-security-exercise-1]] — the CIA classification discipline that question 1(d) of sheet 2
  applies to encryption.
- `raw/lectures/Advanced IT Security/Vorlesung/20261105_1_Symmetric.pdf` — the source (35 pages,
  extracted 2026-11-07).

## Open Questions

- **The deck is still not about symmetric cryptography**, despite the file name. It ends at slide 55
  introducing encryption; no cipher, mode, key length or construction detail is given, so agenda item
  3 remains untaught.
- **Slides 33–40 and 45 are image-only**, so the rogue-CA-certificate walkthrough and the MAC diagram
  are not recoverable as text — the certificates' details (issuer, validity, the two colliding
  requests) are lost in extraction.
- **The birthday-paradox formula on slide 21 extracts as garbage** ("the expected number of draws
  before a previously drawn number appears is …"), so the exact expression is not verified against the
  slide; ≈ √(πm/2) is the standard result.
- **The MD5 pre-image figure 2^123.4 is labelled "theoretical"** — whether it was ever run is not
  stated.
- **The 100 K$ price for arbitrary colliding files and the $20 000 EC2 equivalent are undated**;
  whether they are 2004–2008 figures or later is not said, and they are certainly not current.
- **HMAC's security analysis is cited but not shown**, so the reasoning about length extension and
  collision attacks has to be reconstructed from the RFC/papers, not from the slides.