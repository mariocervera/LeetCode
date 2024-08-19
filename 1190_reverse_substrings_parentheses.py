def reverseParentheses(s):
    n = len(s)
    indexes_dict, stack = {}, []
    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            open_index = stack.pop()
            indexes_dict[open_index] = i
            indexes_dict[i] = open_index
    res, i, direction = [], 0, 1
    while i < n:
        if s[i] in "()":
            i = indexes_dict[i]
            direction *= -1
        else:
            res.append(s[i])
        i += direction
    return "".join(res)


print(reverseParentheses("(abcd)"))  # "dcba"
print(reverseParentheses("(u(love)i)"))  # "iloveu"
print(reverseParentheses("(ed(et(oc))el)"))  # "leetcode"
