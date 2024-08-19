def lengthOfLongestSubstring(s):
    indexes = {}
    i, best = 0, -1
    for j, c in enumerate(s):
        if c in indexes and indexes[c] >= i:
            i = indexes[c]+1
        indexes[c] = j
        best = max(best, j-i+1)
    return best



print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring("abba"))  # 2


