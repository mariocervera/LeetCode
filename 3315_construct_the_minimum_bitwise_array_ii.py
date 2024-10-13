
def find_rightmost_zero(n):
    i = 0
    while n > 0:
        if n % 2 == 0:
            return i
        n >>= 1
        i += 1
    return i


def clear_bit_at(n, index):
    return n & ~(1 << index)


def minBitwiseArray(nums):
    res = []
    for num in nums:
        if num % 2 == 0:
            res.append(-1)
            continue
        i = find_rightmost_zero(num)
        res.append(clear_bit_at(num, i-1))
    return res


print(minBitwiseArray([2, 3, 5, 7]))  # [-1,1,4,3]
print(minBitwiseArray([11, 13, 31]))  # [9,12,15]
print(minBitwiseArray([6, 23]))  # [-1,19]
