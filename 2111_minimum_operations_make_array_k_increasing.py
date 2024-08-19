from collections import defaultdict


def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def len_longest_non_decreasing_subsequence(arr):
    subsequence = []
    for num in arr:
        if not subsequence or subsequence[-1] <= num:
            subsequence.append(num)
        else:
            subsequence[binary_search(subsequence, num)] = num
    return len(subsequence)


def kIncreasing(arr, k) -> int:
    d = defaultdict(list)
    for i in range(len(arr)):
        d[i % k].append(arr[i])
    res = 0
    for v in d.values():
        res += (len(v) - len_longest_non_decreasing_subsequence(v))
    return res



print(kIncreasing(arr=[5, 4, 3, 2, 1], k=1))  # 4
print(kIncreasing(arr=[4, 1, 5, 2, 6, 2], k=2))  # 0
print(kIncreasing(arr=[4, 1, 5, 2, 6, 2], k=3))  # 2
print(kIncreasing(arr=[2, 2, 2, 2, 2, 1, 1, 4, 4, 3, 3, 3, 3, 3], k=1))  # 4
print(kIncreasing(arr=[1, 1, 3, 3, 2, 2, 2, 2, 2], k=1))  # 2
