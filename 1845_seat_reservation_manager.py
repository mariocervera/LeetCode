import heapq

class SeatManager:
    def __init__(self, n):
        self.last = 0
        self.pq = []

    def reserve(self):
        if not self.pq:
            self.last += 1
            return self.last
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber):
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.pq, seatNumber)


sm = SeatManager(5)
print(sm.reserve())  # 1
print(sm.reserve())  # 2
sm.unreserve(2)
print(sm.reserve())  # 2
print(sm.reserve())  # 3
print(sm.reserve())  # 4
print(sm.reserve())  # 5
sm.unreserve(5)
