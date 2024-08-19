from collections import defaultdict

def subarraySum(nums, k):
    sum_frequencies = defaultdict(int)
    sum_frequencies[0] = 1
    res, current_sum = 0, 0
    for num in nums:
        current_sum += num
        if current_sum-k in sum_frequencies:
            res += sum_frequencies[current_sum-k]
        sum_frequencies[current_sum] += 1
    return res



print(subarraySum(nums=[1, 1, 1], k=2))  # 2
print(subarraySum(nums=[1, 2, 3], k=3))  # 2
