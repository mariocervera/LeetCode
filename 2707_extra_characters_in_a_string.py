

def minExtraChar(s, dictionary):
    n, ht = len(s), set(dictionary)
    dp = [-1] * n
    dp[0] = 0 if s[0] in ht else 1
    for i in range(1, n):
        min_extra_chars = float("inf")
        for word in dictionary:
            wlen = len(word)
            if i-wlen+1 >= 0 and s[i-wlen+1:i+1] in ht:
                min_extra_chars = min(min_extra_chars, dp[i-wlen] if i-wlen >= 0 else 0)
        dp[i] = min(dp[i-1]+1, min_extra_chars)
    return dp[n-1]

print(minExtraChar(s="leetscode", dictionary=["leet", "code", "leetcode"]))  # 1
print(minExtraChar(s="sayhelloworld", dictionary=["hello", "world"]))  # 3
