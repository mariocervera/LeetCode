
def longestIncreasingPath(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    def dfs(s_i, s_j):
        if dp[s_i][s_j] > 0:
            return dp[s_i][s_j]
        max_len_from_source = 1
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i, new_j = s_i + d[0], s_j + d[1]
            if not (0 <= new_i < m) or not (0 <= new_j < n):
                continue
            if matrix[s_i][s_j] < matrix[new_i][new_j]:
                max_len_from_source = max(max_len_from_source, 1 + dfs(new_i, new_j))
        dp[s_i][s_j] = max_len_from_source
        return max_len_from_source


    max_len = float("-inf")
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 0:
                len_from_ij = dfs(i, j)
                max_len = max(max_len, len_from_ij)
    return max_len


print(longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))  # 4
print(longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))  # 4
print(longestIncreasingPath([[1]]))  # 1
