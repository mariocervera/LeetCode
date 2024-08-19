
def max_subarray(nums):
    current_sum, max_sum = 0, float("-inf")
    for num in nums:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray([1]))  # 1
print(max_subarray([5, 4, -1, 7, 8]))  # 23
