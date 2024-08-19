
def threeSum(nums):
    nums.sort()
    i, res = 0, []
    while i < len(nums)-2:
        target = -nums[i]
        j, k = i+1, len(nums)-1
        while j < k:
            _sum = nums[j]+nums[k]
            if _sum == target:
                res.append([nums[i], nums[j], nums[k]])
            if _sum <= target:
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
            else:
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        i += 1
        while i < len(nums)-2 and nums[i] == nums[i-1]:
            i += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(threeSum([0, 0, 0]))  # [[0,0,0]]
print(threeSum([0, 1, 1]))  # []
print(threeSum([1, 2, -2, -1]))  # []
