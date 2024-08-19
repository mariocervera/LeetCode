from collections import deque

letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


# Recursive solution (DFS): beats 82.48% (runtime) and 57.33% (memory)

def letterCombinations(digits):
    solutions = []
    if not digits:
        return solutions

    def dfs(current_word, i):
        nonlocal solutions
        if i == len(digits):
            solutions.append(current_word)
            return
        for letter in letters[digits[i]]:
            dfs(current_word + letter, i+1)

    dfs("", 0)
    return solutions

'''
# Iterative solution (BFS): beats 67.70% (runtime) and 57.33% (memory)
def letterCombinations(digits):
    solutions = []
    if not digits:
        return solutions
    q = deque([""])
    level = -1
    while q:
        level += 1
        for _ in range(len(q)):
            node = q.popleft()
            for adjacent in letters[digits[level]]:
                if level == len(digits)-1:
                    solutions.append(node + adjacent)
                else:
                    q.append(node + adjacent)
    return solutions
'''

print(letterCombinations("23"))
