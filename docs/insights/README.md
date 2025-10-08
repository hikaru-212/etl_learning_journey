# 🧭 Engineering Insights

This section documents my personal journey of **engineering growth** — from early mistakes to evolving design philosophies.  
It is organized into three complementary parts:

1. **Core Insights** — key “Aha!” moments that shaped my engineering mindset.  
2. **Curiosity Records** — experiments, questions, and reflections that fueled deeper exploration.  
3. **From ETL to ELT** — the turning point story: from bottlenecks to paradigm shift.

The goal is to make the **thinking process and decision-making visible**, not just the final implementation.

> 🌐 Each document is available in both English and Chinese.  
> 每篇文件皆提供 **英文版** 與 **中文版**。

[← Back to Docs Overview](../README.md)

---

## 📌 Core Insights

- **[00 Risk-Driven Beginnings (EN)](./aha_moment/en/00_risk_driven_beginnings.md)**  
  [中文版](./aha_moment/zh/00_risk_driven_beginnings.md)  
  *The first seed of my engineering philosophy — how a GitHub credential risk led me to discover the principle of least privilege and risk-driven design thinking.*

- **[01 Airflow and Debugging → Core vs Enablers (EN)](./aha_moment/en/01_airflow_and_debugging.md)**  
  [中文版](./aha_moment/zh/01_airflow_and_debugging.md)  
  *Reflections on Airflow and debugging that gave birth to the Core vs Enablers model.*

- **[01B Core vs Enablers Dynamic (EN)](./aha_moment/en/01B_core_vs_enablers_dynamic.md)**  
  [中文版](./aha_moment/zh/01B_core_vs_enablers_dynamic.md)  
  *Extending Core vs Enablers into a dynamic diagnostic toolkit — context-driven by SLA, role, and cost.*

- **[02 Tests are the Safeguard Between Assumption and Reality (EN)](./aha_moment/en/02_tests_vs_validation.md)**  
  [中文版](./aha_moment/zh/02_tests_vs_validation.md)  
  *An analogy between unit tests for code and Pandera for data.*

- **[02B ENUM as Database — Pandera as Validation Layer (EN)](./aha_moment/en/02B_enum_as_db_pandera.md)**  
  [中文版](./aha_moment/zh/02B_enum_as_db_pandera.md)  
  *A cross-layer reflection: understanding how ENUM mirrors Pandera schemas and dbt tests, unifying validation across data and logic.*

- **[03 Function as a Recursive Mental Model (EN)](./aha_moment/en/03_function_as_model.md)**  
  [中文版](./aha_moment/zh/03_function_as_model.md)  
  *Discovering the fractal-like Input–Bridge–Output structure that repeats from a single function up to an entire system.*

- **[04 A Unified Design Philosophy: From Blueprint to Reality (EN)](./aha_moment/en/04_unified_philosophy.md)**  
  [中文版](./aha_moment/zh/04_unified_philosophy.md)  
  *The capstone philosophy: using a static mental model as a dynamic compass to navigate real-world engineering.*

---

## 🔍 Curiosity Records

> A collection of open-ended questions and experiments that push beyond tutorials.  
> Each entry reflects a curiosity loop — asking, testing, and reframing until an *Aha!* emerges.  

Example topics:  
- What happens if stochastic process logic is applied to validation design?  
- Can AI be stress-tested like distributed systems?  
- Where is the practical boundary between Core and Enablers?

👉 Files are located in the [`curiosity/`](./curiosity/) folder.  
(English and Chinese versions available.)

---

## 📖 From ETL to ELT

- **[From Bottleneck to Breakthrough (EN)](./from_ETL_to_ELT.md)**  
  [中文版](./from_ETL_to_ELT_zh.md)  
  *A painful defeat by 10M rows led to rethinking I/O itself, discovering the ELT paradigm, and realizing that true power lies in massively parallel cloud execution.*

---

### 🧩 Summary

Together, these three parts form the **reflection layer** of my project —  
showing *how insights were formed, validated, and integrated* into my overall engineering mindset.
