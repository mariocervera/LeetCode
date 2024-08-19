from collections import defaultdict

def findDiagonalOrder(mat):
    m, n = len(mat), len(mat[0])
    diagonals = defaultdict(list)
    for i in range(m):
        for j in range(n):
            diagonals[i+j].append(mat[i][j])
    res = []
    for diagonal in diagonals:
        if diagonal % 2 != 0:
            res.extend(diagonals[diagonal])
        else:
            res.extend(diagonals[diagonal][::-1])
    return res



print(findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,4,7,5,3,6,8,9]
print(findDiagonalOrder([[1, 2], [3, 4]]))  # [1,2,3,4]
