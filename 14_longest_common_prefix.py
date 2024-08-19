
def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    s1, s2 = strs[0], strs[-1]
    i, n = 0, min(len(s1), len(s2))
    while i < n and s1[i] == s2[i]:
        i += 1
    return s1[:i]


print(longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # ""
print(longestCommonPrefix(["", "b"]))  # ""
print(longestCommonPrefix(["c", "acc", "ccc"]))  # ""
