from collections import deque

def traverse_island(grid, i, j, m, n, border):
    grid[i][j] = 2
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_i, new_j = i + d[0], j + d[1]
        if 0 <= new_i < m and 0 <= new_j < n:
            if grid[new_i][new_j] == 0:
                grid[new_i][new_j] = 3
                border.add((new_i, new_j))
            elif grid[new_i][new_j] == 1:
                traverse_island(grid, new_i, new_j, m, n, border)

def shortestBridge(grid):
    m, n = len(grid), len(grid[0])
    island_found, border = False, set()
    i = 0
    while i < m and not island_found:
        j = 0
        while j < n and not island_found:
            if grid[i][j] == 1:
                traverse_island(grid, i, j, m, n, border)
                island_found = True
            j += 1
        i += 1
    q = deque(border)
    while q:
        cell_i, cell_j = q.popleft()
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i, new_j = cell_i + d[0], cell_j + d[1]
            if 0 <= new_i < m and 0 <= new_j < n:
                if grid[new_i][new_j] == 1:
                    return grid[cell_i][cell_j] - 2
                if grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = grid[cell_i][cell_j] + 1
                    q.append((new_i, new_j))
    return -1



print(shortestBridge([[0,0,0,0,0,0],
                      [0,1,0,0,0,0],
                      [1,1,0,0,0,0],
                      [1,1,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,1,1,0,0]]))  # 2

# print(shortestBridge([[0, 1], [1, 0]]))  # 1
# print(shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))  # 2
# print(shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))  # 1
