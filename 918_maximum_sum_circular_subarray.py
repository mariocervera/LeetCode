def maxSubarraySumCircular(nums):
    current_max, max_sum, current_min, min_sum, total = 0, float("-inf"), 0, float("inf"), 0
    for num in nums:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)
        total += num
    return max(max_sum, total-min_sum) if max_sum > 0 else max_sum


print(maxSubarraySumCircular([1, -2, 3, -2]))  # 3
print(maxSubarraySumCircular([5, -3, 5]))  # 10
print(maxSubarraySumCircular([-3, -2, -3]))  # -2


# print(maxSubarraySumCircular([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
# print(maxSubarraySumCircular([5, 4, -1, 7, 8]))  # 23






