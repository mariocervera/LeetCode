from collections import deque


def copy_matrix(mat):
    return [row[:] for row in mat]


def is_all_zero(mat):
    return all(num == 0 for row in mat for num in row)


def flip_cell(mat, i, j, m, n):
    for d in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_i, new_j = i + d[0], j + d[1]
        if 0 <= new_i < m and 0 <= new_j < n:
            mat[new_i][new_j] = 0 if mat[new_i][new_j] == 1 else 1
    return mat


def next_cell(i, j, m, n):
    if j < n-1:
        return i, j+1
    if i == m-1:
        return None
    return i+1, 0

def minFlips(mat):
    m, n = len(mat), len(mat[0])
    q = deque()
    q.append((copy_matrix(mat), (0, 0)))
    steps = 0
    while q:
        for _ in range(len(q)):
            matrix, cell = q.popleft()
            if is_all_zero(matrix):
                return steps
            cell_to_flip = cell
            while cell_to_flip:
                q.append(
                    (flip_cell(copy_matrix(matrix), cell_to_flip[0], cell_to_flip[1], m, n),
                     next_cell(cell[0], cell[1], m, n))
                )
                cell_to_flip = next_cell(cell_to_flip[0], cell_to_flip[1], m, n)
        steps += 1
    return -1


print(minFlips([[0, 1], [0, 1]]))  # 2  (I get wrong result)
print(minFlips([[0, 0], [0, 1]]))  # 3
print(minFlips([[0]]))  # 0
print(minFlips([[1, 0, 0], [1, 0, 0]]))  # -1


