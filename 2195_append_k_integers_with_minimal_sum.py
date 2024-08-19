
def minimalKSum(nums, k):
    nums = list(set(nums))
    i, n = 0, len(nums)
    nums.sort()
    first_int, last_int = 1, k
    res = 0
    while True:
        extra_nums_count = 0
        total = last_int - first_int + 1
        res += total * (first_int + last_int) // 2
        while i < n and nums[i] <= last_int:
            res -= nums[i]
            extra_nums_count += 1
            i += 1
        if not extra_nums_count:
            break
        first_int, last_int = (last_int + 1), (last_int + extra_nums_count)
    return res


print(minimalKSum(nums=[1, 4, 25, 10], k=2))  # 5
print(minimalKSum(nums=[1, 4, 25, 10, 25], k=2))  # 5
print(minimalKSum(nums=[5, 6], k=6))  # 25
print(minimalKSum(nums=[5, 5, 6], k=6))  # 25
print(minimalKSum(nums=[1, 3, 5], k=3))  # 12

