
def findMaxForm(strs, m, n):
    strs_len = len(strs)
    dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(strs_len + 1)]
    for i in range(1, strs_len + 1):
        s = strs[i - 1]
        zeroes = s.count("0")
        ones = len(s) - zeroes
        for j in range(m + 1):
            for k in range(n + 1):
                if zeroes <= j and ones <= k:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeroes][k - ones] + 1)
                else:
                    dp[i][j][k] = dp[i - 1][j][k]
    return dp[strs_len][m][n]



print(findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))  # 4
print(findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=4, n=3))  # 3
print(findMaxForm(strs=["10", "0", "1"], m=1, n=1))  # 2
