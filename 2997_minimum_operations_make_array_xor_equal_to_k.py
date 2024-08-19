
def minOperations(nums, k):
    xor = 0
    for num in nums:
        xor ^= num
    xor ^= k
    res = 0
    while xor:
        res += (xor & 1)
        xor >>= 1
    return res


print(minOperations(nums=[2, 1, 3, 4], k=1))  # 2
print(minOperations(nums=[2, 0, 2, 0], k=0))  # 0
