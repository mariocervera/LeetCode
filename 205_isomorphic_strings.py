
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    arr_s, arr_t = [-1] * 128, [-1] * 128
    for i in range(len(s)):
        if arr_s[ord(s[i])] != arr_t[ord(t[i])]:
            return False
        arr_s[ord(s[i])] = i
        arr_t[ord(t[i])] = i
    return True



print(isIsomorphic(s = "egg", t = "add"))  # True
print(isIsomorphic(s = "foo", t = "bar"))  # False
print(isIsomorphic(s = "badc", t = "baba"))  # False


