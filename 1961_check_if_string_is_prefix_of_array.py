def isPrefixString(s, words):
    prefix = ""
    for word in words:
        prefix += word
        if prefix == s:
            return True
    return False


print(isPrefixString(s="iloveleetcode", words=["i", "love", "leetcode", "apples"]))  # True
print(isPrefixString(s="iloveleetcode", words=["apples", "i", "love", "getcode"]))  # False
