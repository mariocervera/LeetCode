def get_array_without_zeros(nums):
    res, count = [], 0
    for num in nums:
        if num != 0:
            res.append(num)
        else:
            count += 1
    return res, count


def findTargetSumWays(nums, target):
    nums, zeros_count = get_array_without_zeros(nums)
    n = len(nums)
    if not n:
        return 2 ** zeros_count
    for i in range(n):
        nums[i] = abs(nums[i])
    _sum = sum(nums)
    if (target + _sum) % 2 != 0:
        return 0
    new_target = abs(target - _sum) // 2
    dp = [[0 for _ in range(new_target + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(1, new_target + 1):
            if j >= nums[i]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
            else:
                dp[i][j] = dp[i - 1][j]
    if zeros_count > 0:
        return dp[n - 1][new_target] * 2 ** zeros_count
    return dp[n - 1][new_target]


print(findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
print(findTargetSumWays([1], 1))  # 1
print(findTargetSumWays([9, 7, 0, 3, 9, 8, 6, 5, 7, 6], 2))  # 40
print(findTargetSumWays([1, 0], 1))  # 2
print(findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))  # 256
print(findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0))  # 1048576
