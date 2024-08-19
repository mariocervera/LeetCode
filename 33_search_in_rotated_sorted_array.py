
def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_minimum(arr):
    low, high = 0, len(arr)-1
    if arr[low] < arr[high]:
        return low
    while low < high:
        mid = (low + high) // 2
        if mid > 0 and arr[mid] < arr[mid-1]:
            return mid
        elif arr[mid] > arr[-1]:
            low = mid+1
        else:
            high = mid
    return low


def search(nums, target):
    index_min = find_minimum(nums)
    right_side = binary_search(nums, index_min, len(nums)-1, target)
    if right_side != -1:
        return right_side
    return binary_search(nums, 0, index_min-1, target) if index_min > 0 else -1


print(search(nums=[3, 1], target=1))  # 1
print(search(nums=[1, 5, 7, 8, 9], target=5))  # 1
print(search(nums=[9, 1, 5, 7, 8], target=9))  # 0
print(search(nums=[9, 1, 5, 7, 8], target=8))  # 4
print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
print(search(nums=[1], target=0))  # -1
