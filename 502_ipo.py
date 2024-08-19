import heapq

# class Project:
#     def __init__(self, capital, profit, sort_by_profit=False):
#         self.capital = capital
#         self.profit = profit
#         self.sort_by_profit = sort_by_profit
#
#     def __lt__(self, other):
#         if self.sort_by_profit:
#             return self.profit > other.profit
#         return self.capital < other.capital


def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    capital_sorted_list = [(capital[i], profits[i]) for i in range(n)]
    capital_sorted_list.sort(reverse=True)
    profit_heap = []
    projects_counter, current_capital = 0, w
    while projects_counter < k:
        while capital_sorted_list and capital_sorted_list[-1][0] <= current_capital:
            heapq.heappush(profit_heap, -capital_sorted_list.pop()[1])
        if len(profit_heap) == 0:
            return current_capital
        current_capital += -heapq.heappop(profit_heap)
        projects_counter += 1
    return current_capital


print(findMaximizedCapital(k=1, w=0, profits=[1, 2, 3], capital=[1, 1, 2]))  # 0
print(findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))  # 4
print(findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))  # 6
