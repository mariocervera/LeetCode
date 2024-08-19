
def canJump(nums):
    i, can_reach, n = 0, 0, len(nums)
    while i < len(nums) and i <= can_reach:
        can_reach = max(can_reach, i + nums[i])
        i += 1
    return i == n

print(canJump([2, 3, 1, 1, 4]))  # True
print(canJump([3, 2, 1, 0, 4]))  # False
