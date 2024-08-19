

def removeDuplicates(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    for j in range(n):
        if j == 0 or nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
    return i


tc0 = [1, 1]
print(removeDuplicates(tc0))  # 1
print(tc0)  # [1,_]

tc1 = [1, 1, 2]
print(removeDuplicates(tc1))  # 2
print(tc1)  # [1,2,_]

tc2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(tc2))  # 5
print(tc2)  # [0,1,2,3,4,_,_,_,_,_]
