
def spiralOrder(matrix):

    def is_bad_cell(x, y):
        return not (0 <= x < m) or not (0 <= y < n) or matrix[x][y] == "#"

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m, n = len(matrix), len(matrix[0])
    _dir, i, j = 0, 0, 0
    res = []
    while not is_bad_cell(i, j):
        res.append(matrix[i][j])
        matrix[i][j] = "#"
        new_i, new_j = i + dirs[_dir][0], j + dirs[_dir][1]
        if is_bad_cell(new_i, new_j):
            _dir = (_dir + 1) % 4
            new_i, new_j = i + dirs[_dir][0], j + dirs[_dir][1]
        i, j = new_i, new_j
    return res


print(spiralOrder([[1]]))  # [1]
print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
