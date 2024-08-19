
def get_limits_arr(heights, _range, prev):
    n = len(heights)
    arr = [-1] * n
    for i in _range:
        if heights[i] > heights[i+prev]:
            arr[i] = i+prev
        elif heights[i] == heights[i+prev]:
            arr[i] = arr[i+prev]
        else:
            index = i+prev
            while index != -1 and heights[index] >= heights[i]:
                index = arr[index]
            arr[i] = index
    return arr

def largestRectangleArea(heights):
    n = len(heights)
    if n == 1:
        return heights[0]

    lower_to_left = get_limits_arr(heights, range(1, n), -1)
    lower_to_right = get_limits_arr(heights, range(n-2, -1, -1), 1)

    max_area = float("-inf")
    for i, h in enumerate(heights):
        limit_low = lower_to_left[i]+1 if lower_to_left[i] != -1 else 0
        limit_high = lower_to_right[i]-1 if lower_to_right[i] != -1 else n-1
        area = (limit_high-limit_low+1) * heights[i]
        max_area = max(max_area, area)
    return max_area


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
print(largestRectangleArea([2, 4]))  # 4

print(largestRectangleArea([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6

