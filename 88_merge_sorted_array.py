def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 or j >= 0:
        if i < 0:
            nums1[k] = nums2[j]
            j -= 1
        elif j < 0 or nums2[j] < nums1[i]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1



x = [1, 2, 3, 0, 0, 0]
merge(x, 3, [2, 5, 6], 3)
print(x)
