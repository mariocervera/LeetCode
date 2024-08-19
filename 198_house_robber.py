# def rob(nums):
#     n = len(nums)
#     dp = [nums[0]] + [0] * (n - 1)
#     if n > 1:
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, n):
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#     return dp[n - 1]


def rob(nums):
    n, mod = len(nums), 3
    dp = [nums[0], 0, 0]
    if n > 1:
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i % mod] = max(dp[(i-1) % mod], dp[(i-2) % mod] + nums[i])
    return dp[(n-1) % mod]


print(rob([1]))  # 1
print(rob([1, 2]))  # 2
print(rob([2, 1]))  # 2
print(rob([1, 2, 3, 1]))  # 4
print(rob([2, 7, 9, 3, 1]))  # 12
