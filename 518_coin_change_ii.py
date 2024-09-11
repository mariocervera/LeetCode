from functools import lru_cache

def change(amount, coins):

    @lru_cache(maxsize=None)
    def backtrack(i, current_sum):
        if current_sum == amount:
            return 1
        if i == len(coins) or current_sum > amount:
            return 0
        return backtrack(i + 1, current_sum) + backtrack(i, current_sum + coins[i])

    return backtrack(0, 0)


print(change(amount=5, coins=[1, 2, 5]))  # 4
print(change(amount=3, coins=[2]))  # 0
print(change(amount=10, coins=[10]))  # 1
