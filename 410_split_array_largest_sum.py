
def is_too_small(arr, k, max_size):
    i, n = 0, len(arr)
    _sum = 0
    while i < n and k > 0:
        _sum += arr[i]
        if _sum > max_size:
            _sum = 0
            k -= 1
        else:
            i += 1
    return k == 0 and i < n


def splitArray(nums, k):
    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if is_too_small(nums, k, mid):
            low = mid + 1
        else:
            high = mid
    return low



print(splitArray(nums=[7, 2, 5, 10, 8], k=2))    # 18
print(splitArray(nums=[1, 2, 3, 4, 5], k=2))     # 9
print(splitArray(nums=[2, 3, 1, 2, 4, 3], k=5))  # 4
