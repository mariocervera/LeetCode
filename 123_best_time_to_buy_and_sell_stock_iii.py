# def maxProfit(prices):
#     n = len(prices)
#     dp = [[0 for _ in range(n)] for _ in range(2)]
#
#     min_price = prices[0]
#     best_1t_choice = [float("-inf")] * n
#     for i in range(1, n):
#         dp[0][i] = max(dp[0][i-1], prices[i] - min_price)
#         best_1t_choice[i] = max(best_1t_choice[i-1], dp[0][i] - prices[i])
#         min_price = min(min_price, prices[i])
#
#     for i in range(1, n):
#         dp[1][i] = max(dp[1][i-1], best_1t_choice[i-1] + prices[i])
#
#     return max(dp[0][n-1], dp[1][n-1])

def maxProfit(prices):
    buy_1, buy_2 = float("inf"), float("inf")
    sell_1, sell_2 = 0, 0
    for i in range(len(prices)):
        buy_1 = min(buy_1, prices[i])
        sell_1 = max(sell_1, prices[i] - buy_1)
        buy_2 = min(buy_2, prices[i] - sell_1)
        sell_2 = max(sell_2, prices[i] - buy_2)
    return sell_2


print(maxProfit([3]))  # 0
print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # 6
print(maxProfit([1, 2, 3, 4, 5]))  # 4
print(maxProfit([7, 6, 4, 3, 1]))  # 0
print(maxProfit([6, 1, 3, 2, 4, 7]))  # 7
print(maxProfit([1, 2]))  # 1
