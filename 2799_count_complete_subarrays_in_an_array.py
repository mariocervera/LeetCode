
def countCompleteSubarrays(nums):
    n = len(nums)
    total_distinct = len(set(nums))
    res = 0
    for i in range(n):
        current_distinct = set()
        for j in range(i, n):
            current_distinct.add(nums[j])
            if len(current_distinct) == total_distinct:
                res += 1
    return res


print(countCompleteSubarrays([1, 3, 1, 2, 2]))  # 4
print(countCompleteSubarrays([5, 5, 5, 5]))  # 10
print(countCompleteSubarrays([1, 1, 2, 2, 3, 4, 5, 6, 2]))  # 4
