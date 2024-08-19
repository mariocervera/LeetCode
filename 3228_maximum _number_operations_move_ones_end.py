
def maxOperations(s):
    ones, res = 0, 0
    for i in range(len(s) - 1):
        if s[i] == "1":
            if s[i+1] == "0":
                res += ones + 1
            ones += 1
    return res


print(maxOperations("1001101"))  # 4
print(maxOperations("010010"))  # 3
print(maxOperations("00111"))  # 0
print(maxOperations("00100101"))  # 3
