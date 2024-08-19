
def hammingWeight(n):
    counter = 0
    while n:
        n = n & (n-1)
        counter += 1
    return counter


print(hammingWeight(0b010111)) # 4