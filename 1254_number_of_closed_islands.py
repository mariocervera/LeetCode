
def traverse_island(grid, i, j, m, n):
    grid[i][j] = 1
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_i, new_j = i + d[0], j + d[1]
        if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
            traverse_island(grid, new_i, new_j, m, n)


def closedIsland(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        if grid[i][0] == 0:
            traverse_island(grid, i, 0, m, n)
        if grid[i][n-1] == 0:
            traverse_island(grid, i, n-1, m, n)
    for j in range(n):
        if grid[0][j] == 0:
            traverse_island(grid, 0, j, m, n)
        if grid[m-1][j] == 0:
            traverse_island(grid, m-1, j, m, n)
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                traverse_island(grid, i, j, m, n)
                res += 1
    return res



print(closedIsland([[1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 0]]))  # 2

print(closedIsland([[0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0]]))  # 1

print(closedIsland([[1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1]]))  # 2
