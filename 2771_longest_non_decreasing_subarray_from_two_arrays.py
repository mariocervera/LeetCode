
def maxNonDecreasingLength(nums1, nums2):
    n = len(nums1)
    best_nums1, best_nums2 = 1, 1
    res = 1
    for i in range(1, n):
        new_best_nums1 = max(
            best_nums1 + 1 if nums1[i-1] <= nums1[i] else 1,
            best_nums2 + 1 if nums2[i-1] <= nums1[i] else 1,
        )
        new_best_nums2 = max(
            best_nums1 + 1 if nums1[i-1] <= nums2[i] else 1,
            best_nums2 + 1 if nums2[i-1] <= nums2[i] else 1,
        )
        res = max(res, max(new_best_nums1, new_best_nums2))
        best_nums1, best_nums2 = new_best_nums1, new_best_nums2
    return res


print(maxNonDecreasingLength(nums1=[1], nums2=[1]))  # 1
print(maxNonDecreasingLength(nums1=[2, 3, 1], nums2=[1, 2, 1]))  # 2
print(maxNonDecreasingLength(nums1=[1, 3, 2, 1], nums2=[2, 2, 3, 4]))  # 4
print(maxNonDecreasingLength(nums1=[1, 1], nums2=[2, 2]))  # 2
