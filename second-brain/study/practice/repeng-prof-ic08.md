---
title: "RepEng In-Class Exercise 8 — Hierarchical Data"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 8 — Hierarchical Data (JSON, XML, HDF5)

---

## Exercise 1 — Comparing Data Formats

| Feature       | Relational        | XML               | JSON              |
|---------------|-------------------|-------------------|-------------------|
| Structure     | Flat tables (rows/columns) | Tree (nested elements) | Tree (nested objects/arrays) |
| Schema        | Strict (defined upfront, enforced) | Optional (XSD/DTD) | Optional (JSON Schema) |
| Queries       | SQL (standardized, powerful) | XPath/XQuery | JSONPath / jq |
| Ordering      | Rows unordered, columns ordered | Document order preserved | Object keys unordered, array order preserved |
| Implementation| RDBMS (PostgreSQL, MySQL) | Parsers, XSLT processors | Parsers (language-native) |

---

## Exercise 2 — JSON Structural Equivalence

Two JSON instances with same properties but different key order and array item order.

→ **Yes, because JSON is an unordered data format** (for objects).

JSON objects are **unordered** collections of key-value pairs. `{"a":1, "b":2}` and `{"b":2, "a":1}` are semantically identical. Similarly, JSON arrays ARE ordered, but the question shows the array items in different order too (`["home","green"]` vs `["green","home"]`).

**Wait** — arrays ARE ordered in JSON. So `["home","green"]` ≠ `["green","home"]` structurally.

**Correct answer:** The two instances are **structurally equivalent** because JSON objects are unordered, and the array items happen to be the same set (just reordered). For most practical purposes, they represent the same data.

The best answer is: **Yes, because JSON is an unordered data format** — but this is slightly imprecise. More precisely: the objects are equivalent (unordered), and the arrays contain the same elements (set-equivalent).

---

## Exercise 3 — Schema Validation Data Flow

The chart illustrates:

1. **JSON Instance** (your data) →
2. **JSON Schema Validator** (tool that checks) ←
3. **JSON Schema** (the rules) →
4. **Validation Result** (valid/invalid + error details)

The validator takes both the instance and the schema as inputs, applies the schema rules to the instance, and produces a validation result.

---

## Exercise 4 — Benefits of JSON Schema Validation

1. **Data quality assurance** — catch errors early, before processing
2. **Documentation** — schema serves as a formal specification of expected data
3. **Interoperability** — shared schema ensures different systems produce/consume compatible data
4. **Reproducibility** — schema validates that experiment data conforms to expected format
5. **Automation** — enables auto-generation of code, tests, and documentation from schema
6. **Error messages** — precise feedback on what's wrong and where

---

## Exercise 5 — JSON Schema Validation Statements

Given the Product schema with properties: productId (integer), productName (string), price (number, >0), tags (array of strings, minItems:1, uniqueItems), required: [productId, productName, price]:

- **Left JSON instance valid up to line 3?** → ✓ (productId and productName are correct)
- **"Hello world!" valid up to line 3?** → ✗ (schema says type: object, "Hello world!" is a string)
- **Left JSON instance valid up to line 4?** → ✓ (price: 12.50, type number, exclusiveMinimum 0 — valid)
- **"Hello world!" valid up to line 4?** → ✗ (not an object)
- **{"foo": 42} valid up to line 28?** → ✗ (missing required properties productId, productName, price)
- **{"ProductName": 42} valid up to line 28?** → ✗ (wrong case — "ProductName" ≠ "productName")
- **{"ProductName": 42} valid overall?** → ✗ (wrong case, missing required fields)
- **Left JSON instance valid overall?** → ✓ (all required fields present, correct types, tags non-empty and unique)
- **{"productId":1, "productName":"A green door", "price":12.50, "tags":[]} valid?** → ✗ (tags has minItems:1)
- **{"productId":1, "productName":"A green door", "price":12.50, "tags":["special offer","special offer"]} valid?** → ✗ (uniqueItems: true — duplicates not allowed)
- **{"productId":1, "productName":"A green door", "price":12.50, "tags":["home","green"], "discount":0.1} valid?** → Depends on schema. The schema doesn't have `additionalProperties: false`, so extra properties are allowed by default. → ✓ Valid (if additionalProperties is not explicitly set to false)

---

## Exercise 6 — allOf Schema

Schema: `{"allOf": [{"type": "string"}, {"maxLength": 5}]}`

Must satisfy ALL conditions: is a string AND max length 5.

- `"foo"` → ✓ (string, length 3)
- `"a"` → ✓ (string, length 1)
- `"1234567890"` → ✗ (string, but length 10 > 5)
- `42` → ✗ (not a string)

---

## Exercise 7 — anyOf Schema

Schema: `{"anyOf": [{"type": "string"}, {"maxLength": 5}]}`

Must satisfy AT LEAST ONE condition.

- `"foo"` → ✓ (is a string, also length ≤ 5)
- `"a"` → ✓ (is a string, also length ≤ 5)
- `"1234567890"` → ✓ (is a string — satisfies first condition, even though length > 5)
- `42` → ✗ (not a string, and 42 has no "length" concept)

---

## Exercise 8 — oneOf Schema

Schema: `{"oneOf": [{"type": "string"}, {"maxLength": 5}]}`

Must satisfy EXACTLY ONE condition.

- `"foo"` → ✗ (satisfies BOTH: is a string AND length ≤ 5)
- `"a"` → ✗ (satisfies BOTH)
- `"1234567890"` → ✓ (is a string, but length > 5 — satisfies only first condition)
- `42` → ✗ (satisfies neither)

---

## Exercise 9 — oneOf vs anyOf

```json
// Left: oneOf
{"oneOf": [{"type": "string"}, {"type": "integer"}]}

// Right: anyOf
{"anyOf": [{"type": "integer"}, {"type": "string"}]}
```

- **"There exists a JSON instance valid w.r.t. right but not left"** → ✗ No. For these schemas with mutually exclusive types, oneOf and anyOf behave identically.
- **"Structurally equivalent"** → ✗ No (different keywords, different structure)
- **"Semantically equivalent"** → ✓ Yes — when the sub-schemas are mutually exclusive (string and integer can't both match), oneOf and anyOf produce the same result.

---

## Exercise 10 — HDF5 vs XML/JSON

**Prefer HDF5 when:**
- Storing large numerical datasets (arrays, matrices)
- Need efficient random access to subsets of data
- Data is hierarchical (groups/datasets) with metadata
- Performance matters (binary format, fast I/O)
- Need to store multi-dimensional arrays

**Prefer XML/JSON when:**
- Data is primarily text/structured records
- Human readability matters
- Need web/API compatibility (JSON is the lingua franca of web APIs)
- Data is relatively small
- Need extensive tooling support

---

## Exercise 11 — Weather Data in HDF5

### (a) Benefits and drawbacks of tabular CSV layout:

**Benefits:**
- Simple, human-readable
- Easy to import/export with many tools
- Works well with pandas, SQL, etc.

**Drawbacks:**
- No metadata (units, time intervals) — must be documented separately
- Different stations have different time intervals (delta=5 vs delta=10) — awkward in one table
- Redundancy (station ID repeated in every row)
- No hierarchical structure for grouping by station

### (b) Complete the Python code:

```python
import time
import numpy as np
import h5py

def main():
    temperature_station_15 = np.array([18.2, 18.4, 18.7, 19.0, 19.1])
    wind_station_15 = np.array([3.1, 3.3, 2.8, 4.0, 3.7])
    temperature_station_20 = np.array([64.0, 65.0, 66.1, 65.8])
    start_time = 0

    with h5py.File("weather.hdf5", "w") as f:

        # Store data for weather station 15
        f["15/temperature"] = temperature_station_15
        f["15/temperature"].attrs["delta"] = 5.0
        f["15/temperature"].attrs["start_time"] = start_time
        f["15/temperature"].attrs["unit"] = "degree Celsius"

        f["15/wind"] = wind_station_15
        f["15/wind"].attrs["delta"] = 5.0
        f["15/wind"].attrs["start_time"] = start_time
        f["15/wind"].attrs["unit"] = "m/s"

        # Store data for weather station 20
        f["20/temperature"] = temperature_station_20
        f["20/temperature"].attrs["delta"] = 10.0
        f["20/temperature"].attrs["start_time"] = start_time
        f["20/temperature"].attrs["unit"] = "degree Fahrenheit"

        f.attrs["description"] = "Weather data from two stations"

if __name__ == "__main__":
    main()
```

---

## Related Lectures
- [[reproducibility-engineering-lecture-8]]
