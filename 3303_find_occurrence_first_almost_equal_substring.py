
def z_function(s: str):
    n = len(s)
    Z = [0] * n
    left, right, k = 0, 0, 0

    for i in range(1, n):
        if i > right:
            left, right = i, i
            while right < n and s[right] == s[right - left]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            k = i - left
            if Z[k] < right - i + 1:
                Z[i] = Z[k]
            else:
                left = i
                while right < n and s[right] == s[right - left]:
                    right += 1
                Z[i] = right - left
                right -= 1

    Z[0] = n
    return Z


def minStartingIndex(s, pattern):
    m, n = len(s), len(pattern)
    z_left = z_function(pattern + s)
    z_right = z_function(pattern[::-1] + s[::-1])
    for i in range(m-n+1):
        if z_left[n+i] + z_right[m-i] + 1 >= n:
            return i
    return -1



print(minStartingIndex(s="abcdefg", pattern="bcdffg"))  # 1
print(minStartingIndex(s="ababbababa", pattern="bacaba"))  # 4
print(minStartingIndex(s="abcd", pattern="dba"))  # -1
print(minStartingIndex(s="dde", pattern="d"))  # 0
