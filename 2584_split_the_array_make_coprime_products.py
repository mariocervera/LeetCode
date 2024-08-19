
max_n = 10 ** 6


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    i = 2
    while i*i <= n:
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
        i += 1
    return [num for num in range(n+1) if is_prime[num]]


def factorize(n):
    factors = set()
    for prime in primes:
        while n % prime == 0:
            factors.add(prime)
            n //= prime
        if n == 1:
            return factors
    return {n}


def findValidSplit(nums):
    global primes
    n = len(nums)
    primes = sieve_of_eratosthenes(max_n)
    factor_indexes = {}
    for i in range(n):
        for factor in factorize(nums[i]):
            if factor not in factor_indexes:
                factor_indexes[factor] = [i, i]
            else:
                factor_indexes[factor][1] = i
    arr = [0] * n
    for f, (low, high) in factor_indexes.items():
        arr[low] += f
        arr[high] -= f
    _sum = 0
    for i in range(len(arr) - 1):
        _sum += arr[i]
        if _sum == 0:
            return i
    return -1


print(findValidSplit([4, 7, 8, 15, 3, 5]))  # 2
print(findValidSplit([4, 7, 15, 8, 3, 5]))  # -1
