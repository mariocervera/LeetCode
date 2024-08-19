
def trailingZeroes(n):
    counter, divisor = 0, 5
    while divisor <= n:
        counter += n//divisor
        divisor *= 5
    return counter


print(trailingZeroes(0))  # 0
print(trailingZeroes(3))  # 0
print(trailingZeroes(5))  # 1
print(trailingZeroes(10))  # 2
print(trailingZeroes(14))  # 2
print(trailingZeroes(15))  # 3
print(trailingZeroes(18))  # 3
print(trailingZeroes(20))  # 4
print(trailingZeroes(30))  # 7

