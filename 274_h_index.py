
def hIndex(citations):
    n = len(citations)
    buckets = [0] * (n+1)
    for citation in citations:
        if citation <= n:
            buckets[citation] += 1
        else:
            buckets[-1] += 1
    papers = 0
    for i in range(n, -1, -1):
        papers += buckets[i]
        if papers >= i:
            return i
    return -1



print(hIndex([2, 2]))  # 2
print(hIndex([1]))  # 1
print(hIndex([3, 0, 6, 1, 5]))  # 3
print(hIndex([1, 3, 1]))  # 1
