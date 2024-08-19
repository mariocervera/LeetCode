
def xorGame(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor == 0 or len(nums) % 2 == 0


print(xorGame([1,1,2]))  # False
print(xorGame([0,1]))  # True
print(xorGame([1,2,3]))  # True