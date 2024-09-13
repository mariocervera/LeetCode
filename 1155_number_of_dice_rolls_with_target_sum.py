from functools import lru_cache

mod = 10 ** 9 + 7


# Top-down solution using memoization

def num_rolls_to_target_top_down(n, k, target):

    @lru_cache(maxsize=None)
    def backtrack(i, _sum):
        if i == n:
            return 1 if _sum == target else 0
        if _sum > target:
            return 0
        res = 0
        for face in range(1, k + 1):
            res = (res + backtrack(i + 1, _sum + face)) % mod
        return res

    return backtrack(0, 0)


# Bottom-up dynamic-programming solution

def num_rolls_to_target_bottom_up(n, k, target):
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

    for j in range(target + 1):
        dp[1][j] = 1 if 1 <= j <= k else 0

    for i in range(2, n + 1):
        for j in range(target + 1):
            for face in range(1, k + 1):
                if j >= face:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % mod

    return dp[n][target]


print(num_rolls_to_target_top_down(n=1, k=6, target=3))  # 1
print(num_rolls_to_target_top_down(n=2, k=6, target=7))  # 6
print(num_rolls_to_target_top_down(n=30, k=30, target=500))  # 222616187

print(num_rolls_to_target_bottom_up(n=1, k=6, target=3))  # 1
print(num_rolls_to_target_bottom_up(n=2, k=6, target=7))  # 6
print(num_rolls_to_target_bottom_up(n=30, k=30, target=500))  # 222616187
