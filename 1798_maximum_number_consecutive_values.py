
def getMaximumConsecutive(coins):
    highest = 0
    coins.sort()
    for coin in coins:
        if coin - highest > 1:
            break
        highest += coin
    return highest + 1


print(getMaximumConsecutive([1, 3]))  # 2
print(getMaximumConsecutive([1, 1, 1, 4]))  # 8
print(getMaximumConsecutive([1, 4, 10, 3, 1]))  # 20
