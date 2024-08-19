
def reductionOperations(nums):
    n = len(nums)
    if n == 1:
        return 0
    nums.sort()
    ops = 0
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            ops += (n-i-1)
    return ops




print(reductionOperations([5, 1, 3]))  # 3
print(reductionOperations([1, 1, 1]))  # 0
print(reductionOperations([1, 1, 2, 2, 3]))  # 4
