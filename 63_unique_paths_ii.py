
def uniquePathsWithObstacles(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    return dp[n-1]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
print(uniquePathsWithObstacles([[0, 1], [0, 0]]))  # 1
