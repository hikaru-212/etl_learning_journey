# 🧩 Module A — Control Flow Basics
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module introduces **Python control flow fundamentals**, including conditionals, loops, and basic logic construction.  
It lays the groundwork for later algorithmic problem-solving and ETL process automation.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **FizzBuzz** | Print numbers 1–n with rules for multiples of 3 and 5 | `if-elif-else` + modulo logic |
| P2 | **Min, Max, Sum Stats** | Return `(min, max, total)` of a list | Conditional aggregation |
| P3 | **Count Even & Odd** | Count number of even and odd integers | Conditional counting in loops |
| P4 | **Factorial (Iterative)** | Compute `n!` using a while-loop | Iteration + accumulator pattern |
| P5 | **First Greater than Threshold** | Return the first element greater than a given value | Early return in loop |

All examples are implemented in `quick.py` with clear, beginner-friendly logic.

---

## ⚙️ Multi-Version Structure

Each problem will be implemented in **three tiers**, organized in the `drills/` directory:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py) | Clean and readable Python logic |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py) | Expanded loops with explicit indexing and manual tracking |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py) | Simulates manual memory and counter management (no Python built-ins) |

Every file ends with a consistent function registry for unified testing:
```python
REGISTRY = {
    "P1": run_P1_fizz_buzz,
    "P2": run_P2_stats,
    "P3": run_P3_count_even_odd,
    "P4": run_P4_facotrial,
    "P5": run_P5_first_greater,
}
```

---

## 🧪 Testing — `tests_drills.py`

The module’s automated test file runs all problems across every implementation version.

Example configuration:
```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": ((15,), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
    "P2": (([1,3,7,2,6],), (1,7,19)),
    "P3": (([1,2,3,4,5],), (2,3)),
    "P4": ((5,), 120),
    "P5": (([1,2,3,5,6],4), 5),
}
```

Run tests with:
```bash
pytest -q coding_training/basic/moduleA_control_flow/drills/tests_drills.py
```

✅ All implementations are validated automatically for correctness and consistency.

---

## 🧭 Learning Goals

- Master conditional structures (`if`, `elif`, `else`)  
- Understand iteration using `for` and `while` loops  
- Learn to use early return patterns for efficiency  
- Build a foundation for data processing and control logic in ETL scripts

---

## 🧩 File Structure

```
moduleA_control_flow/
└─ drills/
   ├─ quick.py          ← Pythonic control flow version
   ├─ lowlevel.py       ← Expanded manual version (WIP)
   ├─ c_like.py         ← Low-level simulation (coming soon)
   ├─ tests_drills.py   ← Centralized testing for all versions
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Control flow is the **foundation of every algorithm**.  
> The patterns learned here — iteration, branching, and early exits — will reappear in every future module, from data validation to pipeline orchestration.
