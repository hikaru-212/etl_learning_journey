# 🧩 Module G — Functions & Recursion
[⬅ Back to Basic Overview](../../README.md)

## 🎯 Overview
This module explores **recursive problem-solving** and **function-based decomposition** — essential skills for algorithm design and understanding execution flow.  
It builds on earlier modules by introducing *self-referential logic*, where functions call themselves to solve subproblems.

---

## 📚 Current Exercises (Quick Version)

| ID | Problem | Description | Core Concept |
|----|----------|--------------|---------------|
| P1 | **Recursive Factorial** | Compute n! recursively | Base case + recursive call |
| P2 | **Fibonacci Sequence** | Compute nth Fibonacci number | Tree recursion + overlapping subproblems |
| P3 | **Reverse String (Recursive)** | Reverse string using recursion | Slice and concatenate recursively |
| P4 | **Recursive Sum** | Compute sum of list elements recursively | Head–tail recursion |
| P5 | **Tree Traversal** | Traverse a nested dictionary tree | Recursion + list accumulation |

All implementations are in `quick.py` using pure recursion and function calls.

---

## ⚙️ Multi-Version Structure

Each problem has **three versions**, all stored under `drills/`:

| Version | File | Purpose |
|----------|------|----------|
| 🟢 Quick | [`quick.py`](quick.py) | Recursive and elegant Python implementations |
| 🟠 Low-Level | [`lowlevel.py`](lowlevel.py)  | Iterative (loop-based) equivalents to recursion |
| 🔵 C-Like (Coming Soon) | [`c_like.py`](c_like.py) | Simulates recursion using an explicit stack |

Each file concludes with a `REGISTRY` that maps problem IDs to function references:
```python
REGISTRY = {
    "P1": run_P1_factorial,
    "P2": run_P2_fib,
    "P3": run_P3_reverse_str,
    "P4": run_P4_recursive_sum,
    "P5": run_P5_traverse_tree,
}
```

This structure allows your test framework to import all problems uniformly.

---

## 🧪 Testing — `tests_drills.py`

`tests_drills.py` runs all problems across implementations automatically.

Example setup:
```python
IMPLS = ["quick", "lowlevel", "c_like"]
CASES = {
    "P1": ((5,), 120),
    "P2": ((6,), 8),
    "P3": (("hello",), "olleh"),
    "P4": (([1,2,3,4,5],), 15),
    "P5": (({"A":["B","C"],"B":["D"],"C":["E","F"]},"A"), ["A","B","D","C","E","F"]),
}
```

Run tests with:
```bash
pytest -q coding_training/basic/moduleG_functions_recursion/drills/tests_drills.py
```

✅ Each recursive function is verified for correctness and stability.

---

## 🧭 Learning Goals

- Understand recursion base cases and call stacks  
- Practice rewriting recursive logic into iterative versions  
- Learn to reason about **time complexity** and **stack depth**  
- Gain intuition for how recursive traversal works in tree and graph structures

---

## 🧩 File Structure

```
moduleG_functions_recursion/
└─ drills/
   ├─ quick.py          ← Recursive implementations (working)
   ├─ lowlevel.py       ← Iterative equivalents (WIP)
   ├─ c_like.py         ← Stack-simulated recursion (coming soon)
   ├─ tests_drills.py   ← Automated test runner
   └─ README.md         ← This file
```

---

> 💡 Tip:  
> Recursion is not just about elegance — it’s about breaking complex problems into simpler self-similar subproblems.  
> Once mastered, it forms the conceptual foundation for **tree traversal**, **divide-and-conquer**, and **dynamic programming**.
