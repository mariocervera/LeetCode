from collections import defaultdict


def maxScore(grid):
    m, n = len(grid), len(grid[0])
    values_rows = defaultdict(set)
    for row in range(m):
        for column in range(n):
            values_rows[grid[row][column]].add(row)
    values_rows = [(val, list(rows)) for val, rows in values_rows.items()]
    dp = {}

    def backtrack(i, mask):
        if (i, mask) in dp:
            return dp[(i, mask)]
        if i == len(values_rows):
            return 0
        res = backtrack(i + 1, mask)
        val, rows = values_rows[i]
        for val_row in rows:
            if mask & (1 << val_row) == 0:
                res = max(res, val + backtrack(i + 1, mask | (1 << val_row)))
        dp[(i, mask)] = res
        return res

    return backtrack(0, 0)


print(maxScore([[1, 2, 3],
                [4, 3, 2],
                [1, 1, 1]]))  # 8

print(maxScore([[8, 7, 6],
                [8, 3, 2]]))  # 15

print(maxScore([[92, 11, 45, 88, 38, 13, 65, 85],
                [52, 83, 3, 14, 82, 51, 27, 59],
                [65, 69, 99, 27, 7, 70, 39, 43],
                [43, 46, 22, 19, 75, 70, 57, 50],
                [54, 36, 91, 80, 74, 43, 62, 61],
                [35, 45, 19, 32, 92, 50, 93, 88],
                [60, 15, 93, 10, 89, 32, 51, 11],
                [82, 66, 42, 61, 78, 94, 66, 7],
                [75, 56, 49, 78, 81, 61, 79, 50]]))  # 797
