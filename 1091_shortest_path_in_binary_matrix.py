
from collections import deque

dirs = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    start, target = (0, 0), (n-1, n-1)
    if grid[start[0]][start[1]] == 1:
        return -1
    q = deque([start])
    grid[start[0]][start[1]] = 2
    path_len = 1
    while q:
        for _ in range(len(q)):
            current_cell = q.popleft()
            if current_cell == target:
                return path_len
            for d in dirs:
                i, j = current_cell[0] + d[0], current_cell[1] + d[1]
                if not 0 <= i < n or not 0 <= j < n or grid[i][j] != 0:
                    continue
                grid[i][j] = 2
                q.append((i, j))
        path_len += 1
    return -1


print(shortestPathBinaryMatrix([[0, 1], [1, 0]]))  # 2
print(shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # 4
print(shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # -1
