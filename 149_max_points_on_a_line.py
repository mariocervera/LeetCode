def maxPoints(points):
    ans = 0
    for i in range(len(points) - 1):
        lines = {}
        for j in range(i + 1, len(points)):
            slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) if points[i][0] != points[j][0] else float("inf")
            lines[slope] = lines.get(slope, 0) + 1
            ans = max(ans, lines[slope])
    return ans + 1


print(maxPoints([[0,0]]))  # 1
print(maxPoints([[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]]))  # 3
print(maxPoints([[-6, -1], [3, 1], [12, 3]]))  # 3
print(maxPoints([[1, 2], [2, 2], [3, 2], [0, 0]]))  # 3
print(maxPoints([[1, 1], [1, 2], [1, 4], [3, 3]]))  # 3
print(maxPoints([[1, 1], [2, 2], [3, 3]]))  # 3
print(maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
