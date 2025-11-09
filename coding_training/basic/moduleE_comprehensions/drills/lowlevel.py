# Coming soon: low-level implementation version

#Q1.
def run_P1_even_squares(nums: list[int]) -> list[int]:
    out = []
    for i in nums:
        if i % 2 == 0:
            out.append(i**2)
    return out


#Q2.
def run_P2_unique_word_lengths(sentence: str) -> set[int]:
    lengths = set()
    current = ""
    #上半段是邊走邊拼字、遇空白就記錄長度
    for ch in sentence:
        if ch == " ":
            if current != "":
                lengths.add(len(current))
                current = ""
        else:
            current += ch
    #下半段是句尾補上最後那個還沒遇空白的字
    if current != "":
        lengths.add(len(current))
    return lengths


#Q3.
def run_P3_char_to_ascii(s: str) -> dict[str, int]:
    result = {}
    for ch in s:
        result[ch] = ord(ch)
    return result

#Q4.
def run_P4_flatten_2d(matrix: list[list[int]]) -> list[int]:
    total_len = sum(len(row) for row in matrix)
    result = [None] * total_len
    k = 0
    for row in matrix:
        for x in row:
            result[k] = x
            k += 1
    return result


#Q5.
def run_P5_filter_upper_p(words: list[str]) -> list[str]:
    result = []
    i = 0
    while i < len(words):
        w = words[i]
        if len(w) > 0 and w[0] == 'p':
            upper_w = ""
            for ch in w:
                code = ord(ch)
                if 97 <= code <= 122:
                    upper_w += chr(code-32)
                else:
                    upper_w += ch
            result.append(upper_w)
        i += 1
    return result

    




REGISTRY ={
    "P1": run_P1_even_squares,
    "P2": run_P2_unique_word_lengths,
    "P3": run_P3_char_to_ascii,
    "P4": run_P4_flatten_2d,
    "P5": run_P5_filter_upper_p,
}

if __name__ == "__main__":
    print(run_P1_even_squares([1,2,3,4,5]))
    print(run_P2_unique_word_lengths("I love Python very much"))
    print(run_P3_char_to_ascii("abc"))
    print(run_P4_flatten_2d([[1,2],[3,4],[5]]))
    print(run_P5_filter_upper_p(["python", "java", "php", "c++"]))