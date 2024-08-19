from collections import deque

_open = "([{"
_closed = {')': '(', ']': '[', '}': '{'}


def isValid(s):
    stack = deque()
    for c in s:
        if c in _open:
            stack.append(c)
        elif len(stack) == 0 or _closed[c] != stack.pop():
            return False
    return len(stack) == 0


print(isValid("()[]{}"))  # True
print(isValid("(())[]"))  # True
print(isValid(""))  # True
print("---")
print(isValid("([)]"))  # False
print(isValid("()]"))  # False
