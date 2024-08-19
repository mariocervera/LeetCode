from collections import Counter

def minimumDeletions(word, k):
    freq = sorted(Counter(word).values())
    n, res = len(freq), float("inf")
    counter_min_freq = 0

    for i in range(n):
        if counter_min_freq >= res:
            return res
        counter_max_freq = 0
        j = n-1
        while i < j and freq[j] - freq[i] > k:
            counter_max_freq += ((freq[j] - freq[i]) - k)
            j -= 1
        res = min(res, counter_min_freq + counter_max_freq)
        counter_min_freq += freq[i]
    return res


print(minimumDeletions("aabcaba", 0))  # 3
print(minimumDeletions("dabdcbdcdcd", 2))  # 2
print(minimumDeletions("aaabaaa", 2))  # 1
print(minimumDeletions("vnnppvvbbn", 0))  # 2
