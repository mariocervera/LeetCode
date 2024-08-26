def are_almost_equal(s1, s2):
    diff_digits_1, diff_digits_2 = [], []
    for i in range(len(s1)):
        d1, d2 = s1[i], s2[i]
        if d1 != d2:
            diff_digits_1.append(d1)
            diff_digits_2.append(d2)
    return len(diff_digits_1) <= 2 and sorted(diff_digits_1) == sorted(diff_digits_2)


def countPairs(nums):
    n = len(nums)
    strs = [str(num) for num in nums]
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s1, s2 = (strs[i], strs[j]) if len(strs[i]) <= len(strs[j]) else (strs[j], strs[i])
            len_diff = len(s2) - len(s1)
            if are_almost_equal("0" * len_diff + s1, s2):
                res += 1
    return res


print(countPairs([3, 12, 30, 17, 21]))  # 2
print(countPairs([1, 1, 1, 1, 1]))  # 10
print(countPairs([123, 231]))  # 0
print(countPairs(
    [886595, 767627, 6691, 593887, 857750, 919155, 830918, 593887, 593788, 593788, 660078, 598873, 310196, 668007,
     597883, 983587, 897853, 668700, 435383, 953887, 631608, 897853, 953887, 240754, 593887, 597883, 455127, 627877,
     643862, 660087, 893587, 129173, 228736, 627877, 775850, 875750, 50701, 830255, 751, 729113, 684778, 114586, 154186,
     593887, 668700, 238726]))  # 59
