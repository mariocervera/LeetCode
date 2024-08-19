
'''
def wordPattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
        return False
    ht = {}
    for i, word in enumerate(words):
        if word not in ht:
            ht[word] = pattern[i]
        elif ht[word] != pattern[i]:
            return False
    return True
'''

def wordPattern(pattern, s):
    words = s.split()
    return list(map(pattern.find, pattern)) == list(map(words.index, words))


print(wordPattern(pattern = "abba", s = "dog cat cat dog"))  # True
print(wordPattern(pattern = "abba", s = "dog cat cat fish"))  # False
print(wordPattern(pattern = "aaaa", s = "dog cat cat dog"))  # False
print(wordPattern(pattern = "abc", s = "b c a"))  # True