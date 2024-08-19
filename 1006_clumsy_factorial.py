operate = [
    lambda x, y: x * y,
    lambda x, y: x // y,
    lambda x, y: x + y,
    lambda x, y: x - y,
]


def clumsy(n):
    op, arr = 0, [n]
    n -= 1
    while n >= 1:
        if 0 <= op <= 1:
            arr[-1] = operate[op](arr[-1], n)
        elif 2 <= op <= 3:
            arr.append(n)
        op = (op + 1) % 4
        n -= 1
    res = arr[0]
    for i in range(1, len(arr)):
        res += (arr[i] if i % 2 != 0 else -arr[i])
    return res


print(clumsy(1))  # 1
print(clumsy(2))  # 2
print(clumsy(4))  # 7
print(clumsy(10))  # 12
