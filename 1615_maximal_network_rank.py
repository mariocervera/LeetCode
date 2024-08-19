
def maximalNetworkRank(n, roads):
    connected = [[False for _ in range(n)] for _ in range(n)]
    degrees = [0] * n
    for i, j in roads:
        connected[i][j] = True
        connected[j][i] = True
        degrees[i] += 1
        degrees[j] += 1
    res = float("-inf")
    for i in range(n-1):
        for j in range(i+1, n):
            network_rank = degrees[i] + degrees[j] - (1 if connected[i][j] else 0)
            res = max(res, network_rank)
    return res




print(maximalNetworkRank(n=5, roads=[[2, 3], [0, 3], [0, 4], [4, 1]]))  # 4
print(maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))  # 4
print(maximalNetworkRank(n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))  # 5
print(maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))  # 5
