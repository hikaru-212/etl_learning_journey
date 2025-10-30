#module G

#Q1.
def run_P1_factorial(n: int) -> int:
    if n == 0 or n == 1 :
        return 1
    return n * run_P1_factorial(n-1)

#Q2.
def run_P2_fib(n: int) -> int:
    if n <= 1:
        return n 
    return run_P2_fib(n-1) + run_P2_fib(n-2)


#Q3.
def run_P3_reverse_str(s: str) -> str:
    if len(s) <= 1:
        return s
    return run_P3_reverse_str(s[1:]) + s[0]

#Q4.
def run_P4_recursive_sum(nums: list[int]) -> int:
    if not nums:
        return 0
    return nums[0] + run_P4_recursive_sum(nums[1:])

#Q5.
def run_P5_traverse_tree(tree: dict[str, list[str]], node: str):
    res = [node]
    for child in tree.get(node, []):
        res.extend(run_P5_traverse_tree(tree,child))
    return res
        



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