from collections import Counter

def findSubstring(s, words):
    def is_substring(substr):
        index, seen = 0, {}
        while index < substring_len:
            _word = substr[index:index + word_len]
            if _word not in words_counter:
                return False
            seen[_word] = seen.get(_word, 0) + 1
            if seen[_word] > words_counter[_word]:
                return False
            index += word_len
        return words_counter == seen

    words_counter = Counter(words)
    word_len = len(words[0])
    substring_len = len(words) * word_len

    if len(s) < substring_len:
        return []

    res = []
    for i in range(len(s) - substring_len + 1):
        sstr = s[i:i + substring_len]
        if is_substring(sstr):
            res.append(i)

    return res


print(findSubstring("barfoothefoobarman", ["foo", "bar"]))  # [0,9]
print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # []
print(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # [6,9,12]
print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))  # [8]
