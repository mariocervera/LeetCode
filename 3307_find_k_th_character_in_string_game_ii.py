import math

alphabet_size = 26


def is_power_of_2(n):
    return n & (n - 1) == 0


def get_smaller_power_of_2(n):
    return n >> 1 if is_power_of_2(n) else 1 << (n.bit_length() - 1)


def kthCharacter(k, operations):
    def k_th_character_rec(n):
        if n <= 1:
            return 0
        power_of_2 = get_smaller_power_of_2(n)
        return k_th_character_rec(n - power_of_2) + operations[int(math.log2(power_of_2))]

    return chr(ord('a') + k_th_character_rec(k) % alphabet_size)


print(kthCharacter(k=5, operations=[0, 0, 0]))  # "a"
print(kthCharacter(k=10, operations=[0, 1, 0, 1]))  # "b"
