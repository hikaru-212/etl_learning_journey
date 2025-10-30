# 🧩 Module E — Comprehensions & Data Transformation
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module focuses on mastering **Python comprehension techniques** — one of the most concise and powerful tools for data transformation.  
Each problem demonstrates how to express loops and conditions within **list, set, and dict comprehensions** efficiently.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **Even Squares** | Return squares of all even numbers | List comprehension + conditional |
| P2 | **Unique Word Lengths** | Collect distinct word lengths from a sentence | Set comprehension |
| P3 | **Character → ASCII Mapping** | Map each character to its ASCII value | Dict comprehension + `ord()` |
| P4 | **Flatten 2D List** | Merge nested lists into one flat list | Nested list comprehension |
| P5 | **Filter & Uppercase 'p'-Words** | Filter words starting with ‘p’ and convert to uppercase | Conditional + transformation in comprehension |

All examples are implemented in `quick.py`, showcasing elegant and readable one-liners.

---

## ⚙️ Multi-Version Structure

Each comprehension problem will be reimplemented in **three versions**, all stored in the `drills/` folder:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py) | Pythonic one-liners using comprehension syntax |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py)  | Expanded loops using `for` and `if` (no comprehension) |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py) | Manual array processing with preallocated memory simulation |

Each file defines identical function names, such as:
```python
def run_P1_even_squares(nums: list[int]) -> list[int]:
    ...
```

and ends with a `REGISTRY` mapping:
```python
REGISTRY = {
    "P1": run_P1_even_squares,
    "P2": run_P2_unique_word_lengths,
    "P3": run_P3_char_to_ascii,
    "P4": run_P4_flatten_2d,
    "P5": run_P5_filter_upper_p,
}
```

This unified format allows automated tests to locate and execute all exercises seamlessly.

---

## 🧪 Testing — `tests_drills.py`

The `tests_drills.py` file serves as the **central test runner** for this module.  
It imports every implementation (`quick`, `lowlevel`, `c_like`) and verifies their correctness using pre-defined input–output pairs.

Example test cases:
```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": (([1,2,3,4,5],), [4,16]),
    "P2": (("I love Python very much",), {1,4,6,5}),
    "P3": (("abc",), {'a':97, 'b':98, 'c':99}),
    "P4": (([[1,2],[3,4],[5]],), [1,2,3,4,5]),
    "P5": ((["python", "java", "php", "c++"],), ["PYTHON", "PHP"]),
}
```

Run all tests automatically with:
```bash
pytest -q coding_training/basic/moduleE_comprehensions/drills/tests_drills.py
```

✅ The test suite will iterate over all implementations,  
compare each function’s output with the expected answer,  
and report any discrepancies for easy debugging.

---

## 🧭 Learning Goals

- Master Python’s **list / set / dict comprehensions**  
- Understand when to prefer comprehension vs. explicit loops  
- Develop habits of concise and functional-style data processing  
- Build groundwork for future **C-style manual loop refactoring**

---

## 🧩 File Structure

```
moduleE_comprehensions/
└─ drills/
   ├─ quick.py          ← Pythonic version (working)
   ├─ lowlevel.py       ← Manual for-loop version (WIP)
   ├─ c_like.py         ← C-style simulation (coming soon)
   ├─ tests_drills.py   ← Automated tests for all versions
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Comprehensions are not just “syntactic sugar.”  
> They reflect **Pythonic data flow thinking**, and this module will prepare you to rewrite them manually in low-level or C-like code when needed.
