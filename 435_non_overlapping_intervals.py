
def eraseOverlapIntervals(intervals):
    intervals.sort()
    res = 0
    high = float("-inf")
    for x, y in intervals:
        if high <= x:
            high = y
        else:
            high = min(high, y)
            res += 1
    return res


print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # 2
print(eraseOverlapIntervals([[1, 2], [2, 3]]))  # 0
