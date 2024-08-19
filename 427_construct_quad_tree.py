
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid):
    n = len(grid)

    if all(grid[i][j] == grid[0][0] for i in range(n) for j in range(n)):
        return Node(grid[0][0], True, None, None, None, None)

    return Node(
        0,
        False,
        construct([row[:n//2] for row in grid[:n//2]]),
        construct([row[n//2:] for row in grid[:n//2]]),
        construct([row[:n//2] for row in grid[n//2:]]),
        construct([row[n//2:] for row in grid[n//2:]]),
    )














