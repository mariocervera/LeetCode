import heapq

def getFinalState(nums, k, multiplier):
    tuples_arr = [(nums[i], i) for i in range(len(nums))]
    heapq.heapify(tuples_arr)
    for _ in range(k):
        num, i = heapq.heappop(tuples_arr)
        nums[i] = num * multiplier
        heapq.heappush(tuples_arr, (nums[i], i))
    return nums


print(getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))  # [8,4,6,5,6]
print(getFinalState(nums=[1, 2], k=3, multiplier=4))  # [16,8]
