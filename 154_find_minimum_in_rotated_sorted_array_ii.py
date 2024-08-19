
def find_min_binary_search(nums, low, high):
    while low < high:
        mid = (low+high) // 2
        if nums[mid] > nums[high]:
            low = mid+1
        else:
            high = mid
    return nums[low]


def findMin(nums):
    n = len(nums)
    if n == 1 or nums[0] < nums[-1]:
        return nums[0]
    low, high = 0, n-1
    if nums[0] == nums[-1]:
        high -= 1
        while high > 0 and nums[high] == nums[high+1]:
            high -= 1
        if low == high or nums[high] > nums[high+1]:
            return nums[low]
    return find_min_binary_search(nums, low, high)



print(findMin([3, 3, 3, 5, 7, 2, 3, 3]))  # 2
print(findMin([3, 3, 3, 5, 7, 3, 3]))  # 3

print(findMin([1, 3, 5]))  # 1
print(findMin([1, 1, 3, 3, 5, 5, 5]))  # 1

print(findMin([2, 2, 2, 0, 1]))  # 0
print(findMin([2, 2, 2, 3, 0, 0, 1]))  # 0
print(findMin([3, 5, 7, 2, 2, 2]))  # 2

