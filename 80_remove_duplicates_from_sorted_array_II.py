
def removeDuplicates(nums):
    i, n = 0, len(nums)
    for j in range(n):
        if i < 2 or (nums[j] != nums[i-1] or nums[j] != nums[i-2]):
            nums[i] = nums[j]
            i += 1
    return i


tc1 = [1,1,1,2,2,3]
print(removeDuplicates(tc1))  # 5
print(tc1)  # [1,1,2,2,3,_]

tc2 = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(tc2))  # 7
print(tc2)  # [0,0,1,1,2,3,3,_,_]

tc3 = [1,2,2]
print(removeDuplicates(tc3))  # 3
print(tc3)  # [1,2,2]