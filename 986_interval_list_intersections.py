
def are_overlapping(interval_i, interval_j):
    return interval_i[0] <= interval_j[0] <= interval_i[1] or interval_j[0] <= interval_i[0] <= interval_j[1]

def intervalIntersection(firstList, secondList):
    m, n = len(firstList), len(secondList)
    i, j, k = 0, 0, 0
    res = []
    while i < m and j < n:
        interval_i, interval_j = firstList[i], secondList[j]
        if are_overlapping(interval_i, interval_j):
            low = max(interval_i[0], interval_j[0])
            high = min(interval_i[1], interval_j[1])
            res.append([low, high])
        if interval_i[1] <= interval_j[1]:
            i += 1
        if interval_j[1] <= interval_i[1]:
            j += 1
    return res


# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
print(intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                           secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

# []
print(intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]))
