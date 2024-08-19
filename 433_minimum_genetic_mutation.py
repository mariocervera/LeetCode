from collections import deque

def is_candidate(s1, s2):
    diffs = 0
    for i in range(8):
        if s1[i] != s2[i]:
            diffs += 1
    return diffs == 1


def get_candidates(s1, bank):
    return [s for s in bank if is_candidate(s1, s)]


def minMutation(startGene, endGene, bank):
    mutations = -1
    q = deque([startGene])
    discovered, bank = set(), set(bank)
    while q:
        mutations += 1
        for _ in range(len(q)):
            gene = q.popleft()
            if gene == endGene:
                return mutations
            for candidate in get_candidates(gene, bank):
                if candidate not in discovered:
                    q.append(candidate)
                    discovered.add(candidate)
    return -1


print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 1
print(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 2
