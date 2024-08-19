
def get_max_subarray_len(nums, low, high):
    count_neg_nums = 0
    for i in range(low, high):
        if nums[i] < 0:
            count_neg_nums += 1
    if count_neg_nums % 2 == 0:
        return high - low
    i, j = low, high - 1
    while i < j and nums[i] > 0:
        i += 1
    res_1 = j - i
    i = low
    while j > i and nums[j] > 0:
        j -= 1
    res_2 = j - i
    return max(res_1, res_2)


def getMaxLen(nums):
    i, j, n = -2, -1, len(nums)
    res = float("-inf")
    while j < n:
        while i < n and (i <= j or nums[i] == 0):
            i += 1
        if i == n:
            break
        while j < n and (j <= i or nums[j] != 0):
            j += 1
        res = max(res, get_max_subarray_len(nums, i, j))
    return res if res != float("-inf") else 0


print(getMaxLen([0, 0, 0, 0, 0]))  # 0
print(getMaxLen([1, -2, -3, 4]))  # 4
print(getMaxLen([0, 1, -2, -3, -4]))  # 3
print(getMaxLen([-1, -2, -3, 0, 1]))  # 2


# print(get_max_subarray_len([0,0,-1,-2,-3,4,0,0], 2, 5))
# print(getMaxLen([1, 0, 3, 1, 2, 0, 0, 1, 1]))  # (0,1), (2,5), (7,9)
# print(getMaxLen([0, 3, 1, 2, 0, 0, 1, 1, 0, 0]))  # (1,4), (6,8)
