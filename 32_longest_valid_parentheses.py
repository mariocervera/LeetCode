
def longestValidParentheses(s):
    stack, arr = [], [0] * len(s)
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif stack:
            index = stack.pop()
            arr[index], arr[i] = 1, 1
    counter, max_len = 0, 0
    for num in arr:
        if num == 0:
            counter = 0
        else:
            counter += 1
            max_len = max(max_len, counter)
    return max_len


print(longestValidParentheses(""))  # 0
print(longestValidParentheses("(()"))  # 2
print(longestValidParentheses(")()())"))  # 4
print(longestValidParentheses("))(((())))()()(("))  # 12
print(longestValidParentheses("())()"))  # 2
print(longestValidParentheses("()(()()"))  # 4
print(longestValidParentheses("()()(()"))  # 4
print(longestValidParentheses("()()(()()()(()"))  # 6
