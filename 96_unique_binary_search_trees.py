
def numTrees(n):
    dp = [1, 1] + [0] * (n-1)
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]


print(numTrees(1))  # 1
print(numTrees(2))  # 2
print(numTrees(3))  # 5
print(numTrees(4))  # 14
print(numTrees(5))  # 42
