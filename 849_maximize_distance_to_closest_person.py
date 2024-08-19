import math

def maxDistToClosest(seats):
    i, n = 0, len(seats)
    while seats[i] != 1:
        i += 1
    first_one = i
    max_border_streak = i
    i = n-1
    while seats[i] != 1:
        i -= 1
    last_one = i
    max_border_streak = max(max_border_streak, n-i-1)
    current_streak, max_center_streak = 0, -1
    for seat in range(first_one+1, last_one):
        if seats[seat] == 1:
            current_streak = 0
            continue
        current_streak += 1
        max_center_streak = max(max_center_streak, current_streak)
    return max(
        max_border_streak,
        math.ceil(max_center_streak / 2)
    )


print(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))  # 2
print(maxDistToClosest([1, 0, 0, 0]))  # 3
print(maxDistToClosest([0, 1]))  # 1
