
def largestOverlap(img1, img2):
    n = len(img1)
    set_1 = {(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1}
    set_2 = {(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1}
    max_overlap = float("-inf")
    for inc_i in range(-(n-1), n):
        for inc_j in range(-(n-1), n):
            updated_set_1 = {(i + inc_i, j + inc_j) for i, j in set_1 if 0 <= i + inc_i < n and 0 <= j + inc_j < n}
            max_overlap = max(max_overlap, len(updated_set_1 & set_2))
    return max_overlap


print(largestOverlap(img1=[[1, 1, 0],
                           [0, 1, 0],
                           [0, 1, 0]],
                     img2=[[0, 0, 0],
                           [0, 1, 1],
                           [0, 0, 1]]))  # 3

print(largestOverlap(img1=[[1]], img2=[[1]]))  # 1

print(largestOverlap(img1=[[0]], img2=[[0]]))  # 0

print(largestOverlap(img1=[[0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]],
                     img2=[[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0]]))  # 1
