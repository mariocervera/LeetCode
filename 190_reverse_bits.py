
def reverseBits(n):
    res = 0
    for _ in range(32):
        res <<= 1
        res |= (n & 1)
        n >>= 1
    return res

print(reverseBits(43261596)) # 964176192