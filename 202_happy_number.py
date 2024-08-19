
def get_product_of_digit_squares(n):
    res = 0
    while n:
        res += (n % 10) ** 2
        n //= 10
    return res


def isHappy(n):
    slow = fast = n
    while True:
        slow = get_product_of_digit_squares(slow)
        fast = get_product_of_digit_squares(fast)
        fast = get_product_of_digit_squares(fast)
        if slow == fast:
            break
    return slow == 1


print(isHappy(1))  # True
print(isHappy(19))  # True
print(isHappy(2))   # False
