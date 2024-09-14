from functools import lru_cache


def findSafeWalk(grid, health):
    m, n = len(grid), len(grid[0])
    visited = set()

    @lru_cache(maxsize=None)
    def backtrack(cell, remaining_health):
        if grid[cell[0]][cell[1]] == 1:
            remaining_health -= 1
        if not remaining_health:
            return False
        if cell == (m-1, n-1):
            return True
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_cell = (cell[0] + d[0]), (cell[1] + d[1])
            if 0 <= new_cell[0] < m and 0 <= new_cell[1] < n and new_cell not in visited:
                visited.add(new_cell)
                if backtrack(new_cell, remaining_health):
                    return True
                visited.remove(new_cell)
        return False

    return backtrack((0, 0), health)


print(findSafeWalk(grid=[[0, 1, 0, 0, 0],
                         [0, 1, 0, 1, 0],
                         [0, 0, 0, 1, 0]],
                   health=1))  # True

print(findSafeWalk(grid=[[0, 1, 1, 0, 0, 0],
                         [1, 0, 1, 0, 0, 0],
                         [0, 1, 1, 1, 0, 1],
                         [0, 0, 1, 0, 1, 0]],
                   health=3))  # False

print(findSafeWalk(grid=[[1, 1, 1],
                         [1, 0, 1],
                         [1, 1, 1]],
                   health=5))  # True
