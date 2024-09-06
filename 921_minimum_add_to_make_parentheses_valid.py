
def minAddToMakeValid(s):
    left, right = 0, 0
    for c in s:
        if c == "(":
            left += 1
        elif left > 0:
            left -= 1
        else:
            right += 1
    return left + right


print(minAddToMakeValid(""))  # 0
print(minAddToMakeValid("(())()"))  # 0
print(minAddToMakeValid("())"))  # 1
print(minAddToMakeValid("())("))  # 2
print(minAddToMakeValid("((("))  # 3
