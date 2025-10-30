#module C

#Q1.
def run_P1_reverse_string(s: str) -> str:
    return s[::-1]

#Q2. 
def run_P2_is_palindrome(s: str) -> bool:
    return s == s[::-1]

#Q3. 
def run_P3_char_count(s: str) -> dict[str, int]:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

#Q4.
def run_P4_clean_string(s: str) -> str:
    return s.strip().lower()

#Q5.
def run_P5_reverse_words(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))




REGISTRY ={
    "P1": run_P1_reverse_string,
    "P2": run_P2_is_palindrome,
    "P3": run_P3_char_count,
    "P4": run_P4_clean_string,
    "P5": run_P5_reverse_words,
}

if __name__ == "__main__":
    print(run_P1_reverse_string("hello"))
    print(run_P2_is_palindrome("racecar"))
    print(run_P2_is_palindrome("hello"))
    print(run_P3_char_count("banana"))
    print(run_P4_clean_string("   HelLo  "))
    print(run_P5_reverse_words("the sky is blue"))