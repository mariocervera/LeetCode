
def is_divisible_by(n, k):
    remainder = 0
    for digit in n:
        remainder = (remainder * 10 + int(digit)) % k
    return remainder == 0

def largestPalindrome(n, k):
    if k == 1:
        return "9" * n
    if k == 2:
        return "8" * n if n <= 2 else "8" + "9" * (n - 2) + "8"
    if k == 3 or k == 9:
        return "9" * n
    if k == 4:
        return "8" * n if n <= 3 else "88" + "9" * (n - 4) + "88"
    if k == 5:
        return "5" * n if n <= 2 else "5" + "9" * (n - 2) + "5"
    if k == 8:
        return "8" * n if n <= 6 else "888" + "9" * (n - 6) + "888"
    if k == 6:
        if n <= 2:
            return "6" * n
        if n % 2 == 0:
            return "8" + "9" * ((n-4) // 2) + "77" + "9" * ((n-4) // 2) + "8"
        return "8" + "9" * ((n - 3) // 2) + "8" + "9" * ((n - 3) // 2) + "8"
    if k == 7:
        if n <= 2:
            return "7" * n
        l_x = list("9" * n)
        for d in range(9, -1, -1):
            if n % 2 != 0:
                l_x[n//2] = str(d)
            else:
                l_x[n // 2 - 1] = str(d)
                l_x[n // 2] = str(d)
            if is_divisible_by(l_x, 7):
                return "".join(l_x)
    return ""


print(largestPalindrome(n=3, k=5))  # "595"
print(largestPalindrome(n=1, k=4))  # "8"
print(largestPalindrome(n=1, k=6))  # "6"
print(largestPalindrome(n=5, k=6))  # "89898"
print(largestPalindrome(n=6, k=7))  # "999999"
print(largestPalindrome(n=7, k=7))  # "9994999"
print(largestPalindrome(n=8, k=7))  # "99944999"
print(largestPalindrome(n=7, k=8))  # "8889888"
