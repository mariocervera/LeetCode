
def countVowels(word):
    n = len(word)
    word_vowels, accumulated_vowels = 0, 0
    for c in word:
        if c in "aeiou":
            word_vowels += 1
        accumulated_vowels += word_vowels
    res = accumulated_vowels
    for i in range(n):
        if word[i] in "aeiou":
            accumulated_vowels -= (n-i)
        res += accumulated_vowels
    return res


print(countVowels("aba"))  # 6
print(countVowels("abc"))  # 3
print(countVowels("ltcd"))  # 0
