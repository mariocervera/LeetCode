
def findMaxFish(grid):
    m, n = len(grid), len(grid[0])

    def traverse_water(row, column):
        total_fish = grid[row][column]
        grid[row][column] = 0
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row, new_column = row + d[0], column + d[1]
            if 0 <= new_row < m and 0 <= new_column < n and grid[new_row][new_column] != 0:
                total_fish += traverse_water(new_row, new_column)
        return total_fish

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                res = max(res, traverse_water(i, j))
    return res


print(findMaxFish(grid=[[0, 2, 1, 0],
                        [4, 0, 0, 3],
                        [1, 0, 0, 4],
                        [0, 3, 2, 0]]))  # 7

print(findMaxFish(grid=[[1, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 1]]))  # 1
