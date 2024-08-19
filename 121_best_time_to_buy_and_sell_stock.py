
def maxProfit(prices):
    profit, buy = 0, 0
    for sell in range(1, len(prices)):
        if prices[sell]-prices[buy] > profit:
            profit = prices[sell]-prices[buy]
        if prices[sell] < prices[buy]:
            buy = sell
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(maxProfit([7, 6, 4, 3, 1]))  # 0
