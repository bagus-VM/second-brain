---
title: "Dynamic Code Rewriting — Code That Is Not in the Binary Until It Has to Be"
tags: [concept, reverse-and-reengineering, semester-2, obfuscation, runtime]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[code-obfuscation]]", "[[static-vs-dynamic-analysis]]", "[[process-memory-layout]]"]
---

## One-line Summary
The strongest anti-analysis move is not to hide the code's meaning but to keep the code out of the file entirely: transform it at build time and reverse the transformation at run time, or generate it at run time and never store it at all.

## Core Intuition
Static analysis is a claim about a file. Dynamic code rewriting breaks the claim by making the file stop being the program: "modifying/packing/encrypting actual code, reverse transformation at runtime", so that the actual code "is not available in binary for disassembly, only at runtime" (slide 10). The three motivations the slide gives are the usual ones, stated from the owner's side — protect intellectual property (a secret algorithm, copy protection), hide application secrets ("magic keys" for special APIs, decryption keys for media decoding) and hide malicious behaviour.

The strongest form escalates past transformation: **code generated at runtime is invisible to reverse-engineering efforts** (slide 11). Nothing is encrypted because nothing was ever written down. The price of that is the analyst's price too — there is no artifact to examine, only a process to watch.

This is where the course's two halves meet. The Virtual Machines course showed a runtime system that *builds* code ([[dynamic-linking]]'s `dlopen`, the JIT of the exercises); this lecture shows the same mechanism used as an anti-analysis device. The mechanism does not care about the intent.

## Formal Definition / Statement
**Dynamic code rewriting (slide 10).** Modifying, packing or encrypting the actual code, with the reverse transformation performed at runtime — the general mechanism of which [[binary-packing]] is one implementation. Purposes, verbatim from the slide: protect intellectual property (e.g. secret algorithm, copy protection); hide application secrets ("magic keys" for special APIs, decryption keys e.g. for media decoding); hide malicious behaviour.

**Generating code at runtime (slide 11).** Three sub-mechanisms, each with its own consequence for the analyst:

- **Dynamic code loading.** "Code is (down-)loaded at runtime and integrated in memory" — which "requires dumping of memory image before reverse engineering". The artifact to analyse is a process image, not a file.
- **Self-modifying code.** "Code modified at runtime, potentially multiple times between executions of same functionality" — so the slide's warning is about *reproducibility*: two runs may contain different code. "Manual effort required, unsetting W XOR X property of code", i.e. the page must be made writable and executable at once, in some order, which is precisely the property the operating system tries to prevent.
- **Packing/encryption.** "Popular with malware, defeats simple pattern detection"; free and commercial implementations are available.

## Key Properties
- **The binary on disk is not the program.** Everything static analysis produces — listing, CFG, strings — describes a template, not behaviour.
- **The observation point moves to the process.** Dumping a memory image becomes mandatory, which is why the previous slide's unpacking discussion is the practical counterpart.
- **Self-modifying code defeats reproducibility, not just readability.** "Potentially multiple times between executions of same functionality" means one dump is one sample of the code.
- **W^X is the obstacle and unsetting it is the technique.** The write/execute split exists to stop exactly this; unsetting it is "manual effort", not a bug.
- **The same mechanism is legitimate.** JIT compilers, dynamic loaders and packers all rewrite or generate code at runtime; only the purpose differs, and the analyst has to establish which one they are looking at.
- **It is the top of the escalation ladder.** Obfuscation hides meaning, packing hides bytes, runtime generation hides existence — and the summary's superlinear-cost claim (slide 22) is the reason the ladder is worth climbing for the owner.

## Worked Example
"Code generated at runtime is invisible to reverse engineering" is easy to say and worth demonstrating. The following 25-line program builds a function in memory at runtime — six bytes, `mov eax, 42; ret` — and calls it. Written for this page and run on this host (WSL/Ubuntu 22.04, built with `zig cc` for `x86_64-linux-gnu.2.35`):

```c
#define _DEFAULT_SOURCE
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

static const unsigned char payload[] = {0xb8, 42, 0x00, 0x00, 0x00, 0xc3};  /* mov eax,42; ret */

int main(void) {
    long page = sysconf(_SC_PAGESIZE);
    unsigned char *code = mmap(NULL, page, PROT_READ | PROT_WRITE,          /* step 1: W, not X */
                               MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    memcpy(code, payload, sizeof payload);
    mprotect(code, page, PROT_READ | PROT_EXEC);                            /* step 2: X, not W */
    int (*f)(void) = (int (*)(void))code;
    printf("calling the generated function -> %d\n", f());
    return 0;
}
```

```
$ ./jit
generated 6 bytes at 0x7aa85615e000 (W, not X): writing to it is allowed, executing it would fault
now PROT_READ|PROT_EXEC: the bytes on disk never contained this code
calling the generated function -> 42
```

The address varies per run; the point does not. The six payload bytes are in the file exactly once, at offset `0x5f3` — as data, in the generator's own initialiser:

```
$ python3 -c 'd=open("jit","rb").read(); print(len(d), d.count(bytes.fromhex("b82a000000c3")), hex(d.find(bytes.fromhex("b82a000000c3"))))'
12528 1 0x5f3
```

That is the honest version of the slide's claim: the bytes are findable, but nothing in the file's metadata says they are a function, that they are copied into an anonymous page, or that the page is later made executable. A generator that *computes* its output rather than tabulating it leaves even less. Static analysis can find the generator; only the running process shows the generated code — and this demo is the two-step `mprotect` the slide calls "unsetting W XOR X".

## Common Pitfalls
- **Reading "invisible to reverse engineering" as "invisible to all analysis".** It is invisible to *static* analysis of the file. The dynamic answer — dump the image, analyse the dump — is the previous slide's technique, and it works (see [[binary-packing]]).
- **Assuming a memory dump is complete or representative.** Self-modifying code can be modified several times per execution, so one dump is one instant of one path.
- **Treating W^X bypass as a malware trick.** JITs do it legitimately; the interesting question is whether the generated code came from a generator the analyst can also run, or from a secret the analyst does not have.
- **Confusing this with plain obfuscation.** Constant unfolding and opaque predicates leave the code static ([[code-obfuscation]]); this family changes what is on disk.
- **Forgetting the loader.** Dynamic code loading reuses the machinery of [[dynamic-linking]] — a library loaded at runtime has to leave the file, be mapped, be relocated and be initialised.

## Connections
- [[code-obfuscation]] — the parent taxonomy; this is the branch that hides the code rather than its meaning.
- [[binary-packing]] — the packaged instance of "encrypt now, decrypt at load time", with the unpacking stub as the visible residue.
- [[static-vs-dynamic-analysis]] — the distinction the whole family is built to exploit: the file is static, the code is not.
- [[process-memory-layout]] — where generated code has to live, and why its page permissions matter.
- [[dynamic-linking]] — the legitimate mechanism this reuses: load at runtime, map, relocate, resolve.
- [[runtime-system]] — the C runtime and dynamic loader from the Virtual Machines course, which do this by design.
- [[disassembly]] — runtime generation is the limit case of the disassembler's problem: there is nothing to disassemble at load time.
- [[reverse-and-reengineering-lecture-4]] — the slides these points come from.
- [[elf-executable-format]] — the file whose metadata is complete on disk and incomplete at runtime.

## Open Questions
- **The slide never says how generated code is analysed in practice.** Dumping a memory image is named, but the problem of *finding* the generated region in a dump — versus megabytes of library mappings — is not addressed.
- **How "unsetting W XOR X" is done** — a single `mprotect` or a dual mapping — is left as "manual effort", with no slide showing the mechanism.
- **Whether self-modifying code in the wild is compiled from a higher-level language at runtime** or patched byte-wise is not distinguished; the two imply different counter-measures.
- **Anti-debugging is named as a dynamic-analysis obstacle** in the packing slide and never described; this page can only point at it.
- **The course gives no example of a real JIT or packer to study**, so everything here is mechanism rather than tooling. Whether a lab follows is unknown from `raw/`.
- **No distinction is drawn between obfuscation-as-product and obfuscation-as-malware-technique**, although the slide's motivation list ("hide malicious behaviour") clearly has both in mind; the exam's position on the distinction is unstated.
