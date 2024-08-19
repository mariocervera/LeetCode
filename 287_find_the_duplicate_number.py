
def findDuplicate(nums):
    slow, fast = 0, 0
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow


print(findDuplicate([1, 3, 4, 2, 2]))  # 2
print(findDuplicate([3, 1, 3, 4, 2]))  # 3
print(findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))  # 9
