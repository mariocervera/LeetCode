
def waysToBuyPensPencils(total, cost1, cost2):
    res = 0
    for i in range(total//cost1 + 1):
        updated_total = total - i * cost1
        res += (updated_total//cost2 + 1)
    return res


print(waysToBuyPensPencils(total=20, cost1=10, cost2=5))  # 9
print(waysToBuyPensPencils(total=5, cost1=10, cost2=10))  # 1
