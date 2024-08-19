
def numberOfPairs(points):
    points.sort(key=lambda p: (-p[1], p[0]))
    res, n = 0, len(points)
    for i in range(n - 1):
        min_x = float("inf")
        for j in range(i + 1, n):
            if points[i][0] <= points[j][0] < min_x:
                res += 1
                min_x = min(min_x, points[j][0])
            if points[j][0] == points[i][0]:
                break
    return res


print(numberOfPairs([[1, 1], [2, 2], [3, 3]]))  # 0
print(numberOfPairs([[6, 2], [4, 4], [2, 6]]))  # 2
print(numberOfPairs([[3, 1], [1, 3], [1, 1]]))  # 2
print(numberOfPairs([[0, 1], [1, 3], [6, 1]]))  # 2
