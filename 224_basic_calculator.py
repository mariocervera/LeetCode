
operate = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y
}

def calculate(s):

    stack = []

    def evaluate_expression():
        while len(stack) > 1:
            operand_1 = stack.pop()
            if operand_1 == "-":
                stack.append(int(stack.pop()) * -1)
                continue
            operand_1 = int(operand_1)
            operator = stack.pop()
            if operator == ")":
                stack.append(operand_1)
                return
            operand_2 = int(stack.pop())
            result = operate[operator](operand_1, operand_2)
            stack.append(result)

    def get_first_digit_position(word, end):
        low = end
        while low >= 0 and word[low].isdigit():
            low -= 1
        return low + 1

    i = len(s)-1
    while i >= 0:
        c = s[i]
        if c == "(":
            evaluate_expression()
        elif c in "-+)":
            stack.append(c)
        elif c.isdigit():
            j = get_first_digit_position(s, i)
            stack.append(s[j:i+1])
            i = j
        i -= 1

    if len(stack) > 1:
        evaluate_expression()

    return int(stack[-1])


print(calculate("1") == 1)
print(calculate("1+1") == 2)
print(calculate("1 + 1") == 2)
print(calculate("2-1+2") == 3)
print(calculate(" 2-1 + 2 ") == 3)
print(calculate("(1+1)") == 2)
print(calculate("(1+1+1+1-1)") == 3)
print(calculate(" ( 1 + 1 + 1 + 1 ) ") == 4)
print(calculate("(5+2) - (1+1)") == 5)
print(calculate("1 + (5+2) - (1+1)") == 6)
print(calculate("(1+(5-2))") == 4)
print(calculate("(1+(4+5+2)-3)+(6+8)") == 23)
print(calculate("-(1+1)") == -2)
print(calculate("1-2") == -1)
print(calculate("-1-2") == -3)
print(calculate("-(1+1)+3") == 1)
print(calculate(" -(1+(-1+5 ))+3") == -2)
print(calculate("100") == 100)
print(calculate("100+1") == 101)
print(calculate("-10 + 1") == -9)
print(calculate("-(10 + 2) + 1") == -11)
