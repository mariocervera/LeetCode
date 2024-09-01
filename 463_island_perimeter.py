def islandPerimeter(grid):
    m, n = len(grid), len(grid[0])
    visited = set()
    perimeter = 0

    def get_cell_perimeter(row, col):
        res = 0
        if row - 1 < 0 or grid[row-1][col] == 0:
            res += 1
        if row + 1 == m or grid[row+1][col] == 0:
            res += 1
        if col - 1 < 0 or grid[row][col-1] == 0:
            res += 1
        if col + 1 == n or grid[row][col+1] == 0:
            res += 1
        return res

    def traverse_island(row, col):
        nonlocal perimeter
        perimeter += get_cell_perimeter(row, col)
        visited.add((row, col))
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < m and 0 <= new_col < n and \
                    grid[new_row][new_col] == 1 and \
                    (new_row, new_col) not in visited:
                traverse_island(new_row, new_col)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                traverse_island(i, j)
                return perimeter

    return -1  # Should never occur


print(islandPerimeter([[0, 1, 0, 0],
                       [1, 1, 1, 0],
                       [0, 1, 0, 0],
                       [1, 1, 0, 0]]))  # 16

print(islandPerimeter([[1]]))  # 4

print(islandPerimeter([[1, 0]]))  # 4

print(islandPerimeter([[0, 1]]))  # 4
