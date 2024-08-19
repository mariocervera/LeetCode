
def orderlyQueue(s, k):
    n = len(s)
    if n == 1:
        return s
    if k == 1:
        min_s = s
        for i in range(1, n):
            rotation = s[i:] + s[:i]
            min_s = rotation if rotation < min_s else min_s
        return min_s
    arr = list(s)
    arr.sort()
    return "".join(arr)




print(orderlyQueue("kuh", 1))  # "hku"
print(orderlyQueue("cba", 1))  # "acb"
print(orderlyQueue("baaca", 3))  # "aaabc"
print(orderlyQueue("gn", 2))  # "gn"
