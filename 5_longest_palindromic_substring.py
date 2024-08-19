
def longestPalindrome(s):
    n, max_pair = len(s), (0, 0)

    def tryToExtend(low, high):
        nonlocal max_pair
        while 0 <= low <= high < n:
            if s[low] != s[high]:
                break
            if high-low > max_pair[1]-max_pair[0]:
                max_pair = (low, high)
            low, high = low - 1, high + 1

    for i in range(n-1):
        tryToExtend(i, i)
        tryToExtend(i, i+1)

    return s[max_pair[0]:max_pair[1] + 1]

'''
def longestPalindrome(s):
    n, max_pair = len(s), (0, 0)
    dp = [[False for _ in range(n)] for _ in range(n)]

    # Size 1
    for i in range(n):
        dp[i][i] = True

    # Size [2-n]
    for k in range(2, n+1):
        for i in range(n - k + 1):
            dp[i][i+k-1] = s[i] == s[i+k-1] and (k == 2 or dp[i+1][i+k-2])
            if dp[i][i+k-1]:
                max_pair = (i, i+k-1)

    return s[max_pair[0]:max_pair[1]+1]
'''


print(longestPalindrome("bb"))  # "bb"
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))  # "bb"
print(longestPalindrome("c"))  # "c"
print(longestPalindrome("reconocer"))  # "reconocer"
print(longestPalindrome("asreconoceriubg"))  # "reconocer"
