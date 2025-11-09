# Coming soon: low-level implementation version

#Q1.
def run_P1_remove_val(nums: list[int], val) -> list[int]:
    n = len(nums)
    out = [0] * n
    i = j = 0
    while i < n:
        if nums[i] != val:
            out[j] = nums[i]
            j += 1
        i += 1
    return out[:j]

#Q2.
def run_P2_reverse_list(nums: list[int]) -> list[int]:
    n = len(nums)
    i = 0
    while i < n//2:
        j = n-1-i
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1
    return nums

#Q3.
def run_P3_word_count(s: str) -> dict[str, int]:
    #Step1. 手動分割字串
    words = []
    word = "" 
    for ch in s:
        if ch == " ":
            if word != "":
                words.append(word)
                word = ""
        else:
            word += ch
    if word != "":
        words.append(word)

    # Step2.: 手動統計頻率
    freq = {}
    for w in words:
        if w in freq.keys():
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1
    return freq

#Q4.
def run_P4_invert_dict(d: dict[str, int]) -> dict[int, str]:
    inv = {}
    for k in d.keys():
        v = d[k]    # 從原字典拿出 key 對應的 value
        inv[v] = k  # 倒過來：以 value 當 key，以 key 當 value
    return inv

# Q5.
def run_P5_merge_dicts(d1: dict, d2: dict) -> dict:
    merged = {}
    for k in d1.keys():
        merged[k] = d1[k]
    for k in d2.keys():
        merged[k] = d2[k]
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