
def countOfSubstrings(word, k):
    n = len(word)
    window_vowels, window_consonants = {}, 0

    def add_character_at(index):
        nonlocal window_consonants
        if word[index] in "aeiou":
            window_vowels[word[index]] = window_vowels.get(word[index], 0) + 1
        else:
            window_consonants += 1

    def remove_character_at(index):
        nonlocal window_consonants
        if word[index] in "aeiou":
            window_vowels[word[index]] -= 1
            if window_vowels[word[index]] == 0:
                del window_vowels[word[index]]
        else:
            window_consonants -= 1

    distance_to_next_consonant = [1] * n
    for i in range(n-2, -1, -1):
        if word[i+1] in "aeiou":
            distance_to_next_consonant[i] = distance_to_next_consonant[i+1] + 1

    i, substrings = 0, 0
    for j in range(n):
        add_character_at(j)
        while window_consonants > k:
            remove_character_at(i)
            i += 1
        while len(window_vowels) == 5 and window_consonants == k:
            substrings += distance_to_next_consonant[j]
            remove_character_at(i)
            i += 1

    return substrings


print(countOfSubstrings(word="aeioqq", k=1))  # 0
print(countOfSubstrings(word="aeiou", k=0))  # 1
print(countOfSubstrings(word="ieaouqqieaouqq", k=1))  # 3
