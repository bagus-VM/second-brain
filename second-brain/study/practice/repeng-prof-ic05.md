---
title: "RepEng In-Class Exercise 5 — Reproducible Builds"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| Exercises 1–2 — Compilation Basics | [[c-preprocessor]] · [[make-and-build-systems]] |
| Exercise 3 — File Update Timestamps | [[deterministic-builds]] · [[source-date-epoch]] |
| Exercises 4–5 — Makefiles | [[make-and-build-systems]] · [[deterministic-builds]] |
| Exercise 6 — C Preprocessor Macros | [[c-preprocessor]] |
| Exercise 7 — Heisenbug | [[build-environment-isolation]] |

# In-Class Exercise Sheet 5 — C Programming, Makefiles & Reproducible Builds

---

## Exercise 1 — Code Magnets (Card Value Program)

Reassembled code:

```c
#include <stdio.h>
#include <stdlib.h>

/*
 * Program to evaluate face values.
 * Released under the Vegas Public License.
 * (c)2014 The College Blackjack Team.
 */

int main()
{
    char card_name[3];
    puts("Enter the card_name: ");
    scanf("%2s", card_name);
    int val = 0;
    if (card_name[0] == 'K') {
        val = 10;
    } else if (card_name[0] == 'Q') {
        val = 10;
    } else if (card_name[0] == 'J') {
        val = 10;
    } else if (card_name[0] == 'A') {
        val = 11;
    } else {
        val = atoi(card_name);
    }
    printf("The card value is: %i\n", val);
    return 0;
}
```

**Key decisions:**
- `#include <stdlib.h>` for `atoi()`
- `#include <stdio.h>` for `printf()` and `scanf()`
- Face cards (K, Q, J) = 10, Ace = 11
- `int main()` with `return 0;`

---

## Exercise 2 — Be the Compiler

The code calculates: Mercury day in hours = 58.65 × 24 = 1407.6

### Fragment 1 (with forward declarations):
```c
float mercury_day_in_earth_days();
int hours_in_an_earth_day();

int main() {
    float length_of_day = mercury_day_in_earth_days();
    int hours = hours_in_an_earth_day();
    float day = length_of_day * hours;
    printf("A day on Mercury is %f hours\n", day);
    return 0;
}
```
→ ✓ You can compile the code (forward declarations present)
→ ⚠ You should display a warning (none, this is correct)
→ ✓ The program will work

### Fragment 2 (declarations after main):
```c
float mercury_day_in_earth_days();

int main() {
    float length_of_day = mercury_day_in_earth_days();
    int hours = hours_in_an_earth_day();  // no declaration!
    float day = length_of_day * hours;
    printf("A day on Mercury is %f hours\n", day);
    return 0;
}
```
→ ✓ You can compile (with implicit declaration warning)
→ ✓ You should display a warning (`hours_in_an_earth_day` implicitly declared)
→ ✓ The program will work (but is technically incorrect C99+)

### Fragment 3 (declarations inside main):
```c
int main() {
    float mercury_day_in_earth_days();  // valid but unusual
    float length_of_day = mercury_day_in_earth_days();
    int hours = hours_in_an_earth_day();  // implicit declaration
    float day = length_of_day * hours;
    printf("A day on Mercury is %f hours\n", day);
    return 0;
}
```
→ ✓ You can compile (with warning)
→ ✓ You should display a warning
→ ✓ The program will work

### Fragment 4 (int instead of float):
```c
float mercury_day_in_earth_days();
int hours_in_an_earth_day();

int main() {
    int length_of_day = mercury_day_in_earth_days();  // truncation!
    int hours = hours_in_an_earth_day();
    float day = length_of_day * hours;
    printf("A day on Mercury is %f hours\n", day);
    return 0;
}
```
→ ✓ You can compile
→ ⚠ You should display a warning (implicit conversion from float to int)
→ ✗ The program will NOT work correctly — `length_of_day` will be truncated to 58 (not 58.65), giving 1392.0 instead of 1407.6

---

## Exercise 3 — File Update Timestamps

### Engine Management System (ems):
Files that need updating (source newer than object):

- `turbo.c` (12:15) is newer than `turbo.o` (12:22)? **No** — turbo.o is newer. But wait: turbo.c (12:15) vs turbo.o (12:22). The .o is newer, so turbo.o is up to date.
- `graticule.c` (14:52) is newer than `graticule.o` (14:25)? **Yes** — needs rebuild.
- `ems` (14:26) depends on all .o files. Since graticule.o is outdated, **ems needs relinking**.
- `thruster.c` (11:43), `thruster.o` (11:48) — .o is newer, OK.
- `servo.c` (13:47), `servo.o` (13:46) — .c is newer! **servo.o needs rebuild**, and therefore **ems needs relinking**.

**Files to update:** graticule.o, servo.o, ems

### Galley:
- `microwave.c` (15:42), `microwave.o` (18:02) — .o is newer, OK.
- `popcorn.c` (17:05), `popcorn.o` (17:07) — .o is newer, OK.
- `juicer.c` (16:41), `juicer.o` (16:43) — .o is newer, OK.
- `galley` (17:09) — all .o files are older than galley? popcorn.o (17:07) < galley (17:09), OK. **Galley is up to date.**

**Files to update:** None.

---

## Exercise 4 — Make Magnets

```makefile
oggswing: oggswing.c oggswing.h
	[TAB]gcc oggswing.c -o oggswing

swing.ogg: whitennerdy.ogg oggswing
	[TAB]./oggswing whitennerdy.ogg swing.ogg
```

**Key points:**
- `oggswing` depends on `oggswing.c` and `oggswing.h`
- `swing.ogg` depends on `whitennerdy.ogg` (input) and `oggswing` (the tool)
- Recipe lines must use TABs, not spaces

---

## Exercise 5 — Unreproducible Makefile

```makefile
SRCS = $(wildcard *.c)
tool: $(SRCS:.c=.o)
	$(CC) -o $@ $^
```

**Problem:** `$(wildcard *.c)` depends on the filesystem state at build time. If you add or remove `.c` files, the build changes. The wildcard expansion is non-deterministic — it depends on which files happen to exist when `make` runs.

Additionally, `$(SRCS:.c=.o)` creates object file targets from source files, but there's no pattern rule for compiling `.c` → `.o`, so make will try implicit rules which may vary across systems.

**Fix:**
```makefile
SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)

tool: $(OBJS)
	$(CC) -o $@ $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
```

Better fix: Explicitly list source files instead of using wildcard:
```makefile
SRCS = main.c utils.c parser.c  # explicit list
```

---

## Exercise 6 — C Preprocessor Macros

**(a)** `#define BUFFSIZE 1024` → `int buf[BUFFSIZE + 1];`
After preprocessing: `int buf[1024 + 1];`
(Evaluation happens at compile time: `int buf[1025];`)

**(b)** `#define a(b) b + 1` → `int x = a(1) + 1;`
After macro expansion: `int x = 1 + 1 + 1;` → `int x = 3;`

**⚠ Pitfall:** This macro is unsafe! `a(2) * 3` would expand to `2 + 1 * 3 = 5` (not 9). Fix: `#define a(b) ((b) + 1)`

**(c)** The `__LINE__`, `__FILE__`, `__TIME__`, `__DATE__` macros:
```
__LINE__ = 3  (the line number of the printf statement)
__FILE__ = testCPP.c
__TIME__ = "hh:mm:ss"  (time of compilation)
__DATE__ = "Mmm dd yyyy"  (date of compilation)
```

**⚠ Reproducibility concern:** `__TIME__` and `__DATE__` change with every compilation, breaking bitwise reproducibility.

---

## Exercise 7 — Heisenbug

```c
#include <assert.h>
#include <stdio.h>

#define FALSE 0

char *p = (char *)5;

int someinitialization(void) {
    p = "abc";
    return FALSE;
}

int main(int argc, char **argv) {
    assert(someinitialization() == FALSE);
    printf("%s\n", p);
    return 0;
}
```

**With assertions enabled** (`gcc heisenbug.c -o heisenbug; ./heisenbug`):
→ Output: `abc`
(assert calls `someinitialization()`, which sets `p = "abc"`)

**With assertions disabled** (`gcc -DNDEBUG heisenbug.c -o heisenbug; ./heisenbug`):
→ **Crash / undefined behavior** — `p` is still `(char *)5` (a garbage pointer), and `printf` tries to dereference it.

**What causes the heisenbug:**
The `assert()` macro has a **side effect** — it calls `someinitialization()`. When `NDEBUG` is defined, `assert()` expands to nothing, so `someinitialization()` is never called, and `p` is never initialized to `"abc"`. The program's behavior changes depending on whether debugging is enabled.

**Fix:** Never put side effects inside `assert()`. Call `someinitialization()` separately:
```c
int init_result = someinitialization();
assert(init_result == FALSE);
```


---

## Related Resources

### 📖 Reproducibility Engineering - Lecture 5: Reproducible Builds
- Lecture topic: [[reproducibility-engineering-lecture-5]]

**Key concepts covered:**
- [[diffoscope]]
- [[deterministic-builds]]
- [[build-environment-isolation]]
- [[source-date-epoch]]
- [[ci-cd-for-reproducibility]]
- [[containerization-for-builds]]
- [[package-manager-reproducibility]]
- [[make-and-build-systems]]
- [[c-preprocessor]]
