# 🧭 Curiosity & Engineering Insights  
> [Switch to Chinese Version / 跳至中文版](../zh/curiosity_and_insights_zh.md)
---

My work and learning are not just about writing code or doing mathematical derivations.
I see myself more like a detective driven by curiosity, constantly searching for common patterns across different domains. This record captures how I transform a simple “why” into insights in both engineering and mathematics.

It contains two levels of thinking:  
1. **Curiosity Logs** → Pure exploration, cross-disciplinary analogies, and experimental designs.  
2. **Engineering Insights** → Building on curiosity to form more rigorous engineering/mathematical understanding.  

---

## Part I. Curiosity Logs  

### Topic: Zero-One Law & Atomic Writes(2025-09-17)
This record is a curiosity-driven exploration rather than a core project feature. It aims to explore a way of thinking, not to provide a flawless final answer.

**“Can the concept of the Zero-One Law be compared to Atomic Writes in engineering?  
Would AI itself agree with such an analogy?”**  

#### Background  
In both research and engineering, I often try to map mathematical intuition to technical concepts.  
This time, I wanted to test whether the Zero-One Law — the idea that an event either happens or does not happen —  
could be viewed as analogous to the **all-or-nothing** nature of atomic writes.  

#### My Curiosity  
1. If we treat “an event must either occur or not occur” as a Zero-One Law,  
   could atomic writes be seen as the engineering equivalent?  
2. How would different AIs respond to this analogy?  
   - Would they agree with this cross-disciplinary comparison?  
   - Or would they push back with counterarguments?  

#### Results After Asking AI  
- **AI #1 and AI #2** agreed with the analogy.  
- **AI #3** disagreed, confusing convergence with certainty.  
- After correction, AI #3 acknowledged the mistake.  
- My question: Since even AI can make mistakes, how can I systematically verify its reliability?
This question guided my curiosity from cross-domain analogies toward repeatable, quantifiable AI experiment design.

---

## Theoretical Experiments & Engineering Considerations 
Here are three experimental designs I formulated to test the boundaries of AI behavior:

> **Experiment 1: The Repetition Test (Consistency)**
> - **Method:** Ask the same precise question (e.g., Zero-One Law vs Atomic Writes) 100 or 1000 times.
> - **Metric:** Measure the probability of the AI giving the correct answer.
> - **Goal:** Quantify the reliability and stability of the AI's reasoning on a known problem.

> **Experiment 2: The Open-Ended Question Test (Distribution of Belief)**
> - **Method:** Ask about an unsolved problem, such as the Riemann Hypothesis, hundreds of times.
> - **Metric:** Analyze the distribution of answers (Agree / Disagree / Admit “Unknown”).
> - **Goal:** Understand how the AI handles ambiguity and problems without a ground truth.

> **Experiment 3: The AI Debate Test (Convergence & Self-Correction)**
> - **Method:** Pit two AIs against each other on an unsolved problem, feeding each one the other's reasoning in a loop.
> - **Metric:** Observe if and how their stances change over iterations.
> - **Goal:** Explore whether AI systems can converge towards a consensus or self-correct through dialectic reasoning.

   Since humans themselves have no final answer in such debates, what would emerge from letting AIs debate the undecidable?
   *Note:* I designed these experiments, but couldn't implement them due to practical cost considerations.

---

## Experiment Design: Cost & Implementation (AI1 provided)

> **Note:** To ensure objectivity, AI systems in this record are presented only with code names (AI 1, AI 2, etc.), focusing on their behavior rather than any specific brand.  

When testing repeated prompts (e.g., 100 or 1000 times), cost is an important factor.  
It’s **not simply “one fixed fee per question”** — instead, billing depends on **token usage**:  

1. **Billing Model**  
   - Each request consumes tokens:  
     - **Input tokens** (prompt + system messages)  
     - **Output tokens** (the reply)  
   - The cost = (input tokens × rate) + (output tokens × rate).  
   - Repeating the *same* question still generates a new request, which uses tokens again.  
   - Therefore, running 1000 queries ≈ 1000 × (average token usage) in cost.  

   > ⚠️ Important: It’s not a “per-question fee,” but a **per-token fee**.  
   > Even identical prompts are billed separately because each request consumes tokens anew.  

2. **Implementation (template idea from AI 1)**  
   - Use a loop to send the same prompt repeatedly.  
   - Collect responses, then analyze the answer distribution.  
   - To control cost, limit output length and keep prompts concise.  

### Example (Python)
> **Note：** The AI1 class is used here as an abstract placeholder. Its behavior is designed to simulate a general large language model API, with the goal of focusing the discussion on model behavior itself, rather than a specific brand or service.
```python
from AI1 import AI1
import collections

client = AI1()

prompt = "Explain the Zero-One Law in probability theory."
results = []

# Run the same prompt 100 times
for i in range(100):
    response = client.chat.completions.create(
        model="(placeholder)",   # simplified, no specific model mentioned
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,          # limit output length
        temperature=0            # reduce randomness
    )
    answer = response.choices[0].message.content.strip()
    results.append(answer)

# Simple analysis: count unique answers
counter = collections.Counter(results)
for ans, count in counter.items():
    print(f"{count} times: {ans[:80]}...")
```

---

### Multi-AI Feedback Cycle  
- After getting the initial template from **AI 1**, I passed it to **AI 2** for review.  
- **AI 2** highlighted some refinements (e.g., phrasing of cost, clarity on parameters).  
- I then fed **AI 2**’s comments back to **AI 1**, asking it to self-reflect.  

### Outcome  
- **AI 1** acknowledged some of **AI 2**’s points and clarified its own intent.  
- The back-and-forth showed how two AI systems can cross-check and refine each other’s answers.  
- For me, this became less about the “perfect code,” and more about observing how AI reasoning **diverges, converges, or self-corrects when challenged**.  
- The purpose of these experiments is not only to verify AI’s accuracy, but also to explore the boundaries of its behavior patterns—and to transform these unpredictable behaviors into analyzable data.

👉 It documents not just AI outputs, but how I **learn, verify, and reflect** through them.  

---

## Part II. Engineering Insights: Core vs. Enablers  

### My Curiosity Log: A Mathematical Analogy Behind AI Mistakes 

This log details my personal thought process, attempting to use limited knowledge to create analogies for complex technology. Through this process, I hope to not only clarify my own doubts but also demonstrate a learning path from intuition to rigorous understanding.

**Goal**: To explore the mechanisms behind AI behavior, instead of treating it as a black-box tool.  

---

### The Thought Process Behind an AI's Mistake

Initially, I intuitively thought that AI's operation might be like a simple transition matrix. But this idea was quickly debunked because the AI clearly remembers our conversation.

So, I revised my guess, thinking it was more like a transition operator with memory. I then analogized a wrong answer in a single turn as the "transition process going wrong and getting trapped in an absorbing state."

But this led to a new question: Why does the AI have a chance to correct its mistake in the next turn based on my explanation? I realized it's not because it "escaped" the absorbing state, but because in the new turn, it builds a whole new transition matrix with corrected memory based on the new context.

This process made me realize that the mechanism between turns is key to understanding AI's behavior.

---

### My Intuitive Understanding (Simplified)
- AI’s responses feel like random  choices.  
- It “remembers” context, like a transition matrix with memory.  
- The implication of a wrong answer in a single turn feels like entering an absorbing state. 

---

### A More Rigorous Technical Understanding 

| Aspect | My Intuitive Understanding (Simplified) | A More Precise Technical Understanding |
|--------|-------------------------------|--------------------------------|
| **Representation** |The AI's response in each turn is like a new transition matrix, inheriting memory from previous turns. | It's an expanding, conditional large-scale stochastic process, primarily driven by an autoregressive model based on the Transformer architecture. The model takes the entire conversation history as input and dynamically adjusts its internal state through Attention Mechanism. |
| **Absorbing State** | A wrong answer in a single turn feels like getting trapped in an absorbing state.| It's a high-probability "local trap." This is not a mathematical "absorbing state," but rather a situation where the probability peak of the wrong answer is higher than the correct one under the current context. By providing new input (e.g., your correction), the probability distribution is reshaped, increasing the likelihood of the correct answer. |
| **Between Turns** | Each conversation turn is like a new transition matrix that inherits previous memory. |Each turn is a new conditional computation. The model takes all the information you've provided as input, dynamically adjusts its internal parameters, and generates a result based on the new information. |


---

### Conclusion  
- The value of this log lies in its demonstration of a process from intuitive analogy to engineering insight.
- Although my initial guesses used terms like transition matrix and absorbing state, which are not entirely precise, they successfully captured the core characteristics of AI behavior: stochasticity and contextual dependence.  
- This process also reveals an important learning method: Even if a guess isn't entirely correct, as long as it leads to deeper inquiry and revision, it is meaningful. This is an effective way to concretize abstract concepts in an unfamiliar field. 
- I learned that understanding a new concept doesn’t have to be perfect at the start. Beginning from an imperfect intuition, through critical reflection and learning, one can eventually build a more precise and rigorous knowledge system.

---

## 📌 Overall Reflection  
This record shows my path from **curiosity** to **engineering insights**:  
1. Making cross-disciplinary analogies (Math ↔ Engineering).
2. Verifying AI's correctness and behavioral patterns.
3. Translating intuition into technical language.  
4. Finally, solidifying into a personal learning method and engineering insight.


### 📌 Insight: The Gap Between Theory and Reality
While I designed a rigorous experiment to verify AI's behavior, the real-world "cost" became a major obstacle. This made me realize that in the real world, pure academic curiosity must be balanced against practical engineering considerations such as budget and resources. This reinforced my belief in Core vs Enablers: in resource-limited situations, priority must go to the elements that solve core problems. This log embodies a crucial engineering mindset: starting with an intuitive phenomenon, using existing knowledge to form a hypothesis, and then, through continuous questioning and verification, ultimately reaching a more rigorous and practical understanding.

---


