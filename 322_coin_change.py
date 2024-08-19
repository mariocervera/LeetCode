def coinChange(coins, amount):
    inf = float("inf")
    dp = [0] + [inf] * amount
    for i in range(1, amount + 1):
        dp[i] = min(dp[i-coin] if i-coin >= 0 else inf for coin in coins) + 1
    return dp[amount] if dp[amount] != inf else -1


print(coinChange(coins=[1, 2, 5], amount=11))  # 3
print(coinChange(coins=[2], amount=3))  # -1
print(coinChange(coins=[1], amount=0))  # 0