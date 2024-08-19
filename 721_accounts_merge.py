from sortedcontainers import SortedSet
from collections import defaultdict


def accountsMerge(accounts):
    parent, size, names = {}, {}, {}

    def find(s):
        if s == parent[s]:
            return s
        parent[s] = find(parent[s])
        return parent[s]

    def merge(s1, s2):
        l1 = find(s1)
        l2 = find(s2)
        if l1 != l2:
            if size[l1] < size[l2]:
                parent[l1] = l2
                size[l2] += size[l1]
            else:
                parent[l2] = l1
                size[l1] += size[l2]

    # Make sets and get names
    for account in accounts:
        account_name = account[0]
        for i in range(1, len(account)):
            email = account[i]
            if email not in parent:
                parent[email] = email
                size[email] = 1
                names[email] = account_name

    # Merge sets
    for account in accounts:
        email_1 = account[1]
        for i in range(2, len(account)):
            email_2 = account[i]
            merge(email_1, email_2)

    # Create sorted groups
    groups = defaultdict(SortedSet)
    for account in accounts:
        for i in range(1, len(account)):
            email = account[i]
            leader = find(email)
            groups[leader].add(email)

    res = []
    for group_leader in groups:
        res.append([names[group_leader]] + list(groups[group_leader]))
    return res



# [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
print(accountsMerge(accounts=[["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
                              ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
                              ["David", "David1@m.co", "David2@m.co"]]))



# [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
# ["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                              ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                              ["John", "johnnybravo@mail.com"]]))

# [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
# ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
# ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
# ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
# ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
print(accountsMerge(accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                              ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                              ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                              ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                              ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
