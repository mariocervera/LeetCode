
def maxWidthRamp(nums):
    arr = list(range(len(nums)))
    arr.sort(key=lambda i: nums[i])
    min_index, res = float("inf"), float("-inf")
    for i in arr:
        min_index = min(min_index, i)
        res = max(res, i-min_index)
    return res



print(maxWidthRamp([6, 0, 8, 2, 1, 5]))  # 4
print(maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))  # 7
