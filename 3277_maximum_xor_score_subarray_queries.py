
def maximumSubarrayXor(nums, queries):
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    for size in range(1, n):
        for i in range(n-size):
            j = i+size
            dp[i][j] = dp[i][j-1] ^ dp[i+1][j]
    for size in range(1, n):
        for i in range(n-size):
            j = i+size
            dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
    res = []
    for l, r in queries:
        res.append(dp[l][r])
    return res


print(maximumSubarrayXor(nums=[2, 8, 4, 32, 16, 1],
                         queries=[[0, 2], [1, 4], [0, 5]]))  # [12,60,60]

print(maximumSubarrayXor(nums=[0, 7, 3, 2, 8, 5, 1],
                         queries=[[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]]))  # [7,14,11,14,5]
