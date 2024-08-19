# from collections import Counter

def build_frequencies_dict(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def canConstruct( ransomNote, magazine):
    frequencies = build_frequencies_dict(magazine)
    for c in ransomNote:
        if c not in frequencies:
            return False
        frequencies[c] -= 1
        if frequencies[c] == 0:
            frequencies.pop(c)
    return True

# def canConstruct( ransomNote, magazine):
#     c1, c2 = Counter(ransomNote), Counter(magazine)
#     return c1 & c2 == c1



print(canConstruct("a","b")) # False
print(canConstruct("aa","ab")) # False
print(canConstruct("aa","aab")) # True