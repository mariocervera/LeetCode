
def findMaximumScore(nums):
    score = add = 0
    for num in nums:
        score += add
        add = max(add, num)
    return score


print(findMaximumScore([1, 3, 1, 5]))  # 7
print(findMaximumScore([4, 3, 1, 3, 2]))  # 16
