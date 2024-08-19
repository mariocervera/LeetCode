
def isSubsequence(s, t):
    if len(s) > len(t):
        return False
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

print(isSubsequence(s = "abc", t = "ahabgdca")) # True
print(isSubsequence(s = "abc", t = "ahbgdc")) # True
print(isSubsequence(s = "axc", t = "ahbgdc")) # False
print(isSubsequence(s = "acb", t = "ahbgdc")) # False