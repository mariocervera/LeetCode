from collections import Counter

def numSplits(s):
    left, right = {}, Counter(s)
    res = 0
    for c in s:
        left[c] = left.get(c, 0) + 1
        right[c] -= 1
        if right[c] == 0:
            del right[c]
        if len(left) == len(right):
            res += 1
    return res


print(numSplits("aacaba"))  # 2
print(numSplits("abcd"))  # 1
print(numSplits("aaaaa"))  # 4
print(numSplits("acbadbaada"))  # 2

