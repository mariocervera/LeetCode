from collections import deque
import heapq

def maximumSafenessFactor(grid):
    n = len(grid)
    q = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                q.append((i, j))
            else:
                grid[i][j] = "X"

    while q:
        i, j = q.popleft()
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_i, new_j = i + d[0], j + d[1]
            if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == "X":
                q.append((new_i, new_j))
                grid[new_i][new_j] = grid[i][j] - 1
                if grid[new_i][new_j] == 0:
                    grid[new_i][new_j] -= 1

    pq = [(grid[0][0], (0,0))]
    visited = [[False for _ in range(n)] for _ in range(n)]
    res = float("-inf")
    while pq:
        dist, cell = heapq.heappop(pq)
        if not visited[cell[0]][cell[1]]:
            visited[cell[0]][cell[1]] = True
            res = max(res, dist)
            for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_i, new_j = cell[0] + d[0], cell[1] + d[1]
                if new_i == n-1 and new_j == n-1:
                    res = max(res, grid[new_i][new_j])
                    return res * -1
                if 0 <= new_i < n and 0 <= new_j < n and not visited[new_i][new_j]:
                    heapq.heappush(pq, (grid[new_i][new_j], (new_i, new_j)))

    return res * -1




print(maximumSafenessFactor([[1, 0, 0],
                             [0, 0, 0],
                             [0, 0, 1]]))  # 0

print(maximumSafenessFactor([[0, 0, 1],
                             [0, 0, 0],
                             [0, 0, 0]]))  # 2

print(maximumSafenessFactor([[0, 0, 0, 1],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [1, 0, 0, 0]]))  # 2
