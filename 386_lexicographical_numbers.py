
def lexicalOrder(n):
    if n < 10:
        return list(range(1, n+1))

    res = []

    def backtrack(num):
        res.append(num)
        num *= 10
        for d in range(10):
            num += d
            if num > n:
                return
            backtrack(num)
            num -= d

    for i in range(1, 10):
        backtrack(i)

    return res


print(lexicalOrder(13))  # [1,10,11,12,13,2,3,4,5,6,7,8,9]
