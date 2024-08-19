
import ctypes

def singleNumber(nums):
    res = 0
    for i in range(32):
        counter = 0
        for num in nums:
            counter += num >> i & 1
        if counter % 3 != 0:
            res |= 1 << i
    return res if not res & (1 << 31) else -(~res+1 & 0xffffffff)


print(singleNumber([-2, -2, -3, -2]))  # -3
print(singleNumber([2, 2, 3, 2]))  # 3
print(singleNumber([2, 2, 3, 2, 5, 5, 5]))  # 3
print(singleNumber([0, 1, 0, 1, 0, 1, 99]))  # 99
print(singleNumber([30000,500,100,30000,100,30000,100]))  # 500
