
mod = 10 ** 9 + 7

def countPalindromes(s):
    n = len(s)
    char_count, subseqs_prefix = [0] * 10, [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n)]
    for i in range(n-3):
        c = s[i]
        if i > 0:
            for j in range(10):
                for k in range(10):
                    subseqs_prefix[i][j][k] = subseqs_prefix[i-1][j][k] + (char_count[j] if c == str(k) else 0)
        char_count[int(c)] += 1
    char_count, subseqs_suffix = [0] * 10, [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n)]
    for i in range(n-1, 2, -1):
        c = s[i]
        if i < n-1:
            for j in range(10):
                for k in range(10):
                    subseqs_suffix[i][j][k] = subseqs_suffix[i+1][j][k] + (char_count[j] if c == str(k) else 0)
        char_count[int(c)] += 1
    subsequences = 0
    for i in range(2, n-2):
        for j in range(10):
            for k in range(10):
                subsequences += (subseqs_prefix[i-1][j][k] * subseqs_suffix[i+1][j][k])
    return subsequences % mod


print(countPalindromes("103301"))  # 2
print(countPalindromes("0000000"))  # 21
print(countPalindromes("9999900000"))  # 2


#print(countPalindromes("11233333"))
# print(countPalindromes("33333211"))
