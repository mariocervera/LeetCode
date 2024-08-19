import heapq
from collections import deque

def smallestRange(nums):
    k = len(nums)
    nums_pq = [(num, i) for i in range(k) for num in nums[i]]
    heapq.heapify(nums_pq)
    window, window_counters = deque(), {}
    res = [float("-inf"), float("inf")]
    while nums_pq:
        window.append(heapq.heappop(nums_pq))
        window_counters[window[-1][1]] = window_counters.get(window[-1][1], 0) + 1
        while len(window_counters) >= k and window_counters[window[0][1]] > 1:
            window_counters[window[0][1]] -= 1
            window.popleft()
        if len(window_counters) >= k and window[-1][0] - window[0][0] < res[1] - res[0]:
            res = [window[0][0], window[-1][0]]
    return res


print(smallestRange([[4, 10, 15, 24, 26],
                     [0, 9, 12, 20],
                     [5, 18, 22, 30]]))  # [20, 24]

print(smallestRange([[1, 2, 3],
                     [1, 2, 3],
                     [1, 2, 3]]))  # [1, 1]

print(smallestRange([[2]]))  # [2, 2]
