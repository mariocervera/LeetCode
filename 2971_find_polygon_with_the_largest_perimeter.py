
def largestPerimeter(nums):
    nums.sort()
    perimeter = nums[0] + nums[1]
    max_perimeter = float("-inf")
    for i in range(2, len(nums)):
        n = nums[i]
        perimeter += n
        if perimeter-n > n:
            max_perimeter = max(max_perimeter, perimeter)
    return max_perimeter if max_perimeter != float("-inf") else -1



print(largestPerimeter([5, 5, 5]))  # 15
print(largestPerimeter([1, 12, 1, 2, 5, 50, 3]))  # 12
print(largestPerimeter([5, 5, 50]))  # -1
