# Coming soon: low-level implementation version

#Q1.
def run_P1_stack_simulation(ops: list[str]) -> list[int]:
    stack = [None] * len(ops)
    top = -1 #指標位置
    
    for op in ops:
        if len(op) == 1 and '0'<= op <='9':
            top += 1
            stack[top] = ord(op) - ord('0')
        elif op == "pop" and top >= 0:
            top -= 1

    return stack[:top+1] #不是回傳stack 是因為stack可能有空值

#Q2.
def run_P2_queue_simulation(ops: list[str]) -> list[int]:
    q = []
    for op in ops:
        #模擬 isdigit() 且限制在數字 0~9之間
        is_number = True
        for ch in op:
            if ch <'0' or ch >'9':
                is_number = False
                break
        #模擬 數字轉整數
        if is_number:
            num = 0
            for ch in op:
                num = num*10 + (ord(ch) - ord('0'))
            #手動模擬append
            q = q + [num]
        # deq 操作
        elif op == "deq" and len(q) > 0:
            q = q[1:]

    return q 

#Q3.
def run_P3_balanced_parentheses(s: str) -> bool:
    #定義列表
    mapping = {')':'(', ']':'[', '}':'{'}
    stack = []





#Q4. 
def run_P4_word_counter(sentence: str) -> dict[str, int]:
    words = sentence.lower().split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq


#Q5.
import heapq
def run_P5_topk_frequent(nums: list[int], k: int):
    #手動計算次數
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # 建立最小堆(min-heap) 用來保留目前最大的k個元素
    heap = [] # 元素格式為(count, num)
    
    for num, count in freq.items():
        heapq.heappush(heap, (count,num)) #推入元素
        if len(heap) > k:                 #若超過k個，移除最小的
            heapq.heappop(heap)

    #取出結果（反轉排序）
    result = [num for (count, num) in sorted(heap, reverse=True)]
    return result
            






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