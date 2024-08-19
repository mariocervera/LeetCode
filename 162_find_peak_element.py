
def is_peak(nums, i):
    n = len(nums)
    return (i == 0 and nums[0] > nums[1]) or (i == n-1 and nums[-1] > nums[-2]) or (nums[i-1] < nums[i] and nums[i+1] < nums[i])

def findPeakElement(nums):
    n = len(nums)
    if n == 1:
        return 0
    low, high = 0, n-1
    while low < high:
        mid = (low+high)//2
        if is_peak(nums, mid):
            return mid
        elif mid == n-1 or (mid > 0 and nums[mid] < nums[mid-1]):
            high = mid-1
        else:
            low = mid+1
    return low

print(findPeakElement([1, 2, 3, 1]))  # 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 5
print(findPeakElement([1, 2]))  # 1
