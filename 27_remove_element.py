

def removeElement(nums, val):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return i

l = [3,2,2,3]
k = removeElement(l, 3)
print(l) # [2,2,_,_]
print(k) # 2

print("-----")

l = [0,1,2,2,3,0,4,2]
k = removeElement(l, 2)
print(l) # [0,1,4,0,3,_,_,_]
print(k) # 5