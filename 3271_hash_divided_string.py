
alphabet_size = 26

def stringHash(s, k):
    n, res = len(s), []
    i = 0
    while i < n:
        char_sum = 0
        j = 0
        while j < k:
            char_sum += (ord(s[i+j]) - ord('a'))
            j += 1
        res.append(chr(char_sum % alphabet_size + ord('a')))
        i += k
    return "".join(res)


print(stringHash(s="abcd", k=2))  # "bf"
print(stringHash(s="mxz", k=3))  # "i"
