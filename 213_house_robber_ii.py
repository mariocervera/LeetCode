
def rob_linear(arr):
    n, mod = len(arr), 3
    dp = [arr[0], 0, 0]
    for i in range(1, n):
        dp[i % mod] = max(dp[(i-1) % mod], dp[(i-2) % mod] + arr[i])
    return dp[(n-1) % mod]

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    return max(rob_linear(nums[:n-1]), rob_linear(nums[1:n]))


print(rob([2, 3, 2]))  # 3
print(rob([1, 2, 3, 1]))  # 4
print(rob([1, 2, 3]))  # 3

