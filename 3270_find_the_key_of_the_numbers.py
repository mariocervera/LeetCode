
def generateKey(num1, num2, num3):
    key_size = 4

    def pad_zeros(n):
        s = str(n)
        return "0" * (key_size - len(s)) + s

    s1, s2, s3 = pad_zeros(num1), pad_zeros(num2), pad_zeros(num3)
    res = [""] * key_size
    for i in range(key_size):
        res[i] = min(s1[i], s2[i], s3[i])
    return int("".join(res))


print(generateKey(num1=1, num2=10, num3=1000))  # 0
print(generateKey(num1=987, num2=879, num3=798))  # 777
print(generateKey(num1=1, num2=2, num3=3))  # 1
