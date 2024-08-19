from random import shuffle
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high + 1):
        if arr[j] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def findKthLargest(nums, k):

    def quick_select(i, j, target_index):
        while i < j:
            pivot_index = partition(nums, i, j)
            if target_index == pivot_index:
                break
            if target_index < pivot_index:
                j = pivot_index-1
            else:
                i = pivot_index+1
        return nums[target_index]

    shuffle(nums)
    return quick_select(0, len(nums) - 1, k-1)



print(findKthLargest([7, 6, 5, 4, 3, 2, 1], 2))  # 6
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
