
def climbStairs(n):
    if n < 3:
        return n

    back = 2
    back_back = 1

    res = 0
    for i in range(3, n+1):
        res = back + back_back
        back_back = back
        back = res

    return res


print(climbStairs(2))  # 2
print(climbStairs(3))  # 3
print(climbStairs(4))  # 5
