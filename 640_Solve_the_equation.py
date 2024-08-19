
def evaluate_expr(s):
    s = s.replace("+", "#+").replace("-", "#-")
    tokens = s.split("#")
    x_coeficient, free_coeficient = 0, 0
    for token in tokens:
        if not token:
            continue
        if token == "x" or token == "+x":
            x_coeficient += 1
        elif token == "-x":
            x_coeficient -= 1
        elif token[-1] == "x":
            x_coeficient += int(token[:len(token)-1])
        else:
            free_coeficient += int(token)
    return x_coeficient, free_coeficient


def solveEquation(equation):
    expr_1, expr_2 = equation.split("=")
    x_coef_left, free_coef_left = evaluate_expr(expr_1)
    x_coef_right, free_coef_right = evaluate_expr(expr_2)
    x_coef_left -= x_coef_right
    free_coef_right -= free_coef_left
    if not x_coef_left and not free_coef_right:
        return "Infinite solutions"
    elif not x_coef_left:
        return "No solution"
    elif not free_coef_right:
        return "x=0"
    return f"x={free_coef_right // x_coef_left}"


print(solveEquation("-x=-1"))  # x=1
print(solveEquation("x=x+2")) # "Infinite solutions"
print(solveEquation("x+5-3+x=6+x-2"))  # "x=2"
print(solveEquation("x=x"))  # "Infinite solutions"
print(solveEquation("2x=x"))  # "x=0"
