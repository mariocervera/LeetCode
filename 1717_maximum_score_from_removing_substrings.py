
def maximumGain(s, x, y):
    res = 0
    points_low, points_high, substr_low, substr_high = (x, y, "ab", "ba") if x < y else (y, x, "ba", "ab")

    stack = []
    for c in s:
        stack.append(c)
        if len(stack) > 1 and (stack[-2] + stack[-1]) == substr_high:
            res += points_high
            stack.pop()
            stack.pop()

    stack2 = []
    for c in stack:
        stack2.append(c)
        if len(stack2) > 1 and (stack2[-2] + stack2[-1]) == substr_low:
            res += points_low
            stack2.pop()
            stack2.pop()

    return res

print(maximumGain(s="aabbab", x=1, y=4))  # 6
print(maximumGain(s="cdbcbbaaabab", x=4, y=5))  # 19
print(maximumGain(s="aabbaaxybbaabb", x=5, y=4))  # 20
