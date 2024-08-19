
def countSquares(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [0 for _ in range(n)]
    res = 0
    for j in range(n):
        dp[j] = 1 if matrix[m-1][j] == 1 else 0
        res += dp[j]
    for i in range(m-2, -1, -1):
        temp = dp[n-1]
        dp[n-1] = 1 if matrix[i][n-1] == 1 else 0
        res += dp[n-1]
        for j in range(n-2, -1, -1):
            new = (min(dp[j], min(dp[j+1], temp)) + 1) if matrix[i][j] == 1 else 0
            temp = dp[j]
            dp[j] = new
            res += dp[j]
    return res


print(countSquares([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))  # 15

print(countSquares([
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))  # 7
