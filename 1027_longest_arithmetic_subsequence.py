
def longestArithSeqLength(nums):
    res, n = -1, len(nums)
    dp = [{} for _ in range(n)]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            diff = nums[i] - nums[j]
            if diff not in dp[i]:
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[i][diff])
    return res


print(longestArithSeqLength([3, 6, 9, 12]))  # 4
print(longestArithSeqLength([9, 4, 7, 2, 10]))  # 3
print(longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))  # 4
