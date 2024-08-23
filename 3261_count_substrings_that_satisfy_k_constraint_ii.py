
def countKConstraintSubstrings(s, k, queries):
    n = len(s)
    left_to_right, right_to_left = [0] * n, [0] * n
    counters = {"0": 0, "1": 0}
    l = 0
    for r in range(n):
        counters[s[r]] += 1
        while counters["0"] > k and counters["1"] > k:
            counters[s[l]] -= 1
            l += 1
        right_to_left[r] = l
    counters = {"0": 0, "1": 0}
    r = n-1
    for l in range(n-1, -1, -1):
        counters[s[l]] += 1
        while counters["0"] > k and counters["1"] > k:
            counters[s[r]] -= 1
            r -= 1
        left_to_right[l] = r
    pref_sum = [0] * n
    for r in range(n):
        pref_sum[r] = r - right_to_left[r] + 1 + (pref_sum[r-1] if r > 0 else 0)
    res = []
    for left_bound, right_bound in queries:
        min_right = min(right_bound, left_to_right[left_bound])
        length = min_right - left_bound + 1
        _sum = length * (length + 1) // 2
        if min_right < right_bound:
            _sum = _sum + pref_sum[right_bound] - pref_sum[min_right]
        res.append(_sum)
    return res


print(countKConstraintSubstrings(s="0001111",
                                 k=2,
                                 queries=[[0, 6]]))  # [26]

print(countKConstraintSubstrings(s="010101",
                                 k=1,
                                 queries=[[0, 5], [1, 4], [2, 3]]))  # [15,9,3]

print(countKConstraintSubstrings(s="000",
                                 k=1,
                                 queries=[[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]]))  # [1,3,6,1,3,1]
