
def getSneakyNumbers(nums):
    res, seen = [], set()
    for num in nums:
        if num in seen:
            res.append(num)
        seen.add(num)
    return res


print(getSneakyNumbers([0, 1, 1, 0]))  # [0,1]
print(getSneakyNumbers([0, 3, 2, 1, 3, 2]))  # [2,3]
print(getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))  # [4,5]
