def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        _sum = numbers[i] + numbers[j]
        if _sum == target:
            break
        if _sum > target:
            j -= 1
        else:
            i += 1
    return [i+1, j+1]


print(twoSum(numbers=[2, 7, 11, 15], target=9))  # [1,2]
print(twoSum(numbers=[2, 3, 4], target=6))  # [1,3]
print(twoSum(numbers=[-1, 0], target=-1))  # [1,2]
