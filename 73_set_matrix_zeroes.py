
def setZeroes(matrix):
    m, n, col0 = len(matrix), len(matrix[0]), 1
    for i in range(m):
        if not matrix[i][0]:
            col0 = 0
        for j in range(1, n):
            if not matrix[i][j]:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(m-1, -1, -1):
        for j in range(n-1, 0, -1):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0
        if not col0:
            matrix[i][0] = 0


m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(m1)
print(m1)  # [[1,0,1],[0,0,0],[1,0,1]]

m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(m2)
print(m2)  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
