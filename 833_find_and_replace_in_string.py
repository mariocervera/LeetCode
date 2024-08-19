
def findReplaceString(s, indices, sources, targets):
    ops = []
    for index, source, target in zip(indices, sources, targets):
        if s[index:index+len(source)] == source:
            ops.append((index, source, target))
    ops.sort()
    s = list(s)
    for index, source, target in reversed(ops):
        s[index:index+len(source)] = list(target)
    return "".join(s)


print(findReplaceString(s="abcd",
                        indices=[0, 2],
                        sources=["a", "cd"],
                        targets=["eee", "ffff"]))  # "eeebffff"

print(findReplaceString(s="abcd",
                        indices=[0, 2],
                        sources=["ab", "ec"],
                        targets=["eee", "ffff"]))  # "eeecd"

print(findReplaceString(s="vmokgggqzp",
                        indices=[3, 5, 1],
                        sources=["kg", "ggq", "mo"],
                        targets=["s", "so", "bfr"]))  # "vbfrssozp"
