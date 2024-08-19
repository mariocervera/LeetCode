
mod = 10**9 + 7

def numberOfWays(corridor):
    if corridor == "S" or corridor == "P":
        return 0
    is_even, plant_streak, first_seat_index, n = True, 0, 0, len(corridor)
    while first_seat_index < n and corridor[first_seat_index] == "P":
        first_seat_index += 1
    if first_seat_index == n:
        return 0
    res = 1
    for i in range(first_seat_index, n):
        if corridor[i] == "S":
            if is_even and plant_streak > 0:
                res *= (plant_streak + 1)
            is_even = not is_even
            plant_streak = 0
        elif corridor[i] == "P" and is_even:
            plant_streak += 1
    return res % mod if is_even else 0



print(numberOfWays("SPSPPSSPSSSS"))  # 6
print(numberOfWays("SSPPSPS"))  # 3
print(numberOfWays("PPSPSP"))  # 1
print(numberOfWays("S"))  # 0