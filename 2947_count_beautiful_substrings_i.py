
def beautifulSubstrings(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res, n = 0, len(s)
    for i in range(n):
        counter_vowels, counter_consonants = 0, 0
        for j in range(i, n):
            if s[j] in vowels:
                counter_vowels += 1
            else:
                counter_consonants += 1
            if counter_vowels == counter_consonants and counter_vowels * counter_consonants % k == 0:
                res += 1
    return res


print(beautifulSubstrings("baeyh", 2))  # 2
print(beautifulSubstrings("abba", 1))  # 3
print(beautifulSubstrings("bcdf", 1))  # 0
