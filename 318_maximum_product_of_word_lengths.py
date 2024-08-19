
def maxProduct(words):
    res, n = 0, len(words)
    masks = [0] * n
    for i in range(n):
        word, mask = words[i], 0
        for ch in word:
            mask |= (1 << (ord(ch) - ord('a')))
        masks[i] = mask
        for j in range(i):
            if masks[i] & masks[j] == 0:
                res = max(res, len(word) * len(words[j]))
    return res


print(maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))  # 16
print(maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))  # 4
print(maxProduct(["a", "aa", "aaa", "aaaa"]))  # 0
