# module E


#Q1.
def run_P1_even_squares(nums: list[int]) -> list[int]:
    return [x * x for x in nums if x % 2 ==0]




#Q2.
def run_P2_unique_word_lengths(sentence: str) -> set[int]:
    return {len(w) for w in sentence.split()}




#Q3.
def run_P3_char_to_ascii(s: str) -> dict[str, int]:
    return {ch: ord(ch) for ch in s}



#Q4.
def run_P4_flatten_2d(matrix: list[list[int]]) -> list[int]:
    return [x for row in matrix for x in row]




#Q5.
def run_P5_filter_upper_p(words: list[str]) -> list[str]:
    return [w.upper() for w in words if w.startswith('p')]




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