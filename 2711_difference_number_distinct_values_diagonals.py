from collections import defaultdict

def differenceOfDistinctValues(grid):
    m, n = len(grid), len(grid[0])
    res = [[0 for _ in range(n)] for _ in range(m)]
    bottom_right = res.copy()
    diagonals = defaultdict(set)

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            diagonals[j-i].add(grid[i][j])
            bottom_right[i][j] = len(diagonals[j-i])

    diagonals.clear()
    for i in range(m):
        for j in range(n):
            tl = len(diagonals[j-i]) if i-1 >= 0 and j-1 >= 0 else 0
            br = bottom_right[i+1][j+1] if i+1 < m and j+1 < n else 0
            res[i][j] = abs(tl - br)
            diagonals[j-i].add(grid[i][j])

    return res


print(differenceOfDistinctValues([[1, 2, 3],
                                  [3, 1, 5],
                                  [3, 2, 1]]))  # [[1,1,0],[1,0,1],[0,1,1]]

print(differenceOfDistinctValues([[1]]))  # [[0]]
