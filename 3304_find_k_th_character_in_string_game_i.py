
def is_power_of_2(n):
    return n & (n-1) == 0


def get_smaller_power_of_2(n):
    return n >> 1 if is_power_of_2(n) else 1 << (n.bit_length() - 1)


def k_th_character(n):
    if n <= 1:
        return 0
    return 1 + k_th_character(n - get_smaller_power_of_2(n))


def kthCharacter(k):
    return chr(ord('a') + k_th_character(k))


print(kthCharacter(4))  # "c"
print(kthCharacter(5))  # "b"
print(kthCharacter(10))  # "c"
print(kthCharacter(15))  # "d"
