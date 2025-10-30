# 🧩 Module C — String Processing
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module focuses on **string manipulation**, **text cleaning**, and **character-level analysis** — all fundamental operations in data preprocessing and ETL text handling.  
It helps you understand how to slice, reverse, count, and normalize strings efficiently in Python.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **Reverse String** | Return the reversed version of the string | String slicing `[::-1]` |
| P2 | **Palindrome Check** | Determine if a string reads the same forward and backward | String comparison |
| P3 | **Character Count** | Count occurrences of each character | Dictionary counting with `.get()` |
| P4 | **Clean String** | Remove spaces and lowercase text | `strip()` + `lower()` |
| P5 | **Reverse Words in Sentence** | Reverse word order in a string | `split()` + `reversed()` + `join()` |

All problems are implemented in `quick.py`, demonstrating practical string handling.

---

## ⚙️ Multi-Version Structure

Each problem will be provided in **three versions**, all under the `drills/` directory:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py) | Pythonic string utilities and slicing |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py)  | Manual iteration and concatenation logic |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py) | Simulates low-level memory-based string reversal and parsing |

Each file concludes with a consistent registry for test automation:
```python
REGISTRY = {
    "P1": run_P1_reverse_string,
    "P2": run_P2_is_palindrome,
    "P3": run_P3_char_count,
    "P4": run_P4_clean_string,
    "P5": run_P5_reverse_words,
}
```

---

## 🧪 Testing — `tests_drills.py`

This test file imports each implementation (`quick`, `lowlevel`, `c_like`) and runs the registered problems automatically.  

Example test cases:
```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": (("hello",), "olleh"),
    "P2": (("racecar",), True),
    "P3": (("banana",), {'b':1, 'a':3, 'n':2}),
    "P4": (("   HelLo  ",), "hello"),
    "P5": (("the sky is blue",), "blue is sky the"),
}
```

Run the tests with:
```bash
pytest -q coding_training/basic/moduleC_string_processing/drills/tests_drills.py
```

✅ Each implementation is validated automatically to ensure consistent behavior across multiple versions.

---

## 🧭 Learning Goals

- Learn Pythonic string slicing and built-in functions (`strip`, `split`, `join`)  
- Understand how to build manual string-processing loops  
- Practice dictionary-based character frequency counting  
- Prepare for deeper text normalization tasks in ETL or NLP preprocessing

---

## 🧩 File Structure

```
moduleC_string_processing/
└─ drills/
   ├─ quick.py          ← Pythonic version (working)
   ├─ lowlevel.py       ← Manual character-by-character version (WIP)
   ├─ c_like.py         ← C-style low-level simulation (coming soon)
   ├─ tests_drills.py   ← Automated tests for all versions
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Strings are immutable in Python — every modification creates a new copy.  
> Learning when to use built-in methods and when to manually build strings helps you balance **readability** and **performance**.
