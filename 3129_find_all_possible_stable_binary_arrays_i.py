
mod = 10 ** 9 + 7

def numberOfStableArrays(zero, one, limit):
    dp = [[[-1, -1] for _ in range(201)] for _ in range(201)]

    def dfs(num_zeros, num_ones, last_bit):
        if num_zeros < 0 or num_ones < 0:
            return 0
        if num_zeros == 0 and num_ones == 0:
            return 1
        if dp[num_zeros][num_ones][last_bit] >= 0:
            return dp[num_zeros][num_ones][last_bit]
        res = 0
        if last_bit == 0:
            for i in range(1, limit + 1):
                res += dfs(num_zeros, num_ones - i, 1)
        else:
            for i in range(1, limit + 1):
                res += dfs(num_zeros - i, num_ones, 0)
        dp[num_zeros][num_ones][last_bit] = res % mod
        return dp[num_zeros][num_ones][last_bit]

    res = 0
    for i in range(1, limit+1):
        res += dfs(zero - i, one, 0)
        res += dfs(zero, one - i, 1)
    return res % mod



print(numberOfStableArrays(zero=1, one=1, limit=2))  # 2
print(numberOfStableArrays(zero=1, one=2, limit=1))  # 1
print(numberOfStableArrays(zero=3, one=3, limit=2))  # 14
print(numberOfStableArrays(zero=19, one=15, limit=15))  # 855954457
print(numberOfStableArrays(zero=20, one=15, limit=75))  # 247943139
print(numberOfStableArrays(zero=200, one=200, limit=25))  # 292126791
print(numberOfStableArrays(zero=198, one=199, limit=197))  # 193931817
