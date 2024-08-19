from collections import deque

def pad_with_zeros(a, b):
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    diff = len(large) - len(small)
    small = ("0" * diff) + small
    return small, large

def addBinary(a, b):
    a, b = pad_with_zeros(a, b)
    binary_sum = deque()
    i, j, carry = len(a) - 1, len(b) - 1, 0
    while i >= 0:
        _sum = int(a[i]) + int(b[j]) + carry
        carry = 1 if _sum > 1 else 0
        binary_sum.appendleft(str(_sum % 2))
        i, j = i - 1, j - 1
    if carry:
        binary_sum.appendleft("1")
    return "".join(binary_sum)


print(addBinary(a="1", b="1"))  # 10
print(addBinary(a="11", b="1"))  # 100
print(addBinary(a="1010", b="1011"))  # 10101
print(addBinary(a="100", b="110010"))  # 110110
