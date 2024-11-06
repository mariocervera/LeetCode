
def findLucky(arr):
    frequencies = {}
    for val in arr:
        frequencies[val] = frequencies.get(val, 0) + 1
    res = float("-inf")
    for val, freq in frequencies.items():
        if val == freq:
            res = max(res, val)
    return res if res != float("-inf") else -1


print(findLucky([2, 2, 3, 4]))  # 2
print(findLucky([1, 2, 2, 3, 3, 3]))  # 3
print(findLucky([2, 2, 2, 3, 3]))  # -1
