from sortedcontainers import SortedSet


def overlap(interval_1, interval_2):
    return interval_1[0] <= interval_2[1] and interval_2[0] <= interval_1[1]


class CountIntervals:
    def __init__(self):
        self.sorted_set = SortedSet()
        self.num_counter = 0

    def add(self, left, right):
        new_interval = (left, right)
        i = self.sorted_set.bisect_left(new_interval)
        if i > 0 and overlap(new_interval, self.sorted_set[i - 1]):
            i = i - 1
        while i < len(self.sorted_set) and overlap(new_interval, self.sorted_set[i]):
            existing_interval = self.sorted_set[i]
            self.num_counter -= (existing_interval[1] - existing_interval[0] + 1)
            new_interval = (min(new_interval[0], existing_interval[0]), max(new_interval[1], existing_interval[1]))
            self.sorted_set.pop(i)
        self.sorted_set.add(new_interval)
        self.num_counter += (new_interval[1] - new_interval[0] + 1)

    def count(self):
        return self.num_counter


obj = CountIntervals()
obj.add(2, 3)
obj.add(7, 10)
print(obj.count())  # 6
obj.add(5, 8)
print(obj.count())  # 8
