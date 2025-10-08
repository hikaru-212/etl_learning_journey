# Stage 0: The Crucial Mindset Shift
> [Switch to Chinese Version / 跳至中文版](../zh/stage0_mindset.md)
---

When I first began this journey, I was tempted to start big.  
"Why not generate 10 million rows and simulate a large-scale scenario right away?" I thought.  

The result was a frozen laptop that I dreaded opening, and hours wasted on memory and I/O issues that had nothing to do with ETL itself.

This painful experience became my first and most valuable lesson.  
It forced me to finally listen to what the AI had been suggesting all along: **start with the smallest possible MVP.**

---

### Why MVP?
The purpose of an MVP isn't to be production-ready, but to validate the entire pipeline from end to end.  
Scaling too early just adds complexity and obscures the real learning goals.  

The MVP approach guarantees progress—once the fundamentals work, you can focus on scaling and optimization.  

---

### Why generate synthetic data?
To put the MVP idea into practice, I needed data—but I hadn’t yet learned web scraping or APIs.  
So instead of being blocked by data sources, I chose the simpler path: **generate synthetic (fake) data**.  

This allowed me to focus entirely on the **pipeline mechanics**,  
while postponing the challenge of connecting to external systems.

> 📌 **Important Note for the Real World**
>
> In real-world projects, data extraction is rarely as simple as generating a CSV. It often involves complex tasks like web scraping or consuming APIs, which come with their own set of challenges such as rate limits, authentication, and data format inconsistencies.
>
> My choice to use synthetic data was a deliberate learning strategy to isolate the core ETL logic. This allowed me to focus on building a robust pipeline foundation before tackling the complexities of external data sources.
---


### Next Step: From Mindset to Training

After clarifying the mindset of starting small and avoiding premature scaling,  
I decided to invest in a **two-week foundational training plan** before Stage 1.  

This plan covers algorithmic fundamentals, Python/SQL fluency, and validation strategies.  
It ensures that when I start implementation, I’ll be coding with clarity, not guesswork.  

📄 See details here: [00 Foundational Training Plan](../../methodology/en/00_foundational_training_plan.md)
