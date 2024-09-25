from collections import Counter


def validSubstringCount(word, prefix):
    valid_substrings = 0
    n = len(word)
    counters_prefix = Counter(prefix)
    window = Counter()
    distinct_chars_prefix = len(counters_prefix)
    window_correct_chars = 0
    left = 0

    for right in range(n):
        c = word[right]
        if c in counters_prefix:
            window[c] += 1
            if window[c] == counters_prefix[c]:
                window_correct_chars += 1

        while window_correct_chars == distinct_chars_prefix:
            valid_substrings += n - right

            left_char = word[left]
            if left_char in counters_prefix:
                if window[left_char] == counters_prefix[left_char]:
                    window_correct_chars -= 1
                window[left_char] -= 1

            left += 1

    return valid_substrings


print(validSubstringCount(word="bcca", prefix="abc"))  # 1
print(validSubstringCount(word="abcabc", prefix="abc"))  # 10
print(validSubstringCount(word="abcabc", prefix="aaabc"))  # 0
print(validSubstringCount(word="dcbdcdccb", prefix="cdd"))  # 18
print(validSubstringCount(word="ddccdddccdddccccdddccdcdcd", prefix="ddc"))  # 279
