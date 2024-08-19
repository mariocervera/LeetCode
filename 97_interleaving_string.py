
def isInterleave(s1, s2, s3):
    m, n = len(s1), len(s2)

    if m + n != len(s3):
        return False

    dp = [[False for _ in range(n+1)] for _ in range(m+1)]

    dp[0][0] = True

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[j+i-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

    return dp[m][n]



print(isInterleave(s1 ="db", s2="b", s3="cbb"))  # False
print(isInterleave(s1="", s2="", s3="a"))  # False
print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))  # True
print(isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))  # False
print(isInterleave(s1="", s2="", s3=""))  # True
