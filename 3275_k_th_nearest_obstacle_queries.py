import heapq


def dist(query):
    return abs(query[0]) + abs(query[1])


def resultsArray(queries, k):
    n = len(queries)
    if n < k:
        return [-1] * n
    max_heap = [dist(queries[i]) * -1 for i in range(k-1)]
    heapq.heapify(max_heap)
    res = [-1] * (k-1)
    for i in range(k-1, n):
        d = dist(queries[i])
        if len(max_heap) < k or d < (max_heap[0] * -1):
            heapq.heappush(max_heap, d * -1)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
        res.append(max_heap[0] * -1)
    return res


print(resultsArray(queries=[[1, 2], [3, 4], [2, 3], [-3, 0]],k=2))  # [-1,7,5,3]
print(resultsArray(queries=[[5, 5], [4, 4], [3, 3]], k=1))  # [10,8,6]
