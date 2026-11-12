---
title: "Classical Cipher Cryptanalysis"
tags: [concept, cryptography, semester-2, advanced-it-security]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[symmetric-encryption]]"]
---

## One-line Summary
Classical ciphers can have many possible keys yet remain insecure when their transformations preserve patterns that ciphertext analysis can exploit.

## Core Intuition
Security is not measured by key count alone. A substitution cipher changes the symbols but preserves repeated-letter and frequency patterns; a transposition changes positions but keeps the symbols. Those regularities give an attacker evidence about the plaintext.

## Formal Definition / Statement
Cryptanalysis is the recovery of plaintext or key information without the secret key, using the cipher's structure and available observations. The lecture's examples include frequency analysis against monoalphabetic substitution, splitting a Vigenère ciphertext by key period into Caesar-like streams, and known-plaintext reasoning against Enigma's rule that no letter maps to itself.

## Key Properties
- Monoalphabetic substitution applies one fixed permutation to each alphabet symbol; repeated plaintext symbols remain repeated ciphertext symbols.
- Homophonic substitution maps symbols to multiple ciphertext symbols to flatten frequencies, but known plaintext/ciphertext can still reveal the mapping.
- Vigenère varies the Caesar shift by position; if the key length is known, each residue class can be analyzed as a Caesar cipher.
- Transposition permutes positions but does not change the letters themselves.
- Combining substitutions with transpositions can add complexity, but a larger key space alone does not prove security.
- Enigma's operational and structural weaknesses mattered alongside the amount of available ciphertext and adversary effort.

## Worked Example
With a Vigenère key of length four, group ciphertext characters by positions 1, 5, 9, …; 2, 6, 10, …; and so on. Each group uses a fixed Caesar shift, so frequency analysis can attack the groups separately. This illustrates why knowing the period changes the attack, not a full recovered plaintext.

## Common Pitfalls
- Equating a large key space with a secure cipher.
- Assuming that hiding letter frequencies is the same as removing all exploitable structure.
- Treating historical Enigma's key count as its whole security argument.
- Confusing a transposition (position changes) with substitution (symbol changes).

## Connections
- [[advanced-it-security-lecture-3]] — source lecture and examples of Caesar, substitution, Vigenère, transposition and Enigma.
- [[cryptographic-security-games]] — formalizes attacker knowledge and the information available during an attack.
- [[symmetric-encryption]] — the shared-key family that includes these historical ciphers.

## Open Questions
- The lecture provides historical examples rather than formal security reductions or modern attack complexities.
- It does not specify the exact Enigma key-space calculation assumptions behind the printed value.
