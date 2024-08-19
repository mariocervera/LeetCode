
def maxDotProduct(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[float("-inf") for _ in range(n)] for _ in range(m)]
    dp[0][0] = nums1[0] * nums2[0]
    for i in range(1, m):
        dp[i][0] = max(dp[i-1][0], nums1[i] * nums2[0])
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], nums1[0] * nums2[j])
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(
                max(dp[i-1][j-1], 0) + nums1[i] * nums2[j],
                dp[i-1][j-1],
                dp[i-1][j],
                dp[i][j-1]
            )
    return dp[m-1][n-1]


print(maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))  # 18
print(maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]))  # 21
print(maxDotProduct(nums1=[-1, -1], nums2=[1, 1]))  # -1
