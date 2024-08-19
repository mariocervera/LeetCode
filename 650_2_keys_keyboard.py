
def highest_prime_factor(n):
    divisor, num, res = 2, n, None
    res = None
    while num > 1:
        if num % divisor == 0:
            res = divisor
            while num % divisor == 0:
                num //= divisor
        divisor += 1
    return res

def minSteps(n):
    if n == 1:
        return 0
    p = highest_prime_factor(n)
    return p + minSteps(n//p)


print(minSteps(1))  # 0
print(minSteps(3))  # 3
print(minSteps(4))  # 4
print(minSteps(5))  # 5
print(minSteps(6))  # 5
print(minSteps(12))  # 7
print(minSteps(16))  # 8
print(minSteps(42))  # 12
