
def processQueries(queries, m):
    res = []
    permutation = list(range(1, m + 1))
    indices = [None] + [num - 1 for num in permutation]
    for query in queries:
        query_index = indices[query]
        res.append(query_index)
        for i in range(query_index - 1, -1, -1):
            permutation[i + 1] = permutation[i]
            indices[permutation[i + 1]] = i + 1
        permutation[0] = query
        indices[query] = 0
    return res


print(processQueries(queries=[3, 1, 2, 1], m=5))     # [2,1,2,1]
print(processQueries(queries=[4, 1, 2, 2], m=4))     # [3,1,2,0]
print(processQueries(queries=[7, 5, 5, 8, 3], m=8))  # [6,5,0,7,5]
