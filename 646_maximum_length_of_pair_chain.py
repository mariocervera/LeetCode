
def findLongestChain(pairs):
    pairs.sort(key=lambda p: (p[1], p[0]))
    last_pair = pairs[0]
    res = 1
    for pair in pairs:
        if pair[0] > last_pair[1]:
            res += 1
            last_pair = pair
    return res


print(findLongestChain([[1, 2], [2, 3], [3, 4]]))  # 2
print(findLongestChain([[1, 2], [7, 8], [4, 5]]))  # 3
