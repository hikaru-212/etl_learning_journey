# 🧩 Module D — Iteration & Enumeration
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module focuses on **iteration patterns**, **enumeration**, and **built-in aggregate functions** such as `any()`, `all()`, and `zip()`.  
These problems are designed to train your ability to traverse and combine collections effectively — a skill that becomes crucial in data pipelines and ETL logic construction.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **First Negative Index** | Find the index of the first negative number | `enumerate` + early return |
| P2 | **Pairwise Sum** | Add two lists element by element | `zip` for parallel iteration |
| P3 | **Chunk Pairs** | Split a list into 2-element tuples | Step slicing + tuple grouping |
| P4 | **Parity & Sign Check** | Return `(any_even, all_positive)` flags | `any()` / `all()` aggregation |
| P5 | **Sort by Length then Lexicographically** | Sort strings first by length, then alphabetically | `sorted()` with `lambda` multi-key |

All problems are implemented in `quick.py`, demonstrating Pythonic iteration idioms.

---

## ⚙️ Multi-Version Structure

Each problem will be provided in **three versions**, all under the `drills/` directory:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py) | Pythonic style with built-in helpers (`zip`, `any`, `all`, `sorted`) |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py)  | Manual iteration using `for` loops and explicit conditions |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py) | Simulates pointer-based iteration using indices only |

Each file ends with a consistent `REGISTRY` mapping to register all problems:
```python
REGISTRY = {
    "P1": run_P1_first_negative_index,
    "P2": run_P2_pairwise_sum,
    "P3": run_P3_chunk_pairs,
    "P4": run_P4_parity_and_sign,
    "P5": run_P5_sort_by_len_then_lex,
}
```

This enables automated testing through a unified interface.

---

## 🧪 Testing — `tests_drills.py`

`tests_drills.py` is the automated test suite for this module.  
It imports each version (`quick`, `lowlevel`, `c_like`) and verifies all registered functions with sample inputs and expected outputs.

Example:
```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": (([3,8,-2,5],), 2),
    "P2": (([1,2,3],[4,5,6]), [5,7,9]),
    "P3": (([1,2,3,4,5,6],), [(1,2),(3,4),(5,6)]),
    "P4": (([2,3,-1],), (True, False)),
    "P5": ((["car","a","bat","aa"],), ["a","aa","bat","car"]),
}
```

Run all tests with:
```bash
pytest -q coding_training/basic/moduleD_iteration_enumeration/drills/tests_drills.py
```

✅ The test framework will run every registered problem across all implementations,  
verifying their outputs automatically.

---

## 🧭 Learning Goals

- Understand and apply `enumerate`, `zip`, and iteration ranges  
- Learn to aggregate logical conditions using `any()` and `all()`  
- Practice multi-key sorting and tuple-based data structuring  
- Build confidence in translating Pythonic loops to lower-level control structures

---

## 🧩 File Structure

```
moduleD_iteration_enumeration/
└─ drills/
   ├─ quick.py          ← Pythonic version (working)
   ├─ lowlevel.py       ← Manual loop version (WIP)
   ├─ c_like.py         ← C-style index-based version (coming soon)
   ├─ tests_drills.py   ← Automated tests for all versions
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Python’s iteration tools like `enumerate`, `zip`, and `sorted(key=...)` are more than shortcuts —  
> they form the foundation for **iterator pipelines** in ETL tasks and data engineering.  
> Learning to express logic with these primitives will make your code both **concise** and **readable**.
