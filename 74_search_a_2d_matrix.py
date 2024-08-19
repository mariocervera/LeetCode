
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    low, high = 0, (m * n) - 1
    while low <= high:
        mid = (low+high)//2
        elem = matrix[mid//n][mid%n]
        if target == elem:
            return True
        elif target < elem:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
