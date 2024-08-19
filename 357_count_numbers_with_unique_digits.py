digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1

    res = 0

    def backtrack(i, digits_left, nonzero_digit_used):
        nonlocal res
        if i == n:
            res += 1
            return
        for digit in digits_left:
            if digit != 0:
                backtrack(i + 1, digits_left - {digit}, True)
            else:
                backtrack(i + 1,
                          digits_left - {digit} if nonzero_digit_used else digits_left,
                          nonzero_digit_used)

    backtrack(1, digits, False)
    for d in range(1, 10):
        backtrack(1, digits - {d}, True)

    return res


print(countNumbersWithUniqueDigits(0))  # 1
print(countNumbersWithUniqueDigits(2))  # 91
print(countNumbersWithUniqueDigits(3))  # 739
print(countNumbersWithUniqueDigits(8))  # 2345851
