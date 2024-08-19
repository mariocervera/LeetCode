

def lengthOfLastWord(s):
    p = len(s) - 1
    while p >= 0 and s[p] == " ":
        p -= 1
    length = 0
    while p >= 0 and s[p] != " ":
        p, length = p-1, length+1
    return length


print(lengthOfLastWord("Hello World"))  # 5
print(lengthOfLastWord("Hola Mario a "))  # 1
print(lengthOfLastWord("aa"))  # 2
