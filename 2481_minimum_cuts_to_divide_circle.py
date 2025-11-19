
def numberOfCuts(n):
    if n == 1:
        return 0
    if n % 2 != 0:
        return n
    return n // 2


print(numberOfCuts(1))  # 0
print(numberOfCuts(3))  # 3
print(numberOfCuts(4))  # 2
