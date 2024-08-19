
def wordBreak(s, wordDict):
    n = len(s)
    ht = set(wordDict)
    dp = [False] * (n+1)
    dp[0] = True

    for j in range(n):
        for i in range(j+1):
            sliced_s = s[i:j+1]
            if sliced_s in ht and dp[i]:
                dp[j+1] = True
                break

    return dp[n]


print(wordBreak(s="leetcode", wordDict=["leet", "code"]))  # True
print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # True
print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # False
