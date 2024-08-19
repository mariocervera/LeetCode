
def rotate(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
    for i in range(n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



mtx = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(mtx)
print(mtx)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
