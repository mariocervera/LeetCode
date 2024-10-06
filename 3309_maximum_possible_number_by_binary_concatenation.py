import functools


def compare(a, b):
    if a == b:
        return 0
    return -1 if a + b > b + a else 1


def maxGoodNumber(nums):
    nums = [bin(num)[2:] for num in nums]
    nums.sort(key=functools.cmp_to_key(compare))
    return int("".join(nums), 2)


print(maxGoodNumber([1, 2, 3]))    # 30
print(maxGoodNumber([1, 11, 5]))   # 221
print(maxGoodNumber([2, 8, 16]))   # 1296
print(maxGoodNumber([2, 67, 25]))  # 13123
