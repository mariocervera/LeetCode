
def restoreMatrix(rowSum, colSum):
    m, n = len(rowSum), len(colSum)
    res = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_val = min(rowSum[i], colSum[j])
            res[i][j] = new_val
            rowSum[i] -= new_val
            colSum[j] -= new_val
    return res


print(restoreMatrix(rowSum=[3, 8], colSum=[4, 7]))  # [[3,0], [1,7]]
print(restoreMatrix(rowSum=[5, 7, 10], colSum=[8, 6, 8]))  # [[0,5,0], [6,1,0], [2,0,8]]
