
def maximumTotalSum(max_heights):
    max_heights.sort(reverse=True)
    res = 0
    last_height = float("inf")
    for max_height in max_heights:
        if max_height < last_height:
            res += max_height
            last_height = max_height
        elif last_height == 1:
            return -1
        else:
            last_height -= 1
            res += last_height
    return res


print(maximumTotalSum([2, 3, 4, 3]))  # 10
print(maximumTotalSum([15, 10]))  # 25
print(maximumTotalSum([2, 2, 1]))  # -1
