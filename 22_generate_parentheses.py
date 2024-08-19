
def generateParenthesis(n):
    parentheses = []
    solution_size = n * 2

    def backtrack(solution, open_parentheses, closed_parentheses, i):
        nonlocal parentheses
        if i == solution_size:
            parentheses.append("".join(solution))
            return
        if open_parentheses == closed_parentheses:
            candidates = "("
        elif open_parentheses == n:
            candidates = ")"
        else:
            candidates = "()"
        for candidate in candidates:
            solution.append(candidate)
            backtrack(solution,
                      open_parentheses+1 if candidate == "(" else open_parentheses,
                      closed_parentheses + 1 if candidate == ")" else closed_parentheses,
                      i+1)
            solution.pop()

    backtrack([], 0, 0, 0)
    return parentheses




print(generateParenthesis(1))  # ["()"]
print(generateParenthesis(2))  # ['(())', '()()']
print(generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(4))  # ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]