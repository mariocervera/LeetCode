from collections import Counter


def gcdValues(nums, queries):
    nums_counts = Counter(nums)
    low, high = 1, max(nums)
    gcds_nums = [0] * (high+1)
    for divisor in range(low, high+1):
        i = 1
        while divisor * i <= high:
            if divisor * i in nums_counts:
                gcds_nums[divisor] += nums_counts[divisor * i]
            i += 1
    gcds_pairs = [0] * (high+1)
    for gcd in range(high, 0, -1):
        gcds_pairs[gcd] = (gcds_nums[gcd] * (gcds_nums[gcd]-1)) // 2
        for multiple in range(2 * gcd, high + 1, gcd):
            gcds_pairs[gcd] -= gcds_pairs[multiple]
    prefix_sum = [0] * (high+1)
    for i in range(1, high+1):
        prefix_sum[i] = prefix_sum[i-1] + gcds_pairs[i]
    res = []
    for query in queries:
        left, right = 0, high
        while left < right:
            mid = (left+right) // 2 + 1
            if prefix_sum[mid] <= query:
                left = mid
            else:
                right = mid - 1
        res.append(left+1)
    return res


print(gcdValues(nums=[2, 3, 4], queries=[0, 2, 2]))  # [1,2,2]
print(gcdValues(nums=[4, 4, 2, 1], queries=[5, 3, 1, 0]))  # [4,2,1,1]
print(gcdValues(nums=[2, 2], queries=[0, 0]))  # [2,2]
