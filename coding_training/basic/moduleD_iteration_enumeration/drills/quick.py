#module D

#Q1.
def run_P1_first_negative_index(nums: list[int]) -> int:
    for i, x in enumerate(nums):
        if x < 0:
            return i
    return -1

#Q2. 
def run_P2_pairwise_sum(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x,y in zip(a,b)]

#Q3. #如果給定的list不是偶數會如何？
def run_P3_chunk_pairs(items: list[int]) -> list[tuple[int, int]]:
    out = []
    for i in range(0, len(items), 2):
        if i+1 < len(items):
            out.append((items[i], items[i+1]))
        else:
            out.append(items[i])
    return out

#Q4.
def run_P4_parity_and_sign(nums: list[int]) -> tuple[bool, bool]:
    any_even = any(x % 2 ==0 for x in nums)
    all_positive = all(x > 0 for x in nums)
    return any_even, all_positive

#Q5.
def run_P5_sort_by_len_then_lex(words: list[str]) -> list[str]:
    return sorted(words, key= lambda w: (len(w), w))




REGISTRY ={
    "P1": run_P1_first_negative_index,
    "P2": run_P2_pairwise_sum,
    "P3": run_P3_chunk_pairs,
    "P4": run_P4_parity_and_sign,
    "P5": run_P5_sort_by_len_then_lex
}

if __name__ == "__main__":
    print(run_P1_first_negative_index([3,8,-2,5]))
    print(run_P2_pairwise_sum([1,2,3],[4,5,6]))
    print(run_P3_chunk_pairs([1,2,3,4,5,6]))
    print(run_P4_parity_and_sign([1,3,5]))
    print(run_P4_parity_and_sign([2,3,-1]))
    print(run_P5_sort_by_len_then_lex(["car","a","bat","aa"]))