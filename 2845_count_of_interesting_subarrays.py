from collections import defaultdict

def countInterestingSubarrays(nums, modulo, k):
    binary_arr = [1 if num % modulo == k else 0 for num in nums]
    res, prefix_sum, sum_freqs = 0, 0, defaultdict(int)
    sum_freqs[0] = 1
    for b in binary_arr:
        prefix_sum = (prefix_sum + b) % modulo
        res += sum_freqs[(prefix_sum - k) % modulo]
        sum_freqs[prefix_sum] += 1
    return res


print(countInterestingSubarrays(nums=[3, 2, 4], modulo=2, k=1))  # 3
print(countInterestingSubarrays(nums=[3, 1, 9, 6], modulo=3, k=0))  # 2
print(countInterestingSubarrays(nums=[1,9,6,1], modulo=2, k=1))  # 6



