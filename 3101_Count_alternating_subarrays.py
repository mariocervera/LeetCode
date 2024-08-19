
def countAlternatingSubarrays(nums):
    res, streak_len, last_bit = 0, 0, None
    for bit in nums:
        if last_bit is None or last_bit != bit:
            streak_len += 1
        else:
            res += streak_len * (streak_len + 1) // 2
            streak_len = 1
        last_bit = bit
    res += streak_len * (streak_len + 1) // 2
    return res


print(countAlternatingSubarrays([0]))  # 1
print(countAlternatingSubarrays([0, 1, 1, 1]))  # 5
print(countAlternatingSubarrays([1, 0, 1, 0]))  # 10
