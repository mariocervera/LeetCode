from collections import deque


def getMaximumGold(grid):
    m, n = len(grid), len(grid[0])
    q = deque([(grid[i][j], (i, j), {(i, j)}) for i in range(m) for j in range(n) if grid[i][j] != 0])
    res = 0
    while q:
        gold, cell, visited = q.popleft()
        res = max(res, gold)
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_cell = (cell[0] + d[0], cell[1] + d[1])
            if 0 <= new_cell[0] < m and 0 <= new_cell[1] < n and new_cell not in visited and grid[new_cell[0]][
                new_cell[1]] != 0:
                q.append((gold + grid[new_cell[0]][new_cell[1]], new_cell, visited | {new_cell}))
    return res


# print(getMaximumGold([[0, 6, 0],
#                       [5, 8, 7],
#                       [0, 9, 0]]))  # 24
#
# print(getMaximumGold([[1, 0, 7],
#                       [2, 0, 6],
#                       [3, 4, 5],
#                       [0, 3, 0],
#                       [9, 0, 20]]))  # 28
#
# print(getMaximumGold([[1, 0, 7, 0, 0, 0],
#                       [2, 0, 6, 0, 1, 0],
#                       [3, 5, 6, 7, 4, 2],
#                       [4, 3, 1, 0, 2, 0],
#                       [3, 0, 5, 0, 20, 0]]))  # 60

print(getMaximumGold([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]]))  # 25
