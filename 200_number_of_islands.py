
def numIslands(grid):
    m, n = len(grid), len(grid[0])

    def traverse_island(row, column):
        nonlocal grid
        if not (0 <= row < m) or not (0 <= column < n) or grid[row][column] in "02":
            return
        grid[row][column] = "2"
        for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_row, new_column = row + d[0], column + d[1]
            traverse_island(new_row, new_column)

    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                traverse_island(i, j)
                islands += 1
    return islands


print(numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))  # 1

print(numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))  # 3
