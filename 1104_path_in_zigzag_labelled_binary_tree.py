
from math import log2


def pathInZigZagTree(label):
    res = []
    level = int(log2(label))
    level_start = 2 ** level
    level_end = level_start * 2 - 1
    node_index = label - level_start if level % 2 == 0 else level_end - label
    while level > 0:
        res.append(level_start + node_index if level % 2 == 0 else level_end - node_index)
        level_start, level_end, node_index = level_start >> 1, level_end >> 1, node_index >> 1
        level -= 1
    res.append(1)
    return res[::-1]


print(pathInZigZagTree(14))  # [1,3,4,14]
print(pathInZigZagTree(26))  # [1,2,6,10,26]
