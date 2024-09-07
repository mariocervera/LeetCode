
def clearDigits(s):
    stack = []
    for c in s:
        if not c.isdigit():
            stack.append(c)
        elif len(stack) > 0:
            stack.pop()
    return "".join(stack)


print(clearDigits("abc"))  # "abc"
print(clearDigits("cb34"))  # ""
print(clearDigits("xy2z"))  # "xz"
