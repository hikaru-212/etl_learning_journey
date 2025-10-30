#module B

#Q1.
def run_P1_remove_val(nums: list[int], val: int) -> list[int]:
    out = []
    for i in nums:
        if i != val:
            out.append(i)
    return out

#Q2.
def run_P2_reverse_list(nums: list[int]) -> list[int]:
    nums.reverse()
    return nums

#Q3. 
def run_P3_word_count(s: str) -> dict[str, int]:
    words = s.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

#Q4.
def run_P4_invert_dict(d: dict[str, int]) -> dict[int, str]:
    inv = {}
    for k, v in d.items():
        inv[v] = k
    return inv

#Q5.
def run_P5_merge_dicts(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    merged.update(d2)
    return merged




REGISTRY ={
    "P1": run_P1_remove_val,
    "P2": run_P2_reverse_list,
    "P3": run_P3_word_count,
    "P4": run_P4_invert_dict,
    "P5": run_P5_merge_dicts,
}

if __name__ == "__main__":
    print(run_P1_remove_val([3,2,2,3,4,3], 3))
    print(run_P2_reverse_list([1,2,3,4,5]))
    print(run_P3_word_count("apple banana apple orange banana apple"))
    print(run_P4_invert_dict({"a": 1, "b": 2, "c": 3}))
    print(run_P5_merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))