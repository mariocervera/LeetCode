

def insert(intervals, new_interval):
    n = len(intervals)
    i, j = 0, n-1
    while i < n and intervals[i][1] < new_interval[0]:
        i += 1
    while j >= 0 and intervals[j][0] > new_interval[1]:
        j -= 1
    left = intervals[:i]
    right = intervals[j+1:]
    merged = [
        min(intervals[i][0] if 0 <= i < n else float("inf"), new_interval[0]),
        max(intervals[j][1] if 0 <= j < n else float("-inf"), new_interval[1])
    ]
    return left + [merged] + right




print(insert([[1, 3], [6, 9]], [4, 5]))  # [[1,3], [4,5], [6,9]]
print(insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5], [6,9]]
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1,2], [3,10], [12,16]]
print(insert([[1, 5]], [2, 3]))  # [[1,5]]
print(insert([[2, 5], [6, 7], [8, 9]], [0, 1]))  # [[0,1],[2,5],[6,7],[8,9]]
print(insert([[1, 5]], [6, 8]))  # [[1,5], [6,8]]
print(insert([[1, 5]], [2, 7]))  # [[1,7]]
