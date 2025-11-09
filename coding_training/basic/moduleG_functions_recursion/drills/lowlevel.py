# Coming soon: low-level implementation version

#Q1.
def run_P1_factorial(n: int) -> int:
    stack = []
    while n >1:
        stack.append(n)
        n -= 1
    result = 1
    while stack:
        result *= stack.pop()
    return result


#Q2.
def run_P2_fib(n: int) -> int:
    #迭代版“手動遞迴”： 每個 frame = (n, state, v1)
    # state 0: 初入，需要先算 F(n-1)
    # state 1: F(n-1)已得，暫存於 v1，接著算 F(n-2)
    # state 2: 二者都得，回傳
    stack = [(n,0,None)] #定義 stack 為一組tuple，
    res = None

    while stack:
        n, state, v1 = stack.pop() #v1 是上一個子問題（F(n-1)）的回傳值， n 為 我要算F(n)
                                   # state 為任務進度（我現在進行到哪個子階段） 
        if n <= 1:                  
            res = n
            continue
        
        if state == 0: #剛進來，要先算第一個子問題 F(n-1) 
            stack.append((n,1,None))
            stack.append((n-1,0,None))
        
        elif state == 1: #第一個子問題完成，準備算第二個 F(n-2)
            stack.append((n,2,res))
            stack.append((n-2,0,None))

        else:            #兩個子問題都完成，合併結果
            res = res + v1
            
    return res
        



#Q3.
def run_P3_reverse_str(s: str) -> str:
    n = len(s)
    if n <=1:
        return s

    stack = [(0,0)]   #每個frame(i, state)代表 我現在在處理第 i 個字元 s[i:] 的反轉問題
    result = ""

    while stack:
        i, state = stack.pop()      # i:表示目前是反轉 s[i:]
                                    # state: 表示這一層做到哪：0 = 還沒處理子問題，1 = 子問題已處理完，要收尾（接自己）
        if i >= n-1:
            result = s[n-1]
            continue      

        if state == 0:
            stack.append((i,1))
            stack.append((i+1,0))

        else:
            result = result + s[i]                            
    return result


#Q4.
def run_P4_recursive_sum(nums: list[int]) -> int:
    n = len(nums)
    stack = [(0,0)]
    res = 0

    if n == 0:
        return 0
    
    while stack:
        i, state = stack.pop()

        if i >=n:
            continue

        if state == 0:
            stack.append((i,1))
            stack.append((i+1,0))

        else:
            res += nums[i]

    return res


#Q5.
def run_P5_traverse_tree(tree: dict[str, list[str]], start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        children = tree.get(node, [])
        for child in reversed(children):
            stack.append(child)

    return visited
    





REGISTRY ={
    "P1": run_P1_factorial,
    "P2": run_P2_fib,
    "P3": run_P3_reverse_str,
    "P4": run_P4_recursive_sum,
    "P5": run_P5_traverse_tree,
}

if __name__ == "__main__":
    print(run_P1_factorial(5))
    print(run_P2_fib(6))
    print(run_P3_reverse_str("hello"))
    print(run_P4_recursive_sum([1,2,3,4,5]))
    tree = {"A": ["B", "C"], "B": ["D"], "C": ["E", "F"]}
    print(run_P5_traverse_tree(tree, "A"))