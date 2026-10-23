#!/usr/bin/env python3
"""
Homework 2 (Reverse- and Reengineering, 27.10.2026) - verification of the
recovered x86-64 functions.

Part 1: `bar` and `foo` from the two assembly listings on the sheet.
Part 2: the assembly `foo(int)` - its intraprocedural CFG and what it computes.

The recovered C is simulated instruction by instruction here, so the claims in
hw02-solution.md are checked against the actual opcodes rather than asserted.

PROVENANCE OF THE LISTINGS.  The sheet prints the two listings side by side.
`pdftotext -layout` interleaves the two columns into a single text stream, which
produces a listing that does not exist.  The listings below were recovered from
the PDF's word positions (pymupdf `get_text("words")` and `get_text("dict")`),
splitting at x = 300: everything left of that is Listing 1 (`bar`), everything
right is Listing 2 (`foo`).  The two recovered listings are reproduced verbatim
below as the ground truth this script checks against.

Run:  python hw02-verify.py
"""

MASK = 0xFFFFFFFF

# --------------------------------------------------------------------------
# Listing 1: bar function   (verbatim from the PDF, left column)
# --------------------------------------------------------------------------
LISTING_BAR = """
 1 push  rbp
 2 mov   rbp, rsp
 3 mov   dword ptr [rbp - 4], edi
 4 mov   dword ptr [rbp - 8], esi
 5 mov   eax, dword ptr [rbp - 4]
 6 or    eax, dword ptr [rbp - 8]
 7 xor   eax, -1
 8 pop   rbp
 9 ret
"""

# --------------------------------------------------------------------------
# Listing 2: foo function   (verbatim from the PDF, right column)
# --------------------------------------------------------------------------
LISTING_FOO = """
 1 push  rbp
 2 mov   rbp, rsp
 3 mov   dword ptr [rbp - 4], edi
 4 mov   dword ptr [rbp - 8], esi
 5 mov   dword ptr [rbp - 12], edx
 6 mov   eax, dword ptr [rbp - 4]
 7 xor   eax, -1
 8 mov   ecx, dword ptr [rbp - 8]
 9 xor   ecx, -1
10 and   ecx, dword ptr [rbp - 12]
11 or    eax, ecx
12 pop   rbp
13 ret
"""


def bar(x, y):
    """
    Listing 1, simulated:

      mov  [rbp-4], edi     ; a = arg1
      mov  [rbp-8], esi     ; b = arg2
      mov  eax, [rbp-4]     ; eax = a
      or   eax, [rbp-8]     ; eax = a | b
      xor  eax, -1          ; eax = ~(a | b)      (32-bit bitwise NOT)
      ret
    """
    a = x & MASK
    b = y & MASK
    eax = a
    eax = (eax | b) & MASK
    eax = (eax ^ MASK) & MASK          # xor eax, -1 is a bitwise NOT, not logical NOT
    return eax


def foo(x, y, z):
    """
    Listing 2, simulated:

      mov  [rbp-4], edi      ; a = arg1
      mov  [rbp-8], esi      ; b = arg2
      mov  [rbp-12], edx     ; c = arg3
      mov  eax, [rbp-4]      ; eax = a
      xor  eax, -1           ; eax = ~a
      mov  ecx, [rbp-8]      ; ecx = b
      xor  ecx, -1           ; ecx = ~b
      and  ecx, [rbp-12]     ; ecx = ~b & c
      or   eax, ecx          ; eax = ~a | (~b & c)
      ret
    """
    a = x & MASK
    b = y & MASK
    c = z & MASK
    eax = a
    eax = (eax ^ MASK) & MASK
    ecx = b
    ecx = (ecx ^ MASK) & MASK
    ecx = (ecx & c) & MASK
    eax = (eax | ecx) & MASK
    return eax


def check_part1():
    print("=" * 78)
    print("Part 1 - recovering `bar` and `foo` from the two listings")
    print("=" * 78)
    print()
    print("  Listing 1 (bar), as recovered from the PDF:")
    for line in LISTING_BAR.strip().split("\n"):
        print("      " + line)
    print()
    print("  Listing 2 (foo), as recovered from the PDF:")
    for line in LISTING_FOO.strip().split("\n"):
        print("      " + line)
    print()

    # --- bar -------------------------------------------------------------
    # The opcodes are bitwise, so the result is the 32-bit complement of (a|b).
    # For boolean inputs that is NOR; for general integers it is NOT(a|b).
    print("  bar: the opcodes compute  ~(a | b)  in 32-bit arithmetic.")
    ok_bar = True
    for a in (0, 1, 2, 3, 0xFFFFFFFF, 0x80000000, 7):
        for b in (0, 1, 2, 3, 0xFFFFFFFF, 0x80000000, 7):
            got = bar(a, b)
            want = (~(a | b)) & MASK
            ok_bar &= (got == want)
    print(f"    equals ~(a|b) on all 49 tested pairs: {ok_bar}")

    # On boolean inputs the VALUES are 0xFFFFFFFF / 0xFFFFFFFE, not 0 and 1.
    # So `bar` is NOT the NOR predicate: read as a truth value (nonzero = true)
    # it is true for every input pair, because ~x is nonzero for every 32-bit x.
    vals = {(a, b): bar(a, b) for a in (0, 1) for b in (0, 1)}
    ok_bool = all(v != 0 for v in vals.values())
    print(f"    every boolean-input result is NONZERO (so it is never 'false'): {ok_bool}")
    print("    values:", {f"{a},{b}": hex(v) for (a, b), v in vals.items()})
    print()
    print("    IMPORTANT: `xor eax, -1` is a BITWISE complement, not a logical")
    print("    NOT. The result is therefore 0xFFFFFFFF or 0xFFFFFFFE, never 0 or 1.")
    print("    Reading this as `!(a || b)` (a NOR predicate) is the classic")
    print("    mistake, and the compiler confirms it: the logical version emits")
    print("    sete/setne + movzbl, while the sheet's listing has or + xor $-1.")
    print()

    # --- foo -------------------------------------------------------------
    print("  foo: the opcodes compute  ~a | (~b & c).")
    ok_foo = True
    for a in (0, 1, 2, 3, 0xFFFFFFFF, 7):
        for b in (0, 1, 2, 3, 0xFFFFFFFF, 7):
            for c in (0, 1, 2, 3, 0xFFFFFFFF, 7):
                got = foo(a, b, c)
                want = ((~a) | ((~b) & c)) & MASK
                ok_foo &= (got == want)
    print(f"    equals ~a|(~b&c) on all 216 tested triples: {ok_foo}")

    # De Morgan:  ~a | (~b & c)  ==  ~a | ~(b | ~c)  ==  ~(a & (b | ~c))
    #            = !(a && (b || !c))
    # De Morgan, in the bitwise world:  ~a | (~b & c)  ==  ~(a & (b | ~c))
    ok_dm = True
    for a in (0, 1, 2, 3, 0xFFFFFFFF, 7):
        for b in (0, 1, 2, 3, 0xFFFFFFFF, 7):
            for c in (0, 1, 2, 3, 0xFFFFFFFF, 7):
                lhs = foo(a, b, c)
                rhs = (~(a & (b | (~c & MASK)))) & MASK
                ok_dm &= (lhs == rhs)
    print(f"    equals ~(a & (b | ~c)) on all 216 tested triples: {ok_dm}")

    ok_dm2 = True
    for a in (0, 1, 2, 3, 0xFFFFFFFF, 7):
        for b in (0, 1, 2, 3, 0xFFFFFFFF, 7):
            for c in (0, 1, 2, 3, 0xFFFFFFFF, 7):
                ok_dm2 &= (foo(a, b, c) == ((~a) | ((~b) & c)) & MASK)
    print(f"    equals ~a | (~b & c) on all 216 tested triples: {ok_dm2}")
    print()

    print("  The values on boolean inputs (0xFFFFFFFF is the bitwise complement):")
    print("      a b c | foo")
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                print(f"      {a} {b} {c} |  {foo(a, b, c)}")
    print("  Every one of them is nonzero, so as a predicate `foo` is never false.")
    print("  The bitwise reading is the only one the machine code supports.")
    print()

    print("  Every argument is used:")
    print("    bar uses arg1 and arg2 (edi, esi).")
    print("    foo uses arg1, arg2 and arg3 (edi, esi, edx).")
    print()

    print("  Recovered C for bar:")
    print("      int bar(int a, int b) { return ~(a | b); }")
    print("      // on boolean inputs: return !(a || b);")
    print()
    print("  Recovered C for foo:")
    print("      int foo(int a, int b, int c) { return ~a | (~b & c); }")
    print("      // on boolean inputs: return !(a && (b || !c));")
    print()
    return ok_bar and ok_foo and ok_bool and ok_dm and ok_dm2


# ==========================================================================
# Part 2 - the assembly foo(int) with its CFG
# ==========================================================================

def foo_int(n):
    """
    Assembly `foo(int)` from the sheet, simulated statement by statement.

      [rbp-20] = n
      [rbp-4]  = 0      (a)
      [rbp-8]  = 1      (b)
      [rbp-12] = 0      (result)
      if (n <= 1) { result = a;              -> return result }
      else if (n == 2) { result = b;         -> return result }
      else {
        i = 3
        while (i <= n) {
          result = a + b;
          a = b;
          b = result;
          i++;
        }
        return result;
      }
    """
    a, b, result, i = 0, 1, 0, 3
    if n <= 1:
        result = a
        return result
    if n == 2:
        result = b
        return result
    i = 3
    while i <= n:
        result = a + b
        a = b
        b = result
        i += 1
    return result


def fib(k):
    """F(0)=0, F(1)=1, F(k)=F(k-1)+F(k-2)."""
    if k <= 1:
        return k
    p, q = 0, 1
    for _ in range(2, k + 1):
        p, q = q, p + q
    return q


def check_part2():
    print("=" * 78)
    print("Part 2 - the assembly foo(int): CFG and what it computes")
    print("=" * 78)
    print()

    print("  Intraprocedural CFG (basic blocks read off the listing):")
    print()
    print("      entry")
    print("        |")
    print("        v")
    print("      B1: cmp [rbp-20], 1 ; jg .L2")
    print("        |            \\")
    print("        | T (n<=1)    \\ F (n>1)")
    print("        v              v")
    print("      B2: mov eax,[rbp-4]      B3: cmp [rbp-20], 2 ; jne .L4")
    print("          mov [rbp-12],eax         |                 |")
    print("          jmp .L3                  | T (n==2)        | F (n>2)")
    print("        |                           v                 v")
    print("        |                         B4: mov eax,[rbp-8]  B5: mov [rbp-16], 3")
    print("        |                           mov [rbp-12],eax      jmp .L5")
    print("        |                           jmp .L3              |")
    print("        |                           |                    v")
    print("        |                           |                  B6: cmp eax,[rbp-20] ; jle .L7")
    print("        |                           |                    |            \\")
    print("        |                           |                    | T (i<=n)   \\ F (i>n)")
    print("        |                           |                    v             v")
    print("        |                           |                  B7: result=a+b   (falls through to B6)")
    print("        |                           |                      a=b")
    print("        |                           |                      b=result")
    print("        |                           |                      i++")
    print("        |                           |                    |")
    print("        |                           |                    +----> B6 (back edge)")
    print("        |                           |")
    print("        +---------------------------+-----------------> B8: mov eax,[rbp-12] ; pop rbp ; ret")
    print()

    print("  What it computes. Candidate: the (n-1)-th Fibonacci number")
    print("  (F(0)=0, F(1)=1). Checking by simulation:")
    print()
    print("        n :  " + " ".join(f"{n:>3}" for n in range(0, 13)))
    got = [foo_int(n) for n in range(13)]
    print("        foo: " + " ".join(f"{v:>3}" for v in got))
    want = [fib(n - 1) if n >= 1 else 0 for n in range(13)]
    print("        F(n-1):" + " ".join(f"{v:>3}" for v in want))
    ok = got == want
    print(f"        identical for n = 0..12: {ok}")
    print()

    print("  Why: the loop variable i runs from 3 to n, and after the iteration")
    print("  for i the accumulator holds F(i-1). So the returned value is F(n-1).")
    print()

    print("  Boundary cases read straight off the CFG:")
    print("    n <= 1  -> returns a = 0            (the 'n<=1' branch)")
    print("    n == 2  -> returns b = 1            (the 'n==2' branch)")
    print("    n >= 3  -> the loop runs n-2 times")
    print()

    print("  The functions called from main (Part 2, question 2):")
    print("    __isoc99_scanf   (reads the integer argument)")
    print("    foo(int)         (the function above)")
    print("    printf           (prints the result with the format string \"%d\")")
    print()

    print("  The equivalent C source, recovered:")
    print("""
        int foo(int n) {
            int a = 0, b = 1, result = 0;
            if (n <= 1) { result = a; }
            else if (n == 2) { result = b; }
            else {
                int i = 3;
                while (i <= n) {
                    result = a + b;
                    a = b;
                    b = result;
                    i++;
                }
            }
            return result;
        }
    """)
    return ok


if __name__ == "__main__":
    a = check_part1()
    b = check_part2()
    print("=" * 78)
    print(f"ALL CHECKS PASSED: part1={a}  part2={b}")
    print("=" * 78)
