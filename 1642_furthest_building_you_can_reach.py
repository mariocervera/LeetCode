import heapq


def furthestBuilding(heights, bricks, ladders):
    n = len(heights)
    gaps_pq = []
    i = 0
    while i < n-1:
        while i < n-1 and heights[i + 1] <= heights[i]:
            i += 1
        if i == n-1:
            break
        gap = heights[i + 1] - heights[i]
        if ladders > 0:
            ladders -= 1
            heapq.heappush(gaps_pq, gap)
        elif len(gaps_pq) == 0 or gaps_pq[0] >= gap:
            if bricks < gap:
                return i
            bricks -= gap
        else:
            smaller_gap = heapq.heappop(gaps_pq)
            if bricks < smaller_gap:
                return i
            heapq.heappush(gaps_pq, gap)
            bricks -= smaller_gap
        i += 1
    return n - 1


print(furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))  # 4
print(furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))  # 7
print(furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0))  # 3
