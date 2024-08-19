
mod = 10 ** 9 + 7


def knightDialer(n):
    dp_prev, dp_current = [1] * 10, [0] * 10
    for i in range(1, n):
        dp_current[0] = dp_prev[4] + dp_prev[6]
        dp_current[1] = dp_prev[6] + dp_prev[8]
        dp_current[2] = dp_prev[7] + dp_prev[9]
        dp_current[3] = dp_prev[4] + dp_prev[8]
        dp_current[4] = dp_prev[3] + dp_prev[9] + dp_prev[0]
        dp_current[5] = 0
        dp_current[6] = dp_prev[1] + dp_prev[7] + dp_prev[0]
        dp_current[7] = dp_prev[2] + dp_prev[6]
        dp_current[8] = dp_prev[1] + dp_prev[3]
        dp_current[9] = dp_prev[2] + dp_prev[4]
        dp_prev = dp_current
        dp_current = [0] * 10
    return sum(dp_prev) % mod

print(knightDialer(1))  # 10
print(knightDialer(2))  # 20
print(knightDialer(3131))  # 136006598
