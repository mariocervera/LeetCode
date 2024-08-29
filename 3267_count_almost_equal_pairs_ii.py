from collections import Counter

def can_make_equal(arr_1, arr_2):
    d = {}
    for i in range(len(arr_1)):
        n1, n2 = arr_1[i], arr_2[i]
        if (n1 in d and d[n1] != n2) or (n2 in d and d[n2] != n1):
            return False
        d[n1] = n2
        d[n2] = n1
    return True


def are_almost_equal(s1, s2):
    diff_digits_1, diff_digits_2 = [], []
    for i in range(len(s1)):
        d1, d2 = s1[i], s2[i]
        if d1 != d2:
            diff_digits_1.append(d1)
            diff_digits_2.append(d2)
    if len(diff_digits_1) > 4 or sorted(diff_digits_1) != sorted(diff_digits_2):
        return False
    return len(diff_digits_1) <= 3 or \
        len(diff_digits_1) > len(set(diff_digits_1)) or \
        can_make_equal(diff_digits_1, diff_digits_2)


def countPairs(nums):
    counters = Counter(nums)
    nums = list(set(nums))
    n = len(nums)
    strs = [str(num) for num in nums]
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s1, s2 = (strs[i], strs[j]) if len(strs[i]) <= len(strs[j]) else (strs[j], strs[i])
            len_diff = len(s2) - len(s1)
            if are_almost_equal("0" * len_diff + s1, s2):
                res += (counters[int(s1)] * counters[int(s2)])
    for k, v in counters.items():
        res += ((v * (v-1)) // 2)
    return res


print(countPairs([1023, 2310, 2130, 213]))  # 4
print(countPairs([1, 10, 100]))  # 3
print(countPairs(
    [4837, 8223, 3487, 3822, 8223, 7032, 172, 8232, 8678, 3758, 2588, 6734, 4301, 2823, 721, 172, 3647, 4031, 3746,
     8232, 6041, 6878, 3282, 3282, 7809, 7023, 3118, 721, 3822, 8852, 2823, 5927, 2823, 8734, 8223, 3822, 3228, 2832,
     2328, 8322, 8322, 3282, 3746, 172, 4310, 3282, 8473, 3822, 4031, 2382, 3764, 4031, 7230, 2382, 5376, 3822, 8232,
     2283, 3282, 3228, 8322, 172, 3282, 8232, 2283, 3746, 2238, 8232, 2328, 7780, 2823, 3476, 8232, 2382, 8223, 2283,
     2283, 8223]))  # 916
