def maxAbsoluteSum(nums):
    positive_current_sum, negative_current_sum, max_sum, min_sum = 0, 0, float("-inf"), float("inf")
    for i in range(len(nums)):
        positive_current_sum = max(positive_current_sum + nums[i], nums[i])
        negative_current_sum = min(negative_current_sum + nums[i], nums[i])
        max_sum = max(max_sum, positive_current_sum)
        min_sum = min(min_sum, negative_current_sum)
    return max(abs(max_sum), abs(min_sum))


print(maxAbsoluteSum([1, -3, 2, 3, -4]))  # 5
print(maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # 8
print(maxAbsoluteSum([-7, -1, 0, -2, 1, 3, 8, -2, -6, -1,
                      -10, -6, -6, 8, -4, -9, -4, 1, 4, -9]))  # 44
