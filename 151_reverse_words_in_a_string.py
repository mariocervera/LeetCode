
def reverse(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i, j = i+1, j-1


def reverse_words(list_s):
    n = len(list_s)
    i, j = 0, 0
    while i < n:
        while i < j or (i < n and list_s[i] == " "):
            i += 1
        while j < i or (j < n and list_s[j] != " "):
            j += 1
        reverse(list_s, i, j-1)


def clean_spaces(list_s):
    n = len(list_s)
    i, j = 0, 0
    while j < n:
        while j < n and list_s[j] == " ":
            j += 1
        while j < n and list_s[j] != " ":
            list_s[i] = list_s[j]
            i, j = i+1, j+1
        while j < n and list_s[j] == " ":
            j += 1
        if j < n:
            list_s[i] = " "
            i += 1
    return list_s[:i]


def reverseWords(s):
    list_s, n = list(s), len(s)
    reverse(list_s, 0, n-1)
    reverse_words(list_s)
    return "".join(clean_spaces(list_s))



print(reverseWords("the sky is blue"))  # "blue is sky the"
print(reverseWords(" the sky is blue   "))  # "blue is sky the"
print(reverseWords("the    sky     is blue "))  # "blue is sky the"
