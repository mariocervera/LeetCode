from collections import Counter

mod = 10 ** 9 + 7


def reverse_number(n):
    return int(str(n)[::-1])


def countNicePairs(nums):
    diffs_counter = Counter([num - reverse_number(num) for num in nums])
    res = 0
    for v in diffs_counter.values():
        res += ((v * (v - 1)) // 2)
    return res % mod


# Alternative solution

# def countNicePairs(nums):
#     res = 0
#     diffs = defaultdict(int)
#     for num in nums:
#         diff = num - reverse_number(num)
#         res += diffs[diff]
#         diffs[diff] += 1
#     return res % mod


# Alternative solution (one line)

#def countNicePairs(nums):
#    return sum([((v * (v - 1)) // 2) for v in Counter([num - int(str(num)[::-1]) for num in nums]).values()]) % (10 ** 9 + 7)


print(countNicePairs([42, 11, 1, 97]))  # 2
print(countNicePairs([13, 10, 35, 24, 76]))  # 4
