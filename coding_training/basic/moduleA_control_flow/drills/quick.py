#module A

#Q1.
def run_P1_fizz_buzz(n: int) -> list[str]:
    out = []
    for x in range(1, n+1):
        if x % 15 == 0:
            out.append("FizzBuzz")
        elif x % 3 == 0:
            out.append("Fizz")
        elif x % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(x))
    return out

#Q2.
def run_P2_stats(nums: list[int]) -> tuple[int, int, int] | None:
    if not nums:
        return None
    mn = mx = nums[0]
    total = 0
    for x in nums:
        if x < mn: mn = x
        if x > mx: mx = x
        total += x
    return mn, mx, total   

#Q3.
def run_P3_count_even_odd(nums: list[int]) -> tuple[int, int]:
    even = odd = 0
    for x in nums:
        even += 1 if x % 2 == 0 else 0
        odd += 1 if x % 2 != 0 else 0
    return even, odd 

#Q4.
def run_P4_factorial(n: int) -> int | None:
    if n < 0:
        return None
    ans = 1
    i = 2
    while i <= n:
        ans *= i
        i += 1
    return ans

#Q5.
def run_P5_first_greater(nums: list[int], threshold: int) -> int | None:
    for x in nums:
        if x > threshold:
            return x 
    else:
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