def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        digits[i] = (digits[i] + 1) % 10
        if digits[i] != 0:
            return digits
    digits.insert(0, 1)
    return digits

print(plusOne([1, 2, 3]))  # [1,2,4]
print(plusOne([4, 3, 2, 1]))  # [4,3,2,2]
print(plusOne([9]))  # [1,0]
print(plusOne([1,9]))  # [2,0]
print(plusOne([9,9]))  # [1,0,0]
