
def combine(n, k):
    combinations = []

    def backtrack(combination, i, candidates):
        nonlocal combinations
        if i == k:
            combinations.append(combination.copy())
            return
        for candidate in candidates:
            combination.append(candidate)
            backtrack(combination, i+1, list(range(candidate+1, n+1)))
            combination.pop()

    backtrack([], 0, list(range(1, n+1)))

    return combinations


print(combine(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(combine(1, 1))  # [[1]]
print(combine(4, 3))  # [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]