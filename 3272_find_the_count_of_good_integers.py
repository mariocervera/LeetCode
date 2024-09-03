from math import factorial
from collections import Counter


def num_distinct_permutations_n_digits(n, digit_counts):
    numerator = factorial(n)
    denominator = 1
    for count in digit_counts.values():
        denominator *= factorial(count)
    return numerator // denominator


def num_distinct_permutations_without_leading_zero(digits):
    n, counters = len(digits), Counter(digits)
    total_permutations = num_distinct_permutations_n_digits(n, counters)
    if counters['0'] == 0:
        return total_permutations
    counters['0'] -= 1
    permutations_with_leading_zero = num_distinct_permutations_n_digits(n - 1, counters)
    return total_permutations - permutations_with_leading_zero


def countGoodIntegers(n, k):
    half_length = (n + 1) // 2

    start = 10 ** (half_length - 1) if n > 1 else 0
    end = 10 ** half_length

    palindromes = set()
    for i in range(start, end):
        half_str = str(i)
        if n % 2 == 0:
            full_palindrome = half_str + half_str[::-1]
        else:
            full_palindrome = half_str + half_str[-2::-1]
        if int(full_palindrome) % k == 0:
            palindromes.add(tuple(sorted(full_palindrome)))
    res = 0
    for palindrome in palindromes:
        res += num_distinct_permutations_without_leading_zero(palindrome)
    return res


print(countGoodIntegers(n=3, k=5))  # 27
print(countGoodIntegers(n=1, k=4))  # 2
print(countGoodIntegers(n=5, k=6))  # 2468
print(countGoodIntegers(n=10, k=6))  # 13249798
