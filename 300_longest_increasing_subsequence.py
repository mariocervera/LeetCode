def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return -1
        elif arr[mid] > target:
            if mid == 0 or arr[mid-1] < target:
                return mid
            else:
                high = mid-1
        else:
            low = mid+1
    return -1


def lengthOfLIS(nums):
    subsequence = [nums[0]]
    for i in range(1, len(nums)):
        if subsequence[-1] < nums[i]:
            subsequence.append(nums[i])
        else:
            index = binary_search(subsequence, nums[i])
            if index >= 0:
                subsequence[index] = nums[i]
    return len(subsequence)

print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
