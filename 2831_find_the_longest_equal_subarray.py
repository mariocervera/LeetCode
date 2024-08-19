from collections import defaultdict

def longestEqualSubarray(nums, k):
    d = defaultdict(list)
    for i in range(len(nums)):
        d[nums[i]].append(i)
    res = float("-inf")
    for indexes in d.values():
        i, j, n = 0, 1, len(indexes)
        budget = k
        while j < n:
            while j < n and (indexes[j]-indexes[j-1]-1) <= budget:
                budget -= indexes[j]-indexes[j-1]-1
                j += 1
            res = max(res, j-i)
            while j < n and (indexes[j]-indexes[j-1]-1) > budget:
                i += 1
                budget += (indexes[i] - indexes[i-1] - 1)
        res = max(res, j - i)
    return res


print(longestEqualSubarray(nums=[1, 3, 2, 3, 1, 3], k=3))  # 3
print(longestEqualSubarray(nums=[1, 1, 2, 2, 1, 1], k=2))  # 4
print(longestEqualSubarray(nums=[1], k=0))  # 1
print(longestEqualSubarray(nums=[1, 2, 1], k=0))  # 1
print(longestEqualSubarray(nums=[4,4,2,2,4], k=1))  # 2

