
def maxSatisfied(customers, grumpy, minutes):
    n = len(customers)
    satisfied = 0
    for i in range(n):
        if not grumpy[i]:
            satisfied += customers[i]
    for i in range(minutes):
        if grumpy[i]:
            satisfied += customers[i]
    i, j = 0, minutes
    res = satisfied
    while j < n:
        if grumpy[i]:
            satisfied -= customers[i]
        if grumpy[j]:
            satisfied += customers[j]
        i, j = i+1, j+1
        res = max(res, satisfied)
    return res


print(maxSatisfied(customers=[5,8], grumpy=[0, 1], minutes=1))  # 13
print(maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))  # 16
print(maxSatisfied(customers=[1], grumpy=[0], minutes=1))  # 1
