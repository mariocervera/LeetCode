
def is_valid(num):
    if "." not in num:
        return not (len(num) > 1 and num[0] == "0")
    left, right = num.split(".")
    if len(left) == 0 or (len(left) > 1 and left[0] == "0"):
        return False
    if len(right) == 0 or right[-1] == "0":
        return False
    return True


def get_decimal_numbers(num):
    numbers = [num] if is_valid(num) else []
    for i in range(1, len(num)):
        decimal_number = f"{num[:i]}.{num[i:]}"
        if not is_valid(decimal_number):
            break
        numbers.append(decimal_number)
    return numbers


def generate_decimal_coordinates(x, y, solutions):
    for x_decimal_num in get_decimal_numbers(x):
        for y_decimal_num in get_decimal_numbers(y):
            solutions.append(f"({x_decimal_num}, {y_decimal_num})")


def ambiguousCoordinates(s):
    coordinates = []
    s = s[1:-1]
    for i in range(1, len(s)):
        generate_decimal_coordinates(s[:i], s[i:], coordinates)
    return coordinates


#print(ambiguousCoordinates("(123)"))  # ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
#print(ambiguousCoordinates("(0123)"))  # ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
print(ambiguousCoordinates("(00011)"))  # ["(0, 0.011)","(0.001, 1)"]


# print(is_valid("01"))
# print(is_valid("00"))
# print(is_valid("0.0"))
# print(is_valid("0.00"))
# print(is_valid("1.0"))
# print(is_valid("00.01"))
# print("---")
# print(is_valid("1"))
# print(is_valid("10"))
# print(is_valid("10.1"))
# print(is_valid("10.1001"))
# print(is_valid("10.00101"))