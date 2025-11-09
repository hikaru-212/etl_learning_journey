# Coming soon: low-level implementation version

#Q1. 
def run_P1_first_negative_index(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            return i
        i += 1
    return -1

#Q2.
def run_P2_pairwise_sum(a: list[int], b: list[int]) -> list[int]:
    result = []
    i = 0
    n = len(a)
    m = len(b)
    limit = n if n < m else m

    while i < limit:
        result.append(a[i]+b[i])
        i += 1
    return result


#Q3.
def run_P3_chunk_pairs(items: list[int]) -> list[tuple[int, int]]:
    n = len(items)
    pair_count = n // 2
    out = [None] * pair_count # 預先分配空間
    i = 0
    j = 0
    while i + 1 < n:
        a = items[i]
        b = items[i+1]
        out[j] = (a,b)
        i += 2
        j +=1
    return out 

#Q4.
def run_P4_parity_and_sign(nums: list[int]) -> tuple[bool, bool]:
    #手動判斷是否有任何偶數
    any_even = False
    for x in nums:
        if x % 2 == 0:
            any_even = True
            break

    #手動判斷是否全部正數
    all_positive = True
    for x in nums:
        if x <= 0:
            all_positive = False
            break
    return (any_even, all_positive)

def run_P5_sort_by_len_then_lex(words: list[int]) -> list[int]:
    n = len(words)
    out = words[:] 

    i = 0
    while i < n-1:
        j = i+1
        while j < n:
            w1 = out[i]
            w2 = out[j]

            #先比長度
            len1 = len(w1)
            len2 = len(w2)

            should_swap = False
            if len1 > len2:
                should_swap = True
            elif len1 == len2 and w1 > w2:
                should_swap = True

            if should_swap:
                temp = out[i]
                out[i] = out[j]
                out[j] = temp

            j += 1

        i += 1
    return out




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