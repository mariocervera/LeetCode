
mod = 10 ** 9 + 7

def countHousePlacements(n):
    prev_prev = 1
    prev = 1
    res = prev_prev + prev
    for i in range(2, n+1):
        prev_prev = prev
        prev = res
        res = (prev_prev + prev) % mod
    return (res ** 2) % mod


print(countHousePlacements(1))  # 4
print(countHousePlacements(2))  # 9
print(countHousePlacements(3))  # 25
print(countHousePlacements(4))  # 64
print(countHousePlacements(1000))  # 500478595
