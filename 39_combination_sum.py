
def combinationSum(candidates, target):
    n, combinations = len(candidates), []

    def backtrack(solution, solution_sum, candidates_index):
        if solution_sum == target:
            combinations.append((solution.copy()))
            return
        for i in range(candidates_index, n):
            if solution_sum + candidates[i] <= target:
                solution.append(candidates[i])
                backtrack(solution, solution_sum + candidates[i], i)
                solution.pop()

    backtrack([], 0, 0)
    return combinations

print(combinationSum(candidates=[2, 3, 6, 7], target=7))  # [[2,2,3],[7]]
print(combinationSum(candidates=[2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum(candidates=[2], target=1))  # []
