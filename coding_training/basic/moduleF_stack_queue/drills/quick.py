#module F 
from collections import deque
from collections import Counter
import heapq

#Q1.
def run_P1_stack_simulation(ops: list[str]) -> list[int]:
    stack = []
    for op in ops:
        if op.isdigit():
            stack.append(int(op))
        elif op == "pop" and stack:
            stack.pop()
    return stack


#Q2.
def run_P2_queue_simulation(ops: list[str]) -> list[int]:
    q = deque()
    for op in ops:
        if op.isdigit():
            q.append(int(op))
        elif op == "deq" and q:
            q.popleft()
    return list(q)


#Q3.
def run_P3_balanced_parentheses(s: str) -> bool:
    stack = []
    mapping = {')':'(', ']':'[','}':'{'}
    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return not stack


#Q4.
def run_P4_word_counter(sentence: str) -> dict[str, int]:
    words = sentence.lower().split()
    return dict(Counter(words))


#Q5.
def run_P5_topk_frequent(nums: list[int], k:int) -> list[int]:
    freq = Counter(nums)
    return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda kv: kv[1])]


REGISTRY ={
    "P1": run_P1_stack_simulation,
    "P2": run_P2_queue_simulation,
    "P3": run_P3_balanced_parentheses,
    "P4": run_P4_word_counter,
    "P5": run_P5_topk_frequent,
}

if __name__ == "__main__":
    print(run_P1_stack_simulation(["1","2","3","pop","4"]))
    print(run_P2_queue_simulation(["1","2","3","deq","4"]))
    print(run_P3_balanced_parentheses("({[]})"))
    print(run_P3_balanced_parentheses("([)]"))
    print(run_P4_word_counter("apple banana apple orange banana apple"))
    print(run_P5_topk_frequent([1,1,1,2,2,3],2))