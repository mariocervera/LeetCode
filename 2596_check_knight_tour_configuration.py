
def get_possible_movements(i, j, n):
    return [(i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1), (i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2)]


def checkValidGrid(grid):
    if grid[0][0] != 0:
        return False
    n = len(grid)
    tour_len = n * n
    step, current_cell = 0, (0, 0)
    for _ in range(tour_len-1):
        possible_movs = get_possible_movements(current_cell[0], current_cell[1], n)
        for mov in possible_movs:
            if 0 <= mov[0] < n and 0 <= mov[1] < n and grid[mov[0]][mov[1]] == step+1:
                current_cell = mov
                step += 1
                break
        else:
            return False
    return True


print(checkValidGrid(
    [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))  # True
print(checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]))  # False
