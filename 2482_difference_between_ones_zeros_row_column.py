
def onesMinusZeros(grid):
    m, n = len(grid), len(grid[0])
    ones_rows, ones_columns = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                ones_rows[i], ones_columns[j] = ones_rows[i] - 1, ones_columns[j] - 1
            else:
                ones_rows[i], ones_columns[j] = ones_rows[i] + 1, ones_columns[j] + 1
    for i in range(m):
        for j in range(n):
            grid[i][j] = ones_rows[i] + ones_columns[j]
    return grid


print(onesMinusZeros([[0, 1, 1],
                      [1, 0, 1],
                      [0, 0, 1]]))  # [[0,0,4],[0,0,4],[-2,-2,2]]


print(onesMinusZeros([[1, 1, 1],
                      [1, 1, 1]]))  # [[5,5,5],[5,5,5]]
