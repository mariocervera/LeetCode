from collections import Counter


def findPairs(nums, k):
    if k == 0:
        return sum([val > 1 for val in Counter(nums).values()])
    res, seen = 0, set()
    for num in nums:
        if num not in seen:
            res += int(num-k in seen) + int(num+k in seen)
        seen.add(num)
    return res


print(findPairs(nums=[3, 1, 4, 1, 5], k=2))  # 2
print(findPairs(nums=[1, 2, 3, 4, 5], k=1))  # 4
print(findPairs(nums=[1, 3, 1, 5, 4], k=0))  # 1
print(findPairs(nums=[1, 1, 1, 1, 1], k=0))  # 1
