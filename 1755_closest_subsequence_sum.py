
# Meet-in-the-middle algorithm

def get_subsets_sums(nums):
    n, sums = len(nums), []
    for i in range(2 ** n):
        _sum = 0
        j = 0
        while i > 0:
            if i & 1:
                _sum += nums[j]
            i >>= 1
            j += 1
        sums.append(_sum)
    return sums


def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid
    if low > 0 and abs(arr[low-1] - target) < abs(arr[low] - target):
        return low-1
    return low

def minAbsDifference(nums, goal):
    n = len(nums)
    sums_low = get_subsets_sums(nums[:n//2])
    sums_high = get_subsets_sums(nums[n // 2:])
    sums_high.sort()
    res = float("inf")
    for s in sums_low:
        target = goal - s
        index = binary_search(sums_high, target)
        res = min(res, abs((s + sums_high[index]) - goal))
    return res


print(minAbsDifference(nums=[5, -7, 3, 5], goal=6))  # 0
print(minAbsDifference(nums=[7, -9, 15, -2], goal=-5))  # 1
print(minAbsDifference(nums=[1, 2, 3], goal=-7))  # 7
