
def digits_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def minElement(nums):
    res = float("inf")
    for num in nums:
        res = min(res, digits_sum(num))
    return res


print(minElement([10, 12, 13, 14]))  # 1
print(minElement([1, 2, 3, 4]))  # 1
print(minElement([999, 19, 199]))  # 10
