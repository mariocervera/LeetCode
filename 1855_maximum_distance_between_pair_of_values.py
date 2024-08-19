
def maxDistance(nums1, nums2):
    max_distance = 0
    i, j, m, n = 0, 0, len(nums1), len(nums2)
    while i < m and j < n:
        while j < n and nums1[i] <= nums2[j]:
            max_distance = max(max_distance, j-i)
            j += 1
        i += 1
    return max_distance


print(maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))  # 2
print(maxDistance([2, 2, 2], [10, 10, 1]))  # 1
print(maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))  # 2
