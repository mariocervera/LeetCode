
def is_possible_score(arr, d, score):
    current_num = arr[0]
    for i in range(len(arr)-1):
        if current_num + score > (arr[i+1] + d):
            return False
        current_num = max(current_num + score, arr[i+1])
    return True

def maxPossibleScore(start, d):
    start.sort()
    low, high = 0, start[-1] + d - start[0]
    while low < high:
        mid = (low + high) // 2 + 1
        if is_possible_score(start, d, mid):
            low = mid
        else:
            high = mid - 1
    return low


print(maxPossibleScore(start=[6, 0, 3], d=2))  # 4
print(maxPossibleScore(start=[2, 6, 13, 13], d=5))  # 5
print(maxPossibleScore(start=[1000000000, 0], d=1000000000))  # 2000000000
