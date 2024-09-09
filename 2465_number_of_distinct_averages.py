
def distinctAverages(nums):
    nums.sort()
    averages = set()
    for i in range(len(nums) // 2):
        a, b = nums[i], nums[-i - 1]
        averages.add((a + b) / 2)
    return len(averages)


print(distinctAverages([4, 1, 4, 0, 3, 5]))  # 2
print(distinctAverages([1, 100]))  # 1
