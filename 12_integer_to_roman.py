from collections import deque

val = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def convert(digit, multiplier):
    res = ""
    while digit > 0:
        if digit == 5:
            return val[multiplier*digit] + res
        if digit == 4 or digit == 9:
            return f"{val[1*multiplier]}{val[multiplier*(digit+1)]}{res}"
        res += val[1*multiplier]
        digit -= 1
    return res


def intToRoman(num):
    res, multiplier = deque(), 1
    while num > 0:
        digit = num % 10
        if digit:
            res.appendleft(convert(digit, multiplier))
        num //= 10
        multiplier *= 10
    return "".join(res)


print(intToRoman(1))  # I
print(intToRoman(3))  # III
print(intToRoman(4))  # IV
print(intToRoman(9))  # IX
print(intToRoman(10))  # X
print(intToRoman(11))  # XI
print(intToRoman(15))  # XV
print(intToRoman(18))  # XVIII
print(intToRoman(19))  # XIX
print(intToRoman(20))  # XX
print(intToRoman(58))  # LVIII
print(intToRoman(1994))  # MCMXCIV
