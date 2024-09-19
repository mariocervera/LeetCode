
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    res = [arr[0]]
    for elem in arr:
        if res[-1] < elem:
            res.append(elem)
        else:
            low, high = 0, (len(res) - 1)
            while low < high:
                mid = (low + high) // 2
                if res[mid] < elem:
                    low = mid + 1
                else:
                    high = mid
            if res[low] > elem:
                res[low] = elem
    return len(res)


def maxPathLength(coordinates, k):
    fixed = coordinates[k]
    lower, higher = [], []
    for coordinate in coordinates:
        if coordinate[0] < fixed[0] and coordinate[1] < fixed[1]:
            lower.append(coordinate)
        elif coordinate[0] > fixed[0] and coordinate[1] > fixed[1]:
            higher.append(coordinate)
    lower.sort(key=lambda t: [t[0], -t[1]])
    higher.sort(key=lambda t: [t[0], -t[1]])
    return (longest_increasing_subsequence([y for x, y in lower]) +
            longest_increasing_subsequence([y for x, y in higher]) + 1)


print(maxPathLength(coordinates=[[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], k=1))  # 3
print(maxPathLength(coordinates=[[2, 1], [7, 0], [5, 6]], k=2))  # 2
print(maxPathLength(coordinates=[[3, 6], [7, 3], [6, 9]], k=1))  # 1
