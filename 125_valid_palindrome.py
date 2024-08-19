
def increment_pointer(s, p):
    while p < len(s) and not s[p].isalnum():
        p += 1
    return p

def decrement_pointer(s, p):
    while p >= 0 and not s[p].isalnum():
        p -= 1
    return p

def isPalindrome(s):
    s.lower()
    i = increment_pointer(s, 0)
    j = decrement_pointer(s, len(s)-1)

    while i < j:
        if s[i] != s[j]:
            return False
        i = increment_pointer(s, i+1)
        j = decrement_pointer(s, j-1)

    return True


print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False
print(isPalindrome(" ")) # True
print(isPalindrome("aa")) # True
print(isPalindrome("aba")) # True
print(isPalindrome("abab")) # False
print(isPalindrome("ab,,,,,ab")) # False
print(isPalindrome("ab,,,,,a")) # True