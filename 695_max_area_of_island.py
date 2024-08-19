def maxAreaOfIsland(grid):
    m, n = len(grid), len(grid[0])
    island_area = 0

    def traverse_island(cell):
        nonlocal island_area
        grid[cell[0]][cell[1]] = 2
        island_area += 1
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i, new_j = cell[0] + d[0], cell[1] + d[1]
            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                traverse_island((new_i, new_j))

    max_area = float("-inf")
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                island_area = 0
                traverse_island((i, j))
                max_area = max(max_area, island_area)
    return max_area


print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))  # 6
