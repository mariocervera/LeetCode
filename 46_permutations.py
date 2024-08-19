'''
def permute(nums):
    all_nums = set(nums)
    n = len(nums)
    permutations = []

    def backtrack(solution, used, k):
        nonlocal permutations
        if k == n:
            permutations.append(solution.copy())
            return
        for candidate in all_nums - used:
            solution.append(candidate)
            used.add(candidate)
            backtrack(solution, used, k+1)
            solution.pop()
            used.remove(candidate)

    backtrack([], set(), 0)
    return permutations


def permute(nums):
    n = len(nums)
    permutations = []

    def backtrack(solution, k):
        nonlocal permutations
        if k == n:
            permutations.append(solution.copy())
            return
        for candidate in nums:
            if candidate not in solution:
                solution.append(candidate)
                backtrack(solution, k+1)
                solution.pop()

    backtrack([], 0)
    return permutations
'''


def permute(nums):
    if len(nums) == 1:
        return [nums]
    permutations = []
    for i in range(len(nums)):
        permutations_subproblem = permute(nums[:i] + nums[i + 1:])
        for permutation in permutations_subproblem:
            new_permutation = [nums[i]] + permutation
            permutations.append(new_permutation)
    return permutations

print(permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute([0, 1]))  # [[0,1],[1,0]]
print(permute([0]))  # [[0]]
