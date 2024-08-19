
def get_arrival_time(arr, speed):
    res = 0
    for i in range(len(arr) - 1):
        kms = arr[i]
        res += kms // speed + int(kms % speed != 0)
    res += arr[-1] / speed
    return res


def minSpeedOnTime(dist, hour):
    n = len(dist)
    if hour <= n-1:
        return -1
    low, high = 1, 2
    while get_arrival_time(dist, high) > hour:
        low = high
        high *= 2
    while low < high:
        mid = (low+high) // 2
        arrival_time = get_arrival_time(dist, mid)
        if arrival_time > hour:
            low = mid + 1
        else:
            high = mid
    return low


print(minSpeedOnTime(dist=[1, 3, 2], hour=6))  # 1
print(minSpeedOnTime(dist=[1, 3, 2], hour=2.7))  # 3
print(minSpeedOnTime(dist=[1, 3, 2], hour=1.9))  # -1
