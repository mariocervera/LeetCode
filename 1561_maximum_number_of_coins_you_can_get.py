
def maxCoins(piles):
    n = len(piles)
    piles.sort(reverse=True)
    i, j = 1, n-1
    res = 0
    while i < j:
        res += piles[i]
        i, j = i+2, j-1
    return res


print(maxCoins([2, 4, 1, 2, 7, 8]))  # 9
print(maxCoins([2, 4, 5]))  # 4
print(maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))  # 18
