
def minBitwiseArray(nums):
    res = []
    for num in nums:
        for i in range(num):
            if i | (i+1) == num:
                res.append(i)
                break
        else:
            res.append(-1)
    return res


print(minBitwiseArray([2, 3, 5, 7]))  # [-1,1,4,3]
print(minBitwiseArray([11, 13, 31]))  # [9,12,15]
