def maxNumOfMarkedIndices(nums):
    n = len(nums)
    i, j = 0, n // 2 + 1 if n % 2 != 0 else n // 2
    nums.sort()
    while j < n:
        while j < n and nums[i] * 2 > nums[j]:
            j += 1
        if j < n:
            i += 1
            j += 1
    return i * 2


print(maxNumOfMarkedIndices([3, 5, 2, 4]))  # 2
print(maxNumOfMarkedIndices([9, 2, 5, 4]))  # 4
print(maxNumOfMarkedIndices([7, 6, 8]))  # 0
print(maxNumOfMarkedIndices([57, 40, 57, 51, 90, 51, 68, 100, 24, 39, 11, 85, 2, 22, 67,
                             29, 74, 82, 10, 96, 14, 35, 25, 76, 26, 54, 29, 44, 63,
                             49, 73, 50, 95, 89, 43, 62, 24, 88, 88, 36, 6, 16, 14, 2,
                             42, 42, 60, 25, 4, 58, 23, 22, 27, 26, 3, 79, 64, 20, 92]))  # 58
