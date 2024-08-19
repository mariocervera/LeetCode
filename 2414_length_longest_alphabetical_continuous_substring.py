
def longestContinuousSubstring(s):
    current_len, max_len = 1, 1
    for i in range(1, len(s)):
        current_len = current_len + 1 if ord(s[i]) == ord(s[i-1]) + 1 else 1
        max_len = max(max_len, current_len)
    return max_len


print(longestContinuousSubstring("abacaba"))  # 2
print(longestContinuousSubstring("abcde"))  # 5
