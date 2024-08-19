
def get_permutations(nums):
    if len(nums) == 1:
        return {(nums[0],)}
    res = set()
    for i in range(len(nums)):
        for permutation in get_permutations(nums[:i] + nums[i+1:]):
            res.add((nums[i],) + permutation)
    return res


def permuteUnique(nums):
    return [list(perm) for perm in get_permutations(nums)]


print(permuteUnique([1, 1, 2]))  # [[1,1,2], [1,2,1], [2,1,1]]
print(permuteUnique([1, 2, 3]))  # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
