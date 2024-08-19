'''
def binary_search(nums, target, look_for_starting):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            if look_for_starting:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    high = mid-1
            else:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    return mid
                else:
                    low = mid+1
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1
'''

def searchRange(nums, target):
    low, high = 0, len(nums)-1
    res = [-1, -1]

    if not nums:
        return res

    while low < high:
        mid = (low+high)//2
        if nums[mid] < target:
            low = mid+1
        else:
            high = mid

    if nums[low] != target:
        return res

    res[0] = low

    high = len(nums)-1
    while low < high:
        mid = (low+high)//2+1
        if nums[mid] > target:
            high = mid-1
        else:
            low = mid

    res[1] = low

    return res


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
print(searchRange(nums=[5, 7, 7, 8, 8, 8, 8, 8], target=8))  # [3,7]
print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
print(searchRange(nums=[], target=0))  # [-1,-1]
