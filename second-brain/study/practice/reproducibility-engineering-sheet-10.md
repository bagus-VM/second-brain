---
title: "Exercise Sheet 10: LLMs and Reproducibility"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# Exercise Sheet 10: LLMs and Reproducibility

## Exercises

### Q1: Passing API Keys via Environment Variable
Set the OpenAI API key as an environment variable and pass it to a Docker container. What is the security problem with this approach?

<details>
<summary>Solution</summary>

Export the key and pass it with `-e`:

```bash
export OPENAI_API_KEY=sk-...
docker run -e OPENAI_API_KEY my-image
```

**Problem:** Anyone with access to the Docker daemon can run `docker inspect` on the container and read the API key in plain text from the container's environment variables. This is a significant security risk on shared machines or CI runners.

</details>

---

### Q2: Using an .env File for Secrets
How do you use a `.env` file to pass secrets to Docker Compose, and what limitation does it share with the environment variable approach?

<details>
<summary>Solution</summary>

1. Copy the example file and fill in your key:
   ```bash
   cp .env.example .env
   # edit .env to set OPENAI_API_KEY=sk-...
   ```

2. In `docker-compose.yml`, reference the variable normally — Docker Compose reads `.env` automatically.

**Limitation:** The secret is still injected into the container's environment. `docker inspect` still reveals it in the environment block, just like the `-e` flag approach. The `.env` file prevents the secret from leaking into shell history or logs, but not from the container's runtime state.

</details>

---

### Q3: Mounted Secret File
Explain how mounting a secret as a read-only file improves security over environment variables. What does `docker inspect` reveal?

<details>
<summary>Solution</summary>

Mount the API key as a file inside the container:

```bash
docker run -v ./secret-key.txt:/run/secrets/api-key:ro my-image
```

Inside the container, read the key from the file path instead of `os.environ`.

**Improvement:** `docker inspect` only shows the mount point (source path and destination path) — it does **not** show the contents of the mounted file. This is better than environment variables, where the actual secret value is visible in the inspect output.

</details>

---

### Q4: Preventing Accidental Secret Exposure
What two files help prevent API keys from leaking, and what does each protect against?

<details>
<summary>Solution</summary>

- **`.dockerignore`** — prevents secret files (e.g., `.env`, `secret-key.txt`) from being copied into the Docker build context. Without this, any `COPY . .` in the Dockerfile would embed secrets into the image layer, where they persist even if later deleted.

- **`.gitignore`** — prevents secret files from being committed to version control. Once a secret is in a Git history, removing it requires rewriting history (e.g., `git filter-branch` or BFG Repo Cleaner), and anyone who cloned before the fix still has it.

Both files should list patterns like `.env`, `*.key`, `secret-*`, etc.

</details>

---

### Q5: Temperature and Seed — Identical Outputs
With `temperature=0` and varying seeds, what happens to the LLM outputs? Why?

<details>
<summary>Solution</summary>

**Result:** Outputs are identical regardless of seed value.

**Why:** `temperature=0` means greedy decoding — the model always selects the token with the highest probability at every step. The seed controls the random number generator used for sampling, but when temperature is 0, no sampling occurs. The seed is irrelevant.

```bash
# All three produce identical output:
curl http://localhost:8080/v1/chat/completions -d '{"messages":[{"role":"user","content":"Hello"}],"temperature":0,"seed":42}'
curl http://localhost:8080/v1/chat/completions -d '{"messages":[{"role":"user","content":"Hello"}],"temperature":0,"seed":123}'
curl http://localhost:8080/v1/chat/completions -d '{"messages":[{"role":"user","content":"Hello"}],"temperature":0,"seed":999}'
```

**Key insight:** `temperature=0` makes output deterministic on the same hardware (CPU). Seed is irrelevant when temperature is 0.

</details>

---

### Q6: Temperature and Seed — Default Temperature
With no temperature specified and a fixed seed, do outputs stay the same across runs?

<details>
<summary>Solution</summary>

**Result:** Outputs vary across runs, even with the same seed.

**Why:** The default temperature in most LLM servers is not 0 (typically 0.7–1.0). At any temperature > 0, the model samples from the probability distribution. A fixed seed makes the sampling reproducible *given the same RNG state*, but the default temperature introduces randomness. The seed alone cannot guarantee reproducibility when temperature > 0 is the default.

</details>

---

### Q7: Temperature and Seed — Fixed Seed, Varying Temperature
What happens when you fix the seed and vary the temperature?

<details>
<summary>Solution</summary>

**Result:** Higher temperature produces more variation in outputs.

- At very low temperature (e.g., 0.01), outputs are nearly deterministic — the distribution is sharply peaked around the most likely token.
- At moderate temperature (e.g., 0.7), there's noticeable variation.
- At high temperature (e.g., 1.5), outputs are highly random and may be incoherent.

**Key insight:** Temperature controls the "creativity" or randomness of generation. Even with a fixed seed, increasing temperature widens the sampling distribution, producing more diverse (and less reproducible) outputs.

</details>

---

### Q8: Schema in Prompt vs Constrained Decoding
Compare putting a JSON schema in the prompt versus using constrained decoding for structured outputs.

<details>
<summary>Solution</summary>

**Schema in prompt:**
```json
{
  "messages": [
    {"role": "system", "content": "Return valid JSON matching this schema: {\"name\": \"string\", \"age\": \"integer\"}"},
    {"role": "user", "content": "My name is Alice and I am 30."}
  ]
}
```
- The model *may* return valid JSON, but there's no guarantee.
- It might add extra text, use wrong types, or produce malformed JSON.
- Parsing requires error handling and retry logic.

**Constrained decoding:**
```json
{
  "messages": [...],
  "response_format": {
    "type": "json_schema",
    "json_schema": {"name": "person", "schema": {"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "integer"}}, "required": ["name", "age"]}}
  }
}
```
- The server enforces the schema during token generation using GBNF grammars or similar.
- Output is **valid by construction** — the model physically cannot produce tokens that violate the schema.
- No retry logic needed.

**For reproducibility:** Constrained decoding is strictly better — it eliminates an entire class of non-determinism (malformed output).

</details>

---

### Q9: oneOf vs anyOf in Constrained Decoding
What is the practical difference between `oneOf` and `anyOf` in JSON Schema when using constrained decoding?

<details>
<summary>Solution</summary>

In JSON Schema semantics:
- `oneOf` — exactly one sub-schema must match
- `anyOf` — one or more sub-schemas may match

**In constrained decoding (GBNF grammar conversion):**
The tool converts the schema to a grammar that the LLM must follow during generation. Depending on the tool:
- Some tools produce **identical grammars** for `oneOf` and `anyOf` (they don't enforce the mutual exclusivity constraint of `oneOf` at the grammar level).
- Other tools produce **different grammars** that correctly enforce the distinction.

**Implication for reproducibility:** If the tool treats `oneOf` and `anyOf` identically in its grammar conversion, the reproducibility guarantee is the same for both — the output will match at least one sub-schema, but the tool won't verify that *exactly* one matches. You should check your specific tool's behavior rather than assuming the JSON Schema semantics are fully enforced.

</details>

---

### Q10: Multiple Choice — Reproducibility Scenarios

**(a)** Is the output reproducible if you send the same request to the same machine running on CPU with `temperature=0`?

**(b)** What does constrained decoding with `oneOf` and `min`/`max` constraints guarantee?

<details>
<summary>Solution</summary>

**(a) Yes, the output is reproducible.**

On CPU (no GPU), floating-point operations are deterministic — the same computation on the same hardware produces the same bits. With `temperature=0` (greedy decoding), the model always picks the highest-probability token. No randomness enters the process, so the same input always produces the same output.

> Note: On GPU, minor non-determinism from floating-point ordering in parallel operations can cause slight differences even at temperature=0, unless deterministic mode is explicitly enabled.

**(b) The output is only guaranteed to match the schema features the tool actually supports.**

If the constrained decoding tool converts `oneOf` to the same grammar as `anyOf`, the mutual exclusivity of `oneOf` is not enforced. Similarly, `min`/`max` constraints on strings or arrays may or may not be enforced depending on the tool's GBNF grammar generator. You should verify which constraints your specific tool enforces rather than assuming full JSON Schema compliance.

</details>

## Related Lectures
- [[reproducibility-engineering-lecture-9]]
