import random


class Solution:
    def __init__(self, w):
        self.weight_sums = []
        weight_sum = 0
        for weight in w:
            weight_sum += weight
            self.weight_sums.append(weight_sum)

    def pickIndex(self):
        random_num = random.randint(1, self.weight_sums[-1])
        return self.lower_bound_binary_search(random_num)

    def lower_bound_binary_search(self, target):
        low, high = 0, len(self.weight_sums) - 1
        while low < high:
            mid = (low+high)//2
            if self.weight_sums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
