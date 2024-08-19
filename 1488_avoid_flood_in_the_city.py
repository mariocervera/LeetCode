from sortedcontainers import SortedSet

def avoidFlood(rains):
    n = len(rains)
    res = [-1] * n
    full, zeros = {}, SortedSet()
    for i in range(n):
        if rains[i] == 0:
            zeros.add(i)
        elif rains[i] not in full:
            full[rains[i]] = i
        else:
            for index_zero in zeros:
                if index_zero > full[rains[i]]:
                    res[index_zero] = rains[i]
                    full[rains[i]] = i
                    zeros.remove(index_zero)
                    break
            else:
                return []
    for index_zero in range(len(zeros)):
        if res[zeros[index_zero]] == -1:
            res[zeros[index_zero]] = 1
    return res


print(avoidFlood([1, 2, 3, 4]))  # [-1,-1,-1,-1]
print(avoidFlood([1, 2, 0, 0, 2, 1]))  # [-1,-1,2,1,-1,-1]
print(avoidFlood([1, 2, 0, 1, 2]))  # []
print(avoidFlood([2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2]))  # []
print(avoidFlood([1, 0, 2, 0, 2, 1]))  # [-1,1,-1,2,-1,-1]
print(avoidFlood([69, 0, 0, 0, 69]))  # [-1,69,1,1,-1]
print(avoidFlood([3, 5, 4, 0, 1, 0, 1, 5, 2, 8, 9]))  # [-1,-1,-1,5,-1,1,-1,-1,-1,-1,-1]
