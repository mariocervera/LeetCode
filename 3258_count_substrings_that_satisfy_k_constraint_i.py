
def countKConstraintSubstrings(s, k):
    i, j, inv_count, n = 0, 0, 0, len(s)
    zeros, ones = (1, 0) if s[0] == "0" else (0, 1)
    while j < n:
        while zeros <= k or ones <= k:
            j += 1
            if j >= n:
                break
            if s[j] == "0":
                zeros += 1
            else:
                ones += 1
        while i < j < n and zeros > k and ones > k:
            inv_count += (n - j)
            if s[i] == "0":
                zeros -= 1
            else:
                ones -= 1
            i += 1
    return n * (n+1) // 2 - inv_count


print(countKConstraintSubstrings(s="10101", k=1))  # 12
print(countKConstraintSubstrings(s="1010101", k=2))  # 25
print(countKConstraintSubstrings(s="11111", k=1))  # 15
print(countKConstraintSubstrings(s="000011", k=1))  # 18
