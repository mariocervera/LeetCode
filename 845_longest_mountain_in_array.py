def longestMountain(arr):
    res, n = 0, len(arr)
    i = 1
    while i < n:
        while i < n and arr[i-1] == arr[i]:
            i += 1
        up = 0
        while i < n and arr[i-1] < arr[i]:
            up += 1
            i += 1
        down = 0
        while i < n and arr[i-1] > arr[i]:
            down += 1
            i += 1
        if up > 0 and down > 0:
            res = max(res, up + down + 1)
    return res



print(longestMountain([0, 2, 2]))  # 0
print(longestMountain([2, 1, 4, 7, 3, 2, 5]))  # 5
print(longestMountain([0, 1, 2, 3, 4, 3, 2, 1, 0]))  # 9
print(longestMountain([0, 1, 2, 3, 4, 2, 1, 0]))  # 8
print(longestMountain([2, 2, 2]))  # 0
