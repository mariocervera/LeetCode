def minPathSum(grid):
    m, n = len(grid), len(grid[0])

    dp = [0] * (n-1) + [grid[m-1][n-1]]
    for j in range(n-2, -1, -1):
        dp[j] = dp[j+1] + grid[m-1][j]

    for i in range(m-2, -1, -1):
        for j in range(n-1, -1, -1):
            dp[j] = dp[j] + grid[i][j] if j == n-1 else min(dp[j], dp[j+1]) + grid[i][j]

    return dp[0]


print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
print(minPathSum([[1, 2, 3], [4, 5, 6]]))  # 12
