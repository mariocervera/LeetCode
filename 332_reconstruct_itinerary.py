from sortedcontainers import SortedDict
from collections import defaultdict

def findItinerary(tickets):
    m, graph = len(tickets), defaultdict(SortedDict)
    for ticket in tickets:
        if ticket[1] not in graph[ticket[0]]:
            graph[ticket[0]][ticket[1]] = 1
        else:
            graph[ticket[0]][ticket[1]] += 1

    itinerary = []

    def backtrack(node, i):
        itinerary.append(node)
        if i == m:
            return True
        for dest_node in graph[node]:
            if graph[node][dest_node] > 0:
                graph[node][dest_node] -= 1
                if backtrack(dest_node, i + 1):
                    return True
                graph[node][dest_node] += 1
        itinerary.pop()
        return False

    backtrack("JFK", 0)
    return itinerary


print(findItinerary([["EZE", "AXA"],
                     ["TIA", "ANU"],
                     ["ANU", "JFK"],
                     ["JFK", "ANU"],
                     ["ANU", "EZE"],
                     ["TIA", "ANU"],
                     ["AXA", "TIA"],
                     ["TIA", "JFK"],
                     ["ANU", "TIA"],
                     ["JFK", "TIA"]]))  # ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]

print(findItinerary([["JFK", "KUL"],
                     ["JFK", "NRT"],
                     ["NRT", "JFK"]]))  # ['JFK', 'NRT', 'JFK', 'KUL']

print(findItinerary([["MUC", "LHR"],
                      ["JFK", "MUC"],
                      ["SFO", "SJC"],
                      ["LHR", "SFO"]]))  # ["JFK","MUC","LHR","SFO","SJC"]

print(findItinerary([["JFK", "SFO"],
                     ["JFK", "ATL"],
                     ["SFO", "ATL"],
                     ["ATL", "JFK"],
                     ["ATL", "SFO"]]))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
