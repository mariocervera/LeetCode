
def maxArea(heights):
    area = lambda pos_i, pos_j: (pos_j - pos_i) * min(heights[pos_i], heights[pos_j])

    i, j = 0, len(heights) - 1
    max_area = float("-inf")
    while i < j:
        max_area = max(max_area, area(i, j))
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
        # Optimization:
        #
        # if heights[i] < heights[j]:
        #     k = i+1
        #     while k != j and heights[k] < heights[i]:
        #         k += 1
        #     i = k
        # else:
        #     k = j-1
        #     while k != i and heights[k] < heights[j]:
        #         k -= 1
        #     j = k
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(maxArea([1, 1]))  # 1
print(maxArea([1, 2, 4, 3]))  # 4
print(maxArea([2, 3, 4, 5, 18, 17, 6]))  # 17
