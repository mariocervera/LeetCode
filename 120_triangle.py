def minimumTotal(triangle):
    dp = triangle[-1]
    for i in range(len(triangle[-1]) - 2, -1, -1):
        for j in range(i+1):
            dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
    return dp[0]


print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
print(minimumTotal([[-10]]))  # -10
