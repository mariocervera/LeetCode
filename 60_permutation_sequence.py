from sortedcontainers import SortedList
from math import factorial

def getPermutation(n, k):
    permutation = [""] * n
    remaining_numbers = SortedList(range(1, n+1))

    def unrank(N, K, i, factorial_n):
        if N == 1:
            permutation[i] = str(remaining_numbers.pop(0))
            return
        fact_n_minus_one = factorial_n // N
        symbol_index = ((K-1) // fact_n_minus_one)
        permutation[i] = str(remaining_numbers.pop(symbol_index))
        unrank(N-1, K % fact_n_minus_one, i+1, fact_n_minus_one)

    unrank(n, k, 0, factorial(n))
    return "".join(permutation)

print(getPermutation(n=4, k=1))  # "1234"
print(getPermutation(n=4, k=6))  # "1432"
print(getPermutation(n=4, k=7))  # "2134"
#print(getPermutation(n=3, k=3))  # "213"
#print(getPermutation(n=4, k=9))  # "2314"
#print(getPermutation(n=3, k=1))  # "123"


