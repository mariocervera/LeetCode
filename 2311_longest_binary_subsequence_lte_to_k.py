
def longestSubsequence(s, k):
    n = len(s)
    bin_num, acc = 0, 1
    res = 0
    for i in range(n-1, -1, -1):
        if s[i] == "0":
            res += 1
        else:
            bin_num += acc
            if bin_num <= k:
                res += 1
        acc <<= 1
    return res


print(longestSubsequence(s="1001010", k=5))  # 5
print(longestSubsequence(s="00101001", k=1))  # 6
