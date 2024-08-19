
def decodeAtIndex(s, k):
    k -= 1
    decoded_len = 0
    for c in s:
        if c.isdigit():
            decoded_len *= int(c)
        else:
            decoded_len += 1
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        if c.isdigit():
            decoded_len //= int(c)
            k %= decoded_len
        else:
            decoded_len -= 1
            if decoded_len == k:
                return c
    return ""


print(decodeAtIndex("a2345678999999999999999", 1))

# print(decodeAtIndex("ha22", 1))
# print(decodeAtIndex("ha22", 2))
# print(decodeAtIndex("ha22", 3))
# print(decodeAtIndex("ha22", 4))
# print(decodeAtIndex("ha22", 5))
# print(decodeAtIndex("ha22", 6))
# print(decodeAtIndex("ha22", 7))
# print(decodeAtIndex("ha22", 8))



# print(decodeAtIndex("leet2code3", 1))
# print(decodeAtIndex("leet2code3", 2))
# print(decodeAtIndex("leet2code3", 3))
# print(decodeAtIndex("leet2code3", 4))
# print(decodeAtIndex("leet2code3", 5))
# print(decodeAtIndex("leet2code3", 6))
# print(decodeAtIndex("leet2code3", 7))
# print(decodeAtIndex("leet2code3", 8))
# print(decodeAtIndex("leet2code3", 9))
# print(decodeAtIndex("leet2code3", 10))
# print(decodeAtIndex("leet2code3", 11))
# print(decodeAtIndex("leet2code3", 12))
# print(decodeAtIndex("leet2code3", 13))
# print(decodeAtIndex("leet2code3", 14))
# print(decodeAtIndex("leet2code3", 15))
# print(decodeAtIndex("leet2code3", 16))
# print(decodeAtIndex("leet2code3", 17))
# print(decodeAtIndex("leet2code3", 18))
# print(decodeAtIndex("leet2code3", 19))
# print(decodeAtIndex("leet2code3", 20))
# print(decodeAtIndex("leet2code3", 21))
# print(decodeAtIndex("leet2code3", 22))
# print(decodeAtIndex("leet2code3", 23))
# print(decodeAtIndex("leet2code3", 24))



