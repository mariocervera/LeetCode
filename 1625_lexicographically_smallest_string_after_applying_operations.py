
from collections import deque

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i+1, j-1


def rotate(arr, k):
    n = len(arr)
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    return arr


def increase(arr, k):
    n = len(arr)
    for i in range(1, n, 2):
        arr[i] = (arr[i] + k) % 10
    return arr


def findLexSmallestString(s, a, b):
    source = [int(c) for c in s]
    discovered = {tuple(source)}
    q = deque([source])
    best = source
    while q:
        current = q.popleft()
        current_increased = increase(current.copy(), a)
        if tuple(current_increased) not in discovered:
            discovered.add(tuple(current_increased))
            q.append(current_increased)
            best = min(best, current_increased)
        current_rotated = rotate(current.copy(), b)
        if tuple(current_rotated) not in discovered:
            discovered.add(tuple(current_rotated))
            q.append(current_rotated)
            best = min(best, current_rotated)
    return "".join([str(d) for d in best])



print(findLexSmallestString(s="5525", a=9, b=2))  # "2050"
print(findLexSmallestString(s="74", a=5, b=1))  # "24"
print(findLexSmallestString(s="0011", a=4, b=2))  # "0011"
