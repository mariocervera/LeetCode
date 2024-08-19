
def canCompleteCircuit(gas, cost):
    res, total_sum, partial_sum = -1, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_sum += diff
        partial_sum += diff
        if partial_sum < 0:
            res, partial_sum = -1, 0
        elif res == -1:
            res = i
    return res if total_sum >= 0 else -1


print(canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
print(canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # -1
