
def reverse_array(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1, j-1


def rotate(nums, k):
    k %= len(nums)
    reverse_array(nums, 0, len(nums)-1)
    reverse_array(nums, 0, k-1)
    reverse_array(nums, k, len(nums) - 1)


arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 3)
print(arr)  # [5,6,7,1,2,3,4]

arr = [-1, -100, 3, 99]
rotate(arr, 2)
print(arr)  # [3,99,-1,-100]

arr = [1, 2]
rotate(arr, 5)
print(arr)  # [2, 1]
