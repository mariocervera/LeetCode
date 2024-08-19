
def trap(height):
    water, n = 0, len(height)

    max_so_far, max_peak_to_left = float("-inf"), ([-1] * n)
    for i in range(n):
        if max_so_far > height[i]:
            max_peak_to_left[i] = max_so_far
        max_so_far = max(max_so_far, height[i])

    max_so_far, max_peak_to_right = float("-inf"), ([-1] * n)
    for i in range(n-1, -1, -1):
        if max_so_far > height[i]:
            max_peak_to_right[i] = max_so_far
        max_so_far = max(max_so_far, height[i])

    for i in range(n):
        if max_peak_to_left[i] == -1 or max_peak_to_right[i] == -1:
            continue
        water += min(max_peak_to_left[i], max_peak_to_right[i]) - height[i]
    return water




print(trap([4, 2, 3]))  # 1
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))  # 9
