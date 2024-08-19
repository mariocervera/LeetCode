
def isReachableAtTime(sx, sy, fx, fy, t):
    if sx == fx and sy == fy:
        return t != 1
    min_distance = max(abs(sx - fx), abs(sy - fy))
    return min_distance <= t


print(isReachableAtTime(sx=1, sy=1, fx=1, fy=1, t=3))  # True
print(isReachableAtTime(sx=1, sy=1, fx=1, fy=5, t=8))  # True
print(isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6))  # True
print(isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3))  # False
