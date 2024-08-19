
def longestPalindromeSubseq(s):
    n = len(s)
    s_reversed = s[::-1]
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s_reversed[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]


print(longestPalindromeSubseq("bbbab"))  # 4
print(longestPalindromeSubseq("cbbd"))  # 2
