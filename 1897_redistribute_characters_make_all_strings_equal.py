
def makeEqual(words):
    n = len(words)
    if n == 1:
        return True
    char_counters = {}
    for word in words:
        for c in word:
            char_counters[c] = char_counters.get(c, 0) + 1
    for c in char_counters:
        if char_counters[c] % n != 0:
            return False
    return True


print(makeEqual(["abc", "aabc", "bc"]))  # True
print(makeEqual(["ab", "a"]))  # False
