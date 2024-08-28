import heapq

mod = 10 ** 9 + 7

def fast_pow(base, exp):
    if exp == 0:
        return 1
    square = fast_pow(base, exp//2) ** 2
    return square if exp % 2 == 0 else square * base


def getFinalState(nums, k, multiplier):
    if multiplier == 1:
        return nums
    pq, max_num, n = [], -1, len(nums)
    for i, num in enumerate(nums):
        heapq.heappush(pq, (num, i))
        max_num = max(max_num, num)
    while True:
        num, i = heapq.heappop(pq)
        original_num = num
        nums[i] = num * multiplier
        heapq.heappush(pq, (nums[i], i))
        k -= 1
        if k == 0:
            return [num % mod for num in nums]
        if original_num == max_num:
            break
    c = k // n
    r = k % n
    j = 0
    while pq and k:
        num, i = heapq.heappop(pq)
        nums[i] = (num * fast_pow(multiplier, c + (1 if j < r else 0))) % mod
        k -= 1
        j += 1
    return nums


print(getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))  # [8,4,6,5,6]
print(getFinalState(nums=[100000, 2000], k=2, multiplier=1000000))  # [999999307,999999993]
print(getFinalState(nums=[2,1], k=3, multiplier=10))  # [20,100]
