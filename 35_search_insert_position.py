
def searchInsert(nums, target):
    i, j = 0, len(nums)-1
    while i < j:
        mid = (i+j)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid-1
        else:
            i = mid+1
    if nums[i] == target:
        return i
    return i if target < nums[i] else i+1


print(searchInsert([1], 1)) # 0
print(searchInsert([1,3,5,6], 5)) # 2

print(searchInsert([1,3,5,6], 0)) # 0
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 4)) # 2
print(searchInsert([1,3,5,6], 7)) # 4