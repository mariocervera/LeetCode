
def minimumCardPickup(cards):
    d, res = {}, float("inf")
    for i, card in enumerate(cards):
        if card in d:
            index = d[card]
            res = min(res, i-index+1)
        d[card] = i
    return res if res != float("inf") else -1

print(minimumCardPickup([3, 4, 2, 3, 4, 7]))  # 4
print(minimumCardPickup([1, 2, 0, 4, 9, 8, 2, 2, 5, 3]))  # 2
print(minimumCardPickup([1, 0, 5, 3]))  # -1
