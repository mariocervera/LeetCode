
def minimumNumbers(num, k):
    dp = [0] + [float("inf")] * num
    candidates = list(range(k, num+1, 10))
    for i in range(1, num+1):
        for candidate in candidates:
            if i-candidate >= 0 and dp[i-candidate] != float("inf"):
                dp[i] = min(dp[i], dp[i-candidate] + 1)
    return dp[num] if dp[num] != float("inf") else -1


print(minimumNumbers(58, 9))  # 2
print(minimumNumbers(37, 2))  # -1
print(minimumNumbers(0, 7))  # 0
