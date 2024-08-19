
# def maximalSquare(matrix):
#     m, n = len(matrix), len(matrix[0])
#
#     dp = [[0 for _ in range(n)] for _ in range(m)]
#
#     max_side = 0
#
#     for i in range(m):
#         dp[i][n-1] = int(matrix[i][n-1])
#         max_side = max(max_side, dp[i][n-1])
#     for j in range(n):
#         dp[m-1][j] = int(matrix[m-1][j])
#         max_side = max(max_side, dp[m-1][j])
#
#     for i in range(m-2, -1, -1):
#         for j in range(n-2, -1, -1):
#             if matrix[i][j] == "0":
#                 continue
#             dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
#             max_side = max(max_side, dp[i][j])
#
#     return max_side ** 2


def maximalSquare(matrix):
    m, n, max_side = len(matrix), len(matrix[0]), 0

    dp = []
    for j in range(n):
        dp.append(int(matrix[m-1][j]))
        max_side = max(max_side, dp[j])

    for i in range(m-2, -1, -1):
        for j in range(n-1, -1, -1):
            if j == n-1:
                temp = dp[j]
                dp[j] = int(matrix[i][j])
            else:
                value = (1 + min(temp, dp[j+1], dp[j])) if matrix[i][j] == "1" else 0
                temp = dp[j]
                dp[j] = value
            max_side = max(max_side, dp[j])

    return max_side ** 2

print(maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))  # 4


print(maximalSquare([["0", "1"],
                     ["1", "0"]]))  # 1


print(maximalSquare([["0"]]))  # 0
