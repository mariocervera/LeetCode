
def maxRotateFunction(nums):
    n = len(nums)
    arr_sum = sum(nums)
    res = func_i = sum([i * nums[i] for i in range(1, n)])
    last = n-1
    for _ in range(n-1):
        func_i = func_i + arr_sum - (n * nums[last])
        res = max(res, func_i)
        last = (last-1) if last > 0 else n-1
    return res


print(maxRotateFunction([4, 3, 2, 6]))  # 26
print(maxRotateFunction([100]))  # 0
