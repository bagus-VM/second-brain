---
title: "Exercise Sheet 8 — Hierarchical Data"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-25
---

# Exercise Sheet 8 — Hierarchical Data

## Exercises

### Q1 Relational vs XML vs JSON

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

### Q2 JSON Structural Equivalence

Consider the two JSON instances below.

Left:
```json
{
    "productId": 1,
    "productName": "A green door",
    "price": 12.50,
    "tags": [ "home", "green" ]
}
```

Right:
```json
{
    "productId": 1,
    "productName": "A green door",
    "tags": [ "green", "home" ],
    "price": 12.50
}
```

Are they structurally equivalent?

<details>
<summary>Solution</summary>

**Yes, they are structurally equivalent.** JSON is an unordered data format. The order of properties inside an object does not matter, so swapping `price` and `tags` changes nothing. A plain text `diff` will flag the lines as different, but that is a syntactic difference, not a structural one.

The order of array items does matter. In these two instances the `tags` arrays are `["home", "green"]` and `["green", "home"]`. For strict structural equivalence you would also need the array contents to match in order. The exercise focuses on the object-property ordering, and the intended answer is: yes, because JSON is unordered.

</details>

### Q3 Schema Validation Data Flow

Label the chart that illustrates the data flow in schema validation.

<details>
<summary>Solution</summary>

The flow has four parts:

1. **Instance** (input): the JSON document being checked.
2. **Schema** (input): the JSON Schema that defines the expected structure.
3. **Validator** (process): the tool that checks the instance against the schema.
4. **Result** (output): `valid` if the instance matches the schema, `invalid` otherwise.

```
Instance ─┐
          ├─→ Validator ─→ valid / invalid
Schema  ──┘
```

</details>

### Q4 Benefits of JSON Schema Validation

What are the benefits of validating JSON instances against a JSON Schema?

<details>
<summary>Solution</summary>

- **Catch errors early**: invalid data is rejected before it reaches downstream code, so a missing field or wrong type fails fast instead of causing a silent bug.
- **Machine-readable**: unlike a README, a schema can be checked automatically. You can run validation in tests and CI pipelines.
- **API contracts**: a published schema documents what a service accepts and returns. Clients and servers agree on the structure.
- **Reproducibility**: when an experiment outputs JSON, a schema pins the data format. A schema violation is a concrete bug, not a vague "the data looks wrong".

</details>

### Q5 Schema Validity

Given the product schema below, decide which statements about instance validity are true.

```json
{
    "title": "Product",
    "description": "A product from Acme's catalog",
    "type": "object",
    "properties": {
        "productId": { "description": "The unique identifier for a product", "type": "integer" },
        "productName": { "description": "Name of the product", "type": "string" },
        "price": { "description": "The price of the product", "type": "number", "exclusiveMinimum": 0 },
        "tags": { "description": "Tags for the product", "type": "array", "items": { "type": "string" }, "minItems": 1, "uniqueItems": true }
    },
    "required": [ "productId", "productName", "price" ]
}
```

<details>
<summary>Solution</summary>

Work through the schema line by line. Lines 1 to 3 are just `title` and `description`, so they add no constraints. Line 4 adds `"type": "object"`. Lines 5 to 28 define `properties` (but properties are optional unless listed in `required`). Line 29 adds the `required` list: `productId`, `productName`, `price`. Note that `additionalProperties` is not set to `false`, so extra keys are allowed. JSON is case-sensitive, so `"ProductName"` is a different key from `"productName"`.

| Instance | Valid? | Reason |
|---|---|---|
| Left instance from Q2 (`productId` 1, `productName` "A green door", `price` 12.50, `tags` ["home", "green"]) | Yes (full schema) | All required fields present with correct types. `price` > 0. `tags` has 2 unique strings, satisfies `minItems` 1. |
| `"Hello world!"`, valid up to line 3 | Yes | No constraints yet. |
| `"Hello world!"`, valid up to line 4 | No | Line 4 requires `type: "object"`. A string is not an object. |
| Left instance from Q2, valid up to line 4 | Yes | It is an object. |
| `{ "foo": 42 }`, valid up to line 28 | Yes | It is an object. No `required` yet, and `foo` is an allowed additional property. |
| `{ "ProductName": 42 }`, valid up to line 28 | Yes | Object with an additional property. `productName` is not required until line 29. |
| `{ "ProductName": 42 }`, valid for the full schema | No | `productName` (lowercase) is required at line 29 and is missing. The capitalised `ProductName` does not satisfy it. |
| Left instance from Q2, valid for the full schema | Yes | Passes every constraint. |
| `tags: [ ]` (empty array) | No | `minItems: 1` fails. |
| `tags: [ "special offer", "special offer" ]` | No | `uniqueItems: true` fails (duplicate values). |
| Instance with an extra `discount: 0.1` | Yes | `additionalProperties` is not `false`, so extra keys are allowed. All required fields and constraints still pass. |

</details>

### Q6 allOf

Schema:
```json
{
    "allOf": [
      { "type": "string" },
      { "maxLength": 5 }
    ]
}
```

Which instances are valid: `"foo"`, `"a"`, `"1234567890"`, `42`?

<details>
<summary>Solution</summary>

`allOf` requires the instance to satisfy **all** subschemas.

- `"foo"`: is a string and has length 3 ≤ 5. Valid.
- `"a"`: is a string and has length 1 ≤ 5. Valid.
- `"1234567890"`: is a string but has length 10 > 5. Fails `maxLength`. Invalid.
- `42`: is not a string. Fails `{ "type": "string" }`. Invalid.

**Valid:** `"foo"`, `"a"`. **Invalid:** `"1234567890"`, `42`.

</details>

### Q7 anyOf

Schema:
```json
{
    "anyOf": [
      { "type": "string" },
      { "maxLength": 5 }
    ]
}
```

Which instances are valid: `"foo"`, `"a"`, `"1234567890"`, `42`?

<details>
<summary>Solution</summary>

`anyOf` requires the instance to satisfy **at least one** subschema.

- `"foo"`: is a string. Satisfies the first subschema. Valid.
- `"a"`: is a string. Satisfies the first subschema. Valid.
- `"1234567890"`: is a string. Satisfies the first subschema (it does not need to satisfy `maxLength`). Valid.
- `42`: is not a string, so it fails `{ "type": "string" }`. The exercise treats `maxLength` as a string-length constraint, so a number does not satisfy `{ "maxLength": 5 }` either. Invalid.

**Valid:** `"foo"`, `"a"`, `"1234567890"`. **Invalid:** `42`.

Note on the spec: strictly, JSON Schema ignores string-only keywords like `maxLength` for non-string instances, so `{ "maxLength": 5 }` alone would accept a number. The exercise frames `maxLength` as a string constraint, which is why `42` is treated as invalid here.

</details>

### Q8 oneOf

Schema:
```json
{
    "oneOf": [
      { "type": "string" },
      { "maxLength": 5 }
    ]
}
```

Which instances are valid: `"foo"`, `"a"`, `"1234567890"`, `42`?

<details>
<summary>Solution</summary>

`oneOf` requires the instance to satisfy **exactly one** subschema. If an instance matches zero or matches more than one, it is invalid.

- `"foo"`: is a string (matches subschema 1) and has length 3 ≤ 5 (matches subschema 2). Matches **both**. Invalid.
- `"a"`: is a string (matches subschema 1) and has length 1 ≤ 5 (matches subschema 2). Matches **both**. Invalid.
- `"1234567890"`: is a string (matches subschema 1) but has length 10 > 5 (does not match subschema 2). Matches **exactly one**. Valid.
- `42`: is not a string (fails subschema 1) and, under the exercise's string-length framing, does not satisfy `maxLength` (fails subschema 2). Matches **zero**. Invalid.

**Valid:** `"1234567890"`. **Invalid:** `"foo"`, `"a"`, `42`.

The trap here is the overlap between the two subschemas. Short strings satisfy both `{ "type": "string" }` and `{ "maxLength": 5 }`, so `oneOf` rejects them. Only a string that is too long for `maxLength` lands in exactly one subschema.

</details>

### Q9 Schema Equivalence

Compare the two schemas:

Left:
```json
{ "oneOf": [ { "type": "string" }, { "type": "integer" } ] }
```

Right:
```json
{ "anyOf": [ { "type": "integer" }, { "type": "string" } ] }
```

Which statements are true?

<details>
<summary>Solution</summary>

- "There exists a JSON instance valid for the right schema but not the left": **false**. Both schemas accept exactly the integers and the strings.
- "The schemas are structurally equivalent": **false**. The left uses `oneOf`, the right uses `anyOf`, and the subschema order differs.
- "The schemas are semantically equivalent": **true**. A value can never be both a string and an integer at once, so matching "at least one" and matching "exactly one" accept the same instances.
- "None of these options": **false**.

**Answer:** the schemas are semantically equivalent but not structurally equivalent. `oneOf` and `anyOf` collapse to the same language whenever the subschemas describe disjoint types.

</details>

### Q10 HDF5 vs XML vs JSON

When would you prefer HDF5 over XML or JSON, and when not?

<details>
<summary>Solution</summary>

**Prefer HDF5 for:**
- Large numerical arrays, especially multi-dimensional ones (climate grids, detector reads, image volumes).
- Scientific data with rich metadata that belongs in a hierarchy (groups for components, datasets for variables, attributes for units and provenance).
- Datasets that need chunking, compression, or parallel I/O for efficient partial reads.

**Prefer XML or JSON for:**
- Human-readable data that people will inspect or edit by hand.
- Web APIs and configuration files, where text-based tools and broad language support matter.
- Small to medium structured records exchanged between systems.

HDF5 is binary and compact but opaque to text tools. XML and JSON are readable and universal but inefficient for large numerical arrays. Pick the format that matches the data shape and the workflow.

</details>

### Q11 Weather Station Data in HDF5

Temperature, wind, and metadata are collected from two weather stations and stored as CSV.

(a) What are the benefits and drawbacks of the tabular layout?
(b) Store the data in HDF5 with the structure below, completing the h5py code.

```
/
+-- 15
|   +-- temperature
|   +-- wind
|
+-- 20
    +-- temperature
```

<details>
<summary>Solution</summary>

**(a) Benefits and drawbacks of the tabular CSV layout**

Benefits:
- Simple and human-readable. Any spreadsheet or text tool can open it.
- Easy to inspect and diff.

Drawbacks:
- Three separate tables (temperature, wind, metadata) must be joined on `station` and `time`. The hierarchy is implicit, not structural.
- Metadata sits in a long key-value table, which is awkward to query and easy to ignore.
- Mixed units across stations (Celsius vs Fahrenheit) live only in the metadata table, so a careless reader can misread a value.
- No type information, no compression, no partial I/O. Reading one station's temperature still scans the whole file.

**(b) Completed h5py code**

```python
import numpy as np
import h5py

def main():
    # Keeping things very simple here.
    temperature_station_15 = np.array([18.2, 18.4, 18.7, 19.0, 19.1])
    wind_station_15 = np.array([3.1, 3.3, 2.8, 4.0, 3.7])
    temperature_station_20 = np.array([64.0, 65.0, 66.1, 65.8])
    start_time = 0  # Should be a proper timestamp.

    with h5py.File("weather.hdf5", "w") as f:

        # Store data for weather station 15.
        # h5py creates the intermediate group "/15" automatically.
        f["/15/temperature"] = temperature_station_15
        f["/15/temperature"].attrs["delta"] = 5.0
        f["/15/temperature"].attrs["start time"] = start_time
        f["/15/temperature"].attrs["temp unit"] = "degree Celsius"

        f["/15/wind"] = wind_station_15
        f["/15/wind"].attrs["delta"] = 5.0
        f["/15/wind"].attrs["start time"] = start_time
        f["/15/wind"].attrs["wind unit"] = "m/s"

        # Store data for weather station 20.
        f["/20/temperature"] = temperature_station_20
        f["/20/temperature"].attrs["delta"] = 10.0
        f["/20/temperature"].attrs["start time"] = start_time
        f["/20/temperature"].attrs["temp unit"] = "degree Fahrenheit"

        f.attrs["description"] = "Weather station data (temperature and wind)"

if __name__ == "__main__":
    main()
```

The hierarchy mirrors the physical setup: one group per station, one dataset per measurement, and attributes carrying `delta`, `start time`, and the unit. Units now travel with the data, so station 20's Fahrenheit values cannot be confused with station 15's Celsius values. The single self-describing file replaces three loosely coupled CSV tables.

</details>

## Key Takeaways
- Relational data is flat and schema-strict. XML and JSON are hierarchical and self-describing. JSON has no schema unless you add JSON Schema.
- JSON objects are unordered, so property order does not affect structural equivalence. Array order does matter.
- JSON Schema combinators compose subschemas: `allOf` (all must match), `anyOf` (at least one), `oneOf` (exactly one). Watch for overlapping subschemas with `oneOf`.
- `oneOf` and `anyOf` over disjoint types are semantically equivalent even when structurally different.
- Pick HDF5 for large numerical arrays and metadata-rich scientific hierarchies. Pick XML or JSON for readable, text-tool-friendly data and APIs.

## Related Vault Pages
- [[json-schema]] — the validation vocabulary used in Q3 to Q9
- [[hdf5]] — the hierarchical format used in Q11
- [[reproducibility-engineering-lecture-8]] — the lecture this sheet accompanies
