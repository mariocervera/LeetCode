
def get_prefix_array(pattern):
    n = len(pattern)
    prefix = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix[k-1]
        if pattern[k] == pattern[i]:
            k += 1
        prefix[i] = k
    return prefix


def minValidStrings(words, target):
    n = len(target)
    arr = [float("-inf")] * n
    for word in words:
        m = len(word)
        prefix_arr = get_prefix_array(word + "#" + target)
        for i in range(m+1, m+n+1):
            arr[i-m-1] = max(arr[i-m-1], prefix_arr[i])
    i, steps = n-1, 0
    while i >= 0 and arr[i] != 0:
        i -= arr[i]
        steps += 1
    return steps if i < 0 else -1


print(minValidStrings(words=["abc", "aaaaa", "bcdef"], target="aabcdabc"))  # 3
print(minValidStrings(words=["abababab", "ab"], target="ababaababa"))  # 2
print(minValidStrings(words=["abcdef"], target="xyz"))  # -1
