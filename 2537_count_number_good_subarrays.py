def countGood(nums, k):
    n = len(nums)
    if n == 1:
        return 0
    ht = {}
    res, i, current_number_pairs = 0, 0, 0
    for j in range(n):
        ht[nums[j]] = ht.get(nums[j], 0) + 1
        current_number_pairs += (ht[nums[j]] - 1)
        while i < j and current_number_pairs >= k:
            res += (n-j)
            ht[nums[i]] -= 1
            current_number_pairs -= ht[nums[i]]
            i += 1
    return res


print(countGood([1, 1, 1, 1, 1], 10))  # 1
print(countGood([3, 1, 4, 3, 2, 2, 4], 2))  # 4
print(countGood([2, 1, 3, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 3, 1], 2))  # 21
