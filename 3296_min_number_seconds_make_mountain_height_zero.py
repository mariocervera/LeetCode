import heapq


class Worker:
    def __init__(self, time):
        self.time = time
        self.penalty = 1
        self.accumulated_seconds = 0

    def __lt__(self, other):
        return self.accumulated_seconds + self.time * self.penalty < other.accumulated_seconds + other.time * other.penalty


def minNumberOfSeconds(mountainHeight, workerTimes):
    pq = [Worker(workerTime) for workerTime in workerTimes]
    heapq.heapify(pq)
    res = float("-inf")
    while mountainHeight > 0:
        current_worker = heapq.heappop(pq)
        current_worker.accumulated_seconds += current_worker.time * current_worker.penalty
        current_worker.penalty += 1
        heapq.heappush(pq, current_worker)
        mountainHeight -= 1
        res = max(res, current_worker.accumulated_seconds)
    return res


print(minNumberOfSeconds(mountainHeight=4, workerTimes=[2, 1, 1]))  # 3
print(minNumberOfSeconds(mountainHeight=10, workerTimes=[3, 2, 2, 4]))  # 12
print(minNumberOfSeconds(mountainHeight=5, workerTimes=[1]))  # 15
print(minNumberOfSeconds(mountainHeight=5, workerTimes=[1, 7]))  # 10
