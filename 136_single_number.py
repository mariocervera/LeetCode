from functools import reduce

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    #return reduce(lambda x, y: x ^ y, nums)


print(singleNumber([2, 2, 1]))  # 1
print(singleNumber([4, 1, 2, 1, 2]))  # 4
print(singleNumber([1]))  # 1
