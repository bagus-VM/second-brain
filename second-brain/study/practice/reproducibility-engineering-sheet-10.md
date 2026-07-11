---
title: "Exercise Sheet 10: LLMs and Reproducibility"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-11
---

# Exercise Sheet 10: LLMs and Reproducibility

## 2 Keeping a Secret

### 2.1 Secrets in an Environment Variable

> [!note]- Solution
> **(a)** Build and run with the API key passed as an environment variable:
>
> ```bash
> cd secrets/1-env-var
> export OPENAI_API_KEY=sk-dem...cdef
> docker build -t env-demo-img .
> docker run --name env-demo-1 -e OPENAI_API_KEY env-demo-img
> ```
>
> **(b)** `docker inspect` reveals the API key in plain text inside the container's environment block. Anyone with Docker daemon access can read it.
>
> ```bash
> docker inspect env-demo-1 2>/dev/null | grep -i openai
> ```
>
> **(c)** With Docker Compose:
>
> ```bash
> docker compose up -d
> ```
>
> **(d)** `docker inspect` still reveals the key in the environment block — same problem as the `-e` flag approach. Docker Compose reads the variable from the host environment and injects it into the container, but `docker inspect` exposes it either way.

### 2.2 Secrets in a .env File

> [!note]- Solution
> **(a)** Run with Docker Compose after setting up the `.env` file:
>
> ```bash
> cd secrets/2-dotenv
> cp .env.example .env
> # edit .env to set OPENAI_API_KEY=sk-dem...cdef
> docker compose up -d
> ```
>
> **(b)** `docker inspect` still reveals the key in the environment block:
>
> ```bash
> docker inspect dotenv-demo 2>/dev/null | grep -i openai
> ```
>
> **(c)** Inside the container, the key is stored identically — it's still an environment variable. What the `.env` file improved: the key no longer appears in shell history or in `compose.yaml` (which might be committed). But it's still visible via `docker inspect` at runtime.

### 2.3 Secrets in a Mounted Secret File

> [!note]- Solution
> **(a)** Run with Docker Compose after creating the secret file:
>
> ```bash
> cd secrets/3-mounted-file
> mkdir -p secrets
> echo "sk-mou...cdef" > secrets/openai_api_key
> docker compose up -d
> ```
>
> **(b)** `docker inspect` only shows the mount point (source and destination paths) — it does **not** show the contents of the mounted file:
>
> ```bash
> docker inspect mounted-file-demo-1 2>/dev/null | grep -i openai
> ```
>
> **(c)** Inside the container, the key is read from a file path (e.g., `/run/secrets/openai_api_key`) instead of from `os.environ`. The improvement: the actual secret value is not visible in `docker inspect` output. An attacker with Docker daemon access can see *where* the file is mounted but not *what* it contains.

### 2.4 Preventing Accidents

> [!note]- Solution
> **(a)** Files that must never be committed:
> - `.env` files (contain secrets in plain text)
> - `secrets/` directories (contain API keys)
> - Any file matching `*.key`, `secret-*`, etc.
>
> Enforcement: add these patterns to `.gitignore`:
>
> ```
> .env
> secrets/
> *.key
> secret-*
> ```
>
> **(b)** Keep the same files out of the Docker build context by adding them to `.dockerignore`:
>
> ```
> .env
> secrets/
> *.key
> secret-*
> ```
>
> Without `.dockerignore`, any `COPY . .` in the Dockerfile would embed secret files into the image layer. They persist in the image even if deleted in a later layer. Both `.gitignore` and `.dockerignore` should list the same secret patterns.

## 3 Reproducible LLM Outputs

### 3.2 Temperature and Seed

#### 3.2.1 Experiments

> [!note]- Solution
> **(a) Temperature = 0, varying seed:**
>
> ```bash
> python generate.py -t 0 -i 3
> python generate.py -t 0 -s 1 -i 3
> python generate.py -t 0 -s 999 -i 3
> ```
>
> **Result:** All three produce identical outputs regardless of seed value.
>
> **Why:** `temperature=0` means greedy decoding — the model always selects the token with the highest probability at every step. The seed controls the random number generator used for sampling, but when temperature is 0, no sampling occurs. The seed is irrelevant.
>
> ---
>
> **(b) No temperature set, fixed seed:**
>
> ```bash
> python generate.py -s 42 -i 3
> ```
>
> **Result:** Outputs vary across runs, even with the same seed.
>
> **Why:** The default temperature in most LLM servers is not 0 (typically 0.7–1.0). At any temperature > 0, the model samples from the probability distribution. A fixed seed makes the sampling reproducible *given the same RNG state*, but the default temperature introduces randomness. The seed alone cannot guarantee reproducibility when temperature > 0 is the default.
>
> ---
>
> **(c) Fixed seed, varying temperature:**
>
> ```bash
> python generate.py -s 42 -t 0.7 -i 3
> python generate.py -s 42 -t 1.5 -i 3
> ```
>
> **Result:** Higher temperature produces more variation in outputs.
>
> - At moderate temperature (0.7), there's noticeable variation.
> - At high temperature (1.5), outputs are highly random and may be incoherent.
>
> **Key insight:** Temperature controls the "creativity" or randomness of generation. Even with a fixed seed, increasing temperature widens the sampling distribution, producing more diverse (and less reproducible) outputs.
>
> ---
>
> **Summary:** `temperature=0` makes output deterministic on the same hardware (CPU). Seed is irrelevant when temperature is 0. For reproducibility, always set `temperature=0`.

## 4 Structured Outputs from LLMs

The model must return a JSON instance matching this schema:
```json
{
  "type": "integer",
  "anyOf": [
    { "type": "integer", "minimum": 3, "maximum": 1 },
    { "type": "integer", "minimum": 12000, "maximum": 12002 }
  ]
}
```

The first branch (`minimum: 3, maximum: 1`) can never be satisfied, so the only valid instances are 12000, 12001, and 12002; the smallest valid answer is 12000.

### 4.1 Schema in the Prompt

> [!note]- Solution
> Running the prompt-only variant:
>
> ```bash
> python schema_in_prompt.py -i 5
> ```
>
> **Result:** The model does **not** always return a valid instance. It may return malformed JSON, wrong types, extra text, or values outside the allowed range.
>
> **Why:** Putting the schema in the prompt is a *hint*, not a constraint. The model generates tokens freely — it may ignore the schema, misinterpret it, or produce invalid JSON. There is no enforcement mechanism; the model *may* comply, but it's not guaranteed.

### 4.2 Constrained Decoding

> [!note]- Solution
> Running the structured-outputs variant:
>
> ```bash
> python structured_output.py -i 5
> ```
>
> **Result:** Every output is valid JSON matching the schema. The server enforces the schema during token generation using GBNF grammars — the model physically cannot produce tokens that violate the schema.
>
> **Difference:** With constrained decoding, output is **valid by construction**. No retry logic needed. The guarantee is syntactic (the JSON structure matches), not semantic (the value is "meaningful").
>
> **However:** The tool's grammar conversion determines which schema features are actually enforced. If the tool doesn't support a feature (e.g., certain `anyOf` patterns), it may silently skip it.

### 4.3 oneOf vs. anyOf

> [!note]- Solution
> Converting both schemas to GBNF grammars:
>
> ```bash
> python json_schema_to_grammar.py schemas/number_oneof.json oneof.gbnf
> python json_schema_to_grammar.py schemas/number_anyof.json anyof.gbnf
> diff oneof.gbnf anyof.gbnf
> ```
>
> **Result:** The `diff` shows that the two grammars are **identical** (or functionally equivalent). The converter does not enforce the mutual exclusivity constraint of `oneOf` at the grammar level.
>
> **Implication for reproducibility:** If the tool treats `oneOf` and `anyOf` identically in its grammar conversion, the reproducibility guarantee is the same for both — the output will match at least one sub-schema, but the tool won't verify that *exactly* one matches. You should check your specific tool's behavior rather than assuming JSON Schema semantics are fully enforced.

## 5 Reproducibility and LLMs (Multiple Choice)

> [!note]- Solution
> **(a)** You send the following request to the local llama.cpp server (CPU) several times:
>
> ```python
> client.chat.completions.create(
>     model="gemma3:1b",
>     messages=[{"role": "user", "content": "Name a colour."}],
>     temperature=0.0,
> )
> ```
>
> Are the responses reproducible?
>
> - No – an LLM's output is always random.
> - **Yes – at temperature=0 the result is deterministic on a local system if the model runs on a CPU.** ✓
> - Only if a seed is also set.
> - Only on a GPU.
> - None of these options
>
> **Explanation:** On CPU, floating-point operations are deterministic — the same computation on the same hardware produces the same bits. With `temperature=0` (greedy decoding), the model always picks the highest-probability token. No randomness enters the process, so the same input always produces the same output. On GPU, minor non-determinism from parallel floating-point ordering can cause slight differences even at temperature=0.
>
> ---
>
> **(b)** A model call uses constrained decoding with a JSON Schema that includes numeric minimum/maximum bounds and a `oneOf`, and it returns successfully. Which statement is correct?
>
> - The instance is guaranteed to satisfy the full schema, regardless of the tool used.
> - **The instance is only guaranteed to match the schema features the tool actually supports.** ✓
> - The call cannot succeed, because minimum is never supported.
> - Structured outputs guarantee that the value is semantically correct.
> - None of these options
>
> **Explanation:** Constrained decoding is only as reliable as the tool's grammar conversion. If the tool doesn't enforce `oneOf` mutual exclusivity (as shown in 4.3) or silently skips `minimum`/`maximum` constraints, the output may violate those schema features. The guarantee is limited to what the tool actually translates into its grammar.

## Related Lectures
- [[reproducibility-engineering-lecture-9]]
