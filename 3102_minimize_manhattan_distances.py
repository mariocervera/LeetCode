
def get_distance(points, i, j):
    return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])


def get_max_distance(points, remove=-1):
    min_sum, max_sum, min_sum_index, max_sum_index = float("inf"), float("-inf"), -1, -1
    min_diff, max_diff, min_diff_index, max_diff_index = float("inf"), float("-inf"), -1, -1
    for i, point in enumerate(points):
        if i != remove:
            _sum = point[0] + point[1]
            diff = point[0] - point[1]
            if _sum < min_sum:
                min_sum_index = i
                min_sum = _sum
            if _sum > max_sum:
                max_sum_index = i
                max_sum = _sum
            if diff < min_diff:
                min_diff_index = i
                min_diff = diff
            if diff > max_diff:
                max_diff_index = i
                max_diff = diff
    if max(max_sum - min_sum, max_diff - min_diff) == max_sum - min_sum:
        return max_sum_index, min_sum_index
    return max_diff_index, min_diff_index


def minimumDistance(points):
    max_dist_p1_index, max_dist_p2_index = get_max_distance(points)
    return min(
        get_distance(points, *get_max_distance(points, max_dist_p1_index)),
        get_distance(points, *get_max_distance(points, max_dist_p2_index))
    )



print(minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]))  # 12
print(minimumDistance([[1, 1], [1, 1], [1, 1]]))  # 0
print(minimumDistance([[9, 8], [1, 8], [3, 1], [9, 1], [7, 7], [3, 6]]))  # 13
print(minimumDistance([[7, 7], [9, 3], [8, 1], [8, 8], [8, 9], [5, 1], [3, 2], [6, 9], [3, 6]]))  # 11
