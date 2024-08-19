
operate = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x/y)
}

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(operate[token](op1, op2))
    return stack[0]



print(evalRPN(["2", "1", "+", "3", "*"]))  # 9
print(evalRPN(["4", "13", "5", "/", "+"]))  # 6
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
