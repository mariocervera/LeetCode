
def twoSum(nums, target):
    indexes = {}
    for i, num in enumerate(nums):
        num_to_search = target - num
        if num_to_search in indexes:
            return [indexes[num_to_search], i]
        indexes[num] = i
    return []


print(twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
print(twoSum(nums=[3, 2, 4], target=6))  # [1,2]
print(twoSum(nums=[3, 3], target=6))  # [0,1]
print(twoSum(nums =[2,5,5,11], target=10))  # [1,2]
