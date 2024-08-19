from collections import deque

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    rotten, fresh = deque(), set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh.add((i, j))
            elif grid[i][j] == 2:
                rotten.append((i, j))

    if not rotten:
        return 0

    minutes = -1
    while rotten:
        for _ in range(len(rotten)):
            rotten_orange = rotten.popleft()
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_rotten_orange = rotten_orange[0] + d[0], rotten_orange[1] + d[1]
                if 0 <= new_rotten_orange[0] < m and 0 <= new_rotten_orange[1] < n and new_rotten_orange in fresh:
                    fresh.remove(new_rotten_orange)
                    rotten.append(new_rotten_orange)
        minutes += 1
    return minutes if not fresh else -1


print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
print(orangesRotting([[0, 2]]))  # 0
print(orangesRotting([[0]]))  # 0
