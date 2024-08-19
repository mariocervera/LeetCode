
def longestSquareStreak(nums):
    nums.sort()
    ht = set(nums)
    res = 0
    for i in range(len(nums)):
        num = nums[i]
        if num in ht:
            ht.remove(num)
            count = 1
            num **= 2
            while num in ht:
                ht.remove(num)
                count += 1
                num **= 2
            if count > 1:
                res = max(res, count)
    return res if res > 0 else -1


print(longestSquareStreak([4, 3, 6, 16, 8, 2]))  # 3
print(longestSquareStreak([2, 3, 5, 6, 7]))  # -1

# [2, 3, 4, 6, 8, 16]
