
def jump(nums):
    n = len(nums)
    if n == 1:
        return 0
    global_max, level_max, jumps = 0, 0, 0
    for i in range(n):
        global_max = max(global_max, i+nums[i])
        if global_max >= n-1:
            return jumps+1
        if i == level_max:
            jumps += 1
            level_max = global_max
    return -1



print(jump([1]))  # 0
print(jump([2, 3, 1, 1, 4]))  # 2
print(jump([2, 3, 0, 1, 4]))  # 2
print(jump([2, 3, 1, 1, 4, 1]))  # 3
print(jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]))  # 2
