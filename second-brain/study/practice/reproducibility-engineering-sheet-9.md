---
title: "Exercise Sheet 9: JSON and JSON Schema"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-08
---

# Exercise Sheet 9: JSON and JSON Schema

## Exercises

### Q1 Docker Environment for JSON Tools

Set up a Docker container with `jq` and `check-jsonschema` available.

<details>
<summary>Solution</summary>

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y jq && rm -rf /var/lib/apt/lists/*
RUN pip install check-jsonschema

WORKDIR /data
```

Build and run:

```bash
docker build -t json-tools .
docker run --rm -it -v $(pwd):/data json-tools
```

The container has `jq` for querying and pretty-printing JSON, `check-jsonschema` for schema validation, and Python for any scripting. Mounting the working directory at `/data` makes files available inside the container.

</details>

### Q2 Pretty-Printing JSON with jq

Given a minified JSON file `data.json`, pretty-print it. Then produce a compact version.

<details>
<summary>Solution</summary>

Pretty-print (indented, one key per line):

```bash
jq . data.json
```

The `.` filter is the identity filter. It passes the input through unchanged, but `jq` formats the output with indentation by default.

Compact (no whitespace, single line):

```bash
jq -c . data.json
```

The `-c` flag produces compact output. This is useful for piping JSON through shell commands or storing it efficiently.

</details>

### Q3 Querying JSON with jq

Given a JSON array of objects with `month`, `year`, and `temperature` fields, write `jq` filters to:
(a) Extract all `month` values.
(b) Count the number of objects.
(c) Filter for objects where `year` is 2019.

<details>
<summary>Solution</summary>

(a) Extract all `month` values:

```bash
jq '.[].month' data.json
```

The `[]` iterates over the array, and `.month` extracts the `month` field from each element.

(b) Count the number of objects:

```bash
jq 'length' data.json
```

`length` on an array returns the number of elements.

(c) Filter for objects where `year` is 2019:

```bash
jq '[.[] | select(.year == 2019)]' data.json
```

`select(.year == 2019)` keeps only objects where `year` equals 2019. The outer `[...]` collects the results back into an array.

</details>

### Q4 Comparing JSON Documents

Two JSON files `a.json` and `b.json` contain the same logical data but differ in formatting and key order. Why does `diff a.json b.json` report differences, and how do you compare them properly?

<details>
<summary>Solution</summary>

`diff` compares files line by line as text. JSON formatting differences (indentation, line breaks, whitespace) and key ordering both cause `diff` to report changes even when the documents are structurally identical.

Fix: sort keys with `jq -S` before comparing:

```bash
diff <(jq -S . a.json) <(jq -S . b.json)
```

`jq -S` sorts object keys alphabetically. Both files are normalized to the same key order and formatting, so `diff` only reports genuine structural differences.

</details>

### Q5 Writing a JSON Schema

Write a JSON Schema for a weather observation object with required fields `station` (string), `temperature` (number), and `timestamp` (string), plus an optional `humidity` (number).

<details>
<summary>Solution</summary>

```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Weather Observation",
    "type": "object",
    "properties": {
        "station": { "type": "string" },
        "temperature": { "type": "number" },
        "timestamp": { "type": "string" },
        "humidity": { "type": "number" }
    },
    "required": ["station", "temperature", "timestamp"],
    "additionalProperties": false
}
```

`station`, `temperature`, and `timestamp` are required. `humidity` is optional because it is not in the `required` list. `additionalProperties: false` rejects any keys not listed in `properties`.

</details>

### Q6 Validating JSON Against a Schema

Validate `data.json` against `schema.json` using `check-jsonschema`.

<details>
<summary>Solution</summary>

```bash
check-jsonschema --schema-file schema.json data.json
```

`check-jsonschema` reads the schema and the instance, validates the instance against the schema, and prints a pass/fail result. On failure, it reports which constraints were violated and where.

For batch validation of multiple files:

```bash
check-jsonschema --schema-file schema.json *.json
```

</details>

### Q7 Handling Broken JSON Files

A JSON file has a trailing comma or a missing closing brace. How do you detect and report this?

<details>
<summary>Solution</summary>

Use `jq` to detect malformed JSON:

```bash
jq . broken.json
```

`jq` parses the input and prints an error message if the JSON is invalid. The error message includes the line and column where parsing failed.

For automated checking:

```bash
if ! jq empty broken.json 2>/dev/null; then
    echo "Invalid JSON"
    jq . broken.json
fi
```

`jq empty` parses the input but produces no output. It succeeds if the JSON is valid and fails if it is not. The `2>/dev/null` suppresses the error message in the conditional, then the second `jq` call prints the diagnostic.

`check-jsonschema` will also fail on broken JSON, but its error message points to the schema violation, not the parse error. Use `jq` first to confirm the JSON is well-formed before running schema validation.

</details>

### Q8 Reproducible Validation with Bowtie

What is Bowtie, and how does it improve reproducibility of JSON Schema validation?

<details>
<summary>Solution</summary>

**Bowtie** is a meta-validator for JSON Schema. Instead of relying on a single validator implementation, Bowtie runs multiple validators in separate Docker containers. Each container freezes a specific validator at a specific version.

Why this matters for reproducibility:

- Different validators support different subsets of JSON Schema. A schema that passes one validator may fail another.
- Validators are software, and they change over time. A schema that validates today may fail tomorrow if the validator is updated.
- Bowtie pins each validator to a specific version in a Docker image, so the validation environment is frozen and reproducible.
- Running multiple validators exposes implementation differences, so you know whether your schema relies on behavior that is universal or implementation-specific.

Running Bowtie:

```bash
bowtie validate -i python-jsonschema -i go-jsonschema schema.json instance.json
```

Each `-i` flag selects a validator implementation. Bowtie pulls the corresponding Docker image, runs the validation, and reports results from each implementation. If all implementations agree, you have higher confidence that your schema behaves consistently. If they disagree, you know your schema depends on implementation-specific behavior.

</details>

### Q9 Relational vs XML vs JSON

Fill in the comparison table for the three data formats.

<details>
<summary>Solution</summary>

| Aspect | Relational | XML | JSON |
|---|---|---|---|
| Structure | Schema-based tables (rows and columns) | Hierarchical tree of elements | Nested key-value pairs (objects and arrays) |
| Schema | Strict, predefined (DDL) | DTD or XSD | None by default (optional JSON Schema) |
| Queries | SQL | XPath, XQuery | No standard query language |
| Ordering | No inherent row order | Document order matters | No object order (array order matters) |
| Implementation | RDBMS with a query engine | XML parsers (DOM, SAX) | JSON parsers (built into most languages) |

Relational data is flat and rigid. XML and JSON are hierarchical and self-describing. JSON carries no schema unless you add one, which is why JSON Schema exists.

</details>

### Q10 JSON Structural Equivalence

Consider two JSON instances that differ only in the order of object properties. Are they structurally equivalent?

<details>
<summary>Solution</summary>

**Yes, they are structurally equivalent.** JSON is an unordered data format. The order of properties inside an object does not matter, so swapping two keys changes nothing structurally. A plain text `diff` will flag the lines as different, but that is a syntactic difference, not a structural one.

The order of array items does matter. If two arrays have the same elements in different order, they are not equivalent unless you treat arrays as unordered (which the JSON spec does not).

This is why `jq -S` (sort keys) is the correct tool for comparing JSON: it normalizes key order so `diff` only reports genuine differences.

</details>

### Q11 Schema Validation Data Flow

Label the components of the schema validation data flow.

<details>
<summary>Solution</summary>

The flow has four parts:

1. **Instance** (input): the JSON document being checked.
2. **Schema** (input): the JSON Schema that defines the expected structure.
3. **Validator** (process): the tool that checks the instance against the schema.
4. **Result** (output): `valid` if the instance matches the schema, `invalid` otherwise.

```
Instance ---+
            +---> Validator ---> valid / invalid
Schema   ---+
```

</details>

### Q12 Combinators: allOf, anyOf, oneOf

Given the schema:
```json
{ "oneOf": [ { "type": "string" }, { "maxLength": 5 } ] }
```

Which instances are valid: `"foo"`, `"a"`, `"1234567890"`, `42`?

<details>
<summary>Solution</summary>

`oneOf` requires the instance to satisfy exactly one subschema.

- `"foo"`: is a string (matches subschema 1) and has length 3, which is 5 or less (matches subschema 2). Matches both. Invalid.
- `"a"`: is a string (matches subschema 1) and has length 1, which is 5 or less (matches subschema 2). Matches both. Invalid.
- `"1234567890"`: is a string (matches subschema 1) but has length 10, which exceeds 5 (does not match subschema 2). Matches exactly one. Valid.
- `42`: is not a string (fails subschema 1) and does not satisfy `maxLength` for non-strings under the exercise framing (fails subschema 2). Matches zero. Invalid.

**Valid:** `"1234567890"`. **Invalid:** `"foo"`, `"a"`, `42`.

The trap is the overlap between the two subschemas. Short strings satisfy both `{"type": "string"}` and `{"maxLength": 5}`, so `oneOf` rejects them.

</details>

## Key Takeaways

- `jq .` pretty-prints JSON. `jq -c` produces compact output. `jq -S` sorts keys for reliable comparison.
- `diff` on raw JSON is unreliable because formatting and key order cause false differences. Normalize with `jq -S` first.
- JSON Schema declares types, required properties, and optional properties. `check-jsonschema` validates instances against schemas.
- Broken JSON (trailing commas, missing braces) is detected by `jq` before schema validation.
- Bowtie runs multiple validators in pinned Docker containers, exposing implementation differences and making validation reproducible.
- JSON objects are unordered, so property order does not affect structural equivalence. Array order does matter.

## Related Vault Pages

- [[json-schema]]: the validation vocabulary used throughout this sheet
- [[reproducibility-engineering-lecture-8]]: the lecture this sheet accompanies
- [[reproducibility-engineering-lecture-9]]: LLMs use JSON Schema for constrained decoding
