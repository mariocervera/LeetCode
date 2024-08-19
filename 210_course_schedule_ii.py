
def findOrder(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for target, source in prerequisites:
        graph[source].append(target)
    discovered, processed = set(), []

    def dfs(node):
        for adjacent in graph[node]:
            if adjacent in discovered:
                return False
            if adjacent not in processed:
                discovered.add(adjacent)
                if not dfs(adjacent):
                    return False
                discovered.remove(adjacent)
        processed.append(node)
        return True

    for i in range(numCourses):
        if i not in processed and not dfs(i):
            return []
    return processed[::-1]


print(findOrder(numCourses=2, prerequisites=[[0,1],[1,0]]))  # []
print(findOrder(numCourses=2, prerequisites=[[1, 0]]))  # [0,1]
print(findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,2,1,3]
print(findOrder(numCourses=1, prerequisites=[]))  # [0]
