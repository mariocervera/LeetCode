def triangleNumber(nums):
    nums.sort()
    n, res = len(nums), 0
    for i in range(n - 2):
        if nums[i] > 0:
            p = i + 2
            for j in range(i + 1, n - 1):
                _sum = nums[i] + nums[j]
                while p < n and nums[p] < _sum:
                    p += 1
                res += (p - j - 1)
    return res


print(triangleNumber([2, 2, 3, 4]))  # 3
print(triangleNumber([4, 2, 3, 4]))  # 4
