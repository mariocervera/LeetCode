
def longest_increasing_subarray(arr):
    res, streak = 1, 1
    for i in range(1, len(arr)):
        streak = (streak + 1) if arr[i-1] < arr[i] else 1
        res = max(res, streak)
    return res


def longestMonotonicSubarray(nums):
    return max(longest_increasing_subarray(nums), longest_increasing_subarray(nums[::-1]))


print(longestMonotonicSubarray([1]))  # 1
print(longestMonotonicSubarray([3, 3, 3, 3]))  # 1
print(longestMonotonicSubarray([1, 4, 3, 3, 2]))  # 2
print(longestMonotonicSubarray([3, 2, 1]))  # 3
