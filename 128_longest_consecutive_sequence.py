
def longestConsecutive(nums):
    if not nums:
        return 0

    max_len = float("-inf")
    ht = set(nums)

    for num in nums:
        if num-1 in ht:
            continue
        i = num+1
        while i in ht:
            i += 1
        max_len = max(max_len, i-num)

    return max_len


print(longestConsecutive([]))  # 0
print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9

