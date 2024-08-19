
class TreeNode:
    def __init__(self):
        self.count = 0
        self.children = {}


def subdomainVisits(cpdomains):
    root = TreeNode()
    for cpdomain in cpdomains:
        split = cpdomain.split()
        visits, domain = int(split[0]), split[1]
        subdomains = domain.split(".")
        current_node = root
        for sd in range(len(subdomains)-1, -1, -1):
            if subdomains[sd] not in current_node.children:
                current_node.children[subdomains[sd]] = TreeNode()
            current_node = current_node.children[subdomains[sd]]
            current_node.count += visits
    res = []
    def dfs(node, subdomain):
        if not node:
            return
        res.append(f"{node.count} {subdomain}")
        for child in node.children:
            dfs(node.children[child], child + "." + subdomain)
    for c in root.children:
        dfs(root.children[c], c)
    return res


# ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
#print(subdomainVisits(["9001 discuss.leetcode.com"]))

# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))