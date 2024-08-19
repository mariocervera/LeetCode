
def maxTurbulenceSize(arr):
    if len(arr) == 1:
        return 1
    res, i = 0, 0
    for j in range(1, len(arr)):
        if arr[j-1] == arr[j]:
            i = j
        elif j-i > 1 and \
                ((arr[j - 1] > arr[j] and arr[j - 2] >= arr[j - 1]) or
                 (arr[j - 1] < arr[j] and arr[j - 2] <= arr[j - 1])):
            i = j - 1
        res = max(res, j-i+1)
    return res


print(maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))  # 5
print(maxTurbulenceSize([4, 8, 12, 16]))  # 2
print(maxTurbulenceSize([100]))  # 1
