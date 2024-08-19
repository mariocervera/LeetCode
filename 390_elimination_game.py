
def lastRemaining(n):
    head, step, remaining, left = 1, 1, n, True
    while n > 1:
        if left or n % 2 != 0:
            head += step
        step *= 2
        n //= 2
        left = not left
    return head

print(lastRemaining(9))  # 6
print(lastRemaining(1))  # 1

print(lastRemaining(100000000))



