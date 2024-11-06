
def encrypt(num):
    return int(max(str(num)) * len(str(num)))


def sumOfEncryptedInt(nums):
    return sum([encrypt(num) for num in nums])


print(sumOfEncryptedInt([1, 2, 3]))  # 6
print(sumOfEncryptedInt([10, 21, 31]))  # 66
