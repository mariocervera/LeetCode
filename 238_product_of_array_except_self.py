

def productExceptSelf(nums):
    n = len(nums)
    suffixes = ([1] * (n-1)) + [nums[n-1], 1]
    for i in range(n-2, -1, -1):
        suffixes[i] = nums[i] * suffixes[i+1]
    res, prefix = [], 1
    for i in range(n):
        res.append(prefix * suffixes[i+1])
        prefix *= nums[i]
    return res

print(productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
