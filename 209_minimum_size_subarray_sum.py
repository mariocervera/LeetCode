
def minSubArrayLen(target, nums):
    i, j, n, min_size, _sum = 0, 0, len(nums), float("inf"), nums[0]
    while i <= j < n and min_size > 1:
        if _sum >= target:
            min_size = min(min_size, j-i+1)
            _sum -= nums[i]
            i += 1
        else:
            j += 1
            if j < n:
                _sum += nums[j]
    return min_size if min_size != float("inf") else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(minSubArrayLen(4, [1, 4, 4]))  # 1
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
print(minSubArrayLen(3, [1, 1, 1, 1, 1]))  # 3
print(minSubArrayLen(7, [1, 2, 1, 1, 2]))  # 5
