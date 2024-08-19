
def maxProfit(prices):
    profit, buy, n = 0, 0, len(prices)
    for sell in range(buy+1, len(prices)):
        if prices[sell] < prices[sell-1]:
            profit += (prices[sell-1] - prices[buy])
            buy = sell
    if n > 1 and buy < n - 1:
        profit += (prices[n-1] - prices[buy])
    return profit


print(maxProfit([1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2]))  # 6
print(maxProfit([1]))                       # 0
print(maxProfit([1, 4, 5, 3, 6, 1]))        # 7
print(maxProfit([1, 5, 3, 6, 1]))           # 7
print(maxProfit([1, 5, 3, 4, 5, 6, 7, 1]))  # 8
print(maxProfit([4, 1, 5, 1]))              # 4
print(maxProfit([1, 3, 2, 5]))              # 5
print(maxProfit([7, 1, 5, 3, 6, 4]))        # 7
print(maxProfit([1, 2, 3, 4, 5]))           # 4
print(maxProfit([7, 6, 4, 3, 1]))           # 0
