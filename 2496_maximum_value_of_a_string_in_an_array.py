
def maximumValue(strs):
    res = float("-inf")
    for s in strs:
        res = max(res, int(s) if s.isdigit() else len(s))
    return res


print(maximumValue(["alic3", "bob", "3", "4", "00000"]))  # 5
print(maximumValue(["1", "01", "001", "0001"]))  # 1
