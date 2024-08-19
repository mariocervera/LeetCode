

def distinctEchoSubstrings(text):
    n = len(text)
    res = set()
    for i in range(n-1):
        for j in range(i+1, n):
            if (j-i+1) % 2 == 0:
                mid = (i+j)//2
                s1 = text[i:mid+1]
                s2 = text[mid+1:j+1]
                if s1 == s2:
                    res.add(s1)
    return len(res)



print(distinctEchoSubstrings("abcabcabc"))  # 3
print(distinctEchoSubstrings("leetcodeleetcode"))  # 2
print(distinctEchoSubstrings("aaaaaaaaaa"))  # 3
