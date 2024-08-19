from collections import defaultdict

def maxTaxiEarnings(n, rides):
    rides_start_at = defaultdict(list)
    for s, e, t in rides:
        rides_start_at[s].append((e, e-s+t))
    dp = [0] * (n+1)
    for i in range(n - 1, 0, -1):
        for e, t in rides_start_at[i]:
            dp[i] = max(dp[i], dp[e] + t)
        dp[i] = max(dp[i], dp[i+1])
    return dp[1]


print(maxTaxiEarnings(n=5, rides=[[2, 5, 4], [1, 5, 1]]))  # 7
print(maxTaxiEarnings(n=20, rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]))  # 20


