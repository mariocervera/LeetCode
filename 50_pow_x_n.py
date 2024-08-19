
'''
def myPow(x, n):
    if not n:
        return 1
    is_negative = n < 0
    n = abs(n)
    y = myPow(x, n//2)
    power = y * y if n % 2 == 0 else y * y * x
    return power if not is_negative else 1.0/power
'''

def myPow(x, n):
    if n < 0:
        x = 1/x
        n = -n
    res = 1
    while n:
        if n % 2 != 0:
            res *= x
        x *= x
        n //= 2
    return res


print(myPow(x=3.0, n=2))  # 9
print(myPow(x=2.0, n=10))  # 1024.0
print(myPow(x=2.1, n=3))  # 9.261
print(myPow(x=2.00000, n=-2))  # 0.25
print(myPow(x=8.95371, n=-1))  # 0.11169