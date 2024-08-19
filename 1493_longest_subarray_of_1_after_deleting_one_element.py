def longestSubarray(nums):
    prev_streak, current_streak = 0, 0
    res = 0
    contains_zero = False
    for i in range(len(nums)):
        if nums[i] == 1:
            current_streak += 1
            continue
        contains_zero = True
        if nums[i-1] == 1:
            res = max(res, prev_streak + current_streak)
        prev_streak = current_streak
        current_streak = 0
    if nums[-1] == 1:
        res = max(res, prev_streak + current_streak)
    return res if contains_zero else res - 1


print(longestSubarray([1, 1, 0, 1]))  # 3
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
print(longestSubarray([0, 1, 1, 1, 0, 0, 1, 1, 0, 1]))  # 3
print(longestSubarray([1, 1, 1]))  # 2
