
def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for target, source in prerequisites:
        graph[source].append(target)
    discovered, processed = set(), set()

    def dfs(node):
        for adjacent in graph[node]:
            if adjacent in discovered:
                return False
            if adjacent not in processed:
                discovered.add(adjacent)
                if not dfs(adjacent):
                    return False
                discovered.remove(adjacent)
        processed.add(node)
        return True

    for i in range(numCourses):
        if i not in processed and not dfs(i):
            return False
    return True

print(canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
