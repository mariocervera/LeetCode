
def closestToTarget(arr, target):
    ands, res = set(), float("inf")
    for num in arr:
        ands = {_and & num for _and in ands} | {num}
        for pr in ands:
            res = min(res, abs(target - pr))
    return res


print(closestToTarget(arr=[9, 12, 3, 7, 15], target=5))  # 2
print(closestToTarget(arr=[1000000, 1000000, 1000000], target=1))  # 999999
print(closestToTarget(arr=[1, 2, 4, 8, 16], target=0))  # 0
