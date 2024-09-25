
def isArraySpecial(nums, queries):
    n = len(nums)
    arr = [0] * n
    for i in range(1, n):
        arr[i] = arr[i - 1] + int(nums[i] % 2 == nums[i - 1] % 2)
    return [arr[i] == arr[j] for i, j in queries]


print(isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))  # [False]
print(isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))  # [False, True]
