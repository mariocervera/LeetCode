from collections import deque


def get_next_states(capacity_1, capacity_2, state):
    res = [
        (0, state[1]),
        (state[0], 0),
        (capacity_1, state[1]),
        (state[0], capacity_2),
    ]
    free_space_1 = capacity_1 - state[0]
    free_space_2 = capacity_2 - state[1]
    from_1_to_2 = min(state[0], free_space_2)
    from_2_to_1 = min(state[1], free_space_1)

    res.append((state[0] - from_1_to_2, state[1] + from_1_to_2))
    res.append((state[0] + from_2_to_1, state[1] - from_2_to_1))

    return res


def canMeasureWater(x, y, target):
    q = deque([(0, 0)])
    visited = {(0, 0)}
    while q:
        current_node = q.popleft()
        if current_node[0] == target or current_node[1] == target or current_node[0] + current_node[1] == target:
            return True
        next_states = get_next_states(x, y, current_node)
        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                q.append(next_state)
    return False


print(canMeasureWater(x=3, y=5, target=4))  # True
print(canMeasureWater(x=2, y=6, target=5))  # False
print(canMeasureWater(x=1, y=2, target=3))  # True
