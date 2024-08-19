
def isAnagram(s, t):
    counters = [0] * 26
    for c in s: counters[ord(c)-ord('a')] += 1
    for c in t: counters[ord(c)-ord('a')] -= 1
    return not any(counters)


print(isAnagram(s = "anagram", t = "nagaram"))  # True
print(isAnagram(s = "rat", t = "car"))  # False
print(isAnagram(s = "abb", t = "aab"))  # False
