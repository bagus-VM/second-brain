---
title: "ELF Symbols and Symbol Tables"
tags: [concept, reverse-and-reengineering, semester-2, elf, symbols]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-29
prerequisites: ["[[elf-executable-format]]"]
---

## One-line Summary
A compiler emits names as well as machine code: each symbol record holds a string-table index, a packed binding-and-type byte and a section index, and while the linker's global symbol table can be stripped away, the dynamic symbol table through which external references are resolved cannot be removed.

## Core Intuition
Slide 29 gives the reason symbols matter: the compiler generates more than just code, and symbolic information recovered from the source can improve the interpretation of machine code. A linker refers to the symbol table to match, reference or modify a symbol; a debugger needs symbols to match variable and function names; and because symbols are so useful, anti-analysis tools remove as many of them as possible. The presence, absence or survival of symbols is therefore itself evidence about a binary.

The mechanism is one indirection. Names live in a separate string table, and each symbol stores an index into it — that is `st_name`. The rest of the record says what the name refers to: visibility (the binding) and kind (the type) are packed into `st_info`, and the owning section is `st_shndx`, with a special undefined value meaning the symbol is external and comes from elsewhere (slide 29).

## Formal Definition / Statement
Slide 29 ("ELF Symbols") gives the fields of a symbol:

- `st_name` — index into the symbol name string table.
- `st_info` — the bind (linker visibility): local, global, (global) weak; and the type: object (variable), func (function), section (ELF section).
- `st_shndx` — the associated section type: undef (external), progbits (in the current object), symtab (symbol table).
- Linkers refer to the symbol table to match, reference or modify a symbol; debuggers need symbols for better matching of variable and function names; anti-analysis tools remove as many symbols as possible.

Slide 30 ("Symbol Tables") bounds the number: at most two symbol tables per ELF object, `.symtab` and `.dynsym`.

- `.symtab` — the binary's global symbol table. Its strings live in the section `.strtab`, holding null-terminated strings referenced from a different section, one per symbol of `.symtab`.
- `.dynsym` — required for dynamic linking of external objects. Its corresponding string table is `.dynstr`.
- `.symtab` can be removed. `.dynsym` cannot, unless nothing is dynamically linked.

Slide 26 names the same sections from the other direction: `.symtab` is the global symbol table, `.dynsym` the table of dynamically linked symbols, `.strtab` the string table of `.symtab`, `.dynstr` the string table of `.dynsym`. Slide 31 ("Symbols Example") shows an example whose only legible extracted text is a `.rodata` annotation; its symbol listings are images and did not survive extraction.

## Key Properties
- **Symbols are extra compiler output, not code** (slide 29).
- **Names are indirected.** `st_name` is an index into a string table, so stripping means deleting one table.
- **Binding is a three-way split**: local, global, (global) weak (slide 29).
- **Type is a three-way split**: object, func, section (slide 29).
- **`st_shndx` locates the symbol**, with `undef` marking an external resolved elsewhere.
- **At most two symbol tables**: `.symtab` droppable, `.dynsym` mandatory while the object is dynamically linked (slide 30).
- **Every symbol table has a paired string table** — `.strtab` for `.symtab`, `.dynstr` for `.dynsym` (slides 26, 30).
- **Stripping is graded anti-analysis**: slide 29 has tools remove "as many symbols as possible", so a binary can sit anywhere between fully named and stripped.
- **The dynamic half is not strippable** — slide 33 says metadata for dynamic linking cannot be stripped.

## Worked Example
```sh
$ readelf --dyn-syms /bin/ls
Symbol table '.dynsym' contains 8 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND
     1: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     4: 0000000000004018     8 OBJECT  GLOBAL DEFAULT   25 stdout@GLIBC_2.2.5
     7: 0000000000001129    27 FUNC    GLOBAL DEFAULT   14 main
```

Read with slide 29's vocabulary: `Bind` is `st_info`'s binding and shows all three values — `LOCAL`, `GLOBAL`, `WEAK`. `Type` shows `FUNC` and `OBJECT`. `Ndx` is `st_shndx`: `UND` means undefined/external, the case that needs `.dynsym` at run time, while `14` on `main` and `25` on `stdout` are section indices. `Value` `0x1129` on `main` is its offset in the executable; external symbols have value `0`.

The index indirection is measurable. In the 64-bit ELF layout an `Elf64_Sym` is 24 bytes: `st_name` (4 bytes, offset 0), `st_info` (offset 4), `st_other` (offset 5), `st_shndx` (2 bytes, offset 6), `st_value` (8 bytes, offset 8), `st_size` (offset 16). `st_info` packs binding in the high nibble and type in the low nibble, so `GLOBAL` (1) with `FUNC` (2) is `0x12`, and `WEAK` (2) with `NOTYPE` (0) is `0x20`. `readelf -p .dynstr /bin/ls` dumps the string table those `st_name` indices point into. `strip /bin/ls` removes `.symtab` and `.strtab`, after which `file` reports "stripped"; `readelf --dyn-syms` still works, because `.dynsym` and `.dynstr` are what the dynamic linker needs (slide 30).

## Common Pitfalls
- **Assuming "stripped" means "no symbols".** Stripping deletes `.symtab`; the `.dynsym` names of imported and exported functions remain (slide 33).
- **Looking up `st_name` as if it were a pointer.** It is an index into `.strtab`/`.dynstr`; the same index means different names in the two tables.
- **Reading `st_shndx` as purely "the section's type".** The slide lists `undef`, `progbits`, `symtab`; `progbits` and `symtab` are section types, while `undef` is the undefined index.
- **Expecting `.symtab` to be present.** Optimised or anti-analysed binaries often have only `.dynsym` (slide 29).
- **Forgetting the pairing.** `.symtab` without `.strtab` leaves `st_name` indices pointing nowhere (slide 30).
- **Treating binding and type as one field.** They share `st_info` but answer different questions.
- **Assuming a `WEAK` symbol resolves like a global one.** All three bindings appear in real tables.

## Connections
- [[elf-executable-format]] — the container whose Section Header Table names `.symtab`, `.dynsym` and their string tables.
- [[got-plt-lazy-linking]] — the dynamic linker consumes `.dynsym` and `.dynstr` to resolve the `UND` symbols above.
- [[dynamic-linking]] — why a dynamically linked object must keep `.dynsym`.
- [[binary-reverse-engineering]] — symbol recovery is the system-level metadata slide 13 of lecture 2 lists.
- [[runtime-system]] — the C library whose exported names fill `.dynsym`.
- [[process-memory-layout]] — where `OBJECT` symbols such as `stdout` live once relocated.
- [[reverse-and-reengineering-lecture-2]] — the lecture that supplies slides 00–19 and 36–38 of this deck.

## Open Questions
- **Slide 31's example is unreadable.** Its symbol listings are images; the extraction keeps only a `.rodata` annotation, so what the example demonstrates is not recoverable.
- **`st_shndx`'s value list is inconsistent.** The slide lists `undef`, `progbits`, `symtab` under "associated section type"; `undef` is an undefined *index* while the other two are *section types*.
- **No binding-versus-type value table is given.** The numeric encodings in the Worked Example come from the ELF specification, not the deck.
- **The stripping claim is qualified but not quantified.** Slide 30 leaves open what happens to `.dynsym` in a fully static binary.
- **Nothing says how much name information survives partial stripping**, or which tool enforces it (slide 29 says only "as many symbols as possible").
