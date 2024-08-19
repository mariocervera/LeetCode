import math


class Point:
    def __init__(self, x, y, ref_point=None):
        self.x = x
        self.y = y
        self.ref_p = ref_point

    def __str__(self):
        return f"({self.x},{self.y})"

    def __lt__(self, other):
        if not self.ref_p:
            return True
        if not other.ref_p:
            return False
        if self.orientation(other) == 1:
            return True
        if self.orientation(other) == -1:
            return False
        return self.distance_to_ref() < other.distance_to_ref()

    def orientation(self, other):
        cp = self.cross_product(other)
        if cp > 0:
            return 1  # Counterclockwise (left turn)
        elif cp < 0:
            return -1  # Clockwise (right turn)
        else:
            return 0  # Collinear

    def cross_product(self, other):
        return (((self.x - self.ref_p.x) * (other.y - self.ref_p.y)) -
                ((other.x - self.ref_p.x) * (self.y - self.ref_p.y)))

    def distance_to_ref(self):
        return math.sqrt((self.ref_p.x - self.x) ** 2 + (self.ref_p.y - self.y) ** 2)


def get_orientation(p1, p2, p_ref):
    ref_point = Point(p_ref[0], p_ref[1])
    _orientation = Point(p1[0], p1[1], ref_point).orientation(Point(p2[0], p2[1], ref_point))
    return _orientation


def outerTrees(trees):
    n = len(trees)
    if n < 4:
        return trees

    # Select point with lowest y coordinate. Break ties with x coordinate.
    lowest_p = trees[0]
    i_lowest_p = 0
    for i, tree in enumerate(trees):
        if (tree[1], tree[0]) < (lowest_p[1], lowest_p[0]):
            lowest_p = tree
            i_lowest_p = i

    tree_points = [
        Point(tree[0], tree[1], Point(lowest_p[0], lowest_p[1])) if i != i_lowest_p else Point(tree[0], tree[1])
        for i, tree in enumerate(trees)
    ]
    tree_points.sort()

    # Reverse last points that are collinear
    i = n-2
    while i > 0 and tree_points[i].orientation(tree_points[-1]) == 0:
        i -= 1
    tree_points = tree_points[:i+1] + (tree_points[i+1:])[::-1]

    convex_hull = [[tree_points[0].x, tree_points[0].y],
                   [tree_points[1].x, tree_points[1].y],
                   [tree_points[2].x, tree_points[2].y]]
    for i in range(3, n):
        while len(convex_hull) > 1 and get_orientation([tree_points[i].x, tree_points[i].y], convex_hull[-2], convex_hull[-1]) not in (0, 1):
            convex_hull.pop()
        convex_hull.append([tree_points[i].x, tree_points[i].y])

    return convex_hull



# [[4,5],[2,5],[6,1],[3,5],[2,1],[1,4],[1,2],[7,4],[7,3],[7,2],[3,0],[0,3],[5,0],[5,5],[4,0],[6,5]]
print(outerTrees([[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]))

print(outerTrees([[3,3],[4,2],[2,1],[3,5],[1,2],[5,2]]))  # [[2,1],[5,2],[3,5],[1,2]]
print(outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))  # [[1,1],[2,0],[4,2],[3,3],[2,4]]
print(outerTrees([[1, 2], [2, 2], [4, 2]]))  # [[1,2],[2,2],[4,2]]
print(outerTrees([[1,2],[2,2],[4,2],[5,2],[6,2],[7,2]])) # [[1,2],[7,2],[6,2],[5,2],[4,2],[2,2]]
