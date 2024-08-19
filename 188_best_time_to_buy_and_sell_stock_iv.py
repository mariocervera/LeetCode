
def maxProfit(k, prices):
    n = len(prices)
    if n == 1:
        return 0

    dp = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(1, k+1):
        tmp_max = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + tmp_max)
            tmp_max = max(tmp_max, dp[i-1][j-1] - prices[j])
    return dp[k][n - 1]



print(maxProfit(k=2, prices=[2, 4, 1]))  # 2
print(maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))  # 7
print(maxProfit(k=2, prices=[2, 1, 4, 5, 2, 9, 7]))  # 11
