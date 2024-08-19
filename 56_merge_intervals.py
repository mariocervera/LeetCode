def merge(intervals):
    n = len(intervals)
    if n == 1:
        return intervals
    intervals.sort()
    res = []
    i = 0
    for j in range(n):
        if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], intervals[j][1])
        else:
            res.append(intervals[i])
            i = j
    res.append(intervals[i])
    return res

print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1, 4], [4, 5]]))  # [[1,5]]
print(merge([[1, 4], [1, 4]]))  # [[1,4]]
print(merge([[0, 4], [1, 4]]))  # [[0,4]]
print(merge([[0, 4]]))  # [[0,4]]
print(merge([[1, 4], [2, 3]]))  # [[1,4]]
