
def nearestValidPoint(x, y, points):
    res, min_distance = -1, float("inf")
    for i, (px, py) in enumerate(points):
        if x != px and y != py:
            continue
        dist = abs(x - px) + abs(y - py)
        if dist < min_distance:
            min_distance = dist
            res = i
    return res


print(nearestValidPoint(x=3,
                        y=4,
                        points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))  # 2

print(nearestValidPoint(x=3,
                        y=4,
                        points=[[3, 4]]))  # 0

print(nearestValidPoint(x=3,
                        y=4,
                        points=[[2, 3]]))  # -1
