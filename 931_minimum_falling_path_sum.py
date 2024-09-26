def minFallingPathSum(matrix):
    n = len(matrix)
    dp = matrix[-1]
    min_sum = float("inf")
    for i in range(n-2, -1, -1):
        for j in range(n):
            new_sum = matrix[i][j] + min(float("inf") if j == 0 else below_left, dp[j], dp[j+1] if j < n-1 else float("inf"))
            below_left = dp[j]
            dp[j] = new_sum
            if i == 0:
                min_sum = min(min_sum, new_sum)
    return min_sum if n > 1 else matrix[0][0]


print(minFallingPathSum([[2, 1, 3],
                         [6, 5, 4],
                         [7, 8, 9]]))  # 13

print(minFallingPathSum([[-19, 57],
                         [-40, -5]]))  # -59

print(minFallingPathSum([[2]]))  # 2
