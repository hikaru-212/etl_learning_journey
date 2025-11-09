# Coming soon: low-level implementation version

# Q1.
def run_P1_fizz_buzz(n: int) -> list[str]:
    out = [""] * n #預先建立固定長度的列表
    for i in range(1, n+1):
        if i % 15 == 0:
            out[i - 1] = "FizzBuzz"
        elif i % 3 == 0:
            out[i - 1] = "Fizz"
        elif i % 5 == 0:
            out[i - 1] = "Buzz"
        else:
            out[i - 1] = str(i)
    return out

# Q2.
def run_P2_stats(nums: list[int]) -> tuple[int, int, int] | None:
    n = len(nums)
    if n == 0:
        return None
    mn = mx = nums[0]
    total = 0
    i = 0
    while i < n:
        val = nums[i]
        if val < mn:
            mn = val
        if val > mx:
            mx = val
        total += val
        i += 1
    return (mx, mn, total)


# Q3.
def run_P3_count_even_odd(nums: list[int]) -> tuple[int, int]:
    n = len(nums)
    odd = 0
    even = 0
    i = 0
    while i < n:
        val = nums[i]
        if val % 2 == 1:
            odd += 1
        else:
            even += 1
        i += 1
    return (odd, even)

#Q4. 
def run_P4_factorial(n: int) -> int | None:
    if n < 0:
        return None
    ans = 1
    i = n 
    while i >= 1:
        ans *= i
        i -= 1
    return ans

#Q5. 
def run_P5_first_greater(nums: list[int], threshold) -> int | None:
    n = len(nums)
    i = 0
    while i < n:
        val = nums[i]
        if val > threshold:
            return val
        i += 1
    return None



REGISTRY ={
    "P1": run_P1_fizz_buzz,
    "P2": run_P2_stats,
    "P3": run_P3_count_even_odd,
    "P4": run_P4_factorial,
    "P5": run_P5_first_greater,
}

if __name__ == "__main__":
    print(run_P1_fizz_buzz(15))
    print(run_P1_fizz_buzz(7))
    print(run_P2_stats([1,3,7,2,6]))
    print(run_P3_count_even_odd([1,2,3,4,5]))
    print(run_P4_factorial(5))
    print(run_P5_first_greater([1,2,3,5,6], 4))