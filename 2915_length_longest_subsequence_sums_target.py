
def lengthOfLongestSubsequence(nums, target):
    n = len(nums)
    dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n+1):
        for j in range(1, target+1):
            if j >= nums[i-1] and dp[i-1][j-nums[i-1]] != -1:
                dp[i][j] = max(dp[i - 1][j], dp[i-1][j-nums[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]


print(lengthOfLongestSubsequence(nums=[1, 2, 3, 4, 5], target=9))  # 3
print(lengthOfLongestSubsequence(nums=[4, 1, 3, 2, 1, 5], target=7))  # 4
print(lengthOfLongestSubsequence(nums=[1, 1, 5, 4, 5], target=3))  # -1
print(lengthOfLongestSubsequence(nums=[1, 2], target=4))  # -1
