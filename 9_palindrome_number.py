# Runtime: beats 19.57%. Memory: beats 9.53%
# def isPalindrome(x):
#     if x < 0:
#         return False
#     s = str(x)
#     return s == s[::-1]

# Runtime: beats 11.69%. Memory: beats 74.83%
# def isPalindrome(x):
#     if x < 0:
#         return False
#     s = str(x)
#     for i in (range(len(s)//2)):
#         if s[i] != s[-1-i]:
#             return False
#     return True

# Runtime: beats 42.16%. Memory: beats 9.53%
# def isPalindrome(x):
#     if x < 0:
#         return False
#     if x == 0:
#         return True
#     l = get_number_len(x)
#     m = 10 ** (l - 1)
#     for _ in range(l // 2):
#         d1 = x // m
#         d2 = x % 10
#         if d1 != d2:
#             return False
#         x %= m
#         x //= 10
#         m //= 100
#     return True
#
# def get_number_len(x):
#     counter = 0
#     while x > 0:
#         x //= 10
#         counter += 1
#     return counter

# Runtime: beats 17.01%. Memory: beats 9.53%
# def isPalindrome(x):
#     if x < 0:
#         return False
#     if 0 <= x <= 9:
#         return True
#     return x == reverse(x)
#
# def reverse(x):
#     res = 0
#     while x > 0:
#         res *= 10
#         res += x % 10
#         x //= 10
#     return res

# Runtime: beats 86.42%. Memory: beats 41.50%
def isPalindrome(x):
    if 0 <= x <= 9:
        return True
    if x < 0 or x % 10 == 0:
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev//10


print(isPalindrome(0))  # True
print(isPalindrome(1))  # True
print(isPalindrome(11))  # True
print(isPalindrome(121))  # True
print(isPalindrome(1221))  # True
print(isPalindrome(12321))  # True
print("-------------")
print(isPalindrome(-121))  # False
print(isPalindrome(-122))  # False
print(isPalindrome(10))  # False
print(isPalindrome(102))  # False
