
def makeStringsEqual(s, target):
    return ("1" in s) == ("1" in target)


print(makeStringsEqual(s="1010", target="0110"))  # True
print(makeStringsEqual(s="11", target="00"))  # False
print(makeStringsEqual(s="001000", target="000100"))  # True
