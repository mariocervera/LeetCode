from collections import Counter

def minWindow(s, t):
    m, n = len(s), len(t)
    if n > m:
        return ""
    if s == t:
        return s

    i, j, matched_chars = 0, 0, 0
    t_map = Counter(t)
    best_i, best_j, min_len = -1, -1, float("inf")

    while j < m:
        if s[j] in t_map:
            if t_map[s[j]] > 0:
                matched_chars += 1
            t_map[s[j]] -= 1
        j += 1
        while matched_chars == n:
            if j-i < min_len:
                min_len = j-i
                best_i, best_j = i, j-1
            if s[i] in t_map:
                t_map[s[i]] += 1
                if t_map[s[i]] > 0:
                    matched_chars -= 1
            i += 1

    return "" if min_len == float("inf") else s[best_i:best_j+1]



print(minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(minWindow("ADDBCABDDCD", "AB"))  # "AB"
print(minWindow("ADCBBBAAAABBBBC", "ABC"))  # "ADCB"
print(minWindow("bbaac", "aba"))  # "baa"
