# Coming soon: low-level implementation version

#Q1. 
def run_P1_reverse_string(s: str) -> str:
    chars = list(s)
    n = len(chars)
    i = 0
    while i < n//2:
        temp = chars[i]
        chars[i] = chars[n-1-i]
        chars[n-1-i] = temp
        i += 1
    return ''.join(chars)

#Q2.
def run_P2_is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
 


#Q3.
def run_P3_char_count(s: str) -> dict[str, int]:
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

#Q4. 
def run_P4_clean_string(s: str) -> str:
    #定義哪些字元算是空白
    whitespace_chars = [' ', '\t', '\n', '\r', '\v', '\f']


    #簡單說就是，先找頭尾，再處理中間
    #手動找到第一個非空白字元位置
    start = 0
    while start < len(s):
        ch = s[start]
        is_space = False
        for w in whitespace_chars:
            if ch == w:
                is_space = True
                break
        if not is_space:
            break
        start += 1

    #手動找到最後一個非空帶字元位置
    end = len(s) - 1
    while end >= 0:
        ch = s[end]
        is_space = False
        for w in whitespace_chars:
            if ch == w:
                is_space = True
                break
        if not is_space:
            break
        end -= 1

    # 收集並轉小寫(A-Z 加32)
    buf = []
    i = start
    while i <= end:
        ch = s[i]
        code = ord(ch)
        if 65 <= code <= 90:
            buf.append(chr(code+32))
        else:
            buf.append(ch)
        i += 1
    return ''.join(buf)

#Q5.
def run_P5_reverse_words(s: str) -> str:
    #Step1. 模擬split() 逐字收集單詞
    words = []
    current = []
    for ch in s:
        if ch == ' ':
            if current:
                words.append(''.join(current))
                current = []
        else:
            current.append(ch)
    if current:
        words.append(''.join(current))

    # Step2. 模擬reversed() (使用雙指標)
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    
    #Step3. 模擬.join()
    #這裡也改用list暫存字元，再一次性''.join()
    buf = []
    for i in range(len(words)):
        buf.append(words[i])
        if i != len(words) - 1:
            buf.append(' ')
    return ''.join(buf)

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