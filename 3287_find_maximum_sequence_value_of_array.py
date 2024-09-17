
def combinations(nums, k):
    n = len(nums)
    dp = [[None for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = {0}
    or_k_choose_k = nums[0]
    for i in range(1, k+1):
        or_k_choose_k |= nums[i-1]
        dp[i][i] = {or_k_choose_k}
    for i in range(2, n+1):
        for j in range(1, min(i, k+1)):
            dp[i][j] = dp[i-1][j].copy()
            for _or in dp[i-1][j-1]:
                dp[i][j].add(_or | nums[i-1])
    return dp



def maxValue(nums, k):
    n = len(nums)
    preffix = combinations(nums, k)
    suffix = combinations(nums[::-1], k)
    res = float("-inf")
    for i in range(k, n-k+1):
        for or_1 in preffix[i][k]:
            for or_2 in suffix[n-i][k]:
                res = max(res, or_1 ^ or_2)
    return res



print(maxValue(nums=[2, 6, 7], k=1))  # 5
print(maxValue(nums=[4, 2, 5, 6, 7], k=2))  # 2
print(maxValue(nums=[15, 97, 31, 53], k=1))  # 126
print(maxValue(nums=[8, 114, 123, 82], k=1))  # 122
