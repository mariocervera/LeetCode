
def strWithout3a3b(a, b):
    res = []
    a_in_a_row, b_in_a_row = 0, 0
    for _ in range(a + b):
        if (a > b and a_in_a_row < 2) or b_in_a_row == 2:
            res.append('a')
            a_in_a_row, b_in_a_row = a_in_a_row + 1, 0
            a -= 1
        else:
            res.append('b')
            a_in_a_row, b_in_a_row = 0, b_in_a_row + 1
            b -= 1
    return "".join(res)



print(strWithout3a3b(a=2, b=3))  # "babab
print(strWithout3a3b(a=3, b=3))  # "ababab
print(strWithout3a3b(a=1, b=2))  # "abb"
print(strWithout3a3b(a=4, b=1))  # "aabaa"
print(strWithout3a3b(a=2, b=4))  # "bbabab"
