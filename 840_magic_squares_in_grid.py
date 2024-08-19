
def contains_valid_digits(grid, i, j):
    arr = []
    for x in range(3):
        arr.extend(grid[i+x][j:j+3])
    return sorted(arr) == list(range(1, 10))


def contains_valid_sums(grid, i, j):
    sums = set()
    square = [row[j:j+3] for row in grid[i:i+3]]
    sums.update({sum(row) for row in square})
    sums.update({sum(column) for column in zip(*square)})
    sums.update({grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]})
    sums.update({grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]})
    return len(sums) == 1

def is_magic(grid, i, j):
    return grid[i+1][j+1] == 5 and contains_valid_digits(grid, i, j) and contains_valid_sums(grid, i, j)


def numMagicSquaresInside(grid):
    m, n = len(grid), len(grid[0])
    if m < 3 or n < 3:
        return 0
    res = 0
    for i in range(m-2):
        for j in range(n-2):
            if is_magic(grid, i, j):
                res += 1
    return res


print(numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))  # 1
print(numMagicSquaresInside([[8]]))  # 0
