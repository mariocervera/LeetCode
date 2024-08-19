
def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def numberOfBoomerangs(points):
    res = 0
    for p1 in points:
        distances = {}
        for p2 in points:
            distance = get_distance(p1, p2)
            distances[distance] = distances.get(distance, 0) + 1
        for v in distances.values():
            res += v * (v-1)
    return res


print(numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))  # 2
print(numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))  # 2
print(numberOfBoomerangs([[1, 1]]))  # 0
