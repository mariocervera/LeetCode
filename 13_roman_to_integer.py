val = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

def romanToInt(s):
    res, n = 0, len(s)
    for i in range(n):
        if i < n-1 and val[s[i]] < val[s[i+1]]:
            res -= val[s[i]]
        else:
            res += val[s[i]]
    return res


print(romanToInt("I"))  # 1
print(romanToInt("III"))  # 3
print(romanToInt("IV"))  # 4
print(romanToInt("X"))  # 10
print(romanToInt("XI"))  # 11
print(romanToInt("IX"))  # 9
print(romanToInt("XV"))  # 15
print(romanToInt("XVIII"))  # 18
print(romanToInt("XIX"))  # 19
print(romanToInt("XX"))  # 20
print(romanToInt("LVIII"))  # 58
print(romanToInt("MCMXCIV"))  # 1994
