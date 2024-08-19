
def findMinArrowShots(points):
    points.sort()
    arrows, i = 1, 0
    for j in range(1, len(points)):
        if points[j][0] <= points[i][1]:  # Intersect
            points[i][0] = points[j][0]
            points[i][1] = min(points[i][1], points[j][1])
        else:
            i = j
            arrows += 1
    return arrows


print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
print(findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
print(findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
