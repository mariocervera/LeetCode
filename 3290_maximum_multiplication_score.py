
def maxScore(a, b):
    m, n = len(a), len(b)
    dp = [[float("-inf") for _ in range(n+1)] for _ in range(m+1)]
    for j in range(n+1):
        dp[0][j] = 0
    for i in range(1, m+1):
        for j in range(i, n+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + a[i-1]*b[j-1])
    return dp[m][n]


print(maxScore(a=[3, 2, 5, 6],
               b=[2, -6, 4, -5, -3, 2, -7]))  # 26

print(maxScore(a=[-1, 4, 5, -2],
               b=[-5, -1, -3, -2, -4]))  # -1
