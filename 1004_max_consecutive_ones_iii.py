
def longestOnes(nums, k):
    i, n, max_1s_len = 0, len(nums),  float("-inf")
    for j in range(n):
        if nums[j] == 0:
            if k > 0:
                k -= 1
            else:
                while i < j and nums[i] == 1:
                    i += 1
                i += 1
        max_1s_len = max(max_1s_len, j-i+1)
    return max_1s_len


# [1,1,1,0,0,1,1,1,1,1,1]
print(longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))  # 6

# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
print(longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))  # 10
