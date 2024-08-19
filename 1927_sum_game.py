
def get_counter_and_sum(num, low, high):
    q_counter, _sum = 0, 0
    for i in range(low, high+1):
        if num[i] == "?":
            q_counter += 1
        else:
            _sum += int(num[i])
    return q_counter, _sum


def sumGame(num):
    n = len(num)
    q_left, sum_left = get_counter_and_sum(num, 0, n//2-1)
    q_right, sum_right = get_counter_and_sum(num, n//2, n-1)
    if q_left > q_right:
        q_left, q_right = q_right, q_left
        sum_left, sum_right = sum_right, sum_left
    diff_q = q_right - q_left
    if diff_q % 2 != 0:
        return True
    if diff_q == 0:
        return sum_left != sum_right
    nines = (diff_q//2) * 9
    if sum_right + nines > sum_left:
        return True
    if sum_left - sum_right > nines:
        return True
    return False



print(sumGame("5023"))  # False (equal sums - Bob wins)
print(sumGame("25??"))  # True
print(sumGame("?3295???"))  # False
print(sumGame("?0?91172275656701?361205452?62??99?9??4478?7967373994600735??4?079246???5827572?81087461?089"))  # True
