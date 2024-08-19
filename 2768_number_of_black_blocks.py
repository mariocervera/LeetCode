
def is_valid_top_left(m, n, i, j):
    return 0 <= i < m-1 and 0 <= j < n-1


def get_black_blocks_for_top_left(i, j, coordinates_set):
    return (int((i, j) in coordinates_set) +
            int((i+1, j) in coordinates_set) +
            int((i, j+1) in coordinates_set) +
            int((i+1, j+1) in coordinates_set))


def compute_blocks(arr, m, n, i, j, coordinates_set, visited):
    if (i, j) in visited:
        return
    visited.add((i, j))
    if is_valid_top_left(m, n, i, j):
        arr[get_black_blocks_for_top_left(i, j, coordinates_set)] += 1


def countBlackBlocks(m, n, coordinates):
    res = [0] * 5
    coordinates_set = {(i, j) for [i, j] in coordinates}
    visited = set()
    for i, j in coordinates_set:
        compute_blocks(res, m, n, i, j, coordinates_set, visited)
        compute_blocks(res, m, n, i-1, j, coordinates_set, visited)
        compute_blocks(res, m, n, i, j-1, coordinates_set, visited)
        compute_blocks(res, m, n, i-1, j-1, coordinates_set, visited)
    total = sum(res)
    res[0] = ((m-1) * (n-1)) - total
    return res


print(countBlackBlocks(m=3, n=3, coordinates=[[0, 0]]))  # [3,1,0,0,0]
print(countBlackBlocks(m=3, n=3, coordinates=[[0, 0], [1, 1], [0, 2]]))  # [0,2,2,0,0]
